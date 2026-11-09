---
titulo: "Chatwoot — central de atendimento omnichannel open source"
resumo: "Inbox único para WhatsApp, Instagram, e-mail e chat do site, em MIT (exceto a pasta enterprise). É exatamente o núcleo do inbox previsto no AsyncHub, então entra num ADR de construir ou integrar antes da primeira linha."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/produto-e-atendimento, open-source, atendimento, asynchub]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: produto-e-atendimento
natureza: ferramenta
quando_usar: "Antes de construir o inbox de WhatsApp e Instagram do AsyncHub: entra como opção no ADR de construir ou integrar."
quando_nao_usar: "Se o inbox for o diferencial do AsyncHub (aí serve só de referência); self-host sem decisão registrada em ADR."
pre_requisito: "ADR com a skill decisao-arquitetural; se integrar, servidor para Rails + Postgres + Redis + Sidekiq."
---

# Chatwoot

> **Radar: ⏳ avaliar.** É o item de maior impacto de produto da lista: pode economizar meses no AsyncHub, ou servir de livro-texto.

## O que é

`chatwoot/chatwoot` (39 mil estrelas, desde 2019). Central de atendimento com caixa única para chat do site, e-mail, Facebook, **Instagram, WhatsApp**, Telegram e SMS. Tem atribuição automática, campanhas e o agente de IA *Captain*. A licença é **MIT, exceto a pasta `enterprise/`**. **[INCERTO]** Não verifiquei quais recursos ficam no `enterprise/`.

## Quando usar

- Na decisão do inbox multi-agente do AsyncHub ([[app-asynchub]]). Registre um ADR com três opções:
  - **(a) construir;**
  - **(b) integrar o Chatwoot self-hosted** via API e webhooks;
  - **(c) usar o Chatwoot como referência** de modelo de dados.

## Quando não usar

- Se o inbox for o diferencial competitivo do AsyncHub. Nesse caso, construa e use o Chatwoot como referência.
- Em self-host sem ADR: é mais um servidor (Rails, Postgres, Redis, Sidekiq) para atualizar e fazer backup, numa stack diferente da sua (TS e Supabase).

## Como usar

1. Rode a skill `decisao-arquitetural` com as três opções acima.
2. Se a decisão for integrar: suba local com Docker, conecte um número de teste da WhatsApp Cloud API e meça o que falta para o AsyncHub.
3. Confira o que está em `enterprise/` antes de depender de um recurso.

## Ver também

- [[app-asynchub]] · [[open-source-self-hosted-triagem]] · [[categoria-produto-e-atendimento]]

## Fontes

- [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) (README e LICENSE, lidos em 2026-11-09)
