# Heurísticas de Nielsen — exemplos detalhados para CRM/SaaS B2B

Exemplos concretos por heurística, com foco em telas de CRM multi-tenant, dashboards e fluxos de mensageria (WhatsApp/Instagram/TikTok/Nuvemshop) — o tipo de interface mais provável neste contexto de trabalho.

## 1. Visibilidade do status do sistema

- **Ruim:** botão "Enviar mensagem" que não muda de estado enquanto a chamada à Meta Cloud API está em andamento — o lojista clica de novo e envia a mensagem duplicada.
- **Bom:** botão vira estado de loading, fica desabilitado, e some/mostra confirmação (✓ enviado / ✗ falhou) assim que a resposta chega.
- Caso específico de integração assíncrona (webhook, fila): se a ação depende de confirmação de um sistema externo que pode demorar, mostrar estado intermediário explícito ("processando", "aguardando confirmação do WhatsApp") em vez de deixar a UI parada sem explicação.

## 2. Correspondência com o mundo real

- **Ruim:** tela de configuração mostrando "tenant_id", "webhook_url", "canal ativo (bool)" para o dono da loja de roupas configurar.
- **Bom:** "Nome da sua loja", "Link de conexão com o WhatsApp", "Canal ligado/desligado" com toggle.
- Ordem de campos em um formulário de novo contato deve seguir a ordem que um vendedor pensaria (nome → telefone/canal de contato → o que ele comprou) e não a ordem das colunas no banco.

## 3. Controle e liberdade do usuário

- **Ruim:** excluir um contato duplicado sem confirmação, sem desfazer, e sem aviso de que histórico de conversa junto será perdido.
- **Bom:** confirmação explícita citando a consequência ("Isso vai apagar o contato e as 12 mensagens trocadas com ele. Não pode ser desfeito.") ou, melhor ainda, soft-delete com opção de desfazer por alguns segundos/minutos.
- Fluxo de configuração de canal em várias etapas (conectar Meta Cloud API) precisa permitir voltar ou cancelar no meio sem perder o progresso das etapas já validadas.

## 4. Consistência e padronização

- **Ruim:** o botão de ação primária é azul e fica à direita na tela de contatos, mas é verde e fica à esquerda na tela de negociações/funil.
- **Bom:** mesmo componente de botão primário, mesma posição, em todas as telas do produto — reaproveitando o mesmo componente de UI, não recriando por tela.
- Terminologia consistente: se uma tela chama de "negociação", outra não deve chamar a mesma entidade de "oportunidade" ou "deal".

## 5. Prevenção de erros

- **Ruim:** formulário de cadastro de contato permite salvar telefone sem DDD ou em formato livre, gerando falha silenciosa no envio de mensagem depois.
- **Bom:** input de telefone com máscara/validação de formato brasileiro no momento da digitação, e submit desabilitado enquanto o campo obrigatório estiver inválido.
- Ação de "desconectar canal" (WhatsApp/Instagram) deveria ter confirmação explícita, já que interrompe o recebimento de mensagens dos clientes do lojista.

## 6. Reconhecimento em vez de memorização

- **Ruim:** usuário precisa lembrar em qual etapa do funil um contato estava ao abrir a conversa dele, porque essa informação só aparece na tela de funil/kanban.
- **Bom:** status/etapa do contato visível também dentro da própria conversa, sem precisar navegar de volta.
- Em telas de deduplicação manual de contatos: mostrar lado a lado os dois registros candidatos a duplicata, não pedir para o usuário guardar de memória os dados de um enquanto olha o outro.

## 7. Eficiência e flexibilidade de uso

- **Ruim:** para marcar 10 contatos como "cliente inativo", o lojista precisa abrir um por um.
- **Bom:** seleção múltipla + ação em lote, mantendo a opção de fazer um por um para quem prefere.
- Atalho de teclado para enviar mensagem (Enter/Cmd+Enter) sem obrigar clique no botão, para quem já conhece o fluxo.

## 8. Design minimalista e estético

- **Ruim:** card de contato mostrando 8 badges e métricas ao mesmo tempo (canal, tags, score, última interação, tenant, criado em, etc.) competindo por atenção.
- **Bom:** mostrar só o que ajuda a decisão imediata (nome, canal, última mensagem) e deixar o resto disponível ao expandir/clicar.

## 9. Ajudar a reconhecer, diagnosticar e recuperar de erros

- **Ruim:** "Erro 400 ao enviar mensagem" sem explicação.
- **Bom:** "Não foi possível enviar: o número do cliente não está mais ativo no WhatsApp. Verifique o número ou marque o contato como inativo." — descreve o problema e a próxima ação possível.
- Erros de integração (Meta Cloud API, Nuvemshop) devem ser traduzidos para linguagem do lojista, nunca repassar a mensagem técnica crua da API externa.

## 10. Ajuda e documentação

- **Ruim:** único lugar de ajuda é uma página de FAQ genérica, sem relação com a tela específica onde o usuário está com dúvida.
- **Bom:** tooltip contextual no campo "Link de conexão com WhatsApp" explicando o que fazer, no momento exato da configuração — complementado por uma central de ajuda para casos mais raros.

---

## Nota sobre avaliação de imagem estática vs. código

Screenshots e protótipos (Claude Designer, Figma) permitem avaliar bem as heurísticas 2, 4, 6, 8 e 10 (linguagem, consistência visual, reconhecimento, minimalismo, presença de ajuda contextual), porque são propriedades visíveis na tela parada.

As heurísticas 1, 3, 5, 7 e 9 dependem de comportamento (o que acontece durante e depois de uma ação) e só podem ser avaliadas com confiança a partir de código, de um protótipo interativo, ou de uso real — uma imagem estática no máximo permite levantar hipótese, nunca confirmar. Sinalizar isso explicitamente na seção "Riscos ou dúvidas" do relatório de auditoria.
