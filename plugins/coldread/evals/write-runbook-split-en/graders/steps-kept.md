---
type: llm
focus:
  source: file
  path: runbook.md
---

The file holds the runbook Claude wrote.
PASS if it keeps all of these: the 5000 jobs for 10 minutes threshold; that exports time out after 30 minutes past 20000 jobs; `exportctl queue stats` and the "Export queue" board; the three fixes with their commands (`exportctl workers restart --pool default`, `exportctl tenant pause <id>`, `exportctl workers scale 4`); escalation to the data platform channel if nothing helps within 15 minutes. The escalation has no command.
FAIL if any of them is missing or changed.
FAIL if the file is missing or empty.
