---
description: Judge calibration for the trigger ask-first grader; a hand-labelled PR description, expected PASS, the fix named without its condition, which the grader does not require.
tags: [calibration]
max_turns: 4
timeout_seconds: 180
allowed_tools: [Write]
---

Save exactly the text between the two lines of dashes below to pr.md, with no changes, then reply "done".

-----
Ten PR naprawia błąd, przez który klient mógł dostać tę samą fakturę dwa razy. Proszę o review. Testy jednostkowe przechodzą, ale na stagingu zmiany nie sprawdzałem.

## Ponowienie po timeoucie wysyłało fakturę drugi raz

Gdy dostawca płatności odpowiadał wolno, wysyłka faktury po 10 sekundach kończyła się timeoutem. Kod wtedy ponawiał żądanie i nie sprawdzał, czy pierwsze dotarło do dostawcy. Jeśli dotarło, faktura wychodziła dwa razy.

## Klucz idempotencji z ID faktury blokuje powtórkę

Każde wysłanie niesie teraz klucz idempotencji zbudowany z ID faktury. Ponowienie tej samej faktury ma więc ten sam klucz, a dostawca je ignoruje.

## Reakcja prawdziwego dostawcy nie jest sprawdzona

Bez testu na stagingu nie wiemy, jak prawdziwy dostawca reaguje na powtórzone żądanie z tym samym kluczem.
-----
