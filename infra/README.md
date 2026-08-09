# 🖥️ Infra

Onde o software roda: sistema operacional, containers, cloud, redes, banco de dados, CI/CD e observabilidade.

**Ainda não há notas neste domínio.** Este arquivo existe para o conhecimento de infra ter um lugar óbvio quando chegar — em vez de virar mais uma pasta improvisada.

## O que entra aqui

| Tópico            | Exemplos de nota                                                   |
| ----------------- | ------------------------------------------------------------------ |
| Linux e shell     | permissões, systemd, processos, diagnóstico com `journalctl`/`ss`  |
| Containers        | Dockerfile, docker compose, imagem enxuta, volumes e rede          |
| Cloud             | provedor usado, custo, VPC/rede, storage, gerenciado vs self-hosted |
| CI/CD             | pipeline, cache, matriz de build, deploy e rollback                 |
| Banco de dados    | backup e restore, migração, índice, connection pool                 |
| Observabilidade   | log estruturado, métrica, alerta que vale acordar alguém           |
| Segurança de infra| secrets, TLS, firewall, princípio do menor privilégio              |

## Como começar

1. Copie [`templates/conceito.md`](../templates/conceito.md).
2. Salve como `infra/<assunto>.md` (ou `infra/<topico>/<assunto>.md` quando o tópico já tiver 3+ notas).
3. Preencha o frontmatter com `dominio: infra`.
4. Registre o link na seção **Notas** abaixo.

## Notas

_(vazio — primeira nota entra aqui)_

---

## Backlog deste domínio

- [ ] Docker: imagem de produção enxuta (multi-stage) para os projetos atuais
- [ ] Deploy: como um projeto sai do local para o ar hoje, passo a passo real
- [ ] Backup de banco: comando exato de dump e de restore, testado
- [ ] Secrets: onde ficam hoje e onde deveriam ficar
