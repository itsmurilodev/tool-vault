---
name: impeccable-ui
description: >
  Aplica as 59 regras determinísticas e comandos de design do Impeccable para
  eliminar 'AI slop' (gradientes roxo/azul clichês, cards aninhados, contraste
  ruim) e garantir interfaces front-end com alto padrão estético, acessibilidade
  e consistência visual em React, Next.js e Tailwind. Usar SEMPRE que for
  escrever, gerar, editar ou auditar componentes de UI, páginas e estilos CSS.
  Quando o pedido for auditar ou refatorar visualmente (ex: "/impeccable polish",
  "/impeccable audit", "refine o design", "tire a cara de IA"), seguir o modo
  de auditoria com relatório de design e catálogo de regras.
---

# Impeccable UI — Linter Determinístico e Design System de Front-end

Esta skill aplica as diretrizes e comandos do **Impeccable** ([impeccable.style](https://impeccable.style)) para garantir que toda interface gerada por IA tenha acabamento de designer sênior, contraste acessível e personalidade visual, sem recorrer a templates saturados ("AI slop").

**Idioma:** toda comunicação (relatórios de auditoria de UI, recomendações) é em português do Brasil, direta e orientada a layout.

Existem dois modos de operação. Escolha um antes de agir:

---

## 🎨 Modo Padrão — Escrever ou Gerar UI (Comportamento Default)

Aplicar silenciosamente estas regras determinísticas ao gerar qualquer componente React, página Next.js ou estilo Tailwind, sem produzir relatórios intermediários:

1. **Eliminar Gradientes Clichês**:
   * Proibido o uso do gradiente roxo-para-azul saturado padrão de IA (`bg-gradient-to-r from-purple-600 to-blue-500`).
   * Priorize fundos com neutros calibrados (ardósia, cinza quente, chumbo) e use cores de destaque pontuais dos tokens do projeto ([[tokens-css]]).
2. **Zero Aninhamento Excessivo de Containers**:
   * Não coloque cards dentro de cards com bordas repetidas e sombras pesadas.
   * Crie separação usando ritmo de espaçamento vertical/horizontal (`gap`, `space-y`, `p`), tipografia e divisores sutis (`border-border/40`).
3. **Contraste Acessível (WCAG AA/AAA)**:
   * Texto primário de alto contraste (`text-foreground`).
   * Texto secundário sempre legível (`text-muted-foreground` com taxa de contraste mínima de 4.5:1 contra o fundo). Nunca use cinza apagado sobre fundo escuro.
4. **Estados Interativos Completos**:
   * Todo elemento clicável (`<button>`, `<a>`, inputs) deve possuir obrigatoriamente:
     * `hover:bg-...` (feedback ao passar o mouse)
     * `focus-visible:ring-2 focus-visible:ring-offset-2` (foco nítido por teclado)
     * `active:scale-[0.98]` (feedback tátil de clique)
     * `disabled:opacity-50 disabled:cursor-not-allowed`
     * Estado de `loading` (spinner ou indicador de carregamento)
5. **Escala Tipográfica Controlada**:
   * No máximo 3 tamanhos de fonte por tela (Título, Corpo e Apoio). Evite misturar múltiplos pesos sem critério de hierarquia.

---

## 🔍 Modo Auditoria — Refinamento e Comandos Impeccable

Acionar quando o usuário pedir expressamente para revisar, auditar ou polir a interface existente (ex: `"/impeccable audit"`, `"/impeccable polish"`, *"remova a cara de IA desta tela"*).

### 1. Comandos Operacionais

Quando a ferramenta Impeccable estiver ativa no repositório (`npx impeccable install`):

* **/impeccable init**: Lê as configurações do projeto e gera `PRODUCT.md` e `DESIGN.md` para calibrar o contexto de marca e tokens.
* **/impeccable audit**: Executa o scanner local (`npx impeccable detect [caminho]`) e lista as regras violadas sem alterar código.
* **/impeccable critique**: Realiza uma avaliação crítica do layout contra as 59 regras determinísticas.
* **/impeccable polish**: Aplica a refatoração focada nas seções com problemas de contraste, espaçamento e hierarquia.
* **/impeccable distill**: Agrupa classes e estilos repetidos em padrões e componentes reutilizáveis.

### 2. Formato de Saída Obrigatório (Markdown)

```markdown
## 🎨 Diagnóstico de Interface (Impeccable UI)
* **Componente/Tela**: [Nome do Arquivo]
* **Nível de AI Slop Detectado**: [Alto / Médio / Limpo]

### 🔍 Violações Identificadas & Correções
| # | Categoria | Regra Violada | Onde | Problema Visual | Refatoração Aplicada |
| :-: | :---: | :--- | :--- | :--- | :--- |
| 1 | Anti-Slop | Nested Card Slop | `src/components/Pricing.tsx` | 3 níveis de cards com bordas | Removido container externo, usado whitespace |
| 2 | Qualidade | Low Contrast Text | `src/components/Footer.tsx:L18` | Cinza apagado sobre escuro | Ajustado para text-slate-300 (WCAG AA) |
| 3 | Qualidade | Missing Focus State | `src/components/Button.tsx` | Sem anel de foco no teclado | Adicionado focus-visible:ring-2 |

### 🛠️ Código Refatorado
[Diff ou snippets concisos da melhoria]

### ✅ Checklist Final de Entrega
- [ ] Zero gradientes genéricos roxo/azul.
- [ ] Contraste verificado e acessível.
- [ ] Estados de hover, focus e active presentes.
- [ ] Tokens de design respeitados.
```

---

## ⚠️ Restrições Rígidas

* **Não Carregar em Backend**: Não ative nem discuta regras de UI em tarefas puramente backend ou de infraestrutura para evitar desperdício de tokens.
* **Respeitar os Tokens do Projeto**: Em projetos da Async, priorize os tokens em [[tokens-css]] sobre cores hexadecimais avulsas.

---

## 📚 Referência Ampliada

Consulte `references/59-regras-impeccable.md` para ver o catálogo completo das 32 regras anti-slop e 27 regras de qualidade visual.
