# coldread

coldread makes Claude Code and OpenCode write for a reader who was not in the session. Its writing skill drafts PR descriptions, review comments, design docs, explainers, handoff notes, prompts for a new agent session and Slack messages. Then a subagent that has seen neither the session nor your CLAUDE.md reads each draft and reports what it could not follow. Optional chat rules make everyday answers easier to follow.

## Claude writes from inside the session

Claude knows what its own working labels mean, and the reader does not. In the evals, Claude wrote a Slack message to a product manager from notes that mentioned `Phase A`, `option B` and `D3` without explaining them. Without coldread, at least one of these labels reached the manager in 9 of 9 attempts. With coldread, none did in 9 of 9. The writing skill cut them because the manager did not need them to decide, and it listed the cuts in its report.

## What you get

| Part | When it works | What it does |
|---|---|---|
| `/coldread:write` | starts on its own when you ask for a PR description, a review, a doc, a message or a prompt for a new session | Sets a brief, drafts, checks that every claim has a source and marks the ones it could not trace, lints the text with Vale, a linter for prose, then hands it to the cold reader. An ADR, a runbook or a design doc gets the sections its readers expect, and material meant for another document is named in the report instead of filling the text. |
| `coldread:cold-reader` | inside `/coldread:write` | A subagent with no session and no CLAUDE.md that reads the text once and reports what it could not follow. |
| `/coldread:reply` | when someone sent you a message you must answer | Says what the sender asks, resolves the names you may not know, then drafts your reply. |
| `/coldread:plain` | when an answer did not land | Names what failed, such as an unknown term, then explains again in new words. |
| Chat rules, in the optional `coldread-chat` plugin | every chat answer | Ten rules, such as: answer first, at most four points, explain every new term, ask questions that make sense on their own. |

## What the evals show

Both plugins ship with evals for `claude plugin eval`, which runs each case with and without the plugin in a clean session. Over four suite runs of 13 chat cases, answers passed 83% to 88% of the checks with the rules and 65% to 70% without them. In the latest suite run of 19 writing cases, 5 runs each, `/coldread:write` averaged 92% per case against 66% without it, measured before the fixes of 2026-10-14 listed in the results. Seven cases test document structure, such as a runbook that leaves design history out, and three of them were written before any run, to check the rules on text they were not tuned on. Bash was blocked on that computer, so the run measured the skill without Vale, the word count and the facts check. An earlier run with Vale on another computer passed 90% against 53% on 8 cases. Each text cost about three times as much as without the skill.

One person wrote the rules, the cases and the checks, and a model does the grading, so treat this as a first signal. [docs/results.md](docs/results.md) has every run and its limits, plus three blind comparisons of answers by that person.

## Install

The commands below are for Claude Code. In OpenCode, run the setup script from the [OpenCode](#opencode) section instead, and install Vale the same way. The three setup steps after this section apply to both tools.

```bash
claude plugin marketplace add patrykwiener/coldread
claude plugin install coldread@coldread        # /coldread:write, /coldread:reply, /coldread:plain and the cold reader
claude plugin install coldread-chat@coldread   # optional: the chat rules in every session
brew install vale                              # optional: the lint step; other systems: vale.sh
# later, to update: claude plugin update coldread@coldread
```

Without Vale, `/coldread:write` skips its lint step and says so. Then set coldread up for yourself and your projects in the three steps below.

## Set it up in three steps

The first two steps take a few minutes each. The third is for teams that want the lint step to know their project.

### 1. Tell Claude what you know, and how you write

This step gives coldread two notes about you. The About me note is for the chat rules from `coldread-chat`, which shape every answer: answer first, at most four points, every new term explained. They use the note to decide which terms are new to you, and without it Claude guesses. Add the note to `~/.claude/CLAUDE.md`, the file Claude Code loads in every session. In two to four sentences, say what Claude can leave unexplained, where you are a layman, and how you read most easily.

```markdown
## About me

Backend engineer: Python, PostgreSQL and AWS need no explanation. A layman in frontend work, construction and electrical installations. I read symbols such as ≤ and × faster than the words for them.
```

[`rules/CLAUDE.example.md`](rules/CLAUDE.example.md) has two more notes, for a product manager and for a data scientist. To check yours, ask Claude about a topic from your layman list and see whether the answer explains its trade terms.

If texts go out under your name, such as review comments or Slack messages, add a How I write note to the same file. It works without the chat rules: `/coldread:write` and `/coldread:reply` follow it for those texts, and it wins over the skill's own shape for a channel, such as the labels it puts on review comments. Measure rather than guess: ask Claude to read 20 to 40 of your own comments or messages and count their words, how they open and end, and the markup you never use.

```markdown
## How I write

Review comments: one or two plain sentences, about 30 words, never over 70. No headings, lists, bold or labels such as nit: or Fix:. Open on the concrete thing in backticks and what it does, and end on a question, such as "wdyt?". Slack messages: friendly and short, with the ask in the first sentence.
```

In OpenCode, both notes go into `~/.config/opencode/AGENTS.md`, which OpenCode loads in every session.

### 2. Tell `/coldread:write` who reads your project's texts

In each project where you write for other people, add a Writing section to the `CLAUDE.md` in the project's root. Say which language documents use, who reads each kind of text, and which names those readers already know. The skill takes the reader for the brief it shows before drafting from this section, so the cold reader does not ask about names your team uses daily. A team can set its review style here too. In that project, the team's style wins over the skill's default shape and over a personal How I write note.

```markdown
## Writing

Documents in English. PR descriptions: a backend developer on the team who knows the codebase, Jira and our deploy pipeline. Slack messages and release notes: the product manager, who knows the product but not the code. Readers know these names: Ledger, Payout API, the nightly sync.
```

[`rules/CLAUDE.project.example.md`](rules/CLAUDE.project.example.md) has versions for a Polish team and for an open-source library. To check the section, ask for a PR description: the brief that `/coldread:write` shows first should describe your reviewer.

Some projects keep `CLAUDE.md` out of git and share `AGENTS.md` instead. Then put the section in `AGENTS.md` and import that file from `CLAUDE.md` with the line `@AGENTS.md`. In OpenCode, the section goes into the project's `AGENTS.md`, which OpenCode reads directly.

### 3. Optional: share your project's terms and texts

A `.coldread/` folder in your project's repository tells `/coldread:write` what your readers know, in Claude Code and in OpenCode alike. Vale uses the first two files, and the skill reads the third. Each file is optional:

| File in `.coldread/` | What it does |
|---|---|
| `vale/styles/config/vocabularies/Project/accept.txt` | Lists terms your readers use daily, one per line, so Vale stops asking you to spell them out. |
| `vale/styles/Project/*.yml` | Adds your own Vale rules, such as the one way to spell a product name. |
| `examples-en.md` or `examples-pl.md` | Holds two or three of your team's English or Polish texts as style anchors, which the skill reads instead of its invented ones. |

This repository has an example folder with four sample terms, one rule for a product name and one invented English text. To copy it, run this in your project's root:

```bash
curl -fsSL https://github.com/patrykwiener/coldread/archive/refs/heads/main.tar.gz | tar -xz --strip-components=2 coldread-main/examples/.coldread
```

To keep the folder out of a shared repository, put it in a folder above the repository instead, for example next to its worktrees. `/coldread:write` uses the nearest `.coldread/`, starting at the repository's root.

Then replace the samples with your own: your terms in `accept.txt`, your product names in `vale/styles/Project/ProductNames.yml`, and your team's texts in `examples-en.md`. Do not list in `accept.txt` a name that one of your rules spells out: Vale accepts every spelling of a listed term, so the rule would never fire. Commit the folder to share it with the team. To check it, ask for a text that uses one of your terms: the Vale warnings that `/coldread:write` lists at the end should not name it.

## Use

`/coldread:write` starts on its own when you ask for a PR description, a doc or a message. To call it directly:

```
/coldread:write PR description for this branch, reader: the reviewer
/coldread:write rewrite docs/design.md for a backend developer who did not work on this
```

It first shows a brief: the reader, the one thing they must do, the points, where the text will be read and a word budget. The points set the length, about 80 words each, so correct a wrong or extra point when you see it. Where the text will be read sets the room: a review comment gets at most three sentences, and a Slack message or a commit body gets no Details section. When the reader must understand how something works, the skill defines each term with an example and walks one case from start to end.

The skill then drafts, fixes what the cold reader could not follow, and reports the cold reader's findings, the Vale warnings and the word count. It also quotes, side by side, what the brief says the reader must do and what the cold reader understood, and checks the cold reader's retelling against the points. When it rewrites or shortens a text, it lists every fact it removed, corrected or added, and every claim it could not trace to your notes, a check or the code. When it rewrites a file, a script lists every number and code span that left it. The skill never posts, sends or commits a text: you do.

Ask for a prompt for a new session, and the skill writes it for an agent that has your repository but not this session. The prompt holds your words verbatim, the decisions already made, the files to read, steps with stops for your approval, and the traps earlier sessions hit. A long document or a set of documents gets a reading path for each kind of reader. A document that asks its readers to choose gets options, a labelled recommendation with its reason, and the evidence that would change it.

When someone sent you a message you do not fully get, paste it after `/coldread:reply`, or just ask what they mean. The skill says what the sender asks, resolves the names you may not know or says who could, and drafts your reply in your voice.

When an answer did not land, type `/coldread:plain`, or say what you missed: `/coldread:plain what is a lease?`

## Settings

| Setting | Where | Default |
|---|---|---|
| Document language: `auto`, `en` or `pl` | `/plugin configure coldread@coldread` | `auto` writes in the language of your request |
| What you know well | the About me section in `~/.claude/CLAUDE.md`, step 1 of the setup | none, so Claude guesses |
| How you write texts that go out under your name | the How I write section in `~/.claude/CLAUDE.md`, step 1 of the setup | none, so the skill's own shapes apply |
| A project's document language and readers | a Writing section in that project's `CLAUDE.md`, step 2 of the setup | none |
| A project's own lint rules, the terms its readers know and its own style anchors | a `.coldread/` folder in that repository, step 3 of the setup | none |

Claude Code keeps plugin options in user settings only, so a project's exceptions go into its `CLAUDE.md`. Chat needs no language setting, because the rules tell Claude to reply in your language. A request can also name its own reader, as in the examples under Use.

## Run coldread from a clone, on one computer or several

Install from a clone when you want to edit the skill, its Vale checks or the chat rules, or to keep several computers on the same version. This replaces the install commands above. If you already installed from GitHub, run `claude plugin marketplace remove coldread` first.

```bash
git clone https://github.com/patrykwiener/coldread ~/Code/coldread && ~/Code/coldread/scripts/setup.sh
```

The script registers the clone as a local marketplace and installs the plugin from it. It sets up the chat rules with one import line in `~/.claude/CLAUDE.md` and backs that file up first. If `coldread-chat` is installed, the script skips that line, because both together load the rules twice. It also warns about copies of coldread that would load next to the plugin, such as one made by `install.sh`. To use another folder, clone there and run the script with `COLDREAD_DIR` set to that folder.

Claude Code loads a plugin from a local marketplace straight from the clone at every session start. So a `git pull` or an edit in the clone applies from the next session, or after `/reload-plugins`. Running the script again also works: it pulls, then checks the rest of the setup.

## Tune the Vale checks

The rules live in `plugins/coldread/skills/write/vale/`. The `.vale.ini` config lints English with the rules in `styles/Write/`. The `pl.ini` config lints Polish with the rules in `styles/WritePL/` and eight of the English ones, such as `SessionLabels`, which flags labels like `Phase A`. The skill runs both through `lint.sh`. For text in another language, `/coldread:write` skips linting and says so.

- **Acronyms**: add the ones every reader of yours knows to `exceptions` in `styles/Write/Acronyms.yml` or `styles/WritePL/Acronyms.yml`, in quotes. YAML reads an unquoted `NULL` or `YES` as a value, which silently disables the rule. Terms that only one project's readers know belong in that project's `.coldread/` folder, from step 3 of the setup.
- **A noisy rule**: change its `level:` to `suggestion`, which the skill treats as a hint rather than something to fix, or delete its file.

Your edits apply only when the plugin runs from your clone, as set up in the section above.

## Claude.ai and ChatGPT

Both limit the length of custom instructions, so [`rules/answering-nano.md`](rules/answering-nano.md) holds the same rules in under 1,000 characters. In Claude.ai, paste it with your About me section into "Instructions for Claude" under Settings, General. That field also covers Cowork. In ChatGPT, paste both into custom instructions.

## Without the plugin system

`./install.sh user` copies the plugin into `~/.claude/skills/coldread`. Claude Code 2.1.157 and later load such a folder as a plugin in every session, with the same commands and subagent. `./install.sh project /path/to/repo` does the same for one repository, so the team gets it through git.

## OpenCode

coldread also runs in OpenCode 2. Set it up from a clone:

```bash
git clone https://github.com/patrykwiener/coldread ~/Code/coldread && ~/Code/coldread/scripts/setup-opencode.sh
```

The script links the skills, the cold reader and the commands from the clone into `~/.config/opencode`. It also copies the chat rules from `coldread-chat`, the ten rules for every answer, into `~/.config/opencode/AGENTS.md` between two marker lines. Run it with `--no-chat` to leave `AGENTS.md` alone, or with `--uninstall` to remove everything it added. If you installed coldread's write skill, cold reader or `/write` command by hand before, the script moves those files to `~/.config/opencode/coldread-backups/`, because both copies would load. Files of yours with other contents stay. Then run `opencode reload`.

To update, run `git pull` in the clone, run the script again so the copy of the chat rules catches up, and run `opencode reload`. OpenCode does not notice a change behind a link until that reload.

| In Claude Code | In OpenCode |
|---|---|
| `/coldread:write`, `/coldread:reply`, `/coldread:plain` | `/coldread/write`, `/coldread/reply`, `/coldread/plain` |
| the `coldread:cold-reader` subagent | the `cold-reader` subagent |
| About me and How I write in `~/.claude/CLAUDE.md` | the same sections in `~/.config/opencode/AGENTS.md` |
| a Writing section in a project's `CLAUDE.md` | the same section in the project's `AGENTS.md` |

OpenCode 2 gives every agent the global and the project's `AGENTS.md`, so its cold reader may know names from those files that your reader does not. `/coldread/write` says so in its report. The evals run in Claude Code only.

For contributors: `scripts/build-opencode.py` generates the `opencode/` folder from `plugins/coldread`, and `scripts/check.sh` fails when that folder is out of date. The folder is in git, so users never run the build.

## Run the evals

```bash
claude plugin eval plugins/coldread-chat --allow-tools Write --judge-model sonnet
claude plugin eval plugins/coldread --allow-tools Write Bash --judge-model sonnet
```

The chat suite has 14 cases, seven of them in Polish, and the write suite has 11. Each case runs 3 times with the plugin and 3 times without it by default. Results go to `plugins/<name>/evals/results/`, which git ignores. Install Vale before you run the write suite, or the skill skips its lint step.

Sonnet judges because Haiku failed texts that met every condition of a grader, as [docs/results.md](docs/results.md) shows. As a judge, Sonnet costs about $0.04 per run. A condition that a pattern can check, such as a local path or a date in the text, uses a `regex` grader. That grader reads the file the case asks Claude to save, so no judge votes on it.

If every run stops at once with an error about the Docker credential store, the Bash sandbox refused to start because `~/.docker` holds a symbolic link. Run the write suite with `--allow-tools Write` only. It then measures the skill without its shell steps: the word count and the lint.

## Related work

- Anthropic's [doc-coauthoring](https://github.com/anthropics/skills) skill tests a document on a fresh model that sees only the document, the same idea as the cold read.
- [humanizer](https://github.com/blader/humanizer) removes word-level AI patterns and works well after `/coldread:write`.
- Two of the Vale checks, Parens and Semicolons, follow the [Google developer style guide](https://developers.google.com/style).

## License

MIT, see [LICENSE](LICENSE).
