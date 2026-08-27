---
titulo: "ADR 001 — Plataforma de observabilidade padrão"
resumo: "Sentry no free tier, instrumentado via OpenTelemetry, como padrão para projeto novo. Proposta."
tipo: decisao
dominio: async
tags: [adr, infra/observabilidade]
status: ativo
atualizado: 2026-08-10
---

# ADR 001 — Plataforma de observabilidade padrão

- **Data:** 2026-08-10
- **Status:** **proposta** — aguardando aceite
- **Escopo:** padrão para projeto próprio novo. Projeto de cliente segue o que for negociado com o cliente; ADR específica de um projeto mora no repositório daquele projeto, não aqui.

## Contexto

Hoje não existe padrão: cada projeto decide (ou não decide) observabilidade na hora do incidente, que é o pior momento possível. O sintoma concreto é o usuário relatar um erro que não se reproduz localmente e não haver de onde puxar stack trace, contexto de release ou frequência.

Restrições reais no momento da decisão:

- Produtos em MVP, pré-receita — não há verba recorrente para justificar plataforma paga.
- Duas pessoas no estúdio, com tempo dividido entre produto e prospecção. Setup e manutenção competem diretamente com desenvolvimento.
- Volume de erro e de tráfego ainda é desconhecido e vai mudar muito — qualquer estimativa de custo feita agora está errada.
- Existe chance real de precisar migrar de plataforma quando o volume crescer.

A última restrição é a que mais pesa: **a decisão precisa ser barata de reverter**, porque provavelmente vai ser revertida.

## Opções consideradas

### Opção A — Sentry no free tier, instrumentado via OpenTelemetry

- **A favor:** menor custo de setup da categoria; responde direto "quebrou onde e por quê"; cobrança por volume de evento é previsível; free tier na ordem de 5.000 eventos/mês cobre aplicação pequena; com OTel, a instrumentação não fica presa ao vendor.
- **Contra:** é rastreamento de erro, não APM full-stack — não responde "por que está lento" com a mesma profundidade; o free tier acaba rápido se a aplicação passar a errar muito.
- **Custo de reverter:** baixo, se a instrumentação for OTel. Trocar de plataforma vira mudança de configuração do Collector, sem tocar código de aplicação.

### Opção B — New Relic no free tier

- **A favor:** free tier objetivamente maior (100 GB de ingestão e um usuário full-platform); já é observabilidade full-stack, então não precisa trocar quando surgir necessidade de APM.
- **Contra:** superfície bem maior para configurar e entender; a maior parte do que ele oferece não tem uso neste estágio; um usuário só no plano gratuito trava colaboração assim que houver mais gente.
- **Custo de reverter:** baixo com OTel, igual à opção A.

### Opção C — não adotar nada ainda

- **A favor:** zero custo, zero manutenção, zero distração.
- **Contra:** é o estado atual, e ele já está cobrando — erro em produção que não se reproduz é exatamente o problema que motivou esta ADR.
- **Custo de reverter:** nenhum, mas o custo de *permanecer* cresce a cada usuário.

Datadog não entrou como opção: não tem free tier real (trial de 14 dias) e a cobrança em *high-water mark* torna o custo imprevisível justamente no estágio em que o volume é desconhecido.

## Decisão

**Opção A — Sentry no free tier, com instrumentação em OpenTelemetry sempre que a stack permitir.**

O trade-off determinante não é qualidade de produto, é **reversibilidade**. Sentry e New Relic resolvem o problema atual; a diferença é que o Sentry entrega isso com a menor superfície a configurar, e o OTel garante que a escolha entre os dois possa ser refeita depois sem reescrever instrumentação.

Regra derivada: **uma plataforma por projeto.** Não manter duas "para comparar".

## Consequências

**Positivas**
- Erro de produção passa a ter stack trace, contexto e frequência, sem depender de reprodução local.
- Projeto novo já nasce com o padrão, sem discussão a cada vez.
- A decisão de plataforma fica isolada atrás do OTel.

**Negativas / dívida aceita**
- Sem APM profundo: pergunta de performance ("por que está lento") continua sem resposta boa por enquanto.
- Instrumentar com OTel custa mais que colar o SDK do vendor. É o preço da reversibilidade, e está sendo pago de propósito.
- Free tier tem teto. Aplicação que errar muito vai estourar o limite — e isso é sinal de problema, não só de plano pequeno.

**O que passa a ser obrigatório**
- Projeto novo configura rastreamento de erro antes do primeiro deploy com usuário real.
- Alerta só para o que muda o comportamento de alguém. Alerta que ninguém age treina o time a ignorar alerta.
- Nada de SDK proprietário de vendor onde OTel resolver.

## Quando revisitar

Qualquer um destes sinais:

- Estouro recorrente do free tier do Sentry.
- Primeira pergunta séria de performance que o rastreamento de erro não responde.
- Entrada de receita recorrente que justifique custo fixo de observabilidade.
- Mais de um serviço em produção precisando de correlação entre eles.

## Ver também

- [[observabilidade]] — a análise comparativa que embasa esta decisão.
- [[adocao-de-ferramenta]] — o portão de estágio aplicado aqui.
- Skill [decisao-arquitetural](../../murilo/ia/agentes/claude/skills/decisao-arquitetural/SKILL.md) — o método usado para escrever esta ADR.
