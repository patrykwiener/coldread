---
description: Judge calibration for the rewrite invented-claims grader; a hand-labelled text, expected PASS.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to rewrite.md, with no changes, then reply "done".

-----
After the migration, the reconciliation pipeline uses the idempotency layer to remove duplicate records across the 3 ingest shards. Idempotency means that processing the same record twice has the same effect as processing it once. As a result, p95 latency fell by 37%, from 820 ms to 517 ms, and the 0.4% duplicate rate seen before the 2 June cutover is gone.
-----
