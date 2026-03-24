# Permissions — Hands-On Exercises

> New to technical terms? See the [Plain-English Glossary](../glossary.md) for jargon-free definitions.

Control what Claude can and can't do. These exercises walk you through setting up permissions so Claude works the way you want — helpful enough to get things done, restricted enough to stay safe.

**Key concept:** Rules are evaluated in order: **deny > ask > allow**. A deny rule always wins.

---

## Exercise 1: View Current Permissions

**What you'll learn:** How to see what Claude is allowed to do right now.

1. Type `/permissions`
2. A list shows all current permission rules and which settings file they came from
3. Browse the three sections: **Allow**, **Ask**, **Deny**
4. Notice which tools are pre-allowed (things you clicked "Yes, don't ask again" for)

**What to expect:** You'll see rules like `Bash(git *)`, `Read(...)`, etc. Each shows its source file.

**Pro tip:** Rules you approve during a session go into `.claude/settings.local.json`. Edit that file directly to clean up accumulated rules.

---

## Exercise 2: Permission Modes

**What you'll learn:** How to switch between different permission strictness levels.

1. Type `/permissions` and look for the mode selector
2. Try **Plan mode**: `/config` > set permission mode to `plan`
   - Ask Claude to edit a file — it will explain what it WOULD do but can't
   - This is great for understanding changes before committing to them
3. Switch to **acceptEdits**: Claude auto-approves file changes but still asks about bash commands
4. Switch back to **default**: Claude asks before most actions

**Modes reference:**

| Mode | File edits | Bash commands | Best for |
|:-----|:-----------|:-------------|:---------|
| `default` | Ask | Ask | Normal use |
| `acceptEdits` | Auto-approve | Ask | Trusted file editing |
| `plan` | Blocked | Blocked | Read-only analysis |
| `dontAsk` | Only if pre-allowed | Only if pre-allowed | Strict lockdown |

**Pro tip:** Start with `default`. Move to `acceptEdits` once you trust Claude with your codebase. Use `plan` when you want Claude to analyze without touching anything.

---

## Exercise 3: Allow Rules for Bash Commands

**What you'll learn:** How to pre-approve specific bash commands so Claude doesn't ask every time.

1. Open your settings: `~/.claude/settings.json` (personal) or `.claude/settings.local.json` (project)
2. Add allow rules:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git *)",
      "Bash(python *)",
      "Bash(ls *)",
      "Bash(cat *)"
    ]
  }
}
```

3. Restart Claude or start a new session
4. Ask Claude to run `npm run build` — it runs without asking
5. Ask Claude to run `rm -rf /` — it still asks (not in your allow list)

**What to expect:** Allowed commands run silently. Everything else still prompts.

**Pro tip:** `Bash(npm *)` allows `npm run build`, `npm install`, `npm test`, etc. The space before `*` matters — `Bash(npm *)` won't match `npmrc`.

---

## Exercise 4: Deny Rules (Block Dangerous Commands)

**What you'll learn:** How to prevent Claude from running specific commands, even if you accidentally approve them.

1. Add deny rules to your settings:

```json
{
  "permissions": {
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Bash(git reset --hard *)",
      "Bash(drop table *)",
      "Bash(shutdown *)"
    ],
    "allow": [
      "Bash(git *)"
    ]
  }
}
```

2. Ask Claude to force-push — it will be blocked even though `git *` is allowed
3. The deny rule takes priority over the allow rule

**What to expect:** Claude won't be able to run denied commands. You'll see a message that the tool is denied.

**Pro tip:** Deny rules are your safety net. They override everything — even if you click "allow" by accident, deny rules still block.

---

## Exercise 5: File Path Permissions

**What you'll learn:** How to control which files Claude can read or edit.

**Allow editing only in src/:**
```json
{
  "permissions": {
    "allow": [
      "Edit(/src/**)"
    ],
    "deny": [
      "Edit(.env)",
      "Edit(/**/.env)",
      "Read(.env)"
    ]
  }
}
```

**Path pattern reference:**

| Pattern | Matches |
|:--------|:--------|
| `/src/**` | Everything in project's src/ directory (recursive) |
| `*.env` | Any .env file in current directory |
| `/**/.env` | Any .env file anywhere in the project |
| `~/.ssh/**` | Your SSH directory |
| `//tmp/*` | Absolute path /tmp/ (note the double slash) |

**Pro tip:** `*` matches files in one directory. `**` matches recursively. Use `**` for "everything inside this folder and subfolders."

---

## Exercise 6: Web and MCP Permissions

**What you'll learn:** How to control external access — web fetching and MCP tools.

**Allow specific domains:**
```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)",
      "WebFetch(domain:docs.python.org)",
      "mcp__filesystem",
      "mcp__database__read_query"
    ],
    "deny": [
      "WebFetch(domain:evil-site.com)",
      "mcp__database__drop_table"
    ]
  }
}
```

**MCP permission patterns:**

| Pattern | Matches |
|:--------|:--------|
| `mcp__server-name` | All tools from that server |
| `mcp__server-name__*` | Same — all tools (wildcard) |
| `mcp__server-name__tool-name` | One specific tool |

**Pro tip:** Be specific with MCP permissions. Allow read operations, deny destructive ones. `mcp__database__read_query` is safer than `mcp__database`.

---

## Exercise 7: Settings File Priority

**What you'll learn:** How different settings files interact and which wins.

**Priority (highest to lowest):**

1. **Managed settings** (enterprise admin) — can't be overridden
2. **CLI flags** — `--allowedTools`, `--disallowedTools`
3. **`.claude/settings.local.json`** — project, local only (gitignored)
4. **`.claude/settings.json`** — project, shared (committed to git)
5. **`~/.claude/settings.json`** — personal, all projects

**Try this:**
1. Add `Bash(echo *)` to your personal settings (`~/.claude/settings.json`) under allow
2. Add `Bash(echo *)` to your project settings (`.claude/settings.json`) under deny
3. Ask Claude to run `echo hello` — it will be denied (project deny beats personal allow)

**Pro tip:** Put your personal preferences in `~/.claude/settings.json`. Put project-specific rules in `.claude/settings.json` and commit it — your whole team gets the same permissions.

---

## Quick Reference

### Rule Syntax

```
Bash(command *)       — bash commands with wildcard
Read(/path/**)        — file read rules (gitignore patterns)
Edit(/path/**)        — file edit rules
WebFetch(domain:x)    — web fetch by domain
mcp__server__tool     — MCP tool rules
Agent(AgentName)      — subagent rules
```

### Precedence

```
deny  →  blocks the action, no matter what
ask   →  prompts every time
allow →  runs without asking
```

### Settings Files

| File | Scope | Shared? |
|:-----|:------|:--------|
| `~/.claude/settings.json` | All projects | Personal |
| `.claude/settings.json` | This project | Team (git) |
| `.claude/settings.local.json` | This project | Personal (gitignored) |
