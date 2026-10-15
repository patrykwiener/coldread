# Run coldread from a clone

Install from a clone when you want to edit the skill, its Vale checks or the chat rules, or to keep several computers on the same version. This replaces the marketplace install in the [README](../README.md#install). The setup steps that follow it there still apply, and you do them by hand. If you already installed from GitHub, run `claude plugin marketplace remove coldread` first. That command also uninstalls `coldread-chat`, so the script below sets up the chat rules through an import line instead.

```bash
git clone https://github.com/patrykwiener/coldread ~/Code/coldread && ~/Code/coldread/scripts/setup.sh
```

The script registers the clone as a local marketplace and installs the plugin from it. It sets up the chat rules with one import line in `~/.claude/CLAUDE.md` and backs that file up first. If the `coldread-chat` plugin is installed, the script skips that line, because that plugin adds the same rules and both together load them twice. It also warns about copies of coldread that would load next to the plugin, such as one made by `install.sh`. To use another folder, clone there and run the script with `COLDREAD_DIR` set to that folder.

## Updates

Claude Code loads a plugin from a local marketplace straight from the clone at every session start. So a `git pull` or an edit in the clone applies from the next session, or after `/reload-plugins`. Running the script again also works, because it pulls and then checks the rest of the setup.

## Without a marketplace

In the clone, `./install.sh user` copies the plugin into `~/.claude/skills/coldread`. Claude Code loads such a folder as a plugin in every session, with the same commands and the cold reader subagent. coldread needs Claude Code 2.1.271 or later. `./install.sh project /path/to/repo` does the same for one repository, so the team gets it through git. A copy does not follow the clone, so run `install.sh` again after a `git pull`.
