# Exercises

Open a terminal in this folder and run `claude`. Do these in order; each builds on the last.

## 1. Get oriented

- Ask Claude for a tour of the project (see `03-prompts/prompt-library.md`).
- Run `/init` and read the `CLAUDE.md` it writes. Compare it to `02-claude-md/CLAUDE.md.example` and merge the best of both.

## 2. Find the bugs (no fixing yet)

There are **four** planted bugs. Without telling Claude where they are, ask:

```text
Read this project and list every bug you can find. For each one, show a
command or input that proves it. Don't change any code.
```

How many did it find? The answer key is in `ANSWER-KEY.md`. Don't peek until you've tried.

## 3. Fix one bug test-first

Pick one bug and ask Claude to write a failing test, then fix it. Watch it run the test before and after.

## 4. Use a skill

Copy `04-skills/fix-issue/` into `.claude/skills/` in this folder. Then fix the next bug with:

```text
/fix-issue the monthly summary includes expenses from other years
```

## 5. Use a subagent

Copy `05-subagents/code-reviewer.md` into `.claude/agents/`. Ask the code-reviewer to review everything you've changed so far.

## 6. Add guard rails

Install the hooks from `06-hooks-and-settings/`. Then ask Claude to edit a `.env` file and watch the hook block it.

## 7. Build a feature with plan mode

Press Shift+Tab until you're in plan mode, then:

```text
Add a `delete` command that removes an expense by its position in the list.
Plan it first: changes, edge cases, tests.
```

Approve the plan and let it build.

## 8. Commit

Run `git init` if you haven't, then `/commit` (after copying `04-skills/commit/`).

## Stretch goals

- Add a `--category` filter to `list`.
- Export a month to CSV.
- Add a budget per category and warn when it's exceeded.
