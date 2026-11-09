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

| Skill | Quando dispara |
| --- | --- |
| [clean-code](skills/clean-code/SKILL.md) | Aplica o padrão pessoal de Clean Code do usuário — nomes que revelam intenção, funções pequenas com responsabilidade única, zero duplicação, tratamento de erro explícito, sem over… |
| [context7](skills/context7/SKILL.md) | Consulta documentação oficial versionada e snippets de código atualizados utilizando o Context7 (servidor MCP ou CLI ctx7 da Upstash). Elimina alucinações de APIs, métodos depreci… |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control s… |
| [decisao-arquitetural](skills/decisao-arquitetural/SKILL.md) | Ajuda a tomar e registrar decisões técnicas/arquiteturais não-triviais usando o formato de Architecture Decision Record (ADR): esclarecer restrições reais antes de propor solução,… |
| [grill-me](skills/grill-me/SKILL.md) | Questiona uma ideia até ela ficar consistente: pergunta, espera a resposta, pergunta de novo, e só resume o que entendeu e pede confirmação antes de aplicar qualquer coisa. Usar S… |
| [heuristicas-nielsen](skills/heuristicas-nielsen/SKILL.md) | Aplica e avalia as 10 Heurísticas de Usabilidade de Nielsen (visibilidade do status, correspondência com o mundo real, controle do usuário, consistência, prevenção de erros, recon… |
| [impeccable-ui](skills/impeccable-ui/SKILL.md) | Aplica as 59 regras determinísticas e comandos de design do Impeccable para eliminar 'AI slop' (gradientes roxo/azul clichês, cards aninhados, contraste ruim) e garantir interface… |
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Ajuda a clarear o pensamento antes de implementar qualquer coisa nova: entender o problema real por trás do pedido, separar requisito funcional de não-funcional, priorizar (MoSCoW… |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of prov… |
| [performance-web](skills/performance-web/SKILL.md) | Aplica o kit de performance web do usuário (Next.js/React, rotas de API, Supabase/Postgres) — padrões baratos ao escrever código (imagens, fontes, scripts de terceiros, Promise.al… |
| [portless-dev](skills/portless-dev/SKILL.md) | Gerencia e executa servidores de desenvolvimento locais através do Portless (proxy reverso com terminação HTTPS e domínios *.localhost determinísticos). Usar SEMPRE que for inicia… |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Usar sempre que o usuário pedir para gerar, melhorar, revisar ou enviar um prompt para uma IA/agente (ChatGPT, Claude, Codex, Antigravity, Gemini). Aplica estrutura em tags XML co… |
| [radar-de-tecnologias](skills/radar-de-tecnologias/SKILL.md) | Consulta e alimenta o radar de tecnologias do usuário (veredito adotar/testar/avaliar/evitar, quando usar, quando não usar, pré-requisito) antes de recomendar, instalar ou adotar… |
| [react-doctor](skills/react-doctor/SKILL.md) | Audita e diagnostica anti-patterns em aplicações React e Next.js utilizando o React Doctor (motor Oxlint em Rust e traces do Chrome DevTools). Detecta uso indevido de useEffect, p… |
| [semgrep-scan](skills/semgrep-scan/SKILL.md) | Audita e blinda código contra vulnerabilidades de segurança (SAST) em tempo real — injeção SQL, brechas em Row Level Security (RLS) do Supabase, CORS permissivo, segredos/tokens e… |
| [spec-compliance](skills/spec-compliance/SKILL.md) | Audita formalmente a conformidade entre uma especificação técnica (SPEC.md, PRD, requisitos de cliente) e o código real implementado em ./src, seguindo o método da Trail of Bits.… |

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
