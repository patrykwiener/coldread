---
type: llm
---

Find the PR description Claude wrote.
PASS if it keeps all of these: PDFs move from Postgres to S3; the invoices table drops from 180 GB to under 10 GB; the nightly backup drops from 4 hours to about 20 minutes, measured on staging; links expire after 15 minutes.
FAIL if any of them is missing or changed.
