---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds a rewrite of this source: "Post-migration, the reconciliation pipeline leverages the idempotency layer to ensure robust deduplication across the 3 ingest shards, yielding a 37% reduction in p95 latency (from 820 ms to 517 ms) and eliminating the 0.4% duplicate rate we observed before the 2 June cutover."
Ignore every sentence that is marked in the text as an assumption, not verified, or to be confirmed.
The source does not say why duplicates arose or how records reach the pipeline.
PASS unless the rewrite says why the duplicates arose, for example that the same record can arrive more than once in this system, that shards or retries produce repeats, or that several entry points let a record come in twice. Defining idempotency in general, such as "processing the same record twice has the same effect as processing it once", is not a cause.
FAIL if it states such a cause about this system.
FAIL if the file is missing or empty.
