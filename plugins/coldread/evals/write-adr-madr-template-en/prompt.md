---
description: ADR in the team's own MADR template, saved to docs/decisions/0012-upload-storage.md; checks that the repository's template wins over the skill's default ADR sections and that the options and reasons survive. Needs --allow-tools Write Bash.
tags: [write, en, structure, adr]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the ADR for where we store user uploads and save it to docs/decisions/0012-upload-storage.md. Readers: developers on the team now and later. Use our template exactly, which is MADR:

# {short title of solved problem and solution}
## Context and Problem Statement
## Considered Options
## Decision Outcome
### Consequences
## Pros and Cons of the Options

My notes: users upload PDFs and images up to 200 MB, about 40 GB a month in total. Today the files sit in a Postgres bytea column, and the nightly backup has grown to 6 hours. Options: keep them in Postgres; an NFS share mounted on every app server; S3-compatible object storage with presigned URLs. Chosen: object storage, because the backup shrinks to the database rows only and the app servers stop streaming files. NFS was rejected because the ops team cannot run it highly available. Postgres was rejected because of the backup time. Downside: we must move about 900 GB of existing files, and links to files stop working if a presigned URL expires, after 15 minutes.
