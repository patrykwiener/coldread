---
description: Why-question where the user supplies the facts; tests answer-first and causal prose instead of a findings list.
tags: [chat, en, why]
max_turns: 3
---

Our nightly export wrote every row twice on 14 March. What I found: the job runner reclaims a job and starts it again if the job sends no heartbeat for 60 seconds. On 14 March the first run stalled for 95 seconds in a slow flush, but it did not crash and it finished. Each run generates a new batch_id, and the database skips an inserted row only if its batch_id is already stored. Why were the rows duplicated?
