---
type: llm
focus:
  source: file
  path: design.md
---

The file holds the design doc Claude wrote. Read only its heading lines, the lines that start with `#`, and ignore everything else.
PASS if those headings alone tell you three things: that the design is a per-tenant limit (a token bucket, or a limit per tenant), that other options were rejected, and that something needs the platform team's approval.
FAIL if any of the three can only be learned from the body text.
