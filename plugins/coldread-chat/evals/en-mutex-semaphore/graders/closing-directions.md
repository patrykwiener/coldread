---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "How a read-write lock lets many readers in but only one writer, with a cache example" and "How two mutexes cause a deadlock, step by step, and the lock-ordering rule that prevents it". A subtopic phrased as an offer counts, such as "I can show both in Python's `threading` module".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Are you protecting shared data inside one process, or limiting calls to an outside service? The first calls for a mutex, the second for a semaphore."
FAIL if the ending only sums up or adds a remark or a table about the topic itself, such as "A connection pool's maximum size acts as a semaphore"; if it names only one subtopic, such as the single offer "If you tell me which language you use, I can show the idiomatic versions"; if it names only a broad area such as "concurrency in general"; or if it closes with a generic offer such as "Let me know if you have questions".
