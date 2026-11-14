---
titulo: "HyperFrames (HeyGen) — vídeo a partir de HTML, feito para agentes"
resumo: "Framework Apache-2.0 da HeyGen que transforma HTML/CSS/animação em MP4 determinístico, com skills para Claude Code. Plugin instalado desde 2026-11-10, mas fora dos fluxos do 05-Editor: concorre com o Remotion, que já é o motor. Avaliar só para avulso com motion graphics."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, video, skills]
status: ativo
atualizado: 2026-11-14
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: marketing-e-conteudo
natureza: ferramenta
quando_usar: "Vídeo avulso explicativo ou de tech com motion graphics que o Remotion e o FilmCraft não resolvem bem; nesse caso, um design.md na raiz do projeto passa a valer (o HyperFrames lê frame.md/design.md)."
quando_nao_usar: "Vlog de rotina e POV (corte seco, só tipografia); como segundo motor ao lado do Remotion; skills reverse-any-video e style-sampling, que são pagas (Pro) e enviam uso à HeyGen."
pre_requisito: "Um vídeo avulso aprovado que precise de motion graphics, e a decisão de usar HyperFrames em vez do Remotion para esse papel."
---

# HyperFrames

> **Radar: ⏳ avaliar.** É uma boa ferramenta, mas hoje somaria um segundo motor de render sem dor que o justifique.

## O que é

`heygen-com/hyperframes`, Apache-2.0, ~84 mil estrelas, mais de 100 contribuidores, commit em 2026-11-14 (verificado via `gh api`). Escreve o vídeo em HTML e renderiza em MP4 determinístico, com CLI (`npx hyperframes`), app desktop gratuito e skills para agentes. No Mac do Murilo: plugin `hyperframes@hyperframes` 0.9.28, instalado em 2026-11-10 e não usado desde que o Remotion virou o motor do 05-Editor.

Útil de verdade para o 05-Editor: `npx hyperframes measure` (cortes, eventos, faixas de quadros em volta de cada corte, sincronia boca × voz), que mede um vídeo sem precisar adotar o motor. O `scripts/previa_corte.py` do 05-Editor cobre a revisão de cortes sem ele.

## Quando usar

- Avulso de tech ou IA com animação de interface, contador, diagrama: gerar o motion e montar no FilmCraft.

## Quando não usar

- Vlog de rotina e POV: o formato é corte seco com tipografia, já resolvido no FilmCraft e no Remotion.
- `reverse-any-video` e `style-sampling`: recursos Pro (pagos); copiar vídeo de terceiro também esbarra em direito de imagem.

## Como usar

1. Num vídeo avulso aprovado, propor como TESTE no briefing, com o motivo.
2. Desligar a telemetria antes: `npx hyperframes telemetry disable`.

## Riscos e custos

- **Telemetria ligada por padrão** (anônima até fazer login), e cada skill manda um "usage beacon" com o nome dela, ligado à conta quando logado.
- Node 22+ e Chrome; o plano Pro do Studio cobra pelos modelos da HeyGen.
- Dois motores (Remotion + HyperFrames) duplicam presets e tipografia.

## Ver também

- [[remotion]] · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes): README, `docs/packages/cli.mdx` (measure), `docs/faq.mdx` (telemetria), `skills/*/SKILL.md` (lidos em 2026-11-14 no plugin instalado)
