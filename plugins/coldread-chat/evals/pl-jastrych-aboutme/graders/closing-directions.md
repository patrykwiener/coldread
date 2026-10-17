---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "Jak działa pomiar wilgotności metodą CM i jaki wynik musi wyjść przed panelami" and "Czym różni się jastrych anhydrytowy od cementowego i kiedy wybrać który". A subtopic phrased as an offer counts, such as "Mogę policzyć, ile tygodni będzie schła wylewka 5 cm w Twoim mieszkaniu".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Co jest teraz na podłodze: goły beton, stara wylewka czy rury ogrzewania podłogowego? Od tego zależy, czy jastrych w ogóle jest potrzebny." The same request phrased as "Jeśli napiszesz, co jest teraz na podłodze, ocenię, czy jastrych jest potrzebny" counts.
FAIL if the ending only gives advice, a next step or a caveat, such as "Poproś ekipę o pokazanie nierówności" or a list of questions to ask the flooring crew; if it names only one subtopic, or only a broad area such as "więcej o wylewkach"; or if it closes with a generic offer such as "Daj znać, jeśli masz pytania".
