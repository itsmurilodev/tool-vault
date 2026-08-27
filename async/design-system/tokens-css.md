---
titulo: "Tokens CSS e Sistema de Design — Async"
resumo: "Tokens de tipografia, espaçamento, bordas e sombras prontos para copiar em CSS/Tailwind."
tipo: referencia
dominio: async
tags: [async/design-system, css, tokens, frontend]
status: ativo
atualizado: 2026-08-26
---

# Tokens CSS e Sistema de Design — Async

> Especificação de tokens CSS variáveis para padronização em todos os projetos da Async.

---

## 🔤 Tipografia

* **Fonte Principal (Sans)**: `Inter`, `Plus Jakarta Sans`, system-ui, -apple-system, sans-serif.
* **Fonte de Código (Mono)**: `JetBrains Mono`, `Fira Code`, monospace.

```css
:root {
  --font-sans: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

## 📐 Espaçamento e Raios de Borda

```css
:root {
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05);
  --shadow-glow: 0 0 25px rgba(99, 102, 241, 0.2);
}
```

---

## 🧩 Efeito Glassmorphism Padrão

```css
.glass-panel {
  background: rgba(17, 22, 34, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
```
