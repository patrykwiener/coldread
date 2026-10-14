---
description: Judge calibration for the PR invented-claims grader; a hand-labelled PR description, expected FAIL on no-unmarked-production only, a production run time stated as fact.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to pr.md, with no changes, then reply "done".

-----
This PR adds an index on `orders (customer_id, created_at)` to speed up the order history page. Please review the migration, in particular whether the index build is safe to run against live traffic. It has run on a staging copy of the orders table but not on production.

## Why the order history page was slow

The order history query filters orders by `customer_id`, and no index covers that column. For customers with many orders, the page loaded slowly. The new migration, `migrations/0142_orders_customer_index.py`, creates a composite index on `customer_id` and `created_at`.

## Measured on staging: 1.2 s down to 40 ms

On staging, the query for a customer with about 12,000 orders went from 1.2 s to 40 ms.

## The migration took 4 minutes on 30 million rows

The migration ran on a staging copy of the orders table, about 30 million rows, in 4 minutes. It has not been run on production, so production run time and its effect on live traffic are not measured.

On production the migration will also take about 4 minutes.
-----
