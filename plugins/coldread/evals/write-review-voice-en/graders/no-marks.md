---
type: regex
target:
  source: file
  path: review.md
pattern: '\((?:to confirm|do potwierdzenia|not verified|unverified|assumption)\)'
flags: i
match: not_contains
---
