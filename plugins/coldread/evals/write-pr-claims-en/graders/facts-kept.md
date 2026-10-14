---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote.
PASS if it keeps all of these: the missing index on customer_id as the cause; the index on orders (customer_id, created_at); 1.2 s to 40 ms on staging for a customer with about 12,000 orders; the migration took 4 minutes on a staging copy of about 30 million rows; and, separately, that running it on production was not tested.
FAIL if any of them is missing or changed.
FAIL if the file is missing or empty.
