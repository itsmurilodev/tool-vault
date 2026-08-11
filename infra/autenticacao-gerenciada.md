---
titulo: "Autenticação gerenciada — Clerk vs Supabase Auth"
resumo: "Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade."
tipo: referencia
dominio: infra
tags: [infra/autenticacao, custo, decisao]
status: ativo
atualizado: 2026-08-11
---

# Autenticação gerenciada — Clerk vs Supabase Auth

## 📌 Resumo

Clerk e Supabase Auth resolvem o mesmo problema (login, sessão, MFA, SSO) com modelos de free tier parecidos. A pergunta que importa não é "qual é melhor" — é **se você já pagou pela outra**. Encaixe já decidiu Supabase (ADR de auth+DB); adicionar Clerk ali é um segundo provedor de identidade sem ganho técnico, só mais uma peça pra manter sincronizada.

> ⚠️ Isso não é uma crítica ao Clerk. É reconhecer que "ferramenta boa" e "ferramenta que soma ao que já existe" são perguntas diferentes — ver [[adocao-de-ferramenta]].

## 🧠 1. Onde os dois empatam

| | Clerk | Supabase Auth |
| - | ----- | -------------- |
| Free tier | 50.000 MRU (retido, não ativo) por app — mudou de 10k pra 50k em fev/2026 | 50.000 MAU (ativo) por organização |
| UI de login pronta | Sim, componentes React prontos | Não nativamente — se monta a UI |
| MFA | Incluso no free | Incluso |
| Multi-tenant / organizações | Nativo, mas add-on B2B custa $100/mês extra no Pro | Modelagem própria via `tenant_id`, sem custo adicional |

A diferença MRU vs MAU importa pouco em escala pequena — MRU é mais rigoroso (só conta quem volta 24h+ depois do cadastro), então o teto real do Clerk costuma ser um pouco mais folgado na prática, não menos.

## 🧠 2. Onde Clerk ganharia, se fosse decisão nova

- **Componentes de UI prontos** economizam tempo de setup quando não existe ainda nenhuma decisão de banco — não é o caso do Encaixe.
- **B2B nativo** (convite de organização, papéis, SSO por cliente) é mais maduro no Clerk — mas custa $100/mês (organizations) + $75/mês por conexão SSO extra no Pro. Isso só se paga se o produto vender para empresas com exigência de SSO, o que ainda não é um requisito descrito para Encaixe ou Async Hub.

## ⚠️ 3. O custo escondido de trocar agora

Adicionar Clerk ao Encaixe não seria "somar uma opção" — seria migrar de auth já implementado (Supabase, com RLS provavelmente amarrado à `auth.uid()` do Postgres) para um provedor externo, reescrevendo a política de acesso a dado. É decisão **cara de reverter**, o critério que a skill `decisao-arquitetural` usa pra exigir ADR formal antes de mudar.

## ✅ Como aplicar

| Situação | Escolha |
| -------- | ------- |
| Projeto já usa Supabase para DB | Supabase Auth — evita segundo vendor e RLS já integra nativamente |
| Projeto novo, sem banco decidido, precisa de UI de login rápida | Clerk pode justificar o setup mais rápido |
| Cliente exige SSO corporativo específico | Reavaliar Clerk Pro/Business no momento em que esse requisito aparecer, não antes |

Para Encaixe e Async Hub: manter Supabase Auth. Reavaliar só se aparecer um requisito de SSO/organização que o modelo atual de `tenant_id` não cobrir — sinal concreto, não hipotético.

## 🔗 Ver também

- [[backend-como-servico]] — o teto do Supabase como um todo, não só o Auth.
- [[adocao-de-ferramenta]] — por que "soma ou substitui" é a pergunta certa antes de qualquer uma dessas duas.

## 📚 Fontes

- [Clerk Pricing Explained 2026](https://clerk.com/articles/clerk-pricing-explained)
- [Clerk Pricing in 2026 — BudgetForge](https://www.budgetforge.dev/tools/clerk-pricing-2026)
- [Clerk Pricing Update — 50k Free MAU](https://saasprices.net/blog/clerk-free-plan-changes)
