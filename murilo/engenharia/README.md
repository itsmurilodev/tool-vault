# 🏗️ Engenharia

Como o software é escrito e estruturado: código, arquitetura, padrões, testes, qualidade e front-end.

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Clean Code — estudo](clean-code.md) — Legibilidade, nomes, responsabilidade única, duplicação, tratamento de erro e overengineering.
- [Ecossistema de UI copy-paste — componentes, ícones e movimento](bibliotecas-de-ui.md) — shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento.
- [Portão de adoção de ferramenta](adocao-de-ferramenta.md) — Como avaliar ferramenta nova, principalmente a que veio de conteúdo viral, antes de colocar no stack.
- [Qualidade automatizada — lint, código morto, testes e contrato de arquitetura](qualidade-automatizada.md) — Biome, Knip, Playwright, Codecov, Stryker e contrato de arquitetura, em ordem de adoção por custo.

### Ferramentas › GitHub

- [Fluxo Issue → PR → commit padronizado](ferramentas/github/fluxo-issue-pr.md) — Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno.
- [Padrão de nomes de repositórios GitHub](ferramentas/github/padrao-de-repositorios.md) — Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case.

### Infraestrutura

- [Analytics de produto — PostHog](infra/analytics-de-produto.md) — PostHog free tier (1M eventos/mês) é a ferramenta que mais serve diretamente a estratégia de validar dor real antes de cobrar — não é infraestrutura de escala, é o instrumento da própria validação.
- [Autenticação gerenciada — Clerk vs Supabase Auth](infra/autenticacao-gerenciada.md) — Clerk é excelente, mas redundante no Encaixe: o ADR já escolheu Supabase Auth, que cobre o mesmo teto free (50 mil usuários) sem adicionar um segundo provedor de identidade.
- [Banco de dados vetorial — Pinecone, pgvector e quando isso vira requisito](infra/banco-de-dados-vetorial.md) — Pinecone é bom, mas pgvector (já dentro do Supabase que Encaixe usa) resolve o mesmo problema sem vendor novo — e nenhum dos dois entra sem uma feature de busca semântica definida.
- [Cache e fila — Upstash Redis e o gatilho real de adoção](infra/cache-e-fila.md) — Upstash resolve cache, rate-limit e o adapter multi-instância do Socket.io — mas só entra quando há pressão de tráfego real, não em MVP de usuário único.
- [Email transacional — Resend](infra/email-transacional.md) — Resend cobre uma lacuna real (confirmação de cadastro, notificação, recuperação de senha) sem redundância com nada já adotado — dos itens do reel, é dos poucos que passam no portão agora.
- [Observabilidade — Sentry, Datadog, New Relic e OpenTelemetry](infra/observabilidade.md) — Sentry, Datadog e New Relic são concorrentes; OpenTelemetry é o padrão que evita lock-in.
- [Supabase como backend-as-a-service — o teto real do free tier](infra/backend-como-servico.md) — 500 MB de banco, 50 mil MAU e pausa após 7 dias de inatividade: os números concretos que decidem quando sair do free tier do Supabase.

<!-- FIM:INDICE -->

## Artefatos relacionados

- Skill [clean-code](../ia/agentes/claude/skills/clean-code/SKILL.md) — versão operacional do estudo, aplicada ao escrever código.
- Skill [decisao-arquitetural](../ia/agentes/claude/skills/decisao-arquitetural/SKILL.md) — método de ADR para decisão estrutural.
- Skill [levantamento-requisitos](../ia/agentes/claude/skills/levantamento-requisitos/SKILL.md) — o que fazer antes de começar a implementar.
- Skill [heuristicas-nielsen](../ia/agentes/claude/skills/heuristicas-nielsen/SKILL.md) — usabilidade aplicada a interface.

---

## Backlog deste domínio

- [ ] Testes: pirâmide, o que vale testar, nomeação de teste
- [ ] Arquitetura em camadas / separação de responsabilidade em projeto real
- [ ] Padrões de tratamento de erro por stack
