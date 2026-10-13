---
description: Judge calibration for the rewrite invented-claims grader; a clean rewrite saved to the file and a report that raises open questions in the reply, expected PASS.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the first pair of dashed lines to rewrite.md, with no changes. Then reply with exactly the text between the second pair of dashed lines, and nothing else.

-----
After the migration, the reconciliation pipeline uses the idempotency layer to remove duplicate records across the 3 ingest shards. Idempotency means that processing the same record twice has the same effect as processing it once. As a result, p95 latency fell by 37%, from 820 ms to 517 ms, and the 0.4% duplicate rate seen before the 2 June cutover is gone.
-----

-----
**What I added:** the definition of idempotency, its general meaning, not checked against your system.

**Questions the original leaves open:** Is the migration the same event as the 2 June cutover? Why did removing duplicates make the pipeline faster? What is the 0.4% a share of, records or batches?
-----
