---
type: llm
focus:
  source: file
  path: status.md
---

The file holds the section Claude wrote.
PASS if the section says what holds until each open question is settled: corrupted uploads are not retried, and the global cap of 3 retries applies. It must also say that a week of production logs would settle the second question.
FAIL if either default or the production logs are missing.
