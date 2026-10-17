---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "Co zrobić, gdy różnicówka wybija sama, i jak znaleźć obwód, który ją wybija" and "Czym różni się test przyciskiem od pomiaru, który robi elektryk". A subtopic phrased as an offer counts, such as "Mogę rozpisać, jak co pół roku robić test bez utraty pracy na komputerze".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Ile różnicówek masz w rozdzielnicy? Przy kilku trzeba sprawdzić każdą osobno."
FAIL if the ending only gives advice, a next step or a caveat, such as "Jeśli przycisk nie działa, wezwij elektryka"; if it names only one subtopic, or only a broad area such as "więcej o instalacji elektrycznej"; or if it closes with a generic offer such as "Daj znać, jeśli masz pytania".
