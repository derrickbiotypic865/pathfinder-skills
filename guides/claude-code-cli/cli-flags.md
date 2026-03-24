# CLI Flags — Hands-On Exercises

> New to technical terms? See the [Plain-English Glossary](../glossary.md) for jargon-free definitions.

Control Claude Code's behavior at launch time. These flags are especially useful for automation, scripting, and custom workflows.

## Plain-English Glossary

Before we start, here are the technical terms you'll see in this guide:

| Term | What it means |
|:-----|:-------------|
| **Flag** | An option you add after `claude` to change how it behaves. Like adding `-p` or `--model sonnet`. Think of flags as settings you choose at startup. |
| **CLI** | "Command Line Interface" — the text-based way to interact with your computer by typing commands instead of clicking icons. |
| **Terminal** | The app where you type commands. On Windows: Git Bash, PowerShell, or Command Prompt. On Mac: Terminal. On Linux: Terminal. |
| **Piping** | Sending the output of one command as the input to another, using the `|` character. It's like an assembly line — one step finishes, passes its result to the next. |
| **stdin / stdout** | "Standard input" and "standard output" — when you pipe content, it goes into stdin. When Claude responds, it comes out of stdout. Think of stdin as "what goes in" and stdout as "what comes out." |
| **Print mode (`-p`)** | A mode where Claude answers your question and immediately exits — no back-and-forth conversation. Like texting someone a question vs. having a phone call. |
| **Session** | A conversation with Claude. It has history, context, and can be resumed later. Like a chat thread. |
| **JSON** | A structured data format that computers can easily read. Looks like `{"name": "Ben", "role": "builder"}`. Used when other programs need to process Claude's output. |

---

## Exercise 1: Print Mode (-p)

**What you'll learn:** How to use Claude as a one-shot tool — ask a question, get an answer, exit.

**In plain English:** Normally when you type `claude`, it opens a conversation you can go back and forth in (like a phone call). With `-p`, you ask ONE question, get ONE answer, and it's done (like sending a text message). This is useful when you just need a quick answer or want to use Claude inside a script.

1. In your terminal (not inside Claude):
```bash
claude -p "what is a Dockerfile?"
```
2. Claude answers and exits — no interactive session
3. Try with a file (the `<` symbol feeds a file's contents to Claude):
```bash
claude -p "explain this code" < my-script.py
```
4. Try piping (the `|` symbol sends one command's output to another — like an assembly line):
```bash
cat error.log | claude -p "what went wrong in this log?"
```
This does two things: `cat error.log` reads the file, then `|` sends its contents to Claude along with your question.

5. Chain with other commands:
```bash
git diff | claude -p "write a concise commit message for these changes"
```
This takes the output of `git diff` (a list of code changes) and asks Claude to write a commit message based on it.

**What to expect:** The answer appears in your terminal and Claude exits. No interactive prompt. It's like asking a question at a drive-through — you get your answer and drive on.

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

**In plain English:** "Piping" means connecting two commands with the `|` character so the output of the first command becomes the input of the second. Think of it like an assembly line:

```
[Command 1 makes something] --pipe--> [Command 2 uses it]
[cat reads a file]          ---|-->    [Claude analyzes it]
```

The `cat` command reads a file and outputs its contents. The `|` pipe sends those contents to Claude. Claude reads them and responds to your question. Here are practical examples:

```bash
# Read a log file and ask Claude what went wrong
# cat = "read this file and show its contents"
# | = "send that to the next command"
# claude -p = "answer this question and exit"
cat error.log | claude -p "what went wrong?"

# Show code changes and ask Claude to review them
# git diff = "show me what changed in my code"
git diff | claude -p "review these changes for issues"

# Show staged changes and ask for a commit message
# git diff --staged = "show changes I'm about to commit"
git diff --staged | claude -p "write a commit message"

# Read a README and ask for a summary
cat README.md | claude -p "summarize in 3 bullet points"

# Read all Python files and check for security issues
# find = "search for files matching a pattern"
find . -name "*.py" -exec cat {} \; | claude -p "find security issues"

# Fix broken JSON and save the result
# The > symbol saves output to a file (instead of showing it on screen)
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
