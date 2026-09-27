---
documento: plano-de-implementacao
projeto: "{{nome do projeto}}"
status: rascunho        # rascunho → em-revisao → aprovado
versao: 0.1
aprovado_por:
aprovado_em:
atualizado: AAAA-MM-DD
---

# 06 · Plano de implementação — {{nome do projeto}}

> [!NOTE]
> **Sobre este documento — leia antes de preencher ou revisar**
>
> **O que é:** a sequência de entregas **pequenas, verificáveis e ordenadas por dependência** que transforma os cinco documentos anteriores em código funcionando.
>
> **Para que serve:** é o roteiro que o agente de IA executa, uma tarefa por vez. Tarefa pequena = contexto pequeno = menos alucinação e revisão possível. Também é o seu painel de progresso: dá para saber, a qualquer momento, onde o projeto está.
>
> **Vem de:** os cinco documentos anteriores, todos aprovados. · **Alimenta:** issues e PRs (fluxo issue → PR), commits e a auditoria final contra o PRD (skill `spec-compliance`).
>
> **Não entra aqui:** decisão de produto ou de arquitetura. Se uma tarefa exige decidir algo novo, a decisão volta para o documento de origem primeiro.

> [!IMPORTANT]
> **Revisão humana — confira antes de aprovar**
>
> - [ ] **Todo RF Must** do PRD aparece em alguma tarefa — e nenhuma tarefa implementa algo fora do PRD.
> - [ ] Cada tarefa é **pequena** (cabe numa PR que eu consigo revisar, idealmente menos de um dia) e tem **critério de pronto verificável**.
> - [ ] **Fundação primeiro** (setup, auth, esquema, deploy vazio) e **o mais incerto cedo** — risco descoberto na semana 1 é barato, na semana 6 é caro.
> - [ ] Existe uma **fatia vertical** funcionando cedo: algo que um usuário real consegue usar de ponta a ponta — em vez de "todo o backend, depois todo o front".
> - [ ] **Teste e validação** estão dentro de cada fase, não numa fase "testes" no final.
> - [ ] Os **pontos de parada** para minha revisão estão marcados.
> - [ ] A **estimativa** é realista. A IA costuma subestimar integração, deploy e correção de bug.
>
> **Sinais de alerta:** tarefa do tipo "implementar o backend"; fase final chamada "ajustes e testes"; nenhum marco demonstrável antes do fim.

---

## 1. Estratégia

_Duas a quatro linhas: qual é a primeira fatia vertical, o que é validado primeiro e por quê._

## 2. Marcos

| Marco | O que dá para demonstrar ao final | RFs cobertos | Data alvo |
| :--- | :--- | :--- | :--- |
| M1 — Fundação | Deploy vazio no ar, login funcionando | | |
| M2 — Fatia vertical | | | |
| M3 — MVP | | | |

## 3. Tarefas

Formato: `T-NN` · o que fazer · referências (RF, TELA, tabela) · depende de · pronto quando.

### Fase 1 — Fundação

- [ ] **T-01** · Criar repositório, lint e CI · — · depende de: nada · **pronto quando:** CI roda verde num commit vazio.
- [ ] **T-02** · …

> ⏸️ **Checkpoint humano:** revisar M1 antes de seguir.

### Fase 2 — {{fatia vertical}}

- [ ] **T-NN** · …

## 4. Definição de pronto (vale para toda tarefa)

- [ ] Critério de pronto da tarefa atendido e demonstrado.
- [ ] Lint, tipos e testes passando.
- [ ] Nada fora do escopo da tarefa foi alterado.
- [ ] Se algo divergiu dos documentos, o documento de origem foi atualizado.

## 5. Riscos e plano B

| Risco | Sinal de que está acontecendo | Plano B |
| :--- | :--- | :--- |
| | | |

## 6. Registro de progresso e desvios

| Data | Tarefa | O que aconteceu / o que mudou | Documento atualizado |
| :--- | :--- | :--- | :--- |
| | | | |

## 7. Registro de mudanças

| Versão | Data | Mudança | Motivo |
| :--- | :--- | :--- | :--- |
| 0.1 | | Primeira versão | |
