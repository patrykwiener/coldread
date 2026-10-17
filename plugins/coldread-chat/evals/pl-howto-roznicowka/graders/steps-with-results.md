---
type: llm
---

Look for one thing only: whether the steps say what the user should see.
PASS if the final response gives numbered steps for the test, and every step except at most one says what the user should see or hear after it, for example "dźwignia różnicówki opada w dół i gaśnie światło w łazience" after pressing T.
FAIL if there are no numbered steps, or if two or more steps say only what to do.
