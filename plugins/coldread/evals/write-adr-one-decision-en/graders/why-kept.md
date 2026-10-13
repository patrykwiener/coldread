---
type: llm
focus:
  source: file
  path: doc/adr/0007-job-system.md
---

The file holds the first ADR Claude wrote, about running jobs from a Postgres table instead of RabbitMQ.
PASS if it keeps both reasons: the jobs must commit in the same transaction as the data they change, and the team did not want to run another broker for about 50 jobs per second.
FAIL if either reason is missing or changed.
