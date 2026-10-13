---
type: llm
focus:
  source: file
  path: runbook.md
---

The file holds a Polish runbook Claude wrote.
PASS if it keeps all of these: the 5-minute threshold for the oldest unprocessed webhook; orders shown as unpaid; the operator retrying after 30 minutes; `payctl webhooks lag` and the "Payment webhooks" board; the three fixes with their commands (`payctl worker restart`, `payctl webhooks skip <id>` with the failed_webhooks table, `payctl worker scale 2`); escalation to the payments team channel after 20 minutes.
FAIL if any of them is missing or changed.
