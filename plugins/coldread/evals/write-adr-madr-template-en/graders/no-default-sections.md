---
type: regex
target:
  source: file
  path: docs/decisions/0012-upload-storage.md
pattern: '^#{2,3} (?:Context|Decision|Status)\s*$'
flags: m
match: not_contains
---
