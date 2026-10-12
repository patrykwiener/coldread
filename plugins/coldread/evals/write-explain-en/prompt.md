---
description: Explainer for a new product manager who must understand how search stays up to date; checks understanding, terms with examples and one case walked through. Needs --allow-tools Write Bash.
tags: [write, en, explainer]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Agent, Read, Glob, Grep, Write, Bash]
---

Write a short explainer for Maria, a product manager who joins the search team next week. She reads it before her first planning meeting. She needs to understand how a product edit reaches the search results; she does not approve anything. My notes: when a seller edits a product, the database writes a row to the change feed. The indexer reads the change feed every 30 seconds and updates the search index, so an edit normally shows up in search within about a minute. "Lag" is how far the indexer is behind the change feed; above 10 minutes an alert goes to the on-call engineer. Once a week we run a full reindex into a new index and then swap the alias, so searches move to the new index at once without downtime. Terms Maria won't know: change feed, indexer, search index, lag, reindex, alias.
