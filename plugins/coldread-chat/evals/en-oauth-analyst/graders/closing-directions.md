---
type: llm
---

Look only at how the final response ends: its last paragraph or list, with the line that introduces it. A one-line caveat after that list does not change the verdict. Nothing earlier matters for this check.
PASS if the ending does at least one of two things:
- It names at least two specific subtopics the user could ask about next, each clear enough that the user knows what they would get, for example "What a refresh token is, and why the BI tool stays connected without asking you to log in again" and "What to send your warehouse admin to register the BI tool, field by field". A subtopic phrased as an offer counts, such as "I can draft the message to your admin".
- It asks one question about the user's own situation and says how the answer changes the advice, for example "Does your BI tool run in the browser or as a desktop app? The admin registers the two kinds differently."
FAIL if the ending only gives a next step or a caveat, such as "Your next step is to send your admin the redirect URI"; if it names only one subtopic, such as the single offer "If you tell me which warehouse you use, I can point you to the exact fields"; if it names only a broad area such as "more about authentication"; or if it closes with a generic offer such as "Let me know if you have questions".
