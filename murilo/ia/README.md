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

`ia/regras/global-rules.md` é o **canônico de comportamento**: o que vale por padrão em qualquer agente. Persona é escalada deliberada além desse padrão, e só registra o que difere dele. Skill é método executável empacotado no formato de um agente.

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Geração de UI e de app por IA — os três níveis](geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.

### Agentes › Claude

- [Conectores do Claude (MCP)](agentes/claude/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](agentes/claude/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

### Conceitos

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](conceitos/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Context7 — Injeção de Documentação Atualizada para Agentes (MCP e Skills)](conceitos/context7.md) — Arquitetura do Context7 da Upstash, protocolo MCP de 2 passos, redução de context bloat (~65%), benefícios, riscos operacionais e matriz de decisão.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](conceitos/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)](conceitos/playwright-mcp.md) — Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão.
- [Prompt Engineering — estudo](conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end](conceitos/skill-ui.md) — Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto.

### Personas

- [Persona — Conselheiro Estratégico Direto](personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.

### Regras

- [Global Rules — comportamento padrão de agente](regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Workspace Rules — regras locais de projeto](regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

<!-- FIM:INDICE -->

## Atalhos

- [Panorama dos agentes](agentes/README.md) — critério do que é portável e o que não é.
- [Claude](agentes/claude/README.md) — skills, conectores e configuração.

---

## Backlog deste domínio

- [ ] Context engineering: janela de contexto, compactação, RAG vs contexto longo
- [ ] Avaliação de saída de LLM — como testar prompt de forma repetível
- [ ] Skill de revisão de arquitetura (citada como "em construção" em `levantamento-requisitos`)
- [ ] Documentar ChatGPT/Codex, Gemini e Antigravity em `agentes/`
