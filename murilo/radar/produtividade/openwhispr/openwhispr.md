---
titulo: "OpenWhispr — ditado por voz local no desktop"
resumo: "Aperta uma tecla, fala, e o texto aparece no cursor. Roda local (Whisper/Parakeet) ou com sua chave na nuvem, e também transcreve reunião. MIT. Uso pessoal imediato para escrever prompts longos e notas."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/produtividade, open-source, voz, prompt]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: produtividade
natureza: ferramenta
quando_usar: "Ditar prompts longos (contexto e cenários), notas do vault e transcrever reunião usando o modelo local."
quando_nao_usar: "Gravar reunião sem consentimento dos participantes; modo nuvem em conversa de cliente."
pre_requisito: "App desktop (macOS, Windows ou Linux) e modelo local baixado no próprio app."
---

# OpenWhispr

> **Radar: ✅ adotar.** Custo zero, risco baixo, ganho direto no prompt de três seções.

## O que é

`OpenWhispr/openwhispr` (11 mil estrelas, MIT). Ditado por voz: você aperta uma tecla, fala, e o texto vai para onde está o cursor. Roda **local** (Whisper ou Parakeet) ou com modelo em nuvem usando a sua chave (BYOK). Também transcreve reuniões e identifica quem falou, localmente.

## Quando usar

- Escrever o contexto e os cenários de verificação de um prompt longo ([[prompt-com-cenarios-de-verificacao]]). Falar é mais rápido que digitar.
- Notas do vault e transcrição de reunião com cliente (com consentimento).

## Quando não usar

- Reunião gravada sem avisar: voz é dado pessoal.
- Modo nuvem em conversa sensível: prefira o modelo local, em que o áudio não sai da máquina.

## Como usar

1. Instale o app pela release oficial (ou `brew` cask) e baixe um modelo local no próprio app.
2. Defina a tecla de atalho e use direto no editor do prompt.

## Ver também

- [[prompt-com-cenarios-de-verificacao]] · [[categoria-produtividade]]

## Fontes

- [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr)
