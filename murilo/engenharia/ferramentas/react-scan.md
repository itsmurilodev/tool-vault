---
titulo: "React Scan — Detecção Automática de Re-renders e Profiling Visual"
resumo: "Ferramenta zero-config de profiling e auditoria de re-renders no React via Canvas overlay e interceptação de Fiber."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, frontend, react, performance, qualidade-de-codigo]
status: ativo
atualizado: 2026-08-28
---

# React Scan — Detecção Automática de Re-renders e Profiling Visual

## 📌 Resumo

O **React Scan** ([react-scan.com](https://react-scan.com)), desenvolvido por Aiden Bai e equipe da Million Software, é uma ferramenta de diagnóstico e auditoria de desempenho em tempo de execução voltada para aplicações React. Diferente do React DevTools tradicional (que exige gravação manual e análise de gráficos de chamas) e de bibliotecas legadas como *why-did-you-render* (que exigem injeção manual de código e geram poluição de logs no console), o React Scan opera no modelo *zero-config*, projetando um overlay visual em Canvas diretamente sobre os componentes que sofrem re-renderizações desnecessárias.

No [[adocao-de-ferramenta]], o React Scan é classificado como **Adoção de Diagnóstico e CI (P1)**: custo financeiro zero (MIT), setup imediato, e alto impacto na detecção de cascatas de renderização e gargalos de responsividade (INP).

---

## 🧠 1. Mecânica Interna e Arquitetura

O React Scan destaca-se por resolver os dois maiores gargalos das ferramentas tradicionais de profiling:

1. **Interceptação de Reconciliação via Bippy**:
   - Conecta-se ao hook global `window.__REACT_DEVTOOLS_GLOBAL_HOOK__` (o mesmo canal do React DevTools oficial).
   - O motor **Bippy** intercepta as árvores Fiber (`FiberRoot`, `FiberNode`) durante a fase de commit do React (compatível com React 17, 18 e 19).
   - Realiza *shallow diffing* entre `memoizedProps`/`pendingProps` e monitora acionamentos de `memoizedState` e Context para classificar a renderização.

2. **Overlay em Canvas Isolado (Zero DOM Pollution)**:
   - Em vez de injetar nós `<div>` ou bordas CSS no DOM do aplicativo (o que causaria mutações de layout, *reflows* e mascaramento de métricas), o React Scan desenha uma camada transparente de `<canvas>` em tela cheia com aceleração via GPU.
   - As caixas delimitadoras (*bounding boxes*) são atualizadas via `requestAnimationFrame` com agrupamento (*batching*) e *throttling*, mantendo o impacto no *main thread* mínimo (`~0.8ms – 3ms` por commit em desenvolvimento).

3. **Heurística Cromática de Renders**:
   - 🟢 **Verde**: Renderizações pontuais com mudança real de estado (saudáveis).
   - 🟡 **Amarelo / Laranja**: Componentes com renderizações frequentes em intervalos curtos.
   - 🔴 **Vermelho**: Renders em alta frequência ou cascatas de renderização causadas por props instáveis, funções inline não memoizadas ou Contexts mal fatiados.

---

## 🛠️ 2. Como Usar e Integrar

### 1. Inspeção Remota Rápida (Sem Alterar Código)
Inspecione qualquer aplicação rodando localmente ou em homologação diretamente pelo terminal:
```bash
npx -y react-scan@latest http://localhost:3000
```

### 2. Integração no Projeto (Vite / Next.js)

```bash
npm install -D react-scan
```

Em projetos com **Vite** (`vite.config.ts`):
```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import reactScan from '@react-scan/vite-plugin-react-scan';

export default defineConfig({
  plugins: [
    react(),
    reactScan({
      enable: process.env.NODE_ENV === 'development',
    }),
  ],
});
```

Em projetos com **Next.js** (injeção client-only no `layout.tsx` raiz):
```tsx
import Script from 'next/script';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <head>
        {process.env.NODE_ENV === 'development' && (
          <Script
            src="https://unpkg.com/react-scan/dist/auto.global.js"
            strategy="beforeInteractive"
          />
        )}
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### 3. Automação de Performance no CI (Playwright)
O React Scan expõe callbacks programáticos (`onCommit`, `onRender`) que permitem falhar testes E2E caso fluxos críticos ultrapassem orçamentos de render:
```typescript
// Exemplo em teste Playwright
test('fluxo de busca não deve disparar mais de 5 re-renders no cabeçalho', async ({ page }) => {
  let headerRenders = 0;

  await page.addInitScript(() => {
    window.reactScan = {
      options: {
        onRender: (fiber) => {
          if (fiber.name === 'HeaderSearch') headerRenders++;
        },
      },
    };
  });

  await page.goto('/dashboard');
  await page.fill('input[type="search"]', 'termo de teste');
  
  expect(headerRenders).toBeLessThanOrEqual(5);
});
```

---

## 🎯 3. Quando Usar e Benefícios Reais

### Quando Usar (Cenários Ideais)
- **Durante Desenvolvimento Local Interativo**: Para identificar visualmente se digitação em inputs, abertura de modais ou cliques em abas estão disparando re-renderizações desnecessárias em listas ou no layout pai.
- **Auditoria de Migração para React Compiler (React 19)**: Para validar se o compilador memoizou os nós automaticamente ou se referências mutadas escaparam da otimização.
- **Refatoração de Estado Global & Context API**: Diagnosticar nós dependentes que re-renderizam por mudanças em chaves não relacionadas do mesmo contexto.
- **Prevenção de Regressões em CI/E2E**: Adicionar assertions de renderização em jornadas de alto impacto (ex: checkout, tabelas com paginação).

### Benefícios Reais
- **Zero Fricção de Setup**: Elimina a necessidade de instrumentar componentes manualmente (`Component.whyDidYouRender = true`).
- **Feedback Visual Imediato**: Revela gargalos sem exigir navegação complexa em abas de Profiler.
- **Diagnóstico Preciso de Causa Raiz**: O inspetor integrado aponta exatamente qual prop ou estado mudou por referência rasa (*shallow reference inequality*).

---

## ⚠️ 4. Quando NÃO Usar, Riscos e Pegadinhas

### Quando NÃO Usar
- **Em Builds de Produção para Usuários Finais**: O pacote adiciona overhead no ciclo de renderização e expõe a estrutura interna de componentes Fiber no escopo global do navegador. Garanta que esteja estritamente isolado para `development` ou staging.
- **Aplicações Baseadas Exclusivamente em WebGL / Canvas / Three.js**: O React Scan mapeia nós do DOM associados ao Fiber; elementos internos de cenas 3D (ex: `@react-three/fiber`) não possuem nós DOM padrão para desenho de caixas delimitadoras.

### Riscos Operacionais & Pegadinhas
1. **Armadilha da Micro-Otimização Prematura**:
   - *O problema*: Nem todo re-render é um gargalo de desempenho. O Virtual DOM do React é extremamente rápido para nós simples.
   - *A consequência*: Tentar "zerar todas as caixas vermelhas" espalhando `useMemo`, `useCallback` e `React.memo` em componentes triviais aumenta a complexidade de manutenção e o consumo de memória sem melhorar o INP.
   - *A diretriz*: Use o React Scan para diagnosticar; valide o ganho real sempre pelas métricas de **INP (Interaction to Next Paint)** e **TBT (Total Blocking Time)**.
2. **Hydration Mismatch em SSR**:
   - Injetar o script do React Scan de forma assíncrona ou após a hidratação pode gerar alertas de discrepância de HTML em frameworks como Next.js App Router e Remix. Use `strategy="beforeInteractive"` ou o plugin de build oficial.
3. **Conflito de Ordem de Boot**:
   - O React Scan precisa ser carregado antes do runtime do React inicializar na janela para interceptar o `__REACT_DEVTOOLS_GLOBAL_HOOK__` corretamente.

---

## ⚖️ 5. Comparativo com Alternativas

| Critério | **React Scan** | **React DevTools Profiler** | **why-did-you-render (WDYR)** |
| :--- | :--- | :--- | :--- |
| **Abordagem** | Overlay visual em Canvas + Interceptação Fiber | Gravação pontual de commits e flamegraph nativo | Monkey-patching de protótipos com logs no console |
| **Invasividade** | Zero (CLI ou import condicional) | Zero (Extensão de browser) | Alta (Requer flags manuais nos componentes) |
| **Feedback** | Visual em tempo real sobre a UI | Gráfico estático pós-gravação | Spam de texto e diffs no DevTools Console |
| **Automação (CI)** | Nativa (callbacks `onCommit`/`onRender`) | Ruim / Complexa via API Profiler | Inviável em larga escala (depende de console) |
| **Overhead em Dev** | Baixo (`~0.8ms – 3ms`) | Mínimo (Inerte quando não está gravando) | Alto em árvores profundas (Deep diffing) |
| **Compatibilidade** | React 17, 18, 19 | React 16.8+ | Parcial / Frágil em canários do React 19 |

---

## 🎯 6. Aplicação nos Produtos da Async Studio

* **[[app-encaixe]]**: Essencial para validar o fluxo de calendário e agendamento mobile, garantindo que a seleção de datas/horários não dispare re-renderizações na listagem inteira de serviços.
* **[[app-asynchub]]**: Utilizado para auditar tabelas densas do CRM e filtros de clientes, assegurando digitação fluida em inputs sem travamento no *main thread*.
* **[[site-institucional]]**: Auditoria em componentes interativos com micro-animações, garantindo compatibilidade com [[tokens-css]] e métricas estritas de Core Web Vitals.

---

## 🔗 Ver também

* [[adocao-de-ferramenta]] — portão de decisão e critérios de estágio para novas ferramentas.
* [[qualidade-automatizada]] — ferramentas determinísticas de lint, testes unitários e E2E (Playwright).
* [[impeccable]] — regras determinísticas para qualidade visual e prevenção de AI slop no front-end.
* [[clean-code]] — padrões de sustentabilidade e clareza de código em React/TypeScript.

---

## 📚 Fontes

- [React Scan — Repositório Oficial no GitHub](https://github.com/aidenybai/react-scan)
- [React Scan — Documentação Oficial](https://react-scan.com)
- [Bippy — Toolkit de Acesso a React Internals](https://github.com/aidenybai/bippy)
- [Web Vitals & Interaction to Next Paint (INP) — web.dev](https://web.dev/articles/inp)
