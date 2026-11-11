---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds a rewrite of the source text below into ASD-STE100, Simplified Technical English. Check only whether each numbered qualifier kept its meaning and its strength. A qualifier may be reworded, split across sentences or turned into a list item, and plainer words such as "start again" for "rerun" are fine. A qualifier is lost if it is missing, or if its strength or scope changed: a recommendation became an obligation, a possibility or a belief became a plain fact, a suggestion became an instruction, an option became a requirement, a reason is no longer given as the reason, or an exception or a limit disappeared or now applies to another action.

PASS if every qualifier kept its meaning and its strength.
FAIL if any qualifier was lost or changed.
FAIL if the file is missing or empty.

Qualifiers:
1. The job may fail when the storage API is slow: a possibility, under that condition only.
2. The reason it may fail is that it retries only twice.
3. If it fails, the on-call engineer should rerun it by hand: a recommendation, not an obligation, and only after a failure.
4. A rerun is safe because each run overwrites the file from the run before.
5. Do not rerun it while the backup window is open, from 01:00 to 02:00 UTC.
6. The exception: a rerun in the backup window is allowed if the export is already more than an hour late.
7. The script suggests `--resume`, which skips files already written: a suggestion, not an instruction.
8. Teams that want a copy of the raw data can ask the data platform team: an option, not a requirement.
9. The team thinks two retries are too few, a belief and not a fact, and has not measured how often the storage API is slow.

Source text:
"The nightly export job may fail when the storage API is slow, because it retries only twice. If it fails, the on-call engineer should rerun it by hand. A rerun is safe, since each run overwrites the file from the run before. Do not rerun it while the backup window is open, from 01:00 to 02:00 UTC, unless the export is already more than an hour late. The script suggests `--resume`, which skips the files that are already written. Teams that want a copy of the raw data can ask the data platform team for one. We think two retries are too few, but we have not measured how often the storage API is slow."
