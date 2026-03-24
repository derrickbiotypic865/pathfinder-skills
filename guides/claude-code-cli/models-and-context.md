# Models & Context — Hands-On Exercises

Learn how to pick the right model, manage your context window, and navigate conversations like a pro.

---

## Exercise 1: Switch Between Models

**What you'll learn:** How to change models and when to use each one.

1. Type `/model` — a picker shows available models
2. Select **Sonnet** — fast, great for everyday work
3. Ask: "What model are you?" — confirms the switch
4. Type `/model opus` — switches to Opus directly (skip the picker)
5. Ask a complex question — notice the deeper reasoning
6. Type `/model haiku` — switches to the fastest, cheapest model

**Model cheat sheet:**

| Model | Speed | Best for |
|:------|:------|:---------|
| **Haiku** | Fastest | Quick questions, simple tasks, high-volume work |
| **Sonnet** | Fast | Daily coding, most tasks, good balance |
| **Opus** | Slower | Complex reasoning, architecture, difficult bugs |

**Pro tip:** Start with Sonnet. Switch to Opus when you're stuck or need deep analysis. Use Haiku for quick lookups.

---

## Exercise 2: Effort Levels

**What you'll learn:** How to control how deeply Claude thinks about your question.

1. Type `/effort low` — Claude responds quickly with minimal analysis
2. Ask: "What are the pros and cons of microservices?"
3. Type `/effort high` — Claude thinks more deeply
4. Ask the same question — notice the more thorough response
5. Type `/effort max` — maximum depth (Opus 4.6 only, current session only)
6. Type `/effort auto` — reset to default

**Effort levels:**

| Level | Persists? | What it does |
|:------|:----------|:-------------|
| `low` | Yes | Quick responses, minimal analysis |
| `medium` | Yes | Standard depth (default) |
| `high` | Yes | Deep analysis, considers more angles |
| `max` | Session only | Maximum depth, Opus 4.6 only |
| `auto` | — | Resets to model default |

**Pro tip:** You can also set effort at launch: `claude --effort high`. In the `/model` picker, use left/right arrows to adjust effort.

---

## Exercise 3: Context Visualization

**What you'll learn:** How to see and manage your context usage.

1. Have a conversation (10+ messages)
2. Type `/context` — a colored grid appears:
   - Green = free space
   - Yellow = used
   - Red = near the limit
3. Look for optimization suggestions — Claude may suggest compacting or removing large file reads

**What to expect:** A visual map of your context. If you see mostly yellow/red, it's time to compact.

**Pro tip:** Large file reads and long conversations eat context fast. `/context` helps you spot what's using the most space.

---

## Exercise 4: Compact Conversations

**What you'll learn:** How to free up context without losing important information.

1. Have a long conversation (15+ messages)
2. Type `/context` — note how much is used
3. Type `/compact` — Claude compresses the conversation
4. Type `/context` again — notice the freed space
5. Now try with focus: `/compact keep the database discussion and the API design`
6. Claude preserves those topics while compressing everything else

**What to expect:** After compacting, Claude still remembers key points but the raw messages are compressed. It's like going from a transcript to meeting notes.

**Pro tip:** Regular compacting keeps your session healthy. Do it whenever `/context` shows you're above 60-70% usage. The focus instructions let you protect important topics.

---

## Exercise 5: Branch and Rewind

**What you'll learn:** How to try risky changes safely and undo them.

1. You're working on a feature. Things are going well.
2. Type `/branch safe-point` — creates a snapshot
3. Ask Claude to try a risky refactor: "Rewrite this module using a completely different approach"
4. Look at the result — not great
5. Type `/rewind` — a list of checkpoints appears
6. Select your "safe-point" — conversation AND code revert to that moment
7. You're back to the good state. The risky refactor never happened.

**What to expect:** `/rewind` shows checkpoints with timestamps. Selecting one restores both the conversation and your files.

**Pro tip:** Always `/branch` before asking Claude to make big architectural changes. It's free insurance.

---

## Exercise 6: Session Resuming

**What you'll learn:** How to pick up exactly where you left off.

**Method 1 — Continue last session:**
```bash
claude -c
```
Loads the most recent session in the current directory.

**Method 2 — Resume by name:**
```bash
claude -n "auth-feature"     # name your session when you start
# ... work for a while ...
claude -r "auth-feature"     # resume it later
```

**Method 3 — Interactive picker:**
```bash
claude -r                    # or /resume in a session
```
Shows all past sessions with names, dates, and directories.

**Method 4 — Fork on resume:**
```bash
claude -r "auth-feature" --fork-session
```
Creates a new branch of the session instead of continuing the original.

**Pro tip:** Name important sessions with `-n`. It makes them easy to find later among dozens of unnamed sessions.

---

## Quick Reference

| What you want | Command |
|:-------------|:--------|
| Switch model | `/model sonnet` or `/model opus` |
| Set effort | `/effort high` |
| See context usage | `/context` |
| Free up context | `/compact` |
| Start fresh | `/clear` |
| Create checkpoint | `/branch name` |
| Go back in time | `/rewind` |
| Continue last session | `claude -c` |
| Resume named session | `claude -r "name"` |
| Name current session | `/rename my-feature` |
