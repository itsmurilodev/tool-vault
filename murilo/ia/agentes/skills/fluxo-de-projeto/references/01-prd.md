---
documento: prd
projeto: "{{nome do projeto}}"
porte: substancial      # pequeno (só PRD enxuto + Plano) | substancial (os 6)
status: rascunho        # rascunho → em-revisao → aprovado
versao: 0.1
aprovado_por:
aprovado_em:
atualizado: AAAA-MM-DD
---

# 01 · PRD — {{nome do projeto}}

> [!NOTE]
> **Sobre este documento — leia antes de preencher ou revisar**
>
> **O que é:** o *Product Requirements Document* define **o que** será construído e **por quê**, do ponto de vista de quem usa e do negócio. Não fala de tecnologia.
>
> **Para que serve:** é a fonte de verdade do escopo. Os outros cinco documentos derivam dele — se algo nos outros não rastreia para um requisito daqui, é escopo inventado. No fim, o código é auditado contra este PRD.
>
> **Vem de:** conversa de levantamento de requisitos (skill `levantamento-requisitos`). · **Alimenta:** todos os outros documentos.
>
> **Não entra aqui:** stack, banco, biblioteca, layout de tela, cor. Isso é TRD, Backend e UI/UX.

> [!IMPORTANT]
> **Revisão humana — confira antes de aprovar**
>
> - [ ] O **problema** descrito é a dor real, ou é a solução que já veio pronta na cabeça? Consigo explicar a dor sem citar a funcionalidade?
> - [ ] Consigo nomear **uma pessoa ou cliente real** que sente essa dor?
> - [ ] A **métrica de sucesso** tem número e prazo? ("aumentar engajamento" não vale)
> - [ ] A lista **Fora do escopo** existe e é explícita — é ela que segura o *scope creep*.
> - [ ] Cada requisito tem **critério de aceite** que dá para demonstrar ou testar.
> - [ ] O MVP cabe no **prazo e orçamento reais**? Se tudo é *Must*, nada é prioridade.
> - [ ] A IA **não inventou** persona, integração, requisito legal ou número que eu não disse? (procure ativamente)
> - [ ] Hipóteses estão marcadas como hipótese, não escritas como fato.
>
> **Sinais de alerta:** adjetivo sem número ("rápido", "intuitivo", "escalável"); mais de ~10 *Musts* no MVP; persona genérica ("usuários que querem produtividade").

## 🎯 Decisões críticas para validar

> [!WARNING]
> **Preenchido pela IA, respondido por você.** De 1 a 5 pontos deste documento em que um erro agora custa caro depois — porque é difícil de reverter, porque se espalha pelos documentos seguintes ou porque se apoia em hipótese não confirmada. Ponto óbvio não entra. **O documento só é aprovado quando todas as linhas tiverem sua resposta.**
>
> _Onde costumam estar neste documento: o problema e o usuário escolhidos · o corte do MVP (o que é Must) · a métrica que define sucesso · o que ficou fora do escopo._

| # | Decisão ou suposição | Por que pesa no futuro | Se estiver errada… | Recomendação da IA | Sua resposta |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | | | | | ⬜ confirmo · ✏️ ajusto: … |

---

## 1. Resumo

_Três linhas: para quem, qual problema, qual resultado esperado._

## 2. Problema

| Pergunta | Resposta | Fato ou hipótese? |
| :--- | :--- | :--- |
| Qual é a dor concreta? | | |
| Quem sente? | | |
| Como resolve hoje (e quanto custa isso)? | | |
| Que evidência temos de que a dor existe? | | |

## 3. Usuários

| Ator | Objetivo principal | Contexto de uso (onde, quando, dispositivo) |
| :--- | :--- | :--- |
| | | |

## 4. Objetivos e métricas de sucesso

| Objetivo | Métrica | Meta | Prazo |
| :--- | :--- | :--- | :--- |
| | | | |

## 5. Requisitos funcionais

Prioridade em MoSCoW: **Must** (sem isso não lança) · **Should** · **Could** · **Won't** (fica na seção 7).

| ID | Requisito (o usuário consegue…) | Prioridade | Critério de aceite |
| :--- | :--- | :--- | :--- |
| RF-01 | | Must | |
| RF-02 | | | |

## 6. Requisitos não funcionais

Só o que tem meta verificável. Cada RNF precisa de resposta técnica no TRD.

| ID | Categoria (desempenho, segurança, privacidade, disponibilidade, acessibilidade…) | Meta mensurável |
| :--- | :--- | :--- |
| RNF-01 | | |

## 7. Fora do escopo (Won't)

- _O que deliberadamente não será feito nesta versão — e por quê._

## 8. Premissas, restrições e riscos

- **Premissas:** _o que estamos assumindo como verdade sem ter confirmado._
- **Restrições:** _prazo, orçamento, time, legal (LGPD), stack imposta._
- **Riscos:** _o que pode invalidar o produto._

## 9. Perguntas em aberto

- [ ] _Pergunta · quem responde · até quando._

## 10. Registro de mudanças

| Versão | Data | Mudança | Motivo |
| :--- | :--- | :--- | :--- |
| 0.1 | | Primeira versão | |
