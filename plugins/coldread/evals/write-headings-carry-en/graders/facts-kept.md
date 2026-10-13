---
type: llm
focus:
  source: file
  path: design.md
---

The file holds the design doc Claude wrote.
PASS if it keeps all of these: about 1500 requests per second from the import; p99 from 300 ms to 4.2 s; the goal of p99 under 500 ms; 200 requests per second with bursts to 400; HTTP 429 with Retry-After; the reason each rejected option was rejected; about 30 MB in the shared Redis cluster.
FAIL if any of them is missing or changed.
