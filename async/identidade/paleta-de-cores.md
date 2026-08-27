---
titulo: "Paleta de Cores e Tokens Visuais — Async"
resumo: "Especificações de cores, tokens CSS e diretrizes de contraste para produtos e site do Async Studio."
tipo: referencia
dominio: async
tags: [async/identidade, async/design-system, cores, ui]
status: ativo
atualizado: 2026-08-26
---

# Paleta de Cores e Tokens Visuais — Async

> Especificação de cores para interfaces e identidade do Async Studio.

---

## 🎨 Paleta Principal (Dark Theme Core)

| Função | Nome do Token | Hex | HSL / RGB | Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Background Dark** | `--bg-primary` | `#0A0D14` | `hsl(222, 33%, 6%)` | Fundo principal da página |
| **Surface Dark** | `--bg-surface` | `#111622` | `hsl(222, 33%, 10%)` | Cards, modais e containers |
| **Surface Border** | `--border-subtle` | `#1E2638` | `hsl(222, 30%, 17%)` | Bordas sutis de componentes |
| **Primary Brand** | `--brand-primary` | `#6366F1` | `hsl(239, 84%, 67%)` | Botões primários, links, destaques (Índigo) |
| **Primary Hover** | `--brand-hover` | `#4F46E5` | `hsl(243, 75%, 59%)` | Estado hover de ações primárias |
| **Accent Cyan** | `--accent-cyan` | `#06B6D4` | `hsl(189, 94%, 43%)` | Badges, indicadores ativos e gradientes |
| **Text Primary** | `--text-primary` | `#F8FAFC` | `hsl(210, 40%, 98%)` | Títulos e texto de alta ênfase |
| **Text Secondary**| `--text-secondary`| `#94A3B8` | `hsl(215, 20%, 65%)` | Subtítulos, labels e descrições |
| **Text Muted** | `--text-muted` | `#64748B` | `hsl(215, 16%, 47%)` | Placeholders e timestamps |

---

## ✨ Gradientes de Destaque

* **Hero Gradient**: `linear-gradient(135deg, #6366F1 0%, #06B6D4 100%)`
* **Surface Glow**: `radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.15), transparent 70%)`
* **Card Border Glow**: `linear-gradient(to bottom right, rgba(99, 102, 241, 0.4), rgba(6, 182, 212, 0.1))`

---

## 📐 Regras de Acessibilidade & Contraste

1. Todo texto principal sobre `--bg-primary` deve manter contraste mínimo de **7:1** (WCAG AAA).
2. Não usar cor pura como único indicador de status (combinar sempre cor + ícone ou texto).
