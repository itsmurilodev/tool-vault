---
titulo: "Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito"
resumo: "Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida."
tipo: referencia
dominio: murilo
tags: [infra/banco-de-dados, ia, custo]
status: ativo
atualizado: 2026-08-11
---

# Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito

## 📌 Resumo

Banco vetorial existe para uma coisa: buscar por *similaridade de significado* em vez de igualdade exata — a base de busca semântica, recomendação e RAG (Retrieval-Augmented Generation). Ele **não resolve nada sozinho** — só importa quando existe uma feature que precisa disso. Hoje, nem Encaixe nem Async Hub têm essa feature definida no roadmap.

> 💡 **Analogia:** comprar um arquivo rotativo de biblioteca antes de ter livros — ótimo produto, zero uso sem o requisito que o justifica.

## 🧠 1. Por que pgvector vem antes de Pinecone

Supabase (que Encaixe já usa) roda Postgres — e Postgres com a extensão `pgvector` faz busca vetorial nativamente, sem infraestrutura extra, sem vendor novo, sem conta adicional. Isso mudou o cenário do setor em 2026: bancos vetoriais dedicados (Pinecone, Qdrant, Weaviate) hoje competem em escala e recurso avançado — não em ser a única forma de ter busca semântica.

Diferença prática, se o requisito aparecer:

| | Pinecone | pgvector no Supabase |
| - | -------- | --------------------- |
| Vendor novo | Sim | Não — já é o banco atual |
| Free tier | ~2 GB, ~100 mil vetores (embedding de 1536 dimensões, ex.: OpenAI) | Dentro dos 500 MB do banco já usado |
| Portabilidade | Formato proprietário — migrar exige reindexar tudo | Padrão Postgres — `pg_dump` já inclui os vetores |
| Latência em escala alta | Melhor, feito sob medida | Compete por CPU com o resto do banco no free tier |

## ⚠️ 2. O portão antes de considerar qualquer um dos dois

Antes de avaliar Pinecone ou pgvector, responda: **existe uma feature descrita** que precisa buscar por significado — busca de produto por descrição livre, recomendação, chatbot com contexto de base de conhecimento? Se a resposta é "ainda não, mas pode ser útil um dia", isso é backlog, não adoção — critério igual ao de [[adocao-de-ferramenta]].

## ✅ Como aplicar quando o requisito aparecer

| Situação | Escolha |
| -------- | ------- |
| Volume pequeno/médio, já usa Supabase | `pgvector` — zero vendor novo, zero custo extra |
| Volume alto ou latência sub-100ms é requisito duro | Avaliar Pinecone/Qdrant dedicado, com o custo real de migração na mesa |
| Quer manter portabilidade máxima | Qdrant self-hosted (open source, sem limite) |

## 🔗 Ver também

- [[backend-como-servico]] — o Supabase que já cobre isso sem custo adicional.
- [[adocao-de-ferramenta]] — o portão que impede adotar infraestrutura antes do requisito existir.

## 📚 Fontes

- [Vector Database Pricing Comparison 2026 — AgentDeals](https://agentdeals.dev/vector-database-pricing)
- [Limit of vectors on free plan — Pinecone Community](https://community.pinecone.io/t/limit-of-vectors-on-free-plan/3821)
