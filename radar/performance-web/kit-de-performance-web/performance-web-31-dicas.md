---
titulo: "Performance web — triagem das 31 dicas do reel e o kit universal"
resumo: "As 31 dicas de performance do reel (@gustagoat.ai), validadas uma a uma e separadas em kit universal (padrão em qualquer projeto), condicionais (só com gatilho medido), já feitas pela plataforma (só verificar) e medição (vem primeiro). Virou a skill performance-web."
tipo: conceito
dominio: radar
tags: [murilo/engenharia, performance, frontend, backend, banco-de-dados]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: performance-web
natureza: skill
quando_usar: "Ao escrever código web (modo padrão da skill performance-web) e quando algo estiver lento (modo auditoria, medindo primeiro)."
quando_nao_usar: "Aplicar as 31 dicas de uma vez; Redis, fila ou balanceador sem sintoma medido."
pre_requisito: "Skill performance-web (já criada); para auditoria, o app rodando."
---

# Performance web — triagem das 31 dicas do reel e o kit universal

## 📌 Resumo

O reel (@gustagoat.ai) lista 31 "pedidos" para o Claude não deixar um app feito com IA lento. Termina com o funil "comenta GOAT que eu te mando o kit". **Quase todas as dicas são técnicas reais e corretas.** O problema é o formato: elas vêm como uma lista para aplicar de uma vez, misturando três tipos diferentes de dica:

1. **Padrão barato**, que deveria estar em qualquer projeto desde o primeiro dia.
2. **Remédio para um gargalo específico** (Redis, fila, balanceador). Aplicado sem o gargalo, é overengineering puro ([[adocao-de-ferramenta]], escada do [[ponytail]]).
3. **Medição**, que aparece no fim da lista (18, 30, 31) mas deveria vir **primeiro**: sem medir, você otimiza o que não está lento.

> 💡 **Analogia:** uma caixa de remédios com 31 itens. Vitamina e protetor solar você usa todo dia. Antibiótico só com diagnóstico. E o termômetro vem antes de tudo.

## 🧠 1. As 31 dicas, validadas

**Legenda:** ✅ **Universal** (padrão em qualquer projeto) · 🔶 **Condicional** (só com gatilho) · ☁️ **Plataforma já faz** (Vercel/Next: só verificar) · 📏 **Medição**

| # | Dica (tag no vídeo) | Veredito | Quando / armadilha |
| --- | --- | --- | --- |
| 01 | Skeleton de carregamento (frontend) | ✅ | Melhora a percepção de velocidade. **Armadilha:** um skeleton com tamanho diferente do conteúdo causa *layout shift* (piora o CLS). Em Next, use `loading.tsx` e Suspense. |
| 02 | Imagens em WebP/AVIF + `srcset` (rede) | ✅ | Em Next, o `next/image` já faz. O erro comum é usar `<img>` cru ou não informar as dimensões. |
| 03 | Evitar chamadas duplicadas na API (api) | ✅ | Use a biblioteca de dados que o projeto já tem (TanStack Query, SWR, `fetch` com cache do Next). Não escreva deduplicação à mão. |
| 04 | Debounce na busca e no autocompletar (frontend) | ✅ | Entre 250 e 400 ms, e cancele a requisição anterior (AbortController). |
| 05 | Paginar resultados da API (api) | ✅ | Toda lista que cresce com o uso. Use `range()` no Supabase e cursor quando a lista for grande. |
| 06 | Estáticos por CDN (rede) | ☁️ | A Vercel já serve pela CDN. Só importa se fizer self-host. |
| 07 | Tarefas lentas para uma fila (backend) | 🔶 | **Gatilho:** a ação passa de alguns segundos ou depende de um terceiro (relatório, envio em massa). Antes do Redis, veja se o Supabase resolve. Ver [[cache-e-fila]]. |
| 08 | Corrigir consultas N+1 (banco) | ✅ | Busque a relação junto (`select('*, servico(*)')` no Supabase) em vez de fazer um loop de consultas. |
| 09 | Compressão Brotli/Gzip (rede) | ☁️ | A Vercel e a CDN já comprimem. Confira o header `content-encoding`. |
| 10 | Cache em Redis dos dados mais consultados (backend) | 🔶 | **Gatilho:** uma consulta medida como lenta **e** muito repetida. Cache traz bug de invalidação (dado velho). Primeiro índice e cache do Next, Redis por último ([[cache-e-fila]]). |
| 11 | Remover dependências não usadas (frontend) | ✅ | Knip no CI ([[qualidade-automatizada]]). Também vale trocar lib pesada por nativo (`moment` → `Intl`), como manda a escada do Ponytail. |
| 12 | Timeout nas APIs externas (api) | ✅ | `AbortSignal.timeout(ms)` em todo `fetch` externo. É mais resiliência que velocidade: evita requisição pendurada para sempre. |
| 13 | Streaming da resposta de IA token por token (api) | 🔶 | **Gatilho:** o app mostra resposta de LLM. Nesse caso é obrigatório: a primeira palavra chega na hora. |
| 14 | Atualizar a tela sem esperar o servidor (optimistic UI) (frontend) | 🔶 | Para ações frequentes e reversíveis (curtir, marcar, reordenar). **Nunca** em ação transacional: no Encaixe, confirmar agendamento antes do servidor mostra um horário que pode já ter sido tomado. |
| 15 | Lazy loading nas imagens fora da tela (frontend) | ✅ | Use `loading="lazy"` (o `next/image` já usa por padrão). **Armadilha:** **nunca** na imagem principal acima da dobra (a do LCP). Ela deve ser prioritária, senão o LCP piora. |
| 16 | Requisições independentes em paralelo (api) | ✅ | `Promise.all` em vez de vários `await` em sequência. Um dos ganhos mais baratos que existem. |
| 17 | Índices para as consultas mais comuns (banco) | ✅📏 | Com evidência: rode `EXPLAIN ANALYZE` e use o *index advisor* e as estatísticas de consulta do Supabase. Índice sem consulta lenta só custa escrita. |
| 18 | Rastrear requisições lentas com OpenTelemetry (medição) | 📏 | Já é o caminho do [[adr-001-observabilidade]] (Sentry via OTel). É isso que diz **qual** das outras dicas aplicar. |
| 19 | Servidor perto do banco (backend) | ✅ | Configuração de uma vez: a região das functions na Vercel igual à região do Supabase (para o Brasil, São Paulo nos dois). Região errada soma latência a **cada** consulta. |
| 20 | Renderizar no servidor ou no build (backend) | 🔶 | Decisão por página: conteúdo estático vai no build, dado por usuário no servidor, e interação pesada no cliente. O Next já oferece os três. Não é "sempre SSR". |
| 21 | Scripts de terceiros depois da página (frontend) | ✅ | `next/script` com `afterInteractive` ou `lazyOnload` para analytics, chat e anúncios. |
| 22 | Dividir o JavaScript por página (frontend) | ☁️✅ | Next e Vite já dividem por rota. O que sobra fazer é `dynamic import` em componente pesado (editor, gráfico, mapa). |
| 23 | Virtualizar listas longas (frontend) | 🔶 | **Gatilho:** centenas ou milhares de itens na tela **depois** de paginar. A paginação (05) costuma resolver antes. |
| 24 | Pedir só as colunas necessárias (banco) | ✅ | Liste as colunas no `select` em vez de `*`. Reduz tráfego e evita expor coluna sensível. |
| 25 | Pool de conexões (banco) | ✅ | Em serverless com Postgres, use a string de conexão do pooler do Supabase (modo *transaction*). **[PROVÁVEL]** Conexão direta de cada function esgota as conexões do banco. |
| 26 | Evitar re-render desnecessário (frontend) | 🔶📏 | Meça primeiro com [[react-scan]] ou [[react-doctor]]. Não espalhe `useMemo`: com o React Compiler, boa parte da memoização é automática. |
| 27 | Cache de estáticos no navegador (rede) | ☁️ | Next e Vite geram arquivos com hash e cache longo. Confira o `Cache-Control` só em asset servido à mão. |
| 28 | Distribuir o tráfego entre instâncias (backend) | ☁️ | Serverless (Vercel) já escala horizontalmente. Só faz sentido com servidor próprio. |
| 29 | Hospedar as fontes e limitar os pesos (frontend) | ✅ | `next/font` (self-host automático) e no máximo 2 pesos por família. |
| 30 | Monitorar a velocidade dos usuários reais (medição) | 📏 | É o *RUM*: Core Web Vitals no p75 de usuários reais (Vercel Speed Insights, Sentry ou PostHog). O seu Mac rápido não é o seu usuário. |
| 31 | Testar no celular em rede lenta (medição) | 📏 | No DevTools, simule um celular com CPU 4x mais lenta e rede *Slow 4G*, ou rode o Lighthouse mobile. Para o público do Encaixe (celular, 4G), esse é o teste que importa. |

**Contagem:** 16 universais · 7 condicionais · 5 que a plataforma já faz (06, 09, 22, 27 e 28; a 22 também tem uma parte universal) · 4 de medição (17, 18, 30, 31, com a 17 e a 26 dependendo de medição). Nenhuma é falsa. O risco está em aplicar as condicionais sem gatilho e em pular a medição.

## ⚠️ 2. Onde a lista pode piorar o app

- **Lazy loading em tudo (15):** a imagem principal fica lazy e o LCP piora.
- **Skeleton com tamanho errado (01):** o conteúdo "pula" quando carrega e o CLS piora.
- **Optimistic UI em transação (14):** mostra sucesso que o servidor depois nega (horário já ocupado, pagamento recusado).
- **Redis e fila sem gatilho (07, 10):** um serviço a mais e bugs de invalidação, em MVP sem tráfego.
- **Memoização espalhada (26):** mais código e mais bug de dependência, para um ganho que ninguém mediu.
- **"Claude, aplique os 31":** um diff enorme, impossível de revisar ([[fluxo-issue-pr]]), em que nenhuma mudança tem medição de antes e depois.

## ✅ 3. O kit universal (vale em qualquer projeto Next/React + Supabase)

Agrupado por **quando** se aplica:

| Momento | Itens | Como fica no dia a dia |
| --- | --- | --- |
| **Uma vez, ao criar o projeto** | 19 região · 25 pooler · 29 fontes · 21 scripts de terceiros · 11 Knip no CI | Checklist de setup, 30 minutos |
| **Sempre, ao escrever código** | 02/15 `next/image` (com prioridade no LCP) · 16 `Promise.all` · 12 timeout · 24 colunas explícitas · 08 sem N+1 · 05 paginação · 04 debounce · 03 lib de dados existente · 01 skeleton com o tamanho certo · 22 `dynamic import` no que é pesado | Regras de escrita, como a `clean-code` |
| **Antes de release / em auditoria** | 31 teste mobile em rede lenta · 30 RUM no p75 · 17 `EXPLAIN` nas consultas lentas · 18 traces lentos | Relatório com medição de antes e depois |
| **Só com gatilho medido** | 07 fila · 10 Redis · 13 streaming (se tiver IA) · 14 optimistic (só ação reversível) · 20 estratégia de render · 23 virtualização · 26 re-render | Tabela "sintoma medido → remédio" |
| **Não fazer (a plataforma já faz)** | 06 CDN · 09 compressão · 27 cache de estáticos · 28 balanceador | Só verificar uma vez |

## 🧩 4. Skill `performance-web` (criada em 2026-11-09)

✅ Criada em [performance-web](../../../agentes/skills/performance-web/SKILL.md), com `checklist-setup.md`, `sintoma-remedio.md` e `auditoria-medicao.md` em `references/`. Ao escrever a skill, conferi três detalhes na documentação:

- no Next 16, o `priority` do `next/image` virou `preload`, e a doc também aponta `loading="eager"` e `fetchPriority="high"`;
- o pooler do Supabase em *transaction mode* usa a porta 6543 e exige desligar *prepared statements*;
- a região São Paulo é `gru1` na Vercel e `sa-east-1` no Supabase.

O desenho original segue abaixo.

**Por que uma skill e não só esta nota:** as regras de escrita precisam estar presentes **enquanto o agente escreve código**, do mesmo jeito que a `clean-code`. Esta nota é para você consultar. A skill é para o agente aplicar.

**Formato proposto**, enxuto e no padrão das suas skills:

```text
agentes/skills/performance-web/
├── SKILL.md                       # 2 modos + portões; ~80 linhas
└── references/
    ├── checklist-setup.md         # itens "uma vez" (19, 25, 29, 21, 11) com comando de verificação
    ├── sintoma-remedio.md         # condicionais: sintoma medido → remédio → armadilha
    └── auditoria-medicao.md       # como medir: Lighthouse mobile, RUM p75, EXPLAIN, traces
```

- **Modo padrão (silencioso, ao escrever):** as regras de "sempre, ao escrever código", com as armadilhas (LCP nunca lazy, skeleton com o tamanho certo, optimistic só em ação reversível).
- **Modo auditoria (quando pedir "audite a performance"):** **medir primeiro** (itens 31, 30, 17, 18), listar os 3 maiores gargalos com número, propor o remédio da tabela sintoma → remédio e entregar um relatório com antes e depois. Nunca aplicar os 31 de uma vez.
- **Portões:** item condicional só entra com o sintoma medido citado. Itens que a plataforma já faz viram verificação, não código.
- **Disparo:** descrição voltada para "escrever ou revisar front-end/API/consulta" e para pedidos explícitos ("está lento", "performance", "Core Web Vitals"). O detalhe fica em `references/` para não pesar no contexto.
- **Relação com o que existe:** complementa a `clean-code` (escrita), [[react-scan]] e [[react-doctor]] (diagnóstico de render) e [[qualidade-automatizada]] (Knip). Não duplica nenhuma.

**Quando criar:** quando for começar ou retomar um projeto front-end (Encaixe, site institucional). **Status:** só proposta.

## 🔗 Ver também

- [[adocao-de-ferramenta]] · [[ponytail]] · [[skills-de-qualidade-de-codigo]]
- [[cache-e-fila]] · [[adr-001-observabilidade]] · [[qualidade-automatizada]]
- [[react-scan]] · [[react-doctor]] · [[backend-como-servico]]

## 📚 Fontes

- Vídeo do reel de @gustagoat.ai ("31 pedidos" de performance), enviado pelo usuário em 2026-11-09. As dicas foram lidas nos frames do vídeo (78 s). O áudio não foi transcrito: não há modelo Whisper local, e baixar um precisaria de autorização.
- [Next.js — Image (preload, Next 16)](https://nextjs.org/docs/app/api-reference/components/image) · [Supabase — Connect to your database](https://supabase.com/docs/reference/postgres/connection-strings) · [Supabase — Disabling prepared statements](https://supabase.com/kb/troubleshooting/disabling-prepared-statements-qL8lEL) · [Vercel — Regions](https://vercel.com/docs/regions)
