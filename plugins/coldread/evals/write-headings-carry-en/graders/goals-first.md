---
type: llm
focus:
  source: file
  path: design.md
---

The file holds the design doc Claude wrote. Headings may be full sentences rather than labels such as "Goals" or "Alternatives".
PASS if the goal (no tenant can push another tenant's p99 above 500 ms) is stated before the text discusses the rejected options (one global limit, a limit per IP address).
FAIL if the goal is missing or comes only after the rejected options.
FAIL if the file is missing or empty.
