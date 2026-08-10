# Clean Code — princípios detalhados

Material de apoio para o SKILL.md principal. Abrir apenas quando for necessário fundamentar uma explicação em mais profundidade — as regras operacionais já estão resumidas no SKILL.md.

## 1. Código é lido mais vezes do que é escrito

Você escreve uma vez, mas depois vai corrigir bug, adicionar função, explicar para outra pessoa, revisar com IA, testar e manter no futuro. Código bom não é só código que funciona — é código que comunica intenção.

```tsx
// ruim
const x = u.filter(a => a.s === true);

// melhor
const usuariosAtivos = usuarios.filter(usuario => usuario.ativo);
```

Se você precisa explicar demais o que o código faz, o próprio código provavelmente não está claro o suficiente.

## 2. Nomes revelam intenção

```tsx
// ruins: vagos, não explicam propósito
const dados = [];
const item = {};
const temp = 10;
function processar() {}

// melhores
const faturasPendentes = [];
const clienteSelecionado = {};
const maxTentativasLogin = 10;
function calcularFaturamentoMensal() {}
```

Regras práticas: nomes específicos, sem abreviação confusa, sem `data`/`info`/`obj`/`temp`/`x`/`y`; função leva nome de ação; variável representa claramente o valor guardado; classe/módulo representa uma responsabilidade clara.

Analogia: nome ruim é como uma pasta chamada "coisas". Nome bom é como uma pasta chamada "contratos-clientes-2026".

## 3. Funções pequenas, uma responsabilidade

```tsx
// ruim: várias responsabilidades numa função só
async function criarUsuario(dadosEntrada) {
  // valida, cria, salva, envia e-mail, loga, retorna
}

// melhor
async function criarUsuario(dadosEntrada) {
  validarDadosUsuario(dadosEntrada);
  const usuario = montarUsuario(dadosEntrada);
  const usuarioSalvo = await usuarioRepository.salvar(usuario);
  await enviarEmailBoasVindas(usuarioSalvo.email);
  await registrarLogCriacaoUsuario(usuarioSalvo.id);
  return usuarioSalvo;
}
```

Função não precisa ser minúscula sempre — precisa ser compreensível e ter responsabilidade bem definida. Evite muitos níveis aninhados de `if`/`for`/`try`. Se um trecho precisa de comentário para ser entendido, considere transformá-lo numa função com nome claro.

## 4. Simples, não esperto

```tsx
// compacto demais
const resultado = usuarios?.filter(u => u.a && !u.b)?.map(u => ({ ...u, x: true })) ?? [];

// claro
const usuariosAtivosSemBloqueio = usuarios.filter(usuario => usuario.ativo && !usuario.bloqueado);
const usuariosFormatados = usuariosAtivosSemBloqueio.map(usuario => ({ ...usuario, podeAcessarSistema: true }));
```

Código limpo não tenta impressionar, tenta ser entendido.

## 5. Evite duplicação

```tsx
// duplicado
const descontoUsuario = usuario.total * 0.1;
const descontoPedido = pedido.total * 0.1;
const descontoProduto = produto.preco * 0.1;

// centralizado
const TAXA_DESCONTO_PADRAO = 0.1;
function calcularDesconto(valor: number) {
  return valor * TAXA_DESCONTO_PADRAO;
}
```

Analogia: duplicação é como anotar a mesma senha em cinco cadernos diferentes — quando a senha muda, é fácil esquecer de atualizar algum.

## 6. Comentários não compensam código ruim

```tsx
// desnecessário — o código já explica
if (usuario.ativo) { permitirAcesso(); }

// útil — explica uma decisão não óbvia
const idCliente = entrada.idCliente ?? entrada.idLegado; // fallback: clientes antigos ainda enviam idLegado
```

Comente decisões técnicas, regras de negócio específicas, limitações conhecidas, motivo de solução não óbvia, comportamento temporário, integrações externas estranhas. Comentário desatualizado é pior que ausência de comentário — engana quem lê.

## 7. Organização visual

Ordem natural sugerida num arquivo: imports → tipos/interfaces → constantes → função principal → funções auxiliares → exportações. Remova import não usado e variável morta, agrupe funções relacionadas, siga o padrão já existente no projeto.

## 8. Tratamento de erro claro

```tsx
// silencioso — esconde o problema
try { await salvarUsuario(usuario); } catch (erro) {}

// tratado
try {
  await salvarUsuario(usuario);
} catch (erro) {
  logger.error("Erro ao salvar usuário", erro);
  throw new Error("Não foi possível salvar o usuário.");
}
```

Não ignore erro, não use `try/catch` vazio, não retorne `null` sem motivo claro, trate casos de borda, valide entradas importantes.

## 9. Testes fazem parte do código limpo

Se uma função é difícil de testar, ela provavelmente está fazendo coisas demais ou está muito acoplada a outras partes do sistema.

```tsx
it("deve retornar erro quando o e-mail é inválido", () => {
  const resultado = validarEmail("email-invalido");
  expect(resultado.valido).toBe(false);
});
```

O nome do teste deve explicar o comportamento esperado. Teste regra importante, caso de erro e caso de sucesso. Não remova teste existente sem justificativa.

## 10. Responsabilidade única

Vale para função, classe, componente, arquivo, módulo, serviço, controller, hook, página.

```
ruim:               melhor:
GerenciadorUsuario  ValidadorUsuario   → valida dados
- valida            RepositorioUsuario → acessa banco
- salva             ServicoUsuario     → regras de negócio
- envia e-mail      ServicoEmail       → envia e-mails
- gera relatório    ControllerUsuario  → recebe requisição, retorna resposta
- renderiza tela
- loga
```

Se um arquivo tem muitos motivos para mudar, ele provavelmente tem responsabilidades demais.

## 11. Regra de negócio separada de detalhe técnico

Regra de negócio (o "porquê") deve ser fácil de encontrar e testar — não deve ficar escondida dentro de detalhe de banco, tela ou API (o "como"). Evite lógica de negócio pesada dentro de componente visual, e lógica de tela dentro de serviço.

## 12. Acoplamento excessivo

Sinais de acoplamento ruim: uma função precisa conhecer detalhes internos de outra; um componente depende diretamente de muitos serviços; mudança pequena exige alteração em muitos arquivos; testar uma função exige subir o sistema inteiro; regra de negócio espalhada em vários lugares.

Como melhorar: separar responsabilidades, funções pequenas, interfaces quando fizer sentido, centralizar regra compartilhada, não passar objeto gigante quando só precisa de um campo.

## 13. Evite overengineering

Não crie abstração antes de existir necessidade real. Crie abstração quando já existe duplicação real, a regra aparece em vários lugares, a mudança futura é provável e concreta, melhora leitura, facilita teste ou reduz dependência entre partes do sistema. Evite quando será usada uma única vez, deixa o código mais difícil, cria arquivos demais, tenta prever um futuro incerto, ou complica uma regra simples.

## 14. Refatoração segura

Refatorar é melhorar a estrutura interna sem mudar comportamento externo. Faça mudanças pequenas por vez, preserve comportamento atual, rode teste depois, evite refatorar tudo de uma vez, explique o motivo, não misture refatoração com criação de funcionalidade grande, não altere regra de negócio sem necessidade.

## Glossário

- **Legibilidade** — capacidade de entender o código rapidamente.
- **Manutenibilidade** — facilidade de alterar o código no futuro.
- **Coesão** — quando uma função/classe/módulo tem responsabilidade bem conectada.
- **Acoplamento** — grau de dependência entre partes diferentes do sistema.
- **Abstração** — esconder detalhe complexo atrás de interface mais simples.
- **Código morto** — função antiga, import inútil, variável abandonada, não mais usada.
- **Número mágico** — valor solto no código sem explicação (`if (tentativas > 3)` em vez de `MAX_TENTATIVAS_LOGIN`).
