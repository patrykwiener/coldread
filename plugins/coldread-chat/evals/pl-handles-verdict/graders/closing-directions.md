---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "Na jakiej wysokości montować listwę, żeby dziecko nie uderzało w nią głową" and "Jakie blokady na dzieci działają z frontami bez uchwytów". A subtopic phrased as an offer counts, such as "Mogę porównać ceny listew aluminiowych na Twoją liczbę frontów".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Ile lat mają dzieci? Przy dzieciach poniżej trzech lat ważniejsze są blokady niż kształt uchwytu."
FAIL if the ending only gives advice, a next step or a caveat, such as "Przed zamówieniem dotknij próbek w salonie"; if it names only one subtopic, or only a broad area such as "więcej o kuchniach"; or if it closes with a generic offer such as "Daj znać, jeśli masz pytania".
