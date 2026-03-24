# Hooks — Hands-On Exercises

> New to technical terms? See the [Plain-English Glossary](../glossary.md) for jargon-free definitions.

Hooks are automated actions that run at specific points in Claude's workflow. Think of them as "when this happens, do that" rules. They live in your settings.json.

---

## Hook Events Reference

| Event | When it fires | Can block? |
|:------|:-------------|:-----------|
| `SessionStart` | Session begins or resumes | No |
| `UserPromptSubmit` | User sends a message | Yes |
| `PreToolUse` | Before a tool runs | Yes |
| `PostToolUse` | After a tool succeeds | Yes (feedback) |
| `PostToolUseFailure` | Tool execution fails | No |
| `Stop` | Claude finishes responding | Yes |
| `SessionEnd` | Session ends | No |
| `Notification` | Notification sent | No |

## Hook Types

| Type | What it is |
|:-----|:-----------|
| `command` | Runs a shell command — receives JSON on stdin, returns via exit codes |
| `http` | Sends JSON via HTTP POST to a URL |
| `prompt` | Single-turn LLM evaluation (yes/no decisions) |
| `agent` | Spawns a subagent with full tool access |

---

## Exercise 1: View Configured Hooks

**What you'll learn:** How to see what hooks are currently active.

1. Type `/hooks` in Claude Code
2. Browse the list — each hook shows its event, matcher, command, and source file
3. If you haven't configured any hooks, the list will be empty

**What to expect:** A summary of all hooks with where they're defined.

**Pro tip:** Hooks can come from multiple sources — personal settings, project settings, plugins, and skill frontmatter.

---

## Exercise 2: Auto-Lint After File Edits

**What you'll learn:** How to automatically run a linter every time Claude edits a file.

1. Open your settings file (either `~/.claude/settings.json` or `.claude/settings.json`)
2. Add this configuration:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$CLAUDE_PROJECT_DIR\" && npm run lint 2>/dev/null || true",
            "timeout": 30,
            "statusMessage": "Running linter..."
          }
        ]
      }
    ]
  }
}
```

3. Start a new Claude session
4. Ask Claude to edit a file
5. After the edit, you'll see "Running linter..." in the status bar
6. If lint errors are found, they appear as feedback to Claude

**What to expect:** Every file edit triggers the linter automatically. Claude sees the lint output and can fix issues.

**Pro tip:** The `|| true` at the end prevents the hook from blocking on lint errors. Remove it if you want lint failures to block the edit.

---

## Exercise 3: Block Dangerous Commands

**What you'll learn:** How to prevent specific bash commands from running.

1. Create a hook script at `.claude/hooks/block-dangerous.sh`:

```bash
#!/bin/bash
# Read the tool input from stdin
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)

# Block dangerous patterns
if echo "$COMMAND" | grep -qE 'rm -rf|drop table|format |shutdown|mkfs'; then
  echo "BLOCKED: This command is not allowed" >&2
  exit 2
fi

# Allow everything else
exit 0
```

2. Make it executable: `chmod +x .claude/hooks/block-dangerous.sh`
3. Add to your settings:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block-dangerous.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

4. Ask Claude to run `rm -rf /tmp/test` — it gets blocked
5. Ask Claude to run `ls -la` — it runs normally

**What to expect:** Exit code 2 = blocked (stderr shown to user). Exit code 0 = allowed.

**Pro tip:** PreToolUse hooks run BEFORE the permission prompt, so they can block actions even if they're in your allow list.

---

## Exercise 4: Auto-Save When Claude Stops

**What you'll learn:** How to automatically commit changes when Claude finishes a response.

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$CLAUDE_PROJECT_DIR\" && git diff --quiet && exit 0; git add -A && git commit -m 'Auto-save from Claude session' 2>/dev/null || true",
            "timeout": 15,
            "statusMessage": "Auto-saving changes..."
          }
        ]
      }
    ]
  }
}
```

**How it works:**
- `git diff --quiet && exit 0` — if there are no changes, do nothing
- `git add -A && git commit` — if there ARE changes, commit them
- Runs every time Claude finishes responding

**What to expect:** After every Claude response that changes files, you'll see "Auto-saving changes..." and a git commit is created.

**Pro tip:** This creates a lot of commits. Consider adding a check for meaningful changes, or use this only during experimental sessions.

---

## Exercise 5: Log All Prompts

**What you'll learn:** How to keep a log of everything you ask Claude.

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import sys,json,datetime; d=json.load(sys.stdin); f=open('claude-prompt-log.txt','a'); f.write(f'{datetime.datetime.now().isoformat()} | {d.get(\\\"content\\\",\\\"\\\")[:200]}\\n'); f.close()\"",
            "timeout": 5,
            "statusMessage": "Logging prompt..."
          }
        ]
      }
    ]
  }
}
```

**What to expect:** A `claude-prompt-log.txt` file grows with each prompt you send, timestamped.

**Pro tip:** This is useful for tracking what you've worked on, creating a session log, or auditing usage.

---

## Exercise 6: Conditional Hooks with Matchers

**What you'll learn:** How to make hooks fire only for specific tools.

**Matcher patterns:**

| Pattern | Matches |
|:--------|:--------|
| `"Bash"` | Only bash commands |
| `"Edit\|Write"` | Edit OR Write tools |
| `"mcp__.*"` | Any MCP tool (regex) |
| `"mcp__db__write.*"` | MCP db server write tools |
| `""` or omitted | ALL tool uses (always fires) |

**Example — run tests only after Python file edits:**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import sys,json; d=json.load(sys.stdin); p=d.get('tool_input',{}).get('file_path',''); exit(0 if p.endswith('.py') else 1)\" && cd \"$CLAUDE_PROJECT_DIR\" && python -m pytest -x --tb=short 2>&1 | tail -20 || true",
            "timeout": 60,
            "statusMessage": "Running tests..."
          }
        ]
      }
    ]
  }
}
```

**Pro tip:** The first python command checks if the edited file is a .py file. If not, it exits 1 (non-blocking skip). If yes, it runs pytest.

---

## Hook Configuration Reference

```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "tool_name_regex",
        "hooks": [
          {
            "type": "command",
            "command": "your-script.sh",
            "timeout": 30,
            "statusMessage": "What the user sees...",
            "async": false
          }
        ]
      }
    ]
  }
}
```

### Exit Codes

| Code | Meaning |
|:-----|:--------|
| 0 | Success — continue normally |
| 2 | Block — stop the action, show stderr to user |
| Other | Non-blocking error — log and continue |

### Environment Variables Available

| Variable | What it contains |
|:---------|:----------------|
| `$CLAUDE_PROJECT_DIR` | The project root directory |
| `$TOOL_INPUT` | JSON string of the tool's input |
| `$TOOL_RESPONSE` | JSON string of the tool's response (PostToolUse only) |

### Where to Define Hooks

| File | Scope |
|:-----|:------|
| `~/.claude/settings.json` | All your projects |
| `.claude/settings.json` | This project (shared with team) |
| `.claude/settings.local.json` | This project (local only) |
| Plugin `hooks/hooks.json` | Plugin-scoped |
| Skill frontmatter | Skill-scoped |
