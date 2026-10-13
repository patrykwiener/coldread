---
type: regex
target:
  source: file
  path: design.md
pattern: '^#{2,4} (?:Overview|Introduction|Background|Misc(?:ellaneous)?|Notes|Summary|Discussion|Proposal|Design|Solution|Approach)\s*$'
flags: m
match: not_contains
---
