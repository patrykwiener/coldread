# Example project CLAUDE.md

`/coldread:write` needs to know who reads your project's texts. Tell it in a `## Writing` section of the `CLAUDE.md` file in the project's root, which Claude Code loads in every session in that project. In two to four sentences, cover three things:

- the language of documents, when it differs from the language you write your requests in
- who reads each kind of text, and what they already know
- the names those readers use daily, so the cold reader does not ask about them

The skill takes the reader for its brief from this section. Commit the file, so everyone on the team writes for the same readers.

If your project keeps `CLAUDE.md` out of git and the team shares an `AGENTS.md`, put the section in `AGENTS.md` and import it from your `CLAUDE.md` with the line `@AGENTS.md`. OpenCode reads `AGENTS.md` directly.

The section can also set how the team writes one kind of text, such as review comments. In that project, the skill then follows it instead of its own default shape and instead of a personal How I write note.

A product team that writes in English:

```markdown
## Writing

Documents in English. PR descriptions: a backend developer on the team who knows the codebase, Jira and our deploy pipeline. Slack messages and release notes: the product manager, who knows the product but not the code. Readers know these names: Ledger, Payout API, the nightly sync.
```

A Polish team whose code is in English:

```markdown
## Pisanie

Dokumenty po polsku, kod i komentarze po angielsku. Opisy PR-ów czyta programista z zespołu: zna repo, Jirę i nasz deploy. Wiadomości na Slacka czyta PM: zna produkt, nie zna kodu. Czytelnicy znają nazwy Ledger i Payout API.
```

An open-source library:

```markdown
## Writing

Docs, PR descriptions and issue comments in English, for outside contributors who know Python packaging and pytest, not our internals. Explain each module name where it first appears. Release notes are for users who upgrade the package and never read its code.
```

A team with its own review style:

```markdown
## Writing

Documents in English, for developers on the team who know the codebase and Azure DevOps. Review comments: label each one blocking or non-blocking in its first word, at most two sentences, and give the fix as code when it is one.
```
