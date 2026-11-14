---
titulo: "instagram-agent-skill — 13 skills do Claude para Instagram (gancho, legenda, auditoria, pesquisa de virais)"
resumo: "Pacote MIT de 13 skills e 5 scripts Python locais (sem rede). O método de auditoria e de pesquisa de virais é bom; o resto é em inglês, genérico e se sobrepõe aos guias do 05-Editor. Sinais de estrelas infladas. Usar como referência, não instalar."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/marketing-e-conteudo, skills, instagram]
status: ativo
atualizado: 2026-11-13
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: marketing-e-conteudo
natureza: skill
quando_usar: "Como referência de método: métricas do ig-audit (múltiplo sobre a mediana, envios e seguidores por alcance) e pesquisa do ig-viral (contas até 10x o seu tamanho), quando houver 10+ posts com métricas."
quando_nao_usar: "Instalar as 13 skills globalmente: inglês (fórmulas, humanizador, 165 palavras/min), genéricas e concorrem com formatos/ e guias do 05-Editor."
pre_requisito: "Métricas por post registradas (views, alcance, envios, seguidores) para o método de auditoria ter dado."
---

# instagram-agent-skill

> **Radar: ⏳ avaliar.** O valor está em duas ideias de método, que dá para aplicar sem instalar nada.

## O que é

`Jakeschincariol/instagram-agent-skill`, MIT, criado em 2026-09-13. Verificado em 2026-11-13 via `gh api`:

- **6.307 estrelas e 1.232 forks**, mas **1 contribuidor, 2 commits**, nenhum commit depois do dia da criação e 60 issues abertas. É o padrão de repositório viral com estrelas possivelmente infladas (mesmo sinal do [[open-higgsfield]]).
- 13 skills (`/ig-reel`, `/ig-viral`, `/ig-caption`, `/ig-audit`, `/ig-plan`, `/ig-human`…) e 5 scripts Python. Li os scripts: só biblioteca padrão, **sem rede, sem chave, sem login**. Não conecta ao Instagram: o dado é colado pelo usuário ou lido no navegador dele.
- O README manda "colar no Claude e instalar": é instrução de terceiro, não seguida.

## O que aproveitar

- **ig-audit:** ranquear posts por múltiplo sobre a própria mediana e por envios por alcance, não por views; olhar seguidores por alcance e retenção em 3 s.
- **ig-viral:** pesquisar referências em contas até ~10x o seu tamanho e medir o múltiplo de cada vídeo sobre a mediana da conta. Ler, não raspar, e nunca logar pelo usuário.

## Quando não usar

- Instalação global: 13 skills a mais no contexto, em inglês, com regras que conflitam com `05-Editor/formatos/`.
- Humanizador e legenda: lista de "slop" e cálculo de tempo de fala feitos para inglês.

## Ver também

- [[metricool]] (fonte dos números) · [[categoria-marketing-e-conteudo]] · [[catalogo-do-radar]]

## Fontes

- [github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) (README e `skills/*/SKILL.md`, `*.py` lidos em 2026-11-13)
- [AlphaSignal — anúncio do pacote](https://alphasignal.ai/news/instagram-agent-skill-packs-13-claude-commands-into-one-open-source-bundle)
