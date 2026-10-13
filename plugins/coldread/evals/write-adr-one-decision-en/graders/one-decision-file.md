---
type: regex
target:
  source: file
  path: doc/adr/0007-job-system.md
pattern: 'dead_jobs|exponential|backoff'
flags: i
match: not_contains
---
