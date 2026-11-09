---
name: heuristicas-nielsen
description: >
  Aplica e avalia as 10 Heurísticas de Usabilidade de Nielsen (visibilidade do
  status, correspondência com o mundo real, controle do usuário, consistência,
  prevenção de erros, reconhecimento vs memorização, flexibilidade, design
  minimalista, recuperação de erros, ajuda/documentação) em qualquer trabalho
  de front-end. Usar SEMPRE que estiver escrevendo, gerando ou editando
  interface de usuário — componentes React, telas, formulários, dashboards,
  fluxos de onboarding, mensagens de erro — não apenas quando o usuário disser
  "Nielsen" ou "heurísticas" explicitamente. Quando o pedido for avaliar,
  auditar, revisar ou dar feedback sobre uma interface já existente (código
  React/HTML/CSS ou uma imagem de protótipo/mockup/screenshot), seguir o modo
  de auditoria com relatório estruturado e severidade descrito abaixo, em vez
  do modo padrão silencioso.
---

# Heurísticas de Nielsen — usabilidade de front-end

Esta skill existe para uma coisa concreta: reduzir a distância entre "a interface funciona" e "a interface é fácil de usar sem explicação". As 10 heurísticas de Jakob Nielsen são o vocabulário padrão da indústria para isso — usadas tanto para desenhar quanto para auditar interfaces.

Um checklist de 10 princípios genéricos, sozinho, tem pouco valor prático: qualquer problema de UI pode ser encaixado em alguma heurística com esforço suficiente, e sem prioridade por impacto o resultado é uma lista de reclamações, não uma lista de decisões. O que torna isso acionável é a **escala de severidade** (seção abaixo) — sem ela, não aplique o modo auditoria de forma completa.

**Idioma:** toda comunicação (relatório de auditoria, explicações) é em português do Brasil, direta e simples, sem jargão desnecessário. Isso vale para a comunicação sobre a interface — não para rótulo/texto já existente na UI real sendo avaliada, que é citado como está.

Existem dois modos. Escolha um antes de agir.

## Modo padrão — escrever ou gerar UI (comportamento default)

Aplicar silenciosamente estas heurísticas ao gerar ou editar qualquer componente de interface, sem produzir relatório visível — o relatório completo é só para o modo auditoria. Para uma tarefa pequena (um formulário, um botão, um modal), isso significa simplesmente já nascer certo, não gerar um checklist.

1. **Visibilidade do status do sistema.** Toda ação assíncrona (submit, upload, chamada de API) precisa de feedback imediato: estado de loading, botão desabilitado durante a requisição, confirmação visível após sucesso, mensagem clara em caso de falha. Nunca deixar o usuário sem saber se um clique "pegou".
2. **Correspondência com o mundo real.** Rótulos, ícones e mensagens usam a linguagem do usuário final do produto (para o CRM: linguagem de lojista/vendedor, não termos técnicos como "payload", "webhook" ou "tenant" na UI). Ordem de campos e fluxo seguem a lógica do processo real do negócio, não a estrutura do banco de dados.
3. **Controle e liberdade do usuário.** Toda ação destrutiva ou de difícil reversão (excluir contato, cancelar pedido, sair de um fluxo no meio) tem confirmação ou desfazer. Modais e fluxos multi-etapa sempre têm saída clara (fechar, voltar, cancelar) — nunca um beco sem saída.
4. **Consistência e padronização.** Mesmo componente, mesmo nome, mesmo comportamento em todo o produto. Um botão de ação primária não muda de cor, posição ou rótulo entre telas equivalentes. Seguir convenções já estabelecidas no projeto (design tokens, nomenclatura de componentes) em vez de inventar padrão novo por tela.
5. **Prevenção de erros.** Preferir impedir o erro a explicar o erro depois: desabilitar submit até campos obrigatórios válidos, usar inputs com tipo/máscara correta (telefone, CPF/CNPJ, e-mail), validação em tempo real antes do submit, valores default seguros. Confirmação explícita antes de ações irreversíveis.
6. **Reconhecimento em vez de memorização.** Nunca exigir que o usuário lembre uma informação mostrada em outra tela ou passo anterior. Opções visíveis (menus, dropdowns) em vez de exigir digitação de algo que poderia ser selecionado. Contexto relevante (nome do contato, status do pedido) visível onde a decisão é tomada.
7. **Eficiência e flexibilidade de uso.** Atalhos de teclado, autocomplete, ações em lote e valores default inteligentes para quem já conhece o sistema — sem que isso compique a experiência de quem está usando pela primeira vez. Não forçar usuário avançado a repetir passos que poderiam ser acelerados.
8. **Design minimalista e estético.** Cada elemento na tela compete por atenção com os outros. Remover informação, badge, texto ou opção que não ajuda a decisão que o usuário está tomando naquele momento específico. Hierarquia visual clara: a ação principal da tela é a mais evidente.
9. **Ajudar a reconhecer, diagnosticar e recuperar de erros.** Mensagens de erro em linguagem simples, dizendo o que aconteceu e o que fazer a seguir — nunca código de erro cru ("Error 400") ou mensagem genérica ("algo deu errado") sem ação possível.
10. **Ajuda e documentação.** Quando o fluxo não é 100% autoexplicativo, oferecer ajuda contextual (tooltip, texto de apoio, link para documentação) no ponto exato da dúvida — não só em uma página de ajuda separada e genérica.

Se uma dessas regras conflitar com um padrão de design já estabelecido no projeto (design system, biblioteca de componentes em uso), siga o padrão do projeto e avise sobre a inconsistência em vez de criar um padrão paralelo.

## Modo auditoria — avaliação explícita de interface existente

Acionar quando o usuário pedir para avaliar, revisar, auditar ou dar feedback de usabilidade sobre uma interface que já existe — seja como **código** (componente React, HTML/CSS) ou como **imagem** (screenshot, protótipo, mockup, print do Claude Designer ou do Figma). Nos dois casos o processo é o mesmo; muda só a fonte da evidência.

### Processo

1. Se a entrada for uma imagem/protótipo e ainda não estiver visível no contexto, localizar e ver o arquivo antes de avaliar (nunca avaliar de memória ou suposição sobre como a tela provavelmente é).
2. Percorrer as 10 heurísticas uma a uma contra a evidência real (código ou imagem) — não pular nenhuma, mesmo que pareça não se aplicar (nesse caso, marcar severidade 0).
3. Para cada problema encontrado, identificar: qual heurística foi violada, onde exatamente (nome do componente/arquivo/linha, ou região da tela — "canto superior direito", "modal de confirmação"), e por que isso atrapalha o usuário na prática (não hipoteticamente).
4. Atribuir severidade usando a escala abaixo. Não inflar severidade para parecer mais completo, e não achatar tudo em "médio" para evitar julgamento — o valor da auditoria está exatamente em diferenciar o que é cosmético do que é bloqueante.
5. Ordenar o relatório final por severidade decrescente, não pela ordem das 10 heurísticas.

### Escala de severidade (Nielsen)

| Nível | Significado | Ação implícita |
|---|---|---|
| 0 | Não é um problema de usabilidade | Nenhuma |
| 1 | Problema cosmético | Corrigir só se sobrar tempo |
| 2 | Problema menor | Baixa prioridade |
| 3 | Problema maior | Alta prioridade, deve ser corrigido antes do lançamento da funcionalidade |
| 4 | Catástrofe de usabilidade | Bloqueante — corrigir antes de qualquer coisa |

### Formato de saída obrigatório (markdown)

```
## Diagnóstico rápido
## Problemas encontrados (ordenados por severidade)
| # | Heurística | Onde | Severidade | Por que atrapalha | Recomendação |
## Pontos que já funcionam bem
## Prioridades imediatas (severidade 3-4)
## Riscos ou dúvidas (o que não deu para avaliar com a evidência disponível)
```

A seção "Riscos ou dúvidas" é obrigatória sempre que a avaliação for feita só a partir de uma imagem estática (sem poder testar interações, estados de erro ou responsividade reais) — não apresentar uma auditoria estática como se fosse equivalente a um teste de uso real.

### Restrições rígidas do modo auditoria

- Não inventar problema que não tem evidência direta no código ou na imagem analisada.
- Não confundir heurísticas para parecer mais completo (ex.: classificar todo problema visual genérico como "design minimalista" quando na verdade é "consistência" ou "prevenção de erros" — a heurística errada leva à correção errada).
- Não propor redesign completo não pedido — o objetivo é diagnóstico, não uma segunda versão da tela, a menos que solicitado.
- Deixar explícito quando uma avaliação de imagem estática não permite confirmar heurísticas que dependem de comportamento (1, 3, 5, 9 costumam depender de interação real).

## Referência ampliada

O arquivo `references/heuristicas-detalhadas.md` tem exemplos adicionais por heurística (bons e ruins) voltados a interfaces de CRM/SaaS B2B, incluindo casos específicos de formulários multi-tenant, dashboards e fluxos de mensageria (WhatsApp/Instagram). Não precisa ser lido para aplicar o modo padrão no dia a dia — abrir quando for necessário fundamentar uma decisão específica em mais detalhe ou quando o modo auditoria pedir exemplos concretos de correção.
