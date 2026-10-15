# Example ~/.claude/CLAUDE.md

Claude Code loads `~/.claude/CLAUDE.md` in every session. For coldread it holds up to three things. An About me note tells Claude what you know, a How I write note describes the texts that go out under your name, and an import line pulls in the chat rules. Copy what you need into your own file and rewrite the notes for yourself. In OpenCode, the same sections go into `~/.config/opencode/AGENTS.md`.

## About me

Write two to four sentences that cover three things: what Claude can leave unexplained, where you are a layman, and how you read most easily. The chat rules use the note to decide which terms to explain. Keep the heading `## About me`, because the rules refer to the note by that name. The note is about you, so it stays in your own file and never goes into a project.

A backend engineer:

```markdown
## About me

Backend engineer: Python, PostgreSQL and AWS need no explanation. A layman in frontend work, construction and electrical installations. I read symbols such as ≤ and × faster than the words for them.
```

A product manager:

```markdown
## About me

Product manager for a B2B invoicing app. I know the product, our customers and basic SQL. I am a layman in infrastructure, so explain terms such as a queue or an index where they first appear. I compare options most easily in a table.
```

A data scientist who reads Polish faster than English:

```markdown
## About me

Data scientist: statistics, pandas and experiment design need no explanation. I am new to this company's infrastructure, so explain our services and any Kubernetes or Terraform term. Reply in Polish even when I ask in English, and keep code, commands and product names in English.
```

## How I write

`/coldread:write` and `/coldread:reply` follow this note for texts that go out under your name: review comments, replies in a thread, chat messages. Where the note and the skill's own shape for a channel disagree, the note wins. The skill still keeps its rules for the reader: names the reader has, a source for every claim, and the ask.

Measure the note rather than guess it. Ask Claude to read 20 to 40 of your own texts of one kind, such as the review comments you left on other people's pull requests, and to report:

- words per text: the median and the longest;
- how the texts open and how they end, with your most common phrases;
- what you never use, such as headings, bold, lists, labels like `nit:` or emoji;
- whether the texts ask or tell, and when.

Then write down what holds for nearly all of them. Keep the heading `## How I write`, because the skills look for the note by that name.

A reviewer who keeps comments short and ends on a question:

```markdown
## How I write

Review comments: one or two plain paragraphs, median 30 words, never over 70. No headings, lists, bold, labels such as nit: or Fix:, or a phrase and a colon in front of the point; the tone carries how serious it is. Open on the concrete thing in backticks and what it actually does, cite file.py:42 inline, and end on a question or a proposal, such as "wdyt?" or "Split it out?". A real defect gets "Please ..."; a naming idea gets "how about ...?". A reply on my own pull request says what changed and nothing else.
Chat messages: friendly and short, the ask in the first sentence, then the link it needs.
```

## The import line

You need this line only when you run coldread from a clone, and `scripts/setup.sh` adds it for you. It pulls in the chat rules from the clone, so `git pull` updates them. If you installed the `coldread-chat` plugin instead, leave the line out, or the rules load twice. Change the path if your clone is elsewhere.

```markdown
@~/Code/coldread/rules/answering.md
```
