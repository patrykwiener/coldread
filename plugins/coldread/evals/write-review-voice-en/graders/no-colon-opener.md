---
type: regex
target:
  source: file
  path: review.md
pattern: '(?:^|(?<=[.!?] ))[^\s:`{}\[\]#*>|-][^\s:.!?`{}\[\]]*[ \t][^:.!?`\n{}\[\]]{0,58}:[ \t]'
flags: m
match: not_contains
---
