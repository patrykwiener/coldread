---
type: regex
target:
  source: file
  path: doc/adr/0007-job-system.md
pattern: '^#{2,3} Status\b|^[-*]? *\**Status\**:'
flags: m
match: contains
---
