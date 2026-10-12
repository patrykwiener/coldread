---
description: Status and open-questions section of a design doc, from notes with a local file path, a dated re-check and decisions nobody owns. Needs --allow-tools Write Bash.
tags: [write, en, design]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Turn my notes into the "Status and open questions" section of our design doc for the thumbnail retry change. The reader is a backend developer on the team who did not work on this. My notes: thumbnail jobs now retry at most 3 times, waiting 2, 4 and 8 seconds, merged in commit 4f2a9c1. Benchmarks are in /Users/sam/scratchpad/bench-thumbs.md: p95 time to a finished thumbnail went from 9.1 s to 6.4 s on staging. I re-checked the staging numbers on 6 October and they still hold. Open: should a corrupted upload be retried at all? Until someone decides, corrupted uploads are not retried. Hank or Will could decide; nobody has picked it up. Open: do we need a per-tenant retry cap? Nobody knows yet; a week of production logs would tell. Until then the global cap of 3 applies.
