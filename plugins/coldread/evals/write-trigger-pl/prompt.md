---
description: Natural Polish request for a PR description; checks that /coldread:write fires without being named. Needs --allow-tools Write Bash.
tags: [write, pl, trigger]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Napisz opis do PR-a dla recenzenta i zapisz go w pr.md. Poprawiłem błąd, przez który faktura wysyłała się dwa razy, gdy dostawca płatności odpowiadał wolno: po 10 sekundach był timeout i ponowienie bez sprawdzenia, czy pierwsze żądanie doszło. Teraz każde wysłanie ma klucz idempotencji zbudowany z ID faktury, więc dostawca ignoruje powtórkę. Testy jednostkowe przechodzą, na stagingu nie sprawdzałem.
