---
type: regex
target:
  source: file
  path: status.md
pattern: '\b6(?:th)?\s+Oct(?:ober)?\b|\bOct(?:ober)?\s+6(?:th)?\b'
flags: i
match: not_contains
---
