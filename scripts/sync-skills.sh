#!/usr/bin/env bash
#
# Liga as skills deste vault ao diretório de skills do Claude, por symlink.
# Editar a skill no vault passa a refletir direto no Claude, sem re-sincronizar.
#
# Uso:
#   ./scripts/sync-skills.sh            # simulação: mostra o que faria (padrão)
#   ./scripts/sync-skills.sh --apply    # cria/atualiza os links
#
# Nunca remove diretório real: se já existir uma skill de mesmo nome que não seja
# link para este vault, o script avisa e pula, deixando a decisão para você.

set -euo pipefail

DIRETORIO_VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIRETORIO_ORIGEM="$DIRETORIO_VAULT/ia/skills"
DIRETORIO_DESTINO="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

APLICAR=false
[[ "${1:-}" == "--apply" ]] && APLICAR=true

if [[ ! -d "$DIRETORIO_ORIGEM" ]]; then
  echo "erro: não encontrei $DIRETORIO_ORIGEM" >&2
  exit 1
fi

$APLICAR || echo "== SIMULAÇÃO (use --apply para valer) =="
echo "origem:  $DIRETORIO_ORIGEM"
echo "destino: $DIRETORIO_DESTINO"
echo

$APLICAR && mkdir -p "$DIRETORIO_DESTINO"

criadas=0
puladas=0
conflitos=0

for caminho_skill in "$DIRETORIO_ORIGEM"/*/; do
  nome_skill="$(basename "$caminho_skill")"
  destino="$DIRETORIO_DESTINO/$nome_skill"

  if [[ ! -f "$caminho_skill/SKILL.md" ]]; then
    echo "!! $nome_skill — sem SKILL.md, pulando"
    ((conflitos++)) || true
    continue
  fi

  if [[ -L "$destino" ]]; then
    alvo_atual="$(readlink "$destino")"
    if [[ "$alvo_atual" == "${caminho_skill%/}" ]]; then
      echo "== $nome_skill — já ligado"
      ((puladas++)) || true
      continue
    fi
    echo "~~ $nome_skill — link aponta para outro lugar ($alvo_atual), refazendo"
    $APLICAR && ln -sfn "${caminho_skill%/}" "$destino"
    ((criadas++)) || true
    continue
  fi

  if [[ -e "$destino" ]]; then
    echo "!! $nome_skill — já existe um diretório real em $destino. Não vou tocar."
    echo "   Resolva à mão: mova ou apague o diretório e rode de novo."
    ((conflitos++)) || true
    continue
  fi

  echo "++ $nome_skill — criar link"
  $APLICAR && ln -s "${caminho_skill%/}" "$destino"
  ((criadas++)) || true
done

echo
echo "resumo: $criadas a criar/atualizar · $puladas já ok · $conflitos com conflito"
$APLICAR || echo "nada foi alterado. rode com --apply para aplicar."
