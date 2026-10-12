#!/usr/bin/env bash
# Install the coldread plugin without a marketplace. Claude Code loads a folder
# under skills/ that holds .claude-plugin/plugin.json as a plugin.
#   ./install.sh user                    -> ${CLAUDE_CONFIG_DIR:-~/.claude}/skills/coldread  (only you, every project)
#   ./install.sh project /path/to/repo   -> /path/to/repo/.claude/skills/coldread           (shared with the team via git)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
case "${1:-}" in
  project) [ -n "${2:-}" ] || { echo "usage: $0 project /path/to/repo"; exit 1; }; BASE="$2/.claude" ;;
  user)    BASE="${CLAUDE_CONFIG_DIR:-$HOME/.claude}" ;;
  *)       echo "usage: $0 user | $0 project /path/to/repo"; exit 1 ;;
esac
TARGET="$BASE/skills/coldread"
# Back up outside skills/: a copy left inside it would load as a second plugin.
if [ -e "$TARGET" ]; then
  BACKUP="$BASE/coldread-backups/$(date +%Y%m%d-%H%M%S)"
  mkdir -p "$BACKUP"; mv "$TARGET" "$BACKUP/"; echo "moved the previous copy to $BACKUP"
fi
mkdir -p "$BASE/skills"
cp -R "$HERE/plugins/coldread" "$TARGET"
echo "installed into $TARGET"
# The pre-plugin version installed /write and cold-reader directly; both would still load.
for old in "$BASE/skills/write" "$BASE/agents/cold-reader.md" "$BASE"/skills/write.bak.*; do
  [ -e "$old" ] && echo "old version found, remove it so it does not load twice: $old"
done
command -v vale >/dev/null 2>&1 || echo "vale not found, so /coldread:write skips linting. To add it: brew install vale"
echo "a new session loads the plugin; in a running one, run /reload-plugins"
