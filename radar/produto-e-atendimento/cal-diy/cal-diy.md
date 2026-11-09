---
titulo: "Cal.diy — agendamento open source (fork MIT do Cal.com)"
resumo: "Versão comunitária do Cal.com sem o código enterprise, 100% MIT, só self-host. Para você, é livro-texto do Encaixe (fuso, disponibilidade, conflito de agenda), não backend; o próprio README desaconselha produção."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/produto-e-atendimento, open-source, agendamento, encaixe]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: produto-e-atendimento
natureza: ferramenta
quando_usar: "Como referência de código ao implementar ou depurar horários, fuso, disponibilidade e conflito de agenda no Encaixe; sendo MIT, dá para reaproveitar um trecho com atribuição."
quando_nao_usar: "Como backend do Encaixe ou em produção (o próprio README recomenda uso pessoal, não produção)."
pre_requisito: "Nenhum para leitura do código."
---

# Cal.diy

> **Radar: ✅ adotar, como referência de código.** Concorrente do Encaixe e livro-texto ao mesmo tempo.

## O que é

`calcom/cal.diy` (50 mil estrelas). Fork comunitário do Cal.com **sem** o código enterprise (times, workflows, SSO, insights), 100% MIT e sem versão hospedada. O README avisa: *"strictly recommended for personal, non-production use"*, e o self-host exige administração avançada de servidor e banco.

## Quando usar

- Ao implementar ou depurar a lógica de horários do [[app-encaixe]]: fuso horário, horário de verão, buffers, conflito com calendário externo, lembretes. Leia como o Cal.diy resolve o caso antes de inventar.
- Para aproveitar um trecho de código: o MIT permite, desde que você mantenha o aviso de copyright.

## Quando não usar

- Como backend do Encaixe: o diferencial do Encaixe (fila de espera e encaixe automático) não existe nele, e o próprio projeto desaconselha produção.

## Como usar

1. Clone para leitura (`git clone --depth 1`) e procure o módulo do caso que você está resolvendo.
2. Ao copiar código, registre a origem no commit e mantenha o aviso MIT.

## Ver também

- [[app-encaixe]] · [[open-source-self-hosted-triagem]] · [[categoria-produto-e-atendimento]]

## Fontes

- [calcom/cal.diy](https://github.com/calcom/cal.diy) (README lido em 2026-11-09)
