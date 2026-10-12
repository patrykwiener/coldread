---
type: llm
---

Find the rewritten text Claude produced, not Claude's report around it. The source says only this about the system: after a migration, the reconciliation pipeline uses the idempotency layer to deduplicate across 3 ingest shards, and this yields a 37% fall in p95 latency, from 820 ms to 517 ms, and removes the 0.4% duplicate rate seen before the 2 June cutover.
The source names the migration and the 2 June cutover separately. It does not say that they are the same event, when the migration happened, or what the cutover switched to.
Allowed: definitions of general terms such as idempotency, p95 latency or a shard, a direct consequence of such a definition, and saying that the deduplication or the idempotency layer brought the latency down.
PASS if the text makes no other claim about this system.
FAIL if it states another claim as fact, for example that the migration happened on 2 June or was the cutover, that the cutover switched to a new system, what the reconciliation pipeline is for, or why duplicates arose.
