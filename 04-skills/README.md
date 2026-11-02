# Skills

A skill is a folder with a `SKILL.md` file. Claude loads it when your request matches its description, or you run it directly with `/skill-name`.

## Install

Copy any skill folder into one of these:

- `.claude/skills/` inside a project (shared with anyone who clones the repo)
- `~/.claude/skills/` in your home folder (available in all your projects)

Then start Claude Code and type `/` to see it in the menu.

## What's here

| Skill | Run it with | What it does |
| --- | --- | --- |
| `summarize-changes` | `/summarize-changes` | Summarises your uncommitted diff and flags risks |
| `fix-issue` | `/fix-issue 42` | Reproduces, fixes and tests a bug (from a GitHub issue number or a description) |
| `write-tests` | `/write-tests src/app.py` | Writes and runs tests for a file |
| `commit` | `/commit` | Stages and commits with a clear message. Only runs when you ask |

## Make your own

Ask Claude: "Turn what we just did into a skill in .claude/skills/". Then read the file it writes and trim it.

Docs: https://code.claude.com/docs/en/skills
