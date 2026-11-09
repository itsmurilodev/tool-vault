# 🤖 Agentes

Tudo que a IA **executa**: skills, regras de comportamento, personas, conectores e configuração.

| Pasta / nota | O que é |
| --- | --- |
| `skills/` | Uma pasta por skill, com `SKILL.md`. Ficam visíveis para o Claude via `./scripts/atualizar.sh` (symlink em `~/.claude/skills`). |
| `regras/` | `global-rules` é o comportamento padrão de qualquer agente; `workspace-rules` explica regra por projeto. |
| `personas/` | Textos para colar quando quiser uma postura além do padrão. |
| `conectores.md` · `configuracao.md` | Conectores MCP do Claude e onde cada instrução deve morar (CLAUDE.md, skill ou hook). |

Formato de skill: [CLAUDE.md](../CLAUDE.md) (seção Convenções) e o modelo [skill.md](../modelos/skill.md).

## Skills

<!-- INICIO:SKILLS (gerado por scripts/gerar-indices.py — não editar à mão) -->

### Suas skills (14)

| Skill | Quando dispara |
| --- | --- |
| [clean-code](skills/clean-code/SKILL.md) | Aplica o padrão pessoal de código do usuário com foco em NOMENCLATURA — nomes que revelam intenção, identificadores em PT-BR sem acento, verbo em função, booleano como pergunta, l… |
| [context7](skills/context7/SKILL.md) | Consulta documentação oficial versionada e snippets de código atualizados utilizando o Context7 (servidor MCP ou CLI ctx7 da Upstash). Elimina alucinações de APIs, métodos depreci… |
| [decisao-arquitetural](skills/decisao-arquitetural/SKILL.md) | Ajuda a tomar e registrar decisões técnicas/arquiteturais não-triviais usando o formato de Architecture Decision Record (ADR): esclarecer restrições reais antes de propor solução,… |
| [grill-me](skills/grill-me/SKILL.md) | Questiona uma ideia até ela ficar consistente: pergunta, espera a resposta, pergunta de novo, e só resume o que entendeu e pede confirmação antes de aplicar qualquer coisa. Usar S… |
| [heuristicas-nielsen](skills/heuristicas-nielsen/SKILL.md) | Aplica e avalia as 10 Heurísticas de Usabilidade de Nielsen (visibilidade do status, correspondência com o mundo real, controle do usuário, consistência, prevenção de erros, recon… |
| [impeccable-ui](skills/impeccable-ui/SKILL.md) | Aplica as 59 regras determinísticas e comandos de design do Impeccable para eliminar 'AI slop' (gradientes roxo/azul clichês, cards aninhados, contraste ruim) e garantir interface… |
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Ajuda a clarear o pensamento antes de implementar qualquer coisa nova: entender o problema real por trás do pedido, separar requisito funcional de não-funcional, priorizar (MoSCoW… |
| [performance-web](skills/performance-web/SKILL.md) | Aplica o kit de performance web do usuário (Next.js/React, rotas de API, Supabase/Postgres) — padrões baratos ao escrever código (imagens, fontes, scripts de terceiros, Promise.al… |
| [portless-dev](skills/portless-dev/SKILL.md) | Gerencia e executa servidores de desenvolvimento locais através do Portless (proxy reverso com terminação HTTPS e domínios *.localhost determinísticos). Usar SEMPRE que for inicia… |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Usar sempre que o usuário pedir para gerar, melhorar, revisar ou enviar um prompt para uma IA/agente (ChatGPT, Claude, Codex, Antigravity, Gemini). Aplica estrutura em tags XML co… |
| [radar-de-tecnologias](skills/radar-de-tecnologias/SKILL.md) | Consulta e alimenta o radar de tecnologias do usuário (veredito adotar/testar/avaliar/evitar, quando usar, quando não usar, pré-requisito) antes de recomendar, instalar ou adotar… |
| [react-doctor](skills/react-doctor/SKILL.md) | Audita e diagnostica anti-patterns em aplicações React e Next.js utilizando o React Doctor (motor Oxlint em Rust e traces do Chrome DevTools). Detecta uso indevido de useEffect, p… |
| [semgrep-scan](skills/semgrep-scan/SKILL.md) | Audita e blinda código contra vulnerabilidades de segurança (SAST) em tempo real — injeção SQL, brechas em Row Level Security (RLS) do Supabase, CORS permissivo, segredos/tokens e… |
| [spec-compliance](skills/spec-compliance/SKILL.md) | Audita formalmente a conformidade entre uma especificação técnica (SPEC.md, PRD, requisitos de cliente) e o código real implementado em ./src, seguindo o método da Trail of Bits.… |

### Copiadas de terceiros (51) — sem alteração; a maioria só roda quando você chama `/nome`

| Skill | Quando dispara |
| --- | --- |
| [architect](skills/architect/SKILL.md) | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivia… |
| [arena](skills/arena/SKILL.md) | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one atte… |
| [automate-me](skills/automate-me/SKILL.md) | Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. D… |
| [benchmark-checklist](skills/benchmark-checklist/SKILL.md) | Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark or r… |
| [blast-radius](skills/blast-radius/SKILL.md) | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for… |
| [bro](skills/bro/SKILL.md) | Restate the last message in plain human language, with no jargon. |
| [correct](skills/correct/SKILL.md) | Find the mistakes agents keep repeating in this repo and make each one impossible. Try architecture first, then types, then a lint whose error names the fix, then a test, and writ… |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control s… |
| [figure-it-out](skills/figure-it-out/SKILL.md) | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, r… |
| [how](skills/how/SKILL.md) | Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\",… |
| [in-your-own-words](skills/in-your-own-words/SKILL.md) | Restate in your own words what you think the user's goals are and what problem they're trying to solve. Use for /in-your-own-words. |
| [interrogate](skills/interrogate/SKILL.md) | Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Adversaries t… |
| [ketchup](skills/ketchup/SKILL.md) | Catch the user up on what changed in this chat since their last message, in plain words and small visuals. List every item waiting on them with what they need to decide it from th… |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of prov… |
| [no-comments](skills/no-comments/SKILL.md) | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. |
| [ponytail](skills/ponytail/SKILL.md) | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing, refactoring, revie… |
| [principle-attack-the-premise](skills/principle-attack-the-premise/SKILL.md) | Apply when two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it. |
| [principle-boundary-discipline](skills/principle-boundary-discipline/SKILL.md) | Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep b… |
| [principle-build-the-lever](skills/principle-build-the-lever/SKILL.md) | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subag… |
| [principle-encode-lessons-in-structure](skills/principle-encode-lessons-in-structure/SKILL.md) | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script inst… |
| [principle-exhaust-the-design-space](skills/principle-exhaust-the-design-space/SKILL.md) | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing. |
| [principle-experience-first](skills/principle-experience-first/SKILL.md) | Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones. |
| [principle-explain-the-number](skills/principle-explain-the-number/SKILL.md) | Apply before you measure, and before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it,… |
| [principle-fix-root-causes](skills/principle-fix-root-causes/SKILL.md) | Apply when debugging. Trace each symptom back to the first place the system went wrong and fix it there. A guard is a fix only when the state it handles is legitimate. |
| [principle-foundational-thinking](skills/principle-foundational-thinking/SKILL.md) | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so dow… |
| [principle-guard-the-context-window](skills/principle-guard-the-context-window/SKILL.md) | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads. |
| [principle-laziness-protocol](skills/principle-laziness-protocol/SKILL.md) | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem. |
| [principle-make-operations-idempotent](skills/principle-make-operations-idempotent/SKILL.md) | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs. |
| [principle-migrate-callers-then-delete-legacy-apis](skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers. |
| [principle-minimize-reader-load](skills/principle-minimize-reader-load/SKILL.md) | Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink… |
| [principle-model-the-domain](skills/principle-model-the-domain/SKILL.md) | Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. |
| [principle-never-block-on-the-human](skills/principle-never-block-on-the-human/SKILL.md) | Apply when tempted to ask 'should I do X?' on reversible work. |
| [principle-outcome-oriented-execution](skills/principle-outcome-oriented-execution/SKILL.md) | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatib… |
| [principle-prove-it-works](skills/principle-prove-it-works/SKILL.md) | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it… |
| [principle-redesign-from-first-principles](skills/principle-redesign-from-first-principles/SKILL.md) | Apply when integrating a new requirement into an existing design. |
| [principle-separate-before-serializing-shared-state](skills/principle-separate-before-serializing-shared-state/SKILL.md) | Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a real… |
| [principle-sequence-verifiable-units](skills/principle-sequence-verifiable-units/SKILL.md) | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check e… |
| [principle-subtract-before-you-add](skills/principle-subtract-before-you-add/SKILL.md) | Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base. |
| [principle-test-behavior-not-implementation](skills/principle-test-behavior-not-implementation/SKILL.md) | Apply when you write, change, or keep a test. Assert what the code's users can observe, so that the test fails when that behavior breaks and keeps passing when only the internals… |
| [principle-type-system-discipline](skills/principle-type-system-discipline/SKILL.md) | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse… |
| [recall](skills/recall/SKILL.md) | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state… |
| [reflect](skills/reflect/SKILL.md) | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect. |
| [sharpen](skills/sharpen/SKILL.md) | Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen. |
| [show-me-your-work](skills/show-me-your-work/SKILL.md) | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewe… |
| [swarm](skills/swarm/SKILL.md) | Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration. |
| [tdd](skills/tdd/SKILL.md) | Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is unclear, e… |
| [teach](skills/teach/SKILL.md) | Explain a body of work plainly so a person actually understands it. Runs the `how` and `why` skills and weaves what they find into one clear explanation. Use for 'teach me this',… |
| [technical-writing](skills/technical-writing/SKILL.md) | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for /technical-writing or when writing… |
| [typescript-best-practices](skills/typescript-best-practices/SKILL.md) | TypeScript best practices. Use when reading or editing any .ts or .tsx file. |
| [unslop](skills/unslop/SKILL.md) | Cut AI tells from any writing. |
| [why](skills/why/SKILL.md) | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence ca… |

<!-- FIM:SKILLS -->

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Conectores do Claude (MCP)](conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

### Personas

- [Persona — Conselheiro Estratégico Direto](personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.

### Regras

- [Global Rules — comportamento padrão de agente](regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Workspace Rules — regras locais de projeto](regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

<!-- FIM:INDICE -->
