# CLI Flags — Hands-On Exercises

Control Claude Code's behavior at launch time. These flags are especially useful for automation, scripting, and custom workflows.

---

## Exercise 1: Print Mode (-p)

**What you'll learn:** How to use Claude as a one-shot tool — ask a question, get an answer, exit.

1. In your terminal (not inside Claude):
```bash
claude -p "what is a Dockerfile?"
```
2. Claude answers and exits — no interactive session
3. Try with a file:
```bash
claude -p "explain this code" < my-script.py
```
4. Try piping:
```bash
cat error.log | claude -p "what went wrong in this log?"
```
5. Chain with other commands:
```bash
git diff | claude -p "write a concise commit message for these changes"
```

**What to expect:** Output goes to stdout. No interactive prompt. Great for scripts and piping.

**Pro tip:** `-p` is the key to using Claude in shell scripts, CI pipelines, and automation. Combine with `--output-format json` for machine-readable output.

---

## Exercise 2: Output Formats

**What you'll learn:** How to get Claude's output in different formats.

```bash
# Plain text (default)
claude -p "list 3 JavaScript frameworks" --output-format text

# JSON (structured, machine-readable)
claude -p "list 3 JavaScript frameworks" --output-format json

# Streaming JSON (real-time events)
claude -p "list 3 JavaScript frameworks" --output-format stream-json
```

**When to use each:**

| Format | Best for |
|:-------|:---------|
| `text` | Human reading, piping to other tools |
| `json` | Scripts that parse the response programmatically |
| `stream-json` | Real-time processing, progress monitoring |

**Pro tip:** Pipe JSON output into `jq` for parsing: `claude -p "query" --output-format json | jq '.result'`

---

## Exercise 3: Session Management Flags

**What you'll learn:** How to manage sessions from the command line.

```bash
# Start a named session
claude -n "refactor-auth"

# Continue the last session in this directory
claude -c

# Resume a specific session by name
claude -r "refactor-auth"

# Resume with a follow-up prompt
claude -r "refactor-auth" "now add error handling"

# Continue in print mode (one-shot follow-up)
claude -c -p "run the tests"

# Fork a session (continue without modifying original)
claude -r "refactor-auth" --fork-session
```

**Pro tip:** `-c -p "query"` is powerful — continue a conversation with a one-shot command without entering interactive mode.

---

## Exercise 4: Model and Effort Flags

**What you'll learn:** How to control the model at launch.

```bash
# Use a specific model
claude --model sonnet
claude --model opus
claude --model haiku

# Set effort level
claude --effort high
claude --effort max  # Opus 4.6 only

# Combine
claude --model opus --effort high

# Use fast mode
claude --fast

# Set a fallback model for rate limits (print mode)
claude -p --fallback-model sonnet "complex query"
```

**Pro tip:** `--model opus --effort max` gives you the absolute maximum reasoning power. Use it for the hardest problems.

---

## Exercise 5: Permission and Security Flags

**What you'll learn:** How to control permissions from the command line.

```bash
# Start in plan mode (read-only, can't modify anything)
claude --permission-mode plan

# Pre-allow specific tools
claude --allowedTools "Bash(git *)" "Bash(npm *)" "Read"

# Block specific tools
claude --disallowedTools "Bash(rm *)" "Edit(.env)"

# Accept all file edits automatically
claude --permission-mode acceptEdits
```

**Pro tip:** `--permission-mode plan` is great for code review — Claude can read and analyze everything but can't change anything.

---

## Exercise 6: Automation Flags

**What you'll learn:** How to use Claude safely in automated workflows.

```bash
# Limit the number of agent turns
claude -p --max-turns 5 "fix the failing tests"

# Set a spending cap
claude -p --max-budget-usd 2.00 "refactor this module"

# Fastest possible startup (skip auto-discovery)
claude --bare -p "what time is it in UTC?"

# Custom system prompt
claude --append-system-prompt "Always respond in bullet points" -p "explain REST APIs"

# Load system prompt from file
claude --append-system-prompt-file ./my-rules.txt -p "review this code"
```

**Flag safety reference:**

| Flag | What it prevents |
|:-----|:----------------|
| `--max-turns` | Runaway agent loops |
| `--max-budget-usd` | Unexpected costs |
| `--bare` | Slow startup from loading plugins/hooks/MCP |
| `--permission-mode plan` | Any file modifications |

**Pro tip:** For CI/CD pipelines, always use `--max-turns` and `--max-budget-usd` to prevent runaway costs.

---

## Exercise 7: Working Directories

**What you'll learn:** How to give Claude access to multiple directories.

```bash
# Add directories at launch
claude --add-dir ../shared-lib ../config

# Or during a session
/add-dir ../other-project
```

**What to expect:** Claude can now read and edit files in those directories too, following the same permission rules.

**Pro tip:** Useful for monorepos or when you need Claude to understand code across multiple projects.

---

## Exercise 8: Piping Recipes

**What you'll learn:** Practical examples of piping content into Claude.

```bash
# Explain an error log
cat error.log | claude -p "what went wrong?"

# Review a diff
git diff | claude -p "review these changes for issues"

# Generate a commit message
git diff --staged | claude -p "write a commit message"

# Summarize a file
cat README.md | claude -p "summarize in 3 bullet points"

# Process multiple files
find . -name "*.py" -exec cat {} \; | claude -p "find security issues"

# Chain: fix errors and pipe the result
cat broken.json | claude -p "fix this JSON" > fixed.json
```

**Pro tip:** Piping works with any command that outputs text. If you can `cat` it, you can pipe it to Claude.

---

## Quick Reference

| Flag | What it does |
|:-----|:-------------|
| `-p "query"` | Print mode (non-interactive) |
| `-c` | Continue last session |
| `-r "name"` | Resume named session |
| `-n "name"` | Name this session |
| `--model opus` | Choose model |
| `--effort high` | Set thinking depth |
| `--fast` | Faster output |
| `--output-format json` | JSON output |
| `--max-turns N` | Limit agent turns |
| `--max-budget-usd N` | Spending cap |
| `--bare` | Skip auto-discovery |
| `--add-dir path` | Add working directory |
| `--permission-mode plan` | Read-only mode |
| `--allowedTools "..."` | Pre-allow tools |
| `--append-system-prompt` | Add to system prompt |
