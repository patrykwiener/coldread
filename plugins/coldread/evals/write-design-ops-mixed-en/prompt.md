---
description: Design doc for a thumbnail service, saved to design.md, from notes that mix the design with step-by-step on-call instructions; a held-out case, written before any run of it. Needs --allow-tools Write Bash.
tags: [write, en, structure, design, holdout]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the design doc for moving thumbnail generation out of the web app and save it to design.md. Readers: the backend team and the infrastructure lead, who approve it before we start. My notes: the web app generates thumbnails inside the upload request, so an upload of a 50-image album takes about 40 seconds and blocks a web worker the whole time. Goal: uploads return in under 2 seconds, and thumbnails appear within a minute. Not a goal: changing the thumbnail sizes. Design: the upload stores the original and puts a job on a queue; a new thumbnail service with 3 workers takes jobs and writes thumbnails to the same bucket. Rejected: generating thumbnails in the browser, because old phones would take minutes; a bigger web worker pool, because it only moves the bottleneck. Needs the infrastructure lead's approval for 3 more containers, about 6 GB of memory in total. For on-call once it runs: if thumbnails stop appearing, run `thumbctl queue depth`; if depth grows, run `thumbctl workers restart`; if one image keeps failing, run `thumbctl job drop <id>`.
