---
description: A prompt for a new agent session from the day's notes; checks the user's words verbatim, the stop before the real run, and the facts, decisions and trap carried over. Needs --allow-tools Write Bash.
tags: [write, en, prompt]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Give me a prompt for a new session that will finish this work tomorrow, and save it to next-session.md. Today we moved invoice PDFs to S3 behind `InvoiceStore` on the branch feat/invoice-s3, which is not merged. Done: `InvoiceStore.put` and `InvoiceStore.get`, and their unit tests pass. Left: run `scripts/migrate_pdfs.py --dry-run` against the staging copy and compare its count with `SELECT count(*) FROM invoices WHERE pdf IS NOT NULL`, which should return 1,204,331; then, only after I approve, run it without `--dry-run`. Decided today: download links expire after 15 minutes, agreed with the product manager, and the migration moves 1,000 files per batch. Trap: the staging database needs the VPN, and without it psql hangs instead of failing. In my own words: „dokończ migrację, ale niczego nie odpalaj na stagingu bez mojej zgody".
