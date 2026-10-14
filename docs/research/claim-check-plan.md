# Plan: find out whether `write` invents claims, then stop it

The full run on 2026-10-13 failed `no-invented-claims` in 5 of 5 runs of two cases, with and without the skill. A grader that fails every run in both arms measures nothing, so this plan first checks the graders against texts with known answers, then measures, and only then changes the skill.

## Steps

1. **Calibrate the two claims graders.** Each grader judges hand-labelled texts in `plugins/coldread/evals-calibration/`: clean texts must pass, texts with an invented claim must fail, and a claim marked in the text as an assumption must pass. A grader is calibrated when every text gets its label in 3 of 3 runs, twice in a row.
2. **Measure the two cases again with the calibrated graders,** 5 runs per arm. This is the baseline for this plan.
3. **Read every failed text and sort the added claims by kind:** a general fact about a tool, a consequence the author inferred, or a recommendation. The kinds decide the rule.
4. **Change the claim check in `SKILL.md` for the kinds that fail,** then write one held-out case before running it, and measure the two cases, the held-out case and the guards.
5. **Run the full suite once,** 5 runs per arm, and record it.

## Status

| Step | Status |
|---|---|
| 1. Calibrate the graders | done: 48 of 48 judgements match their labels over two rounds |
| 2. Baseline | done: the claims grader fails 5 of 5 in both arms of both cases |
| 3. Sort the added claims | done: general tool facts, inferred consequences and recommendations; all listed in the report, none marked in the text |
| Decide the rule | done: mark claims about the user's system in the text; general tool facts only in the report |
| 4. Change the rule | done: rewrite and ADR additions now marked or gone; graders split into narrow, calibrated checks; one load grader stays uncalibrated |
| 5. Full run | done: 92% against 66% per case over 19 cases; review fixes of 2026-10-14 measured in the touched cases |
