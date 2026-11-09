---
titulo: "Lote — 9 ferramentas open source de uma lista viral (2026-11)"
resumo: "Registro do lote 'ferramentas open source que você pode usar': Higgsfield, VoiceStudio, OpenSEO, AppFlowy, OpenWhispr, OpenProject, Cal.diy, Chatwoot e Cap. Cada uma tem ficha própria no radar; aqui ficam a visão geral, o resumo de licenças e a regra de self-host."
tipo: referencia
dominio: radar
tags: [murilo/radar, open-source, self-hosted, licenca]
status: ativo
atualizado: 2026-11-09
---

# Lote — 9 ferramentas open source de uma lista viral (2026-11)

## 📌 Resumo

Uma lista de "ferramentas open source que você pode usar" foi checada item por item no GitHub: o repositório certo, a **licença**, sinais de **atividade real** e o **custo escondido**. Cada ferramenta tem ficha própria no radar. Esta nota guarda só o que vale para o lote inteiro.

> 💡 **Analogia:** "receitas grátis" num livro de culinária. A receita é grátis, os ingredientes não, e algumas exigem um forno industrial.

## 🧠 1. Visão geral (veredito na ficha de cada uma)

| Ferramenta | Alternativa a | Licença | Radar | Ficha |
| --- | --- | --- | --- | --- |
| Chatwoot | Intercom, Zendesk | MIT, exceto `enterprise/` | ⏳ avaliar (ADR do inbox do AsyncHub) | [[chatwoot]] |
| Cal.diy | Calendly / Cal.com | MIT | ✅ adotar, como referência do Encaixe | [[cal-diy]] |
| OpenWhispr | Wispr Flow | MIT | ✅ adotar | [[openwhispr]] |
| Cap | Loom | AGPL-3.0 | ✅ adotar | [[cap]] |
| OpenSEO | Semrush, Ahrefs | MIT (API paga) | ⏳ avaliar | [[openseo]] |
| VoiceStudio | ElevenLabs | AGPL-3.0 (modelos com licença própria) | ⏳ avaliar | [[voicestudio]] |
| AppFlowy | Notion | AGPL-3.0 | ⏳ avaliar | [[appflowy]] |
| OpenProject | Jira, MS Project | GPL-3.0 | ⏳ avaliar | [[openproject]] |
| Open Higgsfield | Higgsfield AI | **nenhuma** | ⛔ evitar | [[open-higgsfield]] |

## 🧠 2. Licença em 30 segundos

- **MIT:** use, copie e embuta no seu produto, inclusive pago, mantendo o aviso de copyright.
- **AGPL-3.0:** usar internamente ou fazer self-host para você é livre. Se você **modificar e oferecer como serviço pela rede** (dentro do Encaixe ou do AsyncHub), tem que publicar o código-fonte dessa versão. Nunca copie trecho de AGPL para dentro de produto fechado.
- **GPL-3.0:** parecida, mas a obrigação vale para distribuição, não para uso em rede.
- **Sem licença:** todos os direitos reservados. Pode ler, não pode usar.

## ✅ 3. Regra geral de self-host

Cada serviço hospedado por você é mais um servidor para atualizar, fazer backup e proteger. No seu estágio, prefira **app desktop** (OpenWhispr, Cap, VoiceStudio) ou **usar como referência de código** (Cal.diy, Chatwoot). Faça self-host só quando o serviço for parte do produto e isso estiver decidido num ADR.

## 🔗 Ver também

- [[como-usar-o-radar]] · [[catalogo-do-radar]] · [[adocao-de-ferramenta]]
- [[categoria-produto-e-atendimento]] · [[categoria-produtividade]] · [[categoria-marketing-e-conteudo]]

## 📚 Fontes

READMEs, LICENSE e metadados lidos via API do GitHub em 2026-11-09. Os links de cada repositório estão nas fichas.
