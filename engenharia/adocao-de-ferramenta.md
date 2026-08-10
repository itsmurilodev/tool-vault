---
titulo: Portão de adoção de ferramenta
resumo: "Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack."
tipo: conceito
dominio: engenharia
tags: [engenharia/processo, decisao, ferramentas]
status: ativo
atualizado: 2026-08-09
---

# Portão de adoção de ferramenta

## 📌 Resumo

Método para decidir se uma ferramenta entra no stack — especialmente quando ela chegou por conteúdo viral ("as 10 ferramentas que todo dev precisa"). Toda ferramenta tem dois custos que a recomendação nunca menciona: **setup** (uma vez) e **manutenção** (para sempre). Adotar uma ferramenta boa no estágio errado é a forma mais comum de overengineering em produto pequeno.

> 💡 **Analogia:** comprar ferramenta de marcenaria profissional antes de saber se você vai marcenar. A serra é ótima. O problema é a oficina que você ainda não tem.

## 🧠 1. Desconfiar da fonte antes do conteúdo

Conteúdo de "comenta X que eu mando na DM" é funil de captura, não curadoria técnica. Otimiza para parecer impressionante em 15 segundos. Isso **não invalida** as ferramentas citadas — mas explica o que sempre falta na lista:

- quando usar e quando **não** usar;
- quanto custa (licença, tempo de setup, manutenção);
- o que ela substitui (ou se é só mais uma camada);
- se as ferramentas listadas são **complementares ou concorrentes**.

O último é o erro mais frequente: listar três plataformas que resolvem o mesmo problema como se você devesse adotar as três.

## 🧠 2. Estágio do produto define o que cabe

O mesmo stack pode ser certo e errado dependendo de onde o produto está.

| Estágio | Pergunta que domina | O que cabe |
| ------- | ------------------- | ---------- |
| **Protótipo / MVP pré-receita** | Isso resolve o problema de alguém? | Ferramenta de custo quase zero, que evita retrabalho já visível hoje |
| **Produto com usuário pagante** | Quebrou, e agora? | Observabilidade, teste de fluxo crítico, alerta |
| **Time / escala** | Como impedir que a qualidade regrida sozinha? | Contrato de arquitetura, mutation testing, gate de cobertura |

Ferramenta de estágio 3 aplicada no estágio 1 cobra manutenção sem ter usuário para justificar.

## 🧠 3. As quatro perguntas do portão

Antes de adotar, responda:

1. **Que dor concreta isso resolve, que já dói?** Se a resposta é hipotética ("quando escalar"), não adote ainda — anote no backlog.
2. **Qual o custo total?** Setup + manutenção + o custo de tirar depois. Ferramenta que entra no CI e no fluxo de todo mundo é cara de remover.
3. **Substitui ou soma?** Substituir (Biome no lugar de ESLint+Prettier) é ganho líquido. Somar é mais uma coisa para manter.
4. **É reversível?** Linter sai em uma hora. Plataforma de observabilidade com instrumentação espalhada no código, não — a menos que a instrumentação seja em padrão aberto.

## ⚠️ Erros comuns

- **Adotar em lote.** Cada ferramenta nova é uma variável a mais quando algo quebra. Uma por vez, com um problema real ligado a ela.
- **Confundir dashboard com capacidade.** Cobertura de teste é um exemplo: o painel não testa nada — ele mostra o número de um test runner que você precisa ter antes.
- **Adotar em projeto de cliente por conta própria.** Stack de cliente é decisão negociada; ferramenta paga vira dependência que alguém herda.
- **Ignorar a stack.** Metade das listas virais é do ecossistema JS/React e não se aplica a projeto PHP, Python ou mobile.

## ✅ Como aplicar

1. Pegue a lista e separe em **substitui / soma / concorre com outra da lista**.
2. Descarte o que é de estágio à frente do seu. Vai para o backlog do domínio, não para o `package.json`.
3. Do que sobrou, adote **uma**, ligada a uma dor específica.
4. Se a escolha for difícil de reverter (plataforma, formato de dado, contrato), aplique a skill `decisao-arquitetural` e registre um ADR com `templates/decisao.md`.

## 🔗 Ver também

- [[qualidade-automatizada]] · [[bibliotecas-de-ui]] · [[observabilidade]] — aplicações deste portão.
- Skill [decisao-arquitetural](../ia/agentes/claude/skills/decisao-arquitetural/SKILL.md) — quando a escolha vira ADR.
- Skill [levantamento-requisitos](../ia/agentes/claude/skills/levantamento-requisitos/SKILL.md) — o portão de porte equivalente para funcionalidade.
