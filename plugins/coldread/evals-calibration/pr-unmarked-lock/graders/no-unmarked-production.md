---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds a PR description for a new index on orders (customer_id, created_at). The notes behind it give only the speed-up on staging, the 4-minute run on a staging copy of about 30 million rows, and that the migration was not run on production.
A question, a sentence that names something as unknown or not tested, and a sentence marked as an assumption or "to confirm" state nothing as fact; ignore them.
PASS unless the description states as fact how long the migration will take on production, that production is about the same size as the staging copy, or that running it on production is safe.
FAIL if it states any of these as fact.
