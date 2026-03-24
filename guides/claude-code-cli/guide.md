# Master Claude Code — A Practical CLI Guide

Your go-to reference for everything Claude Code can do from the command line. Start with the quick reference cards below, then dive into the detail pages for hands-on exercises.

## Quick Navigation

| Section | What it covers | Detail Page |
|:--------|:--------------|:------------|
| [Slash Commands](#slash-commands) | Built-in `/` commands | [Deep dive](slash-commands.md) |
| [Permissions](#permissions) | Control what Claude can access | [Deep dive](permissions.md) |
| [Models & Context](#models--context) | Switch models, manage conversations | [Deep dive](models-and-context.md) |
| [CLI Flags](#cli-flags) | Launch-time options | [Deep dive](cli-flags.md) |
| [MCP Servers](#mcp-servers) | Connect external tools | [Deep dive](mcp-servers.md) |
| [Hooks](#hooks) | Automate actions on events | [Deep dive](hooks.md) |
| [Plugins & Skills](#plugins--skills) | Extend with community packages | [Deep dive](plugins-and-skills.md) |
| [Settings & Config](#settings--config) | Customize your environment | [Deep dive](settings-and-config.md) |

---

## Slash Commands

Type `/` in Claude Code to see all available commands, or type `/` followed by letters to filter. Here are the most useful ones grouped by what you're trying to do.

### Essential (use daily)

| Command | What it does |
|:--------|:-------------|
| `/help` | Show all available commands |
| `/clear` | Clear conversation and free up context (aliases: `/reset`, `/new`) |
| `/compact [focus]` | Compress conversation to save context — add focus instructions like `/compact keep the API discussion` |
| `/model [name]` | Switch models — `opus`, `sonnet`, `haiku`, or full model ID |
| `/cost` | Show how much this session has used (tokens and cost) |
| `/diff` | Interactive viewer showing uncommitted code changes |
| `/context` | Visualize how much context you've used (colored grid) |

### Session Management

| Command | What it does |
|:--------|:-------------|
| `/resume` | Resume a previous conversation (alias: `/continue`) |
| `/rename [name]` | Name your session for easy resuming later |
| `/branch [name]` | Fork the conversation at this point (alias: `/fork`) |
| `/rewind` | Go back to an earlier point in the conversation (alias: `/checkpoint`) |
| `/export [file]` | Save conversation as text — to clipboard or a file |
| `/copy [N]` | Copy last response to clipboard — add a number for older responses |

### Configuration

| Command | What it does |
|:--------|:-------------|
| `/config` | Open settings interface (alias: `/settings`) |
| `/permissions` | View and edit allow/deny rules (alias: `/allowed-tools`) |
| `/hooks` | View configured hooks |
| `/memory` | Edit CLAUDE.md files and auto-memory settings |
| `/mcp` | Manage MCP server connections |
| `/plugin` | Manage plugins (install, remove, browse) |
| `/skills` | List all available skills |
| `/init` | Initialize a project with CLAUDE.md |

### Tools & Integrations

| Command | What it does |
|:--------|:-------------|
| `/add-dir <path>` | Give Claude access to an additional directory |
| `/pr-comments [PR]` | Fetch GitHub PR comments (auto-detects current branch) |
| `/install-github-app` | Set up Claude GitHub Actions for a repo |
| `/security-review` | Scan pending changes for security vulnerabilities |
| `/voice` | Toggle push-to-talk voice dictation |
| `/chrome` | Configure Chrome browser integration |

### Display & Preferences

| Command | What it does |
|:--------|:-------------|
| `/theme` | Change color theme (light, dark, colorblind-accessible) |
| `/color [color]` | Change prompt bar color (red, blue, green, yellow, purple, etc.) |
| `/fast [on/off]` | Toggle fast mode (same model, faster output) |
| `/effort [level]` | Set effort level: `low`, `medium`, `high`, `max` (Opus only) |
| `/vim` | Toggle Vim editing mode |
| `/stats` | Show usage stats, session history, streaks |

### Bundled Skills (prompt-based, not fixed logic)

| Command | What it does |
|:--------|:-------------|
| `/batch <instruction>` | Orchestrate large-scale changes in parallel across a codebase |
| `/simplify [focus]` | Review recent changes for quality, then fix issues |
| `/debug [description]` | Troubleshoot your current session by reading debug logs |
| `/loop [interval] <prompt>` | Run a prompt repeatedly on a schedule |

---

## Permissions

Control what Claude can and can't do. Rules are evaluated in order: **deny > ask > allow**.

### Permission Modes

| Mode | What it does |
|:-----|:-------------|
| `default` | Prompts for permission on first use of each tool |
| `acceptEdits` | Auto-approves file edits for the session |
| `plan` | Read-only — Claude can analyze but not modify anything |
| `dontAsk` | Auto-denies unless pre-approved in your allow list |
| `bypassPermissions` | Skips all prompts (use only in sandboxed environments) |

### Common Permission Rules

```
Bash(npm run *)        — allow any npm run command
Bash(git *)            — allow all git commands
Bash(python *)         — allow python execution
Read(.env)             — allow reading .env files
Edit(/src/**)          — allow editing anything in src/
WebFetch(domain:github.com) — allow fetching from github.com
mcp__server-name       — allow all tools from an MCP server
```

### Where to Configure

| Command | What it does |
|:--------|:-------------|
| `/permissions` | Interactive UI to add/remove rules |
| `~/.claude/settings.json` | Your personal rules (all projects) |
| `.claude/settings.json` | Project rules (shared with team via git) |
| `.claude/settings.local.json` | Project rules (local only, gitignored) |

---

## Models & Context

### Switching Models

| Method | How |
|:-------|:----|
| During session | `/model` then select, or `/model sonnet` |
| At launch | `claude --model opus` |
| Aliases | `opus`, `sonnet`, `haiku` (resolves to latest version) |

### Effort Levels

| Level | When to use |
|:------|:------------|
| `low` | Simple questions, quick lookups |
| `medium` | Standard tasks (default) |
| `high` | Complex reasoning, architecture decisions |
| `max` | Maximum depth (Opus 4.6 only, session-scoped) |

Set with `/effort high` or `claude --effort high`.

### Context Management

| Command | What it does |
|:--------|:-------------|
| `/context` | See how much context you've used |
| `/compact` | Compress conversation to free space |
| `/clear` | Start fresh (clears everything) |
| `/branch` | Fork here — try something without losing your place |
| `/rewind` | Go back to an earlier point |

---

## CLI Flags

Launch Claude with options for automation, scripting, or custom workflows.

### Most Used Flags

| Flag | What it does | Example |
|:-----|:-------------|:--------|
| `-p "query"` | Print mode — run once and exit | `claude -p "explain this repo"` |
| `-c` | Continue last conversation | `claude -c` |
| `-r <name>` | Resume a named session | `claude -r "my-feature"` |
| `-n <name>` | Name this session | `claude -n "auth-refactor"` |
| `--model` | Choose model | `claude --model sonnet` |
| `--effort` | Set effort level | `claude --effort high` |
| `--add-dir` | Add working directories | `claude --add-dir ../lib ../shared` |
| `--permission-mode` | Set permission mode | `claude --permission-mode plan` |
| `--allowedTools` | Pre-allow specific tools | `claude --allowedTools "Bash(git *)" "Read"` |
| `--fast` | Enable fast mode | `claude --fast` |

### Automation Flags (for scripts and CI)

| Flag | What it does | Example |
|:-----|:-------------|:--------|
| `-p` | Non-interactive mode | `claude -p "fix lint errors"` |
| `--output-format` | Output as `text`, `json`, or `stream-json` | `claude -p --output-format json "query"` |
| `--max-turns` | Limit agent turns | `claude -p --max-turns 5 "query"` |
| `--max-budget-usd` | Spending cap | `claude -p --max-budget-usd 2.00 "query"` |
| `--bare` | Skip all auto-discovery (fastest startup) | `claude --bare -p "quick question"` |
| `--system-prompt` | Replace system prompt entirely | `claude --system-prompt "You are a Python expert"` |
| `--append-system-prompt` | Add to default system prompt | `claude --append-system-prompt "Always use TypeScript"` |

### Piping Content

```bash
# Explain a file
cat error.log | claude -p "what went wrong?"

# Process multiple files
cat src/*.ts | claude -p "find security issues"

# Chain commands
git diff | claude -p "write a commit message for these changes"
```

---

## MCP Servers

MCP (Model Context Protocol) lets Claude connect to external tools and services — databases, APIs, browsers, custom tooling.

### Managing MCP Servers

| Command | What it does |
|:--------|:-------------|
| `claude mcp add <name> <command>` | Add an MCP server |
| `claude mcp remove <name>` | Remove an MCP server |
| `claude mcp list` | List configured servers |
| `/mcp` | Manage servers during a session |

### Example: Adding a Server

```bash
# Add a filesystem server
claude mcp add filesystem npx @anthropic-ai/mcp-filesystem /path/to/dir

# Add a server with environment variables
claude mcp add my-server --env API_KEY=xxx -- npx my-mcp-server

# Load servers from a config file
claude --mcp-config ./mcp-servers.json
```

### Using MCP Tools

Once connected, MCP tools appear alongside Claude's built-in tools. They use the format `mcp__<server-name>__<tool-name>`.

Set permissions for MCP tools:
```
mcp__filesystem           — allow all tools from filesystem server
mcp__filesystem__read     — allow only the read tool
```

---

## Hooks

Hooks are automated actions that run at specific points in Claude's workflow. Define them in your settings.json.

### Hook Events

| Event | When it fires | Can block? |
|:------|:-------------|:-----------|
| `PreToolUse` | Before a tool runs | Yes |
| `PostToolUse` | After a tool succeeds | Yes (feedback) |
| `Stop` | Claude finishes responding | Yes |
| `UserPromptSubmit` | User sends a message | Yes |
| `SessionStart` | Session begins | No |
| `SessionEnd` | Session ends | No |

### Example: Auto-lint After File Edits

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npm run lint --fix",
            "timeout": 30,
            "statusMessage": "Running linter..."
          }
        ]
      }
    ]
  }
}
```

### Example: Block Dangerous Commands

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo $TOOL_INPUT | grep -q 'rm -rf' && exit 2 || exit 0"
          }
        ]
      }
    ]
  }
}
```

### Example: Auto-Save on Stop

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "git add -A && git commit -m 'Auto-save from Claude session'",
            "timeout": 30,
            "statusMessage": "Auto-saving changes..."
          }
        ]
      }
    ]
  }
}
```

### Hook Exit Codes

| Code | Meaning |
|:-----|:--------|
| 0 | Success — continue normally |
| 2 | Block — stop the action, show error |
| Other | Non-blocking error — log and continue |

### View Hooks

Type `/hooks` to see all configured hooks, their sources, and their status.

---

## Plugins & Skills

### Plugins

Plugins are packaged extensions from community marketplaces.

| Command | What it does |
|:--------|:-------------|
| `/plugin install <name>` | Install a plugin |
| `/plugin install <owner/repo>` | Install from a GitHub repo |
| `/plugin list` | List installed plugins |
| `/plugin remove <name>` | Remove a plugin |
| `/plugin marketplace add <owner/repo>` | Add a marketplace source |

**Example — Install Pathfinder Skills:**
```
/plugin install ChewbaccaRoars/pathfinder-skills
```
This installs 19 skills including `/pathfinder`, `/learn`, `/build`, `/reflect`, and `/share`.

### Skills

Skills are `.md` files that teach Claude new behaviors. They live in `~/.claude/skills/<name>/SKILL.md` (personal) or `.claude/skills/<name>/SKILL.md` (project).

| Command | What it does |
|:--------|:-------------|
| `/skills` | List all available skills |
| `/<skill-name>` | Invoke a skill directly |

**Skill file structure:**
```
my-skill/
├── SKILL.md           # Instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/          # Example outputs
└── scripts/           # Scripts Claude can execute
```

**SKILL.md format:**
```yaml
---
name: my-skill
description: What it does and when to use it
---

Instructions for Claude go here...
```

**Key frontmatter options:**

| Field | What it does |
|:------|:-------------|
| `name` | Slash command name |
| `description` | When Claude should use this skill |
| `disable-model-invocation: true` | Only you can trigger it (not Claude) |
| `user-invocable: false` | Only Claude can trigger it (hidden from `/` menu) |
| `context: fork` | Run in an isolated subagent |
| `allowed-tools` | Tools available when this skill is active |

---

## Settings & Config

### Settings Files (highest to lowest priority)

| File | Scope | Shared? |
|:-----|:------|:--------|
| Managed settings (enterprise) | All users | Admin-controlled |
| `~/.claude/settings.json` | All your projects | No (personal) |
| `.claude/settings.json` | This project | Yes (commit to git) |
| `.claude/settings.local.json` | This project | No (gitignored) |

### Quick Config Commands

| Command | What it does |
|:--------|:-------------|
| `/config` | Open interactive settings UI |
| `/theme` | Change color theme |
| `/model` | Switch model |
| `/effort` | Set effort level |
| `/fast` | Toggle fast mode |
| `/permissions` | Manage allow/deny rules |

### CLAUDE.md (Memory)

Claude reads `CLAUDE.md` files for project context and instructions.

| Location | Loaded when |
|:---------|:------------|
| `~/CLAUDE.md` | Every session (personal) |
| `CLAUDE.md` in project root | When working in that project |
| `.claude/CLAUDE.md` | Same as above |
| Auto-memory (`~/.claude/projects/*/memory/`) | Persistent notes across sessions |

Manage with `/memory` or `/init`.

---

## Quick Reference Card

### The Big Five (start here)

| What you want | What to type |
|:-------------|:-------------|
| See all commands | `/help` |
| Switch models | `/model sonnet` |
| Free up context | `/compact` |
| Check usage/cost | `/cost` |
| See what's allowed | `/permissions` |

### Daily Workflow

```
claude                          # start a session
claude -c                       # continue where you left off
claude -r "my-feature"          # resume a named session
claude -p "quick question"      # ask and exit
git diff | claude -p "review"   # pipe content in
```

### Key Shortcuts (in interactive mode)

| Shortcut | What it does |
|:---------|:-------------|
| `Esc` | Cancel current generation |
| `Up Arrow` | Recall previous message |
| `Ctrl+C` | Cancel or exit |
| `!command` | Run a shell command inline |
| `/` then type | Filter available commands |
