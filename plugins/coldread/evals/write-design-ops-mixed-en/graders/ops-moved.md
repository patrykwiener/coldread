---
type: llm
---

The user's notes held, besides the main text, three on-call steps with `thumbctl` commands.
This grader reads only Claude's reply to the user; another grader checks the saved file.
PASS if the reply tells the user where that steps belongs, such as a runbook, or says that Claude wrote it to a second file.
FAIL if the reply says nothing about it.
