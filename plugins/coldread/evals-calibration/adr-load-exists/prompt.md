---
description: Judge calibration for the ADR invented-claims grader; a hand-labelled ADR, expected PASS, job queries on the database stated as fact, their amount marked.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to doc/adr/0007-job-system.md, with no changes, then reply "done".

-----
# 7. Background jobs in a Postgres table

## Context

Each background job must commit in the same transaction as the data it changes. The load is about 50 jobs per second, and the team did not want to run another broker for that.

## Decision

Background jobs run from a Postgres table instead of RabbitMQ. Workers claim jobs with `SELECT ... FOR UPDATE SKIP LOCKED`, which lets each worker skip rows that another worker has locked.

## Status

Accepted on 3 September.

## Consequences

A job and the data it changes commit together, and there is no separate broker to run. Job traffic adds reads and writes to the main database. How much load it adds has not been measured.
-----
