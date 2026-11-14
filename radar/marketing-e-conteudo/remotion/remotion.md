---
titulo: "Remotion — vídeo feito com código React (motor do Fluxo 1 do 05-Editor)"
resumo: "Framework React que renderiza vídeo quadro a quadro. É o motor de render da edição automática do 05-Editor desde 2026-11-10 (V01, V02, V04, V06). Licença própria: grátis para pessoa física e empresa de até 3 funcionários."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, video]
status: ativo
atualizado: 2026-11-14
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: marketing-e-conteudo
natureza: ferramenta
quando_usar: "Render da edição automática (Fluxo 1) do 05-Editor: trechos cortados + tipografia (presets em remotion/src/estilo.tsx, composição Lote.tsx)."
quando_nao_usar: "Corte e revisão de timeline com o usuário (é o FilmCraft, Fluxo 2); motion graphics ao lado de outro motor (HyperFrames) no mesmo projeto; empresa com mais de 3 funcionários sem licença Company."
pre_requisito: "Node 22+ e o projeto remotion/ do 05-Editor; se a Async Studio passar de 3 funcionários, licença Company."
---

# Remotion

> **Radar: ✅ adotar.** Já está em uso real no 05-Editor; o concorrente direto (HyperFrames) fica em avaliar para não haver dois motores.

## O que é

`remotion-dev/remotion`, 73 mil estrelas, ativo (commit em 2026-11-13). Escreve o vídeo como componentes React e renderiza quadro a quadro com Chrome headless + FFmpeg. Versão em uso no 05-Editor: 4.0.542.

**Licença (lida em `node_modules/remotion/LICENSE.md`, 2026-11-14):** não é open source padrão (o GitHub mostra `NOASSERTION`). Grátis, inclusive para uso comercial, para pessoa física, organização sem fins lucrativos e empresa com até 3 funcionários; acima disso, licença Company paga. A versão 5.0 vai mudar um pouco os termos.

## Quando usar

- Fluxo 1 do 05-Editor: `scripts/finalizar.sh` renderiza a composição `Lote` sobre os trechos preparados.
- Tipografia por código quando o FilmCraft não estiver no fluxo.

## Quando não usar

- Revisão de corte com o usuário: a timeline do FilmCraft (Fluxo 2) é mais rápida para ajustar.
- Junto com o HyperFrames para a mesma função: escolha um motor.

## Como usar

1. Siga `05-Editor/guias/edicao-ia.md` e `05-Editor/scripts/README.md`.

## Riscos e custos

- Licença por tamanho de empresa: rever se a Async Studio crescer.
- O ffmpeg do Mac não tem `drawtext` nem `libass`, por isso todo texto queimado no vídeo passa pelo Remotion (ou pelo FilmCraft).

## Ver também

- [[hyperframes]] · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [github.com/remotion-dev/remotion](https://github.com/remotion-dev/remotion) e `LICENSE.md` do pacote 4.0.542 (lidos em 2026-11-14)
- `05-Editor/historico/PLANO.md` (por que o Remotion virou o motor no lugar do HyperFrames)
