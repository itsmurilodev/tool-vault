---
titulo: "Supabase como backend-as-a-service — o teto real do free tier"
resumo: "500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase."
tipo: referencia
dominio: infra
tags: [infra/banco-de-dados, custo, supabase]
status: ativo
atualizado: 2026-08-11
---

# Supabase como backend-as-a-service — o teto real do free tier

## 📌 Resumo

Supabase empacota Postgres, Auth, Storage, Realtime e Edge Functions num único free tier. É a base padrão para Encaixe e Async Hub. O free tier **é real e generoso**, mas tem tetos concretos — e um deles (pausa por inatividade) é mais perigoso na fase de validação do que o limite de espaço.

> ⚠️ O reel que fala em "$0/mês para rodar startup" está certo sobre o Supabase especificamente, mas esconde a armadilha: o teto que mais derruba projeto em validação não é armazenamento, é a **pausa automática**.

## 🧠 1. Limites do free tier (2026)

| Recurso | Limite |
| ------- | ------ |
| Banco de dados | 500 MB (Postgres, dados + índices) |
| Usuários ativos mensais (Auth) | 50.000 MAU |
| Armazenamento de arquivo | 1 GB |
| Egress (banda) | 5 GB descoberto + 5 GB cacheado |
| Edge Functions | 500.000 invocações/mês |
| Conexões Realtime simultâneas | 200 |
| Projetos ativos | 2 por organização |
| Backup automático | Nenhum |

## ⚠️ 2. A armadilha real não é o espaço

Projeto free **pausa depois de 7 dias sem requisição**. Isso é o que trava um projeto em validação de mercado — se o Encaixe ficar uma semana sem uso real (fim de semana prolongado, cliente-piloto de férias), o projeto para até alguém entrar no painel e reativar manualmente.

Contorno de baixo custo: um workflow do GitHub Actions rodando um `SELECT` leve a cada 5-6 dias mantém o projeto acordado — e desde abril de 2026 isso funciona no plano free sem precisar de Pro.

500 MB de banco, na prática, aguenta bastante antes de virar problema: nas estimativas do setor, algo como ~2 milhões de linhas de perfil de usuário simples ou ~500 mil eventos de log. Para Encaixe (agendamentos, estabelecimentos, contatos), isso não é o gatilho mais próximo — a pausa por inatividade é.

## 🧠 3. Redundância que o reel ignora

O free tier do Supabase já inclui:

- **Auth** (até 50 mil MAU) — torna Clerk redundante enquanto não houver requisito B2B específico que só Clerk resolve. Ver [[autenticacao-gerenciada]].
- **pgvector** (busca vetorial via extensão Postgres) — torna Pinecone desnecessário até existir uma feature de RAG/busca semântica definida. Ver [[banco-de-dados-vetorial]].

Pagar por um segundo vendor pra fazer o que o Supabase já cobre de graça é custo de manutenção sem ganho — o erro mais comum descrito em [[adocao-de-ferramenta]].

## ✅ Como decidir quando sair do free

| Sinal | Ação |
| ----- | ---- |
| Base de dados perto de 500 MB | Avaliar Pro ($25/mês) — antes de bater o teto, não depois |
| MAU perto de 50 mil | Pro cobre até lá; acima disso, custo por usuário adicional |
| Precisa de backup point-in-time | Pro obrigatório — free não tem |
| Precisa de SLA/SSO/compliance | Team ($599/mês) ou Enterprise |
| Nenhum dos sinais acima, só quer evitar a pausa | Cron de keep-alive resolve sem custo |

Regra prática: **o gatilho de migração é o uso real batendo um desses números, não a previsão de que vai bater.** É exatamente a lógica de custo-zero-até-validar já em uso.

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão que decide se vale trocar agora.
- [[autenticacao-gerenciada]] — por que Clerk não soma ao que o Supabase Auth já cobre.
- [[banco-de-dados-vetorial]] — por que Pinecone é redundante sem um requisito de RAG definido.

## 📚 Fontes

- [Supabase Pricing 2026 — UI Bakery](https://uibakery.io/blog/supabase-pricing)
- [Supabase Free Tier Limits 2026 — ITPath Solutions](https://www.itpathsolutions.com/supabase-free-tier-limits)
- [Supabase Free Tier Limits — AIAgencyPlus](https://aiagencyplus.com/supabase-free-tier-limits/)
