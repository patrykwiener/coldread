---
type: regex
target:
  source: file
  path: pr.md
pattern: '^#{1,3} (?:Context|Decision|Consequences|Status|Goals?|Non-goals?|Alternatives considered)\s*$'
flags: m
match: not_contains
---
