---
description: On-call runbook for a queue backlog alert, saved to runbook.md, from notes that also hold the queue's migration history and two open design questions; checks that the runbook keeps alert, impact and mitigation in that order and moves the design material out. Needs --allow-tools Write Bash.
tags: [write, en, structure]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the on-call doc for the ExportQueueBacklog alert and save it to runbook.md. The reader is an on-call backend engineer paged at night who has never touched the export service. My notes: the alert fires when the export queue holds more than 5000 pending jobs for 10 minutes. It pages, because customers' CSV exports are delayed; past 20000 jobs exports start timing out after 30 minutes. Check first: `exportctl queue stats` shows pending jobs per worker pool, and the Grafana board "Export queue" shows whether workers are processing at all. To mitigate: 1) if workers are stuck, run `exportctl workers restart --pool default`; 2) if one tenant floods the queue, pause it with `exportctl tenant pause <id>`; 3) if the database is slow, scale workers down to 4 with `exportctl workers scale 4` so they stop competing for locks; 4) if none of this helps within 15 minutes, escalate to the data platform channel. History: the queue lived in Redis until release 4.2; we moved it to a Postgres table because Redis evicted jobs under memory pressure and we lost about 300 exports in March. Open questions for later: should we shard the queue per region? Should we cap pending exports per tenant?
