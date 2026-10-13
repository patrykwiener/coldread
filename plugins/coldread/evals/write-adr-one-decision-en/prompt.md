---
description: ADR request whose notes hold two independent decisions, saved to doc/adr/0007-job-system.md; checks that Claude writes or proposes one ADR per decision, and that the first ADR has Context, Decision and Consequences in order and a Status, keeps its reasons and states no claim the notes do not support. Needs --allow-tools Write Bash.
tags: [write, en, structure, adr]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write an ADR for these decisions and save it as doc/adr/0007-job-system.md. Our ADRs are numbered, and 0007 is the next free number. The readers are developers who join the team later and want to know why the job system works this way. My notes: we run background jobs from a Postgres table with SELECT ... FOR UPDATE SKIP LOCKED instead of RabbitMQ, because the jobs must commit in the same transaction as the data they change, and we did not want to run another broker for about 50 jobs per second. Accepted on 3 September. Separately, failed jobs now retry 5 times with exponential backoff from 1 to 16 seconds, then move to a dead_jobs table that on-call reviews each morning; before this, a failed job retried forever and blocked its queue. Accepted on 10 September.
