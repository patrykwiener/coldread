# coldread

coldread makes Claude Code write for a reader who was not in the session. Its writing skill drafts PR descriptions, review comments, design docs, explainers, handoff notes and Slack messages. Then a subagent that has seen neither the session nor your CLAUDE.md reads each draft and reports what it could not follow. Optional chat rules make everyday answers easier to follow.

## Claude writes from inside the session

Claude knows what its own working labels mean, and the reader does not. In the evals, Claude wrote a Slack message to a product manager from notes that mentioned `Phase A`, `option B` and `D3` without explaining them. Without coldread, at least one of these labels reached the manager in 9 of 9 attempts. With coldread, none did in 9 of 9. The writing skill cut them because the manager did not need them to decide, and it listed the cuts in its report.

## What you get

| Part | When it works | What it does |
|---|---|---|
| `/coldread:write` | starts on its own when you ask for a PR description, a review, a doc or a message | Sets a brief, drafts, checks that every claim has a source, lints the text with Vale, a linter for prose, then hands it to the cold reader. |
| `coldread:cold-reader` | inside `/coldread:write` | A subagent with no session and no CLAUDE.md that reads the text once and reports what it could not follow. |
| `/coldread:plain` | when an answer did not land | Names what failed, such as an unknown term, then explains again in new words. |
| Chat rules, in the optional `coldread-chat` plugin | every chat answer | Nine rules, such as: answer first, at most four points, explain every new term. |

## Install

```bash
claude plugin marketplace add patrykwiener/coldread
claude plugin install coldread@coldread        # /coldread:write, /coldread:plain and the cold reader
claude plugin install coldread-chat@coldread   # optional: the chat rules in every session
brew install vale                              # optional: the lint step; other systems: vale.sh
# later, to update: claude plugin update coldread@coldread
```

With the chat rules, also add a `## About me` section to `~/.claude/CLAUDE.md` that says what you know well and where you are a layman. The rules use it to decide which terms to explain, and without it Claude guesses. [`rules/CLAUDE.example.md`](rules/CLAUDE.example.md) shows one.

## What the evals show

Both plugins ship with evals for `claude plugin eval`, which runs each case with and without the plugin in a clean session. Over four suite runs of 13 chat cases, answers passed 83% to 88% of the checks with the rules and 65% to 70% without them. In the latest suite run of 8 writing cases, `/coldread:write` passed 90% against 53% without it, and against 77% for the skill before its rules for reviews, explainers and claims. The gain comes from the four new cases, which test those rules. On the four older ones, both versions passed 96% to 98%. Each text cost about three times as much as without the skill.

One person wrote the rules, the cases and the checks, and a model does the grading, so treat this as a first signal. [docs/results.md](docs/results.md) has every run and its limits, plus three blind comparisons of answers by that person.

## Use

`/coldread:write` starts on its own when you ask for a PR description, a doc or a message. To call it directly:

```
/coldread:write PR description for this branch, reader: the reviewer
/coldread:write rewrite docs/design.md for a backend developer who did not work on this
```

It first shows a brief: the reader, the one thing they must do, the points, where the text will be read and a word budget. The points set the length, about 80 words each, so correct a wrong or extra point when you see it. Where the text will be read sets the room: a review comment gets at most three sentences, and a Slack message or a commit body gets no Details section. When the reader must understand how something works, the skill defines each term with an example and walks one case from start to end.

The skill then drafts, fixes what the cold reader could not follow, and reports the cold reader's findings, the Vale warnings and the word count. It also quotes, side by side, what the brief says the reader must do and what the cold reader understood. When it rewrites or shortens a text, it lists every fact it removed, corrected or added, and every claim it could not trace to your notes, a check or the code.

When an answer did not land, type `/coldread:plain`, or say what you missed: `/coldread:plain what is a lease?`

## Settings

| Setting | Where | Default |
|---|---|---|
| Document language: `auto`, `en` or `pl` | `/plugin configure coldread@coldread` | `auto` writes in the language of your request |
| A project's document language and readers | two or three lines in that project's `CLAUDE.md` | none |
| What you know well | the About me section in `~/.claude/CLAUDE.md` | none, so Claude guesses |
| A project's own lint rules, the terms its readers know and its own style anchors | a `.coldread/` folder in that repository, see [Tune the Vale checks](#tune-the-vale-checks) | none |

A project's lines can read: "Documents in English. Reader: a backend developer on the team who knows the codebase and Jira." Claude Code keeps plugin options in user settings only, so a project's exceptions go into its `CLAUDE.md`. Chat needs no language setting, because the rules tell Claude to reply in your language.

Tell the skill what your readers already know, such as the codebase, tools and product names, in the request or in the project's `CLAUDE.md`. The skill passes this on in its description of the reader, so the cold reader does not ask for explanations of them.

## Run coldread from a clone, on one computer or several

Install from a clone when you want to edit the skill, its Vale checks or the chat rules, or to keep several computers on the same version. This replaces the install commands above. If you already installed from GitHub, run `claude plugin marketplace remove coldread` first.

```bash
git clone https://github.com/patrykwiener/coldread ~/Code/coldread && ~/Code/coldread/scripts/setup.sh
```

The script registers the clone as a local marketplace and installs the plugin from it. It sets up the chat rules with one import line in `~/.claude/CLAUDE.md` and backs that file up first. If `coldread-chat` is installed, the script skips that line, because both together load the rules twice. It also warns about copies of coldread that would load next to the plugin, such as one made by `install.sh`. To use another folder, clone there and run the script with `COLDREAD_DIR` set to that folder.

Claude Code loads a plugin from a local marketplace straight from the clone at every session start. So a `git pull` or an edit in the clone applies from the next session, or after `/reload-plugins`. Running the script again also works: it pulls, then checks the rest of the setup.

## Tune the Vale checks

The rules live in `plugins/coldread/skills/write/vale/`. The `.vale.ini` config lints English with the rules in `styles/Write/`. The `pl.ini` config lints Polish with the rules in `styles/WritePL/` and seven of the English ones, such as `SessionLabels`, which flags labels like `Phase A`. The skill runs both through `lint.sh`. For text in another language, `/coldread:write` skips linting and says so.

- **Acronyms**: add the ones every reader of yours knows to `exceptions` in `styles/Write/Acronyms.yml` or `styles/WritePL/Acronyms.yml`, in quotes. YAML reads an unquoted `NULL` or `YES` as a value, which silently disables the rule. Terms that only one project's readers know belong in that project's own layer, described below.
- **A noisy rule**: change its `level:` to `suggestion`, which the skill treats as a hint rather than something to fix, or delete its file.

Your edits apply only when the plugin runs from your clone, as set up in the section above.

### A project's own rules and examples

A repository can add its own layer without changing the plugin. `/coldread:write` uses these files when they exist, and each one is optional:

| File in the repository | What it does |
|---|---|
| `.coldread/vale/styles/config/vocabularies/Project/accept.txt` | Lists terms the project's readers use daily, one per line, so Vale stops flagging them, for example as acronyms to spell out. |
| `.coldread/vale/styles/Project/*.yml` | Adds the project's own Vale rules, such as product names it must spell one way. |
| `.coldread/examples-en.md` and `.coldread/examples-pl.md` | Holds style anchors from the project's own texts, which the skill reads instead of the invented ones. |

Commit the folder to share it with the team, or keep it out of git for yourself.

## Claude.ai and ChatGPT

Both limit the length of custom instructions, so [`rules/answering-nano.md`](rules/answering-nano.md) holds the same rules in under 1,000 characters. In Claude.ai, paste it with your About me section into "Instructions for Claude" under Settings, General. That field also covers Cowork. In ChatGPT, paste both into custom instructions.

## Without the plugin system

`./install.sh user` copies the plugin into `~/.claude/skills/coldread`. Claude Code 2.1.157 and later load such a folder as a plugin in every session, with the same commands and subagent. `./install.sh project /path/to/repo` does the same for one repository, so the team gets it through git.

## Run the evals

```bash
claude plugin eval plugins/coldread-chat --allow-tools Write
claude plugin eval plugins/coldread --allow-tools Write Bash
```

The chat suite has 13 cases, six of them in Polish, and the write suite has 8. Each case runs 3 times with the plugin and 3 times without it by default. Results go to `plugins/<name>/evals/results/`, which git ignores. Install Vale before you run the write suite, or the skill skips its lint step.

If every run stops at once with an error about the Docker credential store, the Bash sandbox refused to start because `~/.docker` holds a symbolic link. Run the write suite with `--allow-tools Write` only. It then measures the skill without its shell steps: the word count and the lint.

## Related work

- Anthropic's [doc-coauthoring](https://github.com/anthropics/skills) skill tests a document on a fresh model that sees only the document, the same idea as the cold read.
- [humanizer](https://github.com/blader/humanizer) removes word-level AI patterns and works well after `/coldread:write`.
- Two of the Vale checks, Parens and Semicolons, follow the [Google developer style guide](https://developers.google.com/style).

## License

MIT, see [LICENSE](LICENSE).
