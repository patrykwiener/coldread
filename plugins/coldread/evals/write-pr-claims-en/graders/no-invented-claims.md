---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote. The user's notes say only this: the order history page was slow for customers with many orders because the query filtered orders by customer_id without an index; the PR adds a migration that creates an index on orders (customer_id, created_at); on staging the query for a customer with about 12,000 orders went from 1.2 s to 40 ms; the migration ran on a staging copy of about 30 million rows in 4 minutes; the changed file is migrations/0142_orders_customer_index.py; running the migration on production was not tested.
Read the description sentence by sentence. A sentence is allowed when it does one of these:
- restates or combines facts from the notes;
- states a general fact about Postgres or about indexes, such as that an index lets a query skip a full table scan;
- is marked in the text as an assumption, not verified, or to be confirmed.
A sentence is new information when it adds something the notes do not give about this team's system, such as that the migration locks the orders table, that writes to orders get slower, that production will take about the same time, how much disk the index uses, or that the migration should run at a quiet hour.
PASS if no sentence is new information without such a mark.
FAIL if at least one is.
