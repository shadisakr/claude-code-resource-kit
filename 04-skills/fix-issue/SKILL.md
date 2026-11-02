---
description: Reproduce, fix and test a bug from a GitHub issue number or a plain description.
argument-hint: "[issue-number or description]"
disable-model-invocation: true
---

Fix this bug: $ARGUMENTS

1. If the argument is a number and the `gh` CLI is available, read the issue with `gh issue view $ARGUMENTS`. Otherwise treat the argument as the bug description.
2. Find the root cause. Explain it in one or two sentences before changing code.
3. Write a test that fails because of the bug. Run it and confirm it fails.
4. Make the smallest change that fixes the root cause.
5. Run the new test and the full test suite. Both must pass.
6. Report: root cause, files changed, and the test you added. Don't commit.
