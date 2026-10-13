---
description: Review comments in the user's own style, which differs from the skill's default shape; checks that the user's style wins, the fix and the test are asked for, and the nice-to-have stays out. Needs --allow-tools Write Bash.
tags: [write, en, review, voice]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write my review comments for PR #521 and save them to review.md, each comment under a line that names its file and line in backticks, such as `billing/invoice.py:88`; I post them myself. This is the How I write note from my CLAUDE.md: "Review comments: one or two plain sentences, never over 50 words. No labels such as Fix: or nit:, no bold, no headings or lists. Open on the concrete thing in backticks and what it does, and end on a question, such as 'wdyt?' or 'Split it out?'." My notes: (1) billing/invoice.py line 88 rounds each line total with `round(total, 2)`, which rounds an exact half to the even neighbour, so 10.125 becomes 10.12 and the customer is charged a cent too little; it should use `Decimal` with `ROUND_HALF_UP`. (2) billing/tests/test_invoice.py has no case for a total whose third decimal is 5. (3) Not for this PR: the module could use type hints.
