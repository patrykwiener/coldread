---
type: llm
---

The user's notes hold two independent decisions: running jobs from a Postgres table instead of RabbitMQ, and the retry policy with a dead_jobs table.
PASS if Claude wrote two ADR files, one per decision, or wrote one and told the user before or after that the notes hold two decisions and proposed a second ADR.
FAIL if one ADR records both decisions and Claude does not point this out.
