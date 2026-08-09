# 🤖 IA

Inteligência artificial e agentes: teoria de LLM e prompt, e os artefatos que os agentes realmente executam.

## Conceitos — estudo e teoria

- [Prompt Engineering](conceitos/prompt-engineering.md) — instruções claras, delimitadores, formato de saída, avaliação iterativa.

## Skills — artefatos executáveis

Pasta espelhada em `~/.claude/skills` via `scripts/sync-skills.sh`.

| Skill | Quando dispara |
| ----- | -------------- |
| [clean-code](skills/clean-code/SKILL.md) | Sempre que houver código sendo escrito, editado ou revisado |
| [decisao-arquitetural](skills/decisao-arquitetural/SKILL.md) | Escolha estrutural difícil de reverter (ADR) |
| [grill-me](skills/grill-me/SKILL.md) | Só sob pedido explícito — interrogatório até a ideia ficar consistente |
| [heuristicas-nielsen](skills/heuristicas-nielsen/SKILL.md) | Qualquer trabalho de interface / front-end |
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Funcionalidade nova ou pedido de cliente antes de implementar |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Gerar, revisar ou melhorar prompt para outra IA |

## Personas — perfis de comportamento

- [Conselheiro Estratégico Direto](personas/conselheiro-estrategico.md) — espelho crítico, sem bajulação, crítica que vira plano.
- [Engenheiro de Prompts Estratégico](personas/engenheiro-de-prompts.md) — avaliador crítico de prompts, com grill-me obrigatório.

## Regras — comportamento base do agente

- [Global Rules](regras/global-rules.md) — comportamento padrão em qualquer projeto.
- [Workspace Rules](regras/workspace-rules.md) — como e onde escrever regra específica de projeto.

---

## Backlog deste domínio

- [ ] Nota sobre context engineering (janela de contexto, compactação, RAG vs contexto longo)
- [ ] Nota sobre avaliação de saída de LLM (como testar prompt de forma repetível)
- [ ] Skill de revisão de arquitetura (citada como "em construção" em `levantamento-requisitos`)
