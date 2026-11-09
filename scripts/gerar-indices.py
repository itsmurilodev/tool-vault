#!/usr/bin/env python3
"""Regenera as seções de índice dos README a partir do frontmatter das notas.

Uso:
    ./scripts/gerar-indices.py            # reescreve os índices
    ./scripts/gerar-indices.py --check    # só verifica; sai com 1 se algo mudaria

O índice fica entre marcadores HTML. Tudo fora deles (prosa, backlog, tabelas
curadas) é preservado — o script só substitui o miolo.
"""

import os
import re
import sys
from glob import glob

try:
    import yaml
except ImportError:
    yaml = None

INICIO = "<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->"
FIM = "<!-- FIM:INDICE -->"

# (README a atualizar, diretório cujas notas ele indexa)
INDICES = [
    ("radar/README.md", "radar"),
    ("empresa/README.md", "empresa"),
    ("empresa/negocio/README.md", "empresa/negocio"),
    ("agentes/README.md", "agentes"),
    ("conhecimento/README.md", "conhecimento"),
    ("conhecimento/ia/README.md", "conhecimento/ia"),
    ("conhecimento/engenharia/README.md", "conhecimento/engenharia"),
    ("conhecimento/engenharia/infra/README.md", "conhecimento/engenharia/infra"),
    ("conhecimento/engenharia/ferramentas/README.md", "conhecimento/engenharia/ferramentas"),
]

# Radar: cada tecnologia tem a própria pasta, mas o índice agrupa por categoria
# (radar/<categoria>/), para não virar um título por tecnologia.
PASTA_RADAR = "radar"
CATALOGO_RADAR = "radar/catalogo-do-radar.md"

# Tabela de skills do agentes/README.md, montada do frontmatter de cada SKILL.md.
PASTA_SKILLS = "agentes/skills"
README_SKILLS = "agentes/README.md"
INICIO_SKILLS = "<!-- INICIO:SKILLS (gerado por scripts/gerar-indices.py — não editar à mão) -->"
FIM_SKILLS = "<!-- FIM:SKILLS -->"
ANEIS_RADAR = [
    ("adotar", "✅ Adotar — usar já"),
    ("testar", "🧪 Testar — experimentar em um projeto antes de padronizar"),
    ("avaliar", "⏳ Avaliar — só quando o gatilho aparecer"),
    ("evitar", "⛔ Evitar — não usar agora"),
]

DOMINIOS_RAIZ = [
    ("radar", "📡 Radar — ferramentas e tendências analisadas"),
    ("empresa", "🏢 Empresa — Async Studio (marca, produtos, negócio)"),
    ("agentes", "🤖 Agentes — skills, regras e personas"),
    ("conhecimento", "📚 Conhecimento — estudos, engenharia e IA"),
]

# Rótulo legível para subpastas
ROTULOS = {
    "github": "GitHub",
    "ia": "IA & Agentes",
    "adr": "Decisões (ADR)",
    "agentes": "Agentes",
    "perfil": "Perfil & Modus Operandi",
    "estudos": "Estudos & Faculdade",
    "engenharia": "Engenharia",
    "infra": "Infraestrutura",
    "ferramentas": "Ferramentas",
    "marca": "Marca & Identidade",
    "personas": "Personas",
    "regras": "Regras",
    "conceitos": "Conceitos",
    "design-system": "Design System & UI",
    "produtos": "Produtos & ADRs",
    "negocio": "Negócio & Marketing",
    "radar": "Radar de tecnologias",
    "verificacao-e-qualidade": "Verificação & Qualidade",
    "fluxo-com-agentes": "Fluxo com agentes",
    "plataformas-de-agentes": "Plataformas de agentes",
    "performance-web": "Performance web",
    "produto-e-atendimento": "Produto & Atendimento",
    "produtividade": "Produtividade",
    "marketing-e-conteudo": "Marketing & Conteúdo",
    "ferramentas-de-agentes": "Ferramentas de agentes",
    "seguranca": "Segurança",
    "infraestrutura": "Infraestrutura",
}

IGNORADOS = ("modelos/", ".obsidian/", "scripts/")


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
    bloco = partes[1]
    if yaml is not None:
        try:
            return yaml.safe_load(bloco) or {}
        except yaml.YAMLError:
            return None

    dados = {}
    for linha in bloco.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", linha)
        if m:
            chave = m.group(1)
            valor = m.group(2).strip().strip('"').strip("'")
            dados[chave] = valor
    return dados


def listar_notas(diretorio, ignoradas=None):
    """Notas de conhecimento sob `diretorio`, agrupadas por subpasta."""
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

        grupos.setdefault(chave_do_grupo(caminho, diretorio), []).append((caminho, dados))
    return grupos


def chave_do_grupo(caminho, diretorio):
    pasta = os.path.dirname(caminho)
    if pasta.startswith(PASTA_RADAR + "/"):
        categoria = pasta[len(PASTA_RADAR) + 1:].split("/")[0]
        pasta = f"{PASTA_RADAR}/{categoria}"
    subpasta = os.path.relpath(pasta, diretorio).replace(os.sep, "/")
    return "" if subpasta == "." else subpasta


def celula(valor):
    texto = " ".join(str(valor or "—").split())
    return texto.replace("|", "\\|")


def montar_catalogo_radar():
    """Tabela de decisão do radar, montada do frontmatter das fichas (campo `radar`)."""
    fichas = []
    for caminho in sorted(glob(f"{PASTA_RADAR}/**/*.md", recursive=True)):
        caminho = caminho.replace(os.sep, "/")
        dados = ler_frontmatter(caminho)
        if dados and dados.get("radar"):
            fichas.append((caminho, dados))
    if not fichas:
        return "_Nenhuma ficha no radar ainda._"

    base = os.path.dirname(CATALOGO_RADAR)
    blocos = []
    for anel, titulo_anel in ANEIS_RADAR:
        itens = [(c, d) for c, d in fichas if d.get("radar") == anel]
        itens.sort(key=lambda item: (item[1].get("categoria", ""), item[1]["titulo"].lower()))
        blocos.append(f"### {titulo_anel} ({len(itens)})\n")
        if not itens:
            blocos.append("_Nenhum item._\n")
            continue
        blocos.append("| Item | Categoria | Natureza | Quando usar | Quando não usar | Pré-requisito |")
        blocos.append("| --- | --- | --- | --- | --- | --- |")
        for caminho, dados in itens:
            nome = dados["titulo"].split(" — ")[0]
            destino = os.path.relpath(caminho, base).replace(os.sep, "/")
            categoria = rotulo(dados.get("categoria", ""))
            blocos.append(
                f"| [{celula(nome)}]({destino}) | {celula(categoria)} | {celula(dados.get('natureza'))} "
                f"| {celula(dados.get('quando_usar'))} | {celula(dados.get('quando_nao_usar'))} "
                f"| {celula(dados.get('pre_requisito'))} |"
            )
        blocos.append("")
    return "\n".join(blocos).strip()


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
        return "_Ainda sem notas neste domínio._"

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


def ler_descricao_skill(caminho):
    """`description` do SKILL.md, inclusive em bloco dobrado (`>`), com ou sem PyYAML."""
    partes = open(caminho, encoding="utf-8").read().split("---\n", 2)
    if len(partes) < 3:
        return ""
    descricao, dentro = [], False
    for linha in partes[1].splitlines():
        if linha.startswith("description:"):
            dentro = True
            descricao.append(linha.split(":", 1)[1].strip().lstrip(">|").strip())
        elif dentro and linha.startswith((" ", "\t")):
            descricao.append(linha.strip())
        elif dentro:
            break
    return " ".join(" ".join(descricao).split()).strip('"')


def montar_tabela_skills():
    """Tabela das skills de agentes/skills/, lida do frontmatter de cada SKILL.md."""
    linhas = ["| Skill | Quando dispara |", "| --- | --- |"]
    for caminho in sorted(glob(f"{PASTA_SKILLS}/*/SKILL.md")):
        caminho = caminho.replace(os.sep, "/")
        nome = caminho.split("/")[-2]
        descricao = ler_descricao_skill(caminho)
        if len(descricao) > 180:
            descricao = descricao[:179].rstrip() + "…"
        destino = os.path.relpath(caminho, os.path.dirname(README_SKILLS)).replace(os.sep, "/")
        linhas.append(f"| [{nome}]({destino}) | {celula(descricao)} |")
    return "\n".join(linhas)


def aplicar(caminho_readme, conteudo, inicio=INICIO, fim=FIM):
    """Substitui o miolo entre marcadores. Devolve (mudou, erro)."""
    if not os.path.isfile(caminho_readme):
        return False, f"{caminho_readme}: arquivo não encontrado"
    original = open(caminho_readme, encoding="utf-8").read()
    if inicio not in original or fim not in original:
        return False, f"{caminho_readme}: sem os marcadores {inicio} / {fim}"

    novo = re.sub(
        re.escape(inicio) + r".*?" + re.escape(fim),
        lambda _match: f"{inicio}\n\n{conteudo}\n\n{fim}",
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
    alvos = []
    for caminho, diretorio in INDICES:
        if os.path.exists(caminho):
            alvos.append((caminho, montar_indice(diretorio, caminho, ignoradas)))
    alvos.append(("README.md", montar_indice_raiz(ignoradas)))
    if os.path.exists(CATALOGO_RADAR):
        alvos.append((CATALOGO_RADAR, montar_catalogo_radar()))
    alvos = [(caminho, conteudo, INICIO, FIM) for caminho, conteudo in alvos]
    if os.path.exists(README_SKILLS):
        alvos.append((README_SKILLS, montar_tabela_skills(), INICIO_SKILLS, FIM_SKILLS))

    desatualizados, erros = [], []
    for caminho_readme, conteudo, inicio, fim in alvos:
        resultado, erro = aplicar(caminho_readme, conteudo, inicio, fim)
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
