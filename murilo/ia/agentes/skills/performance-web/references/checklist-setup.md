# Checklist de setup — uma vez por projeto

Itens que se configuram uma vez e valem para todas as páginas. Verifique antes de qualquer otimização de código: um item errado aqui anula ganhos feitos no código.

| Item | Por que importa | Como verificar | Como corrigir |
| --- | --- | --- | --- |
| **Região do servidor = região do banco** | Cada consulta paga a distância de ida e volta. Função nos EUA com banco em São Paulo soma latência em **toda** consulta. | Região do projeto no painel do Supabase; região das funções no painel da Vercel (Settings → Functions) ou `regions` no `vercel.json`. | Mesma região nos dois. Para público brasileiro: Supabase `sa-east-1` (São Paulo) e Vercel `gru1` (São Paulo). |
| **Pooler de conexões em serverless** | Função serverless abre conexão nova a cada execução; conexão direta ao Postgres esgota o limite do banco sob carga. | String de conexão usada por ORM/driver (`DATABASE_URL`). Quem usa só `supabase-js` (HTTP/PostgREST) não precisa disso. | Supavisor em **transaction mode** (porta `6543`, botão *Connect → Transaction pooler* no painel). **Desligue prepared statements** no driver/ORM (Prisma: `?pgbouncer=true`; Drizzle/postgres-js: `prepare: false`). Migrações rodam pela conexão de sessão (`5432`) ou direta. |
| **Fontes hospedadas, poucos pesos** | Fonte externa é requisição bloqueante a outro domínio; cada peso é um arquivo. | Procurar `fonts.googleapis.com` / `<link>` de fonte no código; contar pesos importados. | `next/font` com só os pesos usados (máx. 2 por família). |
| **Scripts de terceiros fora do caminho crítico** | Analytics/chat/pixel no `<head>` atrasam a página toda. | Procurar `<script src=` e snippets colados em layout. | `next/script` com `afterInteractive` ou `lazyOnload`. |
| **Dependências mortas** | Peso no bundle e superfície de ataque sem uso. | `npx knip` (arquivos, exports e dependências não usados). | Remover; trocar lib pesada por nativo quando der (`moment` → `Intl`/`date-fns`, `lodash` → nativo). |
| **Bundle por rota** | Uma página não deve carregar o JS de outra. | `next build` mostra o tamanho por rota; `@next/bundle-analyzer` para ver o que pesa. | Next/Vite já dividem por rota; mover componente pesado para `dynamic import`. |
| **O que a plataforma já faz (só verificar)** | Evita reimplementar CDN, compressão e cache. | Na resposta de um asset: header `content-encoding: br` ou `gzip`; `cache-control` longo em arquivo com hash; servido pela CDN da Vercel. | Nada a fazer na Vercel. Só se for self-host: configurar CDN, compressão e cache no servidor/proxy. |

## Itens que NÃO se configuram em projeto Vercel serverless

- **Balanceador de carga entre instâncias:** a plataforma escala sozinha. Só relevante com servidor próprio (VPS, container).
- **CDN para estáticos:** já incluída.
