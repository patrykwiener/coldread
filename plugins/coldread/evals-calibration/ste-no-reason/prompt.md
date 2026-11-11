---
description: Judge calibration for write-rewrite-ste-en/strength-kept; a hand-labelled text, expected FAIL, the reason for the failure is no longer given as the reason.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to rewrite.md, with no changes, then reply "done".

-----
The nightly export job may fail when the storage API is slow. The job tries again only two times.

If the job fails, the on-call engineer should start it again manually. It is safe to start the job again, because each run writes over the file from the previous run.

Do not start the job again during the backup window, from 01:00 to 02:00 UTC. Exception: if the export is already more than one hour late, you can start it again during the backup window.

The script suggests the `--resume` option. This option skips the files that the job already wrote.

Teams that want a copy of the raw data can ask the data platform team for it.

We think that two retries are not sufficient. But we did not measure how frequently the storage API is slow.
-----
