# 👤 Murilo — Conhecimento Pessoal & Engenharia

> Hub central de conhecimento pessoal: princípios de trabalho, estudos acadêmicos/cursos, boas práticas de engenharia de software e artefatos de inteligência artificial.

---

## 🗂️ Estrutura deste Pilar

* **`perfil/`**: Modus operandi, diretrizes de código e postura esperada de agentes.
* **`estudos/`**: Anotações e disciplinas da faculdade (`faculdade/`) e cursos (`cursos/`).
* **`engenharia/`**: Clean code, qualidade de software, infraestrutura (`infra/`) e ferramentas (`ferramentas/`).
* **`ia/`**: Engenharia de prompts, personas, regras globais e skills do Claude (`agentes/claude/skills/`).

---

## 📚 Índice de Conhecimento

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

### Engenharia

- [Clean Code — estudo](engenharia/clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](engenharia/bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Portão de adoção de ferramenta](engenharia/adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](engenharia/qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.

### Engenharia › Ferramentas › GitHub

- [Fluxo Issue → PR → commit padronizado](engenharia/ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [Padrão de nomes de repositórios GitHub](engenharia/ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.

### Engenharia › Infraestrutura

- [Analytics de produto — PostHog](engenharia/infra/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](engenharia/infra/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](engenharia/infra/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](engenharia/infra/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Email transacional — Resend](engenharia/infra/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](engenharia/infra/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Supabase como backend-as-a-service — o teto real do free tier](engenharia/infra/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.

### IA & Agentes

- [Geração de UI e de app por IA — os três níveis](ia/geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.

### IA & Agentes › Agentes › Claude

- [Conectores do Claude (MCP)](ia/agentes/claude/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](ia/agentes/claude/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

### IA & Agentes › Conceitos

- [Prompt Engineering — estudo](ia/conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.

### IA & Agentes › Personas

- [Persona — Conselheiro Estratégico Direto](ia/personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](ia/personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.

### IA & Agentes › Regras

- [Global Rules — comportamento padrão de agente](ia/regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Workspace Rules — regras locais de projeto](ia/regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

### Perfil & Modus Operandi

- [Modus Operandi — Como o Murilo Trabalha](perfil/modus-operandi.md) — Diretrizes de engenharia, princípios inegociáveis e postura esperada de agentes de IA.

<!-- FIM:INDICE -->
