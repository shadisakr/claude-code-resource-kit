# Claude Code cheat sheet

## Start

| Command | What it does |
| --- | --- |
| `claude` | Start a session in the current folder |
| `claude "task"` | Start with a first prompt |
| `claude -p "task"` | Run once, print the answer, exit (for scripts) |
| `claude -c` | Continue your last conversation |
| `claude -r` | Pick an earlier conversation to resume |
| `claude --version` | Check the install |

## Inside a session

| Command | What it does |
| --- | --- |
| `/init` | Write a starter CLAUDE.md for this project |
| `/memory` | Open and edit CLAUDE.md files |
| `/clear` | Start fresh (clears the conversation) |
| `/compact` | Summarise the conversation to free up context |
| `/model` | Switch model |
| `/permissions` | See and edit allow and deny rules |
| `/hooks` | See configured hooks |
| `/mcp` | Manage connected MCP servers |
| `/skills` | See available skills |
| `/doctor` | Check and fix your setup |
| `/help` | All commands |

## Keys

| Key | What it does |
| --- | --- |
| Shift+Tab | Cycle permission modes (including plan mode) |
| Esc | Stop Claude mid-step |
| Esc Esc | Rewind to an earlier message or checkpoint |
| `@` | Mention a file, folder or subagent |
| `!` | Run a shell command directly (e.g. `!git status`) |
| Ctrl+B | Send a running task to the background |
| Ctrl+O | Open the full transcript |

## Where things live

| File | Purpose |
| --- | --- |
| `CLAUDE.md` | Project instructions read every session |
| `.claude/settings.json` | Project permissions and hooks (commit it) |
| `.claude/settings.local.json` | Your personal overrides (don't commit) |
| `.claude/skills/<name>/SKILL.md` | Project skills |
| `.claude/agents/<name>.md` | Project subagents |
| `.mcp.json` | Shared MCP servers |
| `~/.claude/` | Your personal versions of all of the above |

## Habits that pay off

- Plan first for anything bigger than a one-line change.
- Give Claude a way to check its work: a test, a command, an expected output.
- Keep CLAUDE.md short. Move procedures into skills.
- Use `/clear` between unrelated tasks.
- Commit often so you can always roll back.

Commands checked against https://code.claude.com/docs in November 2026.
