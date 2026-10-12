---
type: llm
---

Act as a layman in electrical work who has only the final response. Try to answer:
1. What does a różnicówka do? Expected: it cuts the power when current leaks somewhere it should not, for example through a person, so it protects against electric shock.
2. What does 30 mA mean? Expected: the leak at which it switches off; 30 mA is the level that protects people.
3. What does the ogranicznik przepięć protect against? Expected: sudden voltage spikes, for example from lightning, that can damage devices.
PASS if the response lets this reader answer all three correctly.
FAIL if any answer is missing or only implied.
