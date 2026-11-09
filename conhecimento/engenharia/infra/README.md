# 🖥️ Infra

Onde o software roda: sistema operacional, containers, cloud, redes, banco de dados, CI/CD e observabilidade.

> Avaliações de **serviços e ferramentas** (Supabase, Resend, PostHog, Sentry, Upstash, Portless…) ficam no radar: [Infraestrutura](../../../radar/infraestrutura/categoria-infraestrutura.md). Aqui fica o conhecimento de *como operar*.

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

_Ainda sem notas neste domínio._

<!-- FIM:INDICE -->

---

## Backlog deste domínio

- [ ] Docker: imagem de produção enxuta (multi-stage) para os projetos atuais
- [ ] Deploy: como um projeto sai do local para o ar hoje, passo a passo real
- [ ] Backup de banco: comando exato de dump e de restore, testado
- [ ] Secrets: onde ficam hoje e onde deveriam ficar
- [ ] Instrumentar um projeto com OpenTelemetry, na prática
