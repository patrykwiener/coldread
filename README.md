# coldread

coldread makes Claude Code and OpenCode write for a reader who was not in the session. Its writing skill drafts PR descriptions, review comments, design docs, explainers, handoff notes, prompts for a new agent session and Slack messages. Then a subagent that has seen neither the session nor your CLAUDE.md reads each draft and reports what it could not follow. Optional chat rules make everyday answers easier to follow.

To get started, read [What you get](#what-you-get), [Install](#install) and [How configuration works](#how-configuration-works), then follow the [three setup steps](#set-it-up-in-three-steps). If you already installed coldread, start at How configuration works. [Keep your settings to yourself](#keep-your-settings-to-yourself) covers settings that stay out of the team's repository or reach every worktree on your computer. OpenCode, an install from a clone, the Vale rules and the evals have pages of their own in [docs/](#more-in-docs).

- [What you get](#what-you-get)
- [Install](#install)
- [How configuration works](#how-configuration-works)
- [Set it up in three steps](#set-it-up-in-three-steps)
- [Keep your settings to yourself](#keep-your-settings-to-yourself)
- [Use](#use)
- [What the evals show](#what-the-evals-show)
- [Claude.ai and ChatGPT](#claudeai-and-chatgpt)
- [More in docs/](#more-in-docs)
- [Related work](#related-work)

## What you get

| Part | When it works | What it does |
|---|---|---|
| `/coldread:write` | starts on its own when you ask for a PR description, a review, a doc, a message or a prompt for a new session | Shows a brief, its plan for the text, then drafts the text, marks each claim it could not trace to a source, lints it with Vale and hands it to the cold reader. |
| `coldread:cold-reader` | inside `/coldread:write` | A subagent with no session and no CLAUDE.md that reads the text once and reports what it could not follow. |
| `/coldread:reply` | when someone sent you a message you must answer | Says what the sender asks, resolves the names you may not know, then drafts your reply. |
| `/coldread:plain` | when an answer did not land | Names what failed, such as an unknown term, then explains again in new words. |
| Chat rules, in the optional `coldread-chat` plugin | every chat answer | Ten rules, such as answering first, giving at most four points, explaining every new term and asking questions that make sense on their own. |

The lint step uses Vale, a linter for prose. An ADR, a runbook or a design doc gets the sections its readers expect, and `/coldread:write` names material meant for another document in its report instead of putting it in the text.

## Install

The commands below are for Claude Code. In OpenCode, follow [docs/opencode.md](docs/opencode.md) instead. The configuration after this section applies to both tools.

```bash
claude plugin marketplace add patrykwiener/coldread
claude plugin install coldread@coldread        # /coldread:write, /coldread:reply, /coldread:plain and the cold reader
claude plugin install coldread-chat@coldread   # optional: the chat rules in every session
brew install vale                              # optional: the lint step; other systems: vale.sh
# later, to update: claude plugin update coldread@coldread
#   and, if installed: claude plugin update coldread-chat@coldread
```

coldread needs Claude Code 2.1.271 or later, because older versions cannot load a plugin whose option offers a fixed list of values. Without Vale, `/coldread:write` skips its lint step and says so. To edit coldread, or to keep several computers on the same version, install from a clone instead, as [docs/clone.md](docs/clone.md) describes.

## How configuration works

coldread works without any settings, and each one you add tells it more about you or your readers. It has five settings. Three belong to you and apply in every project, one belongs to a project, and the `.coldread/` folder can belong to either. The table shows what each setting does, where it lives, whom it applies to, and what happens without it.

| What it sets | Where it lives | Applies to | Without it |
|---|---|---|---|
| The language `/coldread:write` writes in, set to `auto`, `en` or `pl` | the plugin option, set with `/plugin configure coldread@coldread` | you, in every project | `auto`, the language of your request |
| What you know, so chat answers from `coldread-chat` and `/coldread:reply` explain only the terms that are new to you | an About me section in `~/.claude/CLAUDE.md`, [step 1](#1-tell-claude-what-you-know-and-how-you-write) | you, in every project | Claude guesses what you know |
| How the texts that go out under your name sound, such as review comments | a How I write section in `~/.claude/CLAUDE.md`, [step 1](#1-tell-claude-what-you-know-and-how-you-write) | you, in every project | the skill's default shape for each kind of text, such as a label in front of each review comment |
| Who reads the project's texts, the names they know, the document language, the team's review style | a Writing section in the project's `CLAUDE.md`, [step 2](#2-tell-coldreadwrite-who-reads-your-projects-texts) | everyone in the project, or only you, as [Keep your settings to yourself](#keep-your-settings-to-yourself) shows | the skill picks the most likely reader and says so in its brief |
| The terms the project's readers know, its own lint rules, and its own sample texts | a `.coldread/` folder in the repository's root or a folder above it, [step 3](#3-optional-share-your-projects-terms-and-texts) | everyone in the project if you commit it, otherwise only you on this computer | coldread's own lint rules and its invented sample texts |

When two places disagree, the narrower one wins where it applies. A project's own rule for a kind of text beats your How I write note inside that project, and your note beats the skill's default shape. For example, your note may say that review comments carry no labels, while the project's Writing section says each comment opens with "blocking" or "non-blocking". Comments in that project then get the label, and comments in your other projects do not. No note lifts the skill's rules for the reader. The text still uses names the reader has, gives a source for every claim, and states the ask. The document language follows the same order, so a language that the project's `CLAUDE.md` names beats the plugin option.

Claude Code keeps plugin options in user settings only, so a project's exceptions go into its `CLAUDE.md`. Chat needs no language setting, because the rules tell Claude to reply in your language. A request can also name its own reader for one text, as in the examples under [Use](#use). In OpenCode, `AGENTS.md` files take the place of `CLAUDE.md`, as [docs/opencode.md](docs/opencode.md#commands-and-settings-in-opencode) shows.

## Set it up in three steps

The first two steps take a few minutes each. The third is for teams that want the lint step to know their project.

### 1. Tell Claude what you know, and how you write

This step gives coldread two notes about you. The About me note is for the chat rules from `coldread-chat`, which shape every answer: answer first, at most four points, every new term explained. They use the note to decide which terms are new to you, and without it Claude guesses. `/coldread:reply` reads it too, to tell which names in a message you may not know. Add the note to `~/.claude/CLAUDE.md`, the file Claude Code loads in every session. If you set `CLAUDE_CONFIG_DIR`, use the `CLAUDE.md` in that folder instead. In two to four sentences, say what Claude can leave unexplained, where you are a layman, and how you read most easily.

```markdown
## About me

Backend engineer: Python, PostgreSQL and AWS need no explanation. A layman in frontend work, construction and electrical installations. I read symbols such as ≤ and × faster than the words for them.
```

[`rules/CLAUDE.example.md`](rules/CLAUDE.example.md) has two more notes, for a product manager and for a data scientist. To check yours, ask Claude about a topic from your layman list and see whether the answer explains its trade terms.

If texts go out under your name, such as review comments or Slack messages, add a How I write note to the same file. It works without the chat rules, because `/coldread:write` and `/coldread:reply` follow it for those texts. It wins over the skill's default shape for that kind of text, such as the labels it puts on review comments. Measure the note rather than guess it. Ask Claude to read 20 to 40 of your own comments or messages and count their words, how they open and end, and the markup you never use.

```markdown
## How I write

Review comments: one or two plain sentences, about 30 words, never over 70. No headings, lists, bold or labels such as nit: or Fix:. Open on the concrete thing in backticks and what it does, and end on a question, such as "wdyt?". Slack messages: friendly and short, with the ask in the first sentence.
```

### 2. Tell `/coldread:write` who reads your project's texts

In each project where you write for other people, add a Writing section to the `CLAUDE.md` in the project's root. Say which language documents use, who reads each kind of text, and which names those readers already know. The skill reads this section to name the reader in the brief it shows before drafting, so the cold reader does not ask about names your team uses daily. A team can set its review style here too. In that project, the team's style wins over the skill's default shape and over a personal How I write note.

```markdown
## Writing

Documents in English. PR descriptions: a backend developer on the team who knows the codebase, Jira and our deploy pipeline. Slack messages and release notes: the product manager, who knows the product but not the code. Readers know these names: Ledger, Payout API, the nightly sync.
```

[`rules/CLAUDE.project.example.md`](rules/CLAUDE.project.example.md) has versions for a Polish team and for an open-source library. To check the section, ask for a PR description. The brief that `/coldread:write` shows first should then describe your reviewer.

Some projects keep `CLAUDE.md` out of git and share `AGENTS.md` instead. Then put the section in `AGENTS.md`. Claude Code 2.1.277 and later read `AGENTS.md` on their own, but only when no `CLAUDE.md` or `CLAUDE.local.md` sits in the working folder or a folder above it. If a `CLAUDE.md` or `CLAUDE.local.md` sits next to the shared `AGENTS.md`, start that file with the line `@AGENTS.md`, which imports the shared file. For such a file in a folder above the project, see [The same settings in every worktree](#the-same-settings-in-every-worktree).

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

Then replace the samples with your own. Put your terms in `accept.txt`, your product names in `vale/styles/Project/ProductNames.yml`, and your team's texts in `examples-en.md`. Do not list in `accept.txt` a name whose spelling one of your rules enforces. Vale then accepts the name in any letter case, so the rule no longer catches a variant such as `Payout Api`. Commit the folder to share it with the team, or keep it to yourself as the next section shows. To check it, ask for a text that uses one of your terms. The Vale warnings that `/coldread:write` lists at the end should not name it.

## Keep your settings to yourself

Your About me and How I write notes stay with you, because they live in your own `~/.claude/CLAUDE.md`. A project's Writing section and its `.coldread/` folder reach the whole team once you commit them. Keep them out of git when the team does not use coldread, or when they hold notes only you need.

### A Writing section only you use

Put the section in a `CLAUDE.local.md` file in the project's root. Claude Code loads that file next to the project's `CLAUDE.md`, and it is meant for notes that stay out of git. If the project shares an `AGENTS.md` and has no `CLAUDE.md`, start the file with the line `@AGENTS.md`. Claude Code stops reading `AGENTS.md` on its own once a `CLAUDE.local.md` exists, so the import keeps the team's file loaded.

```markdown
@AGENTS.md

## Writing

Documents in UK English. PR descriptions: a developer on the team who knows the codebase and did not work on the change. Readers know these names: Ledger, Payout API.
```

Then keep the file out of git without changing the team's `.gitignore`. Git also reads the file `info/exclude` in the clone's `.git` folder, and that file is never committed. The command below adds a line to it. It works inside a worktree too, because `--git-common-dir` points at the main `.git` folder:

```bash
echo 'CLAUDE.local.md' >> "$(git rev-parse --git-common-dir)/info/exclude"
```

### A `.coldread/` folder only you use

Add the folder to the same file:

```bash
echo '.coldread/' >> "$(git rev-parse --git-common-dir)/info/exclude"
```

### The same settings in every worktree

`git worktree add` checks out only what is committed, so a private file in the main checkout is missing from every worktree. Put such files in the folder that holds the checkout and its worktrees instead. That folder must hold only this project's checkouts, because both files below also reach every other repository inside it. For `~/Code/acme/acme-api` and its worktree `~/Code/acme/acme-api-pr12`, that folder is `~/Code/acme/`:

- `~/Code/acme/.coldread/` covers every worktree, because coldread looks for `.coldread/` in the repository's root first, then in each folder above it, and uses the nearest one.
- `~/Code/acme/CLAUDE.local.md` covers every worktree too, because Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` from the working folder and from every folder above it. Leave `@AGENTS.md` out of this file. An import path counts from the file that holds it, so here it would look for `~/Code/acme/AGENTS.md`.

`~/Code/acme/CLAUDE.local.md` also stops Claude Code from reading each worktree's `AGENTS.md` on its own. If the project shares an `AGENTS.md` and no `CLAUDE.md` of the project imports it, tell Claude Code to read `AGENTS.md` files together with `CLAUDE.md` files. The setting belongs to `cc-plugin-agents-md@builtin`, the built-in plugin that reads `AGENTS.md`. Add this to `~/.claude/settings.json`, or to `settings.json` in your `CLAUDE_CONFIG_DIR` folder if you set one, because Claude Code ignores the setting in a project's settings. It needs Claude Code 2.1.285 or later:

```json
{
  "pluginConfigs": {
    "cc-plugin-agents-md@builtin": {
      "options": { "instructionFiles": "claude-md-and-agents-md" }
    }
  }
}
```

The setting applies in every project. Claude Code skips an `AGENTS.md` that it has already loaded through an import, so no file loads twice.

## Use

`/coldread:write` starts on its own when you ask for a PR description, a doc or a message. To call it directly:

```
/coldread:write PR description for this branch, reader: the reviewer
/coldread:write rewrite docs/design.md for a backend developer who did not work on this
```

It first shows a brief, which names the reader, the one thing they must do, the points, where the text will be read and a word budget. The points set the length, about 80 words each, so correct a wrong or extra point when you see it. Where the text will be read sets the room, so a review comment gets at most three sentences, and a Slack message or a commit body gets no Details section. When the reader must understand how something works, the skill defines each term with an example and walks one case from start to end.

The skill then drafts, fixes what the cold reader could not follow, and reports the cold reader's findings, the Vale warnings and the word count. It also quotes, side by side, what the brief says the reader must do and what the cold reader understood, and checks the cold reader's retelling against the points. When it rewrites or shortens a text, it lists every fact it removed, corrected or added, and every claim it could not trace to your notes, a check or the code. When it rewrites a file, a script lists every number and code span that left it. The skill never posts, sends or commits a text. You do that yourself.

Ask for a prompt for a new session, and the skill writes it for an agent that has your repository but not this session. The prompt holds your words verbatim, the decisions already made, the files to read, steps with stops for your approval, and the traps earlier sessions hit. A long document or a set of documents gets a reading path for each kind of reader. A document that asks its readers to choose gets options, a labelled recommendation with its reason, and the evidence that would change it.

When someone sent you a message you do not fully get, paste it after `/coldread:reply`, or just ask what they mean. The skill says what the sender asks, resolves the names you may not know or says who could, and drafts your reply in your voice.

When an answer did not land, type `/coldread:plain`, or say what you missed: `/coldread:plain what is a lease?`

## What the evals show

Claude knows what its own working labels mean, and the reader does not. In the evals, Claude wrote a Slack message to a product manager from notes that mentioned `Phase A`, `option B` and `D3` without explaining them. Without coldread, at least one of these labels reached the manager in 9 of 9 attempts. With coldread, none did in 9 of 9. The writing skill cut them because the manager did not need them to decide, and it listed the cuts in its report.

Both plugins ship with evals for `claude plugin eval`, which runs each case with and without the plugin in a clean session. Over four suite runs of 13 chat cases, answers passed 83% to 88% of the checks with the rules and 65% to 70% without them. In the latest suite run of 19 writing cases, 5 runs each, `/coldread:write` averaged 92% per case against 66% without it, measured before the fixes of 2026-10-14 listed in the results. Seven cases test document structure, such as a runbook that leaves design history out, and three of them were written before any run, to check the rules on text they were not tuned on. Bash was blocked on that computer, so the run measured the skill without Vale, the word count and the facts check. An earlier run with Vale on another computer passed 90% against 53% on 8 cases. Each text cost about three times as much as without the skill.

One person wrote the rules, the cases and the checks, and a model does the grading, so treat this as a first signal. [docs/results.md](docs/results.md) has every run and its limits, plus three blind comparisons of answers by that person. [docs/evals.md](docs/evals.md) shows how to run the evals yourself.

## Claude.ai and ChatGPT

Both limit the length of custom instructions, so [`rules/answering-nano.md`](rules/answering-nano.md) holds the same rules in under 1,000 characters. In Claude.ai, paste it with your About me section into "Instructions for Claude" under Settings, General. That field also covers Cowork. In ChatGPT, paste both into custom instructions.

## More in docs/

- [docs/opencode.md](docs/opencode.md) sets coldread up in OpenCode 2 and maps its commands and settings.
- [docs/clone.md](docs/clone.md) installs coldread from a clone, so you can edit the skill, its checks or the chat rules, or keep several computers on one version. It also covers an install without a marketplace.
- [docs/vale.md](docs/vale.md) shows how to add the acronyms your readers know, or quiet a noisy Vale rule.
- [docs/evals.md](docs/evals.md) runs the evals with `claude plugin eval`.
- [docs/results.md](docs/results.md) has every eval run so far and its limits.

## Related work

- Anthropic's [doc-coauthoring](https://github.com/anthropics/skills) skill tests a document on a fresh model that sees only the document, the same idea as the cold read.
- [humanizer](https://github.com/blader/humanizer) removes word-level AI patterns and works well after `/coldread:write`.
- Two of the Vale checks, Parens and Semicolons, follow the [Google developer style guide](https://developers.google.com/style).

## License

MIT, see [LICENSE](LICENSE).
