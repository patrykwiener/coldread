---
type: llm
---

Act as a product manager who knows nothing about this search system and has only the explainer. Try to answer:
1. A seller changes a product's price at 10:00. Roughly when does search show the new price, and what happens in between? Expected: within about a minute; the edit is written to the change feed, the indexer picks it up within 30 seconds and updates the search index.
2. What is lag, and what happens when it grows too large? Expected: how far the indexer is behind the change feed; above 10 minutes the on-call engineer gets an alert.
3. Why does the weekly reindex not interrupt search? Expected: it builds a new index and then swaps the alias, so searches move to the new index at once.
PASS if the explainer lets this reader answer all three correctly.
FAIL if any answer is missing or only implied.
