# Sintoma medido → remédio

Remédios condicionais. Cada um só entra quando o sintoma da primeira coluna foi **medido** (número, trace, `EXPLAIN`, profiler). Sem o sintoma, o remédio é custo sem benefício.

| Sintoma medido | Remédio | Armadilha / quando NÃO usar |
| --- | --- | --- |
| Consulta aparece lenta no trace ou no `EXPLAIN ANALYZE` com *Seq Scan* em tabela grande | **Índice** na coluna do filtro/ordenação (o *index advisor* do Supabase sugere) | Índice custa em toda escrita. Não indexar tabela pequena nem coluna pouco filtrada. |
| Mesma consulta lenta, já indexada, repetida muitas vezes com o mesmo resultado | **Cache**: primeiro o cache do próprio framework (`fetch`/`unstable_cache`/revalidação no Next), depois Redis (Upstash) | Cache traz dado velho e bug de invalidação. Defina quando o dado expira antes de cachear. Redis é mais um serviço para manter. |
| Ação do usuário espera vários segundos por trabalho que não precisa terminar na hora (relatório, envio em massa, processamento de arquivo, chamada lenta a terceiro) | **Fila / job em segundo plano**: responder rápido e processar depois, avisando o usuário quando terminar | Não usar para o que o usuário precisa ver na hora. Não adicionar fila para tarefa que já leva menos de ~1 s. |
| Ação frequente e reversível (curtir, marcar, reordenar, favoritar) parece lenta mesmo com API rápida | **Optimistic UI**: atualizar a tela antes da resposta e desfazer se falhar | **Nunca** em ação transacional: agendamento (horário pode ter sido tomado), pagamento, estoque, permissão. Ali o usuário precisa da confirmação real. |
| Lista com centenas/milhares de itens renderizados trava a rolagem, **mesmo depois de paginar** | **Virtualização** (TanStack Virtual / react-window): desenha só o que está visível | Paginação resolve a maioria dos casos antes. Virtualização complica busca no navegador, acessibilidade e altura variável. |
| Profiler (React Scan / React DevTools) mostra componente re-renderizando sem mudança visível e custando tempo | **Memoização pontual** (`memo`, `useMemo`, `useCallback`) ou mover estado para mais perto de onde é usado | Com React Compiler ativo, boa parte é automática. Memoizar sem medição adiciona código e bug de dependência. Mover estado costuma resolver melhor que memoizar. |
| Página de conteúdo igual para todos demora no primeiro carregamento | **Renderizar no build** (estático/ISR) | Não para dado por usuário. |
| Página com dado por usuário mostra tela vazia e depois carrega tudo no cliente | **Renderizar no servidor** (Server Components / SSR) com streaming e Suspense | Não mover para o servidor interação que precisa de resposta instantânea no cliente. |
| Resposta de LLM demora para aparecer | **Streaming** token a token | — (se o app mostra resposta de IA, é padrão, não remédio). |

**Regra:** um remédio por vez, num diff próprio, com medição antes e depois. Se o número não melhorou, desfaça.
