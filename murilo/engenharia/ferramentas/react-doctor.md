---
titulo: "React Doctor — Auditoria Estática e Profiling de Anti-Patterns em React"
resumo: "Scanner em Rust (Oxlint) e profiler de DevTools para diagnosticar gargalos de render, anti-patterns de estado/efeitos e guiar agentes de IA."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, frontend, react, qualidade-de-codigo, performance, ia]
status: ativo
atualizado: 2026-08-28
---

# React Doctor — Auditoria Estática e Profiling de Anti-Patterns em React

## 📌 Resumo

O **React Doctor** (`millionco/react-doctor`), mantido por Aiden Bai e pela equipe da Millionco, é um utilitário CLI de diagnóstico e auditoria focado exclusivamente no ecossistema React, Next.js, Vite e React Native. 

Ele combina **análise estática ultra-rápida baseada em Rust (motor Oxlint/Oxc)** com **profiling dinâmico via traces do Chrome DevTools**, atribuindo uma pontuação de saúde técnica de 0 a 100 (*Health Score*) para a base de código e servindo como guardrail para agentes de IA de desenvolvimento (Cursor, Claude Code, Cline).

No [[adocao-de-ferramenta]], o React Doctor se qualifica como **Camada Complementar de Diagnóstico (P1/P2)**: custo financeiro zero (MIT open-source), zero acoplamento em produção (não adiciona bytes ao bundle final) e reversibilidade total e imediata.

---

## 🧠 1. Arquitetura e Mecânica Interna

O React Doctor opera em dois pilares técnicos:

### 1.1 Motor Estático Paralelo (Oxlint / Rust)
* **Travessia de AST Multi-Thread:** Utiliza o parser e linter do ecossistema Oxc escrito em Rust, executando verificações de AST em dezenas a centenas de arquivos por milissegundo através de threads em paralelo.
* **Detecção Automática de Framework:** Identifica automaticamente se o projeto utiliza Next.js (App Router ou Pages Router), Vite, Remix/React Router, TanStack Start ou Expo/React Native, ligando regras de contexto específicas (ex: regras de Server Components vs Client Components).
* **Catálogo de 60+ Regras Especializadas:** Focado em problemas estruturais que linters genéricos ignoram:
  * *State & Effects:* `useEffect` redundante para estado derivado, dependências instáveis de hooks, loops de renderização infinitos.
  * *Performance:* Alocações excessivas em render loops, props instáveis repassadas a componentes pesados, waterfalls de fetch no cliente.
  * *Arquitetura:* Declaração de componentes aninhados dentro do corpo de outros componentes, prop drilling excessivo (>4 níveis), acoplamento indevido de lógica e UI.
  * *Segurança & Correção:* Índices de array como `key` em listas dinâmicas, mutações diretas de state ou refs, riscos com `dangerouslySetInnerHTML`.

### 1.2 Profiling Dinâmico de Runtime (`scan`)
* **DevTools Performance Trace:** O comando `npx react-doctor scan <url>` inicializa uma instância isolada do Chromium via DevTools Protocol, captura um trace de performance em tempo de execução enquanto a UI é manipulada e mapeia gargalos de layout/renderização diretamente aos nós JSX correspondentes no código-fonte.

---

## 🛠️ 2. Como Usar

### Varredura Local Rápida (CLI)
```bash
# Diagnóstico rápido do diretório atual
npx react-doctor@latest .

# Modo detalhado (exibe caminhos de arquivo, linhas e regras violadas)
npx react-doctor@latest . --verbose
```

### Profiling de Performance em Runtime
```bash
# Inicia browser isolado e grava trace de interação
npx react-doctor@latest scan http://localhost:3000
```

### Configuração de Regras (`doctor.config.ts`)
```typescript
// doctor.config.ts
import { defineConfig } from 'react-doctor/config';

export default defineConfig({
  ignore: ['**/*.test.tsx', '**/dist/**'],
  rules: {
    'react-doctor/no-nested-components': 'error',
    'react-doctor/no-array-index-as-key': 'error',
    'react-doctor/no-unnecessary-use-effect': 'warn',
  },
  categories: {
    'react-native': 'off', // Desativa se o projeto for puramente web
  },
});
```

### Integração em CI/CD (GitHub Actions - Modo Delta)
Recomendado usar com `--diff` para avaliar somente o código alterado no Pull Request:

```yaml
name: React Doctor Audit
on: [pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Executar React Doctor no Delta
        run: npx react-doctor@latest --diff
```

---

## 🎯 3. Quando Usar (Cenários Ideais)

1. **Quality Gate Rápido em CI/CD:** Para barrar a introdução de novos anti-patterns em PRs sem aumentar os minutos de pipeline de build (execução em sub-segundo graças ao Rust).
2. **Contexto / Guardrail para Agentes de IA (Cursor / Claude Code):** Quando agentes autônomos de código estão gerando telas e componentes React, o React Doctor serve como barreira contra o vício recorrente de LLMs de usar `useEffect` para tudo ou declarar sub-componentes dentro da função principal.
3. **Auditoria de Saúde Técnica em Onboarding:** Diagnóstico inicial ao herdar uma base de código React/Next.js legada para mapear rapidamente a densidade de débitos técnicos.

---

## ⚠️ 4. Quando NÃO Usar & Limitações Operacionais

1. **Não Substitui Linters de Tipos Profundos (typescript-eslint / Biome):** O React Doctor não faz verificação de tipagem completa inter-arquivos (`type-aware linting`). Mantenha TypeScript e seu linter padrão ativos.
2. **Não Substitui o React Compiler (React 19):** O React Doctor diagnostica código problemático; ele **não otimiza ou reescreve** componentes para memorização automática em tempo de compilação.
3. **Não Usar para Detecção de Dead Code:** A partir da versão 0.2, a detecção de código morto interno foi descontinuada. Use o `knip` (conforme [[qualidade-automatizada]]) para encontrar arquivos e exports órfãos.
4. **Projetos Backend Puro ou Fora de React:** Não deve ser executado em APIs Node puro, scripts de banco ou projetos Vue/Svelte.

---

## ⚖️ 5. Benefícios Reais vs Riscos & Cuidados

### Benefícios Reais
* **Impacto Zero em Produção:** Ferramenta 100% de desenvolvimento/CI; não injeta runtime no bundle da aplicação.
* **Velocidade de Execução Estrema:** 30x a 50x mais rápido que suítes tradicionais de ESLint em JavaScript puro.
* **Feedback Acionável:** Fornece métricas claras (Health Score de 0 a 100) que facilitam a priorização de refatorações técnicas.

### Riscos e Mitigações
* **Risco de Falsos Positivos em `useEffect`:** Heurísticas podem sinalizar integrações legítimas com bibliotecas imperativas (D3, WebSockets, Canvas). **Mitigação:** Desative ou ajuste a severidade da regra no `doctor.config.ts` ou adicione comentários de ignore pontuais.
* **Refatoração Cega por IA:** Se um agente de IA tentar resolver todas as violações do score de uma vez, ele pode alterar comportamentos sutis de ciclo de vida. **Mitigação:** Exija testes unitários/e2e ([[qualidade-automatizada]]) e use a skill `clean-code` para guiar correções atômicas.

---

## 🎯 6. Impacto nos Produtos da Async Studio

* **[[site-institucional]]**: Assegura que componentes Next.js App Router usem Server Components por padrão, evitando hidratação desnecessária no cliente.
* **[[app-encaixe]]**: Previne waterfalls de data fetching e re-renderizações excessivas nas telas de agendamento mobile em React / Expo.
* **[[app-asynchub]]**: Garante que tabelas de dados dinâmicas e formulários complexos mantenham estabilidade de referências em hooks e performance fluida.

---

## 🔗 Ver também

* [[adocao-de-ferramenta]] — portão de adoção técnica de ferramentas.
* [[qualidade-automatizada]] — Biome, Knip, Playwright e camadas de qualidade.
* [[clean-code]] — padrões de sustentabilidade e clareza de código.
* [react-doctor](../../ia/agentes/skills/react-doctor/SKILL.md) — skill operacional para agentes de IA auditarem código React.
* [[impeccable]] — linter determinístico para design e estética de UI.
