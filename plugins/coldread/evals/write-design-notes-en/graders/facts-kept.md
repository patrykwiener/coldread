---
type: llm
focus:
  source: file
  path: status.md
---

The file holds the section Claude wrote.
PASS if it keeps all of these: at most 3 retries; waits of 2, 4 and 8 seconds; p95 from 9.1 s to 6.4 s on staging; both open questions.
FAIL if any of them is missing or changed.
