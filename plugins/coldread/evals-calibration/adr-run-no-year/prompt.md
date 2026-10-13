---
description: Judge calibration for the ADR invented-claims grader; a hand-labelled ADR, expected PASS, a real run without the year, keeping the shared-database sentence.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to doc/adr/0007-job-system.md, with no changes, then reply "done".

-----
# 7. Background jobs in a Postgres table

## Context

Each background job must commit in the same transaction as the data it changes. Either both the job and its data changes are saved, or neither is. A message broker such as RabbitMQ cannot take part in a Postgres transaction, so it cannot give that guarantee by itself.

The load is about 50 jobs per second. We did not want to run another broker for that volume.

## Decision

Background jobs live in a Postgres table, and workers take them with `SELECT ... FOR UPDATE SKIP LOCKED`. A worker locks the job row it takes. Other workers skip locked rows instead of waiting for them, so no two workers run the same job at once. Because jobs and application data are in the same database, a job commits in the same transaction as the data it changes.

## Status

Accepted on 3 September.

## Consequences

- A job and the data it changes are committed or rolled back together.
- There is no separate broker to run, monitor or upgrade.
- Job traffic adds load to the main Postgres database (to confirm).
- If job volume grows far beyond about 50 per second, this decision may need revisiting (to confirm).
-----
