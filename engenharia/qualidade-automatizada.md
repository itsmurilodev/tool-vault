---
titulo: Qualidade automatizada — lint, código morto, testes e contrato de arquitetura
resumo: "Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo."
tipo: referencia
dominio: engenharia
tags: [engenharia/qualidade, testes, ferramentas]
status: ativo
atualizado: 2026-08-09
---

# Qualidade automatizada — lint, código morto, testes e contrato de arquitetura

## 📌 Resumo

Ferramentas que verificam qualidade sem alguém precisar revisar à mão. Elas se dividem em quatro camadas de custo crescente — e a ordem de adoção importa mais do que a escolha dentro de cada camada. As duas primeiras se pagam em dias; as duas últimas só fazem sentido depois que existe algo a proteger.

## 🧠 1. Camada barata — lint e código morto

Adotar aqui é quase sem custo e o retorno aparece na primeira semana.

**Biome** — linter + formatter escrito em Rust, substitui ESLint + Prettier em uma ferramenta só. Ordens de grandeza mais rápido (formata ~25x mais rápido que Prettier; lint de 10 mil arquivos em menos de um segundo contra dezenas de segundos do ESLint). Em 2026 está na v2.3, com 400+ regras, lint com informação de tipo e sistema de plugin.

O trade-off real não é performance, é ecossistema: o ESLint tem milhares de regras de comunidade e o Biome não cobre todas. Critério prático: **projeto novo → Biome** (menos uma ferramenta, CI mais rápido). **Projeto maduro já em ESLint+Prettier → só migre com motivo concreto.**

**Knip** — encontra arquivo, export e dependência que ninguém usa. Parte dos entry points, calcula a árvore de dependência e marca o resto como não usado. Tem 150+ plugins (Next.js, Vite, Vitest, Jest, Storybook, GitHub Actions) e `--fix` para remover export morto automaticamente.

Casa diretamente com a skill `clean-code`, item "remover import, variável, função ou arquivo morto" — Knip é a versão automatizada dessa checagem. Cuidado herdado da própria skill: código que **parece** morto pode ser usado indiretamente (import dinâmico, rota registrada em outro arquivo). Revise antes de aceitar o `--fix`.

## 🧠 2. Camada de teste real

**Playwright** — runner de teste end-to-end de verdade: sobe navegador e exercita o fluxo como usuário. É o que responde "o cadastro ainda funciona depois dessa mudança?".

Custo honesto: teste e2e é o mais caro de escrever e o mais frágil de manter. Em produto pequeno, o retorno vem de cobrir **poucos fluxos críticos** (login, checkout, o fluxo que gera receita) — não a aplicação inteira.

**Codecov não testa nada.** É painel que agrega o percentual de cobertura produzido por um test runner que você já precisa ter (Vitest, Jest). Sem testes escritos, Codecov mostra zero muito bem. Listas virais costumam omitir essa dependência.

E cobertura é métrica enganosa: 90% de linhas executadas não significa que os testes verificam comportamento — significa que as linhas rodaram.

## 🧠 3. Camada de time — mutation testing

**Stryker (StrykerJS)** — mutation testing: introduz pequenas alterações no seu código (troca `>` por `>=`, inverte um booleano) e verifica se algum teste falha. Mutação que **sobrevive** é um ponto cego: aquela linha está coberta, mas nada verifica o comportamento dela.

É a resposta honesta ao problema da cobertura. Suporta Jest, Mocha, Jasmine e Vitest.

Custo: roda a suíte muitas vezes, então é lento — lugar dele é em CI agendado, não a cada commit. Só faz sentido quando **já existe uma suíte de testes que vale auditar**. Antes disso, é auditar o vazio.

## 🧠 4. Camada de arquitetura — contrato testável

"Arch-contract" não é um produto: é a categoria de **fitness function** — testar a arquitetura como se fosse teste unitário. A regra ("a camada de domínio não importa nada de infraestrutura", "componente de UI não chama repositório direto") vira teste que quebra o PR quando alguém viola.

**ArchUnitTS** é a implementação em TypeScript (regras por arquivo, analisando relação de import; roda em Jest, Vitest, Mocha). **dependency-cruiser** resolve o mesmo problema por outro caminho: valida o grafo de dependências contra regras declaradas.

Só vale quando **já existem camadas definidas que valem proteger**. Em projeto sem fronteira arquitetural clara, não há contrato a escrever — e escrever um contrato sobre uma arquitetura que ainda vai mudar cria atrito sem benefício. Sistema multi-tenant, onde vazar contexto de tenant entre camadas é falha grave, é o caso que justifica isso mais cedo.

## ✅ Ordem de adoção

| Camada | Ferramenta | Adote quando |
| ------ | ---------- | ------------ |
| 1 | Biome, Knip | Sempre — o custo é quase zero |
| 2 | Vitest/Jest → Playwright nos fluxos críticos | Existe fluxo cuja quebra você só descobriria pelo usuário |
| 2b | Codecov | Já existe suíte e a cobertura precisa ser visível no PR |
| 3 | Stryker | A suíte existe e você duvida da qualidade dela |
| 4 | ArchUnitTS / dependency-cruiser | Existem camadas definidas e mais de uma pessoa mexendo |

Pular direto para 3 e 4 é o erro clássico: instalar auditoria de teste antes de ter teste, e contrato de arquitetura antes de ter arquitetura.

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão de estágio.
- [[clean-code]] — Knip automatiza a parte de código morto; Biome, a de formatação e regra básica.
- Skill [clean-code](../ia/agentes/claude/skills/clean-code/SKILL.md).

## 📚 Fontes

- [Biome vs ESLint + Prettier em 2026 — PkgPulse](https://www.pkgpulse.com/blog/biome-vs-eslint-prettier-linting-2026)
- [Knip — site oficial](https://knip.dev/) · [repositório](https://github.com/webpro-nl/knip)
- [StrykerJS — repositório](https://github.com/stryker-mutator/stryker-js)
- [ArchUnitTS — repositório](https://github.com/LukasNiessen/ArchUnitTS) · [Fitness functions](https://lukasniessen.com/blog/12-architecture-fitness-functions/)
