# Nomenclatura PT-BR — vocabulário de referência

Material de apoio para o `SKILL.md`. Abrir quando for preciso decidir um nome concreto (variável, função, booleano, constante) ou justificar por que um nome existente está ruim. As regras de decisão já estão resumidas no `SKILL.md` — aqui está o vocabulário.

## Quando o nome vai em português

Português PT-BR é o padrão para o que é **seu**: domínio, regra de negócio, funções internas, variáveis internas, classes próprias e módulos próprios.

Inglês quando:

- a linguagem, o framework ou a biblioteca exigir;
- a API externa ou o contrato já existente estiver em inglês;
- o padrão dominante do projeto já for inglês;
- traduzir quebrar compatibilidade.

Regra de desempate: **projeto existente manda.** Em código novo sem padrão prévio, use PT-BR. Em projeto que já é inglês, siga o inglês e aponte a inconsistência em vez de misturar dois idiomas no mesmo arquivo.

## Sem acento e sem cedilha em identificador

```text
# errado                  # certo
usuário                   usuario
validação                 validacao
permissão                 permissao
relatório                 relatorio
configuração              configuracao
```

Acento vale para texto exibido ao usuário e para comentário — nunca para nome de identificador.

## Variáveis

Devem explicar o valor guardado.

```text
# evite                   # prefira
data                      usuarioAtivo
info                      clienteSelecionado
obj                       notasPendentes
item                      valorTotalPedido
temp                      resultadoValidacao
aux                       prazoCalculado
valor / resultado / x
```

## Funções

Começam com verbo e indicam a ação.

Verbos de referência:

```text
buscar    obter      listar     criar      validar
verificar calcular   gerar      formatar   converter
montar    preparar   salvar     atualizar  remover
enviar    registrar
```

```text
# bons
validarCpfCliente
buscarUsuarioPorEmail
calcularValorTotalPedido
gerarRelatorioMensal
formatarDataBrasileira
verificarPermissaoUsuario

# genéricos demais — só com contexto que deixe a ação óbvia
processar   executar   handle   fazer   tratar   dados
```

## Booleanos

Devem soar como pergunta de verdadeiro ou falso.

```text
# prefira                 # evite
usuarioEstaAtivo          ativo
clientePossuiPermissao    status
pedidoFoiPago             flag
deveEnviarEmail           controle
podeEditarNota            permissao
temAnexo
existePrazoAberto
```

## Listas

Sempre no plural.

```text
usuarios   clientes   notasPendentes   prazosVencidos   pedidosAprovados
```

## Constantes

Nome claro e, quando o projeto permitir, `UPPER_SNAKE_CASE`.

```text
LIMITE_MAXIMO_TENTATIVAS_LOGIN
VALOR_MINIMO_PEDIDO
PRAZO_PADRAO_RESPOSTA_DIAS
```

Número mágico solto no código é sempre um nome faltando.

## Checklist rápido de nomes

- [ ] O nome explica o propósito sem precisar ler a implementação?
- [ ] Está sem acento e sem cedilha?
- [ ] O idioma segue o padrão do projeto (e não mistura os dois no mesmo arquivo)?
- [ ] Função começa com verbo?
- [ ] Booleano soa como pergunta?
- [ ] Lista está no plural?
- [ ] Nenhum contrato externo (API, biblioteca, framework) foi traduzido indevidamente?
