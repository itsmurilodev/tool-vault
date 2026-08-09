#!/usr/bin/env python3
"""Verifica se o vault segue as convenções de CONVENCOES.md.

Uso:
    ./scripts/validar-vault.py

Sai com código 1 quando encontra problema, para poder virar hook de pre-commit
ou passo de CI depois. PyYAML é opcional: sem ele, a checagem de frontmatter
cai para uma validação mais simples, baseada em texto.
"""

import os
import re
import sys
from glob import glob

try:
    import yaml
except ImportError:
    yaml = None

CAMPOS_OBRIGATORIOS = {"titulo", "tipo", "dominio", "tags", "status", "atualizado"}
TIPOS_VALIDOS = {"conceito", "referencia", "persona", "regra", "decisao"}
DOMINIOS_VALIDOS = {"ia", "engenharia", "infra", "ferramentas"}
STATUS_VALIDOS = {"rascunho", "ativo", "arquivado"}

# Documentação e modelos usam wikilinks e frontmatter como exemplo, não como link real.
ARQUIVOS_META = {"README.md", "CONVENCOES.md"}
PREFIXOS_IGNORADOS = (".obsidian/", "templates/")


def listar_notas():
    caminhos = sorted(glob("**/*.md", recursive=True))
    return [c for c in caminhos if not c.startswith(PREFIXOS_IGNORADOS)]


def remover_blocos_de_codigo(texto):
    sem_cercas = re.sub(r"```.*?```", "", texto, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", sem_cercas)


def ler_frontmatter(texto):
    """Devolve (dados, erro). dados é None quando não há frontmatter."""
    if not texto.startswith("---\n"):
        return None, None
    partes = texto.split("---\n", 2)
    if len(partes) < 3:
        return None, "frontmatter aberto e não fechado"
    bloco = partes[1]
    if yaml is None:
        campos = set(re.findall(r"^([a-z_]+):", bloco, flags=re.MULTILINE))
        return {campo: "" for campo in campos}, None
    try:
        return yaml.safe_load(bloco) or {}, None
    except yaml.YAMLError as erro:
        return None, f"YAML inválido: {erro}"


def validar_nomes_unicos(notas, problemas):
    por_nome = {}
    for caminho in notas:
        nome = os.path.splitext(os.path.basename(caminho))[0]
        por_nome.setdefault(nome, []).append(caminho)

    for nome, caminhos in sorted(por_nome.items()):
        if len(caminhos) > 1 and nome not in ("README", "SKILL"):
            problemas.append(
                f"nome duplicado no vault: '{nome}' em {caminhos} — wikilink fica ambíguo"
            )
    return por_nome


def validar_links(notas, por_nome, problemas):
    for caminho in notas:
        texto = remover_blocos_de_codigo(open(caminho, encoding="utf-8").read())

        for alvo in re.findall(r"\[[^\]]*\]\(([^)#]+?\.md)\)", texto):
            if alvo.startswith(("http://", "https://")):
                continue
            destino = os.path.normpath(os.path.join(os.path.dirname(caminho), alvo))
            if not os.path.exists(destino):
                problemas.append(f"{caminho}: link quebrado -> {alvo}")

        if os.path.basename(caminho) in ARQUIVOS_META:
            continue
        for alvo in re.findall(r"\[\[([^\]|]+)", texto):
            nome = alvo.split("/")[-1].strip()
            if nome not in por_nome:
                problemas.append(f"{caminho}: wikilink sem destino -> [[{alvo}]]")
            elif len(por_nome[nome]) > 1:
                problemas.append(f"{caminho}: wikilink ambíguo -> [[{alvo}]]")


def validar_frontmatter_das_notas(notas, problemas):
    for caminho in notas:
        base = os.path.basename(caminho)
        if base in ARQUIVOS_META or base == "SKILL.md" or "/references/" in caminho:
            continue

        dados, erro = ler_frontmatter(open(caminho, encoding="utf-8").read())
        if erro:
            problemas.append(f"{caminho}: {erro}")
            continue
        if dados is None:
            problemas.append(f"{caminho}: sem frontmatter (veja CONVENCOES.md seção 4)")
            continue

        faltando = CAMPOS_OBRIGATORIOS - set(dados)
        if faltando:
            problemas.append(f"{caminho}: frontmatter sem {sorted(faltando)}")
        if yaml is None:
            continue
        for campo, validos in (
            ("tipo", TIPOS_VALIDOS),
            ("dominio", DOMINIOS_VALIDOS),
            ("status", STATUS_VALIDOS),
        ):
            valor = dados.get(campo)
            if valor is not None and valor not in validos:
                problemas.append(
                    f"{caminho}: {campo}='{valor}' fora dos valores aceitos {sorted(validos)}"
                )


def validar_skills(problemas):
    for caminho in sorted(glob("ia/skills/*/SKILL.md")):
        pasta = caminho.split(os.sep)[2]
        dados, erro = ler_frontmatter(open(caminho, encoding="utf-8").read())
        if erro:
            problemas.append(f"{caminho}: {erro}")
            continue
        if dados is None:
            problemas.append(f"{caminho}: SKILL.md sem frontmatter name/description")
            continue
        if yaml is None:
            continue
        if dados.get("name") != pasta:
            problemas.append(
                f"{caminho}: name='{dados.get('name')}' diferente da pasta '{pasta}'"
            )
        if not dados.get("description"):
            problemas.append(f"{caminho}: sem description — a skill nunca vai disparar")
        extras = set(dados) - {"name", "description"}
        if extras:
            problemas.append(
                f"{caminho}: campos extras no frontmatter {sorted(extras)} — "
                "SKILL.md aceita só name e description"
            )

    for pasta in sorted(glob("ia/skills/*/")):
        if not os.path.isfile(os.path.join(pasta, "SKILL.md")):
            problemas.append(f"{pasta}: pasta de skill sem SKILL.md")


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(raiz)

    notas = listar_notas()
    problemas = []

    por_nome = validar_nomes_unicos(notas, problemas)
    validar_links(notas, por_nome, problemas)
    validar_frontmatter_das_notas(notas, problemas)
    validar_skills(problemas)

    print(f"{len(notas)} notas verificadas em {raiz}")
    if yaml is None:
        print("aviso: PyYAML não instalado — checagem de frontmatter reduzida "
              "(pip install pyyaml para a completa)")

    if problemas:
        print(f"\n{len(problemas)} problema(s):\n")
        for problema in problemas:
            print(f"  - {problema}")
        return 1

    print("tudo certo — vault dentro das convenções")
    return 0


if __name__ == "__main__":
    sys.exit(main())
