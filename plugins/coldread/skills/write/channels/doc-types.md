# Kinds of documents with fixed sections

Read this when the text is one of the kinds of documents below and the repository has no template for it. Each kind has sections its readers expect to find under these names, so they count as a template: keep the headings and their order as they are, and apply the rest of the skill inside each section. The first sentence under a fixed heading carries what a heading of your own would have said, as in "Jobs live in Postgres because they must commit in the same transaction as their data" under `## Decision`.

## ADR, an architecture decision record

An ADR records one decision and why it was made, for readers who join later and wonder why the system works this way. The sections come from Michael Nygard's post that introduced ADRs ([Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)):

1. A title: the number and a short noun phrase, as in `# 7. Background jobs in a Postgres table`. ADRs are numbered in order, and a number is never reused.
2. `## Context`: the forces at play when the decision was made, such as the constraints, the load and the options.
3. `## Decision`: what was decided, in full sentences.
4. `## Status`: proposed, accepted, or superseded by a later ADR, which it names.
5. `## Consequences`: what is true after the decision, including the costs and the risks, not just the gains.

One ADR holds one decision. When the notes hold more than one, write one ADR per decision. When the user named a single file, write the first decision there, and in the report name each other decision with the file you propose for it, such as `doc/adr/0008-job-retries.md`, and ask whether to write it. Keep an ADR to one or two pages. Write it in sentences and paragraphs; a list is fine for consequences that are truly parallel.
