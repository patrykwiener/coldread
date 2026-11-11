---
description: Rewrite of a short ops note in ASD-STE100, saved to rewrite.md; checks that every requirement, recommendation, option, possibility, reason, exception and limit keeps its strength. Written before any run. Needs --allow-tools Write Bash.
tags: [write, en, rewrite, ste, holdout]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Rewrite this in ASD-STE100 and save the result to rewrite.md:

The nightly export job may fail when the storage API is slow, because it retries only twice. If it fails, the on-call engineer should rerun it by hand. A rerun is safe, since each run overwrites the file from the run before. Do not rerun it while the backup window is open, from 01:00 to 02:00 UTC, unless the export is already more than an hour late. The script suggests `--resume`, which skips the files that are already written. Teams that want a copy of the raw data can ask the data platform team for one. We think two retries are too few, but we have not measured how often the storage API is slow.
