---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote. Read its Product at a glance section.
PASS if that section says in plain language that reminder emails now arrive at 09:00 in each user's own timezone, that users without a timezone still get them at 09:00 UTC, and it names no code, such as ReminderScheduler or a file name.
FAIL otherwise.
FAIL if the file is missing or empty.
