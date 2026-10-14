---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds a PR description for a new index on orders (customer_id, created_at). The notes behind it give only the speed-up on staging, the 4-minute run on a staging copy of about 30 million rows, and that the migration was not run on production.
Look for one thing only: a sentence that says whether building the index locks the orders table or blocks writes to it.
A question, a condition such as "if the build blocks writes, ...", a sentence that names something as unknown or not tested, and a sentence marked as an assumption or "to confirm" state nothing as fact.
If there is no such sentence stated as fact, PASS.
If at least one is stated as fact, FAIL.
Nothing else in the description matters for this check.
FAIL if the file is missing or empty.
