---
type: regex
target:
  source: file
  path: docs/decisions/0012-upload-storage.md
pattern: '^## Context and Problem Statement\s*$[\s\S]*^## Considered Options\s*$[\s\S]*^## Decision Outcome\s*$[\s\S]*^### Consequences\s*$[\s\S]*^## Pros and Cons of the Options\s*$'
flags: m
match: contains
---
