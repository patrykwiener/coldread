---
type: llm
focus:
  source: file
  path: pr.md
---

The file holds the PR description Claude wrote.
PASS if it keeps all of these: exports over 200,000 rows timed out; rows now stream in chunks of 1,000 and memory stays at about 30 MB; the unit test with 500,000 rows; the staging export of about 350,000 rows in 48 seconds; and, separately, that a client disconnecting mid-download was not tested.
FAIL if any of them is missing or changed.
