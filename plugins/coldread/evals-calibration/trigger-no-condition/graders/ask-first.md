---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote.
PASS if its first two sentences say what was fixed (invoices sent twice when the payment provider was slow) and what the reviewer should do or check. A plain request for a review, such as "Proszę o review", counts as what the reviewer should do.
FAIL otherwise.
FAIL if the file is missing or empty.
