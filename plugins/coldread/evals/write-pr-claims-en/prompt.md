---
description: PR description for a new database index, saved to pr.md, from notes that give the speed-up but no side effects; a held-out case for the claim rule, written before any run of it. Needs --allow-tools Write Bash.
tags: [write, en, claims, holdout]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the PR description for this change and save it to pr.md. The reviewer is a backend developer on the team. My notes: the order history page was slow for customers with many orders, because the query filtered orders by customer_id without an index. This PR adds a migration that creates an index on orders (customer_id, created_at). On staging, the query for a customer with about 12,000 orders went from 1.2 s to 40 ms. The migration ran on a staging copy of the orders table, about 30 million rows, in 4 minutes. Changed: migrations/0142_orders_customer_index.py. Not tested: running the migration on production.
