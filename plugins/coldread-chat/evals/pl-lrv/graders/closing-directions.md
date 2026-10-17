---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "Jak dobrać LRV blatu, żeby nie zlał się z frontami, z różnicą policzoną na przykładowych kolorach" and "Jak światło w kuchni zmienia wygląd dwóch kolorów o tym samym LRV". A subtopic phrased as an offer counts, such as "Mogę policzyć kontrast dwóch dekorów, jeśli podasz ich LRV".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Na którą stronę świata wychodzi okno kuchni? Przy oknie na północ doradzę jaśniejsze fronty niż przy oknie na południe."
FAIL if the ending only gives advice, a next step or a caveat, such as "Połóż obie próbki obok siebie przy dziennym świetle" or "LRV mówi tylko o jasności, a nie o odcieniu"; if it names only one subtopic, or only a broad area such as "więcej o kolorach we wnętrzach"; if it only asks for product names or codes so that Claude can compare them, which counts as one subtopic; or if it closes with a generic offer such as "Daj znać, jeśli masz pytania".
