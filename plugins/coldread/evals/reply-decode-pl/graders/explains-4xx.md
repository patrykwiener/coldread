---
type: llm
---

PASS if Claude's answer explains in plain words why 4xx errors from S3 should not be retried: they are client errors, such as a missing permission or a missing file, which the next attempt hits again, so the retries only delay the failure.
FAIL otherwise.
