# coldread in OpenCode

coldread also runs in OpenCode 2, set up from a clone with one script. This page covers that setup, its updates, and where each command and setting lives in OpenCode. What each setting does, and which one wins, is in [How configuration works](../README.md#how-configuration-works) in the README.

## Set it up

```bash
git clone https://github.com/patrykwiener/coldread ~/Code/coldread && ~/Code/coldread/scripts/setup-opencode.sh
brew install vale   # optional: lets /coldread/write lint its drafts; other systems: vale.sh
```

The script links the skills, the cold reader and the commands from the clone into `~/.config/opencode`. It also copies coldread's chat rules into `~/.config/opencode/AGENTS.md` between two marker lines. These ten rules make every answer easier to follow, for example by answering first and explaining every new term, as [What you get](../README.md#what-you-get) in the README lists. Run it with `--no-chat` to leave `AGENTS.md` alone, with `--no-pull` to set up the clone as it is, or with `--uninstall` to remove everything it added. Before it links a file, the script moves a file or folder already at that path to `~/.config/opencode/coldread-backups/`, because both copies would load. It also moves an older copy of coldread's write skill or `/write` command that you installed by hand. A file of yours named like those two but with other contents stays where it is. At the end, the script runs `opencode reload`.

## Update it

To update, run the script again. It runs `git pull --ff-only` in the clone. When the pull brings new commits, the script starts over from the new version, so a skill added upstream gets its link too. Then it refreshes the copy of the chat rules and reloads OpenCode. If the pull fails, for example offline or because the clone holds commits of your own, the script stops and suggests `--no-pull`. A branch without an upstream, such as one you work on, is set up without a pull.

## Commands and settings in OpenCode

The settings go into `AGENTS.md` files where Claude Code uses `CLAUDE.md`. The README's [setup steps](../README.md#set-it-up-in-three-steps) show what each section holds. coldread's OpenCode build has no language option, so texts follow the language of your request unless the project's `AGENTS.md` names one.

| In Claude Code | In OpenCode |
|---|---|
| `/coldread:write`, `/coldread:reply`, `/coldread:plain` | `/coldread/write`, `/coldread/reply`, `/coldread/plain` |
| the `coldread:cold-reader` subagent | the `cold-reader` subagent |
| About me and How I write in `~/.claude/CLAUDE.md` | the same sections in `~/.config/opencode/AGENTS.md` |
| a Writing section in a project's `CLAUDE.md` | the same section in the project's `AGENTS.md` |
| the document language, set with `/plugin configure coldread@coldread` | `auto`, unless the project's `AGENTS.md` names a language |

A `.coldread/` folder with a project's terms and sample texts, from [step 3](../README.md#3-optional-share-your-projects-terms-and-texts) of the setup, works the same in both tools.

OpenCode 2 gives every agent the global and the project's `AGENTS.md`, so its cold reader may know names from those files that the person you write for does not. `/coldread/write` says so in its report. coldread's [evals](evals.md) run in Claude Code only.

## For contributors

`scripts/build-opencode.py` generates the `opencode/` folder from `plugins/coldread`, and `scripts/check.sh` fails when that folder is out of date. The folder is in git, so users never run the build.
