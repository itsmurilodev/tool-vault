---
titulo: Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry
resumo: "Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in."
tipo: referencia
dominio: infra
tags: [infra/observabilidade, monitoramento, custo]
status: ativo
atualizado: 2026-08-09
---

# Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry

## 📌 Resumo

Observabilidade é conseguir responder "o que quebrou e por quê" sem reproduzir o bug na sua máquina. Três produtos dominam a categoria — **e eles não se somam.** Sentry, Datadog e New Relic são **concorrentes**: escolhe-se um. OpenTelemetry não é concorrente de nenhum: é o **padrão de instrumentação** que alimenta qualquer um deles.

> ⚠️ Lista que manda "adicione Sentry + Datadog + New Relic + OpenTelemetry" está errada tecnicamente e financeiramente. São três contas pagas para o mesmo trabalho.

## 🧠 1. Quem é o quê

| Ferramenta | Categoria | Foco |
| ---------- | --------- | ---- |
| **Sentry** | Error tracking / APM leve | Rastrear exceção com stack trace, contexto e release. Mais simples e mais barato |
| **New Relic** | Observabilidade full-stack | APM completo — performance de aplicação, infra, logs |
| **Datadog** | Observabilidade full-stack | Nasceu em monitoramento de infra e cresceu para tudo. Mais completo, mais caro |
| **OpenTelemetry** | Padrão aberto de instrumentação | Coleta trace/métrica/log de forma neutra e envia para a plataforma que você escolher |

## 🧠 2. OpenTelemetry é a decisão que evita lock-in

Esta é a parte que importa a longo prazo. Instrumentar com OTel significa que trocar de plataforma muda só a configuração do Collector — **o código da aplicação não é tocado**. Instrumentar com o SDK proprietário de um vendor significa que migrar é reescrever a instrumentação.

Em produto pequeno onde o volume (e o custo) ainda vai mudar muito, essa reversibilidade vale mais do que qualquer diferença de recurso entre as plataformas.

## 🧠 3. Custo — onde a decisão realmente se decide

Free tiers (referência de 2026, confirme antes de decidir, isso muda):

- **New Relic** — 100 GB de ingestão e um usuário full-platform. O mais generoso para início.
- **Sentry** — na ordem de 5.000 eventos de erro por mês. Suficiente para aplicação pequena.
- **Datadog** — tem um free tier real desde 2026, mas estreito: até 5 hosts, só Infrastructure Monitoring, retenção de métrica de 1 dia. Fora disso (APM, log, full-stack), o caminho é o trial de 14 dias e depois pago. Na prática equivale a "não serve para o que este documento está decidindo" — o free tier existe, mas não cobre error tracking/APM, que é o que MVP pré-receita precisa.

O custo do Datadog compõe por eixos que se acumulam: taxa por host de infraestrutura, taxa por host de APM, cobrança de log em dois níveis e sobretaxa de métrica custom — com cobrança em *high-water mark* (a conta do mês segue o pico, não a média). É a razão de contas de Datadog surpreenderem.

Sentry cobra por volume de evento, o que dá previsibilidade.

## ✅ Como decidir

| Estágio | Escolha |
| ------- | ------- |
| MVP pré-receita | **Sentry no free tier.** Responde "quebrou onde" com o menor custo de setup. Instrumente via OTel se der |
| Produto com usuário pagante e infra própria | Sentry para erro **ou** New Relic para full-stack — um, não os dois |
| Time, múltiplos serviços, SLA | Aí sim avaliar Datadog/New Relic full-stack com o custo real na mesa |

Regra: **uma plataforma, instrumentada por OpenTelemetry.**

## ⚠️ Erros comuns

- Adotar duas plataformas "para comparar" e manter as duas pagando.
- Instrumentar com SDK proprietário e descobrir o lock-in na hora de migrar por custo.
- Ligar alerta para tudo. Alerta que não muda comportamento de ninguém treina o time a ignorar alerta.
- Tratar observabilidade como coisa de infra grande. Rastrear erro em produção é barato no free tier e é a primeira coisa que falta quando um usuário reclama de algo que você não reproduz.

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão que decide se isso é para agora.
- [[analytics-de-produto]] — PostHog também rastreia erro (100 mil eventos/mês no free tier); a divisão atual é Sentry para "quebrou onde" e PostHog para "onde o usuário desistiu", não redundância.
- [Conectores do Claude](../ia/agentes/claude/conectores.md) — existe conector de Sentry, útil depois que a plataforma estiver escolhida.

## 📚 Fontes

- [New Relic vs Sentry 2026 — SigNoz](https://signoz.io/comparisons/newrelic-vs-sentry/)
- [Datadog vs New Relic 2026 — Better Stack](https://betterstack.com/community/comparisons/datadog-vs-newrelic/)
- [Datadog vs Sentry — Better Stack](https://betterstack.com/community/comparisons/datadog-vs-sentry/)
