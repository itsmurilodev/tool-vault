---
titulo: Conectores do Claude (MCP)
resumo: "Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar."
tipo: referencia
dominio: murilo
tags: [ia/claude, mcp, conectores]
status: ativo
atualizado: 2026-08-09
---

# Conectores do Claude (MCP)

Conector é a embalagem de produto para um **servidor MCP remoto**. MCP (Model Context Protocol) é o padrão aberto criado pela Anthropic para ligar aplicações de IA a ferramentas e dados; o conector é o mesmo mecanismo com OAuth e um botão de "Conectar".

## O fato que muda a decisão de segurança

**Conector remoto roda na infraestrutura da Anthropic, não na sua máquina.** Ao conectar, é o servidor da Anthropic que abre a conexão com o serviço — não o seu notebook. Isso vale em claude.ai, Desktop e mobile.

Consequências práticas:

- O conector funciona em qualquer dispositivo logado, sem instalar nada. É a vantagem.
- O serviço do outro lado vê tráfego vindo da Anthropic, não do seu IP. Importa se houver allowlist de IP.
- Dado que passa pelo conector sai do seu perímetro. Para dado de cliente, isso é uma decisão contratual, não só técnica.

Servidor MCP **local** (stdio, configurado no Desktop ou no Claude Code) é o oposto: roda na sua máquina, acessa arquivo e processo local, e **não** aparece no claude.ai nem no mobile.

| | Conector remoto | MCP local |
| --- | --- | --- |
| Onde executa | Nuvem da Anthropic | Sua máquina |
| Disponível em | claude.ai, Desktop, mobile, Claude Code | Onde foi configurado |
| Acessa arquivo local | Não | Sim |
| Instalação | OAuth, um clique | Config manual por máquina |
| Bom para | SaaS (Notion, Drive, Sentry, Vercel) | Ferramenta interna, script, banco local |

O diretório traz conectores **verificados pela Anthropic** e **da comunidade** — o rótulo importa: comunidade significa que ninguém auditou o que o servidor faz com o que você manda.

## O custo escondido de conectar tudo

Cada conector ativo injeta as definições das ferramentas dele no contexto de toda conversa. Vinte conectores ligados significam:

1. **Menos contexto útil** — a descrição das ferramentas ocupa espaço que seria do seu código ou do seu problema.
2. **Escolha pior de ferramenta** — com dezenas de ferramentas parecidas, a chance de o modelo escolher a errada sobe.
3. **Superfície de injeção maior** — conteúdo que volta de um conector (issue, e-mail, página, comentário) é texto de terceiro. Se ele contiver instrução disfarçada, ela entra no contexto.

Conector não é plugin de navegador: o certo é ligar o que tem função, não colecionar.

## Critério para conectar

Ligue quando as três forem verdade:

1. **Tem trabalho recorrente ali.** Você já perde tempo copiando dado desse serviço para o chat.
2. **Leitura resolve, ou a escrita é reversível.** Conector que só lê é decisão barata. Conector que escreve em produção (banco, deploy) merece o mesmo cuidado de uma credencial.
3. **O dado pode sair do seu perímetro.** Vale especialmente para conta de cliente.

Desligue quando: você não usou nos últimos 30 dias, ou o serviço já está coberto por outro conector.

## Avaliação dos conectores do diretório

Recorte pelo perfil de trabalho (dev/produto/estúdio pequeno), não pela lista inteira.

### Valem cedo

| Conector | Por quê | Cuidado |
| -------- | ------- | ------- |
| **Notion** | Se a documentação de projeto já vive lá, elimina copiar/colar contexto | Escreve — confirme antes de deixar editar página |
| **Sentry** | Erro de produção vira contexto direto no debug, sem screenshot de stack trace | Leitura; risco baixo |
| **Vercel** | Deploy, log de build e diagnóstico de projeto | Ação de deploy é irreversível na prática |
| **Supabase** | Banco, auth e storage sob consulta | **Escreve em banco.** O de maior risco da lista — trate como credencial de produção |
| **Google Drive / Gmail / Calendar** | Só se o trabalho real acontece lá | E-mail é a maior fonte de conteúdo não confiável entrando no contexto |

### Valem em contexto específico

| Conector | Quando |
| -------- | ------ |
| **Excalidraw** | Diagrama de arquitetura junto com ADR — casa com a skill `decisao-arquitetural` |
| **Postman** | Se as coleções de API já estão versionadas lá |
| **Granola / Wispr Flow** | Se reunião com cliente já é gravada e transcrita nessa ferramenta |
| **Canva / Gamma / Adobe** | Entrega visual e apresentação para cliente |
| **Microsoft Learn** | Documentação confiável de stack Microsoft — só se a stack for essa |

### Ainda não — mas com portão definido

**ZoomInfo, Apollo.io e Windsor.ai** são ferramentas de vendas B2B e mídia paga. Não são inadequadas por natureza: são inadequadas *antes* de existir o processo que elas aceleram (ICP escrito, outbound repetível, verba em mais de um canal). Cada uma tem um portão diferente — e Apollo tem free tier real, então o teste é barato quando a hora chegar. Detalhamento, preço verificado e as implicações de LGPD: [[prospeccao-e-midia-paga]].

### Sem função aqui

**PubMed** é literatura biomédica. **Mercado Libre Inmuebles** é busca de imóvel. **Spotify** não tem função de trabalho.

## Revisão periódica

Trate a lista de conectores como dependência de projeto: revise a cada poucos meses e remova o que não tem uso. Conector esquecido é acesso concedido que ninguém está observando.

## Ver também

- [Configuração e automação do Claude](configuracao.md)
- [Observabilidade](../../../engenharia/infra/observabilidade.md) — o conector do Sentry só faz sentido depois de decidir a plataforma
- Fontes: [Anthropic Connectors Directory FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq) · [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) · [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) · [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/develop/connect-remote-servers)
