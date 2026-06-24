---
name: clean-code
description: Use esta skill para revisar, implementar ou refatorar código aplicando Clean Code, nomenclatura em português PT-BR, simplicidade, responsabilidade única, menor alteração segura e preservação de comportamento.
---

# Clean Code — PT-BR

## Objetivo

Aplicar Clean Code de forma prática durante criação, revisão ou refatoração de código.

Priorize código:

- fácil de ler;
- fácil de entender;
- fácil de testar;
- fácil de manter;
- com nomes claros em português PT-BR;
- sem mudança inesperada de comportamento.

Clean Code não é reescrever tudo. É melhorar clareza e manutenção com a menor alteração segura.

---

## Quando usar

Use esta skill quando a tarefa envolver:

- criar código novo;
- revisar código existente;
- refatorar funções, classes, componentes, services, controllers ou módulos;
- melhorar nomes;
- reduzir duplicação;
- separar responsabilidades;
- melhorar tratamento de erro;
- tornar código mais testável;
- avaliar risco de overengineering.

---

## Regra principal

Antes de alterar qualquer código:

1. Entenda o comportamento atual.
2. Preserve o que já funciona.
3. Siga o padrão existente do projeto.
4. Faça a menor alteração segura.
5. Não altere regra de negócio sem necessidade.
6. Não crie abstração antes de existir necessidade real.

---

## Nomenclatura em português PT-BR

Use nomes em português PT-BR para domínio, regras de negócio, funções internas, variáveis internas, classes próprias e módulos próprios.

Use inglês somente quando:

- a linguagem exigir;
- o framework exigir;
- a biblioteca exigir;
- a API externa exigir;
- o contrato existente estiver em inglês;
- o padrão dominante do projeto estiver em inglês;
- traduzir quebrar compatibilidade.

Não use acentos, cedilha ou espaços em nomes de código.

Errado:

```text
usuário
validação
permissão
relatório
configuração
````

Certo:

```text
usuario
validacao
permissao
relatorio
configuracao
```

---

## Boas práticas de nomes

### Variáveis

Variáveis devem explicar claramente o valor armazenado.

Evite:

```text
data
info
obj
item
temp
aux
valor
resultado
retorno
x
y
```

Prefira:

```text
usuarioAtivo
clienteSelecionado
notasPendentes
valorTotalPedido
resultadoValidacao
prazoCalculado
```

### Funções

Funções devem começar com verbo e indicar ação clara.

Bons verbos:

```text
buscar
obter
listar
criar
validar
verificar
calcular
gerar
formatar
converter
montar
preparar
salvar
atualizar
remover
enviar
registrar
processar
```

Exemplos bons:

```text
validarCpfCliente
buscarUsuarioPorEmail
calcularValorTotalPedido
gerarRelatorioMensal
formatarDataBrasileira
verificarPermissaoUsuario
```

Evite funções genéricas:

```text
processar
executar
handle
fazer
tratar
dados
```

Use esses nomes apenas quando o contexto deixar a ação muito clara.

### Booleanos

Booleanos devem parecer perguntas de verdadeiro ou falso.

Prefira:

```text
usuarioEstaAtivo
clientePossuiPermissao
pedidoFoiPago
deveEnviarEmail
podeEditarNota
temAnexo
existePrazoAberto
```

Evite:

```text
ativo
status
flag
controle
permissao
```

### Listas

Listas devem estar no plural.

```text
usuarios
clientes
notasPendentes
prazosVencidos
pedidosAprovados
```

### Constantes

Use nomes claros e, quando o projeto permitir, `UPPER_SNAKE_CASE`.

```text
LIMITE_MAXIMO_TENTATIVAS_LOGIN
VALOR_MINIMO_PEDIDO
PRAZO_PADRAO_RESPOSTA_DIAS
```

Não deixe números mágicos soltos no código.

---

## Princípios obrigatórios

### 1. Clareza acima de esperteza

Não compacte lógica só para parecer avançado.

Código limpo não tenta impressionar. Código limpo tenta ser entendido.

### 2. Responsabilidade única

Cada função, classe, componente ou módulo deve ter um motivo principal para mudar.

Se uma função valida, salva, envia e-mail, registra log e formata resposta, ela está fazendo coisas demais.

### 3. Simplicidade

Não crie camadas, factories, managers, helpers ou abstrações sem necessidade real.

Crie abstração apenas quando:

* existe duplicação real;
* melhora a leitura;
* reduz acoplamento;
* facilita teste;
* representa uma regra reutilizável.

### 4. Evite duplicação

Não repita:

* regra de negócio;
* validação;
* cálculo;
* mensagem;
* consulta;
* transformação de dados;
* tratamento de erro.

Centralize apenas quando houver ganho real de manutenção.

### 5. Comentários não compensam código ruim

Antes de comentar, tente melhorar nomes, funções e organização.

Use comentários para explicar:

* decisão técnica;
* regra de negócio não óbvia;
* compatibilidade com legado;
* limitação conhecida;
* integração externa estranha;
* motivo de solução temporária.

Evite comentários que só repetem o código.

### 6. Tratamento de erro claro

Não aceite:

```text
catch vazio
erro ignorado
retorno null sem motivo
mensagem genérica demais
falha silenciosa
```

Erros devem indicar contexto suficiente para entender e debugar, sem expor dados sensíveis.

### 7. Testabilidade

Ao alterar código, avalie:

* a regra ficou fácil de testar?
* a função tem entrada e saída claras?
* há casos de sucesso e erro?
* alguma regra importante precisa de teste?
* o comportamento antigo foi preservado?

Não remova testes sem justificativa.

---

## Processo de aplicação

Ao usar esta skill, siga esta ordem:

1. Identifique o objetivo da alteração.
2. Entenda o comportamento atual.
3. Localize o menor trecho necessário.
4. Avalie nomes, duplicação, responsabilidade, erro e testabilidade.
5. Aplique a menor melhoria segura.
6. Preserve contratos, APIs, formatos de resposta e compatibilidade com legado.
7. Indique como validar.

---

## Checklist final

Antes de concluir, verifique:

* [ ] Os nomes estão claros?
* [ ] Os nomes em português estão sem acento e sem cedilha?
* [ ] O padrão do projeto foi respeitado?
* [ ] Nenhum contrato externo foi traduzido indevidamente?
* [ ] Funções começam com verbo claro?
* [ ] Booleanos indicam verdadeiro ou falso?
* [ ] Listas estão no plural?
* [ ] Foram evitados nomes genéricos?
* [ ] Cada função tem responsabilidade principal?
* [ ] Existe duplicação desnecessária?
* [ ] O código ficou mais simples?
* [ ] O tratamento de erro está claro?
* [ ] A regra de negócio está separada de detalhe técnico?
* [ ] O comportamento existente foi preservado?
* [ ] A alteração foi a menor possível?
* [ ] Não houve overengineering?

---

## Formato de resposta

Quando aplicar esta skill, responda neste formato:

```text
## Diagnóstico

O que foi encontrado.

## Decisão

O que será feito e por quê.

## Alterações

Mudanças aplicadas ou propostas.

## Validação

Como confirmar que nada quebrou.

## Riscos

Pontos que ainda exigem atenção.

## Próximo passo

Menor próxima melhoria recomendada, se existir.
```

---

## Restrições

Não use Clean Code como desculpa para reescrever o projeto inteiro.

Não altere arquitetura sem necessidade.

Não crie abstrações prematuras.

Não mude regra de negócio sem autorização.

Não remova código legado sem confirmar uso.

Não troque o padrão do projeto por preferência pessoal.

Não adicione dependências para resolver problema simples.

Não traduza nomes de APIs, bibliotecas, frameworks ou contratos externos.

Não misture português e inglês sem motivo.

Não faça refatoração ampla quando uma melhoria local resolver.


