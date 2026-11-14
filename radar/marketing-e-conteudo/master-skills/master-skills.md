---
titulo: "master-skills (Jake Schincariol) — skills edit, virality e build num pacote"
resumo: "Pacote MIT com 3 skills (editar vídeo, roteiro viral, construir site) e scripts Python locais. Mesmo autor do instagram-agent-skill, 1 commit. O corte de silêncio e o método da mediana já existem no 05-Editor; duas ideias de revisão de EDL valem como referência. Não instalar."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, skills, video]
status: ativo
atualizado: 2026-11-14
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: marketing-e-conteudo
natureza: skill
quando_usar: "Como referência: revisar a EDL antes do render com veto por corte (apply:false) e, em frase repetida, ficar com a última tomada."
quando_nao_usar: "Instalar: em inglês (hookscore, humanizador, 170 palavras/min), concorre com os guias e scripts do 05-Editor (pausas.py com VAD, montar_edl.py, método da mediana em social/README.md)."
pre_requisito: "Nenhum para ler."
---

# master-skills

> **Radar: ⏳ avaliar.** Referência de método; o 05-Editor já faz o mesmo de forma mais adequada ao material dele.

## O que é

`Jakeschincariol/master-skills`, MIT, criado em 2026-10-04, 179 estrelas, 37 forks, **1 contribuidor e 1 commit** (verificado via `gh api` em 2026-11-14). Mesmo autor do [[instagram-agent-skill]] (6 mil estrelas com 2 commits) e do `youtube-agent-skill`. Três skills:

- `edit`: corta silêncio, hesitação e tomada repetida (`deadspace.py`, limiar de energia adaptativo, crossfade de 30 ms), legenda de 1–3 palavras, exporta a −14 LUFS. Encaminha motion graphics para HyperFrames ou Remotion.
- `virality`: coleta posts (colado pelo usuário ou `yt-dlp` em Shorts públicos), ranqueia pelo múltiplo sobre a mediana do criador, pontua o gancho em 26 fórmulas.
- `build`: sites.

Os scripts usam só a biblioteca padrão do Python e ffmpeg (sem chamada de rede nos arquivos lidos).

## Quando usar

- Ideias para a revisão de cortes do 05-Editor: veto por corte na EDL antes do render; "a última tomada vence" em frase repetida.

## Quando não usar

- Corte de silêncio: o 05-Editor usa VAD (Silero), melhor que limiar de energia no ruído do óculos.
- Gancho e legenda: fórmulas e humanizador em inglês.

## Como usar

1. Ler `skills/edit/SKILL.md` ao mexer em `05-Editor/scripts/montar_edl.py`; não instalar.

## Riscos e custos

- Estrelas possivelmente infladas (mesmo padrão do instagram-agent-skill).

## Ver também

- [[claude-virality-skill]] · [[instagram-agent-skill]] · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [github.com/Jakeschincariol/master-skills](https://github.com/Jakeschincariol/master-skills) (`skills/edit/SKILL.md`, `skills/virality/SKILL.md`, `collect.py`, `deadspace.py` lidos em 2026-11-14)
