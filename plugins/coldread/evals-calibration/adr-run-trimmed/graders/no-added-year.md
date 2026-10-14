---
type: regex
target:
  source: file
  path: doc/adr/0007-job-system.md
pattern: '\b\d{1,2}\s+[A-Z][a-z]+,?\s+(?:19|20)\d{2}\b(?!\s*\((?:to confirm|do potwierdzenia)\))'
match: not_contains
---
