---
type: llm
focus:
  source: file
  path: rewrite.md
---

The file holds the rewrite Claude wrote. Its reader is a junior developer who joined the team last week.
PASS if it drops "leverages" and "robust", and says in plain words what idempotency or the idempotency layer means, for example that processing the same record twice has the same effect as processing it once.
FAIL if it keeps that jargon, or uses "idempotency" without saying what it means.
FAIL if the file is missing or empty.
