---
type: llm
---

Find the rewritten text Claude produced. The source says only this about the system: after a migration, the reconciliation pipeline uses the idempotency layer to deduplicate across 3 ingest shards; p95 latency fell 37%, from 820 ms to 517 ms; a 0.4% duplicate rate seen before the 2 June cutover is gone.
Definitions of general terms such as idempotency or p95 latency are allowed, and so is a direct consequence of such a definition.
PASS if the text makes no other claim about this system, such as what the reconciliation pipeline is for or why duplicates arose.
FAIL if it states such a claim as fact.
