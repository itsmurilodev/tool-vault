---
titulo: "OpenSEO — SEO open source com API paga por uso (alternativa ao Semrush/Ahrefs)"
resumo: "Pesquisa de palavra-chave, rastreio de posição e concorrentes, com MCP e skills para agentes. MIT, mas exige chave da DataForSEO paga por requisição; a versão hospedada cobra US$ 10/mês mais 28% em cada requisição."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/marketing-e-conteudo, open-source, seo, aeo]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: marketing-e-conteudo
natureza: ferramenta
quando_usar: "Projeto de SEO ou AEO com escopo definido (ex.: Hamidi) que precisa de dado de palavra-chave, posição e concorrência."
quando_nao_usar: "Para ter, sem projeto ativo: cada requisição é paga."
pre_requisito: "Chave da DataForSEO (pago por uso); o self-host evita os 28% de acréscimo da versão hospedada."
---

# OpenSEO

> **Radar: ⏳ avaliar.** Barato **por uso**, então só faz sentido com um projeto de SEO rodando.

## O que é

`every-app/open-seo` (27 mil estrelas, MIT, desde 2026-02). Ferramenta de SEO com pesquisa de palavra-chave, rastreio de posição e análise de concorrentes, com **MCP e skills** para agentes (Claude Code, entre outros). O dado vem da **DataForSEO**:

- **com self-host,** você paga a DataForSEO direto;
- **na versão hospedada** (`openseo.so`), paga US$ 10/mês mais **28%** sobre cada requisição.

## Quando usar

- No SEO e AEO da Hamidi ([[aeo-geo-otimizacao-para-ia]]) ou de outro cliente com escopo, quando a decisão depender de volume de busca e posição.

## Quando não usar

- Sem projeto de SEO ativo: é custo sem dor.
- Em volume alto e contínuo: compare com uma assinatura antes.

## Como usar

1. Crie a conta na DataForSEO e defina um teto de gasto.
2. Self-host local ou no EveryApp e conecte o MCP ao agente só durante o projeto.

## Ver também

- [[aeo-geo-otimizacao-para-ia]] · [[open-source-self-hosted-triagem]] · [[categoria-marketing-e-conteudo]]

## Fontes

- [every-app/open-seo](https://github.com/every-app/open-seo) (seção *Costs*)
