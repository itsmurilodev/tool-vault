---
titulo: "Analytics de produto — PostHog"
resumo: "PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação."
tipo: referencia
dominio: infra
tags: [infra/analytics, custo, produto]
status: ativo
atualizado: 2026-08-11
---

# Analytics de produto — PostHog

## 📌 Resumo

PostHog mede o que usuário real faz dentro do produto: quais telas usa, onde abandona, quais funcionalidades pega ou ignora. Isso não é infraestrutura de escala como Redis ou banco vetorial — é o instrumento que produz o dado que a estratégia de "rodar de graça até validar dor real" já pressupõe ter. Sem isso, "dor real" vira relato informal, não dado.

## 🧠 1. Free tier (2026)

| Produto | Limite |
| ------- | ------ |
| Eventos de analytics | 1.000.000/mês |
| Gravação de sessão (replay) | 5.000/mês |
| Feature flags | 1.000.000 de requisições/mês |
| Error tracking | 100.000 eventos/mês |
| Retenção de dado | 1 ano |

1 milhão de eventos/mês equivale a ~33 mil eventos/dia — generoso o bastante para uma base de 10 a 50 mil usuários ativos mensais rastreando as ações centrais, o que cobre folgadamente a fase de piloto do Encaixe.

## 🧠 2. Onde encaixa em cada produto

- **Encaixe:** funil de agendamento (visitou → escolheu horário → confirmou) revela em qual etapa o estabelecimento-piloto trava, sem precisar perguntar.
- **Async Hub:** uso do inbox multi-agente — qual canal (WhatsApp/Instagram) gera mais volume, quanto tempo até resposta — dado que hoje só existiria por observação manual.

## ⚠️ 3. Erro comum

Instrumentar tudo de uma vez ("autocapture" ligado sem critério) queima o orçamento de eventos rápido e gera ruído em vez de sinal. Definir 5-10 eventos-chave por produto (ex: `agendamento_confirmado`, `mensagem_recebida`) rende mais insight que capturar todo clique.

## ✅ Como aplicar

Adotar agora — item que passa direto no portão de [[adocao-de-ferramenta]] porque a dor que resolve (não saber onde o usuário trava) já dói hoje, custo zero no volume do piloto, e não compete com nada já adotado.

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão que este item passa sem ressalva.
- [[observabilidade]] — Sentry cobre "quebrou onde"; PostHog cobre "onde o usuário desistiu" — são complementares, não concorrentes.

## 📚 Fontes

- [PostHog Pricing 2026 — BudgetForge](https://www.budgetforge.dev/tools/posthog-pricing-2026)
- [PostHog Free Tier 2026 — AgentDeals](https://agentdeals.dev/vendor/posthog)
