---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds a rewrite of this source: "Post-migration, the reconciliation pipeline leverages the idempotency layer to ensure robust deduplication across the 3 ingest shards, yielding a 37% reduction in p95 latency (from 820 ms to 517 ms) and eliminating the 0.4% duplicate rate we observed before the 2 June cutover."
Ignore every sentence that is marked in the text as an assumption, not verified, or to be confirmed.
The source does not say what the reconciliation pipeline is for or how the shards are run.
PASS unless the rewrite says what the reconciliation pipeline does beyond removing duplicates, such as checking or matching records, or says how this system's shards work beyond a general definition of a shard, such as that they run in parallel or on separate servers. Saying that data comes in through the 3 ingest shards only restates their name and is allowed.
FAIL if it states such a fact about this system.
FAIL if the file is missing or empty.
