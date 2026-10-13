---
description: PR description in the project's template, saved to pr.md, whose last section is for a product manager; checks section order, a plain product section and the split between tests run and not run. Needs --allow-tools Write Bash.
tags: [write, en, template]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write the PR description for this change and save it to pr.md. The reviewer reads all of it; our product manager reads only the last section. Use our PR template exactly:

## Summary
## Changes
## Tests
## Product at a glance
(Must stay the last section. Explain in plain language what changes for the user.)

My notes: reminder emails were scheduled at 09:00 UTC for everyone, so users in New York got them at 05:00 and users in Sydney at 19:00. ReminderScheduler now converts 09:00 in the user's profile timezone to UTC before queueing; users without a timezone keep 09:00 UTC. Changed: reminders/scheduler.py, reminders/tests/test_scheduler.py. Tests: unit tests for the conversion pass, including the daylight saving switch on 2 November; on staging I scheduled reminders for three test users in New York, London and Sydney and each arrived at 09:00 local time. Not tested: users whose timezone changes between scheduling and sending.
