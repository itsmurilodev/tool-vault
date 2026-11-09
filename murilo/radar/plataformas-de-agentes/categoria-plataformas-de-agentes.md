---
titulo: "Categoria — Plataformas de agentes"
resumo: "Página-guia de onde os agentes rodam: worktree local, Claude Code na nuvem, claude-code-action no GitHub, e as plataformas da Cursor e da xAI (Cloud Agents, Grok Bot) que ficam fora por redundância e risco."
tipo: conceito
dominio: murilo
tags: [murilo/radar, radar/plataformas-de-agentes, categoria, agentes]
status: ativo
atualizado: 2026-11-09
---

# Plataformas de agentes

> **Em uma frase:** onde o agente trabalha (sua máquina, uma VM na nuvem ou o GitHub) e quando vale tirar ele da sua máquina.

## 🧠 A ideia em linguagem simples

Editar código em paralelo é fácil: cada agente fica numa cópia dos arquivos (git worktree). O que trava é **verificar** em paralelo, porque cada agente precisa subir o próprio app e o próprio banco, e na sua máquina as portas e o banco colidem. É aí que uma VM na nuvem vale a pena. Você **já tem** isso no Claude Code e no Codex. Cursor Cloud Agents e Grok Bot fazem coisa parecida, mas seriam plataformas extras.

> 💡 **Analogia:** worktree é dar uma mesa para cada marceneiro na mesma oficina, dividindo a serra. A nuvem é dar uma oficina inteira para cada um. Para desenhar, a mesa basta. Para testar a peça montada, a serra compartilhada vira fila.

## 🗺️ Onde cada coisa roda

```mermaid
flowchart TD
    subgraph LOCAL["Sua máquina"]
        W["Worktree por sessão<br/>(app desktop do Claude Code)"]
    end
    subgraph NUVEM["Nuvem (VM por tarefa)"]
        CC["Claude Code na nuvem"]
        CX["Codex cloud"]
    end
    subgraph GH["GitHub"]
        ACT["claude-code-action<br/>(issue com label)"]
    end
    subgraph FORA["Fora do stack hoje"]
        CUR["Cursor Cloud Agents"]
        GB["Grok Bot"]
    end
```

## 📋 Itens da categoria

| Plataforma | Radar | Quando usar | Ficha |
| --- | --- | --- | --- |
| Claude Code na nuvem | ⏳ avaliar | 2+ tarefas verificando o app ao mesmo tempo, ou tarefa longa com você fora | [[claude-code-na-nuvem]] |
| claude-code-action | ⏳ avaliar | Agente disparado por issue quando **você** aplica a label | [[claude-code-action]] |
| Cursor Cloud Agents | ⛔ evitar | Só se a Cursor virar seu ambiente principal | [[cursor-cloud-agents]] |
| Grok Bot | ⛔ evitar | Só com time maior e computador compartilhado sem logins sensíveis | [[grok-bot]] |

## 🧭 Como decidir onde rodar

```mermaid
flowchart TD
    Q0{"Precisa de credencial<br/>de produção?"} -- "sim" --> X["Nenhum: reveja a tarefa"]
    Q0 -- "não" --> Q1{"Quantas tarefas precisam<br/>subir o app ao mesmo tempo?"}
    Q1 -- "1 ou 2" --> L["Worktree local + Portless"]
    Q1 -- "2 ou mais" --> N["Claude Code na nuvem"]
    Q1 -- "tarefa longa, você fora" --> N
    Q2{"O trabalho começa<br/>numa issue triada?"} -- "sim" --> A["claude-code-action<br/>(label aplicada por você)"]
```

## 🔗 Análises da categoria

- [[agentes-em-nuvem-vs-worktrees]]: comparação completa entre local e nuvem.
- [[portless]]: domínios locais por serviço, que resolve portas em worktree.
- Voltar ao [[catalogo-do-radar]] · [[como-usar-o-radar]]
