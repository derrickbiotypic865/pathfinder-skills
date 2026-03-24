# Slash Commands — Hands-On Exercises

> New to technical terms? See the [Plain-English Glossary](../glossary.md) for jargon-free definitions.

These exercises walk you through the most useful Claude Code slash commands. Try each one in a live Claude Code session.

---

## Exercise 1: Discover Commands

**What you'll learn:** How to find and filter slash commands.

1. Type `/` in the prompt — a list of all available commands appears
2. Start typing letters after `/` to filter — try `/co` and watch it narrow to `/compact`, `/config`, `/context`, `/copy`, `/cost`
3. Use arrow keys to browse, press Enter to select
4. Try `/help` to see a summary of key commands

**What to expect:** A filterable list of 40+ commands. You don't need to memorize them — just type `/` and start filtering.

**Pro tip:** Custom skills (like `/pathfinder` or `/learn`) appear in the same list alongside built-in commands.

---

## Exercise 2: Switch Models

**What you'll learn:** How to change which AI model you're using.

1. Type `/model`
2. A picker appears showing available models — use arrow keys to browse
3. Select **Sonnet** — notice it switches immediately
4. Ask Claude a question — it responds using Sonnet
5. Type `/model opus` to switch directly without the picker
6. Type `/model` again and use left/right arrows to adjust effort level

**What to expect:** The model name in your status bar changes. Different models have different speeds and capabilities.

**Pro tip:** Use `sonnet` for fast everyday work, `opus` for complex reasoning. `/fast` toggles faster output on the same model.

---

## Exercise 3: Manage Context

**What you'll learn:** How to see and free up context when conversations get long.

1. Have a conversation with Claude (at least 5-10 messages)
2. Type `/context` — a colored grid shows how much context you've used
3. Type `/compact` — Claude compresses the conversation, freeing space
4. Type `/compact keep the discussion about APIs` — compresses but preserves specific topics
5. Type `/context` again — notice the freed space

**What to expect:** The context grid shows green (free), yellow (used), red (near limit). After compacting, you'll see more green.

**Pro tip:** Claude auto-compacts when it gets close to the limit, but doing it manually with focus instructions gives you better control over what's preserved.

---

## Exercise 4: Review Code Changes

**What you'll learn:** How to interactively review what Claude changed.

1. Ask Claude to make a code change (edit a file or create one)
2. Type `/diff`
3. An interactive viewer opens showing all uncommitted changes
4. Use **left/right arrows** to switch between the full git diff and individual Claude turns
5. Use **up/down arrows** to browse between files
6. Press `q` or `Esc` to exit

**What to expect:** A colored diff view — green lines are additions, red are deletions. Each turn shows exactly what Claude changed.

**Pro tip:** This is essential for reviewing changes before committing. Always `/diff` before you `git commit`.

---

## Exercise 5: Session Management

**What you'll learn:** How to name, resume, and manage sessions.

1. Type `/rename auth-refactor` — your session now has a name
2. Notice the name appears in the prompt bar
3. Type `/exit` to leave
4. In your terminal, type `claude -r auth-refactor` — you're back exactly where you left off
5. Start a new session: `claude`
6. Type `/resume` — a picker shows all your past sessions

**What to expect:** Named sessions are easy to find and resume. The picker shows session names, dates, and directories.

**Pro tip:** `claude -c` continues the most recent session in the current directory without the picker.

---

## Exercise 6: Conversation Branching

**What you'll learn:** How to fork conversations and rewind to earlier points.

1. Have a conversation with Claude (ask a few questions, make some changes)
2. Type `/branch experiment` — creates a fork at this point
3. Try something risky — ask Claude to make a big change
4. Don't like the result? Type `/rewind`
5. A list of checkpoints appears — pick an earlier point
6. You're back to before the risky change, with all your code restored

**What to expect:** Branching creates a snapshot. Rewinding lets you go back to any point in the conversation AND restores your code to that state.

**Pro tip:** Use `/branch` before trying something you're not sure about. It's your undo button for entire conversations.

---

## Exercise 7: Export Content

**What you'll learn:** How to get content out of Claude Code.

1. Ask Claude to explain something or generate some content
2. Type `/copy` — the last response is copied to your clipboard
3. Type `/copy 2` — copies the second-to-last response
4. If there are code blocks, a picker lets you choose individual blocks or the full response
5. Type `/export` — options to copy the whole conversation or save to a file
6. Type `/export conversation.txt` — saves directly to that file

**What to expect:** `/copy` is quick (clipboard), `/export` is comprehensive (whole conversation).

**Pro tip:** `/copy` with code blocks shows a picker — useful when you want just the code, not the explanation around it.

---

## Exercise 8: Project Memory

**What you'll learn:** How to set up persistent context for a project.

1. Navigate to a project directory
2. Type `/init` — Claude walks you through creating a CLAUDE.md
3. Answer the prompts about your project
4. Type `/memory` — see all memory files and auto-memory settings
5. Edit a memory file to add instructions like "always use TypeScript" or "run tests before committing"
6. Start a new session in the same directory — Claude remembers your instructions

**What to expect:** `/init` creates a CLAUDE.md in your project. `/memory` shows all loaded memory sources.

**Pro tip:** CLAUDE.md at `~/CLAUDE.md` loads for ALL projects. Project-level CLAUDE.md files load only in that project.

---

## Exercise 9: Bundled Skills

**What you'll learn:** How to use Claude's built-in prompt-based skills.

1. Type `/simplify` — Claude reviews your recent changes for quality issues and fixes them
2. Type `/debug` — Claude reads the session debug log and troubleshoots issues
3. Type `/batch migrate all .js files to .ts` — Claude plans and executes parallel work (requires a git repo)
4. Type `/loop 5m check if the tests pass` — runs a check every 5 minutes

**What to expect:** Bundled skills are more sophisticated than simple commands — they spawn agents, read files, and adapt to your codebase.

**Pro tip:** `/batch` is incredibly powerful for large-scale changes. It creates a plan, shows you for approval, then spawns parallel agents in git worktrees.

---

## Exercise 10: Quick Side Questions

**What you'll learn:** How to ask a question without polluting your conversation.

1. You're in the middle of a complex task
2. Type `/btw what's the syntax for a JavaScript map function?`
3. Claude answers the side question without adding it to the conversation history
4. Your main conversation continues uninterrupted

**What to expect:** The answer appears but doesn't consume context or change Claude's focus.

**Pro tip:** Use `/btw` for quick lookups, syntax checks, or "how do I..." questions while you're focused on something else.

---

## Quick Reference

| Command | One-line summary |
|:--------|:----------------|
| `/` then type | Filter all commands |
| `/model` | Switch models |
| `/effort` | Set thinking depth |
| `/compact` | Free up context |
| `/context` | See context usage |
| `/diff` | Review code changes |
| `/rename` | Name your session |
| `/resume` | Resume a past session |
| `/branch` | Fork conversation |
| `/rewind` | Go back in time |
| `/copy` | Copy response to clipboard |
| `/export` | Save conversation to file |
| `/init` | Set up project memory |
| `/memory` | Edit memory files |
| `/btw` | Quick side question |
| `/batch` | Parallel codebase changes |
| `/simplify` | Review and fix code quality |
