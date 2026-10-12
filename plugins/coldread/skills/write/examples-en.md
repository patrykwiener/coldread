<!-- These anchors are invented examples. They show the register and opening to aim
for. Replace them with 2-3 texts from your own project once you have rewritten them
with /write and they passed the cold read. -->

# Style anchors

Match the register, density and opening of these examples, not their topics.

## Handoff note

> The fix for duplicate invoices (#412) merged on 3 March in PR #88 and shipped in release 2.4.0. What is left is a cleanup of the duplicates already sent, and one open question for the finance team. I found nothing showing the cleanup was run, so treat it as not done.
>
> **The bug.** `POST /api/invoices/send` retried on a timeout without checking whether the first attempt had reached the payment provider. When the provider was slow, customers got two identical invoices.
>
> **The fix.** Each send now carries an idempotency key built from the invoice ID, so the provider ignores a repeat. Retries are unchanged.
>
> **To do.**
> 1. Run `scripts/find_duplicate_invoices.py --since 2024-01-01` against production. It lists pairs; it changes nothing.
> 2. Ask finance whether duplicates already paid should be refunded or credited.

Why it works: the first sentence says what happened, with the ticket explained in plain words next to its number. The second says what is left. Status is checked, not assumed, and the text says so.

## PR description opening

> One thing needs your decision before merge: exports now retry five times instead of once, which can delay a failed export's error email by up to two minutes.
>
> Monthly exports failed for about one customer in fifty because the storage API drops a small share of uploads. Each failed upload now retries with a growing pause, and the export only fails after the fifth attempt. Measured on last month's run, failures fell from 41 to 0.

Why it works: the reader's decision comes first, with its cost. What changed follows in two sentences, with one measured number. There is no history of the other retry counts that were tried.

## Proposal opening

> This change moves invoice PDFs from the database to object storage, and it needs your approval for one trade-off: download links will expire after 15 minutes instead of working forever.
>
> The invoices table is 180 GB, of which 170 GB is PDF data, and nightly backups now take four hours. Moving the files out brings the table under 10 GB.

Why it works: the goal and the one decision the approver must make are in the first sentence. The problem is then stated with numbers, and nothing in it depends on a document the reader does not have.
