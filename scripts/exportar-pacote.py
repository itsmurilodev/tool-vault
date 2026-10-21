#!/usr/bin/env python3
"""Empacota skills e notas de tecnologia para um agente avaliar em outro projeto.

Uso:
    ./scripts/exportar-pacote.py    # gera dist/pacote-agentes/ e dist/pacote-agentes.zip

O pacote é gerado, não versionado (dist/ está no .gitignore). Rode de novo
sempre que uma skill ou nota mudar.
"""

import importlib.util
import os
import shutil
import sys
from glob import glob

NOME_PACOTE = "pacote-agentes"
DIRETORIO_SAIDA = "dist"
DIRETORIO_SKILLS = "murilo/ia/agentes/skills"

# Notas de tecnologia exportadas. Caminho relativo a murilo/ é preservado dentro
# de tecnologias/, para que links relativos entre elas continuem funcionando.
FONTES_TECNOLOGIAS = [
    "murilo/engenharia/**/*.md",
    "murilo/ia/conceitos/*.md",
    "murilo/ia/agentes/conectores.md",
    "murilo/ia/geracao-de-ui-por-ia.md",
]

NOTA_CRITERIO = "engenharia/adocao-de-ferramenta.md"

LEIA_ME = """# Pacote de skills e tecnologias — tool-vault

Este pacote é um **catálogo para avaliação**, não uma instalação. Ele foi exportado
do vault pessoal do Murilo e contém skills de agente e notas sobre tecnologias já
estudadas. Nada aqui deve ser adotado só por estar no pacote.

## Sua tarefa (agente que está lendo isto)

1. **Entenda o projeto antes do pacote.** Leia o `CLAUDE.md`/`AGENTS.md` do projeto,
   o manifesto de dependências (`package.json`, `pyproject.toml`, etc.), a estrutura
   de pastas e o estágio do produto (protótipo, com usuário pagante, em escala).
2. **Leia o critério de adoção** em `tecnologias/{criterio}` — ele define o portão
   que cada item precisa passar (estágio do produto, custo de setup e manutenção,
   redundância com o que já existe).
3. **Percorra o `CATALOGO.md`.** Para cada item, leia o arquivo só se o resumo
   indicar relação com o projeto. Não carregue tudo no contexto.
4. **Classifique cada item** em uma das três categorias abaixo, sempre com
   evidência do projeto (arquivo, dependência ou trecho que justifica).

## Formato da resposta

```markdown
## Adotar agora
| Item | Tipo | Evidência no projeto | Custo/risco |

## Avaliar depois (com gatilho)
| Item | Tipo | Gatilho que faria valer a pena |

## Não se aplica
| Item | Motivo em uma linha |
```

Agrupe em "Não se aplica" tudo que for claramente fora do escopo, sem justificar
item por item além de uma linha.

## Restrições

- **Não instale, copie ou configure nada** sem aprovação explícita do usuário.
  A saída desta tarefa é a recomendação, não a mudança.
- Aponte quando dois itens forem **concorrentes** (resolvem o mesmo problema) —
  recomende um, não os dois.
- Aponte quando o projeto **já tem** algo equivalente; redundância é motivo de recusa.
- Se faltar informação para decidir, diga qual informação falta em vez de chutar.

## Como instalar uma skill aprovada

Copie a pasta `skills/<nome>/` para o diretório de skills do agente do projeto
(por exemplo `.claude/skills/<nome>/`). A pasta precisa conter o `SKILL.md`.
"""


def carregar_gerar_indices():
    """Reaproveita o leitor de frontmatter de gerar-indices.py (nome com hífen)."""
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gerar-indices.py")
    spec = importlib.util.spec_from_file_location("gerar_indices", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def ler_skill(caminho_skill_md):
    """Lê name/description do frontmatter de um SKILL.md."""
    texto = open(caminho_skill_md, encoding="utf-8").read()
    partes = texto.split("---\n", 2)
    if len(partes) < 3:
        return None
    dados = {}
    chave_atual = None
    for linha in partes[1].splitlines():
        if linha and not linha.startswith(" ") and ":" in linha:
            chave_atual, valor = linha.split(":", 1)
            dados[chave_atual] = valor.strip().lstrip(">|").strip()
        elif chave_atual:
            dados[chave_atual] = f"{dados[chave_atual]} {linha.strip()}".strip()
    return dados


def resumir(texto, limite=220):
    texto = " ".join(texto.split())
    return texto if len(texto) <= limite else texto[: limite - 1].rstrip() + "…"


def exportar_skills(destino):
    linhas = []
    for pasta in sorted(glob(f"{DIRETORIO_SKILLS}/*/")):
        nome = os.path.basename(pasta.rstrip("/"))
        caminho_skill_md = os.path.join(pasta, "SKILL.md")
        if not os.path.isfile(caminho_skill_md):
            print(f"  !! {nome}: sem SKILL.md, pulando")
            continue
        shutil.copytree(pasta, os.path.join(destino, nome), ignore=shutil.ignore_patterns(".DS_Store"))
        dados = ler_skill(caminho_skill_md) or {}
        descricao = resumir(dados.get("description", ""))
        linhas.append(f"| `{nome}` | {descricao} | [SKILL.md](skills/{nome}/SKILL.md) |")
    return linhas


def listar_notas_tecnologia():
    caminhos = set()
    for padrao in FONTES_TECNOLOGIAS:
        for caminho in glob(padrao, recursive=True):
            caminho = caminho.replace(os.sep, "/")
            if os.path.basename(caminho) != "README.md":
                caminhos.add(caminho)
    return sorted(caminhos)


def exportar_tecnologias(destino, ler_frontmatter):
    grupos = {}
    for caminho in listar_notas_tecnologia():
        relativo = os.path.relpath(caminho, "murilo").replace(os.sep, "/")
        alvo = os.path.join(destino, relativo)
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        shutil.copy2(caminho, alvo)

        dados = ler_frontmatter(caminho) or {}
        titulo = dados.get("titulo") or os.path.basename(caminho)
        categoria = os.path.dirname(relativo)
        linha = f"| {titulo} | {resumir(dados.get('resumo', ''))} | [{relativo}](tecnologias/{relativo}) |"
        grupos.setdefault(categoria, []).append(linha)
    return grupos


def montar_catalogo(linhas_skills, grupos_tecnologias):
    total_notas = sum(len(v) for v in grupos_tecnologias.values())
    blocos = [
        "# Catálogo",
        "",
        f"{len(linhas_skills)} skills · {total_notas} notas de tecnologia. "
        "Leia o `LEIA-ME.md` antes de avaliar.",
        "",
        "## Skills",
        "",
        "| Skill | Quando dispara | Arquivo |",
        "| --- | --- | --- |",
        *linhas_skills,
        "",
        "## Tecnologias",
    ]
    for categoria in sorted(grupos_tecnologias):
        blocos += [
            "",
            f"### {categoria}",
            "",
            "| Nota | Resumo | Arquivo |",
            "| --- | --- | --- |",
            *grupos_tecnologias[categoria],
        ]
    return "\n".join(blocos) + "\n"


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(raiz)

    destino = os.path.join(DIRETORIO_SAIDA, NOME_PACOTE)
    if os.path.exists(destino):
        shutil.rmtree(destino)
    os.makedirs(destino)

    ler_frontmatter = carregar_gerar_indices().ler_frontmatter
    linhas_skills = exportar_skills(os.path.join(destino, "skills"))
    grupos_tecnologias = exportar_tecnologias(os.path.join(destino, "tecnologias"), ler_frontmatter)

    if not os.path.isfile(os.path.join(destino, "tecnologias", NOTA_CRITERIO)):
        print(f"erro: nota de critério {NOTA_CRITERIO} não foi exportada", file=sys.stderr)
        return 1

    with open(os.path.join(destino, "LEIA-ME.md"), "w", encoding="utf-8") as arquivo:
        arquivo.write(LEIA_ME.format(criterio=NOTA_CRITERIO))
    with open(os.path.join(destino, "CATALOGO.md"), "w", encoding="utf-8") as arquivo:
        arquivo.write(montar_catalogo(linhas_skills, grupos_tecnologias))

    arquivo_zip = shutil.make_archive(destino, "zip", DIRETORIO_SAIDA, NOME_PACOTE)

    total_notas = sum(len(v) for v in grupos_tecnologias.values())
    print(f"{len(linhas_skills)} skills · {total_notas} notas de tecnologia")
    print(f"pasta: {destino}/")
    print(f"zip:   {os.path.relpath(arquivo_zip)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
