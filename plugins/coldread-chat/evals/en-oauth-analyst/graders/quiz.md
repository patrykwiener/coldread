---
type: llm
---

Act as a reader with no authentication background who has only the final response. Try to answer:
1. Does the BI tool see the analyst's password? Expected: no.
2. What does the BI tool get at the end? Expected: a token, a temporary pass that lets it read the warehouse.
3. What does PKCE add, in plain terms? Expected: a one-time secret that proves the app finishing the flow is the one that started it, so a stolen code is useless.
PASS if the response lets this reader answer all three correctly.
FAIL if any answer is missing or only implied.
