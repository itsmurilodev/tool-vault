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

- [Analytics de produto — PostHog](analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Email transacional — Resend](email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD](guarita.md) — Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS](portless.md) — Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes.
- [Supabase como backend-as-a-service — o teto real do free tier](backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.

<!-- FIM:INDICE -->

---

## Backlog deste domínio

- [ ] Docker: imagem de produção enxuta (multi-stage) para os projetos atuais
- [ ] Deploy: como um projeto sai do local para o ar hoje, passo a passo real
- [ ] Backup de banco: comando exato de dump e de restore, testado
- [ ] Secrets: onde ficam hoje e onde deveriam ficar
- [ ] Instrumentar um projeto com OpenTelemetry, na prática
