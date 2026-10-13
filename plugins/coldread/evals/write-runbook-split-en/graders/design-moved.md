---
type: llm
---

The user's notes held, besides the runbook material, the history of moving the queue from Redis to Postgres and two open questions (sharding per region, a per-tenant cap).
PASS if Claude kept that material out of runbook.md and either wrote it to a second file, or told the user where it belongs instead, such as a design doc or an ADR.
FAIL if runbook.md contains it, or if Claude dropped it without telling the user.
