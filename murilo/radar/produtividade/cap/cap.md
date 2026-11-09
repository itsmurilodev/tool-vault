---
titulo: "Cap — gravação de tela open source (alternativa ao Loom)"
resumo: "App nativo que grava a tela e gera link na hora (Instant) ou edita localmente (Studio). Guarda local, num bucket S3/R2 seu ou em self-host. AGPL, o que não pesa para uso próprio."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/produtividade, open-source, video, comunicacao]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: produtividade
natureza: ferramenta
quando_usar: "Demo para cliente, gravação de bug para a issue, explicação assíncrona de entrega, evidência humana num PR quando o screenshot não basta."
quando_nao_usar: "Self-host da plataforma inteira: o app desktop com armazenamento local ou bucket seu já resolve."
pre_requisito: "App desktop (macOS, Windows ou Linux)."
---

# Cap

> **Radar: ✅ adotar, quando precisar gravar.** Substitui o Loom sem prender o vídeo num fornecedor.

## O que é

`CapSoftware/Cap` (25 mil estrelas). Dois modos de gravação:

- ***Instant***: sobe enquanto grava e entrega o link na hora.
- ***Studio***: grava localmente e abre o editor (fundo, zoom, corte, legenda).

O armazenamento pode ser o Cap Cloud, um bucket seu (S3, R2, B2, MinIO) ou self-host completo. A licença é AGPL-3.0, com algumas *crates* em MIT. Usar internamente não gera obrigação.

## Quando usar

- Mostrar uma entrega ou demo para cliente sem marcar reunião.
- Gravar um bug e colar o link na issue.
- Mostrar um fluxo funcionando quando o screenshot no PR não basta.

## Quando não usar

- Para montar uma plataforma de vídeo self-hosted: não há dor que justifique.

## Como usar

1. Instale o app desktop.
2. Armazenamento local, ou um bucket R2/S3 seu se quiser link compartilhável sem o Cap Cloud.

## Ver também

- [[open-source-self-hosted-triagem]] · [[categoria-produtividade]]

## Fontes

- [CapSoftware/Cap](https://github.com/CapSoftware/Cap) (README e LICENSE)
