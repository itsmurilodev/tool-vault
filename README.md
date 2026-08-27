# 🧰 tool-vault

> Segundo Cérebro e base canônica de conhecimento técnico, identidade corporativa e artefatos operacionais para agentes de IA.

Toda nota é Markdown puro, navegável no Obsidian, consumível via MCP/Agentes e versionada no Git.

---

## 🏛️ Como este vault é organizado

O repositório é estruturado em **dois grandes pilares canônicos**:

```text
tool-vault/
├── murilo/                     # PILAR 1: Pessoal, Estudos, Engenharia & IA
│   ├── perfil/                 #   Modus operandi pessoal e preferências
│   ├── estudos/                #   Faculdade (disciplinas) e cursos
│   ├── engenharia/             #   Clean code, qualidade, infra e ferramentas
│   │   ├── infra/              #     Supabase, Sentry, Redis, Resend, etc.
│   │   └── ferramentas/        #     GitHub Flow, commits, convenções
│   └── ia/                     #   Engenharia de prompts, personas, regras e skills
│       └── agentes/claude/     #     Skills locais do Claude (~/.claude/skills)
│
├── async/                      # PILAR 2: Async Studio (Marca, Produtos & Negócio)
│   ├── identidade/             #   Brandbook, paleta de cores, tom de voz
│   ├── design-system/          #   Tokens CSS, componentes base, regras de UI
│   ├── produtos/               #   Visão de produtos e decisões arquiteturais (ADRs)
│   └── negocio/                #   Prospecção B2B, AEO/GEO e estratégias comerciais
│
├── templates/                  # Modelos reutilizáveis para agentes criarem notas
├── scripts/                    # Automações em Python/Shell e base do MCP Server
└── CONVENCOES.md               # Manual de regras canônicas de escrita
```

---

## 📚 Índice Consolidado

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

### 👤 Murilo (Pessoal & Engenharia) → [índice do domínio](murilo/README.md)

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](murilo/ia/conceitos/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Analytics de produto — PostHog](murilo/engenharia/infra/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](murilo/engenharia/infra/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](murilo/engenharia/infra/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](murilo/engenharia/infra/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Clean Code — estudo](murilo/engenharia/clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Conectores do Claude (MCP)](murilo/ia/agentes/claude/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](murilo/ia/agentes/claude/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](murilo/engenharia/bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Email transacional — Resend](murilo/engenharia/infra/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](murilo/ia/conceitos/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [Fluxo Issue → PR → commit padronizado](murilo/engenharia/ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [Geração de UI e de app por IA — os três níveis](murilo/ia/geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.
- [GitHub Issue Creator — Estruturação Automatizada de Chamados](murilo/engenharia/ferramentas/github/github-issue-creator.md) — Skill para conversão de logs e stack traces em issues formatadas no GitHub com sanitização de segredos.
- [Global Rules — comportamento padrão de agente](murilo/ia/regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD](murilo/engenharia/infra/guarita.md) — Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção.
- [Impeccable — Linter Determinístico e Design System para UI por IA](murilo/engenharia/ferramentas/impeccable.md) — Ferramenta de 59 regras determinísticas e comandos de design para eliminar padrões genéricos ('AI slop') e polir interfaces no front-end.
- [Modus Operandi — Como o Murilo Trabalha](murilo/perfil/modus-operandi.md) — Diretrizes de engenharia, princípios inegociáveis e postura esperada de agentes de IA.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](murilo/engenharia/infra/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Padrão de nomes de repositórios GitHub](murilo/engenharia/ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.
- [Persona — Conselheiro Estratégico Direto](murilo/ia/personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](murilo/ia/personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.
- [Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS](murilo/engenharia/infra/portless.md) — Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes.
- [Portão de adoção de ferramenta](murilo/engenharia/adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Prompt Engineering — estudo](murilo/ia/conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](murilo/engenharia/qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.
- [Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código](murilo/engenharia/ferramentas/semgrep-guardian.md) — Auditoria estática de segurança integrada ao loop de agentes de IA, bloqueando vulnerabilidades em tempo real antes do commit.
- [Spec to Code Compliance — Auditoria Determinística de Requisitos por IA](murilo/engenharia/ferramentas/spec-to-code-compliance.md) — Plugin da Trail of Bits para verificação formal de conformidade entre especificações (SPEC.md/PRD) e código implementado.
- [Supabase como backend-as-a-service — o teto real do free tier](murilo/engenharia/infra/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.
- [Workspace Rules — regras locais de projeto](murilo/ia/regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

### 🏢 Async Studio (Marca, Produtos & Negócio) → [índice do domínio](async/README.md)

- [ADR 001 — Plataforma de observabilidade padrão](async/produtos/adr-001-observabilidade.md) — Sentry no free tier, instrumentado via OpenTelemetry, como padrão para projeto novo. Proposta.
- [AEO/GEO — otimizar conteúdo para ser citado por IA generativa](async/negocio/aeo-geo-otimizacao-para-ia.md) — AEO e GEO são o mesmo campo sem consenso de nome: estruturar conteúdo para ChatGPT, Perplexity e AI Overviews citarem como fonte. Técnica concreta, aplicável já ao SEO da Hamidi.
- [Brand Guidelines — Async Studio](async/identidade/brand-guidelines.md) — Identidade institucional, proposta de valor, visão e posicionamento do Async Studio.
- [Paleta de Cores e Tokens Visuais — Async](async/identidade/paleta-de-cores.md) — Especificações de cores, tokens CSS e diretrizes de contraste para produtos e site do Async Studio.
- [Prospecção B2B e mídia paga — quando essas ferramentas passam a valer](async/negocio/prospeccao-e-midia-paga.md) — Apollo.io, ZoomInfo e Windsor.ai: custo real, portão de cada uma e o que a LGPD exige.
- [Site Institucional — Async Studio](async/produtos/site-institucional.md) — Arquitetura, páginas, stack e diretrizes de deploy do site institucional do Async Studio.
- [Tokens CSS e Sistema de Design — Async](async/design-system/tokens-css.md) — Tokens de tipografia, espaçamento, bordas e sombras prontos para copiar em CSS/Tailwind.
- [Tom de Voz e Comunicação — Async](async/identidade/tom-de-voz.md) — Diretrizes de redação técnica, tom de voz e copywriting para produtos e comunicação da Async.
- [Visão do Produto — AsyncHub CRM](async/produtos/app-asynchub.md) — Plataforma central de gestão de clientes, leads e automação de processos internos da Async.
- [Visão do Produto — Encaixe (Agendamento Inteligente)](async/produtos/app-encaixe.md) — Arquitetura, objetivos de negócio e decisões técnicas do aplicativo Encaixe.

<!-- FIM:INDICE -->

---

## 🤖 Usando as Skills com Agentes de IA

As skills em `murilo/ia/agentes/claude/skills/` seguem o formato padrão de skills (pasta com `SKILL.md` + frontmatter `name`/`description`). Para instalá-las localmente:

```bash
./scripts/sync-skills.sh          # simulação (mostra o que faria)
./scripts/sync-skills.sh --apply  # cria os links em ~/.claude/skills/
```

O script usa symlinks: editar uma skill no vault reflete instantaneamente nos agentes sem re-sincronizar.

---

## ⚙️ Automações e Scripts

```bash
./scripts/nova-nota.sh murilo/engenharia docker-compose "Docker Compose na Prática"
```

| Script | Para quê |
| :--- | :--- |
| `./scripts/nova-nota.sh <pilar/subpasta> <nome-kebab>` | Criar nota nova já com frontmatter preenchido |
| `./scripts/gerar-indices.py` | Regenerar automaticamente os índices de todos os READMEs |
| `./scripts/validar-vault.py` | Validar links quebrados, wikilinks ambíguos e integridade |
| `./scripts/sync-skills.sh --apply` | Sincronizar skills locais para agentes |

---

## 📌 Regras Essenciais

1. **Kebab-Case Único**: Todo arquivo possui nome em `kebab-case` sem acentos e único no vault.
2. **Dois Pilares**: Toda informação pertence a `murilo/` ou `async/`.
3. **Sem Overengineering**: Notas curadas e focadas em aplicação prática.
4. Para detalhes completos, consulte o arquivo [CONVENCOES.md](CONVENCOES.md).
