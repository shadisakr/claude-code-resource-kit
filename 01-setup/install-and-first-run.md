# Install Claude Code and run your first session

You need a paid Claude plan (Pro, Max, Team or Enterprise) or an Anthropic Console account.

## 1. Install

Pick the line for your system and paste it into a terminal.

**macOS, Linux or WSL (recommended)**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell** (your prompt starts with `PS C:\`)

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD** (your prompt starts with `C:\`, no `PS`)

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Other options**

| Tool | Command | Auto-updates? |
| --- | --- | --- |
| Homebrew | `brew install --cask claude-code` | No, run `brew upgrade claude-code` |
| WinGet | `winget install Anthropic.ClaudeCode` | No, run `winget upgrade Anthropic.ClaudeCode` |

On native Windows, install Git for Windows too so Claude Code can use Bash. WSL doesn't need it.

## 2. Check it worked

Open a **new** terminal window and run:

```bash
claude --version
```

You should see a version number. If you get "command not found", the install folder isn't on your PATH yet. See https://code.claude.com/docs/en/troubleshoot-install

## 3. Start your first session

```bash
cd path/to/starter-project
claude
```

Claude Code asks you to log in the first time. After that, try:

```text
What does this project do? Give me a two-paragraph overview.
```

## 4. Run a health check

Inside a session, type:

```text
/doctor
```

It checks your install, settings and CLAUDE.md files and offers fixes.

## Prefer not to use a terminal?

- **Desktop app:** download Claude for macOS or Windows, sign in, open the Code tab.
- **VS Code / Cursor:** search "Claude Code" in Extensions.
- **Browser:** go to claude.ai/code (needs a GitHub repo).

The course uses the terminal, but everything in this kit works on every surface.
