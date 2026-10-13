---
type: llm
focus:
  source: file
  path: design.md
---

The file holds the design doc Claude wrote.
PASS if it keeps all of these: a 50-image album takes about 40 seconds and blocks a web worker; the goals of uploads under 2 seconds and thumbnails within a minute; the non-goal of keeping thumbnail sizes; the queue and a thumbnail service with 3 workers writing to the same bucket; both rejected options with their reasons; the approval for 3 containers and about 6 GB of memory.
FAIL if any of them is missing or changed.
