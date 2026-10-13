#!/usr/bin/env bash
# Run before a commit: the two copies of the answering rules must match,
# the manifests must validate, the OpenCode build must be current, and the
# README must pass our own Vale rules.
set -euo pipefail
cd "$(dirname "$0")/.."
cmp -s rules/answering.md plugins/coldread-chat/rules/answering.md || {
  echo "rules/answering.md and plugins/coldread-chat/rules/answering.md differ: copy the edited one over the other"; exit 1; }
for p in . plugins/coldread plugins/coldread-chat; do claude plugin validate "$p" >/dev/null; done
python3 scripts/build-opencode.py --check
for s in install.sh scripts/*.sh plugins/coldread/skills/write/facts.sh plugins/coldread/skills/write/vale/lint.sh; do bash -n "$s"; done
if command -v vale >/dev/null 2>&1; then
  vale --config plugins/coldread/skills/write/vale/.vale.ini README.md
else
  echo "vale not found, README lint skipped"
fi
echo "all checks passed"
