---
name: react-doctor
description: >
  Audita e diagnostica anti-patterns em aplicações React e Next.js utilizando o
  React Doctor (motor Oxlint em Rust e traces do Chrome DevTools). Detecta uso
  indevido de useEffect, prop drilling severo, mutações diretas, waterfalls de
  data fetching e vazamentos de renderização. Usar ao escrever, revisar ou
  otimizar componentes React, páginas Next.js, ou quando o usuário solicitar
  auditoria de saúde do código ("/react-doctor", "audite o react", "verifique
  performance").
---

# React Doctor — Auditoria e Diagnóstico de Anti-Patterns em React

Esta skill aplica as diretrizes e diagnósticos do **React Doctor** (`millionco/react-doctor`) para garantir que código React, Next.js e React Native mantenha alto padrão arquitetural, ausência de re-renders desnecessários e sincronização correta de estado sem alucinação de anti-patterns por agentes de IA.

**Idioma:** toda comunicação (relatórios de diagnóstico, planos de refatoração) é em português do Brasil, técnica e direta.

Existem dois modos de operação. Escolha um antes de agir:

---

## ⚡ Modo Padrão — Escrever ou Editar Componentes React (Default)

Ao gerar ou editar qualquer componente React, página Next.js ou hook customizado, aplique silenciosamente estas regras determinísticas sem produzir relatórios intermediários:

1. **Zero `useEffect` para Estado Derivado**:
   * Não use `useEffect` para recalcular dados a partir de props ou outro state. Calcule diretamente durante a renderização (ou use `useMemo` apenas para computações custosas).
2. **Zero Componentes Aninhados**:
   * Proibido declarar funções de componentes dentro do corpo de outro componente. Extraia para o nível do módulo ou para um arquivo separado para evitar perda de estado e recriações de DOM a cada render.
3. **Chaves de Lista Estáveis**:
   * Nunca use índices de array (`key={index}`) em listas mutáveis, ordenáveis ou filtráveis. Use IDs únicos e estáveis.
4. **Respeitar Fronteiras de Server vs Client (Next.js)**:
   * Mantenha componentes como Server Components por padrão. Só adicione `'use client'` quando houver interatividade (event handlers, hooks de estado, APIs de navegador).
5. **Prevenção de Prop Drilling Severo**:
   * Se props passarem por mais de 3-4 níveis intermediários sem serem usadas, recomende composição (`children`), estado elevado ou contexto dedicado.

---

## 🔍 Modo Auditoria — Diagnóstico Explícito e Refatoração

Acione este modo quando o usuário solicitar expressamente uma revisão técnica ou auditoria de saúde do React (ex: `"/react-doctor"`, `"audite este componente React"`, `"qual o health score deste código?"`).

### 1. Comandos Operacionais da Ferramenta

Quando a CLI do React Doctor puder ser executada no repositório:
```bash
# Diagnóstico estático rápido
npx react-doctor@latest . --verbose

# Diagnóstico focado no delta do Pull Request
npx react-doctor@latest --diff

# Profiling dinâmico com gravação de trace DevTools
npx react-doctor@latest scan http://localhost:3000
```

### 2. Formato de Saída Obrigatório (Markdown)

```markdown
## 🩺 Diagnóstico de Saúde React (React Doctor)
* **Alvo**: [Arquivo ou Diretório Auditado]
* **Health Score Estimado**: [0 a 100 / Classificação: Great (>=75) | Needs Work (50-74) | Critical (<50)]

### 🔍 Anti-Patterns & Violações Identificadas
| # | Categoria | Regra | Localização | Problema / Risco | Refatoração Recomendada |
| :-: | :---: | :--- | :--- | :--- | :--- |
| 1 | State & Effects | `no-unnecessary-use-effect` | `src/components/UserList.tsx:L24` | Efeito sincronizando filtro derivado | Calcular `filteredUsers` em tempo de render |
| 2 | Arquitetura | `no-nested-components` | `src/components/Card.tsx:L12` | `SubItem` declarado dentro de `Card` | Extrair `SubItem` para fora do componente |
| 3 | Performance | `no-waterfall-fetching` | `src/app/dashboard/page.tsx:L15` | Múltiplos `await` sequenciais no client | Usar `Promise.all` ou Server Component |

### 🛠️ Código Refatorado
[Snippet de código conciso demonstrando a correção com Clean Code]

### ✅ Validação de Integridade
- [ ] Regras de hooks do React preservadas.
- [ ] Comportamento e props públicas mantidas sem breaking changes.
- [ ] Zero dependências desnecessárias adicionadas.
```

---

## ⚠️ Restrições Rígidas

* **Não Carregar em Backend Puro:** Não ative nem discuta regras de React em projetos puramente Node.js, Express, scripts de banco ou pipelines.
* **Cuidado com Falsos Positivos:** Não remova `useEffect` que integram bibliotecas imperativas externas (ex: instâncias do Chart.js, D3, conexões WebSocket) que genuinamente exigem setup e cleanup no DOM.
* **Ajustes Atômicos:** Não refatore arquivos inteiros sem necessidade; aplique correções cirúrgicas e preserve a semântica do projeto.

---

## 🔗 Referência Técnica

Consulte a nota de conhecimento completa em [[react-doctor]] no vault para detalhes sobre arquitetura interna, benchmarks de Oxlint e portão de adoção técnica.
