---
type: llm
focus:
  source: file
  path: doc/adr/0007-job-system.md
---

The file holds an ADR about running background jobs from a Postgres table instead of RabbitMQ. The notes behind it give no measurement of database load.
That job traffic sends queries or reads and writes to the database follows from keeping jobs in a table; it is allowed as fact.
Look for one thing only: a sentence that states how much load the jobs add, or what that load does to the database or the application, for example that it is significant, small, or slows other queries.
If there is no such sentence, PASS.
If every such sentence is marked as an assumption, not measured, or "to confirm", PASS.
If at least one such sentence is not marked, FAIL.
Nothing else in the ADR matters for this check.
