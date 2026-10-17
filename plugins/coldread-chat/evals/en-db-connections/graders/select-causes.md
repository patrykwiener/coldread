---
type: llm
---

Count the causes the final response offers as explanations of this error, in its body and in its ending.
PASS if it names one main cause, plus at most one second cause to look at if a check rules out the first. A closing line that offers a related subtopic, such as how to size the pool or what PgBouncer does, is not a cause.
FAIL if it offers three or more candidate causes, for example the pool size, connections held open during the restart and other clients on the same database.
