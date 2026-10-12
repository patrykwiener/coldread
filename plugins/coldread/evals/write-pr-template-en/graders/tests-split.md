---
type: llm
---

Find the Tests section of the PR description.
PASS if it says what ran and its result (the unit tests pass; on staging, reminders for test users in three cities arrived at 09:00 local time) and, separately, that a timezone change between scheduling and sending was not tested.
FAIL if the untested case is missing or the text implies everything was tested.
