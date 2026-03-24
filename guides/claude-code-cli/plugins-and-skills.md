# Plugins & Skills — Hands-On Exercises

Extend Claude Code with community plugins and custom skills. Plugins are packaged extensions from marketplaces. Skills are .md files that teach Claude new behaviors.

---

## Exercise 1: Install a Plugin

**What you'll learn:** How to add new capabilities from a GitHub repo.

1. In a Claude session, type:
```
/plugin install ChewbaccaRoars/pathfinder-skills
```
2. Claude downloads and installs the plugin
3. Type `/skills` to see the new skills available
4. Try one: `/pathfinder`

**What to expect:** 19 new skills appear including `/learn`, `/build`, `/reflect`, `/share`, and domain-specific skills like `/apps-script-builder` and `/courage-mode`.

**Pro tip:** Plugins from GitHub repos install all skills, hooks, and configurations in one command.

---

## Exercise 2: Browse and Manage Plugins

**What you'll learn:** How to find, list, and remove plugins.

```
/plugin list                  — see installed plugins
/plugin remove <name>         — uninstall a plugin
/plugin marketplace add <owner/repo>  — add a marketplace source
```

**Try it:**
1. Type `/plugin list` — see what's installed
2. Type `/plugin` — browse the interactive plugin manager
3. If you want to explore more plugins, check [github.com/topics/claude-skills](https://github.com/topics/claude-skills)

**Pro tip:** Use `/reload-plugins` after modifying a plugin's files to apply changes without restarting.

---

## Exercise 3: Create Your First Skill

**What you'll learn:** How to create a custom slash command.

1. Create the skill directory:
```bash
mkdir -p ~/.claude/skills/my-reviewer
```

2. Create the SKILL.md file:
```bash
cat > ~/.claude/skills/my-reviewer/SKILL.md << 'EOF'
---
name: my-reviewer
description: Reviews code for common issues. Use when asked to review code or check for problems.
---

When reviewing code, check for:

1. **Security**: SQL injection, XSS, hardcoded secrets, unsafe input handling
2. **Error handling**: Missing try/catch, unhandled promises, silent failures
3. **Performance**: N+1 queries, unnecessary loops, missing pagination
4. **Readability**: Unclear variable names, missing comments on complex logic, deep nesting

For each issue found, explain:
- What the problem is (in plain English)
- Where it is (file and line)
- How to fix it (with a code example)
- Why it matters

End with a summary: "Found X issues: Y critical, Z warnings."
EOF
```

3. Start a new Claude session
4. Type `/my-reviewer` — your skill is live
5. Or type `/skills` — it appears in the list

**What to expect:** Your custom command works just like a built-in one. Claude follows your instructions whenever the skill is invoked.

**Pro tip:** Personal skills (`~/.claude/skills/`) work in ALL your projects. Project skills (`.claude/skills/`) only work in that project.

---

## Exercise 4: Skill Frontmatter Options

**What you'll learn:** How to control when and how a skill is invoked.

```yaml
---
name: my-skill
description: What it does and when Claude should use it
disable-model-invocation: true    # Only YOU can invoke it (not Claude)
user-invocable: false              # Only CLAUDE can invoke it (hidden from / menu)
context: fork                      # Run in an isolated subagent
agent: Explore                     # Which agent type to use in fork mode
allowed-tools: Read, Grep, Glob   # Restrict available tools
model: sonnet                      # Override model for this skill
effort: high                       # Override effort level
---

Your instructions here...
```

**Key options explained:**

| Option | What it does | When to use |
|:-------|:-------------|:------------|
| `disable-model-invocation: true` | Only you can trigger it with `/name` | Commands with side effects: deploy, send email, delete |
| `user-invocable: false` | Hidden from the `/` menu — Claude uses it when relevant | Background knowledge: style guides, conventions |
| `context: fork` | Runs in an isolated subagent | Long research tasks, things that shouldn't pollute your conversation |
| `allowed-tools` | Limits what Claude can do when the skill is active | Read-only analysis, safe browsing |

**Try it:** Create a skill with `disable-model-invocation: true` and verify Claude can't auto-trigger it — you have to type `/name` explicitly.

---

## Exercise 5: Skills with Arguments

**What you'll learn:** How to pass arguments to skills.

```yaml
---
name: explain-file
description: Explain a file in plain English
---

Read the file at $ARGUMENTS and explain what it does in plain English.
Include:
1. What the file's purpose is
2. How it connects to other parts of the project
3. Key functions or classes and what they do
```

**Usage:**
```
/explain-file src/auth/login.ts
```

`$ARGUMENTS` gets replaced with whatever you type after the command.

**For multiple arguments:**
```yaml
---
name: compare-files
description: Compare two files
---

Compare $ARGUMENTS[0] and $ARGUMENTS[1].
Show the key differences and which approach is better.
```

**Usage:**
```
/compare-files src/old-auth.ts src/new-auth.ts
```

**Pro tip:** `$0` is shorthand for `$ARGUMENTS[0]`, `$1` for `$ARGUMENTS[1]`.

---

## Exercise 6: Skills with Supporting Files

**What you'll learn:** How to bundle templates, examples, and scripts with a skill.

```
my-skill/
├── SKILL.md              # Main instructions (required)
├── template.md           # Template for Claude to fill in
├── examples/
│   └── sample-output.md  # Example of expected output
└── scripts/
    └── validate.sh       # Script Claude can execute
```

Reference supporting files from SKILL.md:

```markdown
---
name: generate-report
description: Generate a formatted report
---

Generate a report following the template in [template.md](template.md).
See [examples/sample-output.md](examples/sample-output.md) for the expected format.
After generating, run [scripts/validate.sh](scripts/validate.sh) to verify.
```

**Pro tip:** Keep SKILL.md under 500 lines. Move detailed reference material to separate files — they only load when Claude needs them.

---

## Exercise 7: Skill Locations

**What you'll learn:** Where to put skills for different scopes.

| Location | Path | Who can use it |
|:---------|:-----|:--------------|
| **Personal** | `~/.claude/skills/<name>/SKILL.md` | You, in all projects |
| **Project** | `.claude/skills/<name>/SKILL.md` | Anyone working on this project |
| **Plugin** | Installed via `/plugin install` | Where the plugin is enabled |

**Priority when names conflict:** Enterprise > Personal > Project. Plugin skills use namespaces so they can't conflict.

**Try it:**
1. Create a personal skill in `~/.claude/skills/`
2. Create a project skill with the same name in `.claude/skills/`
3. The personal one wins (higher priority)

---

## Quick Reference

### Plugin Commands

| Command | What it does |
|:--------|:-------------|
| `/plugin install <owner/repo>` | Install from GitHub |
| `/plugin list` | List installed plugins |
| `/plugin remove <name>` | Remove a plugin |
| `/reload-plugins` | Reload without restarting |
| `/skills` | List all available skills |

### SKILL.md Template

```yaml
---
name: my-skill
description: What it does
---

Instructions for Claude go here.
Use $ARGUMENTS for user input.
```

### Skill Locations

```
~/.claude/skills/<name>/SKILL.md     # Personal (all projects)
.claude/skills/<name>/SKILL.md       # Project (this project)
```
