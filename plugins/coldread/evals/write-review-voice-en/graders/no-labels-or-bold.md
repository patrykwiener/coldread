---
type: regex
target:
  source: file
  path: review.md
pattern: '\*\*|^\s*(?:[-*>]\s*)?(?:Fix|Question|Nit|nit|Suggestion|Issue|Blocking|Non-blocking)\s*:'
flags: m
match: not_contains
---
