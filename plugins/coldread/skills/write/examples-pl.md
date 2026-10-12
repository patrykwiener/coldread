<!-- These anchors are invented examples. They show the register and opening to aim
for in Polish. To use texts from your own project instead, put 2-3 of them in
.coldread/examples-pl.md in that repository once they passed the cold read. -->

# Style anchors (Polish)

Match the register, density and opening of these examples, not their topics.

## Handoff note

> Poprawka błędu z podwójnymi fakturami (#412) weszła do `main` w PR #88 i od wydania 2.4.0 działa na produkcji. Zostało sprzątanie duplikatów, które już poszły do klientów, i jedno pytanie do działu finansów. Nie znalazłem śladu, że ktoś to sprzątanie uruchomił, więc traktuj je jako niezrobione.
>
> **Błąd.** `POST /api/invoices/send` po przekroczeniu czasu ponawiał wysyłkę i nie sprawdzał, czy pierwsza próba dotarła do operatora płatności. Gdy operator odpowiadał wolno, klient dostawał dwie identyczne faktury.
>
> **Poprawka.** Każda wysyłka niesie teraz klucz idempotencji zbudowany z identyfikatora faktury, więc operator ignoruje powtórkę. Ponawianie działa tak jak wcześniej.
>
> **Do zrobienia.**
> 1. Uruchom `scripts/find_duplicate_invoices.py --since 2024-01-01` na produkcji. Skrypt wypisuje pary duplikatów i niczego nie zmienia.
> 2. Zapytaj finanse, czy opłacone duplikaty zwracamy klientom, czy zaliczamy na poczet kolejnych faktur.

Why it works: the first sentence says what happened, with the ticket explained in plain words next to its number. The second says what is left. Status is checked, not assumed, and the text says so. Verbs carry the action ("weszła", "ponawiał", "uruchom"), never a noun built from a verb.

## PR description opening

> Przed merge'em potrzebuję twojej decyzji w jednej sprawie: eksport ponawia teraz wysyłkę pięć razy zamiast raz, więc mail o nieudanym eksporcie może przyjść nawet dwie minuty później.
>
> Miesięczny eksport padał mniej więcej u jednego klienta na pięćdziesięciu, bo storage gubi niewielką część uploadów. Teraz każdy nieudany upload ponawia się z coraz dłuższą przerwą, a eksport pada dopiero po piątej próbie. Na danych z zeszłego miesiąca liczba nieudanych eksportów spadła z 41 do 0.

Why it works: the reader's decision comes first, with its cost. What changed follows in two sentences, with one measured number. There is no history of the other retry counts that were tried, and no word like "kluczowy" or "znacząco" where a number does the job. Software terms stay as developers say them: merge, storage, upload.

## Proposal opening

> Ta zmiana przenosi PDF-y faktur z bazy danych do S3 i wymaga twojej zgody na jeden kompromis: link do pobrania wygaśnie po 15 minutach, zamiast działać bez końca.
>
> Tabela faktur zajmuje 180 GB, z czego 170 GB to pliki PDF, a nocny backup trwa przez to cztery godziny. Po przeniesieniu plików tabela zmieści się w 10 GB.

Why it works: the goal and the one decision the approver must make are in the first sentence. The problem is then stated with numbers, and nothing in it depends on a document the reader does not have.

## Review comments

> **Do poprawy:** Strony numerujemy od 1, więc `offset = page * page_size` na pierwszej stronie pomija pierwsze 20 wyników. Użytkownik nigdy nie widzi najnowszych zamówień.
> ```suggestion
>     offset = (page - 1) * page_size
> ```

> **Pytanie:** Po tej poprawce `?page=0` daje ujemny offset. Ma zwracać pierwszą stronę, jak dziś, czy błąd 400?

> Nowe parametry filtrów czyta się dobrze. Przed merge'em popraw offset i zdecyduj, co zwraca strona 0. Na później jeden test: prośba o stronę 1 i sprawdzenie, że jest na niej najnowsze zamówienie.

Why it works: each comment holds one problem, why it matters and the fix, in at most three sentences, and the code change is a suggestion the author can apply. The summary says what is good, what blocks the merge and the one follow-up. Style preferences and the reviewer's evidence stay out.

## Explainer opening

> Link do resetu hasła pozwala użytkownikowi, który zapomniał hasła, ustawić nowe bez pisania do supportu. Ta notatka pokazuje, co się dzieje od kliknięcia „Nie pamiętam hasła" do chwili, gdy nowe hasło działa. Jest dla osób, które odpowiadają na zgłoszenia w tej sprawie.
>
> **Token resetu.** Losowy ciąg znaków, który potwierdza, że link wysłaliśmy my. Przykład: `k3J9…` w `https://app.example.com/reset?token=k3J9…`. Leży w tabeli `password_resets`, jeden wiersz na prośbę.
>
> **Ważność.** Jak długo token działa: 30 minut. Link z prośby z 10:00 otwarty o 10:31 pokazuje „Link wygasł".
>
> **Jeden reset krok po kroku.** O 10:00 Ana prosi o reset. Zapisujemy token dla jej konta i wysyłamy jej link mailem. O 10:12 Ana otwiera link i ustawia nowe hasło, a my oznaczamy token jako zużyty, więc ten sam link przy drugim kliknięciu już nie działa.

Why it works: two sentences say what the thing does and who the note is for. Each term gets one sentence, one example with values, and where it lives. Then one invented case runs from start to end, so the reader sees how the terms fit together.
