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
├── ferramentas/         # git/github, editor, terminal, CLIs
└── negocio/             # marketing, vendas, prospecção, SEO/AEO, growth
```

Cada domínio tem um `README.md` que serve de índice e backlog — é lá que se registra nota nova.

---

## Índice

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

### 🤖 IA → [índice do domínio](ia/README.md)

- [Conectores do Claude (MCP)](ia/agentes/claude/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](ia/agentes/claude/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*
- [Geração de UI e de app por IA — os três níveis](ia/geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.
- [Global Rules — comportamento padrão de agente](ia/regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Persona — Conselheiro Estratégico Direto](ia/personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](ia/personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.
- [Prompt Engineering — estudo](ia/conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [Workspace Rules — regras locais de projeto](ia/regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

### 🏗️ Engenharia → [índice do domínio](engenharia/README.md)

- [Clean Code — estudo](engenharia/clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](engenharia/bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Portão de adoção de ferramenta](engenharia/adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](engenharia/qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.

### 🖥️ Infra → [índice do domínio](infra/README.md)

- [ADR 001 — Plataforma de observabilidade padrão](infra/adr-001-observabilidade.md) — Sentry no free tier, instrumentado via OpenTelemetry, como padrão para projeto novo. Proposta.
- [Analytics de produto — PostHog](infra/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](infra/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](infra/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](infra/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Email transacional — Resend](infra/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](infra/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Supabase como backend-as-a-service — o teto real do free tier](infra/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.

### 🔧 Ferramentas → [índice do domínio](ferramentas/README.md)

- [Fluxo Issue → PR → commit padronizado](ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [Padrão de nomes de repositórios GitHub](ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.

### 💼 Negócio → [índice do domínio](negocio/README.md)

- [AEO/GEO — otimizar conteúdo para ser citado por IA generativa](negocio/aeo-geo-otimizacao-para-ia.md) — AEO e GEO são o mesmo campo sem consenso de nome: estruturar conteúdo para ChatGPT, Perplexity e AI Overviews citarem como fonte. Técnica concreta, aplicável já ao SEO da Hamidi.
- [Prospecção B2B e mídia paga — quando essas ferramentas passam a valer](negocio/prospeccao-e-midia-paga.md) — Apollo.io, ZoomInfo e Windsor.ai: custo real, portão de cada uma e o que a LGPD exige.

<!-- FIM:INDICE -->

---

## Usando as skills

As skills em `ia/agentes/claude/skills/` seguem o formato do Claude (pasta com `SKILL.md` + frontmatter `name`/`description`). Para instalá-las localmente:

```bash
./scripts/sync-skills.sh          # mostra o que faria
./scripts/sync-skills.sh --apply  # cria os links em ~/.claude/skills/
```

O script usa symlink: editar a skill aqui já reflete no Claude, sem sincronizar de novo. Ele nunca apaga diretório real — se avisar que já existe um, veja [configuração do Claude](ia/agentes/claude/configuracao.md).

---

## Adicionando conhecimento

```bash
./scripts/nova-nota.sh infra docker-compose
```

Cria a nota com frontmatter e data preenchidos, valida o nome e **regenera os índices**. Depois é só escrever e preencher o `resumo` — é ele que aparece no índice.

Ative as verificações uma vez por clone:

```bash
git config core.hooksPath .githooks
```

A partir daí, todo commit checa convenções e índices. O mesmo par roda no CI.

| Script | Para quê |
| ------ | -------- |
| `./scripts/nova-nota.sh <dominio> <nome>` | Criar nota nova |
| `./scripts/gerar-indices.py` | Regenerar os índices (`--check` só verifica) |
| `./scripts/validar-vault.py` | Link quebrado, wikilink ambíguo, nome duplicado, frontmatter, skill |
| `./scripts/sync-skills.sh --apply` | Ligar as skills em `~/.claude/skills` |

As regras completas estão em [CONVENCOES.md](CONVENCOES.md). O essencial:

1. Nome de arquivo em `kebab-case`, descritivo e **único no vault** (`clean-code.md`, nunca `estudo.md`).
2. `titulo` e `resumo` **entre aspas** — um `:` solto quebra o YAML e a nota some do índice.
3. `SKILL.md` **não** leva o frontmatter de nota — o formato dele é o do Claude e quebra se alterado.
4. Conhecimento fica no domínio, não em `ia/` só porque foi estudado com IA.
5. Índice de README é **gerado**. Não edite entre os marcadores.

## Navegando no Obsidian

`vault.base` traz cinco visões sobre as mesmas notas: **Todas** (por domínio), **Rascunhos**, **Sem resumo**, **Referências** e **Decisões (ADR)**. É navegação dentro do Obsidian; o README continua sendo a porta de entrada no GitHub.
