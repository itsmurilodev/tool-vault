# Clean Code
---

## 📌 Resumo

**Clean Code** é a prática de escrever código que seja fácil de ler, entender, alterar, testar e manter.

A ideia principal não é apenas “fazer o código funcionar”, mas fazer com que ele continue compreensível para você, para outros desenvolvedores e até para uma IA que precise revisar ou evoluir o projeto depois.

> 💡 **Analogia:** Código limpo é como uma oficina organizada. As ferramentas estão no lugar certo, cada peça tem uma função clara e qualquer pessoa consegue continuar o trabalho sem perder tempo tentando entender a bagunça.
> 

---

## 🧠 1. Código é lido mais vezes do que é escrito

Um dos princípios mais importantes do Clean Code é entender que o código será lido muitas vezes depois de ser escrito.

Você escreve uma vez, mas depois precisa:

- corrigir bugs;
- adicionar novas funções;
- explicar para outra pessoa;
- revisar com uma IA;
- testar;
- manter no futuro.

Por isso, código bom não é só código que funciona. Código bom é código que comunica intenção.

### ❌ Código difícil de entender

```tsx
const x = u.filter(a => a.s === true);
```

### ✅ Código mais limpo

```tsx
const activeUsers = users.filter(user => user.isActive);
```

> ⚠️ Se você precisa explicar demais o que o código faz, talvez o próprio código não esteja claro o suficiente.
> 

---

## 🧾 2. Nomes devem revelar intenção

Nomes são uma das partes mais importantes do Clean Code. Um bom nome deve explicar o que uma variável, função, classe ou arquivo representa.

### Nomes ruins

```tsx
const data = [];
const item = {};
const temp = 10;
function process() {}
```

Esses nomes são vagos. Eles não explicam o propósito real.

### Nomes melhores

```tsx
const pendingInvoices = [];
const selectedCustomer = {};
const maxLoginAttempts = 10;
function calculateMonthlyRevenue() {}
```

### Regras práticas

- Use nomes específicos.
- Evite abreviações confusas.
- Evite nomes genéricos como `data`, `info`, `obj`, `temp`, `x`, `y`.
- Uma função deve ter nome de ação.
- Uma variável deve representar claramente o valor armazenado.
- Uma classe ou módulo deve representar uma responsabilidade clara.

> 💡 **Analogia:** Nome ruim é como uma pasta chamada “coisas”. Nome bom é como uma pasta chamada “contratos-clientes-2026”.
> 

---

## 🧱 3. Funções devem ser pequenas e fazer uma coisa

Uma função limpa deve ter uma responsabilidade principal.

Se uma função valida dados, salva no banco, envia e-mail, atualiza log e formata resposta, ela está fazendo coisas demais.

### ❌ Função com responsabilidades demais

```tsx
async function createUser(input) {
  // valida dados
  // cria usuário
  // salva no banco
  // envia e-mail
  // cria log
  // retorna resposta
}
```

### ✅ Função mais organizada

```tsx
async function createUser(input) {
  validateUserInput(input);

  const user = buildUser(input);
  const savedUser = await userRepository.save(user);

  await sendWelcomeEmail(savedUser.email);
  await registerUserCreationLog(savedUser.id);

  return savedUser;
}
```

### Regras práticas

- Cada função deve ter um objetivo claro.
- Funções grandes devem ser divididas.
- Evite muitos níveis de `if`, `else`, `for` e `try/catch`.
- Se um trecho de código precisa de comentário para ser entendido, talvez ele mereça virar uma função com nome claro.
- Evite funções que fazem “um pouco de tudo”.

> ⚠️ Uma função não precisa ser minúscula sempre. Ela precisa ser compreensível e ter uma responsabilidade bem definida.
> 

---

## 🧩 4. Código deve ser simples, não esperto

Clean Code valoriza simplicidade. Um código muito “inteligente”, cheio de atalhos, truques e lógica compactada, pode parecer bonito, mas ser ruim para manutenção.

### ❌ Código compacto demais

```tsx
const result = users?.filter(u => u.a && !u.b)?.map(u => ({ ...u, x: true })) ?? [];
```

### ✅ Código mais claro

```tsx
const activeUsersWithoutBlock = users.filter(user => {
  return user.isActive && !user.isBlocked;
});

const formattedUsers = activeUsersWithoutBlock.map(user => {
  return {
    ...user,
    canAccessSystem: true,
  };
});
```

### Regra principal

> Código limpo não tenta impressionar. Código limpo tenta ser entendido.
> 

---

## 🔁 5. Evite duplicação

Duplicação é um dos maiores inimigos da manutenção.

Quando a mesma regra aparece em vários lugares, qualquer mudança futura precisa ser feita em vários pontos. Isso aumenta a chance de erro.

### ❌ Código duplicado

```tsx
const userDiscount = user.total * 0.1;
const orderDiscount = order.total * 0.1;
const productDiscount = product.price * 0.1;
```

### ✅ Código centralizado

```tsx
const DEFAULT_DISCOUNT_RATE = 0.1;

function calculateDiscount(value: number) {
  return value * DEFAULT_DISCOUNT_RATE;
}
```

### Regras práticas

- Não repita regras de negócio.
- Não repita validações importantes.
- Não espalhe números mágicos pelo código.
- Use constantes com nomes claros.
- Extraia funções reutilizáveis quando fizer sentido.

> 💡 **Analogia:** Duplicação é como anotar a mesma senha em cinco cadernos diferentes. Quando a senha muda, você pode esquecer de atualizar algum.
> 

---

## 🧼 6. Comentários não devem compensar código ruim

Comentários são úteis, mas não devem ser usados para explicar código confuso.

Primeiro, tente deixar o código mais claro com bons nomes, funções menores e melhor organização.

### ❌ Comentário desnecessário

```tsx
// Verifica se o usuário está ativo
if (user.isActive) {
  allowAccess();
}
```

O código já explica isso.

### ✅ Comentário útil

```tsx
// Mantemos esse fallback porque clientes antigos ainda enviam legacyId.
const customerId = input.customerId ?? input.legacyId;
```

### Quando comentar

Use comentários para explicar:

- decisões técnicas;
- regras de negócio específicas;
- limitações conhecidas;
- motivos de uma solução não óbvia;
- comportamento temporário;
- integrações externas estranhas.

### Quando evitar

Evite comentários que apenas repetem o código.

> ⚠️ Comentário desatualizado é pior que ausência de comentário, porque engana quem está lendo.
> 

---

## 🧱 7. Código deve ter boa organização visual

A forma como o código é organizado influencia diretamente na leitura.

Um arquivo limpo deve ter uma ordem natural.

### Exemplo de organização

```tsx
// 1. Imports
// 2. Tipos e interfaces
// 3. Constantes
// 4. Função principal
// 5. Funções auxiliares
// 6. Exportações
```

### Regras práticas

- Remova imports não usados.
- Remova variáveis mortas.
- Evite arquivos enormes.
- Agrupe funções relacionadas.
- Use espaçamento para separar blocos lógicos.
- Siga o padrão já existente no projeto.
- Não misture estilos diferentes no mesmo arquivo.

> 💡 **Analogia:** Um arquivo de código é como uma página de Notion. Se tudo estiver jogado sem títulos, blocos e ordem, fica cansativo de ler.
> 

---

## ⚠️ 8. Tratamento de erros deve ser claro

Um erro bem tratado ajuda a entender o que aconteceu e facilita a correção.

### ❌ Erro silencioso

```tsx
try {
  await saveUser(user);
} catch (error) {}
```

Esse código esconde o problema.

### ✅ Erro tratado melhor

```tsx
try {
  await saveUser(user);
} catch (error) {
  logger.error("Erro ao salvar usuário", error);
  throw new Error("Não foi possível salvar o usuário.");
}
```

### Regras práticas

- Não ignore erros.
- Não use `try/catch` vazio.
- Não retorne `null` sem motivo claro.
- Use mensagens de erro úteis.
- Trate casos de borda.
- Valide entradas importantes.
- Evite deixar o sistema falhar de forma inesperada.

> ⚠️ Um erro escondido hoje pode virar um bug difícil de encontrar amanhã.
> 

---

## 🧪 9. Testes fazem parte do código limpo

Código limpo precisa ser testável.

Se uma função é difícil de testar, talvez ela esteja fazendo coisas demais ou esteja muito acoplada a outras partes do sistema.

### Exemplo de teste claro

```tsx
it("should return an error when email is invalid", () => {
  const result = validateEmail("email-invalido");

  expect(result.isValid).toBe(false);
});
```

### Regras práticas

- O nome do teste deve explicar o comportamento esperado.
- Teste regras importantes.
- Teste casos de erro.
- Teste casos de sucesso.
- Não remova testes existentes sem justificativa.
- Evite testes frágeis que quebram por detalhes irrelevantes.
- Sempre que alterar regra de negócio, pense em como validar.

> 💡 **Analogia:** Teste é como cinto de segurança. Você não usa porque espera bater, usa porque sabe que imprevistos acontecem.
> 

---

## 🧠 10. Responsabilidade única

Cada parte do sistema deve ter uma responsabilidade clara.

Esse princípio vale para:

- funções;
- classes;
- componentes;
- arquivos;
- módulos;
- serviços;
- controllers;
- hooks;
- páginas.

### ❌ Exemplo ruim

```
UserManager
- valida usuário
- salva no banco
- envia e-mail
- gera relatório
- renderiza tela
- faz log
```

### ✅ Exemplo melhor

```
UserValidator
- valida dados do usuário

UserRepository
- acessa o banco de dados

UserService
- executa regras de negócio

EmailService
- envia e-mails

UserController
- recebe requisição e retorna resposta
```

### Regra prática

> Se um arquivo tem muitos motivos para mudar, talvez ele tenha responsabilidades demais.
> 

---

## 🏗️ 11. Separação entre regra de negócio e detalhes técnicos

Um código limpo separa o que é regra importante do sistema e o que é detalhe de implementação.

### Exemplo

Regra de negócio:

```
Usuário menor de idade não pode criar conta empresarial.
```

Detalhe técnico:

```
Salvar usuário no PostgreSQL.
Enviar e-mail via Resend.
Renderizar botão com Tailwind.
```

A regra de negócio deve ser fácil de encontrar e testar. Ela não deve ficar escondida dentro de detalhes de banco, tela ou API.

### Regras práticas

- Evite colocar regra de negócio pesada dentro de componentes visuais.
- Evite colocar lógica de tela dentro de serviços.
- Evite misturar validação, banco e interface no mesmo lugar.
- Separe entrada, processamento e saída.

> 💡 **Analogia:** A regra de negócio é o “porquê”. O banco, a API e a interface são apenas o “como”.
> 

---

## 📦 12. Evite acoplamento excessivo

Acoplamento acontece quando uma parte do código depende demais de outra.

Quanto maior o acoplamento, mais difícil é alterar uma coisa sem quebrar outra.

### Sinais de acoplamento ruim

- Uma função precisa conhecer detalhes internos de outra.
- Um componente depende diretamente de muitos serviços.
- Uma mudança pequena exige alteração em muitos arquivos.
- Testar uma função exige subir o sistema inteiro.
- Regras de negócio estão espalhadas em vários lugares.

### Como melhorar

- Separe responsabilidades.
- Use funções pequenas.
- Crie interfaces quando fizer sentido.
- Evite dependências desnecessárias.
- Centralize regras compartilhadas.
- Não passe objetos gigantes quando só precisa de um campo.

---

## 🧰 13. Evite overengineering

Clean Code não significa transformar tudo em arquitetura complexa.

Às vezes, a melhor solução é simples.

### ❌ Exagero

Criar:

```
UserFactoryProviderManagerServiceHandler
```

para apenas montar um objeto simples.

### ✅ Melhor

```tsx
function createUserPayload(input: CreateUserInput) {
  return {
    name: input.name,
    email: input.email,
  };
}
```

### Regra principal

> Não crie abstração antes de existir uma necessidade real.
> 

### Quando criar abstração

Crie abstrações quando:

- existe duplicação real;
- a regra aparece em vários lugares;
- a mudança futura é provável;
- melhora a leitura;
- facilita testes;
- reduz dependência entre partes do sistema.

### Quando evitar

Evite abstração quando:

- só será usada uma vez;
- deixa o código mais difícil;
- cria arquivos demais;
- tenta prever um futuro incerto;
- complica uma regra simples.

---

## 🧹 14. Refatoração deve ser segura

Refatorar é melhorar a estrutura interna do código sem mudar o comportamento externo.

### Boa refatoração

```
Antes:
Código funciona, mas está confuso.

Depois:
Código continua funcionando, mas está mais claro, organizado e fácil de manter.
```

### Regras práticas

- Faça pequenas mudanças por vez.
- Preserve o comportamento atual.
- Rode testes depois.
- Evite refatorar tudo de uma vez.
- Explique o motivo das mudanças.
- Não misture refatoração com criação de funcionalidade grande.
- Não altere regra de negócio sem necessidade.

> ⚠️ Refatoração boa melhora o código sem gerar surpresa para o usuário final.
> 

---

## 🔍 15. Código limpo facilita revisão por IA

Quando o código é bem organizado, a IA consegue entender melhor o projeto.

Isso melhora:

- revisão de bugs;
- geração de testes;
- refatoração;
- documentação;
- sugestões de melhoria;
- manutenção futura.

### Para facilitar o trabalho da IA

- Use nomes claros.
- Separe responsabilidades.
- Evite arquivos gigantes.
- Documente decisões importantes.
- Mantenha padrão de pastas.
- Remova código morto.
- Escreva testes claros.
- Use tipagem quando possível.

> 💡 **Analogia:** Pedir para uma IA revisar código bagunçado é como pedir para alguém arrumar um quarto no escuro. Quanto mais organizado o ambiente, melhor o resultado.
> 

---

## 🧠 16. Conceitos importantes de Clean Code

### Legibilidade

Capacidade de entender o código rapidamente.

### Manutenibilidade

Facilidade de alterar o código no futuro.

### Coesão

Quando uma função, classe ou módulo tem uma responsabilidade bem conectada.

### Acoplamento

Grau de dependência entre partes diferentes do sistema.

### Abstração

Forma de esconder detalhes complexos atrás de uma interface mais simples.

### Refatoração

Melhorar a estrutura do código sem mudar o comportamento esperado.

### Código morto

Código que não é mais usado, como funções antigas, imports inúteis e variáveis abandonadas.

### Números mágicos

Valores soltos no código sem explicação.

Exemplo ruim:

```tsx
if (attempts > 3) {}
```

Exemplo melhor:

```tsx
const MAX_LOGIN_ATTEMPTS = 3;

if (attempts > MAX_LOGIN_ATTEMPTS) {}
```

### Responsabilidade única

Cada parte do código deve ter um motivo principal para mudar.

### Testabilidade

Facilidade de criar testes para garantir que o código funciona.

---

## 🧪 17. Checklist rápido de Clean Code

Use este checklist antes de finalizar uma alteração:

- [ ]  Os nomes estão claros?
- [ ]  As funções têm uma responsabilidade principal?
- [ ]  Existe duplicação desnecessária?
- [ ]  Existem imports, variáveis ou arquivos mortos?
- [ ]  O código está simples ou ficou complexo demais?
- [ ]  O tratamento de erro está claro?
- [ ]  Os comentários explicam decisões importantes?
- [ ]  Os comentários óbvios foram removidos?
- [ ]  A regra de negócio está separada de detalhes técnicos?
- [ ]  O código segue o padrão do projeto?
- [ ]  A alteração é fácil de testar?
- [ ]  O comportamento original foi preservado?
- [ ]  Existe risco de quebrar outra parte do sistema?
- [ ]  A solução foi a menor alteração segura?

---

## 🧰 18. Como pedir para uma IA aplicar Clean Code

Use este prompt quando quiser que uma IA revise ou refatore um projeto.

```
<papel>
Você é um desenvolvedor sênior especialista em Clean Code, refatoração segura, arquitetura simples e qualidade de código.
</papel>

<objetivo>
Analise o código/projeto enviado e aplique boas práticas de Clean Code, priorizando legibilidade, simplicidade, manutenção e testabilidade.
</objetivo>

<contexto>
O objetivo não é redesenhar todo o sistema, mas melhorar a qualidade do código com segurança.
Preserve o comportamento atual e siga o padrão já existente no projeto.
</contexto>

<tarefas>
1. Identificar nomes genéricos, confusos ou pouco descritivos.
2. Identificar funções grandes ou com múltiplas responsabilidades.
3. Identificar duplicações de lógica, validação ou regra de negócio.
4. Identificar comentários desnecessários, óbvios ou desatualizados.
5. Identificar ausência de comentários quando houver decisão técnica importante.
6. Melhorar tratamento de erros e casos de borda.
7. Remover imports, variáveis, funções ou arquivos mortos, somente se houver segurança.
8. Melhorar organização dos arquivos sem alterar arquitetura fora do escopo.
9. Sugerir ou criar testes quando fizer sentido.
10. Explicar quais mudanças foram feitas e por quê.
</tarefas>

<restricoes>
- Não alterar regra de negócio sem explicar claramente.
- Não fazer refatoração grande sem necessidade.
- Não criar abstrações desnecessárias.
- Não adicionar dependências sem justificativa.
- Não remover testes existentes.
- Não alterar estilo visual, layout ou comportamento de usuário sem solicitação.
- Não mexer em arquivos fora do escopo sem avisar.
- Priorizar sempre a menor alteração segura.
</restricoes>

<formato_saida>
Retorne em Markdown:

## Diagnóstico rápido
## Problemas encontrados
## Melhorias aplicadas ou recomendadas
## Arquivos alterados
## Riscos técnicos
## Como testar
## Checklist final
</formato_saida>

<validacao_final>
Antes de finalizar, confirme:
- O código ficou mais legível.
- O comportamento atual foi preservado.
- As responsabilidades ficaram mais claras.
- Não foram criadas abstrações desnecessárias.
- Não foram feitas alterações fora do escopo.
- Existe forma clara de testar a alteração.
</validacao_final>
```

---

## ⚠️ 19. Cuidados ao usar Clean Code com IA

Nem toda sugestão de Clean Code deve ser aceita automaticamente.

A IA pode tentar:

- refatorar demais;
- criar arquitetura desnecessária;
- renomear coisas demais;
- alterar comportamento sem perceber;
- remover código que parecia inútil, mas era usado indiretamente;
- criar funções pequenas demais;
- adicionar complexidade para parecer “mais profissional”.

### Regra de ouro

> Clean Code deve deixar o projeto mais fácil, não mais complicado.
> 

Sempre peça para a IA explicar:

- o que mudou;
- por que mudou;
- quais arquivos foram afetados;
- qual risco existe;
- como testar;
- se o comportamento foi preservado.

---

## 🧠 Frase para memorizar

> Código limpo é código que uma pessoa consegue ler, entender, alterar e testar sem precisar adivinhar a intenção de quem escreveu.
> 

---

## 🏷️ Tags sugeridas

`clean-code` `boas-praticas` `programacao` `refatoracao` `qualidade-de-codigo` `engenharia-de-software` `testes` `manutencao` `ia-para-programar` `notion`
