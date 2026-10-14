#!/usr/bin/env bash
# Set coldread up for OpenCode 2 on this computer, or update it. Safe to run again.
#   scripts/setup-opencode.sh              pull the clone, link the skills, the cold reader and the commands, add the chat rules
#   scripts/setup-opencode.sh --no-chat    the same, but leave AGENTS.md alone
#   scripts/setup-opencode.sh --no-pull    the same, but set up the clone as it is
#   scripts/setup-opencode.sh --uninstall  remove what this script added
# The links point into this clone, so the pull updates the skills. The chat rules
# are a copy in AGENTS.md, which every run refreshes. Each run ends with opencode reload.
set -euo pipefail

CLONE="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG="${COLDREAD_OPENCODE_CONFIG:-${XDG_CONFIG_HOME:-$HOME/.config}/opencode}"
AGENTS="$CONFIG/AGENTS.md"
START='<!-- coldread chat rules: start'
END='<!-- coldread chat rules: end -->'
BACKUP="$CONFIG/coldread-backups/$(date +%Y%m%d-%H%M%S)"

MODE=install
CHAT=1
PULL=1
for arg in "$@"; do
  case "$arg" in
    --no-chat) CHAT=0 ;;
    --no-pull) PULL=0 ;;
    --uninstall) MODE=uninstall ;;
    *) echo "usage: $0 [--no-chat] [--no-pull] | --uninstall" >&2; exit 2 ;;
  esac
done

# Pull first, then carry on in the script the pull brought, so a skill added upstream gets its link.
if [ "$MODE" = install ] && [ "$PULL" = 1 ]; then
  if ! { [ "$0" -ef "$CLONE/scripts/setup-opencode.sh" ] && command -v git >/dev/null 2>&1 \
      && [ "$(git -C "$CLONE" rev-parse --show-toplevel 2>/dev/null)" -ef "$CLONE" ]; }; then
    echo "$CLONE is not a git clone of coldread, so nothing was pulled"
  elif ! git -C "$CLONE" rev-parse --verify --quiet '@{upstream}' >/dev/null; then
    echo "$CLONE has no upstream branch to pull from, so nothing was pulled"
  else
    before="$(git -C "$CLONE" rev-parse HEAD)"
    git -C "$CLONE" pull --ff-only --quiet || {
      echo "git pull --ff-only failed in $CLONE. To set up the version it holds, run $0 --no-pull" >&2
      exit 1
    }
    if [ "$(git -C "$CLONE" rev-parse HEAD)" != "$before" ]; then
      echo "pulled into $CLONE:"
      git --no-pager -C "$CLONE" log --oneline --no-decorate "$before..HEAD"
      exec "$BASH" "$CLONE/scripts/setup-opencode.sh" --no-pull "$@"
    fi
    echo "$CLONE is up to date"
  fi
fi

[ -d "$CLONE/opencode/skills" ] || { echo "$CLONE/opencode is missing: run scripts/build-opencode.py first" >&2; exit 1; }

# path in the config -> target in the clone
LINKS=(
  "skills/coldread-write:opencode/skills/coldread-write"
  "skills/coldread-plain:opencode/skills/coldread-plain"
  "skills/coldread-reply:opencode/skills/coldread-reply"
  "agents/cold-reader.md:opencode/agents/cold-reader.md"
  "commands/coldread:opencode/commands/coldread"
)

back_up() {
  mkdir -p "$BACKUP"
  mv "$1" "$BACKUP/"
  echo "moved $1 to $BACKUP/"
}

# Write AGENTS.md with the block between the markers replaced by the file in $1,
# or removed when $1 is empty, into the file in $2. A new block goes at the end.
put_block() {
  local block="$1" out="$2"
  awk -v start="$START" -v end="$END" -v blockfile="$block" '
    index($0, start) == 1 {
      if (blockfile != "" && !done) { while ((getline line < blockfile) > 0) print line; done = 1 }
      skip = 1; next
    }
    skip && index($0, end) == 1 { skip = 0; next }
    !skip { print }
    END {
      if (blockfile != "" && !done) {
        if (NR > 0) print ""
        while ((getline line < blockfile) > 0) print line
      }
    }' "$AGENTS" > "$out"
}

reload_opencode() {
  command -v opencode >/dev/null 2>&1 && opencode reload && return
  echo "Run opencode reload, or restart OpenCode, to load the changes."
}

markers_ok() {
  local starts ends
  starts="$(grep -c "^$START" "$AGENTS" || true)"
  ends="$(grep -cxF "$END" "$AGENTS" || true)"
  [ "$starts" = "$ends" ] && [ "$starts" -le 1 ]
}

if [ "$MODE" = uninstall ]; then
  for entry in "${LINKS[@]}"; do
    path="$CONFIG/${entry%%:*}"
    if [ -L "$path" ] && [ "$(readlink "$path")" = "$CLONE/${entry#*:}" ]; then
      rm "$path"
      echo "removed $path"
    fi
  done
  if [ -f "$AGENTS" ] && grep -q "^$START" "$AGENTS"; then
    markers_ok || { echo "$AGENTS has broken coldread markers; fix them by hand" >&2; exit 1; }
    cleaned="$(mktemp)"
    put_block "" "$cleaned"
    mv "$cleaned" "$AGENTS"
    grep -q '[^[:space:]]' "$AGENTS" || rm "$AGENTS"
    echo "removed the chat rules from $AGENTS"
  fi
  [ -d "$CONFIG/coldread-backups" ] && echo "Earlier copies this script moved aside are in $CONFIG/coldread-backups/"
  reload_opencode
  exit 0
fi

for entry in "${LINKS[@]}"; do
  path="$CONFIG/${entry%%:*}"
  target="$CLONE/${entry#*:}"
  mkdir -p "$(dirname "$path")"
  if [ -L "$path" ]; then
    [ "$(readlink "$path")" = "$target" ] && continue
    rm "$path"
  elif [ -e "$path" ]; then
    back_up "$path"
  fi
  ln -s "$target" "$path"
  echo "linked $path"
done

# A copy of the write skill or its /write command from before this setup would load next to it.
if [ -f "$CONFIG/skills/write/SKILL.md" ] && grep -q '^# Write for the reader who was not here' "$CONFIG/skills/write/SKILL.md"; then
  back_up "$CONFIG/skills/write"
fi
if [ -f "$CONFIG/commands/write.md" ] && grep -q 'Load the `write` skill' "$CONFIG/commands/write.md"; then
  back_up "$CONFIG/commands/write.md"
fi
# OpenCode also reads ~/.claude/skills, where install.sh puts its copy for Claude Code.
CLAUDE_COPY="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/coldread"
if [ -d "$CLAUDE_COPY/skills/write" ]; then
  echo "OpenCode also loads $CLAUDE_COPY, the copy install.sh made for Claude Code, as the skills write, plain and reply, with paths only Claude Code fills in. Use the coldread-* skills, or remove that copy if Claude Code has the plugin."
fi

if [ "$CHAT" = 1 ]; then
  block="$(mktemp)"
  {
    echo "$START. scripts/setup-opencode.sh writes this block from rules/answering.md in $CLONE; edit that file and run the script again. -->"
    echo "These rules cover answers to the user. A subagent's report to the agent that started it follows that agent's instructions instead."
    echo
    cat "$CLONE/rules/answering.md"
    echo "$END"
  } > "$block"
  [ -f "$AGENTS" ] || : > "$AGENTS"
  markers_ok || { rm -f "$block"; echo "$AGENTS has broken coldread markers; fix them by hand" >&2; exit 1; }
  updated="$(mktemp)"
  put_block "$block" "$updated"
  rm -f "$block"
  if cmp -s "$updated" "$AGENTS"; then
    rm -f "$updated"
    echo "the chat rules in $AGENTS are up to date"
  else
    if [ -s "$AGENTS" ]; then
      mkdir -p "$BACKUP"
      cp "$AGENTS" "$BACKUP/AGENTS.md"
      echo "backed up $AGENTS to $BACKUP/"
    fi
    mv "$updated" "$AGENTS"
    echo "wrote the chat rules into $AGENTS"
  fi
  grep -q '^## About me' "$AGENTS" || echo "Add an About me note to $AGENTS: what you know well and where you are a layman. Example: $CLONE/rules/CLAUDE.example.md"
  grep -q '^## How I write' "$AGENTS" || echo "Optional: a How I write note in $AGENTS for texts that go out under your name. Example: $CLONE/rules/CLAUDE.example.md"
fi

command -v vale >/dev/null 2>&1 || echo "Optional: brew install vale, for the lint step of the write skill in English and Polish"
reload_opencode
echo "Done. To update later, run this script again. The commands are /coldread/write, /coldread/reply and /coldread/plain."
