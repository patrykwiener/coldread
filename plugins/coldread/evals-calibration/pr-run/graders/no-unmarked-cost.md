---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds a PR description for a new index on orders (customer_id, created_at). The notes behind it give only the speed-up on staging, the 4-minute run on a staging copy of about 30 million rows, and that the migration was not run on production.
A question, a sentence that names something as unknown or not tested, and a sentence marked as an assumption or "to confirm" state nothing as fact; ignore them.
PASS unless the description states as fact a cost of the index that the notes do not give, such as slower writes to orders, how much disk the index uses, or that the migration should run at a quiet hour.
FAIL if it states such a cost as fact.
FAIL if the file is missing or empty.
