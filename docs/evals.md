# Run the evals

Both plugins ship with evals for `claude plugin eval`, which runs each case with and without the plugin in a clean session. This page shows how to run them from the root of a clone of this repository. [results.md](results.md) has every run so far and its limits.

```bash
claude plugin eval plugins/coldread-chat --allow-tools Write --judge-model sonnet
claude plugin eval plugins/coldread --allow-tools Write Bash --judge-model sonnet
```

The chat suite in `plugins/coldread-chat` has 14 cases, seven of them in Polish, and the write suite in `plugins/coldread` has 19. Each case runs 3 times with the plugin and 3 times without it by default. Results go to `plugins/<name>/evals/results/`, which git ignores. Install Vale before you run the write suite, or `/coldread:write` skips its lint step.

Each case has graders, and each grader checks one condition of the text. Sonnet judges because Haiku failed texts that met every condition of a grader, as [results.md](results.md) shows. As a judge, Sonnet costs about $0.04 per run. A condition that a pattern can check, such as a local path or a date in the text, uses a `regex` grader. In the write suite, that grader reads the file the case asks Claude to save. In the chat suite, it reads Claude's last answer. Either way, no judge votes on it.

If every run stops at once with an error about the Docker credential store, Claude Code's Bash sandbox refused to start because `~/.docker` holds a symbolic link. Run the write suite with `--allow-tools Write` only. It then measures the skill without the word count, the facts check and the lint, which all run in the shell.
