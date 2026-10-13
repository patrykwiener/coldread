---
description: Polish on-call runbook for a webhook lag alert, saved to runbook.md, from notes that also hold why the worker was split out and an open design question; a held-out case, written before any run of it. Needs --allow-tools Write Bash.
tags: [write, pl, structure, holdout]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Napisz instrukcję dla dyżurnego do alertu PaymentWebhookLag i zapisz ją w runbook.md. Czytelnik: backendowiec na dyżurze, obudzony w nocy, który nie zna serwisu płatności. Moje notatki: alert odpala się, gdy najstarszy nieprzetworzony webhook od operatora płatności czeka dłużej niż 5 minut. Skutek: klienci widzą zamówienia jako nieopłacone, a po 30 minutach operator zaczyna ponawiać webhooki i kolejka rośnie jeszcze szybciej. Najpierw sprawdź `payctl webhooks lag`, który pokazuje opóźnienie na partycję, i dashboard „Payment webhooks” w Grafanie. Co robić: 1) jeśli worker stoi, `payctl worker restart`; 2) jeśli jedna partycja jest zablokowana jednym złym webhookiem, `payctl webhooks skip <id>`, a webhook trafi do tabeli failed_webhooks; 3) jeśli baza odpowiada wolno, `payctl worker scale 2`. Jeśli po 20 minutach opóźnienie nie spada, pisz na kanał zespołu płatności. Historia: do wersji 3.8 webhooki obsługiwało API w tym samym procesie, ale przy pikach Black Friday API zaczęło zwracać 502, więc wydzieliliśmy osobny worker z kolejką w Kafce. Otwarte pytanie na później: czy przejść na webhooki w wersji v2 od operatora, które mają podpisy i deduplikację?
