---
description: Judge calibration for the trigger ask-first grader; a hand-labelled PR description, expected FAIL, background first, no fix or ask in the first two sentences.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to pr.md, with no changes, then reply "done".

-----
Wysyłka faktury do dostawcy płatności ma timeout 10 sekund. Po timeoucie kod ponawiał żądanie i nie sprawdzał, czy pierwsze dotarło.

Jeśli dotarło, faktura wychodziła drugi raz. Ten PR dodaje klucz idempotencji zbudowany z ID faktury, więc dostawca ignoruje powtórkę. Proszę o review. Testy jednostkowe przechodzą, na stagingu nie sprawdzałem.
-----
