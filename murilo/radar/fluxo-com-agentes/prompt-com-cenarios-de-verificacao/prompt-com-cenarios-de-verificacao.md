---
titulo: "Prompt em três seções — tarefa, contexto e cenários de verificação"
resumo: "Episódio 5 da série do reel: todo prompt de tarefa tem objetivo, contexto e uma lista de cenários que precisam passar para a tarefa contar como feita. A terceira seção já foi aplicada na skill prompt-engineering-agente. O contexto deve ser ponteiro, não despejo."
tipo: conceito
dominio: murilo
tags: [murilo/ia, prompt-engineering, agentes, verificacao]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: fluxo-com-agentes
natureza: pratica
quando_usar: "Toda tarefa delegada a um agente: objetivo, contexto como ponteiros e cenários de verificação observáveis."
quando_nao_usar: "Versão longa (15 a 30 min) em bug de uma linha ou pergunta pontual; aí basta o repro como cenário único."
pre_requisito: "Nenhum: já embutido na skill prompt-engineering-agente."
---

# Prompt em três seções — tarefa, contexto e cenários de verificação

## 📌 Resumo

No episódio 5, o autor descreve o prompt dele em três seções:

1. **Tarefa:** o bug ou a feature.
2. **Contexto:** referências de arquivos, documentos de design e tudo que puder ajudar.
3. **Cenários de validação e verificação:** o que precisa passar para a tarefa contar como concluída. Para ele, é a parte mais importante.

Ele gasta de 15 a 30 minutos no prompt, porque "a engenharia agora é antecipada na escrita do prompt". De todo o material da série, **é o que mais te serve com o menor custo**: não exige ferramenta nova e corrige uma lacuna real da sua skill `prompt-engineering-agente`.

> 💡 **Analogia:** o critério de aceite de uma obra. "Reformar o banheiro" é a tarefa. A planta e o catálogo do piso são o contexto. "Ralo escoa 10 litros em 1 minuto sem empoçar" e "rejunte sem fissura" são o critério que o pedreiro conhece **antes** de começar e que você confere na entrega.

## 🧠 1. Comparando com a sua skill atual

| Seção do reel | Sua `prompt-engineering-agente` | Lacuna |
| --- | --- | --- |
| Tarefa | `<objetivo>` + `<tarefas>` | Nenhuma |
| Contexto | `<contexto>` ("stack, projeto, estado atual"; no compacto, 1 a 2 linhas) | Falta pedir **ponteiros**: arquivos, docs e o feature map |
| **Cenários de verificação** | `<validacao_final>`: "O objetivo foi atendido? A solução é simples?" | **É aqui que está a lacuna.** Hoje é uma autochecagem genérica que o próprio agente responde. A sua skill já admite que o modelo tende a validar a própria resposta. |

A diferença é de natureza. "O objetivo foi atendido?" é **opinião** do agente. "Agendar às 23h30 no fuso `America/Sao_Paulo` aparece no dia certo na agenda do estabelecimento e no e-mail de confirmação" é **fato observável**: alguém roda e vê se passou.

## ⚠️ 2. Onde ajustar o que o reel diz

1. **"Todo pedaço de contexto que possa ser útil" leva ao inchaço.** Despejar documentos inteiros no prompt gasta tokens e piora o raciocínio. É o mesmo problema de [[context7]] e [[find-skills]], e o pstack tem até um princípio para isso (*guard the context window*). O certo é **ponteiro com motivo**: `src/booking/slots.ts — onde o horário é calculado`. O agente abre o arquivo quando precisar.
2. **15 a 30 minutos é para feature, não para tudo.** A sua skill já tem o portão certo (completo, compacto ou nenhum template). Bug de uma linha não precisa de meia hora de prompt. Precisa de **um** cenário de verificação, que é o repro que falhava.
3. **Faltam duas seções:**
   - **Fora de escopo:** o que o agente *não* pode fazer. A sua skill já tem isso em `<restricoes>`, e vale manter.
   - **Forma da evidência:** *como* provar cada cenário (transcrição do `verify-<app>`, saída do teste, snapshot), não só *o que* provar.
4. **Contradição dentro da série.** No fim, o autor diz que não é seguro ficar tão longe do código e dos detalhes de implementação. Nos episódios 2 e 3, o pipeline dele faz merge sem revisão humana quando o próprio agente julga a mudança pequena ([[captura-de-erros-para-agentes]]). Neste ponto o episódio 5 concorda com você, não com ele mesmo.
5. **A citação do tweet** ("um dos criadores do código, Coda") está truncada e embaralhada na transcrição. Não deu para identificar nem verificar.

## 🧠 3. Ligação com o resto da série

- **Os cenários de verificação são as jornadas do feature map** do `verify-<app>` ([[pstack-verificacao]]). Se a feature já está no mapa, o cenário pode ser "rodar a jornada `create-save` e mais este caso novo".
- **Em bug fix, o primeiro cenário é sempre o repro** ([[correcao-de-bug-com-agentes]]): "com a fixture X, o erro Y acontece antes e não acontece depois".
- **Escrever os cenários é levantamento de requisito.** Para feature nova, a skill `levantamento-requisitos` gera os critérios de aceite que viram esta seção.

## ✅ 4. Como aplicar: seção `<cenarios_de_verificacao>`

✅ **Aplicado em 2026-11-09** na skill [prompt-engineering-agente](../../../ia/agentes/skills/prompt-engineering-agente/SKILL.md): a seção substituiu `<validacao_final>` no template completo e entrou no compacto, o `<contexto>` passou a pedir ponteiros e as duas regras foram para a seção 4. O formato ficou assim:

```xml
<cenarios_de_verificacao>
A tarefa só está concluída quando TODOS passarem, com evidência anexada.
1. [Dado <estado>] Quando <ação do usuário> Então <resultado observável>.
   Evidência: <saída do teste | transcrição/screenshot do verify-<app> | resposta da API>.
2. Caso de borda: <entrada vazia | fuso | acento | concorrência | permissão negada> → <resultado>.
3. Regressão: <jornada existente do feature map> continua passando.
Se algum cenário não puder ser executado, diga qual e por quê. Não declare concluído.
</cenarios_de_verificacao>
```

E `<contexto>` passa a pedir ponteiros:

```xml
<contexto>
Stack: <1 linha>.
Ler antes de mexer:
- <caminho/arquivo> — <por que importa>
- <verify-app/features/x.md> — <jornada afetada>
- <doc/ADR> — <decisão que restringe a solução>
</contexto>
```

**Regra de bolso:** se você não consegue escrever o cenário 1, a tarefa ainda não está entendida. Volte para `levantamento-requisitos` antes de gastar tokens de agente.

## 🔗 Ver também

- [[prompt-engineering]] · [[pstack-verificacao]] · [[correcao-de-bug-com-agentes]] · [[skills-de-qualidade-de-codigo]]
- Skills [prompt-engineering-agente](../../../ia/agentes/skills/prompt-engineering-agente/SKILL.md) · [levantamento-requisitos](../../../ia/agentes/skills/levantamento-requisitos/SKILL.md)

## 📚 Fontes

- Transcrição do reel (episódio 5 da série) colada pelo usuário em 2026-11-09 (autor não identificado).
- [backnotprop/pstack — principle-guard-the-context-window](https://github.com/backnotprop/pstack/tree/main/skills/principle-guard-the-context-window), lido em 2026-11-09.
