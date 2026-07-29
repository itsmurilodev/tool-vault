---
name: clean-code
description: >
  Aplica o padrão pessoal de Clean Code do usuário — nomes que revelam intenção,
  funções pequenas com responsabilidade única, zero duplicação, tratamento de
  erro explícito, sem overengineering. Usar SEMPRE que for escrever, gerar,
  editar ou revisar qualquer trecho de código, em qualquer linguagem ou projeto —
  não apenas quando o usuário disser "clean code" explicitamente. Quando o
  pedido for uma auditoria/revisão de código já existente (por exemplo "revise
  esse código", "refatore isso", "aplique clean code aqui", "esse arquivo está
  bagunçado"), seguir o modo de auditoria com relatório estruturado descrito
  abaixo em vez do modo padrão silencioso.
---

# Clean Code — padrão pessoal

Este skill define como o usuário quer que código seja escrito e revisado: legível, sem duplicação, com responsabilidade clara por função/arquivo, e sem abstração antes de existir necessidade real. Duas coisas emergem do princípio central: código é lido muitas vezes mais do que é escrito, e o objetivo não é impressionar — é ser entendido por outra pessoa (ou por uma IA) sem precisar adivinhar a intenção de quem escreveu.

**Idioma:** toda comunicação (comentários de código, explicações de mudança, relatório de auditoria) é em português do Brasil, direta e simples, sem jargão desnecessário. Nome de variável/função segue o padrão já existente no projeto — não force tradução de identificador em projeto que já usa inglês.

Existem dois modos de aplicação. Escolha um antes de agir.

## Modo padrão — escrever ou editar código (comportamento default)

Aplicar silenciosamente estas regras em qualquer código gerado ou editado, sem produzir relatório — o relatório completo é só para o modo auditoria abaixo. Para uma tarefa pequena (um script, uma função, um trecho), isso significa simplesmente escrever direto no padrão certo, não gerar um checklist visível.

- **Nomes revelam intenção.** Nada de `dados`, `temp`, `x`, `item`, `processar()`. Se o nome não explica o que a variável guarda ou o que a função faz, ele está errado. Funções levam nome de ação (`calcularFaturamentoMensal`, não `calc`).
- **Uma função, uma responsabilidade.** Se uma função valida, salva, envia e-mail e loga ao mesmo tempo, ela deve virar várias funções menores, cada uma com um verbo claro. Tamanho não é o critério — clareza de propósito é.
- **Simples em vez de esperto.** Prefira código explícito e um pouco mais longo a uma linha compacta com encadeamento de `?.`, `??`, `&&` difícil de ler de relance. Ninguém deve precisar reler uma linha três vezes para saber o que ela faz.
- **Sem duplicação de regra.** Se a mesma conta, validação ou número mágico aparece em mais de um lugar, extraia para uma constante ou função nomeada antes de continuar.
- **Comentário só quando o código não consegue falar sozinho.** Não comente o óbvio (`// verifica se está ativo` acima de um `if (user.isActive)`). Comente decisão técnica não óbvia, regra de negócio específica, ou motivo de uma solução estranha.
- **Erros nunca somem em silêncio.** Nada de `catch (e) {}` vazio. Trate, logue com contexto útil, ou relance com uma mensagem que ajude a próxima pessoa a entender o que aconteceu.
- **Regra de negócio separada de detalhe técnico.** O "porquê" (regra de negócio) não deve ficar escondido dentro do "como" (chamada de banco, requisição HTTP, render de tela).
- **Sem abstração especulativa.** Não crie camada, factory ou interface para um caso de uso único "porque pode precisar no futuro". Abstração se justifica quando já existe duplicação real ou repetição comprovada — não antes.

Se qualquer uma dessas regras conflitar com um padrão já estabelecido no projeto em que está trabalhando, siga o padrão do projeto e avise sobre a inconsistência em vez de misturar estilos no mesmo arquivo.

## Modo auditoria — revisão ou refatoração explícita de código existente

Acionar este modo quando o usuário pedir para revisar, auditar ou refatorar código que já existe (não para código sendo escrito do zero). Aqui sim produza um relatório visível, seguindo esta ordem de trabalho:

1. Identificar nomes genéricos, confusos ou pouco descritivos.
2. Identificar funções grandes ou com responsabilidades demais.
3. Identificar duplicação de lógica, validação ou regra de negócio.
4. Identificar comentários desnecessários, óbvios ou desatualizados — e a ausência de comentário onde havia decisão técnica importante.
5. Melhorar tratamento de erro e casos de borda.
6. Remover import, variável, função ou arquivo morto — só quando houver segurança de que não é usado indiretamente em outro lugar.
7. Melhorar organização de arquivo sem alterar arquitetura fora do escopo pedido.
8. Sugerir ou criar testes quando fizer sentido.
9. Explicar cada mudança feita e por quê.

**Restrições rígidas do modo auditoria:**
- Não alterar regra de negócio sem apontar isso explicitamente.
- Não fazer refatoração ampla não pedida — priorizar sempre a menor alteração seguras.
- Não criar abstração nova sem necessidade comprovada no próprio código analisado.
- Não remover teste existente.
- Não alterar comportamento visível ao usuário final sem ter sido solicitado.
- Não tocar em arquivo fora do escopo sem avisar antes.

**Formato de saída obrigatório** (markdown):

```
## Diagnóstico rápido
## Problemas encontrados
## Melhorias aplicadas ou recomendadas
## Arquivos alterados
## Riscos técnicos
## Como testar
## Checklist final
```

Antes de entregar, confirme mentalmente: o código ficou mais legível, o comportamento atual foi preservado, as responsabilidades ficaram mais claras, nenhuma abstração desnecessária foi criada, nada fora do escopo foi tocado, e existe um jeito claro de o usuário testar a mudança.

## Guardrails gerais (valem nos dois modos)

Um dos maiores riscos de aplicar Clean Code de forma automática é exagerar. Evite:
- Refatorar mais do que o pedido exige.
- Renomear coisas em excesso só por preferência estética.
- Alterar comportamento sem perceber, ao "limpar" um trecho.
- Remover código que parece morto mas é usado indiretamente (reflection, import dinâmico, rota registrada em outro arquivo, etc.) — se não tiver certeza, pergunte ou deixe.
- Quebrar uma função útil em pedaços tão pequenos que a leitura fica pior, não melhor.
- Adicionar complexidade (camadas, padrões de projeto) só para parecer mais "profissional".

Regra de ouro: Clean Code deve deixar o código mais fácil, nunca mais complicado.

## Referência ampliada

O arquivo `references/principios.md` tem a explicação estendida de cada princípio (com analogias e exemplos adicionais de código). Ele não precisa ser lido para aplicar as regras acima no dia a dia — só vale abrir se for necessário fundamentar uma decisão específica em mais detalhe (por exemplo, para explicar ao usuário por que uma função está sendo dividida, ou por que um nível de acoplamento é problemático).
