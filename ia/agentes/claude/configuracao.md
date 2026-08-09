---
titulo: Configuração e automação do Claude
tipo: referencia
dominio: ia
tags: [ia/claude, configuracao, hooks]
status: rascunho
atualizado: 2026-08-09
---

# Configuração e automação do Claude

Mapa de onde cada tipo de instrução mora. O erro comum é colocar tudo em um lugar só: `CLAUDE.md` vira um monólito de 400 linhas que entra em todo contexto, quando metade daquilo deveria ser skill (carregada sob demanda) ou hook (executada pelo harness).

## Qual mecanismo para qual instrução

| Mecanismo | Carregamento | Use para |
| --------- | ------------ | -------- |
| `CLAUDE.md` (raiz do projeto) | Sempre, em toda conversa daquele projeto | Fato do projeto: stack, comandos de build/teste, estrutura de pastas, convenção local |
| **Skill** (`SKILL.md`) | Sob demanda, quando a `description` casa com o pedido | Método reutilizável entre projetos: como revisar código, como escrever ADR |
| **Hook** (`settings.json`) | Executado pelo harness em um evento | Automação determinística: rodar linter ao salvar, bloquear commit fora do padrão |
| **Persona** (texto colado) | Manual | Mudar o tom/postura de uma conversa específica |

Regra de bolso: **fato do projeto → `CLAUDE.md`. Método → skill. "Sempre que X acontecer, faça Y" → hook.**

O terceiro é o mais confundido. Pedido do tipo "toda vez que eu salvar, rode o teste" não se resolve escrevendo isso no `CLAUDE.md` — o modelo pode esquecer. Isso é hook: quem executa é o harness, não o modelo.

## Precedência

Do mais específico para o mais geral:

1. Regra de workspace / `CLAUDE.md` do projeto
2. Configuração global do usuário
3. Comportamento padrão do agente

Conflito entre regra global e regra de projeto: **projeto ganha** — desde que não viole segurança, escopo ou honestidade técnica. Isso já está registrado em [`ia/regras/global-rules.md`](../../regras/global-rules.md) seção 14, e vale para qualquer agente, não só o Claude.

## Skills

Formato, regras de escrita e checklist: [CONVENCOES.md](../../../CONVENCOES.md) seção 6.

Dois pontos que quebram skill na prática:

- **`description` vaga = skill que nunca dispara.** É o único texto que o modelo lê para decidir carregar a skill. Precisa conter os gatilhos como eles aparecem na fala real.
- **Frontmatter extra quebra o carregamento.** `SKILL.md` aceita `name` e `description`. Os campos de nota do vault (`tipo`, `dominio`, `tags`) não entram ali — `./scripts/validar-vault.py` checa isso.

## Instalação das skills deste vault

```bash
./scripts/sync-skills.sh          # simula
./scripts/sync-skills.sh --apply  # cria os symlinks em ~/.claude/skills
```

Se o script reportar *"já existe um diretório real"*, é porque a skill foi **copiada** para `~/.claude/skills` em vez de ligada. Cópia é o pior dos dois mundos: edita no vault e o Claude continua lendo a versão velha. Para converter, tendo confirmado que o vault tem a versão boa:

```bash
rm -rf ~/.claude/skills/<nome-da-skill>
./scripts/sync-skills.sh --apply
```

---

## Backlog

- [ ] Documentar os hooks realmente em uso (evento, comando, por que existe)
- [ ] `settings.json` vs `settings.local.json` — o que versionar e o que manter fora do Git
- [ ] Permissões: quais comandos vale pré-aprovar para reduzir prompt
- [ ] Subagentes: quando delegar compensa o custo de contexto frio

## Ver também

- [Conectores (MCP)](conectores.md)
- [Global Rules](../../regras/global-rules.md) · [Workspace Rules](../../regras/workspace-rules.md)
