---
titulo: "Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)"
resumo: "Comparação arquitetural entre Playwright MCP (JSON-RPC) e Playwright CLI (Shell/Skills), análise de consumo de tokens (114k vs 27k) e matriz de decisão."
tipo: conceito
dominio: murilo
tags: [murilo/ia, mcp, cli, automacao, browser, ferramentas, testes]
status: ativo
atualizado: 2026-08-28
---

# Playwright para Agentes — MCP vs. CLI (Automação de Browser e Economia de Tokens)

## 📌 Resumo

Para permitir que agentes de IA (Claude, Cursor, Claude Code, Antigravity, Copilot) naveguem e interajam com páginas web sem o custo proibitivo de analisar HTML bruto ou screenshots pesados, a equipe do Playwright na Microsoft desenvolveu duas interfaces distintas de automação baseadas em **árvores de acessibilidade (ARIA Snapshots)**:

1. **Playwright MCP (`@playwright/mcp`)**: Servidor baseado no padrão *Model Context Protocol*, operando via JSON-RPC com ferramentas nativas injetadas no contexto do modelo.
2. **Playwright CLI (`@playwright/cli`)**: Utilitário de linha de comando para agentes que possuem acesso a shell/terminal, operando no modelo *Snapshot → Ref → Act* guiado por documentação de **Skill (`SKILL.md`)**.

> 💡 **Analogia:** O **Playwright MCP** é como contratar um motorista particular com um rádio comunicador dedicado instalado no painel do seu carro (ocupa espaço fixo no painel o tempo todo, mas fala o protocolo nativo do veículo). O **Playwright CLI** é como dar um mapa de bolso (Skill) para o agente usar as chaves e os pedais comuns da garagem quando precisar sair.

---

## 🧠 1. Arquitetura Interna: MCP vs. CLI

```text
======================= ABORDAGEM 1: PLAYWRIGHT MCP =======================
+------------------+    JSON-RPC (stdio)     +----------------------+
|    AI Agent      | <=====================> |    Playwright MCP    | ---> [Chromium / WK]
| (Claude Desktop) |   (Tool Calls / Tools)  | (Injeta 40+ Schemas) |
+------------------+                         +----------------------+

======================= ABORDAGEM 2: PLAYWRIGHT CLI =======================
+------------------+       Shell Exec        +----------------------+
|  Coding Agent    | ----------------------> |    playwright-cli    | ---> [Chromium / WK]
| (Claude Code/AGY)| <---------------------- | (Persiste no disco / |
+------------------+      Stdout/File        |  daemon de sessão)   |
        ^                                    +----------------------+
        | lê sob demanda
   [ SKILL.md ]
```

### A. Playwright MCP (`@playwright/mcp`)
* **Transporte:** Protocolo JSON-RPC 2.0 via `stdio` ou `SSE`.
* **Mecanismo:** Registra de 20 a 40+ ferramentas (`browser_navigate`, `browser_click`, `browser_snapshot`, etc.) diretamente no *system prompt* da IA.
* **Retorno:** Entrega a árvore ARIA diretamente como payload de resposta da tool call em memória.

### B. Playwright CLI (`@playwright/cli`)
* **Transporte:** Execução padrão de processos via shell (`bash`/`zsh`).
* **Mecanismo:** O agente executa comandos atômicos como `playwright-cli open <url>` e `playwright-cli click e5`. Mantém a sessão do navegador ativa via daemon em segundo plano (com suporte a sessões nomeadas via `-s=nome`).
* **Economia de Contexto via Skills:** Em vez de poluir o prompt com dezenas de schemas JSON complexos de ferramentas, o agente carrega um arquivo leve de instrução (`SKILL.md`) apenas quando precisa navegar.

---

## 📊 2. Dados de Desempenho e Economia de Tokens

Benchmarks oficiais e testes de engenharia revelam um impacto massivo no consumo da janela de contexto (*context window*):

| Métrica | Playwright MCP | Playwright CLI + Skill | Diferença / Ganho |
| :--- | :--- | :--- | :--- |
| **Carga Inicial de Schemas (Upfront Tax)** | **~13.000 a 17.000 tokens** (schemas de 40+ tools fixos) | **0 tokens** de schema (~1.200t se carregar a Skill) | **~90% menos overhead inicial** |
| **Consumo em Tarefa Típica de Navegação** | **~114.000 tokens** (payloads JSON acumulados) | **~27.000 tokens** (snapshots em disco / stdout enxuto) | **~76% de economia total de tokens** |
| **Latência por Ação (Engine)** | 80ms – 300ms | 90ms – 320ms (pequeno overhead de spawn de CLI) | Equivalente |
| **Consumo de Memória (RAM)** | ~180MB – 350MB por instância | ~180MB – 350MB por sessão de daemon | Idêntico (mesmo core Chromium) |

---

## ⚖️ 3. Matriz Comparativa Direta

| Critério | Playwright MCP (`@playwright/mcp`) | Playwright CLI (`@playwright/cli`) |
| :--- | :--- | :--- |
| **Ambiente Alvo** | Clientes GUI com suporte a MCP (Claude Desktop, Cursor, Windsurf). | Agentes de código com acesso a terminal/shell (Claude Code, Antigravity, Aider). |
| **Invocação** | Chamada de função estruturada (Native Tool Calling). | Comandos de linha de comando (`playwright-cli <cmd>`). |
| **Custo de Contexto** | Alto (sobretaxa fixa em todas as mensagens da conversa). | Baixo (consome tokens apenas nos passos em que é executado). |
| **Gerenciamento de Sessão** | Mantido pelo processo do servidor MCP. | Gerenciado via flag de sessão (`-s=minha-sessao`). |
| **Controle Fino de Rede** | Ferramentas dedicadas (`browser_route`, `browser_unroute`). | Comandos de configuração e flags de execução. |
| **Curva de Configuração** | Adicionar bloco JSON no arquivo de configuração MCP. | `npm install -g @playwright/cli` e instalação de skill. |

---

## 🎯 4. Critérios de Decisão: O Que Usar e Quando

### Cenário 1: Escolha **Playwright CLI** se:
* Você está usando ferramentas de terminal (Claude Code, Antigravity, Cursor em modo terminal/bash).
* O custo de tokens e a preservação da janela de contexto são prioridades críticas.
* A tarefa faz parte de um fluxo longo de programação onde você só precisa inspecionar a interface esporadicamente.

### Cenário 2: Escolha **Playwright MCP** se:
* Seu cliente de IA não tem permissão para rodar comandos de terminal arbitrários, mas tem suporte nativo a MCP (ex: Claude Desktop App).
* Você está construindo uma aplicação personalizada onde a IA interage via protocolo padronizado JSON-RPC/SSE.
* Você precisa de introspecção avançada e contínua de rotas de rede (`browser_route`) no loop agêntico.

### Cenário 3: NÃO use nenhum dos dois (Use Playwright Determinístico em Código):
* **Para Suítes de Testes de Regressão e CI/CD:** Utilize scripts de teste clássicos (`playwright test`) versionados no repositório ([[qualidade-automatizada]]). Testes orquestrados por LLM são lentos, caros e sofrem de não-determinismo.
* **Para Web Scraping Massivo:** Use scrapers HTTP ou bibliotecas headless dedicadas sem inferência de IA.

---

## ⚠️ 5. Riscos de Segurança e Cuidados Operacionais

1. **SSRF (Server-Side Request Forgery) e Acesso Local:**
   * Tanto o MCP quanto a CLI acessam portas locais (`localhost:3000`, `127.0.0.1`, APIs de metadados `169.254.169.254`).
   * **Risco:** Instruções maliciosas em páginas externas (*Indirect Prompt Injection*) podem induzir o agente a visitar endpoints administrativos locais e vazar dados.
2. **Invalidação de Refs em SPAs Dinâmicas:**
   * Se a interface sofrer re-renderização (ex: React/Vue após um fetch), identificadores como `e5` deixam de existir (*stale element reference*), exigindo um novo `snapshot`.
3. **Processos Zumbis do Navegador:**
   * Se o agente travar ou for interrompido abruptamente, certifique-se de executar `playwright-cli close` ou encerrar os processos filhos do Chromium para liberar memória.

---

## 🛠️ 6. Instalação e Exemplos Práticos

### Modo CLI (Recomendado para Coding Agents)
```bash
# 1. Instalação global
npm install -g @playwright/cli@latest

# 2. Fluxo básico de navegação
playwright-cli open https://app.exemplo.com
playwright-cli snapshot
playwright-cli fill e1 "usuario@async.com"
playwright-cli click e3
playwright-cli close
```

### Modo MCP (Para Clientes MCP como Claude Desktop / Cursor)
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

---

## 🔗 Ver também

* [[agent-browser]] — análise da ferramenta de navegação CLI da Vercel Labs.
* [[qualidade-automatizada]] — testes determinísticos com Playwright e Vitest em engenharia de software.
* [[conectores]] — servidores MCP remotos vs locais e superfície de segurança.
* [[find-skills]] — riscos de inchaço de contexto e controle de dependências em agentes.
* [[adocao-de-ferramenta]] — critérios do portão de adoção técnica do vault.

## 📚 Fontes

* [microsoft/playwright-mcp — Repositório Oficial](https://github.com/microsoft/playwright-mcp)
* [Playwright CLI for Coding Agents — Documentação Oficial Playwright](https://playwright.dev/)
* [Model Context Protocol — Anthropic Specification](https://modelcontextprotocol.io/)
