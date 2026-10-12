---
name: plain
description: Re-explain the last answer after finding why it was hard to follow.
argument-hint: "[what you did not get]"
disable-model-invocation: true
---

The user did not understand your last answer. Saying the same thing in other words fails the same way.

What the user said: $ARGUMENTS

1. **Diagnose.** Use the user's hint; otherwise pick the most likely failure. Fix every one that applies:
   - Answered another question: restate the question in one line and answer only that.
   - Unexplained term, or a code or tag you invented: say what it is in plain words.
   - Skipped step or missing reason: add it in order, with "because" and "so".
   - Stayed abstract: open with one real case, values included.
   - Too much at once: give the main point and at most three more; say what you cut.
   - No verdict where the user had to choose: name your pick and the main reason first.
   - Wrong or unsupported: say so first, then correct it. Only in this case read files again.
2. **State the diagnosis in one sentence**, such as "I used 'lease' without saying what it is." No apology. Then re-explain.
3. Reuse no sentence from the last answer. It may grow only by the definitions, steps and example you add; if the last answer had more than four points, it must get shorter. Reply in the user's language.
