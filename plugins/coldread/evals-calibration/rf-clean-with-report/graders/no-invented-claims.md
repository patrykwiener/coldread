---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds the rewrite Claude wrote. The source says only this about the system: after a migration, the reconciliation pipeline uses the idempotency layer to deduplicate across 3 ingest shards; this yields a 37% fall in p95 latency, from 820 ms to 517 ms, and removes the 0.4% duplicate rate seen before the 2 June cutover. The source names the migration and the 2 June cutover separately.
Read the rewrite sentence by sentence. A sentence is allowed when it does one of these:
- restates or combines facts from the source, including that the deduplication or the idempotency layer brought the latency down and removed the duplicates;
- gives the general meaning of a term, such as idempotency, p95 latency or a shard;
- is marked in the text as an assumption, not verified, or to be checked.
A sentence is new information when it adds something the source does not give about this system, such as that the migration happened on 2 June or was the cutover, what the cutover switched to, what the reconciliation pipeline is for, or why duplicates arose.
PASS if no sentence is new information without such a mark.
FAIL if at least one is.
