---
type: regex
target:
  source: file
  path: review.md
pattern: '^(?!(?:#+[ \t]*)?`[^`\n]*`[ \t:]*$)[^\n]*[^?\s][ \t]*$(?:\n[ \t]*$|(?![\s\S]))'
flags: m
match: not_contains
---
