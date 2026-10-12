---
description: PR description from notes, with one trade-off that needs the reviewer's approval. Needs --allow-tools Write Bash.
tags: [write, en]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the PR description for this change; the reader is the reviewer. My notes: invoice PDFs move from a Postgres bytea column to S3 behind InvoiceStore.put/get. scripts/migrate_pdfs.py moves the existing 170 GB in batches of 1,000. The invoices table drops from 180 GB to under 10 GB, and the nightly backup from 4 hours to about 20 minutes, measured on staging. Trade-off that needs approval: download links become presigned URLs that expire after 15 minutes instead of permanent links. Tested: unit tests for InvoiceStore and a migration dry run on a staging copy. Not tested: the migration at production volume.
