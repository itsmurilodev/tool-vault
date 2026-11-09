---
titulo: "VoiceStudio — voz por IA local (alternativa ao ElevenLabs)"
resumo: "Clonagem e design de voz, dublagem, ditado, transcrição e audiolivro em 646 idiomas, rodando local (Apple Silicon, CUDA ou CPU). O app é AGPL; cada modelo e cada áudio gerado têm licença própria. Clonar voz exige consentimento."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, open-source, voz, conteudo]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: marketing-e-conteudo
natureza: ferramenta
quando_usar: "Narração ou dublagem de conteúdo da Async com a sua voz ou com voz sintética de licença comercial."
quando_nao_usar: "Clonar voz de cliente ou de terceiro sem autorização escrita; usar modelo sem licença comercial em material comercial."
pre_requisito: "Conferir a licença de cada modelo no Model Manager do app antes do uso comercial."
---

# VoiceStudio

> **Radar: ⏳ avaliar.** Tecnicamente forte e local. O cuidado é jurídico (licença de modelo e consentimento de voz), não técnico.

## O que é

`debpalash/VoiceStudio` (106 mil estrelas desde 2026-04, AGPL-3.0). Tem mais de 7 mil commits e mais de 100 contribuidores, então a atividade é real. **[PROVÁVEL]** Parte das estrelas vem de viralização. Roda local em macOS (Metal), Windows e Linux (CUDA, ROCm ou CPU). Há versões Pro e Cloud pagas.

## Quando usar

- Narrar um vídeo ou demo da Async, ou dublar para outro idioma, com a **sua** voz ou com uma voz sintética de licença comercial.

## Quando não usar

- Com voz de cliente ou terceiro sem autorização escrita: voz é dado pessoal e biométrico.
- Com modelo cuja licença não permite uso comercial: o README avisa que pesos, vozes e áudio gerado têm licenças próprias.

## Como usar

1. Instale a release desktop.
2. No Model Manager, escolha um modelo com licença comercial e registre qual foi usado.
3. Guarde o consentimento de qualquer voz clonada que não seja a sua.

## Ver também

- [[open-source-self-hosted-triagem]] · [[categoria-marketing-e-conteudo]]

## Fontes

- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) (seção *License & responsible use*)
