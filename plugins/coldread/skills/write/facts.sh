#!/usr/bin/env bash
# List what a rewrite may have lost: every number and every inline code span
# in the original that appears in none of the new files.
#   facts.sh <original> <new file>...
# For a set of documents, give the others as more new files: a value that moved
# to one of them is not lost.
set -euo pipefail
export LC_ALL=C
[ "$#" -ge 2 ] || { echo "usage: $0 <original> <new file>..." >&2; exit 2; }
values() { cat -- "$@" | grep -oE '`[^`]+`|[0-9][0-9,.]*%?' | sed -E 's/[.,]+$//' | sort -u || true; }
ORIGINAL="$1"
shift
LOST="$(comm -23 <(values "$ORIGINAL") <(values "$@"))"
if [ -z "$LOST" ]; then
  echo "Every number and code span from $ORIGINAL is still there."
  exit 0
fi
echo "$(printf '%s\n' "$LOST" | wc -l | tr -d ' ') value(s) from $ORIGINAL appear in none of the new files:"
printf '%s\n' "$LOST" | sed 's/^/  /'
