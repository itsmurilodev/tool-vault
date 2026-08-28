---
titulo: "Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end"
resumo: "Padrão de UI Skills para agentes de IA: arquitetura SKILL.md, injeção progressiva, combate a AI slop e governança de contexto."
tipo: conceito
dominio: murilo
tags: [murilo/ia, frontend, agentes, skills, design-system]
status: ativo
atualizado: 2026-08-28
---

# Skill UI — Engenharia de Contexto para Interfaces e Geração de Front-end

## 📌 Resumo

Uma **Skill de UI** (ou *UI Agent Skill*) é um artefato padronizado de **engenharia de contexto** estruturado no formato `SKILL.md` (e recursos auxiliares em `scripts/` e `references/`). Ao contrário de bibliotecas de componentes tradicionais (`npm i ...`) ou prompts monolíticos estáticos (`.cursorrules` de milhares de linhas), as UI Skills ensinam e restringem o comportamento de assistentes de código (Claude Code, Cursor, Codex, Antigravity) sob demanda.

O objetivo central é converter prompts vagos de interface em código de front-end com padrão de produção (React, Next.js, Tailwind, Radix UI), erradicando o chamado **"AI Slop"** (interfaces genéricas com gradientes roxo/azul saturados, falta de acessibilidade WCAG e ausência de estados interativos).

---

## ⚙️ 1. Arquitetura e Mecânica Interna

### O Modelo de Descoberta Progressiva (*Progressive Disclosure*)

Em fluxos tradicionais, desenvolvedores inseriam regras completas de design no prompt de sistema global, consumindo continuamente milhares de tokens em todas as requisições. As UI Skills operam em três fases desacopladas:

```
[Início de Sessão] ──> Metadados Leves (Name + Description) ~60 tokens
                              │
[Intenção Detectada] ──> Usuário solicita criação ou auditoria de UI
                              │
[Ativação On-Demand] ──> Agente executa view_file(SKILL.md)
                              │
[Compilação de Contexto] ─> Aplica Design Tokens, Primitivas e Regras A11y
                              │
[Fechamento de Loop] ───> Validação com MCP (Playwright / Chrome DevTools)
```

1. **Fase de Descoberta (Metadados):** O agente carrega apenas a assinatura YAML (`name`, `description`). Ocupa menos de 0.1% do budget de contexto.
2. **Fase de Ativação (On-Demand):** Quando o usuário solicita construção ou refatoração visual, o agente carrega o corpo das instruções (`SKILL.md`).
3. **Restrições Determinísticas:** A skill impõe regras como:
   - Uso obrigatório do utilitário `cn()` (`clsx` + `tailwind-merge`) para mesclagem limpa de classes.
   - Utilização de primitivas de acessibilidade (Radix UI, React Aria) em vez de `<div>` com manipuladores de clique soltos.
   - Presença obrigatória de estados completos: `hover:`, `focus-visible:`, `active:`, `disabled:` e `loading`.
   - Paletas e tokens calibrados a partir das variáveis CSS do projeto, evitando cores arbitrárias.

---

## 🎯 2. Quando Usar (Cenários Ideais & Benefícios)

| Cenário | Benefício Técnico |
| :--- | :--- |
| **Geração de Componentes e Telas** | Garante código com tipagem TypeScript estrita, hierarquia visual calibrada e semântica acessível. |
| **Padronização de Equipe Multi-Agente** | Assegura que múltiplos desenvolvedores usando diferentes IAs (Claude, Cursor, Codex) gerem código alinhado ao mesmo padrão de front-end. |
| **Auditoria e Refinamento de UI Legada** | Permite invocar o agente em modo de crítica/inspeção para identificar e corrigir violações de contraste e layout. |
| **Economia de Tokens e Latência** | Elimina a saturação da janela de contexto quando a tarefa não envolve interface (ex: desenvolvimento de APIs backend). |

---

## ⛔ 3. Quando NÃO Usar (Cenários Inadequados & Riscos)

| Cenário Inadequado | Risco Técnico / Consequência |
| :--- | :--- |
| **Codebase com Design System Proprietário Não Mapeado** | Injetar uma UI Skill genérica em um projeto com biblioteca legada própria (ex: CSS Modules ou Emotion customizado) causa conflito de classes e retrabalho. |
| **Pequenas Alterações de Texto ou Ajustes Pontuais** | Ativar a skill inteira para trocar uma string adiciona overhead desnecessário de leitura de contexto. |
| **Auto-instalação Dinâmica de Skills Comunitárias** | Baixar skills arbitrárias via CLI em runtime introduz risco crítico de *prompt injection* e poluição de regras (vide [[find-skills]]). |
| **Substituição de Testes Visuais e E2E** | A skill orienta a sintaxe do código, mas o LLM não enxerga o layout renderizado sem um loop de inspeção com navegador (vide [[playwright-mcp]]). |

---

## ⚠️ 4. Pegadinhas Técnicas & Cuidados Operacionais

1. **Context Window Drift (Degradação em Sessões Longas):** Em chats que ultrapassam 40 a 50 turnos, as instruções lidas na ativação da skill perdem peso atencional. Para mitigar, reinicie a sessão ou instrua o agente a reler a skill.
2. **Conflito de Regras (Rule Shadowing):** Se existirem regras de UI espalhadas em `.cursorrules`, `CLAUDE.md` e `SKILL.md`, o agente pode gerar classes conflitantes. Centralize as diretrizes operacionais no padrão de skills.
3. **Overengineering de Estilos:** Evite criar abstrações prematuras ou dezenas de variantes `cva` para componentes simples de uso único.

---

## 🛡️ 5. Governança e Aplicação no Tool-Vault

No ecossistema do Murilo e da Async Studio, a adoção de UI Skills segue diretrizes claras:

1. **Conexão com Níveis de Automação:** Enquadra-se no **Nível 2** de [[geracao-de-ui-por-ia]] (geração e refinamento de componentes sob medida com revisão obrigatória).
2. **Curadoria Estática de Skills:** Novas skills de UI devem ser avaliadas pelo [[adocao-de-ferramenta]] e mantidas em `murilo/ia/agentes/skills/` (ex: a skill operacional [impeccable-ui](../agentes/skills/impeccable-ui/SKILL.md) e a nota técnica [[impeccable]]).
3. **Régua Tripla de Revisão:** Todo componente gerado via UI Skill deve ser validado contra:
   - [[clean-code]] (nomes com intenção, responsabilidade única, tratamento de erro).
   - [heuristicas-nielsen](../agentes/skills/heuristicas-nielsen/SKILL.md) (visibilidade de status, prevenção de erros e consistência).
   - [[tokens-css]] e [[paleta-de-cores]] (aderência à identidade visual da Async Studio).

---

## 🔗 Ver também

* [[geracao-de-ui-por-ia]] — os três níveis de geração de UI e seus riscos de reversibilidade.
* [[find-skills]] — análise de segurança contra inchaço de contexto e meta-skills.
* [[impeccable]] — ferramenta e linter determinístico de interface para eliminar AI slop.
* [[clean-code]] — padrões de legibilidade e manutenibilidade para componentes.
* [[adocao-de-ferramenta]] — portão de decisão para novas ferramentas e extensões.
* [[playwright-mcp]] — automação e fechamento de loop visual no navegador.
* [[tokens-css]] — tokens de design e variáveis CSS do ecossistema.

---

## 📚 Fontes e Referências

* [Agent Skills Open Specification](https://agentskills.io) · [Claude Skills Reference](https://claude.com)
* [ibelick/ui-skills](https://github.com/ibelick/ui-skills) · [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
* [Impeccable Style Guide](https://impeccable.style)
