---
type: llm
focus:
  source: file
  path: docs/decisions/0012-upload-storage.md
---

The file holds the ADR Claude wrote.
PASS if it keeps all of these: uploads up to 200 MB, about 40 GB a month; the 6-hour nightly backup; all three options; object storage chosen because the backup shrinks and app servers stop streaming files; NFS rejected because ops cannot run it highly available; Postgres rejected because of the backup time; about 900 GB to move; presigned URLs that expire after 15 minutes.
FAIL if any of them is missing or changed.
FAIL if the file is missing or empty.
