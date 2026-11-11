---
type: llm
---

The user asked Claude to rewrite a short note in ASD-STE100. The note uses words that the ASD-STE100 dictionary does not approve, such as "may", "should" and "suggests".
This grader reads only Claude's reply to the user; another grader checks the saved file.
PASS if the reply says which of those words Claude kept, or replaced without changing their strength, or says that it changed none of them.
FAIL if the reply says nothing about such words.
