---
type: llm
---

Look only at how the final response ends. The task asked only for the file.
PASS if it ends with the result, with how it was checked, or with what the user must decide, such as whether a size that is not an integer should raise an error.
FAIL if it ends with two or more subtopics to explore or learn about, such as `itertools.batched`, generators for large lists or property-based tests, or with a heading such as "Where to go next".
