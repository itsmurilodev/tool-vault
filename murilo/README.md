# 👤 Murilo — Conhecimento Pessoal & Engenharia

> Hub central de conhecimento pessoal: princípios de trabalho, estudos acadêmicos/cursos, boas práticas de engenharia de software e artefatos de inteligência artificial.

---

## 🗂️ Estrutura deste Pilar

* **`perfil/`**: Modus operandi, diretrizes de código e postura esperada de agentes.
* **`estudos/`**: Anotações e disciplinas da faculdade (`faculdade/`) e cursos (`cursos/`).
* **`engenharia/`**: Clean code, qualidade de software, infraestrutura (`infra/`) e ferramentas (`ferramentas/`).
* **`ia/`**: Engenharia de prompts, personas, regras globais e skills de agentes (`agentes/skills/`).

---

## 📚 Índice de Conhecimento

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

### Engenharia

- [Clean Code — estudo](engenharia/clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](engenharia/bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Portão de adoção de ferramenta](engenharia/adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](engenharia/qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.

### Engenharia › Ferramentas

- [Impeccable — Linter Determinístico e Design System para UI por IA](engenharia/ferramentas/impeccable.md) — Ferramenta de 59 regras determinísticas e comandos de design para eliminar padrões genéricos ('AI slop') e polir interfaces no front-end.
- [React Doctor — Auditoria Estática e Profiling de Anti-Patterns em React](engenharia/ferramentas/react-doctor.md) — Scanner em Rust (Oxlint) e profiler de DevTools para diagnosticar gargalos de render, anti-patterns de estado/efeitos e guiar agentes de IA.
- [React Scan — Detecção Automática de Re-renders e Profiling Visual](engenharia/ferramentas/react-scan.md) — Ferramenta zero-config de profiling e auditoria de re-renders no React via Canvas overlay e interceptação de Fiber.
- [Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código](engenharia/ferramentas/semgrep-guardian.md) — Auditoria estática de segurança integrada ao loop de agentes de IA, bloqueando vulnerabilidades em tempo real antes do commit.
- [Spec to Code Compliance — Auditoria Determinística de Requisitos por IA](engenharia/ferramentas/spec-to-code-compliance.md) — Plugin da Trail of Bits para verificação formal de conformidade entre especificações (SPEC.md/PRD) e código implementado.
- [Strix — Pentest Autônomo e Validação Dinâmica de Segurança por IA](engenharia/ferramentas/strix.md) — Framework open-source de agentes de IA para descoberta, exploração ativa e validação via PoC de vulnerabilidades em aplicações.

### Engenharia › Ferramentas › GitHub

- [Fluxo Issue → PR → commit padronizado](engenharia/ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [GitHub Issue Creator — Estruturação Automatizada de Chamados](engenharia/ferramentas/github/github-issue-creator.md) — Skill para conversão de logs e stack traces em issues formatadas no GitHub com sanitização de segredos.
- [Padrão de nomes de repositórios GitHub](engenharia/ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.

### Engenharia › Infraestrutura

- [Analytics de produto — PostHog](engenharia/infra/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](engenharia/infra/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](engenharia/infra/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](engenharia/infra/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Email transacional — Resend](engenharia/infra/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD](engenharia/infra/guarita.md) — Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](engenharia/infra/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS](engenharia/infra/portless.md) — Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes.
- [Supabase como backend-as-a-service — o teto real do free tier](engenharia/infra/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.

### IA & Agentes

- [Geração de UI e de app por IA — os três níveis](ia/geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.

### IA & Agentes › Agentes

- [Conectores do Claude (MCP)](ia/agentes/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](ia/agentes/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

### IA & Agentes › Conceitos

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](ia/conceitos/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Caveman — Stack de Otimização e Eficiência de Tokens para Agentes de IA](ia/conceitos/caveman.md) — Ecossistema de compressão de tokens para agentes de IA (Caveman Skill para output telegráfico, Caveman Proxy para compressão de input com recuperação CCR e Caveman Learn).
- [Context7 — Injeção de Documentação Atualizada para Agentes (MCP e Skills)](ia/conceitos/context7.md) — Arquitetura do Context7 da Upstash, protocolo MCP de 2 passos, redução de context bloat (~65%), benefícios, riscos operacionais e matriz de decisão.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](ia/conceitos/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [Graphify — Grafos de Conhecimento Estrutural e Navegação de Codebase para Agentes de IA](ia/conceitos/graphify.md) — Indexação estática via Tree-sitter AST, enriquecimento semântico e geração de grafos de dependência queryáveis para agentes de codificação.
- [Graphiti — Grafos de Conhecimento Temporal e Memória Dinâmica para Agentes de IA](ia/conceitos/graphiti.md) — Framework open-source da Zep para construção de Temporal Knowledge Graphs, unindo busca híbrida (vetor, BM25, grafo) e invalidação temporal de fatos para agentes.
- [Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)](ia/conceitos/playwright-mcp.md) — Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão.
- [Ponytail — Engenharia Minimalista e Prevenção de Over-engineering para Agentes de IA](ia/conceitos/ponytail.md) — Skill e framework de decisão que induz agentes de IA a priorizarem soluções nativas, bibliotecas padrão e código mínimo (YAGNI), reduzindo LOC em 54%.
- [Prompt Engineering — estudo](ia/conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [RTK (Rust Token Killer) — Otimização e Filtragem de Saída CLI para Agentes de IA](ia/conceitos/rtk.md) — Proxy CLI de alta performance em Rust que comprime saídas de terminal (git, testes, linters) em 60-90% antes da injeção no contexto do LLM.
- [Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end](ia/conceitos/skill-ui.md) — Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto.

### IA & Agentes › Personas

- [Persona — Conselheiro Estratégico Direto](ia/personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](ia/personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.

### IA & Agentes › Regras

- [Global Rules — comportamento padrão de agente](ia/regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Workspace Rules — regras locais de projeto](ia/regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

### Perfil & Modus Operandi

- [Modus Operandi — Como o Murilo Trabalha](perfil/modus-operandi.md) — Diretrizes de engenharia, princípios inegociáveis e postura esperada de agentes de IA.

<!-- FIM:INDICE -->
