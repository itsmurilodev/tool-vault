# 🧰 tool-vault

> Vault pessoal de conhecimento técnico. Duas coisas vivem aqui: **conhecimento** (o que eu estudei e quero reencontrar depois) e **artefatos** (o que uma IA executa — skills, personas, regras).

Toda nota é Markdown, navegável no Obsidian e versionada no Git.

---

## Como este vault é organizado

O primeiro nível é **domínio** (o assunto). O segundo nível separa conhecimento de artefato.

```text
tool-vault/
├── CONVENCOES.md        # como adicionar conhecimento aqui (leia antes de criar nota)
├── templates/           # modelos para notas novas
├── scripts/             # automações do vault
│
├── ia/                  # inteligência artificial e agentes
│   ├── conceitos/       #   conhecimento: estudos e teoria
│   ├── skills/          #   artefato: skills executáveis (espelha ~/.claude/skills)
│   ├── personas/        #   artefato: perfis de comportamento de agente
│   └── regras/          #   artefato: regras globais e de workspace
│
├── engenharia/          # engenharia de software (código, arquitetura, testes)
├── infra/               # infraestrutura, cloud, containers, redes, CI/CD
└── ferramentas/         # ferramentas do dia a dia (git/github, editor, CLI)
```

Cada domínio tem um `README.md` que serve de índice — é lá que se registra nota nova.

---

## Índice

### 🤖 IA

- **Conceitos** — [Prompt Engineering](ia/conceitos/prompt-engineering.md)
- **Skills** — [clean-code](ia/skills/clean-code/SKILL.md) · [decisao-arquitetural](ia/skills/decisao-arquitetural/SKILL.md) · [grill-me](ia/skills/grill-me/SKILL.md) · [heuristicas-nielsen](ia/skills/heuristicas-nielsen/SKILL.md) · [levantamento-requisitos](ia/skills/levantamento-requisitos/SKILL.md) · [prompt-engineering-agente](ia/skills/prompt-engineering-agente/SKILL.md)
- **Personas** — [Conselheiro Estratégico](ia/personas/conselheiro-estrategico.md) · [Engenheiro de Prompts](ia/personas/engenheiro-de-prompts.md)
- **Regras** — [Global Rules](ia/regras/global-rules.md) · [Workspace Rules](ia/regras/workspace-rules.md)

→ [Índice completo do domínio](ia/README.md)

### 🏗️ Engenharia

- [Clean Code](engenharia/clean-code.md)

→ [Índice completo do domínio](engenharia/README.md)

### 🖥️ Infra

Domínio ainda vazio. → [O que entra aqui](infra/README.md)

### 🔧 Ferramentas

- [Padrão de nomes de repositórios GitHub](ferramentas/github/padrao-de-repositorios.md)

→ [Índice completo do domínio](ferramentas/README.md)

---

## Usando as skills

As skills em `ia/skills/` seguem o formato de skill do Claude (pasta com `SKILL.md` + frontmatter `name`/`description`). Para instalá-las localmente:

```bash
./scripts/sync-skills.sh          # mostra o que faria
./scripts/sync-skills.sh --apply  # cria os links em ~/.claude/skills/
```

O script usa symlink: editar a skill aqui já reflete no Claude, sem precisar sincronizar de novo.

---

## Antes de adicionar conhecimento

Leia [CONVENCOES.md](CONVENCOES.md). Em resumo:

1. Nome de arquivo em `kebab-case`, descritivo e único no vault (`clean-code.md`, nunca `estudo.md`).
2. Toda nota de conhecimento começa com frontmatter YAML (`tipo`, `dominio`, `tags`, `status`, `atualizado`).
3. `SKILL.md` **não** leva esse frontmatter — o formato dele é o do Claude e quebra se alterado.
4. Conhecimento fica no domínio, não em `ia/` só porque foi estudado com IA.
5. Registrou a nota? Adicione o link no `README.md` do domínio.

Para conferir se está tudo dentro do padrão:

```bash
./scripts/validar-vault.py
```

Ele checa link quebrado, wikilink ambíguo, nome de arquivo duplicado, frontmatter faltando e skill mal formada.
