#!/usr/bin/env bash
# Set up coldread on this computer, or update it. Safe to run again.
# It clones or updates the repo, registers the clone as a local marketplace,
# installs the plugin, and imports the chat rules in your user CLAUDE.md.
set -euo pipefail

DIR="${COLDREAD_DIR:-$HOME/Code/coldread}"
REPO_URL="${COLDREAD_REPO:-https://github.com/patrykwiener/coldread}"
CONFIG="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
CLAUDE_MD="$CONFIG/CLAUDE.md"

command -v git >/dev/null || { echo "git is missing" >&2; exit 1; }
command -v claude >/dev/null || { echo "Claude Code (claude) is missing" >&2; exit 1; }

if [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull --ff-only
else
  git clone "$REPO_URL" "$DIR" || {
    echo "Clone failed. If the repo is private, run: gh auth login && gh auth setup-git" >&2
    exit 1
  }
fi

# The marketplace lists the plugin by a relative path, so Claude Code loads it
# straight from the clone at every session start, and the pull above already
# updates it. The update below only matters on old Claude Code versions that
# ran such a plugin from a cached copy.
claude plugin marketplace add "$DIR"
claude plugin install coldread@coldread
claude plugin update coldread@coldread

# A copy installed before the plugin, or by install.sh, would load next to it,
# and an edit made there would never reach the repo.
for old in "$CONFIG/skills/write" "$CONFIG/agents/cold-reader.md" "$CONFIG/skills/coldread" "$CONFIG"/skills/write.bak.*; do
  [ -e "$old" ] && echo "Older copy of coldread found. Remove it, or it loads twice: $old"
done

case "$DIR" in
  "$HOME"/*) RULES="~${DIR#"$HOME"}/rules/answering.md" ;;
  *) RULES="$DIR/rules/answering.md" ;;
esac
IMPORT="@$RULES"

PLUGINS="$(claude plugin list 2>/dev/null || true)"
case "$PLUGINS" in
  *coldread-chat@coldread*)
    echo "coldread-chat adds the rules, so $CLAUDE_MD gets no import line" ;;
  *)
    mkdir -p "$(dirname "$CLAUDE_MD")"
    touch "$CLAUDE_MD"
    if grep -qF -- "$IMPORT" "$CLAUDE_MD"; then
      echo "$CLAUDE_MD already imports the rules"
    elif [ -s "$CLAUDE_MD" ]; then
      BACKUP="$CLAUDE_MD.bak.$(date +%Y%m%d%H%M%S)"
      cp "$CLAUDE_MD" "$BACKUP"
      { printf '%s\n\n' "$IMPORT"; cat "$BACKUP"; } > "$CLAUDE_MD"
      echo "Added $IMPORT to $CLAUDE_MD (backup: $BACKUP)"
    else
      printf '%s\n' "$IMPORT" > "$CLAUDE_MD"
      echo "Created $CLAUDE_MD with $IMPORT"
    fi ;;
esac

if ! grep -q '^## About me' "$CLAUDE_MD" 2>/dev/null; then
  echo "Add an About me note to $CLAUDE_MD: what you know well and where you are a layman."
  echo "Example: $DIR/rules/CLAUDE.example.md"
fi

command -v vale >/dev/null || echo "Optional: brew install vale, for the lint step of /coldread:write in English and Polish"

echo "Done. Start a new Claude Code session, or run /reload-plugins in an open one."
