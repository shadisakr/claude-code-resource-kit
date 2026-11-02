# Subagents

A subagent is a helper Claude can hand work to. It runs in its own context window, so long logs or file dumps stay out of your main conversation, and it can be limited to specific tools.

## Install

Copy the `.md` files into:

- `.claude/agents/` in a project, or
- `~/.claude/agents/` for all your projects.

## Use

Ask for one by name ("Use the code-reviewer subagent on my changes"), or type `@` and pick it from the list. Claude also delegates on its own when your request matches a description.

| File | What it does | Tools |
| --- | --- | --- |
| `code-reviewer.md` | Reviews changes, read-only | Read, Grep, Glob, Bash |
| `debugger.md` | Finds root causes and fixes failures | All default tools |
| `test-writer.md` | Writes and runs tests | Read, Write, Edit, Bash, Grep, Glob |

Docs: https://code.claude.com/docs/en/sub-agents
