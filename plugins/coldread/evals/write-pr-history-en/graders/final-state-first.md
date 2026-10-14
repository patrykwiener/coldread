---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote.
PASS if its first two sentences say that the CSV export now streams rows instead of building the file in memory, or that large exports no longer time out, and the description does not walk through the two abandoned attempts in the order they were tried.
FAIL if it opens with the history, or tells the attempts as a story.
FAIL if the file is missing or empty.
