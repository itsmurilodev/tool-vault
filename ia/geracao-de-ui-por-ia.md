---
titulo: Geração de UI e de app por IA — os três níveis
tipo: conceito
dominio: ia
tags: [ia/geracao-de-codigo, mcp, frontend, vibe-coding]
status: ativo
atualizado: 2026-08-10
---

# Geração de UI e de app por IA — os três níveis

## 📌 Resumo

"IA que constrói interface" virou uma categoria só no discurso, mas são **três níveis diferentes** de automação, com risco e reversibilidade muito diferentes. Confundi-los é o que faz alguém adotar uma plataforma que gera o app inteiro quando o problema era só instalar um componente mais rápido.

O eixo que organiza tudo: **quanto da decisão você delegou.**

| Nível | O que a IA faz | Reversibilidade | Exemplos |
| ----- | -------------- | --------------- | -------- |
| **1. Instalação** | Busca e instala um componente que **já existe** | Alta — é a CLI que você rodaria à mão | MCP do shadcn, MCP do 21st |
| **2. Geração de componente** | Escreve um componente **novo** a partir de descrição | Média — é código no seu projeto, revisável | 21st AI (`/ui …`), Claude/Cursor direto |
| **3. Geração de app** | Gera projeto, estrutura e telas inteiras | Baixa — a arquitetura veio pronta e você não participou | 10x.app, v0, Lovable, Bolt |

> 💡 **Analogia:** nível 1 é pedir para alguém buscar uma peça no estoque. Nível 2 é pedir para fabricarem uma peça sob medida. Nível 3 é encomendar a casa montada e descobrir depois onde passaram os canos.

## 🧠 1. Nível 1 — MCP que instala componente

O caso mais seguro e o mais subestimado. O **MCP oficial do shadcn** expõe as operações da CLI (`init`, `add`, listar itens e blocos) como ferramentas que um agente pode chamar, e funciona com qualquer registro compatível — inclusive registro próprio ou self-hosted. O **21st MCP** (antigo Magic MCP) conecta o agente ao catálogo de 12.000+ componentes do 21st.dev para buscar e instalar sem sair do editor.

Por que isso é diferente dos outros níveis: **o resultado é determinístico.** A ferramenta executa o mesmo comando que você executaria; a IA só decidiu qual. Se errar o componente, você desfaz com um `git checkout`.

É o nível que vale adotar primeiro — ganho real de velocidade com risco quase nulo.

## 🧠 2. Nível 2 — IA escreve o componente

O 21st AI gera componentes em variantes a partir de descrição em linguagem natural (via `/ui …` no agente, pela web ou pela CLI), produzindo código em shadcn + Tailwind + Radix. Na prática, Claude ou Cursor fazem a mesma coisa sem catálogo — a diferença do 21st é partir de componentes já testados em vez de gerar do zero.

Aqui entra o risco real, e ele não é técnico — é de **revisão**. Código gerado chega pronto, bonito e plausível, e é exatamente por isso que passa sem leitura. As duas réguas que você já tem existem para esse momento:

- **[clean-code](agentes/claude/skills/clean-code/SKILL.md)** — o componente gerado tem nome que revela intenção? Erro tratado? Responsabilidade única? Código de IA tende a nomes genéricos e a `catch` vazio.
- **[heuristicas-nielsen](agentes/claude/skills/heuristicas-nielsen/SKILL.md)** — tem estado de loading, de vazio e de erro? Foco de teclado funciona? Rótulo junto do ícone? Gerador otimiza o caso feliz; os outros estados costumam sair faltando.

Regra: **componente gerado entra pela mesma porta que componente copiado de catálogo** — o de [[bibliotecas-de-ui]]. É código de origem externa, e você assume a manutenção dele.

## 🧠 3. Nível 3 — plataforma que gera o app

**10x.app** gera aplicativo iOS nativo a partir de descrição: escreve SwiftUI, monta o projeto Xcode e mostra no simulador, sem webview nem wrapper híbrido. Tecnicamente, roda um loop agêntico do lado do cliente — chama o Claude por um proxy fino, interpreta os blocos de `tool_use`, executa operações de arquivo localmente e itera até terminar. Preço por crédito: free com US$ 5, Plus US$ 20/mês, Max US$ 200/mês, com teto de gasto configurável.

Dois fatos decidem se isso serve para você:

1. **É SwiftUI/iOS nativo.** Não gera React, Next.js nem PHP. Para uma stack web, ele simplesmente não se aplica — não é questão de qualidade, é de alvo.
2. **A arquitetura vem pronta.** Em protótipo isso é a vantagem inteira. Em produto que vai ser mantido, você herda decisões estruturais das quais não participou e que só descobre ao precisar mudar algo.

Onde nível 3 é honestamente bom: **provar uma ideia rápido**, mostrar algo clicável para um cliente, ou testar se vale construir de verdade. Onde ele cobra caro: quando o protótipo é promovido a produto sem ninguém reescrever a base.

> Detalhe que vale reter para além da ferramenta: a arquitetura do 10x.app — loop agêntico client-side chamando um modelo por proxy, com execução de ferramenta local — é o mesmo desenho de qualquer agente de código. É referência útil se um dia você construir um.

## ⚠️ Erros comuns

- **Tratar os três níveis como a mesma decisão.** Adotar MCP de instalação é barato e reversível; adotar plataforma de geração de app é decisão de arquitetura.
- **Não revisar porque "a IA fez".** Código gerado tem a mesma dívida de código escrito — só chega mais rápido e com aparência melhor, o que reduz a chance de alguém olhar.
- **Promover protótipo a produto.** O código de nível 3 foi otimizado para existir, não para ser mantido.
- **Confundir velocidade de geração com velocidade de entrega.** O gargalo raramente é escrever o componente; é decidir o que construir. Isso é escopo de [levantamento-requisitos](agentes/claude/skills/levantamento-requisitos/SKILL.md), e nenhuma dessas ferramentas toca nisso.

## ✅ Como aplicar

| Situação | Nível certo |
| -------- | ----------- |
| Já uso shadcn e quero parar de trocar de janela para instalar componente | **1** — MCP do shadcn. Adote |
| Preciso de um componente que não existe no catálogo | **2** — gerar, e revisar com clean-code + Nielsen antes de aceitar |
| Quero validar uma ideia de app em um fim de semana | **3** — desde que fique claro que é protótipo descartável |
| Vou construir produto para manter | **1 e 2** dentro do seu projeto. Nível 3 não |

Sobre ligar o MCP: vale o custo de contexto já registrado em [conectores do Claude](agentes/claude/conectores.md) — cada servidor ativo injeta as definições de ferramenta em toda conversa. MCP de UI ligado num projeto de back-end é peso morto.

## 🔗 Ver também

- [[bibliotecas-de-ui]] — o catálogo que os níveis 1 e 2 consomem, e as regras de ícone e movimento.
- [[adocao-de-ferramenta]] — o portão de estágio.
- [[conectores]] — custo de manter servidor MCP ligado.

## 📚 Fontes

- [MCP do shadcn/ui](https://ui.shadcn.com/docs/registry/mcp) · [21st MCP](https://21st.dev/mcp) · [21st AI](https://21st.dev/ai)
- [10x.app](https://www.10x.app/) · [Welcome to 10x](https://www.10x.app/blog/welcome-to-10x)
