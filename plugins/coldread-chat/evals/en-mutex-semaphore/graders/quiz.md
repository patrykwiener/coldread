---
type: llm
---

Act as a backend developer with no concurrency background who has only the final response. Try to answer:
1. How many holders can a mutex have at once? Expected: one.
2. What does a semaphore's count mean? Expected: how many holders may enter at once.
3. Name one situation where a semaphore fits and a mutex does not. Expected: limiting access to N identical resources, such as N connections.
PASS if the response lets this reader answer all three correctly.
FAIL if any answer is missing or only implied.
