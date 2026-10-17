---
type: llm
---

Look only at the first sentence of the final response.
PASS if it states the cause: the app can now open more connections than Postgres accepts. A sentence that names the error and gives this cause, such as "The error appears because your 12 workers can open up to 120 connections, but Postgres accepts only 97", passes, and so does the same sentence in bold.
FAIL if it opens with background, a list of possible causes, or the error restated without its cause.
