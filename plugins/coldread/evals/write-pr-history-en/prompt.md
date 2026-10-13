---
description: PR description with no template, saved to pr.md, from notes that tell the story of three attempts; a held-out case that checks the document-type rules do not leak into a PR. Needs --allow-tools Write Bash.
tags: [write, en, structure, holdout]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the PR description for this change and save it to pr.md. The reviewer is a backend developer on the team. My notes: the CSV export timed out for accounts with more than 200,000 rows, because it built the whole file in memory. First I tried raising the request timeout to 5 minutes, but the load balancer cuts requests at 60 seconds. Then I tried paginating the export into several files, but support said customers want one file. Now the export streams rows to the response in chunks of 1,000 with a generator, so memory stays flat at about 30 MB. Changed: exports/csv_export.py, exports/tests/test_csv_export.py. Tests: a unit test streams 500,000 generated rows and checks the row count and the header; on staging the largest account, about 350,000 rows, exported in 48 seconds. Not tested: a client that disconnects in the middle of the download.
