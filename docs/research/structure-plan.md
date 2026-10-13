# Plan: teach `write` to plan and check structure

`write` already makes sentences clear, but it does not pick a document type, show an outline before drafting, or check structure, so a clear text can still lose its reader. This plan adds those three things in the order below, measuring before and after each change. The sources and their verification are in [document-structure.md](document-structure.md).

## Steps

1. **Add three eval cases that test structure, and measure the current skill.** The cases are `write-runbook-split-en`, `write-headings-carry-en` and `write-adr-one-decision-en`, from the Measuring section of the research. Run them with and without the plugin and record the scores in `docs/results.md`. This run is the baseline that every later step is compared with.
2. **Add a Type line and an Outline line to the brief.** Type names the kind of document, such as runbook, ADR or how-to guide. Outline lists the planned headings in order, each with the point it carries, and the user sees it before the draft. A new `channels/doc-types.md` gives each type its sections and order. A repository template still wins. Skip the outline for texts under about 200 words.
3. **Replace the "more than four points" rule with split signals.** A text should split when it mixes two document types, serves two reader groups with different needs, records more than one decision, is longer than its type allows, or holds more than about four new points at one level. The proposal names the signal and the second document.
4. **Add a headings-only check before the cold read.** A fresh reader gets only the headings and the first sentence of each section, and retells the argument and the ask. A retelling that misses the Must or a point is fixed like a blocker.
5. **Run the suite again after steps 2 to 4** and compare with the baseline from step 1, including the older cases, so a gain on structure does not cost the older checks.
6. **Decide on `/coldread:plan-docs` only after step 5.** The command would plan a set of files (type, reader, Must and outline for each, and which facts go where) and write no prose. The research sketches it, but most of it is inference, not sourced, so it waits until the changes to `write` show an effect.

## Status

| Step | Status |
|---|---|
| 1. Eval cases and baseline | done: 64% with the skill, 50% without; see `docs/results.md`, 2026-10-13 |
| 2a. Fixed sections for an ADR | done: the ADR case went from 42% to 100%; see `docs/results.md` |
| 2b. Control case for the ADR rule | done: the team's MADR template wins in 3 of 3 runs; ADRs still add unsourced claims, a gap in the claim check |
| 2c. Runbook and design doc in `doc-types.md`, the kind of document named in the Channel line | next |
| Outline | postponed: the evals cannot measure it, and headings already pass |
| 3. Split signals | not started |
| 4. Headings-only check | not started |
| 5. Measure again | not started |
| 6. Decide on `plan-docs` | not started |
