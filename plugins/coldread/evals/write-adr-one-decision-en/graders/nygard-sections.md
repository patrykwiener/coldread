---
type: regex
target:
  source: file
  path: doc/adr/0007-job-system.md
pattern: '^#{2,3} Context\b[\s\S]*^#{2,3} Decision\b[\s\S]*^#{2,3} Consequences\b'
flags: m
match: contains
---
