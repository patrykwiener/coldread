---
description: Guard case. Plain coding task; the rules must not lower correctness. Needs --allow-tools Write.
tags: [guard, en]
max_turns: 8
allowed_tools: [Write, Read]
---

Create chunk.py with a function chunk(items: list, size: int) -> list[list] that splits a list into consecutive lists of length size, with a shorter last list if needed. It must return [] for an empty list and raise ValueError when size is less than 1. Only write the file.
