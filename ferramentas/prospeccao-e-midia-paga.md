---
titulo: Prospecção B2B e mídia paga — quando essas ferramentas passam a valer
resumo: "Apollo.io, ZoomInfo e Windsor.ai: custo real, portão de cada uma e o que a LGPD exige."
tipo: referencia
dominio: ferramentas
tags: [ferramentas/vendas, gtm, custo, lgpd]
status: ativo
atualizado: 2026-08-09
---

# Prospecção B2B e mídia paga — quando essas ferramentas passam a valer

## 📌 Resumo

ZoomInfo, Apollo.io e Windsor.ai aparecem juntas em listas de conectores, mas resolvem **dois problemas diferentes** e têm portões de adoção diferentes. Nenhuma é inadequada por natureza — são inadequadas *antes* de existir o processo que elas aceleram. Ferramenta de vendas não cria demanda: ela multiplica um processo que já funciona. Multiplicar zero dá zero, e cobra assinatura por isso.

> 💡 **Analogia:** é a diferença entre comprar uma máquina de embalar e ter o que embalar. A máquina é ótima quando existe produção; antes disso é custo fixo parado.

## 🧠 1. São duas categorias, não três ferramentas

### Prospecção / dados de lead — ZoomInfo e Apollo.io

Bancos de dados de empresas e contatos profissionais, com filtro por setor, porte, cargo e tecnologia usada. Você define o perfil de cliente ideal, a ferramenta devolve uma lista de empresas e pessoas com e-mail e telefone, e (no caso do Apollo) dispara sequências de contato.

**São concorrentes entre si.** Escolhe-se uma.

| | Apollo.io | ZoomInfo |
| --- | --- | --- |
| Preço de entrada | Plano gratuito permanente: 900 créditos/ano, 2 sequências, 250 e-mails/dia | Não é público — contato comercial |
| Pago | Basic ~US$ 49/usuário/mês · Professional ~US$ 79 · Organization ~US$ 119 | Professional a partir de ~US$ 15 mil/ano para 3 assentos; tiers acima vão a US$ 25–40 mil/ano |
| Modelo | Crédito por export, **não acumula** — crédito não usado expira no mês | Contrato anual |
| Perfil | Solo e time pequeno | Time de vendas estruturado |

Apollo tem free tier real e é acessível; ZoomInfo é compra corporativa com contrato anual — fora de cogitação para estúdio pequeno, não por ser ruim, mas porque o piso de preço pressupõe um time de vendas que justifique US$ 15 mil/ano.

Cuidado com o modelo de crédito: relatos consistentes de times gastando 30–50% acima do plano base por excedente de crédito. O preço de tabela não é o custo real.

### Dados de mídia paga — Windsor.ai

Categoria diferente: é **ETL de marketing**. Puxa dados de 325+ fontes (Google Ads, Meta, TikTok, LinkedIn Ads, GA4, HubSpot, Shopify) e joga num destino de análise (Looker Studio, BigQuery, Sheets, Power BI). Inclui modelagem de atribuição multi-touch.

Preço: free tier, depois ~US$ 19/mês (Basic), ~US$ 99 (Standard), US$ 249–499 (Plus/Professional).

**O pré-requisito é aritmético:** Windsor.ai unifica dados de anúncio. Sem verba de anúncio rodando, não há dado para unificar. Com um único canal, o painel nativo da própria plataforma já resolve — a ferramenta existe para o caso de 2+ canais onde ninguém sabe qual está gerando o resultado.

## 🧠 2. O portão de cada uma

| Ferramenta | Passa a valer quando | Sinal de que ainda não é hora |
| ---------- | -------------------- | ----------------------------- |
| **Apollo.io** | Existe um ICP escrito (setor, porte, cargo que decide) e um processo de outbound repetível que hoje trava por falta de lista | Cliente vem por indicação e rede pessoal; prospecção é ad-hoc |
| **ZoomInfo** | Time de vendas dedicado, ticket alto o suficiente para amortizar US$ 15 mil/ano | Qualquer coisa abaixo disso |
| **Windsor.ai** | Verba em 2+ canais de anúncio e decisão real de realocação de budget dependendo do dado | Verba zero, ou canal único |

O gargalo determina a ordem. Se o problema é **não saber quem abordar**, Apollo ajuda. Se é **não conseguir converter quem já respondeu**, ferramenta de lista não resolve — o problema está na oferta ou no processo comercial, e comprar lista maior só aumenta o volume de "não".

## 🧠 3. LGPD — o custo que não aparece na tabela de preço

Prospecção B2B no Brasil é legal, mas tem regra. Vale entender antes, não depois.

- **Dado de pessoa jurídica** (razão social, endereço comercial, telefone e e-mail institucional do tipo `contato@`) não é dado pessoal e está fora do escopo da LGPD.
- **Dado de pessoa física** (e-mail nominal `nome@empresa.com`, nome do sócio, celular) **é dado pessoal**, mesmo em contexto profissional. O uso em prospecção se apoia na base legal de **legítimo interesse**, não em consentimento prévio.

O que legítimo interesse exige na prática:

1. **Interesse comercial genuíno e contato pertinente ao perfil.** Disparo em massa sem segmentação, para quem não tem relação plausível com o que você vende, descaracteriza a base legal.
2. **Origem defensável.** Dado que estava em contexto comercial público (site, LinkedIn da empresa, rodapé, cartão digital) é defensável. Lista comprada de origem obscura, não.
3. **Respeitar oposição imediatamente.** Pediu para não ser contatado, encerra — e o registro do opt-out precisa existir.
4. **Transparência.** A pessoa deve conseguir saber de onde você tirou o contato dela.

Isso importa duplamente em estúdio que atende cliente: se você usa a ferramenta em nome de um cliente, o tratamento de dado passa a ter mais de um responsável, e isso é cláusula de contrato, não detalhe operacional.

## 🧠 4. O que muda ao ligar como conector do Claude

Conectar essas ferramentas ao Claude não substitui o processo — remove o passo de exportar CSV e colar. Só ganha valor depois que o dado já existe e já é usado.

Windsor.ai tem MCP próprio, que envia dado de marketing direto para o assistente. Útil para perguntar "qual canal caiu semana passada" sem abrir o painel. Continua valendo o pré-requisito: precisa haver canal e verba.

E vale o custo geral de conector já registrado em [conectores do Claude](../ia/agentes/claude/conectores.md): cada conector ativo ocupa contexto em toda conversa e amplia a superfície de injeção. Conector de vendas ligado "para quando eu precisar" cobra esse preço todos os dias.

## ✅ Caminho de adoção

1. **Antes de qualquer ferramenta:** ICP escrito e uma oferta que já fechou pelo menos alguns negócios. Sem isso, o gargalo não é lista.
2. **Primeiro passo pago (ou grátis):** Apollo no free tier — 900 créditos/ano dão para testar se outbound funciona para o seu perfil, sem contrato.
3. **Só se o outbound provar retorno:** subir para o plano pago, olhando o custo real com excedente de crédito, não o de tabela.
4. **Windsor.ai só depois de existir verba** em mais de um canal.
5. **ZoomInfo:** só com time de vendas dedicado. Reavaliar apenas se o cenário mudar de patamar.

Reavalie a cada trimestre. O portão que hoje diz "ainda não" é o mesmo que um dia dirá "agora sim" — o erro é nunca voltar a olhar.

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão genérico de estágio, do qual esta nota é uma aplicação.
- [Conectores do Claude](../ia/agentes/claude/conectores.md) — custo de manter conector ligado.

## 📚 Fontes

- [Apollo.io pricing 2026 — Salesmotion](https://salesmotion.io/blog/apollo-pricing) · [Apollo vs ZoomInfo](https://salesmotion.io/zoominfo-vs-apollo)
- [Windsor.ai pricing — Coefficient](https://coefficient.io/windsor-ai-pricing) · [review](https://portermetrics.com/en/compare/windsor-ai-overview/)
- [LGPD na prospecção B2B — Neoway](https://blog.neoway.com.br/lgpd-na-prospeccao/) · [O legítimo interesse na LGPD — Data Privacy Brasil](https://www.dataprivacybr.org/wp-content/uploads/2021/10/O-legitimo-interesse-na-LGPD.pdf)
