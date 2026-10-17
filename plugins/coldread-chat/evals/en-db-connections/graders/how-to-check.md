---
type: llm
---

Look for one thing only: a way for the user to confirm the cause on their own system.
PASS if the final response says how to check that the pools really use up the connection slots, for example by counting connections with `SELECT count(*) FROM pg_stat_activity` while the error occurs, or by comparing that count with `max_connections` minus the reserved slots.
FAIL if it states the cause and the fix but gives no way to check the cause.
