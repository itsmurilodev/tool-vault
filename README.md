# 🧰 tool-vault

> Vault pessoal de conhecimento técnico. Duas coisas vivem aqui: **conhecimento** (o que eu estudei e quero reencontrar depois) e **artefatos** (o que uma IA executa — skills, personas, regras).

Toda nota é Markdown, navegável no Obsidian e versionada no Git.

---

## Como este vault é organizado

O primeiro nível é **domínio** (o assunto). Dentro de `ia/`, há um segundo corte: o que é portável entre agentes vs. o que é específico de um.

```text
tool-vault/
├── CONVENCOES.md        # como adicionar conhecimento aqui (leia antes de criar nota)
├── templates/           # modelos para notas novas
├── scripts/             # validação e sync
│
├── ia/                  # inteligência artificial e agentes
│   ├── conceitos/       #   teoria — vale para qualquer LLM
│   ├── personas/        #   perfis de comportamento (portáveis)
│   ├── regras/          #   Global / Workspace Rules (portáveis)
│   └── agentes/
│       └── claude/      #   skills, conectores (MCP), configuração e hooks
│
├── engenharia/          # código, arquitetura, testes, qualidade, front-end
├── infra/               # cloud, containers, redes, CI/CD, observabilidade
└── ferramentas/         # git/github, editor, terminal, CLIs
```

Cada domínio tem um `README.md` que serve de índice e backlog — é lá que se registra nota nova.

---

## Índice

### 🤖 IA → [índice do domínio](ia/README.md)

- **Conceitos** — [Prompt Engineering](ia/conceitos/prompt-engineering.md) · [Geração de UI e de app por IA](ia/geracao-de-ui-por-ia.md)
- **Personas** — [Conselheiro Estratégico](ia/personas/conselheiro-estrategico.md) · [Engenheiro de Prompts](ia/personas/engenheiro-de-prompts.md)
- **Regras** — [Global Rules](ia/regras/global-rules.md) · [Workspace Rules](ia/regras/workspace-rules.md)
- **Claude** — [conectores (MCP)](ia/agentes/claude/conectores.md) · [configuração e hooks](ia/agentes/claude/configuracao.md) · [skills](ia/agentes/claude/README.md)

### 🏗️ Engenharia → [índice do domínio](engenharia/README.md)

- [Portão de adoção de ferramenta](engenharia/adocao-de-ferramenta.md)
- [Clean Code](engenharia/clean-code.md)
- [Qualidade automatizada](engenharia/qualidade-automatizada.md)
- [Ecossistema de UI copy-paste](engenharia/bibliotecas-de-ui.md)

### 🖥️ Infra → [índice do domínio](infra/README.md)

- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](infra/observabilidade.md)

### 🔧 Ferramentas → [índice do domínio](ferramentas/README.md)

- [Padrão de nomes de repositórios GitHub](ferramentas/github/padrao-de-repositorios.md)
- [Fluxo Issue → PR → commit padronizado](ferramentas/github/fluxo-issue-pr.md)
- [Prospecção B2B e mídia paga](ferramentas/prospeccao-e-midia-paga.md)

---

## Usando as skills

As skills em `ia/agentes/claude/skills/` seguem o formato do Claude (pasta com `SKILL.md` + frontmatter `name`/`description`). Para instalá-las localmente:

```bash
./scripts/sync-skills.sh          # mostra o que faria
./scripts/sync-skills.sh --apply  # cria os links em ~/.claude/skills/
```

O script usa symlink: editar a skill aqui já reflete no Claude, sem sincronizar de novo. Ele nunca apaga diretório real — se avisar que já existe um, veja [configuração do Claude](ia/agentes/claude/configuracao.md).

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
