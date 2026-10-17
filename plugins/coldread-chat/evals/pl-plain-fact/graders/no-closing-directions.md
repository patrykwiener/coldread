---
type: llm
---

Look only at how the final response ends.
PASS if it ends with the answer itself or with one practical point about the user's own setup, such as how to check which port their server really uses (`SHOW port;`) or where the port is set (`postgresql.conf`). A paragraph that already answers a likely next question, such as how to change the port, also passes.
FAIL if it ends with a list of subtopics to explore next, such as connecting from another computer or securing remote access, or with an offer to explain more, such as "Jeśli chcesz, opiszę, jak zmienić port".
