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
│   ├── ia/                     #   Engenharia de prompts, personas, regras e skills
│   │   └── agentes/skills/     #     Skills operacionais para agentes de IA
│   └── radar/                  #   Radar de tecnologias analisadas (veredito + quando usar)
│       ├── catalogo-do-radar.md #    Tabela de decisão de todos os itens (gerada)
│       ├── como-usar-o-radar.md #    Protocolo de decisão para agentes
│       └── <categoria>/<item>/ #     Uma pasta por tecnologia, com página por categoria
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

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](murilo/radar/ferramentas-de-agentes/agent-browser/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Agentes de verificação em nuvem vs git worktrees locais](murilo/radar/plataformas-de-agentes/agentes-em-nuvem-vs-worktrees.md) — Worktree isola só os arquivos; VM em nuvem isola o ambiente inteiro, e é a verificação (app + banco por agente) que quebra worktrees em paralelo. Você já tem nuvem no Claude Code e no Codex: não adote o Cursor por isso; use worktree local para 1–2 tarefas e nuvem quando houver verify-<app> e seed anonimizado.
- [Analytics de produto — PostHog](murilo/radar/infraestrutura/analytics-de-produto/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [AppFlowy — workspace open source (alternativa ao Notion)](murilo/radar/produtividade/appflowy/appflowy.md) — Docs, wikis e projetos com IA, em AGPL e cliente Flutter, com nuvem própria opcional. Hoje só somaria ao Notion, Obsidian e Trello que você já usa; entra se você decidir sair do Notion.
- [Autenticação gerenciada — Clerk vs Supabase Auth](murilo/radar/infraestrutura/autenticacao-gerenciada/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](murilo/radar/infraestrutura/banco-de-dados-vetorial/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Bots donos de feature — Grok Bot e o modelo de 'colega de trabalho' por recurso](murilo/radar/fluxo-com-agentes/bots-donos-de-feature/bots-donos-de-feature.md) — Episódio 3 da série do reel: um bot persistente por feature (Grok Bot), com memória atualizada a cada merge, chat em grupo entre bots e um bot de erro que roteia para o dono. A ideia de dono por feature é boa; a memória fora do repositório e o computador compartilhado não. Para o seu porte, a versão sem ferramenta nova é um documento por feature no repositório, que é o feature map do verify-<app>.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](murilo/radar/infraestrutura/cache-e-fila/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Cal.diy — agendamento open source (fork MIT do Cal.com)](murilo/radar/produto-e-atendimento/cal-diy/cal-diy.md) — Versão comunitária do Cal.com sem o código enterprise, 100% MIT, só self-host. Para você, é livro-texto do Encaixe (fuso, disponibilidade, conflito de agenda), não backend; o próprio README desaconselha produção.
- [Cap — gravação de tela open source (alternativa ao Loom)](murilo/radar/produtividade/cap/cap.md) — App nativo que grava a tela e gera link na hora (Instant) ou edita localmente (Studio). Guarda local, num bucket S3/R2 seu ou em self-host. AGPL, o que não pesa para uso próprio.
- [Captura de erros para agentes — do alerta em produção ao PR](murilo/radar/fluxo-com-agentes/captura-de-erros-para-agentes/captura-de-erros-para-agentes.md) — Episódio 2 da série do reel: PostHog captura o erro, um bot dispara um agente em nuvem e o agente decide sozinho o risco do merge. A captura via issue é ótima; o gatilho por evento e o agente julgando o próprio risco não passam no portão. Aqui fica o pipeline adaptado: alerta só em issue nova, issue no GitHub como chamado, label humano como gatilho e gate de risco determinístico.
- [Categoria — Ferramentas de agentes](murilo/radar/ferramentas-de-agentes/categoria-ferramentas-de-agentes.md) — Página-guia do que o agente usa para ler e agir: documentação atualizada (Context7), economia de contexto (Caveman, RTK), mapa do código (Graphify), memória (Graphiti), navegador (Playwright, agent-browser), padrão de UI (Skill UI) e criação de issue. Inclui o risco de auto-instalar skills (find-skills).
- [Categoria — Fluxo com agentes](murilo/radar/fluxo-com-agentes/categoria-fluxo-com-agentes.md) — Página-guia das práticas para trabalhar com agentes de código: prompt com cenários de verificação, processo de correção de bug, captura de erros virando issue e dono por feature como documento. Inclui a ordem de adoção, porque cada prática depende da anterior.
- [Categoria — Infraestrutura](murilo/radar/infraestrutura/categoria-infraestrutura.md) — Página-guia dos serviços que sustentam os produtos: Supabase (base), Supabase Auth, Resend, PostHog e Sentry adotados ou em teste; Upstash, pgvector/Pinecone, Portless e SyncPay só com gatilho. Inclui a decisão em aberto PostHog vs Sentry (ADR-001).
- [Categoria — Marketing & Conteúdo](murilo/radar/marketing-e-conteudo/categoria-marketing-e-conteudo.md) — Página-guia das ferramentas de SEO e produção de conteúdo: OpenSEO (dado de SEO pago por uso) e VoiceStudio (voz local) entram com projeto definido; Open Higgsfield é descartado por licença e risco.
- [Categoria — Performance web](murilo/radar/performance-web/categoria-performance-web.md) — Página-guia de performance: medir primeiro, aplicar o kit universal ao escrever e usar remédio caro (cache, fila, virtualização) só com sintoma medido. Aplicado pela skill performance-web.
- [Categoria — Plataformas de agentes](murilo/radar/plataformas-de-agentes/categoria-plataformas-de-agentes.md) — Página-guia de onde os agentes rodam: worktree local, Claude Code na nuvem, claude-code-action no GitHub, e as plataformas da Cursor e da xAI (Cloud Agents, Grok Bot) que ficam fora por redundância e risco.
- [Categoria — Produtividade](murilo/radar/produtividade/categoria-produtividade.md) — Página-guia das ferramentas de uso pessoal e de gestão: OpenWhispr (ditado) e Cap (gravação de tela) para usar já; AppFlowy e OpenProject só com gatilho, porque somariam ao que você já tem.
- [Categoria — Produto & Atendimento](murilo/radar/produto-e-atendimento/categoria-produto-e-atendimento.md) — Página-guia de ferramentas open source que tocam os produtos da Async: Chatwoot (inbox omnichannel, decisão de construir ou integrar no AsyncHub) e Cal.diy (referência de código para o Encaixe).
- [Categoria — Segurança](murilo/radar/seguranca/categoria-seguranca.md) — Página-guia de segurança em três momentos: Semgrep no código (todo dia), Strix em staging antes de release de mudança sensível, e Guarita na superfície externa do que já está em produção.
- [Categoria — Verificação & Qualidade](murilo/radar/verificacao-e-qualidade/categoria-verificacao-e-qualidade.md) — Página-guia da categoria: como provar que o código do agente funciona (verify-<app>) e como mantê-lo enxuto e legível (clean-code + escada do Ponytail, revisão rígida só em relatório, regras mecânicas no CI).
- [Catálogo do radar — tabela de decisão de todas as tecnologias](murilo/radar/catalogo-do-radar.md) — Todos os itens do radar agrupados por anel (adotar, testar, avaliar, evitar), com quando usar, quando não usar e pré-requisito. Gerado do frontmatter das fichas: é o ponto de partida de qualquer agente antes de recomendar uma ferramenta.
- [Caveman — Stack de Otimização e Eficiência de Tokens para Agentes de IA](murilo/radar/ferramentas-de-agentes/caveman/caveman.md) — Ecossistema de compressão de tokens para agentes de IA (Caveman Skill para output telegráfico, Caveman Proxy para compressão de input com recuperação CCR e Caveman Learn).
- [Chatwoot — central de atendimento omnichannel open source](murilo/radar/produto-e-atendimento/chatwoot/chatwoot.md) — Inbox único para WhatsApp, Instagram, e-mail e chat do site, em MIT (exceto a pasta enterprise). É exatamente o núcleo do inbox previsto no AsyncHub, então entra num ADR de construir ou integrar antes da primeira linha.
- [Claude Code na nuvem — sessões em VM da Anthropic](murilo/radar/plataformas-de-agentes/claude-code-na-nuvem/claude-code-na-nuvem.md) — Sessões do Claude Code em VM Ubuntu (4 vCPU, 16 GB, Docker, Postgres, Chrome) que você já tem no plano. É a opção de nuvem quando várias tarefas precisam subir o app ao mesmo tempo ou rodar com você fora.
- [claude-code-action — agente disparado por issue/label no GitHub Actions](murilo/radar/plataformas-de-agentes/claude-code-action/claude-code-action.md) — GitHub Action oficial da Anthropic que roda o Claude Code numa issue ou PR via @claude, label ou assignee. É o gatilho do pipeline de captura de erros, com a label aplicada por você como portão.
- [Clean Code — estudo](murilo/engenharia/clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Como usar o radar — protocolo de decisão para agentes e para o Murilo](murilo/radar/como-usar-o-radar.md) — Regra do radar de tecnologias: o que significa cada anel (adotar, testar, avaliar, evitar), como a pasta está organizada, o passo a passo que um agente segue antes de recomendar ou adotar qualquer ferramenta, e como registrar um item novo.
- [Conectores do Claude (MCP)](murilo/ia/agentes/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](murilo/ia/agentes/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*
- [Context7 — Injeção de Documentação Atualizada para Agentes (MCP e Skills)](murilo/radar/ferramentas-de-agentes/context7/context7.md) — Arquitetura do Context7 da Upstash, protocolo MCP de 2 passos, redução de context bloat (~65%), benefícios, riscos operacionais e matriz de decisão.
- [Correção de bug com agentes — reproduzir, corrigir, provar, revisar](murilo/radar/fluxo-com-agentes/correcao-de-bug-com-agentes/correcao-de-bug-com-agentes.md) — Processo de 4 etapas visto em reel (reproduzir com dado real, corrigir, verificar com o app rodando, revisão multi-modelo com auto-merge). A espinha está certa; dado de produção cru e merge sem humano não passam no portão para o seu estágio.
- [Cursor Cloud Agents — agentes em VM própria que testam e gravam demo](murilo/radar/plataformas-de-agentes/cursor-cloud-agents/cursor-cloud-agents.md) — Agentes da Cursor que rodam numa VM isolada, usam o app no navegador e devolvem PR com vídeo e screenshot. Funciona, mas seria a terceira plataforma; o Claude Code na nuvem cobre o mesmo para você.
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](murilo/engenharia/bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Email transacional — Resend](murilo/radar/infraestrutura/email-transacional/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](murilo/radar/ferramentas-de-agentes/find-skills/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [Fluxo Issue → PR → commit padronizado](murilo/engenharia/ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [Geração de UI e de app por IA — os três níveis](murilo/ia/geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.
- [GitHub Issue Creator — Estruturação Automatizada de Chamados](murilo/radar/ferramentas-de-agentes/github-issue-creator/github-issue-creator.md) — Skill para conversão de logs e stack traces em issues formatadas no GitHub com sanitização de segredos.
- [Global Rules — comportamento padrão de agente](murilo/ia/regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Graphify — Grafos de Conhecimento Estrutural e Navegação de Codebase para Agentes de IA](murilo/radar/ferramentas-de-agentes/graphify/graphify.md) — Indexação estática via Tree-sitter AST, enriquecimento semântico e geração de grafos de dependência queryáveis para agentes de codificação.
- [Graphiti — Grafos de Conhecimento Temporal e Memória Dinâmica para Agentes de IA](murilo/radar/ferramentas-de-agentes/graphiti/graphiti.md) — Framework open-source da Zep para construção de Temporal Knowledge Graphs, unindo busca híbrida (vetor, BM25, grafo) e invalidação temporal de fatos para agentes.
- [Grok Bot — bots persistentes com memória, rotinas e chat em grupo (xAI/Cursor)](murilo/radar/plataformas-de-agentes/grok-bot/grok-bot.md) — Bots que funcionam como colegas de trabalho, com nome, memória, rotinas e chat em grupo, e que disparam agentes da Cursor. Em beta desde 2026-08. Todos os bots de uma conta dividem o mesmo computador e os mesmos logins, e a memória fica fora do repositório.
- [Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD](murilo/radar/seguranca/guarita/guarita.md) — Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção.
- [Impeccable — Linter Determinístico e Design System para UI por IA](murilo/radar/verificacao-e-qualidade/impeccable/impeccable.md) — Ferramenta de 59 regras determinísticas e comandos de design para eliminar padrões genéricos ('AI slop') e polir interfaces no front-end.
- [Lote — 9 ferramentas open source de uma lista viral (2026-11)](murilo/radar/open-source-self-hosted-triagem.md) — Registro do lote 'ferramentas open source que você pode usar': Higgsfield, VoiceStudio, OpenSEO, AppFlowy, OpenWhispr, OpenProject, Cal.diy, Chatwoot e Cap. Cada uma tem ficha própria no radar; aqui ficam a visão geral, o resumo de licenças e a regra de self-host.
- [Modus Operandi — Como o Murilo Trabalha](murilo/perfil/modus-operandi.md) — Diretrizes de engenharia, princípios inegociáveis e postura esperada de agentes de IA.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](murilo/radar/infraestrutura/observabilidade/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Open Higgsfield — interface de geração de imagem e vídeo (descartado)](murilo/radar/marketing-e-conteudo/open-higgsfield/open-higgsfield.md) — Vendido como alternativa open source ao Higgsfield AI, mas não tem licença, tem 1 contribuidor e 3 commits contra 5,5 mil estrelas, é só uma interface para uma API de geração paga, e a versão hospedada pede a sua chave de API.
- [OpenProject — gestão de projeto e portfólio open source](murilo/radar/produtividade/openproject/openproject.md) — Gestão pesada (Gantt, portfólio, horas, boards) em Ruby e GPL. Superdimensionado para um estúdio de duas pessoas: GitHub Issues e Projects cobrem o dia a dia. Entra só se um cliente exigir.
- [OpenSEO — SEO open source com API paga por uso (alternativa ao Semrush/Ahrefs)](murilo/radar/marketing-e-conteudo/openseo/openseo.md) — Pesquisa de palavra-chave, rastreio de posição e concorrentes, com MCP e skills para agentes. MIT, mas exige chave da DataForSEO paga por requisição; a versão hospedada cobra US$ 10/mês mais 28% em cada requisição.
- [OpenWhispr — ditado por voz local no desktop](murilo/radar/produtividade/openwhispr/openwhispr.md) — Aperta uma tecla, fala, e o texto aparece no cursor. Roda local (Whisper/Parakeet) ou com sua chave na nuvem, e também transcreve reunião. MIT. Uso pessoal imediato para escrever prompts longos e notas.
- [Padrão de nomes de repositórios GitHub](murilo/engenharia/ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.
- [Performance web — triagem das 31 dicas do reel e o kit universal](murilo/radar/performance-web/kit-de-performance-web/performance-web-31-dicas.md) — As 31 dicas de performance do reel (@gustagoat.ai), validadas uma a uma e separadas em kit universal (padrão em qualquer projeto), condicionais (só com gatilho medido), já feitas pela plataforma (só verificar) e medição (vem primeiro). Virou a skill performance-web.
- [Persona — Conselheiro Estratégico Direto](murilo/ia/personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](murilo/ia/personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.
- [Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)](murilo/radar/ferramentas-de-agentes/playwright-mcp/playwright-mcp.md) — Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão.
- [Ponytail — Engenharia Minimalista e Prevenção de Over-engineering para Agentes de IA](murilo/radar/verificacao-e-qualidade/ponytail/ponytail.md) — Skill e framework de decisão que induz agentes de IA a priorizarem soluções nativas, bibliotecas padrão e código mínimo (YAGNI), reduzindo LOC em 54%.
- [Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS](murilo/radar/infraestrutura/portless/portless.md) — Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes.
- [Portão de adoção de ferramenta](murilo/engenharia/adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Prompt em três seções — tarefa, contexto e cenários de verificação](murilo/radar/fluxo-com-agentes/prompt-com-cenarios-de-verificacao/prompt-com-cenarios-de-verificacao.md) — Episódio 5 da série do reel: todo prompt de tarefa tem objetivo, contexto e uma lista de cenários que precisam passar para a tarefa contar como feita. A terceira seção já foi aplicada na skill prompt-engineering-agente. O contexto deve ser ponteiro, não despejo.
- [Prompt Engineering — estudo](murilo/ia/conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [pstack — coleção de skills de engenharia da Cursor (poteto)](murilo/radar/verificacao-e-qualidade/pstack/pstack.md) — Cerca de 47 skills e 23 playbooks da Lauren Tan (Cursor). Vale copiar skills isoladas quando houver dor: as duas de verificação já estão no vault. O pacote inteiro e o poteto-mode não.
- [pstack — create-verification-skill e maintain-verification-skill](murilo/radar/verificacao-e-qualidade/pstack/pstack-verificacao.md) — Par de skills da Lauren Tan (Cursor) que gera e mantém uma skill de verificação por projeto: o agente sobe o app, usa como usuário e guarda evidência. Adota agora, copiando só as duas skills, em um projeto.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](murilo/engenharia/qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.
- [React Doctor — Auditoria Estática e Profiling de Anti-Patterns em React](murilo/radar/performance-web/react-doctor/react-doctor.md) — Scanner em Rust (Oxlint) e profiler de DevTools para diagnosticar gargalos de render, anti-patterns de estado/efeitos e guiar agentes de IA.
- [React Scan — Detecção Automática de Re-renders e Profiling Visual](murilo/radar/performance-web/react-scan/react-scan.md) — Ferramenta zero-config de profiling e auditoria de re-renders no React via Canvas overlay e interceptação de Fiber.
- [RTK (Rust Token Killer) — Otimização e Filtragem de Saída CLI para Agentes de IA](murilo/radar/ferramentas-de-agentes/rtk/rtk.md) — Proxy CLI de alta performance em Rust que comprime saídas de terminal (git, testes, linters) em 60-90% antes da injeção no contexto do LLM.
- [Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código](murilo/radar/seguranca/semgrep-guardian/semgrep-guardian.md) — Auditoria estática de segurança integrada ao loop de agentes de IA, bloqueando vulnerabilidades em tempo real antes do commit.
- [Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end](murilo/radar/ferramentas-de-agentes/skill-ui/skill-ui.md) — Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto.
- [Skills de qualidade de código — Ponytail, pstack e thermo-nuclear review empilhados](murilo/radar/verificacao-e-qualidade/skills-de-qualidade-de-codigo.md) — Episódio 4 da série do reel: rodar Ponytail + no-comments + typescript-best-practices + unslop + thermo-nuclear em todo PR. As peças são boas, mas se sobrepõem (o próprio autor admite) e duas se contradizem: Ponytail subtrai, thermo-nuclear reestrutura. Para você: uma regra na escrita (clean-code), uma revisão no PR e regra mecânica no lint/CI.
- [Spec to Code Compliance — Auditoria Determinística de Requisitos por IA](murilo/radar/verificacao-e-qualidade/spec-to-code-compliance/spec-to-code-compliance.md) — Plugin da Trail of Bits para verificação formal de conformidade entre especificações (SPEC.md/PRD) e código implementado.
- [Strix — Pentest Autônomo e Validação Dinâmica de Segurança por IA](murilo/radar/seguranca/strix/strix.md) — Framework open-source de agentes de IA para descoberta, exploração ativa e validação via PoC de vulnerabilidades em aplicações.
- [Supabase como backend-as-a-service — o teto real do free tier](murilo/radar/infraestrutura/backend-como-servico/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.
- [SyncPay — Infraestrutura de Pagamentos, Pix, Recorrência e Automação via MCP](murilo/radar/infraestrutura/sync-pay/sync-pay.md) — Gateway de pagamentos focado no mercado brasileiro com Pix instantâneo, Pix Automático, cartão tokenizado, split e servidor MCP nativo para agentes de IA.
- [Thermo-nuclear code quality review — revisão rígida de manutenibilidade (Cursor)](murilo/radar/verificacao-e-qualidade/thermo-nuclear-review/thermo-nuclear-review.md) — Skill da Cursor (MIT) que faz uma auditoria implacável da branch: code judo, arquivo acima de 1.000 linhas, if solto, wrapper fino. Útil só em modo relatório e em PR grande; aplicada sozinha, viola a regra de menor alteração.
- [VoiceStudio — voz por IA local (alternativa ao ElevenLabs)](murilo/radar/marketing-e-conteudo/voicestudio/voicestudio.md) — Clonagem e design de voz, dublagem, ditado, transcrição e audiolivro em 646 idiomas, rodando local (Apple Silicon, CUDA ou CPU). O app é AGPL; cada modelo e cada áudio gerado têm licença própria. Clonar voz exige consentimento.
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

As skills em `murilo/ia/agentes/skills/` seguem o formato padrão de skills (pasta com `SKILL.md` + frontmatter `name`/`description`). Para instalá-las localmente:

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
| `./scripts/exportar-pacote.py` | Gerar `dist/pacote-agentes.zip` (skills + notas de tecnologia + instruções) para o agente de outro projeto avaliar o que adotar |

---

## 📌 Regras Essenciais

1. **Kebab-Case Único**: Todo arquivo possui nome em `kebab-case` sem acentos e único no vault.
2. **Dois Pilares**: Toda informação pertence a `murilo/` ou `async/`.
3. **Sem Overengineering**: Notas curadas e focadas em aplicação prática.
4. Para detalhes completos, consulte o arquivo [CONVENCOES.md](CONVENCOES.md).
