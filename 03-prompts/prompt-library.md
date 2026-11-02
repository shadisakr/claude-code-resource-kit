# Prompt library

Copy, paste, and fill in the brackets. The pattern behind all of these: say what you want, point to the files, and give Claude a way to check its own work.

## Understand a codebase

```text
Give me a tour of this project: what it does, the main folders, how a request
(or command) flows from entry point to output, and where the tests are.
Keep it under 300 words.
```

```text
Where is [feature/behaviour] implemented? List the files and functions involved
and explain how they connect. Don't change anything.
```

## Plan before you build

Press Shift+Tab to switch into plan mode first, then:

```text
I want to add [feature]. Read the relevant code, then propose a plan:
files to change, new files, edge cases, and how we'll test it.
Ask me anything you need to know before you start.
```

```text
Interview me about [feature] one question at a time until you have enough
to write a short spec. Then write the spec to SPEC.md.
```

## Fix a bug

```text
[Paste the error or describe the symptom.]
Find the root cause, not just the line that throws. Write a failing test that
reproduces it, then fix the code until the test passes. Run the full test suite
at the end.
```

```text
This worked on [date/commit] and broke after. Use git log and git diff to find
the change that caused it and explain why.
```

## Write tests

```text
Write tests for [file or function]. Cover the happy path, empty input,
invalid input and one edge case you think I'd miss. Run them and fix any that
fail because of a real bug (tell me which ones those were).
```

## Refactor safely

```text
Refactor [file] to [goal, e.g. split the 200-line function into smaller ones].
Behaviour must not change. Run the tests before and after and show me both
results.
```

## Review

```text
Review my uncommitted changes as a senior engineer would. Group findings by
severity (must fix / should fix / nit). Point to exact lines. Don't edit files.
```

## Git

```text
Commit my changes with a clear message. If they cover more than one thing,
split them into separate commits.
```

```text
Create a branch, push it, and open a pull request with a summary of what
changed and how to test it.
```

## Docs

```text
Update the README so a new contributor can install, run and test this project
in under five minutes. Check every command actually works.
```

## Course or content work (non-code)

Claude Code works in any folder, not just code.

```text
This folder has my course scripts. Check every script for the same module
structure: hook, what you'll learn, steps, recap. List any that are missing a
section.
```

## When things go sideways

```text
Stop. Summarise what you've tried, what failed and why, then suggest two
different approaches before doing anything else.
```

Tip: press Esc to interrupt, Esc twice to rewind to an earlier point.
