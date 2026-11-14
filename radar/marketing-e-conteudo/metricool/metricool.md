---
titulo: "Metricool — gestor de redes com MCP oficial (Instagram, TikTok e YouTube no mesmo lugar)"
resumo: "Analíticas e agendamento de Instagram, TikTok e YouTube com MCP oficial no diretório do Claude; MCP liberado no plano Free (30 dias de histórico). Testar para preencher as métricas D+1/D+7 do 05-Editor."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, redes-sociais, mcp, metricas]
status: ativo
atualizado: 2026-11-13
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: marketing-e-conteudo
natureza: plataforma
quando_usar: "Coletar métricas D+1 e D+7 dos posts do 05-Editor nas três redes (Instagram, TikTok, YouTube) sem copiar número à mão, somente leitura pelo MCP."
quando_nao_usar: "Para agendar posts enquanto o Buffer for o canal de postagem (seriam dois agendadores); para retenção segundo a segundo, que só existe no app de cada rede."
pre_requisito: "Instagram como conta Profissional (Criador ou Empresa) e as três redes conectadas na Metricool."
---

# Metricool

> **Radar: 🧪 testar.** É a opção que resolve a dor já registrada no 05-Editor (nenhum post tem métricas) com custo zero e um só conector para as três redes.

## O que é

SaaS espanhol de gestão de redes sociais (analíticas, planner, inbox, anúncios). Tem **MCP oficial** (`https://ai.metricool.com/mcp`, OAuth) listado no diretório de conectores do Claude, com 7 ferramentas: `getAnalyticsAvailableMetrics`, `getAnalyticsDataByMetrics`, `getBestTimeToPostByNetwork`, `getBrandSettings`, `getScheduledPosts`, `createScheduledPost` e `updateScheduledPost`.

Fatos verificados na central de ajuda (lida em 2026-11-13):

- O MCP funciona em **qualquer plano, incluindo o Free**; a API da Metricool é outro produto (só Advanced/Custom).
- Plano Free: **30 dias de histórico de analíticas** e no máximo 20 posts agendados por mês.
- Pelo MCP **não** há Inbox, comentários nem gestão de campanhas de anúncios.
- A tela de permissões do OAuth é **mais ampla** do que o MCP usa (aviso da própria Metricool).

## Quando usar

- Fechar D+1 e D+7 das fichas em `05-Editor/publicados/` para Instagram, TikTok e YouTube de uma vez.
- Perguntar "qual post teve mais envios por alcance" sem abrir três apps.

## Quando não usar

- Como agendador junto com o Buffer: escolha um. Hoje o Buffer já está integrado aos scripts (`postar_buffer.py`).
- Para curva de retenção e taxa de quem pula o vídeo: isso continua só nos Insights do app.

## Como usar

1. Conta Free, conectar Instagram, TikTok e YouTube na Metricool.
2. Adicionar o conector Metricool no Claude e manter a aprovação das ferramentas que escrevem (`createScheduledPost`, `updateScheduledPost`).
3. Rodar `getAnalyticsAvailableMetrics` e conferir quais métricas de Reels existem (tempo médio, envios, salvamentos) antes de confiar no fluxo.
4. Comparar com o app em um post; se bater, usar em D+7.

## Riscos e custos

- Free cobre o teste; preço dos planos pagos não verificado [INCERTO].
- Histórico: não verificado se posts publicados **antes** da conexão entram nas analíticas [INCERTO].
- Métricas de Reels expostas pelo MCP não verificadas [INCERTO].

## Ver também

- [[windsor-ai]] (concorrente) · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [Limites do MCP e requisitos do plano](https://help.metricool.com/mcp-limits-and-plan-requirements-h72jg) (lida em 2026-11-13)
- [FAQ do MCP da Metricool](https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0) (lida em 2026-11-13)
- Diretório de conectores do Claude (registro MCP, consultado em 2026-11-13)
