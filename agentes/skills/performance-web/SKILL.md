---
name: performance-web
description: Aplica o kit de performance web do usuário (Next.js/React, rotas de API, Supabase/Postgres) — padrões baratos ao escrever código (imagens, fontes, scripts de terceiros, Promise.all, timeout, colunas explícitas, sem N+1, paginação, debounce) e, quando pedido, auditoria que mede antes de otimizar. Usar ao escrever ou revisar componente React/Next, página, rota de API, chamada a serviço externo ou consulta ao banco em projeto web, e SEMPRE que o usuário disser "está lento", "performance", "Core Web Vitals", "LCP", "otimiza o carregamento", "audite a performance". Não usar para script, CLI ou código sem interface/rede.
---

# Performance web — padrão do usuário

**Idioma:** comunicação com o usuário em português do Brasil, direta. Identificadores seguem o padrão do projeto.

**Princípio:** padrão barato sempre; remédio caro só com sintoma medido. Nunca aplicar uma lista inteira de otimizações de uma vez — cada mudança de performance precisa caber num diff revisável e, quando for remédio, ter número de antes e depois. Esta skill complementa a `clean-code` (a escada de decisão dela continua valendo: nada de dependência nova para ganhar milissegundos) e não a substitui.

Existem dois modos. Escolha um antes de agir.

## Modo padrão — ao escrever ou editar código (silencioso)

Aplique sem gerar relatório, como parte de escrever certo:

**Front-end**
- **Imagens:** use o componente de imagem do framework (`next/image`) com `width`/`height` ou `fill` + `sizes`; ele entrega WebP/AVIF, `srcset` e lazy loading. **A imagem principal acima da dobra (candidata a LCP) nunca é lazy:** marque como prioritária — no Next 16, `preload` (substituiu `priority`) ou `loading="eager"`/`fetchPriority="high"`; confira a prop na versão instalada. Uma por página, não várias.
- **Fontes:** `next/font` (hospeda junto, sem requisição externa), no máximo 2 pesos por família, `display: swap`.
- **Scripts de terceiros** (analytics, chat, pixel, anúncio): `next/script` com `strategy="afterInteractive"` ou `"lazyOnload"`. Nunca no `<head>` bloqueando a página.
- **Componente pesado** (editor rico, gráfico, mapa, player): `dynamic(() => import(...))` em vez de import estático na página.
- **Busca/autocompletar:** debounce de 250–400 ms e cancele a requisição anterior com `AbortController`.
- **Carregamento:** skeleton (`loading.tsx` / Suspense) **com as mesmas dimensões** do conteúdo final — skeleton de tamanho diferente faz a página pular (CLS).
- **Dados no cliente:** use a biblioteca de dados que o projeto já tem (TanStack Query, SWR, cache do `fetch` do Next) para deduplicar e cachear requisições. Não escreva deduplicação à mão.

**API / servidor**
- **Chamadas independentes em paralelo:** `await Promise.all([...])` em vez de `await` em sequência.
- **Todo `fetch` para serviço externo tem timeout:** `fetch(url, { signal: AbortSignal.timeout(ms) })`, com erro tratado (nada de requisição pendurada para sempre).
- **Listas que crescem com o uso são paginadas** (no Supabase, `.range(inicio, fim)`; cursor quando a lista for grande). Nunca devolver a tabela inteira.
- **Resposta de LLM para o usuário:** transmita em stream, nunca espere o texto completo.

**Banco (Supabase/Postgres)**
- **Colunas explícitas:** `.select('id, nome, avatar_url')`, não `.select('*')` — menos tráfego e não vaza coluna sensível.
- **Sem N+1:** relação vem na mesma consulta (`.select('*, servico(nome)')`) ou num `in(...)` só; nunca consulta dentro de loop.
- **Índice:** só proponha com a consulta lenta identificada (`EXPLAIN ANALYZE`); não crie índice "por via das dúvidas".

Se uma regra conflitar com padrão já estabelecido no projeto, siga o projeto e avise da inconsistência.

## Modo auditoria — "está lento", "audite a performance"

Ordem obrigatória: **medir → apontar gargalo → remédio → medir de novo.** Detalhe de cada medição em `references/auditoria-medicao.md`.

1. **Medir como o usuário real:** Lighthouse/DevTools em perfil mobile (CPU 4x mais lenta, rede Slow 4G) nas páginas principais; dados de usuário real (p75 de LCP, INP, CLS) se o projeto tiver Speed Insights/Sentry/PostHog. Registre os números.
2. **Rodar o checklist de setup** (`references/checklist-setup.md`): região, pooler, fontes, scripts de terceiros, dependências mortas, o que a plataforma já faz.
3. **Achar os 3 maiores gargalos com evidência** (trace lento, consulta no `EXPLAIN`, bundle grande, imagem LCP lenta). Sem número, não é gargalo.
4. **Propor o remédio pela tabela** `references/sintoma-remedio.md` — remédio condicional (cache, fila, virtualização, optimistic UI, mudança de estratégia de render, memoização) só entra com o sintoma medido citado.
5. **Aplicar um gargalo por vez**, cada um num diff pequeno, e medir de novo.

**Formato de saída obrigatório:**

```
## Medição inicial (como e números)
## Checklist de setup (ok / problema)
## Gargalos (top 3, com evidência)
## Remédios propostos (sintoma → remédio → risco)
## Aplicado nesta rodada + medição depois
## Fica para depois
```

**Restrições do modo auditoria:**
- Não adicionar serviço novo (Redis, fila, CDN extra) sem o sintoma medido e sem avisar o custo de manutenção.
- Não aplicar optimistic UI em ação transacional (agendamento, pagamento, estoque) — só em ação frequente e reversível.
- Não espalhar `useMemo`/`useCallback`/`memo` sem medição de re-render (React Scan / React DevTools Profiler); com React Compiler, boa parte é automática.
- Não otimizar o que a plataforma já faz (CDN, compressão, cache de asset com hash, balanceamento na Vercel) — só verificar.
- Não declarar ganho sem número de antes e depois.

## Referências (abrir só quando precisar)

- `references/checklist-setup.md` — itens de uma vez por projeto, com como verificar cada um.
- `references/sintoma-remedio.md` — remédios condicionais: sintoma medido → remédio → armadilha.
- `references/auditoria-medicao.md` — como medir: Lighthouse mobile, usuário real (p75), `EXPLAIN ANALYZE`, traces, bundle.
