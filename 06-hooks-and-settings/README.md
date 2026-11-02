# Hooks and settings

`settings.json` does two jobs:

- **Permissions:** commands Claude may run without asking (`allow`) and things it may never do (`deny`), such as reading `.env`.
- **Hooks:** scripts that always run at set moments. Unlike instructions in CLAUDE.md, hooks are guaranteed.

## Install (macOS, Linux, WSL)

From your project root:

```bash
mkdir -p .claude/hooks
cp path/to/kit/06-hooks-and-settings/settings.json .claude/settings.json
cp path/to/kit/06-hooks-and-settings/hooks/*.sh .claude/hooks/
chmod +x .claude/hooks/*.sh
```

If you already have a `.claude/settings.json`, merge the `permissions` and `hooks` blocks instead of overwriting it.

The scripts need `jq` (`brew install jq` or `sudo apt-get install jq`). On native Windows, use WSL or rewrite the scripts in PowerShell.

## Check it

1. Start Claude Code and type `/hooks`. You should see both hooks listed.
2. Ask: "Add a comment to .env". The edit should be blocked with a "Blocked:" message.
3. Type `/permissions` to see your allow and deny rules.

## Desktop notification when Claude needs you (optional)

Add this to `~/.claude/settings.json` (your personal settings, not the project's). macOS version:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

On Linux, replace the command with `notify-send 'Claude Code' 'Claude Code needs your attention'`.

Docs: https://code.claude.com/docs/en/hooks-guide
