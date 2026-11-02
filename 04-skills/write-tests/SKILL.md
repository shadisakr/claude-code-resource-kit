---
description: Write and run tests for a file or function. Use when the user asks for tests, test coverage, or to make code safer to change.
argument-hint: "[file or function]"
---

Write tests for: $ARGUMENTS

1. Read the code and the existing tests to match the project's test style and framework. If there are no tests yet, use the framework named in CLAUDE.md, or the standard one for the language (pytest for Python, the existing runner for JavaScript).
2. Cover: the normal case, empty or missing input, invalid input, and at least one boundary (zero, very large, first/last item).
3. Run the tests.
4. If a test fails, decide whether the test or the code is wrong. Fix the test if it's wrong. If the code is wrong, leave the test failing and tell the user: that's a bug they should know about.
5. Finish with a short list: tests added, what each checks, and any bugs found.
