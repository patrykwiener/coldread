<!-- These anchors are invented examples. They show the register and opening to aim
for. To use texts from your own project instead, put 2-3 of them in
.coldread/examples-en.md in that repository once they passed the cold read. -->

# Style anchors

Match the register, density and opening of these examples, not their topics.

## Handoff note

> The fix for duplicate invoices (#412) merged in PR #88 and shipped in release 2.4.0. What is left is a cleanup of the duplicates already sent, and one open question for the finance team. I found nothing showing the cleanup was run, so treat it as not done.
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

## Review comments

> **Fix:** Page numbers start at 1, so `offset = page * page_size` skips the first 20 results on page 1. Users never see the newest orders.
> ```suggestion
>     offset = (page - 1) * page_size
> ```

> **Question:** With this fix, `?page=0` gives a negative offset. Should it return page 1, as it does today, or a 400 error?

> The new filter parameters read well. Before merging, please fix the offset and decide what page 0 returns. One follow-up: a test that asks for page 1 and finds the newest order on it.

Why it works: each comment holds one problem, why it matters and the fix, in at most three sentences, and the code change is a suggestion the author can apply. The summary says what is good, what blocks the merge and the one follow-up. Style preferences and the reviewer's evidence stay out.

## Explainer opening

> A password reset link lets a user who forgot their password set a new one without contacting support. This note shows what happens between the click on "Forgot password" and the new password working, for anyone who answers support tickets about it.
>
> **Reset token.** A random string that proves the link came from us. Example: `k3J9…` in `https://app.example.com/reset?token=k3J9…`. It lives in the `password_resets` table, one row per request.
>
> **Expiry.** How long a token works: 30 minutes. A link from a request made at 10:00 and opened at 10:31 shows "This link has expired".
>
> **One reset, step by step.** At 10:00 Ana asks for a reset. We store a token for her account and email her the link. At 10:12 she opens it and sets a new password, and we mark the token as used, so the same link fails if she clicks it again.

Why it works: two sentences say what the thing does and who the note is for. Each term gets one sentence, one example with values, and where it lives. Then one invented case runs from start to end, so the reader sees how the terms fit together.
