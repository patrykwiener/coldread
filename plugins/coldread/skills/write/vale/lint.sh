#!/usr/bin/env bash
# Lint a text with the coldread Vale rules for its language.
#   lint.sh en|pl <file>...
# When the repository holds .coldread/vale/styles, its Project/ rules run too and
# the terms in config/vocabularies/Project/accept.txt count as known to the reader.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
usage() { echo "usage: $0 en|pl <file>..." >&2; exit 2; }
case "${1:-}" in
  en) BASE="$HERE/.vale.ini" ;;
  pl) BASE="$HERE/pl.ini" ;;
  *) usage ;;
esac
shift
[ "$#" -gt 0 ] || usage
command -v vale >/dev/null 2>&1 || { echo "vale not found, so the lint step is skipped. To add it: brew install vale, or see vale.sh" >&2; exit 3; }

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
PROJECT="$ROOT/.coldread/vale/styles"
[ -d "$PROJECT" ] || PROJECT=""
VOCAB=""
[ -n "$PROJECT" ] && [ -f "$PROJECT/config/vocabularies/Project/accept.txt" ] && VOCAB=1
RULES=""
[ -n "$PROJECT" ] && [ -d "$PROJECT/Project" ] && RULES=1

# Vale searches every StylesPath line, so the project's folder sits next to ours.
TMP="$(mktemp -d "${TMPDIR:-/tmp}/coldread-vale.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
awk -v styles="$HERE/styles" -v project="$PROJECT" -v vocab="$VOCAB" -v rules="$RULES" '
  /^StylesPath[[:space:]]*=/ {
    print "StylesPath = " styles
    if (project != "") print "StylesPath = " project
    if (vocab != "") print "Vocab = Project"
    next
  }
  /^BasedOnStyles[[:space:]]*=/ && rules != "" { print $0 ", Project"; next }
  { print }
' "$BASE" > "$TMP/.vale.ini"

vale --config "$TMP/.vale.ini" "$@"
