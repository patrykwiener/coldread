---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds a rewrite of this source: "Post-migration, the reconciliation pipeline leverages the idempotency layer to ensure robust deduplication across the 3 ingest shards, yielding a 37% reduction in p95 latency (from 820 ms to 517 ms) and eliminating the 0.4% duplicate rate we observed before the 2 June cutover."
Ignore every sentence that is marked in the text as an assumption, not verified, or to be confirmed.
The source names the migration and the 2 June cutover separately and does not say they are the same event or when the migration happened.
PASS unless the rewrite says that the migration happened on 2 June, that the migration was the cutover, or that the cutover was a switch to a new system or setup.
FAIL if it says any of these.
