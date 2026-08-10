# 🤖 IA

Inteligência artificial e agentes. A divisão interna segue uma pergunta: **isso funciona em qualquer agente, ou só em um?**

```text
ia/
├── conceitos/   # teoria — vale para qualquer LLM
├── personas/    # texto que você cola em qualquer agente
├── regras/      # regras de comportamento (Global/Workspace Rules)
└── agentes/     # específico de cada agente
    └── claude/  # skills, conectores, configuração
```

## Conceitos — portável

- [Prompt Engineering](conceitos/prompt-engineering.md) — instruções claras, delimitadores, formato de saída, avaliação iterativa.
- [Geração de UI e de app por IA](geracao-de-ui-por-ia.md) — os três níveis (instalar componente, gerar componente, gerar app), com risco e reversibilidade de cada um.

## Personas — portável

- [Conselheiro Estratégico Direto](personas/conselheiro-estrategico.md) — espelho crítico, sem bajulação, crítica que vira plano.
- [Engenheiro de Prompts Estratégico](personas/engenheiro-de-prompts.md) — avaliador crítico de prompts, com grill-me obrigatório.

## Regras — portável

- [Global Rules](regras/global-rules.md) — comportamento padrão em qualquer projeto.
- [Workspace Rules](regras/workspace-rules.md) — como e onde escrever regra específica de projeto.

## Agentes — específico

- [Claude](agentes/claude/) — [skills](agentes/claude/skills/), [conectores (MCP)](agentes/claude/conectores.md), [configuração e hooks](agentes/claude/configuracao.md).
- [Panorama dos agentes](agentes/README.md) — critério do que é portável e o que não é.

---

## Backlog deste domínio

- [ ] Context engineering: janela de contexto, compactação, RAG vs contexto longo
- [ ] Avaliação de saída de LLM — como testar prompt de forma repetível
- [ ] Skill de revisão de arquitetura (citada como "em construção" em `levantamento-requisitos`)
- [ ] Documentar ChatGPT/Codex, Gemini e Antigravity em `agentes/`
