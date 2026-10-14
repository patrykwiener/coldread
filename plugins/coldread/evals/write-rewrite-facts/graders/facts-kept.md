---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds the rewrite Claude wrote. Check only whether the original facts survive; ignore anything added.
PASS if all of these are present and unchanged: 3 ingest shards; p95 latency down 37%, from 820 ms to 517 ms; a 0.4% duplicate rate before the cutover on 2 June, which is now gone.
FAIL if any of them is missing or changed.
FAIL if the file is missing or empty.
