---
titulo: "Correção de bug com agentes — reproduzir, corrigir, provar, revisar"
resumo: "Processo de 4 etapas visto em reel (reproduzir com dado real, corrigir, verificar com o app rodando, revisão multi-modelo com auto-merge). A espinha está certa; dado de produção cru e merge sem humano não passam no portão para o seu estágio."
tipo: conceito
dominio: radar
tags: [murilo/engenharia, agentes, verificacao, processo, lgpd]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: fluxo-com-agentes
natureza: pratica
quando_usar: "Bug reportado (usuário ou tracker) que não é óbvio lendo o código: reproduzir, corrigir com teste falhando antes, provar no app, revisar."
quando_nao_usar: "Typo, texto ou estilo; com dado de produção cru; com merge automático sem histórico de autonomia."
pre_requisito: "verify-<app> no projeto e fixture anonimizada."
---

# Correção de bug com agentes — reproduzir, corrigir, provar, revisar

## 📌 Resumo

O processo do reel tem quatro etapas: (1) reproduzir o erro com o dado real que o causou, (2) corrigir usando esse mesmo dado, (3) provar a correção subindo o app de verdade e anexando capturas de tela no PR, e (4) pedir revisão a dois modelos diferentes e deixar o agente fazer o merge sozinho se os três concordarem.

A **espinha** é boa e é praticamente o playbook *Bug fix* do pstack ([[pstack-verificacao]]): reproduzir antes de corrigir, ter evidência de runtime e verificar na mesma superfície. Duas peças **não passam** no [[adocao-de-ferramenta]] para o seu estágio:

- **Dado de produção cru na máquina local e no contexto do modelo.** Isso esbarra na LGPD, abre um vetor de prompt injection e vaza dados nas capturas de tela.
- **Merge sem humano.** O argumento de "big tech" apresentado no reel é o contrário do que essas empresas fazem.

> 💡 **Analogia:** perícia de acidente. O perito reconstrói a batida com as mesmas condições (velocidade, piso molhado, ângulo), mas não precisa do nome e do CPF do motorista para isso. O que causou o acidente é a condição, não a identidade.

## 🧠 1. O que está certo e por quê

| Etapa | Por que funciona |
| --- | --- |
| **Reproduzir antes de corrigir** | Sem reprodução não existe "corrigido", só "parou de aparecer". O pstack exige o mesmo: o repro que falhava precisa passar depois, e "inconclusivo" não conta como sucesso. |
| **Corrigir sobre o caso que quebrou** | Dado fictício costuma ser limpo demais. O bug geralmente mora no formato: `null` onde ninguém esperava, acento, emoji, fuso horário, string enorme, registro órfão. |
| **Provar com o app rodando** | Teste unitário mostra que um ramo do código se comporta, não que o bug sumiu. É exatamente o que o `verify-<app>` gerado pela `create-verification-skill` faz. |
| **Segunda opinião de outro modelo** | Modelos diferentes erram de jeitos diferentes. Uma revisão cruzada barata pega coisas que o implementador não vê. |

**A ligação com verificação que você suspeitou existe:** a etapa 3 é literalmente o `verify-<app>`, e a etapa 1 também deveria usá-lo, porque reproduzir na mesma superfície onde o usuário viu o erro é o mesmo roteiro rodado antes da correção.

## ⚠️ 2. Onde o processo do reel quebra

### 2.1 Dado real de produção (LGPD + segurança)

- Encaixe e AsyncHub guardam **dado pessoal** (clientes, agendamentos, leads). Clonar produção para a máquina local e colocar esse dado no contexto do modelo significa compartilhá-lo com o provedor do modelo (Anthropic, OpenAI, xAI), quase sempre fora do Brasil. **[PROVÁVEL]** Pela LGPD, isso exige base legal, minimização e medidas de segurança (princípios de finalidade e necessidade, art. 6º; segurança, art. 46; transferência internacional, art. 33). Antes de usar em projeto real, confirme com quem cuida do jurídico.
- Em projeto de cliente o problema é maior: o dado é do cliente (controlador) e você é operador. Usar esse dado em desenvolvimento exige autorização dele.
- **Prompt injection:** texto de produção é texto que *usuários digitaram*, como observação de agendamento, mensagem de lead ou nome. Um agente que lê esse texto **e** tem permissão de fazer merge é exatamente o cenário de injeção que suas diretrizes mandam evitar.
- **Capturas de tela com dado real no PR** publicam dado pessoal no GitHub e deixam esse dado no histórico do repositório.
- A transcrição também fala em "dados reais na **instância de produção real**". Se isso quer dizer depurar contra o banco de produção, é pior ainda: o agente passa a ter escrita no banco real. Nunca.

**Alternativa:** reproduzir o **formato** do dado sem a identidade. Extraia só as linhas envolvidas no erro, troque os campos pessoais por valores falsos que preservem tipo, tamanho, nulos, acentos e fuso, e grave isso como fixture de teste. O bug continua reproduzindo, porque o que o causou foi o formato, e nada pessoal sai do banco.

### 2.2 Consenso de modelos com auto-merge

- **Os erros dos modelos andam juntos.** Revisores leem o mesmo diff e a mesma descrição de PR escrita pelo implementador. Se a premissa estiver errada (o requisito foi mal entendido), os três concordam com a premissa errada. E modelo revisor tem tendência a aprovar.
- **Merge em `main` com deploy automático (Vercel) é um deploy.** O próprio pstack põe *deploys* na lista de ações que sempre pausam para o humano.
- **"Pense em como funciona uma big tech":** o argumento se inverte. Em empresas grandes, a revisão por outra pessoa é obrigatória. No Google, toda mudança precisa de aprovação de um revisor, e controles de *change management* em auditoria (SOC 2) costumam exigir separação entre quem escreve e quem aprova. **[PROVÁVEL, prática pública amplamente documentada]**
- **Revisar não é "segurança psicológica", é operabilidade.** Quando o Encaixe cair às 3h da manhã, quem depura é você. Código que você nunca leu é um sistema que você não conhece.

## ✅ 3. Versão adaptada para o seu estágio

```text
Sentry (erro) ─► 1. Reproduzir ─► 2. Corrigir ─► 3. Provar ─► 4. Revisar ─► você faz o merge
                  fixture anonimizada  teste falhando   verify-<app>  2º modelo
                  + verify-<app>       antes do fix     + evidência   + CI verde
```

1. **Contexto e reprodução.** Puxe do Sentry o stack trace, os breadcrumbs e o ID do registro. Extraia só as linhas envolvidas, anonimize com script e grave como fixture. Reproduza pelo `verify-<app>` na mesma superfície (tela, rota ou API). Sem reprodução, não passa para a etapa 2: instrumente até o erro aparecer.
2. **Corrigir.** Primeiro faça commit do teste que falha (com a fixture), depois do fix, para que o histórico prove a sequência. Aplique a menor mudança que a evidência justifica. Se o fix for um *guard* em volta do sintoma, ele só conta como correção quando o estado que ele trata é legítimo.
3. **Provar.** Rode o `verify-<app>`: o repro que falhava agora passa e a feature continua funcionando. Na descrição do PR vão a saída antes e depois, a transcrição ou o snapshot ARIA (texto, sem dado pessoal). Capturas de tela só com dado anonimizado. **[PROVÁVEL]** O `gh` não sobe imagem para comentário de PR, então a forma mais simples é evidência em texto na descrição e imagens como artifact do CI ou guardadas localmente.
4. **Revisar.** CI verde (lint, testes, `semgrep-scan`) mais revisão de um **segundo modelo**: o `/code-review` do Claude Code e o Codex, que você já usa. O merge fica com você, com branch protection exigindo sua aprovação.

### Escada de autonomia: auto-merge se conquista com histórico

| Degrau | Quando subir | Merge |
| --- | --- | --- |
| **0 — hoje** | — | Sempre você |
| **1** | Algumas semanas em que a sua revisão não encontrou nada que os modelos deixaram passar | Auto-merge só para mudanças de baixo risco: texto, estilo, dependência *patch*, teste |
| **2** | Degrau 1 estável e rollback testado | Ampliar para bug fix pequeno, **nunca** para migração, auth, RLS, pagamento ou dado pessoal |

## 🔗 Ver também

- [[pstack-verificacao]]: a etapa 3 é o `verify-<app>`.
- [[captura-de-erros-para-agentes]]: como o erro de produção chega até a etapa 1.
- [[fluxo-issue-pr]]: PR pequeno o bastante para ser revisado de verdade e check verde obrigatório.
- [[observabilidade]] · [[adr-001-observabilidade]]: o Sentry é a origem da etapa 1.
- [[qualidade-automatizada]] · [[adocao-de-ferramenta]]
- Skills [semgrep-scan](../../../agentes/skills/semgrep-scan/SKILL.md) · [create-verification-skill](../../../agentes/skills/create-verification-skill/SKILL.md)

## 📚 Fontes

- Transcrição do reel colada pelo usuário em 2026-11-09 (autor não identificado).
- [pstack — playbook Bug fix e seção Autonomy do poteto-mode](https://github.com/backnotprop/pstack/tree/main/skills/poteto-mode), lidos em 2026-11-09.
- [LGPD — Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), arts. 6º, 33 e 46.
- [Google Engineering Practices — Code Review](https://google.github.io/eng-practices/review/)
