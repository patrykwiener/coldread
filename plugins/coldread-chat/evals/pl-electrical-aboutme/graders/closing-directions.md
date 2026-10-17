---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "Czym różni się różnicówka typu A od AC i którą wybrać przy pralce i płycie indukcyjnej" and "Jak samemu sprawdzić przyciskiem T, czy różnicówka działa". A subtopic phrased as an offer counts, such as "Mogę rozpisać, ile obwodów warto mieć w kuchni przy Twoich urządzeniach".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Czy w kuchni będzie płyta indukcyjna? Od tego zależy, czy warto poprosić elektryka o osobny obwód na płytę."
FAIL if the ending only gives advice, a next step or a caveat, such as a list of questions to ask the electrician or "Poproś o protokół z pomiarów"; if it names only one subtopic, or only a broad area such as "więcej o instalacji elektrycznej"; or if it closes with a generic offer such as "Daj znać, jeśli masz pytania".
