# 🖥️ Infra

Onde o software roda: sistema operacional, containers, cloud, redes, banco de dados, CI/CD e observabilidade.

## O que entra aqui

| Tópico             | Exemplos de nota                                                    |
| ------------------ | ------------------------------------------------------------------- |
| Linux e shell      | permissões, systemd, processos, diagnóstico com `journalctl`/`ss`   |
| Containers         | Dockerfile, docker compose, imagem enxuta, volumes e rede           |
| Cloud              | provedor usado, custo, VPC/rede, storage, gerenciado vs self-hosted  |
| CI/CD              | pipeline, cache, matriz de build, deploy e rollback                  |
| Banco de dados     | backup e restore, migração, índice, connection pool                  |
| Observabilidade    | log estruturado, métrica, alerta que vale acordar alguém            |
| Segurança de infra | secrets, TLS, firewall, princípio do menor privilégio               |

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [ADR 001 — Plataforma de observabilidade padrão](adr-001-observabilidade.md) — Sentry no free tier, instrumentado via OpenTelemetry, como padrão para projeto novo. Proposta.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.

<!-- FIM:INDICE -->

---

## Backlog deste domínio

- [ ] Docker: imagem de produção enxuta (multi-stage) para os projetos atuais
- [ ] Deploy: como um projeto sai do local para o ar hoje, passo a passo real
- [ ] Backup de banco: comando exato de dump e de restore, testado
- [ ] Secrets: onde ficam hoje e onde deveriam ficar
- [ ] Instrumentar um projeto com OpenTelemetry, na prática
