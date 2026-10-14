---
name: write
description: Write or rewrite text that a person or another agent will read - PR descriptions, review comments on a pull request, commit message bodies, design docs, ADRs, RFCs, runbooks, change proposals, explainers, READMEs, issue-tracker comments, emails, Slack or Teams messages, handoff notes, prompts for a new agent session - so a reader who was not in this session understands it on the first read. Use whenever you draft such text, when the user asks to make a text clearer, shorter or "more human", or before posting anything outside the terminal. Polish phrasings count the same, such as „napisz opis PR-a", „napisz komentarze do review", „przepisz to czytelniej", „skróć to", „notatka przekazania", „wiadomość na Slacka", „opisz to dla zespołu", „daj mi prompt do nowej sesji". Not for code comments or docstrings.
---

# Write for the reader who was not here

By the time you write, you have spent hours inside this work. You know what "Phase A", "option B" and "the fix" mean, and you cannot un-know it. The reader has none of that. Text written from your context reads to them as a list of private references, and they give up or ask you. Everything below exists to close that gap, and the cold read checks that it closed.

## 1. Fix the brief before writing

Show the user the brief before the draft, for example:

```
Reader: backend dev on the team; knows the codebase, the issue tracker and the product; did not work on this
Must: approve the PR, including one change to the retry policy
Points: (1) what changed for the export job (2) the retry change that needs approval (3) how it was measured
Channel: PR description
Budget: ~280 words for the main part; Details unlimited
Language: English (project default)
```

- **Reader**: their role and what they already know, concretely enough that the cold reader can tell what needs no explanation. If the user named a person, use what you know about their role. If the reader is genuinely unclear and it changes the text, ask one question; otherwise pick the most likely reader and say so.
- **Must**: the one thing the reader should do, decide or know after reading, or the thing they should understand, such as how a flow works. A Must to understand follows `channels/explainer.md`. If you cannot say it in one sentence, you are not ready to write.
- **Points**: the things the reader must know or decide to act on the Must, one line each. Keep a point only if the reader would do or decide something differently without it. This list, not the genre, sets the length. More than four points means the text is doing too much, because readers hold about four new things at once: propose splitting it, or moving some points to Details, before you write.
- **Channel**: where the text will be read. It sets the room before the budget does. Some channels have rules of their own in this skill's `channels/` folder: read the file before you write the brief, and name it in the Channel line, as in `Channel: review on a pull request (channels/review.md)`.
  - Comments and a summary for a review on a pull request: `channels/review.md`.
  - An explainer, or any text whose Must is to understand how something works: `channels/explainer.md`.
  - A prompt or a handoff that a new agent session will run: `channels/prompt.md`.
  - An ADR (architecture decision record), a runbook or a design doc, when the repository has no template for it: `channels/doc-types.md`. Name the kind in the Channel line, as in `Channel: runbook (channels/doc-types.md)`.
  - A document over about 1,500 words, a set of documents that link to each other, or a document that asks its readers to choose, such as an RFC: `channels/long-docs.md`.
  - A chat message, an issue comment or a commit body has no Details. What does not fit goes into the report for the user, not into the text.
  - A PR description, design doc, proposal or handoff note uses the budget below and may end with Details.
- **Budget** for the main part: about 40 words for the opening plus up to 80 words per point. A one-point Slack message or commit body lands near 100 words; a PR with two decisions near 200; a proposal with four points near 360. Details, at the end, have no budget; they hold descriptive material for the readers who want it.
- **Language**: the configured default is `${user_config.doc_language}`. If the project's instructions (its CLAUDE.md or AGENTS.md) name a language for documents, use that. Otherwise, with `auto` or any value other than `en` or `pl`, write in the language of the request, or in the reader's language when the user named a reader who uses another one. Code and everything that lives in it keeps the code's language, usually English: identifiers, comments, docstrings, log, error and assertion messages, also inside code blocks of a document in another language. When rewriting, keep the source's language unless the user asks otherwise.

## 2. Draft

**Lead with the answer and the ask.** The first one or two sentences say what changed or what you found, and what the reader must do about it, such as "Please approve the retry policy change below" or "No action needed; this is for your information". Anything that needs the reader's explicit decision is named up there, not discovered later. When the decision is a choice, name the options in those sentences, as in "Please decide by Thursday: release on Friday without retries for files over 2 GB, or wait until Tuesday"; a list below can add the details. A reader who stops after two sentences must still have the most important thing. A PR description, a review, an issue comment or a message gets no title heading above them: its title field or its thread already names it, so the first line is the answer. Then one short section per point. Material only some readers need goes under "Details" at the end.

**A template sets the structure.** When the repository has a template or a skill for this kind of text (a PR or issue template, an ADR template, a skill that opens pull requests), or the kind of text has fixed sections listed in `channels/doc-types.md`, keep its sections, their order, its fixed lines such as `Closes #` and its own instructions, including which sections to delete. Apply this skill inside each section: the answer first, names the reader has, one idea per sentence. Material that fits none of its sections goes under "Details" after the last one, or before it when the template says which section must come last. Material that `channels/doc-types.md` sends to another document does not go under Details at all. When the template says that, nothing may follow that section, not even a trailer such as an attribution line: leave the trailer out and say so in the report. Otherwise trailers, footers and badges follow the project's instructions too.

**Some templates serve two readers.** A PR description may end with a summary for a product manager, while the reviewer reads the rest. Give such a section its own reader line in the brief and write it for that reader. Simplify the words, not the facts: keep every time, amount and condition the section needs, such as "files up to 50 MB" rather than "small files". The budget then covers the opening section and each section for another reader. File tables, links and test commands count as Details, and a length the template sets wins over the budget.

**Write in the user's voice when the text goes out under their name.** A review comment, a reply in a thread or a message the user sends reads as theirs. If the user's instructions hold a note on how they write, such as a `## How I write` section, follow its length, register, openers, closers and the things it never does. A project's own rule for a kind of text, such as its review style, counts the same, and inside that project it wins over the user's note. Where such a note and a shape in this skill disagree, the note wins. It does not lift the rules for the reader: names the reader has, a source for every claim, and the ask. The note decides where the ask goes, not whether it is there.

**When rewriting an existing text, change how it says things, not what it says.** Add a fact only to explain a name the reader lacks, or to correct something you checked and found wrong. Do not add scope, new findings or adjacent advice the source did not contain, even when they are true and you found them while checking. Report every correction and every addition to the user, one line each, so they decide whether it belongs. Details hold material for the same decision, not everything you learned. If the source can be read two ways and you cannot check which reading is right, do not pick one: keep the source's wording and ask the user in the report. Treat two names in the source as two things unless you checked that they are one. A source that mentions "the release" and "the 14 May rollout" does not say the release happened on 14 May, so writing that adds a fact; it does not just reword one. Never answer a cold reader's question by guessing a fact. Before you change an existing file, copy it to the scratchpad: step 4 checks the rewrite against that copy.

**Describe the final state.** Say what is true now and why, not the order in which you discovered it. "Exports retry five times because the storage API drops about one request in a thousand" is better than a history of trying three retries, then ten, then going back. Mention an abandoned option only when the reader would otherwise suggest it, and then in one sentence. Tie what you verified to something the reader can check, such as a commit, a release or a named test run, not to the day you checked it. Keep a date only when the timing itself matters, such as when an incident began.

**Use names the reader already has.** Labels you invented while working (D3, Phase A, R1, option B, "the gate") mean nothing to them; replace each with what it is. When a label comes from the user's notes and you do not know what it stands for, do not pass it on: leave the sentence out if the reader does not need it for the Must, and list it in the report; ask the user only if the reader does need it. Ticket numbers are references, not names: write "the duplicate-invoice bug (#412)", never "#412 is fixed". Use one name per thing throughout.

**Explain at the reader's level.** Explain only what is specific to this project or this change and missing from the reader line. Never explain what anyone in the reader's role knows: a backend dev needs no definition of caching, JWT or an N+1 query. When something does need explaining, a clause is enough, as in "`build_manifest()` (lists the files an export contains)". If it needs more than a sentence, link the source or put the explanation in Details.

**Keep the text self-contained.** Instead of "see D4" or "as described in the design", state the needed fact in one sentence here, and link the source for those who want more. Never point to a file the reader cannot open, such as your local notes, a scratchpad or a path in your home directory: state what they need from it, or attach the file.

**In Polish text for developers, software terms stay English.** Write the word a Polish developer says out loud: endpoint, cache, payload, middleware, callback, namespace, feature flag. Never a forced translation such as "punkt końcowy" or "pamięć podręczna", which the reader has to translate back. Inflect the English term the way the team does (endpointu, cache'u, PR-a). Established Polish words stay Polish: żądanie, zapytanie, wyjątek, blokada, gałąź, wdrożenie. Where the team's documents settle a word either way, follow them.

**One idea per sentence.** Aim for about 20 words. A sentence carrying more than two facts becomes two sentences or a short list.

**Write prose by default.** Use a list for steps or truly parallel items, a table for comparisons, a code block for commands. Each paragraph should follow from the one before it; if the reader cannot tell why this paragraph comes next, add the sentence that says so.

**Make headings say something.** A reader skimming only the headings should get the argument: "The retry change needs your approval" tells them more than "Reliability". A template's fixed headings, such as an ADR's `## Decision`, stay as they are: the first sentence under them says it instead.

**Be plain about certainty.** Say once what you verified and what you did not. Do not hedge every sentence. For tests and checks, say separately what ran and with what result, what you only read, and what is still planned; a command or a test name is not a result. An open question says what would settle it, such as a decision, a measurement or a check, and what holds until then. Name a person as the one who decides or owns it only if they agreed to; otherwise say what kind of decision it needs, and list the names you left out in the report.

**Wrap Markdown the way the project does.** If the project has a rule on line wrapping, follow it; otherwise keep the wrapping of the file you edit. In a new file and in a PR or issue description, keep each paragraph on one line and break lines only where the break carries meaning: list items, table rows, code.

Before drafting a PR description, review, handoff note, proposal, explainer or doc, read the style anchors for the text's language and match the register and density of their examples, not their topics. If the repository's root, or the nearest folder above it, has its own anchors in `.coldread/examples-pl.md` or `.coldread/examples-en.md`, use those; otherwise use `examples-pl.md` or `examples-en.md` in this skill's directory.

## 3. Check every claim

The cold reader finds what a reader cannot follow, not what is false. So before you fit the budget, go through the main part and find the source of each sentence that states a number, how the system behaves, a consequence, a recommendation, or a status such as merged, tested or deployed. A source is the user's notes or the source text, a check you ran, or code you read; name the check or the file. What follows from the notes by necessity has them as its source, such as "jobs and their data are in the same database" when the notes say they commit in one transaction. A claim about the user's system with no source does not stay as a fact: cut it, or keep it and mark it in the text, in the text's language, as in "Job traffic slows the application's queries (to confirm).", and list it in the report. The mark stays in the file after the report is gone, so a reader who never saw the report still knows. This covers a consequence you inferred, a recommendation you added, a definition you applied to this system, such as "the same record can arrive twice", and a detail you completed, such as a year for a date the notes give without one: give the date as the notes do. A general fact about a named tool, such as what `SKIP LOCKED` does or that a message broker cannot join a Postgres transaction, needs no mark, because the reader can check it in the tool's documentation; list it in the report as an addition. Never fill a gap with a plausible fact, however likely.

## 4. Fit the budget without losing facts

Count the words of the main part (`wc -w`). If it is over budget:

- **Move before you cut.** Descriptive material, evidence and edge cases go to Details, or to the report for the user when the channel has no Details. Moving is the default.
- **Delete only** the history of attempts, repetition, and narration of process ("we ran three reviews").
- **Never compress to fit.** Packing facts into longer sentences, parentheses or semicolons to save words recreates the density this skill removes. If the main part still does not fit, the points list is too long; say so instead.
- **Every other fact you remove** goes into the report for the user, one line each, so nothing disappears silently.

When the text rewrites an existing file, check what left it. Run the facts check on the copy you made and the new version, and add the other documents of a set when facts may have moved there:

```bash
"${CLAUDE_PLUGIN_ROOT}/skills/write/facts.sh" <copy> <file> [<other documents>...]
```

It lists every number and inline code span of the original that appears in none of the new files. Put each one back, or report it as removed.

## 5. Lint

Run the rules for the text's language:

```bash
"${CLAUDE_PLUGIN_ROOT}/skills/write/vale/lint.sh" pl <file>   # Polish
"${CLAUDE_PLUGIN_ROOT}/skills/write/vale/lint.sh" en <file>   # English
```

The rules exist for English and Polish. For a text in another language, skip this step and say so in the report. When the repository's root or a folder above it has a `.coldread/vale/styles` folder, the script uses the nearest one. It runs the project's own rules from its `Project/` folder and accepts the terms its readers use daily, listed in `config/vocabularies/Project/accept.txt`.

Both check mechanically what is cheap to check: undefined acronyms, session labels such as D3, Phase A or Wariant B, bare IDs and issue numbers such as #412, invented tags such as [OPINION], paths on your own machine, the dates on which you checked something, parentheses, semicolons, long sentences (over 30 words in Polish, over 35 in English) and table cells over 40 words. The Polish config adds words AI-generated Polish overuses, forced translations of software terms ("punkt końcowy"), calques from English ("w oparciu o", "adresować problem"), officialese and verbs hidden in nouns ("dokonać zmiany"), filler transitions ("Ponadto", "Warto zauważyć"), more than one dash in a paragraph, and a FOG-PL readability score per paragraph. The English config adds overused AI words, filler transitions, em dashes and reading grade. Fix warnings unless they are wrong for this reader, for example an acronym the reader uses daily. Suggestions are hints. Running this before the cold read saves the reader from reporting what a regex can find. If `vale` is not installed, say so and skip this step.

## 6. Cold read

Save the draft to a file if it is not one already (use the scratchpad). Then spawn one fresh reader:

- Use the `coldread:cold-reader` subagent. It starts without any CLAUDE.md, so it knows only what the reader line tells it. If it is not available, use a general-purpose subagent and tell it to read `${CLAUDE_PLUGIN_ROOT}/agents/cold-reader.md` first and follow it exactly. That reader still loads CLAUDE.md, so say so in the report.
- Never run the reader as a fork: a fork inherits this whole session, which is exactly what the reader must not have.
- Give it only the file path and the reader line from the brief. Never pass session context, a glossary, your summary or what you meant.
- When the brief gives some sections their own reader, save each reader's sections to their own file and run one reader per file.
- For a review, build the reader's file as `channels/review.md` says: the summary, then each comment under the code lines it is attached to.
- An empty result or an error is a failed run, not a clean read: start one new reader.

Then:

1. **Compare its section 1 with your Must, and show both in the report.** This is the real test. Quote your Must and the reader's sentence side by side, so the user judges the match instead of taking your word for it. If the reader understood what is asked of them, the text works, even with a few minor findings left.
2. **Compare its retelling, section 7, with your Points.** A point the reader left out or got wrong is a gap in the text, not in the reader: fix it like a blocker.
3. **Fix every `[blocker]`.** Fix a `[minor]` only when the fix is small and does not add length to the main part.
4. **Run a second reader only if** its summary did not match the Must, or `ask_up_front` was `no`, or fixing the blockers changed the structure. Use a new reader, because one that saw the earlier draft already knows your terms. Never run a third.

Skip the cold read for texts under 40 words.

## 7. Report

Give the user the final text, then:

- one line of evidence, for example `Cold read: 1 round, blockers 3 → 0 · Vale 0 warnings · main part 236/280 words · claims 11 sourced, 1 cut`;
- the ask check: `Must: "approve the retry change" · reader: "approve raising export retries to five"`;
- the facts you removed rather than moved, and the claims you cut or marked as unverified, one line each, or "none";
- when rewriting, the facts you corrected or added, one line each, or "none", and the command that shows the change: `git diff --no-index --word-diff <copy> <file>`;
- for a review, the points you kept out of the comments, one line each;
- anything still open after the cold read.

Never post, send or commit the text yourself, even when a tool for it is at hand. Show it and stop: the user decides what happens next.

If the text still has word-level AI tics that Vale does not catch ("not X but Y", rule-of-three lists, manufactured punchlines), an optional word-level pass can follow, such as [humanizer](https://github.com/blader/humanizer) if the user has it installed. It never replaces the steps above, and if it changes more than wording, run Vale again. Humanizer's word lists are English, so on a text in another language use it only for those structural tics.
