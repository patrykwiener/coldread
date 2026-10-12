# Example ~/.claude/CLAUDE.md

Claude Code loads `~/.claude/CLAUDE.md` in every session. For coldread it holds up to two things: an About me note that tells Claude what you know, and an import line for the chat rules. Copy what you need into your own file and rewrite the note for yourself.

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

## The import line

You need this line only when you run coldread from a clone, and `scripts/setup.sh` adds it for you. It pulls in the chat rules from the clone, so `git pull` updates them. If you installed the `coldread-chat` plugin instead, leave the line out, or the rules load twice. Change the path if your clone is elsewhere.

```markdown
@~/Code/coldread/rules/answering.md
```
