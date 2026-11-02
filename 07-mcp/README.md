# MCP: connect Claude Code to other tools

MCP (Model Context Protocol) lets Claude Code use tools beyond its built-in set: a browser, your issue tracker, a database, docs search.

## Try it in two minutes

Run these in your terminal (not inside a `claude` session).

**A hosted server, no sign-in needed** (searches the Claude Code docs):

```bash
claude mcp add --transport http claude-code-docs https://code.claude.com/docs/mcp
claude mcp list
```

**A local server** (a browser Claude can drive; needs Node.js 18+):

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

Then start `claude` and ask:

```text
Use playwright to open https://example.com and tell me the page title
```

## Share servers with your team

Copy `.mcp.json` from this folder into your project root and commit it. Anyone who clones the project gets asked to approve the servers the first time they start Claude Code.

## Scopes

| Flag | Who gets it |
| --- | --- |
| (none) / `--scope local` | Only you, only this project |
| `--scope project` | Everyone who clones the project (writes `.mcp.json`) |
| `--scope user` | Only you, every project |

## Services that need a sign-in

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

Then inside Claude Code run `/mcp`, pick the server and choose Authenticate.

## Tips

- Every server adds its tool list to every session. Remove ones you don't use: `claude mcp remove <name>`.
- Stuck? `claude mcp get <name>` shows the error detail.

Docs: https://code.claude.com/docs/en/mcp-quickstart
