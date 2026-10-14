---
type: llm
focus:
  source: file
  path: next-session.md
---

The file holds a prompt for a new agent session.
PASS if it presents the 15-minute link expiry and the batch of 1,000 files as decisions already made, which the session should not reopen.
FAIL if it presents them as open, or only as plain facts without saying they are settled.
FAIL if the file is missing or empty.
