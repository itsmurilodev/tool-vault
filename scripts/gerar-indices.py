#!/usr/bin/env python3
"""Regenera as seções de índice dos README a partir do frontmatter das notas.

Uso:
    ./scripts/gerar-indices.py            # reescreve os índices
    ./scripts/gerar-indices.py --check    # só verifica; sai com 1 se algo mudaria

O índice fica entre marcadores HTML. Tudo fora deles (prosa, backlog, tabelas
curadas) é preservado — o script só substitui o miolo.

Existe para eliminar o modo de falha "adicionei nota e esqueci de registrar no
índice", que é como um vault deixa de ser navegável.
"""

import os
import re
import sys
from glob import glob

try:
    import yaml
except ImportError:
    print("erro: este script precisa de PyYAML (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

INICIO = "<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->"
FIM = "<!-- FIM:INDICE -->"

# (README a atualizar, diretório cujas notas ele indexa)
INDICES = [
    ("ia/README.md", "ia"),
    ("engenharia/README.md", "engenharia"),
    ("infra/README.md", "infra"),
    ("ferramentas/README.md", "ferramentas"),
    ("negocio/README.md", "negocio"),
    ("ia/agentes/claude/README.md", "ia/agentes/claude"),
]

DOMINIOS_RAIZ = [
    ("ia", "🤖 IA"),
    ("engenharia", "🏗️ Engenharia"),
    ("infra", "🖥️ Infra"),
    ("ferramentas", "🔧 Ferramentas"),
    ("negocio", "💼 Negócio"),
]

# Rótulo legível para subpastas cujo nome não fica bom só capitalizado.
ROTULOS = {
    "github": "GitHub",
    "ia": "IA",
    "adr": "Decisões (ADR)",
    "agentes/claude": "Agentes › Claude",
    "agentes": "Agentes",
}

IGNORADOS = ("templates/", ".obsidian/")


def rotulo(caminho_relativo):
    if caminho_relativo in ROTULOS:
        return ROTULOS[caminho_relativo]
    partes = [ROTULOS.get(p, p.replace("-", " ").capitalize()) for p in caminho_relativo.split("/")]
    return " › ".join(partes)


def ler_frontmatter(caminho):
    texto = open(caminho, encoding="utf-8").read()
    if not texto.startswith("---\n"):
        return None
    partes = texto.split("---\n", 2)
    if len(partes) < 3:
        return None
    try:
        return yaml.safe_load(partes[1]) or {}
    except yaml.YAMLError:
        return None


def listar_notas(diretorio, ignoradas=None):
    """Notas de conhecimento sob `diretorio`, agrupadas por subpasta.

    Nota sem frontmatter válido é registrada em `ignoradas` em vez de sumir em
    silêncio — índice que perde nota sem avisar é pior do que índice manual.
    """
    grupos = {}
    for caminho in sorted(glob(f"{diretorio}/**/*.md", recursive=True)):
        caminho = caminho.replace(os.sep, "/")
        base = os.path.basename(caminho)
        if base in ("README.md", "SKILL.md") or "/references/" in caminho:
            continue
        if caminho.startswith(IGNORADOS):
            continue
        dados = ler_frontmatter(caminho)
        if not dados or not dados.get("titulo"):
            if ignoradas is not None:
                ignoradas.add(caminho)
            continue

        subpasta = os.path.relpath(os.path.dirname(caminho), diretorio).replace(os.sep, "/")
        chave = "" if subpasta == "." else subpasta
        grupos.setdefault(chave, []).append((caminho, dados))
    return grupos


def linha_da_nota(caminho, dados, base_do_readme):
    destino = os.path.relpath(caminho, base_do_readme).replace(os.sep, "/")
    titulo = dados["titulo"]
    linha = f"- [{titulo}]({destino})"
    if dados.get("resumo"):
        linha += f" — {dados['resumo']}"
    if dados.get("status") == "rascunho":
        linha += " *(rascunho)*"
    return linha


def montar_indice(diretorio, caminho_readme, ignoradas=None):
    base = os.path.dirname(caminho_readme)
    grupos = listar_notas(diretorio, ignoradas)
    if not grupos:
        return "_Ainda sem notas neste domínio. Crie a primeira com `./scripts/nova-nota.sh`._"

    blocos = []
    for chave in sorted(grupos, key=lambda k: (k != "", k)):
        notas = sorted(grupos[chave], key=lambda item: item[1]["titulo"].lower())
        if chave:
            blocos.append(f"### {rotulo(chave)}\n")
        blocos.append("\n".join(linha_da_nota(c, d, base) for c, d in notas))
        blocos.append("")
    return "\n".join(blocos).strip()


def montar_indice_raiz(ignoradas=None):
    blocos = []
    for diretorio, titulo in DOMINIOS_RAIZ:
        grupos = listar_notas(diretorio, ignoradas)
        total = sum(len(v) for v in grupos.values())
        blocos.append(f"### {titulo} → [índice do domínio]({diretorio}/README.md)\n")
        if not total:
            blocos.append("_Domínio ainda vazio._\n")
            continue
        todas = [item for lista in grupos.values() for item in lista]
        todas.sort(key=lambda item: item[1]["titulo"].lower())
        blocos.append("\n".join(linha_da_nota(c, d, ".") for c, d in todas))
        blocos.append("")
    return "\n".join(blocos).strip()


def aplicar(caminho_readme, conteudo):
    """Substitui o miolo entre marcadores. Devolve (mudou, erro)."""
    if not os.path.isfile(caminho_readme):
        return False, f"{caminho_readme}: arquivo não encontrado"
    original = open(caminho_readme, encoding="utf-8").read()
    if INICIO not in original or FIM not in original:
        return False, f"{caminho_readme}: sem os marcadores INICIO:INDICE / FIM:INDICE"

    novo = re.sub(
        re.escape(INICIO) + r".*?" + re.escape(FIM),
        lambda _match: f"{INICIO}\n\n{conteudo}\n\n{FIM}",
        original,
        flags=re.DOTALL,
    )
    if novo == original:
        return False, None
    return novo, None


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(raiz)
    somente_checar = "--check" in sys.argv

    ignoradas = set()
    alvos = [
        (caminho, montar_indice(diretorio, caminho, ignoradas))
        for caminho, diretorio in INDICES
    ]
    alvos.append(("README.md", montar_indice_raiz(ignoradas)))

    desatualizados, erros = [], []
    for caminho_readme, conteudo in alvos:
        resultado, erro = aplicar(caminho_readme, conteudo)
        if erro:
            erros.append(erro)
            continue
        if resultado is False:
            continue
        desatualizados.append(caminho_readme)
        if not somente_checar:
            open(caminho_readme, "w", encoding="utf-8").write(resultado)

    for erro in erros:
        print(f"  - {erro}")

    if ignoradas:
        print("\nnotas fora do índice por frontmatter inválido ou sem titulo:")
        for caminho in sorted(ignoradas):
            print(f"  - {caminho}")
        print("rode ./scripts/validar-vault.py para o diagnóstico completo.")

    if erros or ignoradas:
        return 2
    if not desatualizados:
        print(f"{len(alvos)} índices já atualizados")
        return 0
    if somente_checar:
        print(f"\n{len(desatualizados)} índice(s) desatualizado(s):")
        for caminho in desatualizados:
            print(f"  - {caminho}")
        print("\nRode ./scripts/gerar-indices.py para atualizar.")
        return 1
    print(f"{len(desatualizados)} índice(s) atualizado(s):")
    for caminho in desatualizados:
        print(f"  - {caminho}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
