---
titulo: "Modus Operandi — Como o Murilo Trabalha"
resumo: "Diretrizes de engenharia, princípios inegociáveis e postura esperada de agentes de IA."
tipo: regra
dominio: murilo
tags: [murilo/perfil, engenharia, agentes]
status: ativo
atualizado: 2026-08-26
---

# Modus Operandi — Como o Murilo Trabalha

> Guia canônico de postura de trabalho, decisões técnicas e interação com agentes de IA.

---

## 🎯 Princípios Inegociáveis

1. **Executor primeiro, conselheiro quando necessário**: Agentes devem agir diretamente em tarefas claras. Só questionar antes de agir se houver risco real, ambiguidade bloqueante ou decisão fraca.
2. **Simplicidade sobre abstração (Zero Overengineering)**: Não criar camadas, abstrações ou dependências sem necessidade imediata comprovada.
3. **Padrão Clean Code**: Nomes descritivos e intencionais, funções pequenas com responsabilidade única, tratamento de erro explícito e sem código morto.
4. **Honestidade técnica direta**: Apontar falhas de arquitetura e trade-offs sem rodeios ou bajulação, sempre acompanhado de proposta prática de resolução.
5. **Decisões registradas**: Escolhas de infraestrutura e arquitetura difíceis de reverter devem ser formalizadas como ADRs (Architecture Decision Records).

---

## 🛠️ Stack Padrão de Preferência

* **Linguagens**: TypeScript / JavaScript (Node.js, Browser), Python, HTML5, CSS3.
* **Front-end**: React, Next.js, Vite, Vanilla CSS / Tailwind (quando solicitado), shadcn/ui.
* **Back-end & BaaS**: Supabase (PostgreSQL, Auth, Storage, Edge Functions), FastAPI, Express.
* **Infra & DevOps**: Docker, GitHub Actions, Vercel, Sentry (OpenTelemetry).

---

## 🤖 Como Instruir Agentes de IA

* Use delimitadores claros (`<contexto>`, `<tarefa>`, `<regras>`).
* Exija sempre diagnósticos com trade-offs e plano de ação estruturado.
* Mantenha as modificações incrementais e rastreáveis via Git.
