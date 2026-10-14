---
type: llm
focus:
  source: file
  path: doc/adr/0007-job-system.md
---

The file holds an ADR about running background jobs from a Postgres table instead of RabbitMQ. The notes behind it give no recommendation for the future.
Look for one thing only: a sentence that tells the team to revisit, review or reconsider the decision later, for example if the load grows.
If there is no such sentence, PASS.
If every such sentence is marked as an assumption or "to confirm", PASS.
If at least one such sentence is not marked, FAIL.
Nothing else in the ADR matters for this check.
FAIL if the file is missing or empty.
