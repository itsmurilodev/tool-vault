---
titulo: "Windsor.ai — conector de dados de marketing com MCP (Instagram, TikTok, YouTube e 350+ fontes)"
resumo: "Conector no diretório do Claude que lê Insights do Instagram e publica posts. Testado em 2026-11-13: entrega taxa de pulo em 3 s, tempo médio, envios e alcance de não seguidores por Reel. Free cobre só 1 fonte (usada no Instagram)."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, redes-sociais, mcp, metricas]
status: ativo
atualizado: 2026-11-13
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: marketing-e-conteudo
natureza: plataforma
quando_usar: "Métricas por Reel do Instagram que a Metricool não entregar (taxa de pulo em 3 s, tempo médio, envios, alcance de não seguidores); cruzar redes com anúncios; analisar contas públicas de concorrentes."
quando_nao_usar: "Só para métricas dos próprios posts nas três redes: a Metricool faz isso no Free; o Free do Windsor cobre uma única fonte."
pre_requisito: "Instagram como conta Profissional; plano pago para mais de uma fonte."
---

# Windsor.ai

> **Radar: 🧪 testar.** Testado no Instagram do 05-Editor: traz as métricas de Reel que mais importam. Para três redes, é pago e concorre com a Metricool.

## Teste de 2026-11-13 (Instagram, conta itsmurilodev, plano Trial)

- **Funcionou:** por Reel, `media_views`, `media_reach`, `media_reel_avg_watch_time` (ms), `media_reel_skip_rate` (pulo em 3 s), `media_shares`, `media_saved`, curtidas e comentários; por dia, alcance e views de seguidores e não seguidores. Os números bateram com o perfil (V01: 1.539 views no Windsor, 1.537 no app horas antes).
- **Não veio:** `media_reposts` (conta conectada por Instagram Login; exige Facebook Login com Página); `media_follows` e `media_profile_visits` não existem para Reels; `follows_and_unfollows` vazio (provável mínimo de 100 seguidores).
- **Plano:** o cadastro abriu como **Trial**, não Free; `force_refresh` não está disponível no Trial (dados em cache).

## O que é

Plataforma de integração de dados de marketing (350+ fontes) com MCP no diretório do Claude (`https://mcp.windsor.ai/`, e variantes `/social_media` e `/paid_media`). Para Instagram, lê posts, Reels, Stories e seguidores, e tem **ações de escrita**: criar post, carrossel, story e vídeo, responder, ocultar e **apagar comentários**.

Preço, segundo o site do fornecedor: Free para **1 fonte, 1 conta, 1 usuário**; pagos a partir de US$ 19/mês (anual) para 3 fontes. Um blog terceiro (Coupler) aponta que o custo sobe com fontes e volume de linhas.

## Quando usar

- Relatório que cruze redes com anúncios (Meta Ads, Google Ads) ou com GA/Search Console.
- Análise de contas públicas de concorrentes no Instagram (conector "Instagram Public").

## Quando não usar

- Só para os próprios posts: Instagram + TikTok + YouTube já são 3 fontes, ou seja, plano pago.
- Junto com a Metricool: escolha um.

## Riscos e custos

- O conector tem permissão de **publicar e apagar**: manter a aprovação manual das ações.
- Preço por fonte e por volume de linhas: o custo cresce sem aviso [preço exato não verificado, INCERTO].

## Ver também

- [[metricool]] (concorrente) · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [Windsor.ai — Instagram MCP](https://windsor.ai/connect/instagram-mcp/) (lida em 2026-11-13)
- [Coupler — preço do Windsor.ai](https://blog.coupler.io/?p=86099)
- Diretório de conectores do Claude (registro MCP, consultado em 2026-11-13)
