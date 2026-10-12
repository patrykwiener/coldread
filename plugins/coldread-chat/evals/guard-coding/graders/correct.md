---
type: llm
focus: { source: file, path: chunk.py }
---

Read the code.
PASS if chunk([1, 2, 3, 4, 5], 2) returns [[1, 2], [3, 4], [5]], chunk([], 3) returns [], and chunk([1], 0) raises ValueError.
FAIL if any of these would behave differently.
