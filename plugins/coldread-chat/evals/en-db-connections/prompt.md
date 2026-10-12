---
description: Harder English case. A diagnosis where models tend to list many possible causes instead of the one the numbers show.
tags: [chat, en, why, hard]
max_turns: 3
---

After today's deploy our API logs this many times: `psycopg2.OperationalError: FATAL: remaining connection slots are reserved for non-replication superuser connections`. Setup: 12 gunicorn workers with 4 threads each; every worker has its own SQLAlchemy pool with pool_size=10 and max_overflow=0. Postgres has max_connections=100. Before the deploy we ran 2 workers. Why does this happen?
