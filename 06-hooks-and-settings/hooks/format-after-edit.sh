#!/bin/bash
# Formats each file Claude edits, using whichever formatter is installed.
# Python files: ruff or black. JS/TS/JSON/CSS/MD: prettier (via npx).
# Missing formatters are skipped quietly.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
[ -z "$FILE_PATH" ] && exit 0

case "$FILE_PATH" in
  *.py)
    if command -v ruff >/dev/null 2>&1; then
      ruff format "$FILE_PATH" >/dev/null 2>&1
    elif command -v black >/dev/null 2>&1; then
      black -q "$FILE_PATH" >/dev/null 2>&1
    fi
    ;;
  *.js|*.jsx|*.ts|*.tsx|*.json|*.css|*.md)
    if command -v npx >/dev/null 2>&1 && [ -f "$CLAUDE_PROJECT_DIR/node_modules/.bin/prettier" ]; then
      npx prettier --write "$FILE_PATH" >/dev/null 2>&1
    fi
    ;;
esac

exit 0
