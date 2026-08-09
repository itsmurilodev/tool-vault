---
name: decisao-arquitetural
description: >
  Ajuda a tomar e registrar decisões técnicas/arquiteturais não-triviais usando
  o formato de Architecture Decision Record (ADR): esclarecer restrições reais
  antes de propor solução, apresentar 2-3 opções com trade-offs em vez de uma
  única opinião, e documentar contexto/decisão/consequências. Usar SEMPRE que
  uma escolha estrutural difícil de reverter estiver em jogo — banco de dados,
  estratégia de multi-tenancy, síncrono vs assíncrono, limite entre
  serviços/módulos, integração com sistema externo, escolha de
  framework/biblioteca com efeito de longo prazo, modelagem de dado com
  implicação estrutural — mesmo que o usuário não diga "arquitetura" ou "ADR"
  explicitamente (ex: "devo usar X ou Y pra isso", "como estruturar esse
  serviço", "isso deveria rodar em fila ou direto"). Aplicar o portão de
  decisão abaixo antes: nem toda escolha técnica precisa virar ADR.
---

# Decisão arquitetural (ADR)

O objetivo aqui é capturar o *porquê* de uma decisão técnica difícil de reverter — não decidir ou guardar a arquitetura atual de um projeto específico. A arquitetura real do CRM, do Hamidi ou de qualquer outro projeto vive no repositório/Notion do projeto, não dentro desta skill. Esta skill é método, não fato de projeto — se algum dia esta skill passar a citar detalhes específicos de um sistema em vez de processo, ela virou documentação de projeto disfarçada de skill, e vai ficar desatualizada no primeiro pivot.

Para princípios de como o código em si deve ser escrito (nomes, tamanho de função, duplicação), usar a skill `clean-code` — não duplicar essa regra aqui. Esta skill é sobre decisão estrutural (o quê e por quê), não sobre estilo de código (como).

**Idioma:** toda comunicação (perguntas, opções, ADR gerada) é em português do Brasil, direta e simples, sem jargão desnecessário.

## Portão — vale a pena virar ADR?

Nem toda escolha técnica precisa de registro formal. Escrever uma ADR quando pelo menos um destes for verdade:

- A decisão é difícil ou cara de reverter depois.
- Afeta mais de um serviço, módulo ou (no caso do CRM) mais de um tenant.
- Envolve trade-off real entre opções, não uma escolha óbvia.
- A mesma pergunta já foi debatida mais de uma vez em conversas diferentes.
- Veio sinalizada como **"provável ADR"** pela skill `levantamento-requisitos` (requisito não-funcional pesado o suficiente para virar decisão estrutural).

Se nenhum critério se aplica: decidir direto na conversa, com uma frase de justificativa se fizer sentido, e seguir. Não gerar documento para escolha trivial só para parecer rigoroso.

## Processo

### 1. Esclarecer restrições antes de propor solução

Nunca recomendar uma solução como primeira resposta a uma decisão estrutural. Perguntar (objetivamente, não em bateria longa):

- Escala esperada real (não hipotética) — quantos tenants, volume de mensagens, etc.
- Prazo e quem vai manter isso depois (só você, ou vai entrar mais gente no time/cliente).
- Restrição de orçamento ou stack já em uso que não pode ser ignorada.
- Se a decisão veio de um requisito sinalizado pela skill de requisitos, puxar o requisito não-funcional já levantado em vez de reperguntar do zero.

### 2. Apresentar opções reais, não uma opinião disfarçada

Trazer 2-3 alternativas genuínas com trade-offs explícitos (custo, complexidade, tempo de implementação, risco, reversibilidade) — mesmo quando uma opção parece claramente melhor. Uma recomendação sem alternativa ao lado não deixa o usuário avaliar se concorda com os critérios usados, só com a conclusão.

### 3. Recomendar com raciocínio explícito

Dar uma recomendação clara, mas identificada como recomendação — não como fato decidido. A decisão final é do usuário; o valor da skill é garantir que ele decida informado, não substituir a decisão dele.

### 4. Registrar em formato ADR

Uma ADR = uma decisão. Se a conversa envolveu mais de uma decisão estrutural (ex.: banco de dados **e** estratégia de fila), gerar uma ADR para cada, nunca uma só cobrindo as duas.

```
# NNNN - Título curto da decisão (verbo + objeto, ex: "Usar Postgres com coluna tenant_id para isolamento")

Status: proposed | accepted | deprecated | superseded

## Contexto
O problema/restrição que forçou essa decisão a ser tomada agora. Situação do projeto, prioridades de negócio relevantes.

## Decisão
O que foi decidido, em uma frase direta ("Vamos usar X em vez de Y").

## Alternativas consideradas
Cada alternativa real avaliada, com o principal trade-off de cada uma.

## Consequências
O que essa decisão implica daqui pra frente — positivo e negativo. Descrever em termos de mudança de comportamento ("a partir de agora, X passa a Y"), não só listar prós/contras soltos.
```

### Convenções

- Nome de arquivo: `NNNN-titulo-curto.md`, numeração sequencial.
- Guardar no repositório do projeto (ex.: `docs/adr/`) ou no Notion do projeto — nunca dentro desta skill.
- Uma ADR aceita não é editada depois. Se a decisão mudar, criar uma nova ADR com status `superseded` referenciando a antiga, e atualizar o status da antiga para `superseded` com link para a nova. Isso preserva o histórico de por que algo mudou, em vez de apagar o registro de uma decisão que fez sentido no contexto da época.

## Restrições

- Não pular a etapa 1 (restrições reais) e ir direto pra uma recomendação — decisão estrutural sem entender escala/prazo/manutenção real é opinião, não análise.
- Não empacotar mais de uma decisão numa ADR só.
- Não propor abstração, camada ou complexidade que o requisito atual não justifica (mesmo espírito de "sem abstração especulativa" do `clean-code`, aplicado em nível estrutural: não desenhar para uma escala hipotética sem evidência de que ela vai ocorrer).
- Não guardar decisão específica de um projeto dentro do corpo desta skill — o entregável de cada uso é uma ADR nova no projeto certo, não uma edição neste arquivo.
- Quando a origem da decisão for um requisito sinalizado como "provável ADR", referenciar isso explicitamente no Contexto da ADR gerada, para manter rastreabilidade entre requisito e decisão.
