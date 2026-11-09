#!/usr/bin/env bash
#
# Um comando para manter o vault em ordem depois de qualquer mudança:
#   1. regenera os índices dos README e o catálogo do radar
#   2. valida links, nomes, frontmatter e fichas
#   3. liga as skills de agentes/skills/ ao Claude (~/.claude/skills)
#
# Uso:  ./scripts/atualizar.sh
#
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

echo "→ 1/3 atualizando índices e catálogo do radar"
python3 scripts/gerar-indices.py
indices=$?

echo
echo "→ 2/3 validando o vault"
python3 scripts/validar-vault.py
validacao=$?

echo
echo "→ 3/3 ligando as skills ao Claude"
./scripts/sync-skills.sh --apply | tail -1

echo
if [[ $indices -ne 0 || $validacao -ne 0 ]]; then
  echo "⚠️  há problemas acima para corrigir."
  exit 1
fi
echo "✅ vault em ordem"
