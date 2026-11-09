---
titulo: "Open Higgsfield — interface de geração de imagem e vídeo (descartado)"
resumo: "Vendido como alternativa open source ao Higgsfield AI, mas não tem licença, tem 1 contribuidor e 3 commits contra 5,5 mil estrelas, é só uma interface para uma API de geração paga, e a versão hospedada pede a sua chave de API."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/marketing-e-conteudo, open-source, geracao-de-imagem, risco]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: evitar
categoria: marketing-e-conteudo
natureza: ferramenta
quando_usar: "Não usar. Para gerar imagem ou vídeo por IA, use direto o serviço oficial escolhido, com a chave guardada só com você."
quando_nao_usar: "Sempre: sem licença (todos os direitos reservados), sinais de estrelas infladas, e a versão hospedada recebe a sua chave de API."
pre_requisito: "—"
---

# Open Higgsfield

> **Radar: ⛔ evitar.** É o exemplo de "open source" que não é open source.

## Sinais de alerta (verificados no GitHub em 2026-11-09)

- **Sem arquivo de licença.** Sem licença valem todos os direitos reservados: você pode ler o código, mas não tem permissão legal para usar, copiar ou modificar.
- **1 contribuidor e 3 commits**, contra 5,5 mil estrelas e 1,2 mil forks em menos de 3 meses. É um padrão comum de estrelas infladas.
- **Não gera nada sozinho.** É uma interface para uma API de geração paga (`HF_API_BASE_URL`, modelos "Soul", que são do Higgsfield), e você entra com a sua chave de plataforma.
- **A versão hospedada** (`openhiggsfield.ai`) pede que você entregue a chave da API a um terceiro desconhecido.

## O que fazer em vez disso

- Gerar imagem ou vídeo direto no serviço oficial escolhido, com a chave guardada no seu cofre.

## Lição para o radar

Na triagem de qualquer repositório viral, confira: **licença**, **número de contribuidores e de commits** versus estrelas, **de onde vem o processamento** (o que é local e o que é API paga) e **quem guarda as suas chaves**. Ver [[como-usar-o-radar]].

## Ver também

- [[open-source-self-hosted-triagem]] · [[categoria-marketing-e-conteudo]]

## Fontes

- [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) (sem LICENSE, 1 contribuidor)
