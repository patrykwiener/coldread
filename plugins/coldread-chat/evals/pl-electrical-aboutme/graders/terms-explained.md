---
type: llm
---

The reader is a layman in electrical work. List the electrical terms in the final response that such a reader would not know, such as różnicówka, mA, ogranicznik przepięć, typ B+C, obwód, rozdzielnica, przekrój przewodu, uziemienie or zabezpieczenie nadprądowe.
PASS if every term from the user's question (różnicówka, 30 mA, ogranicznik przepięć, typ B+C, 2,5 mm²) is explained in plain words, and at most one other electrical term is left without an explanation.
FAIL if a term from the question is not explained, or two or more other electrical terms are left without an explanation.
