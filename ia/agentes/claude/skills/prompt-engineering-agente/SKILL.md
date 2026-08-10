---
name: prompt-engineering-agente
description: Usar sempre que o usuário pedir para gerar, melhorar, revisar ou enviar um prompt para uma IA/agente (ChatGPT, Claude, Codex, Antigravity, Gemini). Aplica estrutura em tags XML com nível de detalhe proporcional ao risco da tarefa.
---

# Prompt Engineering — Padrão do usuário

**Idioma:** a comunicação com o usuário (declaração do nível escolhido, explicações) é em português do Brasil, direta e simples. O conteúdo do prompt entregue segue o idioma mais adequado à tarefa/agente-alvo, salvo indicação em contrário do usuário.

## 1. Decida o nível antes de montar o prompt

- **Completo** (todas as tags abaixo): tarefa envolve múltiplos arquivos, mudança de arquitetura, ação irreversível, ou o usuário pediu explicitamente o template cheio.
- **Compacto** (objetivo + contexto + tarefas + formato_saida): consulta pontual, escopo pequeno, baixo risco.
- **Nenhum template**: pergunta direta que não é um prompt para terceiros.

Nunca aplique o template completo por padrão — isso contradiz o próprio princípio de prompt enxuto. Declare qual nível está usando e por quê, em uma linha, antes do prompt.

## 2. Estrutura completa (quando aplicável)

```
<papel>
[Especialidade exigida do agente.]
</papel>

<objetivo>
[O que deve ser feito, em uma frase.]
</objetivo>

<contexto>
[Stack, projeto, estado atual, estilo desejado.]
</contexto>

<tarefas>
1. Diagnosticar.
2. Identificar causa provável.
3. Propor a menor correção segura.
4. Aplicar apenas o necessário.
5. Validar o resultado.
</tarefas>

<restricoes>
- Não refatorar fora do escopo.
- Não criar dependências sem necessidade.
- Não remover arquivos sem justificar.
- Não quebrar responsividade / build.
</restricoes>

<formato_saida>
## Diagnóstico
## Causa provável
## Correção aplicada/recomendada
## Arquivos alterados
## Riscos técnicos
## Checklist final
</formato_saida>

<validacao_final>
- O objetivo foi atendido?
- As restrições foram respeitadas?
- A solução é simples e segura?
- Não há alterações desnecessárias?
</validacao_final>
```

## 3. Estrutura compacta (padrão para a maioria dos casos)

```
<objetivo>
[Corrigir/gerar/melhorar X.]
</objetivo>

<contexto>
[Stack e restrição essencial, 1-2 linhas.]
</contexto>

<tarefas>
[Diagnosticar, corrigir com menor alteração possível, validar.]
</tarefas>

<formato_saida>
[Diagnóstico + arquivos alterados + checklist.]
</formato_saida>
```

## 4. Regras de conteúdo

- Delimitar sempre com tags XML (`<objetivo>`, `<contexto>`, etc.) — funciona bem especificamente com Claude; para outros modelos, testar se markdown puro performa melhor antes de assumir que XML é universal.
- Few-shot: incluir 1-2 exemplos de saída esperada apenas quando o formato exato importa (ex.: padronizar commits, docs, auditorias).
- **Não pedir "pense passo a passo e mostre todo o raciocínio"** quando o agente-alvo tem raciocínio nativo (Claude com extended thinking, modelos da série o-x, Gemini em modo reasoning) — é redundante e infla a resposta.
- **Pedir raciocínio antes da conclusão** quando o agente-alvo é um modelo padrão sem essa camada — nesse caso ainda aumenta a precisão de forma mensurável.
- Rubrica de avaliação: ao usar rubrica para o próprio agente se autoavaliar, deixar explícito que essa aprovação não é uma verificação independente — o mesmo modelo que respondeu tende a validar a própria resposta. Sugerir uma segunda passada (nova conversa) ou revisão humana antes de aceitar como definitivo.
- Ao revisar um prompt que falhou, registrar: versão anterior, problema observado, ajuste feito — não apenas "ajustar e testar de novo" sem rastro.

## 5. Portão de entrada — não gerar prompt em cima de pedido vazio

Antes de montar qualquer prompt, classifique o que o usuário deu:

- **Suficiente** — tem objetivo, contexto mínimo, agente-alvo e restrição. Gere o prompt.
- **Incompleto** — tem a ideia, falta contexto, restrição ou formato esperado. Pergunte só o que falta, de forma objetiva, e diga por que aquilo muda o resultado.
- **Vazio** ("faz um prompt bom", "melhora isso", "cria algo legal", "quero um agente melhor") — **não gere.** Prompt inventado em cima de pedido vago produz um prompt que parece bom e não serve. Peça o mínimo antes.

O mínimo, quando a entrada for fraca:

1. Qual é o objetivo final?
2. Para qual IA/agente/ferramenta o prompt vai?
3. Qual o contexto do projeto ou problema?
4. O agente deve analisar, gerar, executar, revisar ou validar?
5. O que ele **não** pode fazer?
6. Qual formato de resposta você quer?
7. Como saber que a resposta ficou boa?

Se o usuário responder parcialmente, pressione só o que ainda falta — não repita o formulário inteiro.

Tom: direto e racional, sem bajulação e sem grosseria performática. "Isso ainda está vago demais", "com esse contexto, qualquer prompt bom seria chute", "falta restrição — sem ela o agente pode mexer onde não deve".

Quando o usuário pedir explicitamente para ser interrogado a fundo, isso é escopo da skill `grill-me`, não desta.

## 6. Segurança em prompt técnico

Quando o prompt envolver código, sistema ou agente de programação, incluir nas restrições: não alterar nada fora do escopo, não criar dependência sem necessidade, não refatorar sem justificativa, preservar o que já funciona, diagnosticar antes de implementar, listar arquivos alterados, validar com teste/build/diff, e não inventar stack, comando, caminho ou arquivo.

## 7. Formato de entrega ao usuário

Sempre entregar o prompt final pronto em bloco de código markdown, pronto para copiar e colar, precedido de uma linha dizendo qual nível (completo/compacto/nenhum) foi usado e por quê.

Quando a entrada for fraca e o prompt não for gerado, entregar: diagnóstico direto do que falta, as perguntas objetivas, e a indicação de que o prompt sai assim que elas forem respondidas.
