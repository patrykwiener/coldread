---
type: regex
target:
  source: file
  path: runbook.md
pattern: '^#{1,6} .*(?:[Ss]everity|[Ii]mpact|[Aa]lert)[\s\S]*^#{1,6} .*(?:[Cc]heck|[Dd]iagnos|[Tt]riage)[\s\S]*^#{1,6} .*(?:[Mm]itigat|[Ff]ix|[Rr]esolv)'
flags: m
match: contains
---
