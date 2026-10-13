---
type: llm
focus:
  source: file
  path: doc/adr/0007-job-system.md
---

The file holds the first ADR Claude wrote. The user's notes say only this about it: background jobs run from a Postgres table with SELECT ... FOR UPDATE SKIP LOCKED instead of RabbitMQ; the jobs must commit in the same transaction as the data they change; the team did not want to run another broker for about 50 jobs per second; the decision was accepted on 3 September.
Read the ADR sentence by sentence. A sentence is allowed when it does one of these:
- restates or combines facts from the notes, such as "A job and the data it changes commit together" or "There is no separate broker to run";
- says what SELECT ... FOR UPDATE SKIP LOCKED does;
- is marked in the text as an assumption, not verified, or to be checked.
A sentence is new information when it adds something the notes do not give about this system, its tools, its costs or its future, such as "Job traffic adds load to the main database", "A broker such as RabbitMQ cannot join a Postgres transaction" or "Revisit this decision if the load grows".
PASS if no sentence is new information without such a mark.
FAIL if at least one is.
