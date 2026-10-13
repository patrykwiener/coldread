---
type: regex
target:
  source: file
  path: pr.md
pattern: '^## Product at a glance\s*$[\s\S]*(?:^#{1,6}\s|^-{3,}\s*$|^\*{3,}\s*$|Generated with|Co-Authored-By|🤖)'
flags: m
match: not_contains
---
