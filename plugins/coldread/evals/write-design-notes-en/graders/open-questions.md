---
type: llm
---

Find the section Claude wrote, not Claude's notes to the user before or after it.
PASS if the section says what holds until each open question is settled: corrupted uploads are not retried, and the global cap of 3 retries applies. It must also say that a week of production logs would settle the second question.
FAIL if either default or the production logs are missing.
