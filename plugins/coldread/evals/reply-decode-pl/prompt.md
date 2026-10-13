---
description: A teammate's review comment with a ticket label the user does not know; checks that /coldread:reply fires, says first what she asks, does not invent the ticket and drafts a Polish reply.
tags: [reply, pl]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Dostałem taki komentarz do mojego PR od Ani: „LGTM poza jednym: w `retry_upload` nadal łapiesz gołe `Exception`, więc 4xx z S3 też idą w backoff. Zrobisz to w tym PR czy osobny ticket jak przy PAY-212?" O co jej chodzi i co mam odpisać? Mój PR dodaje ponawianie uploadu do S3 w `retry_upload()`: 5 prób, przerwy od 2 do 32 s.
