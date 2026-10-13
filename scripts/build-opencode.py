#!/usr/bin/env python3
"""Generate the OpenCode version of coldread in opencode/ from plugins/coldread.

  scripts/build-opencode.py          write opencode/
  scripts/build-opencode.py --check  exit 1 when opencode/ differs from a fresh build

The skills keep one source: the Claude Code plugin. This script copies each
SKILL.md with the few lines that only Claude Code understands rewritten, links
the files the skills read from the plugin, and writes the cold reader and the
commands in OpenCode's own format. It fails when a line it rewrites has
changed in the source, so a change to the plugin cannot slip past it.
"""

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "coldread"
OUT = ROOT / "opencode"


class BuildError(Exception):
    pass


def replace(text, old, new, count, where):
    found = text.count(old)
    if found != count:
        raise BuildError(f"{where}: expected {count} of {old!r}, found {found}")
    return text.replace(old, new)


def split_frontmatter(text, where):
    if not text.startswith("---\n"):
        raise BuildError(f"{where}: no frontmatter")
    end = text.index("\n---\n", 4)
    return text[4:end], text[end + 5:]


ARGUMENTS_LINE = "What the user said: $ARGUMENTS"
ARGUMENTS_OPENCODE = "What the user said: the text that came with the command that loaded this skill, if any."


def write_skill(text):
    where = "skills/write/SKILL.md"
    text = replace(text, "\nname: write\n", "\nname: coldread-write\n", 1, where)
    text = replace(
        text,
        "Everything below exists to close that gap, and the cold read checks that it closed.\n",
        "Everything below exists to close that gap, and the cold read checks that it closed.\n\n"
        "In the commands below, `<base directory>` stands for the base directory that OpenCode "
        "prints with this skill. Use it verbatim; do not guess the path.\n",
        1,
        where,
    )
    text = replace(text, "`${user_config.doc_language}`", "`auto`", 1, where)
    text = replace(text, '"${CLAUDE_PLUGIN_ROOT}/skills/write/facts.sh"', '"<base directory>/facts.sh"', 1, where)
    text = replace(text, '"${CLAUDE_PLUGIN_ROOT}/skills/write/vale/lint.sh"', '"<base directory>/vale/lint.sh"', 2, where)
    text = replace(text, "copy it to the scratchpad:", "copy it to the system temporary folder:", 1, where)
    text = replace(text, "(use the scratchpad)", "(use the system temporary folder)", 1, where)
    text = replace(
        text,
        "- Use the `coldread:cold-reader` subagent. It starts without any CLAUDE.md, so it knows only what the "
        "reader line tells it. If it is not available, use a general-purpose subagent and tell it to read "
        "`${CLAUDE_PLUGIN_ROOT}/agents/cold-reader.md` first and follow it exactly. That reader still loads "
        "CLAUDE.md, so say so in the report.\n",
        "- Use the `cold-reader` subagent. OpenCode gives it the global and the project's AGENTS.md, so it may "
        "know names the real reader does not: say in the report that the reader saw them. If the subagent is not "
        "available, use the `general` subagent and tell it to read `agents/cold-reader.md` in the OpenCode "
        "config folder, `~/.config/opencode/`, first and follow it exactly.\n",
        1,
        where,
    )
    text = replace(
        text,
        "- Never run the reader as a fork: a fork inherits this whole session, which is exactly what the reader "
        "must not have.\n",
        "",
        1,
        where,
    )
    if "${" in text or "coldread:" in text:
        raise BuildError(f"{where}: a Claude Code reference is left: rewrite it in build-opencode.py")
    return text


def plain_skill(text):
    where = "skills/plain/SKILL.md"
    text = replace(text, "\nname: plain\n", "\nname: coldread-plain\n", 1, where)
    return replace(text, ARGUMENTS_LINE, ARGUMENTS_OPENCODE, 1, where)


def reply_skill(text):
    where = "skills/reply/SKILL.md"
    text = replace(text, "\nname: reply\n", "\nname: coldread-reply\n", 1, where)
    text = replace(text, ARGUMENTS_LINE, ARGUMENTS_OPENCODE, 1, where)
    text = replace(text, "the `coldread:write` skill", "the `coldread-write` skill", 1, where)
    if "coldread:" in text:
        raise BuildError(f"{where}: a Claude Code reference is left: rewrite it in build-opencode.py")
    return text


def cold_reader(text):
    where = "agents/cold-reader.md"
    frontmatter, body = split_frontmatter(text, where)
    descriptions = [line for line in frontmatter.splitlines() if line.startswith("description: ")]
    if len(descriptions) != 1:
        raise BuildError(f"{where}: expected one description line")
    return (
        "---\n"
        f"{descriptions[0]}\n"
        "mode: subagent\n"
        "permissions:\n"
        '  - action: "*"\n'
        '    resource: "*"\n'
        "    effect: deny\n"
        "  - action: read\n"
        '    resource: "*"\n'
        "    effect: allow\n"
        "  - action: external_directory\n"
        '    resource: "*"\n'
        "    effect: allow\n"
        "---\n" + body
    )


COMMANDS = {
    "write.md": """---
description: Write or rewrite a text that a person or another agent will read, with the coldread-write skill. Give a file to rewrite or a description of the text, and its reader if you know it.
---

Load the `coldread-write` skill with the skill tool and follow all its steps for:

$ARGUMENTS

If that names a file, rewrite that file. If it describes a text, draft it in a new file in the system temporary folder. If it is empty, ask which text to write or rewrite, and who will read it.
""",
    "reply.md": """---
description: Make sense of a message someone sent you and draft your reply, with the coldread-reply skill. Paste the message after the command.
---

Load the `coldread-reply` skill with the skill tool and follow it for this message and request:

$ARGUMENTS
""",
    "plain.md": """---
description: Explain your last answer again after naming why it was hard to follow, with the coldread-plain skill. Optionally say what you did not get.
---

Load the `coldread-plain` skill with the skill tool and follow it. What I did not get, if I said it: $ARGUMENTS
""",
}

README = """# coldread for OpenCode

Generated by `scripts/build-opencode.py` from `plugins/coldread`; edit the plugin, then run the build. `scripts/setup-opencode.sh` links these folders into your OpenCode config. The README at the root of the repository describes the setup.
"""

# Files the write skill reads, linked from the plugin so that they exist once.
WRITE_LINKS = ["channels", "vale", "facts.sh", "examples-en.md", "examples-pl.md"]


def build(out):
    skills = out / "skills"
    write_dir = skills / "coldread-write"
    write_dir.mkdir(parents=True)
    (write_dir / "SKILL.md").write_text(write_skill((PLUGIN / "skills/write/SKILL.md").read_text()))
    for name in WRITE_LINKS:
        source = PLUGIN / "skills/write" / name
        if not source.exists():
            raise BuildError(f"skills/write/{name} does not exist")
        os.symlink(os.path.relpath(source, OUT / "skills" / "coldread-write"), write_dir / name)
    for name, transform in (("plain", plain_skill), ("reply", reply_skill)):
        folder = skills / f"coldread-{name}"
        folder.mkdir()
        (folder / "SKILL.md").write_text(transform((PLUGIN / f"skills/{name}/SKILL.md").read_text()))
    (out / "agents").mkdir()
    (out / "agents/cold-reader.md").write_text(cold_reader((PLUGIN / "agents/cold-reader.md").read_text()))
    commands = out / "commands/coldread"
    commands.mkdir(parents=True)
    for name, text in COMMANDS.items():
        (commands / name).write_text(text)
    (out / "README.md").write_text(README)


def snapshot(root):
    entries = {}
    for folder, dirs, files in os.walk(root):
        for name in dirs + files:
            path = Path(folder) / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                entries[relative] = ("link", os.readlink(path))
            elif path.is_file():
                entries[relative] = ("file", path.read_bytes())
        dirs[:] = [d for d in dirs if not (Path(folder) / d).is_symlink()]
    return entries


def main():
    parser = argparse.ArgumentParser(description="Generate opencode/ from plugins/coldread.")
    parser.add_argument("--check", action="store_true", help="exit 1 when opencode/ is out of date")
    check = parser.parse_args().check
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp) / "opencode"
        try:
            build(fresh)
        except BuildError as error:
            sys.exit(f"build-opencode: {error}")
        if check:
            expected, actual = snapshot(fresh), snapshot(OUT) if OUT.exists() else {}
            stale = sorted(k for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k))
            if stale:
                print("opencode/ is out of date; run scripts/build-opencode.py. Differs: " + ", ".join(stale))
                sys.exit(1)
            return
        if OUT.exists():
            shutil.rmtree(OUT)
        shutil.copytree(fresh, OUT, symlinks=True)
    print(f"wrote {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
