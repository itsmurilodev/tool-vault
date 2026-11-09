# 📡 Radar de tecnologias

Tudo que foi **analisado** (quase sempre vindo de redes sociais): ferramentas, apps, skills, plataformas e práticas, cada um com veredito, quando usar, quando não usar e como usar.

- **Para decidir rápido:** [catálogo do radar](catalogo-do-radar.md), uma tabela de decisão por anel (adotar, testar, avaliar, evitar).
- **Para agentes:** [como usar o radar](como-usar-o-radar.md), com o protocolo de decisão e o passo a passo para registrar item novo.
- **Para entender com diagrama:** uma página por categoria:
  - [Verificação & Qualidade](verificacao-e-qualidade/categoria-verificacao-e-qualidade.md)
  - [Fluxo com agentes](fluxo-com-agentes/categoria-fluxo-com-agentes.md)
  - [Plataformas de agentes](plataformas-de-agentes/categoria-plataformas-de-agentes.md)
  - [Performance web](performance-web/categoria-performance-web.md)
  - [Produto & Atendimento](produto-e-atendimento/categoria-produto-e-atendimento.md)
  - [Produtividade](produtividade/categoria-produtividade.md)
  - [Marketing & Conteúdo](marketing-e-conteudo/categoria-marketing-e-conteudo.md)
  - [Ferramentas de agentes](ferramentas-de-agentes/categoria-ferramentas-de-agentes.md)
  - [Segurança](seguranca/categoria-seguranca.md)
  - [Infraestrutura](infraestrutura/categoria-infraestrutura.md)

Cada tecnologia tem a própria pasta: `radar/<categoria>/<item>/<item>.md`.

## 📚 Índice

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Catálogo do radar — tabela de decisão de todas as tecnologias](catalogo-do-radar.md) — Todos os itens do radar agrupados por anel (adotar, testar, avaliar, evitar), com quando usar, quando não usar e pré-requisito. Gerado do frontmatter das fichas: é o ponto de partida de qualquer agente antes de recomendar uma ferramenta.
- [Como usar o radar — protocolo de decisão para agentes e para o Murilo](como-usar-o-radar.md) — Regra do radar de tecnologias: o que significa cada anel (adotar, testar, avaliar, evitar), como a pasta está organizada, o passo a passo que um agente segue antes de recomendar ou adotar qualquer ferramenta, e como registrar um item novo.
- [Lote — 9 ferramentas open source de uma lista viral (2026-11)](open-source-self-hosted-triagem.md) — Registro do lote 'ferramentas open source que você pode usar': Higgsfield, VoiceStudio, OpenSEO, AppFlowy, OpenWhispr, OpenProject, Cal.diy, Chatwoot e Cap. Cada uma tem ficha própria no radar; aqui ficam a visão geral, o resumo de licenças e a regra de self-host.

### Ferramentas de agentes

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](ferramentas-de-agentes/agent-browser/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Categoria — Ferramentas de agentes](ferramentas-de-agentes/categoria-ferramentas-de-agentes.md) — Página-guia do que o agente usa para ler e agir: documentação atualizada (Context7), economia de contexto (Caveman, RTK), mapa do código (Graphify), memória (Graphiti), navegador (Playwright, agent-browser), padrão de UI (Skill UI) e criação de issue. Inclui o risco de auto-instalar skills (find-skills).
- [Caveman — Stack de Otimização e Eficiência de Tokens para Agentes de IA](ferramentas-de-agentes/caveman/caveman.md) — Ecossistema de compressão de tokens para agentes de IA (Caveman Skill para output telegráfico, Caveman Proxy para compressão de input com recuperação CCR e Caveman Learn).
- [Context7 — Injeção de Documentação Atualizada para Agentes (MCP e Skills)](ferramentas-de-agentes/context7/context7.md) — Arquitetura do Context7 da Upstash, protocolo MCP de 2 passos, redução de context bloat (~65%), benefícios, riscos operacionais e matriz de decisão.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](ferramentas-de-agentes/find-skills/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [GitHub Issue Creator — Estruturação Automatizada de Chamados](ferramentas-de-agentes/github-issue-creator/github-issue-creator.md) — Skill para conversão de logs e stack traces em issues formatadas no GitHub com sanitização de segredos.
- [Graphify — Grafos de Conhecimento Estrutural e Navegação de Codebase para Agentes de IA](ferramentas-de-agentes/graphify/graphify.md) — Indexação estática via Tree-sitter AST, enriquecimento semântico e geração de grafos de dependência queryáveis para agentes de codificação.
- [Graphiti — Grafos de Conhecimento Temporal e Memória Dinâmica para Agentes de IA](ferramentas-de-agentes/graphiti/graphiti.md) — Framework open-source da Zep para construção de Temporal Knowledge Graphs, unindo busca híbrida (vetor, BM25, grafo) e invalidação temporal de fatos para agentes.
- [Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)](ferramentas-de-agentes/playwright-mcp/playwright-mcp.md) — Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão.
- [RTK (Rust Token Killer) — Otimização e Filtragem de Saída CLI para Agentes de IA](ferramentas-de-agentes/rtk/rtk.md) — Proxy CLI de alta performance em Rust que comprime saídas de terminal (git, testes, linters) em 60-90% antes da injeção no contexto do LLM.
- [Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end](ferramentas-de-agentes/skill-ui/skill-ui.md) — Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto.

### Fluxo com agentes

- [Bots donos de feature — Grok Bot e o modelo de 'colega de trabalho' por recurso](fluxo-com-agentes/bots-donos-de-feature/bots-donos-de-feature.md) — Episódio 3 da série do reel: um bot persistente por feature (Grok Bot), com memória atualizada a cada merge, chat em grupo entre bots e um bot de erro que roteia para o dono. A ideia de dono por feature é boa; a memória fora do repositório e o computador compartilhado não. Para o seu porte, a versão sem ferramenta nova é um documento por feature no repositório, que é o feature map do verify-<app>.
- [Captura de erros para agentes — do alerta em produção ao PR](fluxo-com-agentes/captura-de-erros-para-agentes/captura-de-erros-para-agentes.md) — Episódio 2 da série do reel: PostHog captura o erro, um bot dispara um agente em nuvem e o agente decide sozinho o risco do merge. A captura via issue é ótima; o gatilho por evento e o agente julgando o próprio risco não passam no portão. Aqui fica o pipeline adaptado: alerta só em issue nova, issue no GitHub como chamado, label humano como gatilho e gate de risco determinístico.
- [Categoria — Fluxo com agentes](fluxo-com-agentes/categoria-fluxo-com-agentes.md) — Página-guia das práticas para trabalhar com agentes de código: prompt com cenários de verificação, processo de correção de bug, captura de erros virando issue e dono por feature como documento. Inclui a ordem de adoção, porque cada prática depende da anterior.
- [Correção de bug com agentes — reproduzir, corrigir, provar, revisar](fluxo-com-agentes/correcao-de-bug-com-agentes/correcao-de-bug-com-agentes.md) — Processo de 4 etapas visto em reel (reproduzir com dado real, corrigir, verificar com o app rodando, revisão multi-modelo com auto-merge). A espinha está certa; dado de produção cru e merge sem humano não passam no portão para o seu estágio.
- [Prompt em três seções — tarefa, contexto e cenários de verificação](fluxo-com-agentes/prompt-com-cenarios-de-verificacao/prompt-com-cenarios-de-verificacao.md) — Episódio 5 da série do reel: todo prompt de tarefa tem objetivo, contexto e uma lista de cenários que precisam passar para a tarefa contar como feita. A terceira seção já foi aplicada na skill prompt-engineering-agente. O contexto deve ser ponteiro, não despejo.

### Infraestrutura

- [Analytics de produto — PostHog](infraestrutura/analytics-de-produto/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](infraestrutura/autenticacao-gerenciada/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](infraestrutura/banco-de-dados-vetorial/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](infraestrutura/cache-e-fila/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Categoria — Infraestrutura](infraestrutura/categoria-infraestrutura.md) — Página-guia dos serviços que sustentam os produtos: Supabase (base), Supabase Auth, Resend, PostHog e Sentry adotados ou em teste; Upstash, pgvector/Pinecone, Portless e SyncPay só com gatilho. Inclui a decisão em aberto PostHog vs Sentry (ADR-001).
- [Email transacional — Resend](infraestrutura/email-transacional/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](infraestrutura/observabilidade/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS](infraestrutura/portless/portless.md) — Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes.
- [Supabase como backend-as-a-service — o teto real do free tier](infraestrutura/backend-como-servico/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.
- [SyncPay — Infraestrutura de Pagamentos, Pix, Recorrência e Automação via MCP](infraestrutura/sync-pay/sync-pay.md) — Gateway de pagamentos focado no mercado brasileiro com Pix instantâneo, Pix Automático, cartão tokenizado, split e servidor MCP nativo para agentes de IA.

### Marketing & Conteúdo

- [Categoria — Marketing & Conteúdo](marketing-e-conteudo/categoria-marketing-e-conteudo.md) — Página-guia das ferramentas de SEO e produção de conteúdo: OpenSEO (dado de SEO pago por uso) e VoiceStudio (voz local) entram com projeto definido; Open Higgsfield é descartado por licença e risco.
- [Open Higgsfield — interface de geração de imagem e vídeo (descartado)](marketing-e-conteudo/open-higgsfield/open-higgsfield.md) — Vendido como alternativa open source ao Higgsfield AI, mas não tem licença, tem 1 contribuidor e 3 commits contra 5,5 mil estrelas, é só uma interface para uma API de geração paga, e a versão hospedada pede a sua chave de API.
- [OpenSEO — SEO open source com API paga por uso (alternativa ao Semrush/Ahrefs)](marketing-e-conteudo/openseo/openseo.md) — Pesquisa de palavra-chave, rastreio de posição e concorrentes, com MCP e skills para agentes. MIT, mas exige chave da DataForSEO paga por requisição; a versão hospedada cobra US$ 10/mês mais 28% em cada requisição.
- [VoiceStudio — voz por IA local (alternativa ao ElevenLabs)](marketing-e-conteudo/voicestudio/voicestudio.md) — Clonagem e design de voz, dublagem, ditado, transcrição e audiolivro em 646 idiomas, rodando local (Apple Silicon, CUDA ou CPU). O app é AGPL; cada modelo e cada áudio gerado têm licença própria. Clonar voz exige consentimento.

### Performance web

- [Categoria — Performance web](performance-web/categoria-performance-web.md) — Página-guia de performance: medir primeiro, aplicar o kit universal ao escrever e usar remédio caro (cache, fila, virtualização) só com sintoma medido. Aplicado pela skill performance-web.
- [Performance web — triagem das 31 dicas do reel e o kit universal](performance-web/kit-de-performance-web/performance-web-31-dicas.md) — As 31 dicas de performance do reel (@gustagoat.ai), validadas uma a uma e separadas em kit universal (padrão em qualquer projeto), condicionais (só com gatilho medido), já feitas pela plataforma (só verificar) e medição (vem primeiro). Virou a skill performance-web.
- [React Doctor — Auditoria Estática e Profiling de Anti-Patterns em React](performance-web/react-doctor/react-doctor.md) — Scanner em Rust (Oxlint) e profiler de DevTools para diagnosticar gargalos de render, anti-patterns de estado/efeitos e guiar agentes de IA.
- [React Scan — Detecção Automática de Re-renders e Profiling Visual](performance-web/react-scan/react-scan.md) — Ferramenta zero-config de profiling e auditoria de re-renders no React via Canvas overlay e interceptação de Fiber.

### Plataformas de agentes

- [Agentes de verificação em nuvem vs git worktrees locais](plataformas-de-agentes/agentes-em-nuvem-vs-worktrees.md) — Worktree isola só os arquivos; VM em nuvem isola o ambiente inteiro, e é a verificação (app + banco por agente) que quebra worktrees em paralelo. Você já tem nuvem no Claude Code e no Codex: não adote o Cursor por isso; use worktree local para 1–2 tarefas e nuvem quando houver verify-<app> e seed anonimizado.
- [Categoria — Plataformas de agentes](plataformas-de-agentes/categoria-plataformas-de-agentes.md) — Página-guia de onde os agentes rodam: worktree local, Claude Code na nuvem, claude-code-action no GitHub, e as plataformas da Cursor e da xAI (Cloud Agents, Grok Bot) que ficam fora por redundância e risco.
- [Claude Code na nuvem — sessões em VM da Anthropic](plataformas-de-agentes/claude-code-na-nuvem/claude-code-na-nuvem.md) — Sessões do Claude Code em VM Ubuntu (4 vCPU, 16 GB, Docker, Postgres, Chrome) que você já tem no plano. É a opção de nuvem quando várias tarefas precisam subir o app ao mesmo tempo ou rodar com você fora.
- [claude-code-action — agente disparado por issue/label no GitHub Actions](plataformas-de-agentes/claude-code-action/claude-code-action.md) — GitHub Action oficial da Anthropic que roda o Claude Code numa issue ou PR via @claude, label ou assignee. É o gatilho do pipeline de captura de erros, com a label aplicada por você como portão.
- [Cursor Cloud Agents — agentes em VM própria que testam e gravam demo](plataformas-de-agentes/cursor-cloud-agents/cursor-cloud-agents.md) — Agentes da Cursor que rodam numa VM isolada, usam o app no navegador e devolvem PR com vídeo e screenshot. Funciona, mas seria a terceira plataforma; o Claude Code na nuvem cobre o mesmo para você.
- [Grok Bot — bots persistentes com memória, rotinas e chat em grupo (xAI/Cursor)](plataformas-de-agentes/grok-bot/grok-bot.md) — Bots que funcionam como colegas de trabalho, com nome, memória, rotinas e chat em grupo, e que disparam agentes da Cursor. Em beta desde 2026-08. Todos os bots de uma conta dividem o mesmo computador e os mesmos logins, e a memória fica fora do repositório.

### Produtividade

- [AppFlowy — workspace open source (alternativa ao Notion)](produtividade/appflowy/appflowy.md) — Docs, wikis e projetos com IA, em AGPL e cliente Flutter, com nuvem própria opcional. Hoje só somaria ao Notion, Obsidian e Trello que você já usa; entra se você decidir sair do Notion.
- [Cap — gravação de tela open source (alternativa ao Loom)](produtividade/cap/cap.md) — App nativo que grava a tela e gera link na hora (Instant) ou edita localmente (Studio). Guarda local, num bucket S3/R2 seu ou em self-host. AGPL, o que não pesa para uso próprio.
- [Categoria — Produtividade](produtividade/categoria-produtividade.md) — Página-guia das ferramentas de uso pessoal e de gestão: OpenWhispr (ditado) e Cap (gravação de tela) para usar já; AppFlowy e OpenProject só com gatilho, porque somariam ao que você já tem.
- [OpenProject — gestão de projeto e portfólio open source](produtividade/openproject/openproject.md) — Gestão pesada (Gantt, portfólio, horas, boards) em Ruby e GPL. Superdimensionado para um estúdio de duas pessoas: GitHub Issues e Projects cobrem o dia a dia. Entra só se um cliente exigir.
- [OpenWhispr — ditado por voz local no desktop](produtividade/openwhispr/openwhispr.md) — Aperta uma tecla, fala, e o texto aparece no cursor. Roda local (Whisper/Parakeet) ou com sua chave na nuvem, e também transcreve reunião. MIT. Uso pessoal imediato para escrever prompts longos e notas.

### Produto & Atendimento

- [Cal.diy — agendamento open source (fork MIT do Cal.com)](produto-e-atendimento/cal-diy/cal-diy.md) — Versão comunitária do Cal.com sem o código enterprise, 100% MIT, só self-host. Para você, é livro-texto do Encaixe (fuso, disponibilidade, conflito de agenda), não backend; o próprio README desaconselha produção.
- [Categoria — Produto & Atendimento](produto-e-atendimento/categoria-produto-e-atendimento.md) — Página-guia de ferramentas open source que tocam os produtos da Async: Chatwoot (inbox omnichannel, decisão de construir ou integrar no AsyncHub) e Cal.diy (referência de código para o Encaixe).
- [Chatwoot — central de atendimento omnichannel open source](produto-e-atendimento/chatwoot/chatwoot.md) — Inbox único para WhatsApp, Instagram, e-mail e chat do site, em MIT (exceto a pasta enterprise). É exatamente o núcleo do inbox previsto no AsyncHub, então entra num ADR de construir ou integrar antes da primeira linha.

### Segurança

- [Categoria — Segurança](seguranca/categoria-seguranca.md) — Página-guia de segurança em três momentos: Semgrep no código (todo dia), Strix em staging antes de release de mudança sensível, e Guarita na superfície externa do que já está em produção.
- [Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD](seguranca/guarita/guarita.md) — Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção.
- [Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código](seguranca/semgrep-guardian/semgrep-guardian.md) — Auditoria estática de segurança integrada ao loop de agentes de IA, bloqueando vulnerabilidades em tempo real antes do commit.
- [Strix — Pentest Autônomo e Validação Dinâmica de Segurança por IA](seguranca/strix/strix.md) — Framework open-source de agentes de IA para descoberta, exploração ativa e validação via PoC de vulnerabilidades em aplicações.

### Verificação & Qualidade

- [Categoria — Verificação & Qualidade](verificacao-e-qualidade/categoria-verificacao-e-qualidade.md) — Página-guia da categoria: como provar que o código do agente funciona (verify-<app>) e como mantê-lo enxuto e legível (ponytail para quanto escrever, clean-code para nomes, revisão rígida só em relatório, regras mecânicas no CI).
- [Impeccable — Linter Determinístico e Design System para UI por IA](verificacao-e-qualidade/impeccable/impeccable.md) — Ferramenta de 59 regras determinísticas e comandos de design para eliminar padrões genéricos ('AI slop') e polir interfaces no front-end.
- [Ponytail — Engenharia Minimalista e Prevenção de Over-engineering para Agentes de IA](verificacao-e-qualidade/ponytail/ponytail.md) — Skill e framework de decisão que induz agentes de IA a priorizarem soluções nativas, bibliotecas padrão e código mínimo (YAGNI), reduzindo LOC em 54%.
- [pstack — coleção de skills de engenharia da Cursor (poteto)](verificacao-e-qualidade/pstack/pstack.md) — 58 skills da Lauren Tan (Cursor), analisadas uma a uma. 50 copiadas para o vault, sem alteração e manuais (só rodam com /nome); ficaram de fora o poteto-mode, as ligadas à Cursor e ao Grok, e o statechart pesado. Inclui a cola de quando usar cada uma.
- [pstack — create-verification-skill e maintain-verification-skill](verificacao-e-qualidade/pstack/pstack-verificacao.md) — Par de skills da Lauren Tan (Cursor) que gera e mantém uma skill de verificação por projeto: o agente sobe o app, usa como usuário e guarda evidência. Adota agora, copiando só as duas skills, em um projeto.
- [Skills de qualidade de código — Ponytail, pstack e thermo-nuclear review empilhados](verificacao-e-qualidade/skills-de-qualidade-de-codigo.md) — Episódio 4 da série do reel: rodar Ponytail + no-comments + typescript-best-practices + unslop + thermo-nuclear em todo PR. As peças são boas, mas se sobrepõem (o próprio autor admite) e duas se contradizem: Ponytail subtrai, thermo-nuclear reestrutura. Para você: uma regra na escrita (clean-code), uma revisão no PR e regra mecânica no lint/CI.
- [Spec to Code Compliance — Auditoria Determinística de Requisitos por IA](verificacao-e-qualidade/spec-to-code-compliance/spec-to-code-compliance.md) — Plugin da Trail of Bits para verificação formal de conformidade entre especificações (SPEC.md/PRD) e código implementado.
- [Thermo-nuclear code quality review — revisão rígida de manutenibilidade (Cursor)](verificacao-e-qualidade/thermo-nuclear-review/thermo-nuclear-review.md) — Skill da Cursor (MIT) que faz uma auditoria implacável da branch: code judo, arquivo acima de 1.000 linhas, if solto, wrapper fino. Útil só em modo relatório e em PR grande; aplicada sozinha, viola a regra de menor alteração.

<!-- FIM:INDICE -->
