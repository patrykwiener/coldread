---
type: llm
focus:
  source: file
  path: review.md
---

The file holds review comments Claude wrote.
PASS if one comment says that round() turns 10.125 into 10.12 and proposes Decimal with ROUND_HALF_UP, and one comment asks for a test with a total whose third decimal is 5.
FAIL if either is missing.
FAIL if the file is missing or empty.
