---
titulo: "Email transacional — Resend"
resumo: "Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora."
tipo: referencia
dominio: infra
tags: [infra/email, custo]
status: ativo
atualizado: 2026-08-11
---

# Email transacional — Resend

## 📌 Resumo

Email transacional é o envio disparado por ação do sistema — confirmação de cadastro, redefinição de senha, notificação de agendamento no Encaixe. Diferente de Clerk/Pinecone/Upstash, isso **não é redundante com nada que já existe** no stack: nem Encaixe nem Async Hub têm hoje uma forma de enviar email.

> ✅ Dos itens do reel original, Resend passa direto no portão de [[adocao-de-ferramenta]]: dor concreta (nenhum envio de email hoje), custo zero no volume atual, não substitui nem soma a nada já pago.

## 🧠 1. Free tier (2026)

| Recurso | Limite |
| ------- | ------ |
| Emails/mês | 3.000 |
| Emails/dia | 100 |
| Domínios verificados | 1 |
| Retenção de log | 30 dias |

O teto diário (100/dia) costuma travar antes do mensal — se um dia tiver pico de cadastro ou lembrete em massa, é o primeiro limite a bater, não os 3.000/mês.

## ⚠️ 2. Contexto de mercado que vale saber

SendGrid, a opção "padrão" historicamente, **descontinuou seu free tier em maio de 2025** — hoje oferece só trial de 60 dias. Isso torna Resend uma escolha ainda mais direta para projeto novo em 2026: não há mais o concorrente gratuito de referência.

## ✅ 3. Como aplicar no Encaixe / Async Hub

- **React Email** (biblioteca de template da própria Resend) encaixa direto na stack Node/TypeScript já em uso.
- Casos de uso imediatos: confirmação de agendamento (Encaixe), redefinição de senha (Async Hub), notificação de novo contato no inbox multi-agente.
- Não precisa de ADR — decisão barata de reverter (trocar provedor de email é reescrever uma camada de envio, não uma migração de dado).

## 🔗 Ver também

- [[adocao-de-ferramenta]] — por que este item, especificamente, passa no portão agora.

## 📚 Fontes

- [Resend Free Tier Explained — Automation Atlas](https://automationatlas.io/answers/resend-free-tier-explained-2026/)
- [Resend vs SendGrid 2026 — DEV Community](https://dev.to/thiago_alvarez_a7561753aa/resend-vs-sendgrid-2026-sendgrid-killed-its-free-tier-now-what-2gh4)
