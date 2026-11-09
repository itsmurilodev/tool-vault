---
titulo: "Categoria — Produto & Atendimento"
resumo: "Página-guia de ferramentas open source que tocam os produtos da Async: Chatwoot (inbox omnichannel, decisão de construir ou integrar no AsyncHub) e Cal.diy (referência de código para o Encaixe)."
tipo: conceito
dominio: murilo
tags: [murilo/radar, radar/produto-e-atendimento, categoria, produto]
status: ativo
atualizado: 2026-11-09
---

# Produto & Atendimento

> **Em uma frase:** projetos open source que fazem parte do que você está construindo. A pergunta não é "uso?", é **"construo, integro ou só estudo?"**.

## 🧠 A ideia em linguagem simples

Dois projetos da lista resolvem o mesmo problema que dois produtos seus:

- O **Chatwoot** já é um inbox de WhatsApp, Instagram e e-mail com atribuição de atendente, que é o núcleo previsto no **AsyncHub**.
- O **Cal.diy** já é um sistema de agendamento (disponibilidade, fuso, conflito de agenda), o mesmo terreno do **Encaixe**.

Isso não quer dizer abandonar os produtos. Quer dizer **não reinventar** o que já foi resolvido, e decidir conscientemente o que é diferencial seu.

> 💡 **Analogia:** antes de construir uma cozinha, visitar uma que já funciona. Você pode copiar a disposição da bancada (referência), comprar o fogão pronto (integrar) ou fazer tudo sob medida (construir), mas decide depois de ver.

## 🧭 Construir, integrar ou estudar

```mermaid
flowchart TD
    Q1{"Essa parte é o diferencial<br/>do seu produto?"} -- "sim" --> B["Construir<br/>(projeto open source vira referência)"]
    Q1 -- "não" --> Q2{"Licença permite?<br/>Stack é sustentável para você?"}
    Q2 -- "sim" --> I["Integrar<br/>(registrar ADR)"]
    Q2 -- "não" --> E["Estudar o modelo de dados<br/>e construir o mínimo"]
```

## 📋 Itens da categoria

| Item | Radar | Quando usar | Ficha |
| --- | --- | --- | --- |
| Chatwoot | ⏳ avaliar | Antes de começar o inbox do AsyncHub: entra no ADR | [[chatwoot]] |
| Cal.diy | ✅ adotar, como referência | Ao implementar ou depurar horários e fuso no Encaixe | [[cal-diy]] |

## 🔗 Relacionados

- [[app-asynchub]] · [[app-encaixe]] · [[open-source-self-hosted-triagem]]
- Skill [decisao-arquitetural](../../ia/agentes/skills/decisao-arquitetural/SKILL.md)
- Voltar ao [[catalogo-do-radar]] · [[como-usar-o-radar]]
