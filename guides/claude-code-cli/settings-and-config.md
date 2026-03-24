# Settings & Config — Hands-On Exercises

Customize your Claude Code environment — from themes and models to CLAUDE.md memory files that give Claude persistent context about your project.

---

## Exercise 1: The Config Interface

**What you'll learn:** How to change settings through the interactive UI.

1. Type `/config` (or `/settings`)
2. Browse the available options:
   - **Model**: which AI model to use
   - **Theme**: light/dark/colorblind-accessible
   - **Output style**: how Claude formats responses
   - **Other preferences**: fast mode, effort level, etc.
3. Make a change — try switching the theme
4. Type `/theme` for a dedicated theme picker with previews

**Quick display commands:**

| Command | What it changes |
|:--------|:---------------|
| `/config` | Opens full settings UI |
| `/theme` | Color theme |
| `/color blue` | Prompt bar color (session only) |
| `/model` | AI model |
| `/effort` | Thinking depth |
| `/fast` | Faster output toggle |
| `/vim` | Vim editing mode toggle |

**Pro tip:** `/status` shows your current version, model, account, and connectivity all at once.

---

## Exercise 2: Settings File Locations

**What you'll learn:** Where settings live and which takes priority.

**Priority (highest wins):**

| Priority | File | Scope |
|:---------|:-----|:------|
| 1 (highest) | Managed settings | Enterprise admin (can't override) |
| 2 | CLI flags | This launch only |
| 3 | `.claude/settings.local.json` | This project, local (gitignored) |
| 4 | `.claude/settings.json` | This project, shared (commit to git) |
| 5 (lowest) | `~/.claude/settings.json` | Personal, all projects |

**Try it:**
1. Open `~/.claude/settings.json` — your personal settings
2. Look at what's there (model, permissions, hooks, etc.)
3. Check if your project has `.claude/settings.json` or `.claude/settings.local.json`
4. Remember: a deny rule at ANY level blocks the action everywhere

**Pro tip:** Put team-shared rules in `.claude/settings.json` (committed to git). Put your personal preferences in `~/.claude/settings.json`. Put sensitive or local-only rules in `.claude/settings.local.json`.

---

## Exercise 3: CLAUDE.md Memory Files

**What you'll learn:** How to give Claude persistent context about your project.

CLAUDE.md files are markdown files that Claude reads at the start of every session. They're instructions, context, and memory.

**Where they load from:**

| Location | When it loads |
|:---------|:-------------|
| `~/CLAUDE.md` | Every session (personal) |
| `CLAUDE.md` in project root | When working in that project |
| `.claude/CLAUDE.md` | Same as above (alternative location) |

**Try it:**
1. Create a file called `CLAUDE.md` in your project root:

```markdown
# Project Context

This is a Node.js project using Express and PostgreSQL.

## Rules
- Always use TypeScript
- Use async/await, never callbacks
- Run `npm test` before committing
- Never commit .env files
```

2. Start a new Claude session in that directory
3. Ask Claude to write some code — it follows your rules automatically

**Pro tip:** Keep CLAUDE.md concise. Claude reads it every session, so long files waste context. Put detailed docs in separate files and reference them.

---

## Exercise 4: Auto-Memory

**What you'll learn:** How Claude saves and retrieves information across sessions.

1. Type `/memory` to see all memory sources
2. Look for **auto-memory** — Claude's persistent notes
3. Auto-memory lives in `~/.claude/projects/<project-hash>/memory/`
4. `MEMORY.md` is always loaded (first 200 lines)
5. Additional topic files can be created for detailed notes

**Managing auto-memory:**
- Tell Claude "remember that we always use port 3000" — it saves to memory
- Tell Claude "forget about the port setting" — it removes the entry
- `/memory` > toggle auto-memory on/off

**What to expect:** Claude remembers things you tell it across sessions — preferences, decisions, patterns, project-specific knowledge.

**Pro tip:** Auto-memory is best for stable facts ("this project uses PostgreSQL") not temporary state ("I'm working on the auth bug"). Keep MEMORY.md under 200 lines.

---

## Exercise 5: Initialize a Project

**What you'll learn:** How to set up Claude Code for a new project.

1. Navigate to your project directory
2. Type `/init`
3. Claude walks you through creating a CLAUDE.md:
   - What kind of project is this?
   - What language/framework?
   - Any conventions or rules?
4. A CLAUDE.md file is created in your project root

**For the interactive flow** (more thorough):
```bash
CLAUDE_CODE_NEW_INIT=true claude --init
```
This walks through skills, hooks, and personal memory files too.

**Pro tip:** Run `/init` at the start of any new project. The 2 minutes you spend setting up CLAUDE.md saves hours of repeating context.

---

## Exercise 6: Customizing Settings Directly

**What you'll learn:** How to edit settings files for precise control.

Open `~/.claude/settings.json` in any text editor:

```json
{
  "model": "claude-sonnet-4-6",
  "permissions": {
    "allow": [
      "Bash(npm *)",
      "Bash(git *)",
      "Bash(python *)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npm run lint --fix 2>/dev/null || true",
            "timeout": 30,
            "statusMessage": "Linting..."
          }
        ]
      }
    ]
  }
}
```

**What you can configure:**

| Setting | What it controls |
|:--------|:----------------|
| `model` | Default model |
| `permissions.allow` | Tools Claude can use without asking |
| `permissions.deny` | Tools Claude can never use |
| `hooks` | Automated actions on events |
| `defaultMode` | Permission mode (default, acceptEdits, plan, etc.) |
| `additionalDirectories` | Extra directories Claude can access |

**Pro tip:** After editing settings, start a new session for changes to take effect. Or use `/config` for changes that apply immediately.

---

## Quick Reference

### Commands

| Command | What it does |
|:--------|:-------------|
| `/config` | Interactive settings UI |
| `/theme` | Change color theme |
| `/status` | Show version, model, account info |
| `/memory` | Manage memory files and auto-memory |
| `/init` | Set up project CLAUDE.md |
| `/doctor` | Diagnose installation issues |
| `/stats` | Usage stats and session history |

### File Locations

```
~/.claude/settings.json                # Personal settings (all projects)
.claude/settings.json                  # Project settings (shared via git)
.claude/settings.local.json            # Project settings (local, gitignored)
~/CLAUDE.md                            # Personal memory (all sessions)
CLAUDE.md                              # Project memory
~/.claude/projects/*/memory/MEMORY.md  # Auto-memory
~/.claude/skills/*/SKILL.md            # Personal skills
.claude/skills/*/SKILL.md              # Project skills
```

### Settings Priority

```
Managed (enterprise)  ← can't override
CLI flags             ← session only
.claude/settings.local.json  ← project, local
.claude/settings.json        ← project, shared
~/.claude/settings.json      ← personal
```
