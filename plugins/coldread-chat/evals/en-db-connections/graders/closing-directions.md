---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "How PgBouncer in transaction mode lets 48 threads share about 20 real connections" and "How to size `pool_size` per worker from your thread count and Postgres's limit". A subtopic phrased as an offer counts, such as "I can write the SQLAlchemy settings for your 12 workers".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Do other services or cron jobs connect to the same database? If so, the budget per API worker is smaller than 97 divided by 12."
FAIL if the ending only gives the fix, a next step or a caveat, such as "Set pool_size=2 and redeploy"; if it names only one subtopic, or only a broad area such as "more about database performance"; or if it closes with a generic offer such as "Let me know if you have questions".
