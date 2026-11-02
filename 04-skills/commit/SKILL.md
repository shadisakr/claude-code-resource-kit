---
description: Stage and commit the current changes with a clear message.
disable-model-invocation: true
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *) Bash(git diff *)
---

## Current state

!`git status --short`

## Instructions

1. Look at the diff. If the changes cover more than one unrelated thing, split them into separate commits.
2. Write each message as: a short summary line under 60 characters in the imperative ("Add monthly summary command"), a blank line, then one to three lines on why.
3. Never commit `.env` files, credentials or large generated files. If you see any staged, stop and tell the user.
4. Don't push.
