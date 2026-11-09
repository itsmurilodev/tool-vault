---
titulo: "Grok Bot — bots persistentes com memória, rotinas e chat em grupo (xAI/Cursor)"
resumo: "Bots que funcionam como colegas de trabalho, com nome, memória, rotinas e chat em grupo, e que disparam agentes da Cursor. Em beta desde 2026-08. Todos os bots de uma conta dividem o mesmo computador e os mesmos logins, e a memória fica fora do repositório."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/plataformas-de-agentes, agentes, grok]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: evitar
categoria: plataformas-de-agentes
natureza: plataforma
quando_usar: "Reavaliar se o time crescer, as features passarem do que um agente carrega de contexto e o computador compartilhado puder ficar sem logins sensíveis."
quando_nao_usar: "Hoje: dev único e poucas features; todos os bots dividem computador, sessões e logins; memória fora do repositório, sem revisão."
pre_requisito: "Plano pago da Cursor ou SuperGrok; produto em beta."
---

# Grok Bot

> **Radar: ⛔ evitar (por enquanto).** Fique com a ideia (contexto por feature) na versão em arquivo: [[bots-donos-de-feature]].

## O que é

Produto da xAI distribuído com a Cursor (documentação em `cursor.com/docs/grok-bot`), em beta desde 2026-08-11. São bots com nome, função, memória e rotinas, que conversam em chat em grupo e passam trabalho de código para os agentes em nuvem da Cursor.

## Fato que contradiz o reel

O reel diz que "cada bot tem o próprio computador". A documentação diz: *"All of your Bots use the same cloud computer, sharing its files, browser sessions, and app logins."* Cada bot tem só a própria tela.

## Quando usar

- Time com várias pessoas e muitas features, quando um computador compartilhado sem logins sensíveis for aceitável.

## Quando não usar

- Hoje. Com prompt injection vindo de um payload de erro, o bot alcança todas as sessões logadas da conta.
- Quando a "memória" do bot for a única fonte sobre a feature, sem versão nem revisão.

## Alternativa que já serve

Um documento por feature no repositório (feature map do `verify-<app>`), atualizado no mesmo PR da mudança. Detalhes em [[bots-donos-de-feature]].

## Ver também

- [[bots-donos-de-feature]] · [[cursor-cloud-agents]] · [[categoria-plataformas-de-agentes]]

## Fontes

- [Cursor Docs — Grok Bot](https://cursor.com/docs/grok-bot) · [xAI — Introducing Grok Bot](https://x.ai/news/introducing-grok-bot)
