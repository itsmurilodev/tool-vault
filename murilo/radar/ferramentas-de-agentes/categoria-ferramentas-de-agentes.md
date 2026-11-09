---
titulo: "Categoria — Ferramentas de agentes"
resumo: "Página-guia do que o agente usa para ler e agir: documentação atualizada (Context7), economia de contexto (Caveman, RTK), mapa do código (Graphify), memória (Graphiti), navegador (Playwright, agent-browser), padrão de UI (Skill UI) e criação de issue. Inclui o risco de auto-instalar skills (find-skills)."
tipo: conceito
dominio: murilo
tags: [murilo/radar, radar/ferramentas-de-agentes, categoria, agentes]
status: ativo
atualizado: 2026-11-09
---

# Ferramentas de agentes

> **Em uma frase:** o que entra no contexto do agente e o que ele usa para agir. Cada ferramenta aqui **ocupa contexto**, então só entra a que paga o lugar.

## 🧠 A ideia em linguagem simples

O agente trabalha com uma "mesa" de tamanho fixo (a janela de contexto). As ferramentas desta categoria fazem uma de quatro coisas:

1. **Trazem informação certa:** documentação atualizada (Context7), mapa do código (Graphify), memória de longo prazo (Graphiti).
2. **Liberam espaço na mesa:** comprimem saída de terminal (RTK) ou a própria conversa (Caveman).
3. **Dão mãos ao agente:** navegador (Playwright, agent-browser), criação de issue.
4. **Padronizam o resultado:** regras de UI em forma de skill (Skill UI).

O erro comum é encher a mesa de ferramenta "porque pode ajudar". O pior caso é deixar o agente **instalar skills sozinho** (find-skills): contexto inchado e porta aberta para prompt injection.

> 💡 **Analogia:** a bancada de um eletricista. O multímetro e o alicate certos ficam à mão. A caixa inteira de ferramentas despejada na bancada só atrapalha.

## 🗺️ Mapa da categoria

```mermaid
flowchart LR
    subgraph INFO["Informação certa"]
        C7["Context7<br/>docs atualizadas"]
        GY["Graphify<br/>mapa do código"]
        GI["Graphiti<br/>memória temporal"]
    end
    subgraph ESPACO["Liberar contexto"]
        RTK["RTK<br/>saída de terminal"]
        CV["Caveman<br/>compressão"]
    end
    subgraph MAOS["Agir"]
        PW["Playwright CLI/MCP"]
        AB["agent-browser"]
        GH["github-issue-creator"]
    end
    subgraph PADRAO["Padronizar"]
        SUI["Skill UI"]
    end
    AG["Agente"] --> INFO
    AG --> ESPACO
    AG --> MAOS
    AG --> PADRAO
```

## 📋 Itens da categoria

| Item | Radar | Quando usar | Ficha |
| --- | --- | --- | --- |
| Context7 | ✅ adotar | Lib que muda rápido ou migração de versão | [[context7]] |
| Playwright para agentes (CLI vs MCP) | ✅ adotar | CLI no terminal; MCP só em cliente sem shell | [[playwright-mcp]] |
| Skill UI (padrão de UI em skill) | ✅ adotar | Gerar ou auditar tela com agente | [[skill-ui]] |
| Caveman | ⏳ avaliar | Custo de token medido em sessão longa ou loop autônomo | [[caveman]] |
| RTK | ⏳ avaliar | Testes e linters ruidosos em sessão autônoma | [[rtk]] |
| Graphify | ⏳ avaliar | Codebase acima de ~30 mil linhas | [[graphify]] |
| Graphiti | ⏳ avaliar | Agente com memória de longo prazo (ex.: copiloto do AsyncHub) | [[graphiti]] |
| github-issue-creator | ⏳ avaliar | Triagem de bugs de terceiros tomando tempo | [[github-issue-creator]] |
| agent-browser | ⛔ evitar | Playwright cobre melhor | [[agent-browser]] |
| find-skills (auto-instalação de skills) | ⛔ evitar | Nunca pelo agente; só o humano pesquisando | [[find-skills]] |

## 🧭 Como decidir

```mermaid
flowchart TD
    Q1{"O problema é o agente<br/>não saber algo?"} -- "API de lib" --> C7["Context7"]
    Q1 -- "estrutura do código grande" --> GY["Graphify"]
    Q1 -- "fatos que mudam no tempo" --> GI["Graphiti"]
    Q2{"O problema é contexto<br/>cheio ou caro (medido)?"} -- "saída de terminal" --> RTK["RTK"]
    Q2 -- "conversa longa" --> CV["Caveman"]
    Q3{"O agente precisa<br/>usar o navegador?"} -- "sim" --> PW["Playwright CLI"]
```

## 🔗 Relacionados

- [[categoria-plataformas-de-agentes]] (onde o agente roda) · [[categoria-verificacao-e-qualidade]]
- Voltar ao [[catalogo-do-radar]] · [[como-usar-o-radar]]
