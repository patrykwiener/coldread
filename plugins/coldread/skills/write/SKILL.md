---
name: write
description: Write or rewrite text that a person will read - PR descriptions, commit message bodies, design docs, ADRs, RFCs, runbooks, change proposals, READMEs, issue-tracker comments, emails, Slack messages, handoff notes - so a reader who was not in this session understands it on the first read. Use whenever you draft such text, when the user asks to make a text clearer, shorter or "more human", or before posting anything outside the terminal. Polish phrasings count the same, such as „napisz opis PR-a", „przepisz to czytelniej", „skróć to", „notatka przekazania", „wiadomość na Slacka", „opisz to dla zespołu". Not for code comments or docstrings.
---

# Write for the reader who was not here

By the time you write, you have spent hours inside this work. You know what "Phase A", "option B" and "the fix" mean, and you cannot un-know it. The reader has none of that. Text written from your context reads to them as a list of private references, and they give up or ask you. Everything below exists to close that gap, and the cold read checks that it closed.

## 1. Fix the brief before writing

Show the user the brief before the draft, for example:

```
Reader: backend dev on the team; knows the codebase, the issue tracker and the product; did not work on this
Must: approve the PR, including one change to the retry policy
Points: (1) what changed for the export job (2) the retry change that needs approval (3) how it was measured
Budget: ~280 words for the main part; Details unlimited
Language: English (project default)
```

- **Reader**: their role and what they already know, concretely enough that the cold reader can tell what needs no explanation. If the user named a person, use what you know about their role. If the reader is genuinely unclear and it changes the text, ask one question; otherwise pick the most likely reader and say so.
- **Must**: the one thing the reader should do, decide or know after reading. If you cannot say it in one sentence, you are not ready to write.
- **Points**: the things the reader must know or decide to act on the Must, one line each. This list, not the genre, sets the length. More than four points means the text is doing too much, because readers hold about four new things at once: propose splitting it, or moving some points to Details, before you write.
- **Budget** for the main part: about 40 words for the opening plus up to 80 words per point. A one-point Slack message or commit body lands near 100 words; a PR with two decisions near 200; a proposal with four points near 360. Details, at the end, have no budget; they hold descriptive material for the readers who want it.
- **Language**: the configured default is `${user_config.doc_language}`. If the project's instructions (its CLAUDE.md or AGENTS.md) name a language for documents, use that. Otherwise, with `auto` or any value other than `en` or `pl`, write in the language of the request, or in the reader's language when the user named a reader who uses another one. Code and everything that lives in it keeps the code's language, usually English: identifiers, comments, docstrings, log, error and assertion messages, also inside code blocks of a document in another language. When rewriting, keep the source's language unless the user asks otherwise.

## 2. Draft

**Lead with the answer and the ask.** The first one or two sentences say what changed or what you found, and what the reader must do about it, such as "Please approve the retry policy change below" or "No action needed; this is for your information". Anything that needs the reader's explicit decision is named up there, not discovered later. When the decision is a choice, name the options in those sentences, as in "Please decide by Thursday: release on Friday without retries for files over 2 GB, or wait until Tuesday"; a list below can add the details. A reader who stops after two sentences must still have the most important thing. Then one short section per point. Material only some readers need goes under "Details" at the end.

**A template sets the structure.** When the repository has a template or a skill for this kind of text (a PR or issue template, an ADR template, a skill that opens pull requests), keep its sections, their order, its fixed lines such as `Closes #` and its own instructions, including which sections to delete. Apply this skill inside each section: the answer first, names the reader has, one idea per sentence. Material that fits none of its sections goes under "Details" after the last one.

**When rewriting an existing text, change how it says things, not what it says.** Add a fact only to explain a name the reader lacks, or to correct something you checked and found wrong. Do not add scope, new findings or adjacent advice the source did not contain, even when they are true and you found them while checking. Report every correction and every addition to the user, one line each, so they decide whether it belongs. Details hold material for the same decision, not everything you learned. If the source can be read two ways and you cannot check which reading is right, do not pick one: keep the source's wording and ask the user in the report. Treat two names in the source as two things unless you checked that they are one. A source that mentions "the release" and "the 14 May rollout" does not say the release happened on 14 May, so writing that adds a fact; it does not just reword one. Never answer a cold reader's question by guessing a fact.

**Describe the final state.** Say what is true now and why, not the order in which you discovered it. "Exports retry five times because the storage API drops about one request in a thousand" is better than a history of trying three retries, then ten, then going back. Mention an abandoned option only when the reader would otherwise suggest it, and then in one sentence.

**Use names the reader already has.** Labels you invented while working (D3, Phase A, R1, option B, "the gate") mean nothing to them; replace each with what it is. When a label comes from the user's notes and you do not know what it stands for, do not pass it on: leave the sentence out if the reader does not need it for the Must, and list it in the report; ask the user only if the reader does need it. Ticket numbers are references, not names: write "the duplicate-invoice bug (#412)", never "#412 is fixed". Use one name per thing throughout.

**Explain at the reader's level.** Explain only what is specific to this project or this change and missing from the reader line. Never explain what anyone in the reader's role knows: a backend dev needs no definition of caching, JWT or an N+1 query. When something does need explaining, a clause is enough, as in "`build_manifest()` (lists the files an export contains)". If it needs more than a sentence, link the source or put the explanation in Details.

**Keep the text self-contained.** Instead of "see D4" or "as described in the design", state the needed fact in one sentence here, and link the source for those who want more.

**In Polish text for developers, software terms stay English.** Write the word a Polish developer says out loud: endpoint, cache, payload, middleware, callback, namespace, feature flag. Never a forced translation such as "punkt końcowy" or "pamięć podręczna", which the reader has to translate back. Inflect the English term the way the team does (endpointu, cache'u, PR-a). Established Polish words stay Polish: żądanie, zapytanie, wyjątek, blokada, gałąź, wdrożenie. Where the team's documents settle a word either way, follow them.

**One idea per sentence.** Aim for about 20 words. A sentence carrying more than two facts becomes two sentences or a short list.

**Write prose by default.** Use a list for steps or truly parallel items, a table for comparisons, a code block for commands. Each paragraph should follow from the one before it; if the reader cannot tell why this paragraph comes next, add the sentence that says so.

**Make headings say something.** A reader skimming only the headings should get the argument: "The retry change needs your approval" tells them more than "Reliability".

**Be plain about certainty.** Say once what you verified and what you did not. Do not hedge every sentence.

**Wrap Markdown the way the project does.** If the project has a rule on line wrapping, follow it; otherwise keep the wrapping of the file you edit. In a new file and in a PR or issue description, keep each paragraph on one line and break lines only where the break carries meaning: list items, table rows, code.

Before drafting a PR description, handoff note, proposal or doc, read the style anchors in this skill's directory for the text's language, `examples-pl.md` or `examples-en.md`, and match the register and density of their examples, not their topics.

## 3. Fit the budget without losing facts

Count the words of the main part (`wc -w`). If it is over budget:

- **Move before you cut.** Descriptive material, evidence and edge cases go to Details. Moving is the default.
- **Delete only** the history of attempts, repetition, and narration of process ("we ran three reviews").
- **Never compress to fit.** Packing facts into longer sentences, parentheses or semicolons to save words recreates the density this skill removes. If the main part still does not fit, the points list is too long; say so instead.
- **Every other fact you remove** goes into the report for the user, one line each, so nothing disappears silently.

## 4. Lint

Pick the config for the text's language:

```bash
vale --config "${CLAUDE_PLUGIN_ROOT}/skills/write/vale/pl.ini" <file>      # Polish
vale --config "${CLAUDE_PLUGIN_ROOT}/skills/write/vale/.vale.ini" <file>   # English
```

The rules exist for English and Polish. For a text in another language, skip this step and say so in the report.

Both check mechanically what is cheap to check: undefined acronyms, session labels such as D3, Phase A or Wariant B, bare IDs and issue numbers such as #412, invented tags such as [OPINION], parentheses, semicolons and long sentences (over 30 words in Polish, over 35 in English). The Polish config adds words AI-generated Polish overuses, forced translations of software terms ("punkt końcowy"), calques from English ("w oparciu o", "adresować problem"), officialese and verbs hidden in nouns ("dokonać zmiany"), filler transitions ("Ponadto", "Warto zauważyć"), more than one dash in a paragraph, and a FOG-PL readability score per paragraph. The English config adds overused AI words, filler transitions, em dashes and reading grade. Fix warnings unless they are wrong for this reader, for example an acronym the reader uses daily. Suggestions are hints. Running this before the cold read saves the reader from reporting what a regex can find. If `vale` is not installed, say so and skip this step.

## 5. Cold read

Save the draft to a file if it is not one already (use the scratchpad). Then spawn one fresh reader:

- Use the `coldread:cold-reader` subagent. It starts without any CLAUDE.md, so it knows only what the reader line tells it. If it is not available, use a general-purpose subagent and tell it to read `${CLAUDE_PLUGIN_ROOT}/agents/cold-reader.md` first and follow it exactly. That reader still loads CLAUDE.md, so say so in the report.
- Never run the reader as a fork: a fork inherits this whole session, which is exactly what the reader must not have.
- Give it only the file path and the reader line from the brief. Never pass session context, a glossary, your summary or what you meant.

Then:

1. **Compare its section 1 with your Must, and show both in the report.** This is the real test. Quote your Must and the reader's sentence side by side, so the user judges the match instead of taking your word for it. If the reader understood what is asked of them, the text works, even with a few minor findings left.
2. **Fix every `[blocker]`.** Fix a `[minor]` only when the fix is small and does not add length to the main part.
3. **Run a second reader only if** its summary did not match the Must, or `ask_up_front` was `no`, or fixing the blockers changed the structure. Use a new reader, because one that saw the earlier draft already knows your terms. Never run a third.

Skip the cold read for texts under 40 words.

## 6. Report

Give the user the final text, then:

- one line of evidence, for example `Cold read: 1 round, blockers 3 → 0 · Vale 0 warnings · main part 236/280 words`;
- the ask check: `Must: "approve the retry change" · reader: "approve raising export retries to five"`;
- the facts you removed rather than moved, one line each, or "none";
- when rewriting, the facts you corrected or added, one line each, or "none";
- anything still open after the cold read.

If the text still has word-level AI tics that Vale does not catch ("not X but Y", rule-of-three lists, manufactured punchlines), an optional word-level pass can follow, such as [humanizer](https://github.com/blader/humanizer) if the user has it installed. It never replaces the steps above, and if it changes more than wording, run Vale again. Humanizer's word lists are English, so on a text in another language use it only for those structural tics.
