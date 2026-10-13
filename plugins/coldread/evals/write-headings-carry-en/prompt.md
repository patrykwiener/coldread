---
description: Design doc for a per-tenant rate limit, saved to design.md, from notes with a decision, two rejected options and one approval; checks that the headings alone carry the argument, that no heading is generic and that goals come before alternatives. Needs --allow-tools Write Bash.
tags: [write, en, structure, design]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write a design doc for the per-tenant rate limit and save it to design.md. The readers are the backend developers and the platform team, who review it before we build. My notes: one tenant's nightly batch import sends about 1500 requests per second to the public API, and p99 latency for every other tenant goes from 300 ms to 4.2 s while it runs. Goal: no tenant can push another tenant's p99 above 500 ms. Not a goal: billing by usage. Decision: a token bucket per tenant, kept in Redis, with 200 requests per second by default and bursts up to 400; a request over the limit gets HTTP 429 with a Retry-After header. Rejected: one global limit, because it slows every tenant when one floods; a limit per IP address, because several tenants share one NAT gateway, so they would throttle each other. Needs approval from the platform team: the buckets add about 30 MB to the shared Redis cluster.
