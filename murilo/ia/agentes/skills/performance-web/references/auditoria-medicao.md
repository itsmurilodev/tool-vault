# Como medir

Medição vem antes de qualquer remédio. Registre como mediu (ferramenta, página, perfil de dispositivo) para que a medição depois seja comparável.

## 1. Como o usuário real vê (laboratório)

- **Lighthouse mobile** (DevTools → Lighthouse → Mobile) ou PageSpeed Insights, nas 2–3 páginas mais usadas. O perfil mobile já simula CPU lenta e rede ruim.
- **DevTools manual:** Performance → CPU *4x slowdown*; Network → *Slow 4G*. Navegue o fluxo principal e observe quando o conteúdo útil aparece.
- **Métricas que importam** (Core Web Vitals, alvo "bom"):
  - **LCP** (maior conteúdo visível) ≤ 2,5 s
  - **INP** (resposta à interação) ≤ 200 ms
  - **CLS** (estabilidade do layout) ≤ 0,1
- Rode 2–3 vezes e use a mediana; um único resultado varia muito.

## 2. Usuário real (campo)

- Se o projeto tem Vercel Speed Insights, Sentry ou PostHog com web vitals: use o **p75** por página (75% dos usuários têm experiência igual ou melhor). O computador do desenvolvedor não representa o usuário.
- Sem ferramenta de campo, diga isso no relatório e use só o laboratório.

## 3. Servidor e banco

- **Traces** (Sentry/OpenTelemetry): abra as requisições mais lentas e veja qual trecho domina (consulta, API externa, render). É isso que escolhe o remédio.
- **Consultas:** `EXPLAIN ANALYZE <consulta>` no SQL editor do Supabase. Procure *Seq Scan* em tabela grande, tempo alto e linhas estimadas vs reais muito diferentes. O painel de *Query Performance* / *index advisor* do Supabase lista as consultas mais caras.
- **API externa:** meça o tempo da chamada isolada; se dominar o trace, o remédio é timeout + cache ou fila, não código local.

## 4. Bundle

- `next build` mostra o JS inicial por rota.
- `@next/bundle-analyzer` mostra quais dependências pesam.
- `npx knip` lista dependências e exports não usados.

## 5. Render no React

- **React Scan** (overlay de re-render) ou **React DevTools Profiler**: grave a interação lenta e veja quais componentes renderizam e quanto custam. Ver também a skill `react-doctor`.

## Registro no relatório

Para cada número: página/rota, ferramenta, perfil (mobile/desktop, rede), valor antes, valor depois. Ganho sem número de antes e depois não conta.
