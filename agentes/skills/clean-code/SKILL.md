---
name: clean-code
description: >
  Aplica o padrão pessoal de código do usuário com foco em NOMENCLATURA — nomes
  que revelam intenção, identificadores em PT-BR sem acento, verbo em função,
  booleano como pergunta, lista no plural, constante nomeada — mais um mínimo de
  legibilidade (uma responsabilidade por função, regra de negócio sem duplicação,
  erro que nunca some em silêncio). Usar SEMPRE que for escrever, gerar, editar
  ou revisar qualquer trecho de código, em qualquer linguagem ou projeto. Quanto
  código escrever (escopo mínimo, dependências, abstração) é da skill ponytail.
  Quando o pedido for revisar, auditar ou refatorar código existente ("revise
  esse código", "aplique clean code", "esses nomes estão ruins"), seguir o modo
  auditoria com relatório.
---

# Clean Code — padrão pessoal (nomenclatura primeiro)

O que o usuário mais exige é **nome bem dado**: código é lido muitas vezes mais do que é escrito, e o nome é o que permite outra pessoa (ou outra IA) entender a intenção sem ler a implementação.

**Divisão com a skill `ponytail`:** o Ponytail decide **quanto** código escrever (precisa existir? já existe? nativo? dependência? uma linha?). Esta skill decide **como o código se lê**: nomes, em primeiro lugar, e o mínimo de organização abaixo. As duas valem juntas; não repita aqui o que é do Ponytail.

**Idioma:** comunicação, comentários e relatório em português do Brasil, direto e simples.

## 1. Nomenclatura — o núcleo (sempre, sem relatório)

**Idioma do identificador**
- Código novo sem padrão prévio: o que é **seu** (domínio, regra de negócio, funções, variáveis, módulos) vai em **PT-BR**.
- Inglês quando a linguagem, o framework ou a biblioteca exigir, quando a API ou o contrato externo for inglês, ou quando o projeto já for inglês. **Projeto existente manda**: siga o padrão dele e aponte a inconsistência, sem misturar idiomas no mesmo arquivo.
- Nunca traduza nome de API, biblioteca, framework ou contrato externo.

**Sem acento e sem cedilha** em identificador: `usuario`, `validacao`, `permissao`, `relatorio`, `configuracao`. Acento só em texto para o usuário e em comentário.

| Tipo | Regra | Bom | Evite |
| --- | --- | --- | --- |
| Variável | Diz o que o valor guarda | `usuarioAtivo`, `valorTotalPedido`, `prazoCalculado` | `data`, `info`, `obj`, `item`, `temp`, `aux`, `x` |
| Função | Começa com verbo e diz a ação | `buscarUsuarioPorEmail`, `calcularValorTotalPedido`, `validarCpfCliente` | `processar`, `executar`, `handle`, `fazer`, `tratar` (sem contexto) |
| Booleano | Soa como pergunta de sim/não | `usuarioEstaAtivo`, `pedidoFoiPago`, `podeEditarNota`, `temAnexo` | `ativo`, `status`, `flag`, `controle` |
| Lista | Plural | `usuarios`, `notasPendentes`, `pedidosAprovados` | `listaUsuario`, `usuarioArray` |
| Constante | Nome claro, `UPPER_SNAKE_CASE` se o projeto permitir | `LIMITE_MAXIMO_TENTATIVAS_LOGIN`, `PRAZO_PADRAO_RESPOSTA_DIAS` | número mágico solto |

Verbos de referência: `buscar`, `obter`, `listar`, `criar`, `validar`, `verificar`, `calcular`, `gerar`, `formatar`, `converter`, `montar`, `preparar`, `salvar`, `atualizar`, `remover`, `enviar`, `registrar`.

**Número mágico solto é sempre um nome faltando.**

**Checklist de cada nome:** explica o propósito sem ler a implementação? Está sem acento? Segue o idioma do projeto? Função começa com verbo? Booleano soa como pergunta? Lista no plural? Nenhum contrato externo traduzido?

Vocabulário completo e mais exemplos: `references/nomenclatura-ptbr.md`.

## 2. Legibilidade — o mínimo (sempre, sem relatório)

- **Uma função, uma responsabilidade.** Se valida, salva, envia e-mail e loga, vira funções com um verbo cada. O critério é clareza de propósito, não tamanho.
- **Regra de negócio sem duplicação.** A mesma conta, validação ou limite em dois lugares vira uma constante ou função nomeada.
- **Regra de negócio separada do detalhe técnico.** O "porquê" não fica escondido dentro da chamada de banco, da requisição HTTP ou do render.
- **Erro nunca some em silêncio.** Nada de `catch (e) {}` vazio: trate, logue com contexto ou relance com mensagem útil.

Se uma regra conflitar com padrão já estabelecido no projeto, siga o projeto e avise.

## 3. Modo auditoria — revisar ou refatorar código existente

Acionar quando o usuário pedir revisão, auditoria ou refatoração. Ordem de trabalho:

1. **Nomes** genéricos, confusos, com acento, no idioma errado, booleano que não é pergunta, lista no singular, número mágico. É a prioridade.
2. Funções com responsabilidade demais.
3. Regra de negócio duplicada.
4. Erro engolido ou sem contexto.
5. Excesso de código, dependência desnecessária ou abstração especulativa: aponte e aplique a skill `ponytail`.

**Restrições:** não alterar regra de negócio nem comportamento visível sem apontar; não fazer refatoração ampla não pedida; não renomear contrato externo ou API pública sem avisar do impacto; não tocar fora do escopo sem avisar; não remover teste.

**Formato de saída** (markdown):

```
## Diagnóstico rápido
## Nomes a corrigir (atual → proposto, motivo)
## Outros problemas encontrados
## Melhorias aplicadas ou recomendadas
## Arquivos alterados
## Riscos técnicos
## Como testar
```

## Guardrails

- Não renomear em excesso por gosto estético: renomeie quando o nome atual engana ou não diz nada.
- Renomear símbolo usado em vários arquivos é mudança de escopo: liste os pontos afetados antes.
- Não quebrar função útil em pedaços tão pequenos que a leitura piore.
- Regra de ouro: o código tem que ficar mais fácil de ler, nunca mais complicado.

## Referências

- `references/nomenclatura-ptbr.md` — vocabulário de nomes em PT-BR com exemplos. Abrir quando a dúvida for um nome concreto.
- `references/principios.md` — explicação estendida dos princípios, com analogias. Abrir para fundamentar uma decisão.
