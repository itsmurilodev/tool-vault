---
titulo: "Visão do Produto — Encaixe (Agendamento Inteligente)"
resumo: "Arquitetura, objetivos de negócio e decisões técnicas do aplicativo Encaixe."
tipo: referencia
dominio: async
tags: [async/produtos, encaixe, saas, supabase]
status: ativo
atualizado: 2026-08-26
---

# Visão do Produto — Encaixe

> Sistema moderno de agendamento online e gestão de encaixes para profissionais e prestadores de serviço.

---

## 🎯 Proposta & Objetivos

* **Problema**: Perda de receita por desistências de última hora e atrito em agendamentos via WhatsApp.
* **Solução**: Link de agendamento direto com fila de espera inteligente para preenchimento automático de horários vagos.

---

## 🛠️ Stack Arquitetural

* **Front-end**: Next.js / React com TailwindCSS e componentes customizados.
* **Back-end & Banco**: Supabase (PostgreSQL, Supabase Auth, Row Level Security).
* **Emails**: Resend para confirmações transacionais.
* **Observabilidade**: Sentry (OpenTelemetry) para captura de exceções em produção. Ver [[adr-001-observabilidade]].
