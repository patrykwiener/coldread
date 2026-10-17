---
type: llm
---

Look only at how the final response ends. It reports a finished task.
PASS if it ends with the result, with how it was checked, or with what the user must decide, such as whether letters with accents stay in the slug. One offer of a concrete follow-up change, such as "I can switch the pattern to `[^a-z0-9]+` for ASCII-only slugs", also passes.
FAIL if it ends with two or more subtopics to explore or learn about, such as how Unicode normalisation works, transliteration libraries or property-based tests, or with a heading such as "Where to go next".
