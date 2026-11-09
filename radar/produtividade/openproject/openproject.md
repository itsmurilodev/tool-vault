---
titulo: "OpenProject — gestão de projeto e portfólio open source"
resumo: "Gestão pesada (Gantt, portfólio, horas, boards) em Ruby e GPL. Superdimensionado para um estúdio de duas pessoas: GitHub Issues e Projects cobrem o dia a dia. Entra só se um cliente exigir."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/produtividade, open-source, gestao-de-projeto]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: produtividade
natureza: ferramenta
quando_usar: "Quando um cliente exigir cronograma Gantt, controle de horas ou gestão formal de portfólio."
quando_nao_usar: "No dia a dia do estúdio: GitHub Issues e Projects, junto com o fluxo issue → PR, já cobrem."
pre_requisito: "Servidor (Docker ou Kubernetes) e um cliente que exija o formato."
---

# OpenProject

> **Radar: ⏳ avaliar.** Ferramenta de empresa grande, sem uso no seu porte atual.

## O que é

`opf/openproject` (17 mil estrelas, GPL-3.0, desde 2012). Gestão de projeto e portfólio com Gantt, controle de horas, boards e orçamento. É em Ruby, roda com Docker ou Kubernetes, e tem edição comunitária e paga.

## Quando usar

- Um contrato que exige relatório de cronograma ou de horas num formato formal.

## Quando não usar

- Gestão interna de um estúdio de duas pessoas: o [[fluxo-issue-pr]] com GitHub Projects já resolve, sem servidor extra.

## Como usar (se o gatilho aparecer)

1. Use a versão hospedada de teste ou suba com o `openproject-docker-compose` oficial, só para aquele cliente.
2. Mantenha o GitHub como fonte da verdade do código e espelhe só o cronograma.

## Ver também

- [[fluxo-issue-pr]] · [[open-source-self-hosted-triagem]] · [[categoria-produtividade]]

## Fontes

- [opf/openproject](https://github.com/opf/openproject)
