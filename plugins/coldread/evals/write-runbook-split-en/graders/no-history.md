---
type: regex
target:
  source: file
  path: runbook.md
pattern: '\bRedis\b|\bevict|\b4\.2\b|\bshard'
flags: i
match: not_contains
---
