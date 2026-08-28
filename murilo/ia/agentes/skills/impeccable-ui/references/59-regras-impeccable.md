# As 59 Regras Determinísticas do Impeccable

Catálogo de referência para eliminação de "AI slop" e garantia de qualidade de design front-end.

---

## 🚫 1. Principais Regras Anti-Slop (32 Regras)

Identificam vícios visuais característicos de modelos generativos:

| Código | Nome da Regra | Descrição do Anti-Padrão | Como Corrigir |
| :--- | :--- | :--- | :--- |
| **SLOP-01** | `ai-purple-blue-gradient` | Gradientes saturados de roxo para azul em botões e hero sections. | Usar cores sólidas neutras ou de marca com contraste real. |
| **SLOP-02** | `nested-card-hell` | Cards dentro de cards, todos com bordas, sombras e cantos arredondados. | Usar espaçamento em branco (*whitespace*) e tipografia para agrupar. |
| **SLOP-03** | `generic-card-shadows` | Sombras difusas pretas (`shadow-xl` ou `shadow-2xl`) em fundos claros. | Sombras sutis (`shadow-sm`) com opacidade baixa ou borda fina. |
| **SLOP-04** | `overused-pill-badges` | Dezenas de badges em formato de pílula espalhados sem significado semântico. | Reduzir badges ao estritamente necessário (status real). |
| **SLOP-05** | `decorative-grid-bloat` | Fundos com padrões de grade decorativos repetidos em todas as páginas. | Fundos limpos ou gradientes radiais extremamente sutis. |
| **SLOP-06** | `uncalibrated-radius` | Mistura de botões `rounded-full`, inputs `rounded-md` e cards `rounded-3xl` na mesma tela. | Padronizar raio de borda único (`rounded-lg` ou `rounded-md`). |

---

## ⭐ 2. Principais Regras de Qualidade (27 Regras)

Forçam fundamentos sólidos de design de interface e acessibilidade:

| Código | Nome da Regra | Requisito de Qualidade | Implementação em Tailwind |
| :--- | :--- | :--- | :--- |
| **QUAL-01** | `contrast-wcag-aa` | Taxa de contraste mínima de 4.5:1 para texto normal e 3:1 para texto grande. | `text-slate-900 dark:text-slate-100` |
| **QUAL-02** | `focus-visible-state` | Todo elemento interativo deve exibir anel de foco nítido ao navegar por teclado. | `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring` |
| **QUAL-03** | `active-tactile-state` | Feedback tátil de clique em botões. | `active:scale-[0.98] transition-transform` |
| **QUAL-04** | `semantic-heading-scale` | Hierarquia estrita de títulos (`h1` único, `h2`, `h3`) com escala proporcional. | Escala com proporção definida (`text-3xl`, `text-xl`, `text-base`). |
| **QUAL-05** | `loading-empty-states` | Componentes que buscam dados devem tratar estado vazio e estado de loading. | Skeletons ou spinners acessíveis (`aria-busy="true"`). |
| **QUAL-06** | `accessible-touch-targets` | Alvos de toque com área mínima de 44x44px em telas mobile. | `min-h-[44px] min-w-[44px]` |
