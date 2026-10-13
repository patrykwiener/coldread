---
type: regex
target:
  source: file
  path: status.md
pattern: '\bHank\b|\b(?:[Oo]r|[Aa]nd|[Aa]sks?|[Pp]ing|[Tt]ell|[Ww]ith|[Ff]rom|[Bb]y)\s+Will\b|\bWill\s+(?:or|and)\b'
match: not_contains
---
