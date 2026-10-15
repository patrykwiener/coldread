# Tune the Vale checks

`/coldread:write` lints every English or Polish draft with Vale, a linter for prose. This page shows where coldread's own rules live and how to change them. Your edits apply only when the plugin runs from your clone, as [clone.md](clone.md) describes. The terms one project's readers know, and Vale rules for one project, belong in that project's `.coldread/` folder instead, from [step 3 of the setup](../README.md#3-optional-share-your-projects-terms-and-texts) in the README.

The rules live in `plugins/coldread/skills/write/vale/`. The `.vale.ini` config lints English with the rules in `styles/Write/`. The `pl.ini` config lints Polish with the rules in `styles/WritePL/`. It also turns on eight English rules by name, such as `Write.SessionLabels`, which flags labels like `Phase A`. The skill runs both through `lint.sh`. Each warning names the rule that raised it, such as `Write.LongCell`, which lives in `styles/Write/LongCell.yml`. For text in another language, `/coldread:write` skips linting and says so.

- To accept an acronym that every reader of yours knows, add it to `exceptions` in `styles/Write/Acronyms.yml` or `styles/WritePL/Acronyms.yml`, in quotes. YAML reads an unquoted `NULL` as an empty value, which silently disables the rule.
- To quiet a noisy rule, change its `level:` to `suggestion`, which the skill treats as a hint rather than something to fix, or delete its file. If `pl.ini` names the rule, delete its line there too.

To check an edit, lint a text by hand from the clone's root, with `en` or `pl` for its language:

```bash
plugins/coldread/skills/write/vale/lint.sh en README.md
```
