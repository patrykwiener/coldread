---
description: Rewrite of one dense, jargon-heavy sentence for a named reader, saved to rewrite.md; every number must survive and nothing may be added. Needs --allow-tools Write Bash.
tags: [write, en, rewrite]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Rewrite this so a junior developer who joined the team last week understands it, and keep every fact: "Post-migration, the reconciliation pipeline leverages the idempotency layer to ensure robust deduplication across the 3 ingest shards, yielding a 37% reduction in p95 latency (from 820 ms to 517 ms) and eliminating the 0.4% duplicate rate we observed before the 2 June cutover." Save the rewrite to rewrite.md.
