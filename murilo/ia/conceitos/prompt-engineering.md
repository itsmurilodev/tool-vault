---
titulo: Prompt Engineering — estudo
resumo: "Instruções claras, delimitadores, formato de saída e avaliação iterativa."
tipo: conceito
dominio: murilo
tags: [ia/prompt-engineering, llm]
status: ativo
atualizado: 2026-08-09
---

# Prompt Engineering

## 📌 Resumo

A DeepLearning.AI ensina prompt engineering como uma prática **testável e iterativa**, não como uma fórmula mágica. Os cursos feitos com a OpenAI reforçam técnicas como: instruções claras, uso de delimitadores, formato de saída definido, exemplos, divisão de tarefas complexas, avaliação com critérios e melhoria contínua do prompt. (DeepLearning.ai)

> 💡 **Analogia:** Um prompt é como uma ordem de serviço para um programador. Se você só fala “arruma meu site”, a pessoa pode mexer em qualquer coisa. Se você fala objetivo, contexto, restrições e validação, a chance de entregar certo aumenta muito.
> 

Usei seu anexo como referência de estilo: resumo inicial, explicação por tópicos, exemplos em blocos de código, analogias, conceitos-chave e tags sugeridas.

---

## 🧠 1. Instruções claras e específicas

A primeira regra da DeepLearning.AI é escrever instruções **claras e específicas**. Eles deixam claro que um prompt bom não precisa ser o mais curto; muitas vezes, um prompt um pouco maior funciona melhor porque dá mais contexto e reduz respostas erradas ou irrelevantes. (DeepLearning.AI - Learning Platform)

### ❌ Prompt fraco

```
Melhore meu site.
```

### ✅ Prompt melhor

```
<objetivo>
Melhorar a seção Home do meu portfólio.
</objetivo>

<contexto>
O projeto usa Next.js, TypeScript e Tailwind.
A estética desejada é terminal moderno, editor de código e Git/dev tools.
</contexto>

<tarefas>
1. Analisar espaçamento.
2. Melhorar hierarquia visual.
3. Corrigir responsividade.
4. Não alterar seções fora da Home.
</tarefas>
```

> ⚠️ Prompt claro não é prompt gigante. É prompt que separa bem **o que fazer**, **onde fazer**, **como responder** e **o que evitar**.
> 

---

## 🧱 2. Delimitadores: `<tags>`, crases e seções

A DeepLearning.AI recomenda usar delimitadores para separar partes diferentes do prompt. Eles citam crases triplas, aspas, tags XML e títulos de seção como formas válidas de deixar claro onde começa e termina cada parte da entrada. (DeepLearning.AI - Learning Platform)

### Principais delimitadores

- **`<objetivo>...</objetivo>`** — separa o objetivo
- **`<contexto>...</contexto>`** — separa o contexto
- **`<restricoes>...</restricoes>`** — separa o que não pode fazer
- — ideal para código, logs e textos longos
- **`## Título`** — bom para organizar prompts em Markdown

### Exemplo

```
<objetivo>
Corrigir o erro abaixo no projeto.
</objetivo>

<erro>
```bash
Module not found: Can't resolve '@/components/Navbar'
```
</erro>

<restricoes>
- Não alterar a arquitetura do projeto.
- Não criar dependências novas sem necessidade.
</restricoes>
```

> 💡 **Analogia:** Delimitadores são como caixas etiquetadas. Em vez de jogar tudo em uma mochila, você separa: “documentos”, “ferramentas”, “peças” e “manual”.
> 

---

## 🧾 3. Definir o formato de saída

Uma técnica muito efetiva é dizer **exatamente como você quer receber a resposta**. Isso reduz respostas bagunçadas e facilita copiar para Notion, GitHub, docs ou prompt de outra IA.

A DeepLearning.AI ensina que pedir saída estruturada é uma das táticas para tornar a resposta mais previsível. (DeepLearning.AI - Learning Platform)

### Modelo

```
<formato_saida>
Retorne em Markdown com:

## Diagnóstico
## Causa provável
## Correção recomendada
## Arquivos afetados
## Checklist final
</formato_saida>
```

### Para código

```
<formato_saida>
Retorne:
1. Diagnóstico curto
2. Arquivos que precisam ser alterados
3. Código corrigido
4. Testes de validação
</formato_saida>
```

> ⚠️ Se você não define formato, a IA escolhe o formato sozinha. Às vezes vem texto longo, às vezes lista, às vezes mistura tudo.
> 

---

## 🧪 4. Desenvolvimento iterativo de prompts

A DeepLearning.AI reforça que não existe “prompt perfeito de primeira”. O processo correto é testar, observar onde falhou, ajustar a instrução e testar de novo. Eles comparam isso ao processo de desenvolvimento em machine learning: ideia → teste → erro → ajuste → nova versão. (DeepLearning.AI - Learning Platform)

### Fluxo recomendado

```
1. Escreva uma primeira versão do prompt.
2. Teste com um caso real.
3. Veja onde a IA errou.
4. Adicione restrições ou contexto.
5. Teste novamente.
6. Salve a versão que funcionou melhor.
```

### Exemplo prático

```
Versão 1:
Corrija a navbar.

Problema:
A IA mexeu em arquivos demais.

Versão 2:
Corrija apenas o estado ativo da navbar.
Não altere layout, cores, animações ou estrutura das seções.
Liste os arquivos modificados no final.
```

> 💡 **Analogia:** Prompt é como treino de academia. O primeiro treino já ajuda, mas o resultado real vem ajustando carga, técnica e frequência.
> 

---

## 🔍 5. “Show rather than tell”: mostrar exemplo em vez de só explicar

Em cursos mais recentes, a DeepLearning.AI recomenda a técnica **show rather than tell**: em vez de explicar demais como a IA deve responder, você mostra 1 ou 2 exemplos do resultado esperado. (DeepLearning.AI - Learning Platform)

### Exemplo

```
<exemplo_saida>
## Diagnóstico
A navbar está marcando a seção errada porque o cálculo do scroll ativo considera offsets antigos.

## Correção
Ajustar a lógica de activeSection para calcular a seção visível com base no centro da viewport.

## Checklist
- [ ] Testar clique em Home
- [ ] Testar clique em Projetos
- [ ] Testar scroll manual
</exemplo_saida>
```

Depois peça:

```
Agora responda seguindo exatamente esse estilo.
```

> ⚠️ Essa técnica é muito boa para padronizar respostas de IA, documentação, commits, auditorias e prompts para Codex/Antigravity.
> 

---

## 🧩 6. Dividir tarefas complexas em subtarefas

No curso **Building Systems with the ChatGPT API**, a DeepLearning.AI ensina a quebrar tarefas complexas em etapas menores, em vez de tentar resolver tudo em um único prompt gigante. (DeepLearning.ai)

### Ruim

```
Analise todo meu projeto, melhore o design, corrija bugs, atualize docs, remova arquivos inúteis e deixe tudo perfeito.
```

### Melhor

```
<tarefas>
1. Primeiro, analise a documentação.
2. Depois, compare docs com o código.
3. Em seguida, liste inconsistências.
4. Só depois sugira alterações.
5. Não implemente nada antes do diagnóstico.
</tarefas>
```

### Para projetos grandes

```
<etapa_1>
Auditar documentação.
</etapa_1>

<etapa_2>
Comparar documentação com código.
</etapa_2>

<etapa_3>
Propor plano de correção.
</etapa_3>

<etapa_4>
Aplicar apenas mudanças aprovadas.
</etapa_4>
```

> 💡 **Analogia:** Não peça para a IA “construir uma casa inteira” de uma vez. Peça primeiro planta, depois fundação, depois elétrica, depois acabamento.
> 

---

## 🧠 7. Dar tempo para a IA analisar sem pedir textão

A DeepLearning.AI ensina o princípio de “dar tempo para o modelo pensar”, principalmente em tarefas com raciocínio ou múltiplas etapas. Mas cursos mais recentes também alertam que pedir raciocínio explícito demais pode gerar respostas enormes e desnecessárias. (DeepLearning.AI - Learning Platform)

### Melhor jeito de pedir

```
Analise cuidadosamente antes de responder.
Retorne apenas a conclusão final organizada.
```

Ou:

```
Antes de propor a correção, verifique:
1. Causa provável
2. Impacto no sistema
3. Menor alteração segura
4. Riscos técnicos

Depois retorne apenas o diagnóstico e o plano.
```

### Evite usar sempre

```
Pense passo a passo e mostre todo seu raciocínio.
```

> ⚠️ Para prompts de código, o melhor é pedir **diagnóstico + solução + checklist**, não um raciocínio enorme.
> 

---

## ✅ 8. Criar rubrica de avaliação

Uma técnica avançada ensinada pela DeepLearning.AI é avaliar respostas usando uma **rubrica**, ou seja, uma lista de critérios. Isso ajuda muito quando você quer saber se a IA entregou algo bom ou só respondeu bonito. (DeepLearning.AI - Learning Platform)

### Modelo de rubrica

```
<rubrica_de_avaliacao>
Avalie a resposta com base nos critérios:

1. Atende ao objetivo inicial?
2. Respeita as restrições?
3. Evita alterações fora do escopo?
4. Mantém a arquitetura do projeto?
5. Tem checklist final?
6. Explica riscos técnicos?
</rubrica_de_avaliacao>
```

### Para seu portfólio

```
<rubrica_de_avaliacao>
A solução será considerada boa se:

- Preservar Next.js App Router.
- Preservar TypeScript.
- Manter estética terminal/dev tools.
- Não parecer SaaS genérico.
- Não quebrar responsividade.
- Não criar dependências sem necessidade.
- Listar arquivos alterados.
</rubrica_de_avaliacao>
```

> 💡 **Analogia:** Rubrica é como checklist de vistoria. Sem ela, a IA pode achar que “ficou bom”; com ela, precisa passar por critérios claros.
> 

---

## 🧷 9. Usar resposta ideal como referência

Além da rubrica, a DeepLearning.AI mostra que você pode fornecer uma **resposta ideal** para a IA comparar se a nova resposta está parecida com o padrão esperado. (DeepLearning.AI - Learning Platform)

### Modelo

```
<resposta_ideal>
Uma boa resposta deve:
- Ser direta.
- Explicar o problema.
- Sugerir a menor correção possível.
- Não sair do escopo.
- Terminar com checklist.
</resposta_ideal>

<tarefa>
Compare a resposta gerada com a resposta ideal e diga se ela está adequada.
</tarefa>
```

> ⚠️ Isso é muito útil para revisar prompts criados por outra IA, auditorias técnicas, documentação e respostas de agentes.
> 

---

## 🔐 10. Verificar entrada e saída

O curso **Building Systems with the ChatGPT API** também aborda avaliação de entradas e saídas para segurança, precisão e relevância. Para você, isso vira uma regra prática: todo prompt importante deve pedir validação final. (DeepLearning.ai)

### Modelo

```
<validacao_final>
Antes de finalizar, verifique:

- A resposta atende ao objetivo?
- Alguma restrição foi quebrada?
- Algum arquivo desnecessário foi criado?
- O código continua coerente com a stack?
- Existem riscos técnicos?
- A solução é simples o suficiente?
</validacao_final>
```

### Para código

```
<validacao_final>
Confirme:

- Build sem erro.
- Console sem erro.
- Responsividade mobile/tablet/desktop.
- Acessibilidade básica.
- Nenhuma dependência nova desnecessária.
- Nenhuma refatoração fora do escopo.
</validacao_final>
```

---

## 🪙 11. Economizar tokens sem perder qualidade

Usar `<tags>` e Markdown não necessariamente reduz tokens sozinho. O que reduz tokens de verdade é **remover repetição**, separar bem os blocos e usar templates reutilizáveis.

### Faça

```
<tarefas>
1. Diagnosticar.
2. Corrigir.
3. Validar.
</tarefas>
```

### Evite

```
Eu quero que você veja o problema, analise o problema, entenda o problema, depois tente corrigir o problema e depois veja se o problema foi resolvido.
```

### Versão compacta

```
<objetivo>
Corrigir [problema].
</objetivo>

<contexto>
Next.js + TS + Tailwind. Preservar arquitetura e visual terminal/dev tools.
</contexto>

<tarefas>
Diagnosticar, corrigir com menor alteração possível e validar build/responsividade.
</tarefas>

<saida>
Diagnóstico + arquivos alterados + checklist.
</saida>
```

> 💡 **Regra:** prompt enxuto não é prompt vago. É prompt sem repetição.
> 

---

## 🧰 12. Template mestre para usar no dia a dia

```
<papel>
Você é um especialista em engenharia de software, frontend, UX e qualidade de código.
</papel>

<objetivo>
[Explique exatamente o que deve ser feito.]
</objetivo>

<contexto>
[Explique o projeto, stack, problema atual e estilo desejado.]
</contexto>

<tarefas>
1. Diagnosticar o problema.
2. Identificar causa provável.
3. Propor a menor correção segura.
4. Aplicar apenas o necessário.
5. Validar o resultado.
</tarefas>

<restricoes>
- Não refatorar fora do escopo.
- Não criar dependências sem necessidade.
- Não remover arquivos sem justificar.
- Não alterar identidade visual sem motivo.
- Não quebrar responsividade.
</restricoes>

<formato_saida>
Retorne em Markdown:

## Diagnóstico
## Causa provável
## Correção aplicada/recomendada
## Arquivos alterados
## Riscos técnicos
## Checklist final
</formato_saida>

<validacao_final>
Antes de finalizar, confirme:
- O objetivo foi atendido.
- As restrições foram respeitadas.
- A solução é simples e segura.
- Não há alterações desnecessárias.
</validacao_final>
```

---

## 🧪 13. Template para melhorar um prompt ruim

```
<papel>
Você é um especialista em prompt engineering baseado em boas práticas da DeepLearning.AI.
</papel>

<objetivo>
Melhorar o prompt abaixo para deixá-lo mais claro, específico, seguro e fácil de validar.
</objetivo>

<prompt_original>
Cole aqui o prompt ruim.
</prompt_original>

<tarefas>
1. Identificar ambiguidades.
2. Remover repetição.
3. Separar objetivo, contexto, tarefas e restrições.
4. Adicionar formato de saída.
5. Adicionar validação final.
</tarefas>

<formato_saida>
Retorne:
1. Problemas do prompt original
2. Prompt melhorado
3. Por que ficou melhor
4. Checklist de uso
</formato_saida>
```

---

## 🧠 Conceitos-chave

- **Instrução clara** — dizer exatamente o que a IA deve fazer
- **Contexto** — informações que a IA precisa para não chutar
- **Delimitadores** — separadores como `<tags>`, crases e títulos
- **Formato de saída** — estrutura esperada da resposta
- **Few-shot** — dar 1 ou 2 exemplos do resultado esperado
- **Show rather than tell** — mostrar exemplo em vez de explicar demais
- **Iteração** — testar, avaliar erro e melhorar o prompt
- **Subtarefas** — quebrar tarefas grandes em etapas menores
- **Rubrica** — critérios para avaliar se a resposta ficou boa
- **Validação final** — checklist para evitar erro, excesso e saída fora do escopo

---

## 🏷️ Tags sugeridas

`prompt-engineering` `deeplearning-ai` `chatgpt` `codex` `antigravity` `gemini` `ia` `produtividade` `desenvolvimento` `boas-praticas`


---

## Ver também

- Skill operacional derivada deste estudo: [`ia/agentes/skills/prompt-engineering-agente/`](../agentes/skills/prompt-engineering-agente/SKILL.md)
- Persona correspondente: [[engenheiro-de-prompts]]
