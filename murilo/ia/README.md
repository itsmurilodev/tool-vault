# 🤖 IA

Inteligência artificial e agentes. A divisão interna segue uma pergunta: **isso funciona em qualquer agente, ou só em um?**

```text
ia/
├── conceitos/   # teoria — vale para qualquer LLM
├── personas/    # texto que você cola em qualquer agente
├── regras/      # regras de comportamento (Global/Workspace Rules)
└── agentes/     # ecossistema de agentes, conectores e skills operacionais
```

`ia/regras/global-rules.md` é o **canônico de comportamento**: o que vale por padrão em qualquer agente. Persona é escalada deliberada além desse padrão, e só registra o que difere dele. Skill é método executável empacotado no formato de um agente.

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Geração de UI e de app por IA — os três níveis](geracao-de-ui-por-ia.md) — Os três níveis — instalar componente, gerar componente, gerar app — com risco e reversibilidade de cada um.

### Agentes

- [Conectores do Claude (MCP)](agentes/conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](agentes/configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

### Conceitos

- [Agent-Browser — Automação e Navegação Web para Agentes de IA](conceitos/agent-browser.md) — Arquitetura Rust/Node.js de navegação autônoma por IA com sistema ref-based, limitações de latência e comparação com Playwright.
- [Caveman — Stack de Otimização e Eficiência de Tokens para Agentes de IA](conceitos/caveman.md) — Ecossistema de compressão de tokens para agentes de IA (Caveman Skill para output telegráfico, Caveman Proxy para compressão de input com recuperação CCR e Caveman Learn).
- [Context7 — Injeção de Documentação Atualizada para Agentes (MCP e Skills)](conceitos/context7.md) — Arquitetura do Context7 da Upstash, protocolo MCP de 2 passos, redução de context bloat (~65%), benefícios, riscos operacionais e matriz de decisão.
- [Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto](conceitos/find-skills.md) — Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes.
- [Graphify — Grafos de Conhecimento Estrutural e Navegação de Codebase para Agentes de IA](conceitos/graphify.md) — Indexação estática via Tree-sitter AST, enriquecimento semântico e geração de grafos de dependência queryáveis para agentes de codificação.
- [Graphiti — Grafos de Conhecimento Temporal e Memória Dinâmica para Agentes de IA](conceitos/graphiti.md) — Framework open-source da Zep para construção de Temporal Knowledge Graphs, unindo busca híbrida (vetor, BM25, grafo) e invalidação temporal de fatos para agentes.
- [Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)](conceitos/playwright-mcp.md) — Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão.
- [Ponytail — Engenharia Minimalista e Prevenção de Over-engineering para Agentes de IA](conceitos/ponytail.md) — Skill e framework de decisão que induz agentes de IA a priorizarem soluções nativas, bibliotecas padrão e código mínimo (YAGNI), reduzindo LOC em 54%.
- [Prompt Engineering — estudo](conceitos/prompt-engineering.md) — Instruções claras, delimitadores, formato de saída e avaliação iterativa.
- [RTK (Rust Token Killer) — Otimização e Filtragem de Saída CLI para Agentes de IA](conceitos/rtk.md) — Proxy CLI de alta performance em Rust que comprime saídas de terminal (git, testes, linters) em 60-90% antes da injeção no contexto do LLM.
- [Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end](conceitos/skill-ui.md) — Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto.

### Personas

- [Persona — Conselheiro Estratégico Direto](personas/conselheiro-estrategico.md) — Escalada deliberada da postura crítica além do padrão; o comportamento base vive em global-rules.
- [Persona — Engenheiro de Prompts Estratégico](personas/engenheiro-de-prompts.md) — Postura crítica para trabalhar prompt; o método canônico vive nas skills, aqui fica só o bloco colável.

### Regras

- [Global Rules — comportamento padrão de agente](regras/global-rules.md) — Comportamento padrão do agente em qualquer projeto — o canônico de comportamento.
- [Workspace Rules — regras locais de projeto](regras/workspace-rules.md) — Como e onde escrever regra específica de projeto.

<!-- FIM:INDICE -->

## Atalhos

- [Agentes & Skills](agentes/README.md) — skills operacionais, conectores e configuração.

---

## Backlog deste domínio

- [ ] Context engineering: janela de contexto, compactação, RAG vs contexto longo
- [ ] Avaliação de saída de LLM — como testar prompt de forma repetível
- [ ] Skill de revisão de arquitetura (citada como "em construção" em `levantamento-requisitos`)
- [ ] Documentar ChatGPT/Codex, Gemini e Antigravity em `agentes/`
