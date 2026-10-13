---
type: regex
target:
  source: file
  path: pr.md
pattern: '^## Summary\s*$[\s\S]*^## Changes\s*$[\s\S]*^## Tests\s*$[\s\S]*^## Product at a glance\s*$'
flags: m
match: contains
---
