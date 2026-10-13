# A prompt for a new agent session

Read this when the user asks for a prompt, a brief or a handoff that another agent session will run, such as "give me a prompt for a new session" or „daj mi prompt do nowej sesji".

## The reader

The reader is an agent that starts a fresh session in the same repository. It has the project's instructions, such as CLAUDE.md or AGENTS.md, and the files, but not this session. Write the reader line that way, for example: "a coding agent starting a fresh session in this repository, with its CLAUDE.md loaded; it did not see the session that wrote this prompt". The Must is what the session produces and where it stops to wait for the user.

## The parts, in this order

Leave out the parts the task does not need.

1. **A title** that names the task.
2. **An opening of at most about 120 words**: what to do, where to run it, such as "paste this into a new session in this repository", that the session has no memory of this one, and what it must not do, such as commit, push, send or deploy.
3. **The want, verbatim**: the user's own words in their language, quoted, with a translation when the prompt is in another language. The session then sees the intent unfiltered.
4. **Decisions already made**, each with its reason in one line, so the session does not reopen them.
5. **Inputs, and which one wins** when they disagree, such as "the code wins over the design doc".
6. **Files to read first**, each with what it holds.
7. **Steps**, each with its output. Mark every point where the session must stop and wait for the user's approval, such as before it changes anything that others use.
8. **Checks** to run before each stop.
9. **Safety**: the environments, accounts and data it must not touch.
10. **Known traps**: tools or commands that failed in earlier sessions, and what worked instead.
11. **What to hand back**: the files and their paths, and the final message with its language.

## Rules for this channel

- Paths on this machine are fine here, because the reader works on the same machine. Keep the paths a step needs, check that each exists, and ignore `LocalPaths` warnings for them.
- Define every label where it first appears: the session cannot ask what "F06" or "decision 2" means.
- State each fact with its source, such as a commit, a file or a check you ran, so the session can verify it instead of trusting it.
- Point to files instead of pasting long excerpts, and quote only the lines a step depends on.
- The budget covers the opening. The rest is reference that the session reads step by step.

## The cold read

The real reader has the project's instructions, so this cold reader should have them too. In Claude Code, use the general-purpose subagent from step 6, told to read the cold reader's instructions first, because `coldread:cold-reader` skips CLAUDE.md. In OpenCode, the `cold-reader` subagent already sees AGENTS.md. Give it the reader line above.

## In the report

List every file the prompt names, each marked as checked to exist.
