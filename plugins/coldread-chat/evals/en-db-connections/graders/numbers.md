---
type: llm
---

PASS if the response computes the connections the app can open as 12 workers × a pool of 10 = 120, because threads in one worker share its pool, and compares that with the limit of 100, or 97 after the slots reserved for superusers.
FAIL if these numbers are missing or wrong, for example 12 × 4 × 10 = 480.
