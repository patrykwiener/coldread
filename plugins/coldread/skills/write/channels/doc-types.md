# Kinds of documents with fixed sections

Read this when the text is one of the kinds of documents below and the repository has no template for it. Each kind has sections its readers expect, so they count as a template. Some kinds fix the names of their sections: keep those headings as they are, and let the first sentence under each carry what a heading of your own would have said, as in "Jobs live in Postgres because they must commit in the same transaction as their data" under `## Decision`. Other kinds fix only the order: keep the order, and write headings that say something. Each kind also says what does not belong in it and where that material goes instead. Such material goes to the report, as step 7 of the skill says.

## ADR, an architecture decision record

An ADR records one decision and why it was made, for readers who join later and wonder why the system works this way. The sections come from Michael Nygard's post that introduced ADRs ([Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)):

1. A title: the number and a short noun phrase, as in `# 7. Background jobs in a Postgres table`. ADRs are numbered in order, and a number is never reused.
2. `## Context`: the forces at play when the decision was made, such as the constraints, the load and the options.
3. `## Decision`: what was decided, in full sentences.
4. `## Status`: proposed, accepted, deprecated, or superseded by a later ADR, which it names.
5. `## Consequences`: what is true after the decision, including the costs and the risks, not just the gains.

One ADR holds one decision. When the notes hold more than one, write one ADR per decision. When the user named a single file, write there the decision they asked about, or the one the others depend on when they named none, and in the report name each other decision with the file you propose for it, such as `doc/adr/0008-job-retries.md`, and ask whether to write it. Keep an ADR to one or two pages. Write it in sentences and paragraphs; a list is fine for consequences that are truly parallel.

## Runbook

A runbook tells an on-call engineer how to respond to one alert, often at night and under stress. Google's SRE workbook, which calls it a playbook, says it explains the severity and impact of the alert, and gives debugging suggestions and actions to mitigate and fully resolve it ([On-Call](https://sre.google/workbook/on-call/)). The workbook also advises a team to agree on the minimal details a playbook must have, because playbook details go out of date as fast as production changes. The order is fixed, the headings are your own:

1. What the alert means: when it fires, how severe it is, and what users see.
2. What to check first, with the commands or dashboards.
3. What to do for each cause, one fix per cause, with its command.
4. When and where to escalate.

Not in a runbook: how the system came to be, why it was designed this way, and open design questions. They belong in a design doc or an ADR; the runbook may link to one in a single line.

## Design doc

A design doc asks its readers to agree on a design before it is built. Malte Ubl, who described how Google writes them, says design docs are informal and "don't follow a strict guideline for their content", but that a certain structure "has established itself as really useful" ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)). The order is fixed, but these are the contents of the sections, not their names. Each heading states what its section concludes, such as "A global limit or a per-IP limit would throttle the wrong tenants" rather than "Alternatives considered":

1. A short overview of the landscape, so readers catch up; link the detail.
2. The goals and the non-goals, the non-goals as explicit as the goals.
3. The design, from an overview down to the details.
4. The designs that would reasonably have reached similar outcomes, and why each lost.
5. Concerns that cut across the design, such as security, privacy and observability, when they apply.

What needs a decision or an approval also goes in the first two sentences, as everywhere in this skill. Not in a design doc: step-by-step operating instructions, which belong in a runbook. Ubl puts a large project's design doc at "around 10-20ish pages" and suggests splitting the problem when it grows far beyond that.
