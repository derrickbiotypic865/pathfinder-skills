# Tech Translator

A Claude Code skill that translates technical concepts, commands, errors, and code into plain, friendly language for non-technical users.

Perfect for onboarding teammates who are new to development tools, helping non-engineers use Claude Code, or making any technical workflow more approachable.

## Features

| Feature | Description |
|:--------|:------------|
| **One-liner analogies** | Every command and concept gets a real-world comparison |
| **Step-by-step breakdowns** | Multi-part commands are explained piece by piece |
| **Safety labels** | `[SAFE]` / `[REVERSIBLE]` / `[CAUTION]` on every action |
| **Difficulty ratings** | `[Beginner]` / `[Intermediate]` / `[Advanced]` tags |
| **Code comments** | All generated code includes plain-English comments |
| **Implementation walkthroughs** | Full setup instructions with exact clicks and menu paths |
| **Personal glossary** | Tracks terms you've learned and adapts over time |
| **Progress tracking** | Reduces explanation depth as you master topics |
| **"Why did you do that?"** | Explains reasoning behind any action |
| **"Show me a simpler version"** | Rewrites code/commands for maximum clarity |
| **"Quiz me"** | Tests your knowledge with friendly multiple-choice questions |
| **"Explain like I'm 5"** | Zero-jargon mode using only everyday analogies |
| **Platform-aware** | Adapts instructions to Windows, Mac, or Linux |
| **Cheat sheet generator** | One-page reference of everything covered |
| **"What should I try next?"** | Suggests follow-up learning after each task |

## Installation

### Option 1: Install as a Plugin (recommended)

```bash
claude /plugin install tech-translator
```

### Option 2: Manual Install (personal, all projects)

```bash
mkdir -p ~/.claude/skills/tech-translator
cp skills/tech-translator/SKILL.md ~/.claude/skills/tech-translator/SKILL.md
```

### Option 3: Project-level (shared with team via git)

```bash
mkdir -p .claude/skills/tech-translator
cp skills/tech-translator/SKILL.md .claude/skills/tech-translator/SKILL.md
git add .claude/skills/tech-translator/
git commit -m "Add tech-translator skill"
```

## Usage

### Startup

On first use, Tech Translator asks you to pick a mode:

- **Always-on** — every response includes explanations automatically
- **On-demand** — explanations only when you ask
- **Off** — no translations

Your choice persists across sessions.

### Trigger Phrases (on-demand mode)

| Say this | To get |
|:---------|:-------|
| "explain that" / "what does that mean" | Explanation of the last thing that happened |
| "teach me about [topic]" | Full beginner-friendly lesson on any topic |
| "why did you do that?" | Reasoning behind Claude's last action |
| "show me a simpler version" | Simplified rewrite of code or commands |
| "quiz me" | 3-5 multiple choice questions on what you've learned |
| "explain like I'm 5" / "ELI5" | Ultra-simple explanation with zero jargon |
| "cheat sheet" | One-page reference of everything covered |
| "what should I try next?" | Suggested next steps for learning |

### Change Settings Mid-Session

```
set translator to always-on
set translator to on-demand
set translator to off
```

### Invoke Directly

```
/tech-translator
```

## Example Output

Running `grep -r "error" ./logs/`:

> *(This is like using Ctrl+F to search every file in the "logs" folder for the word "error")*
> `[Beginner]` `[SAFE — this only reads files, nothing is changed]`
>
> **Breaking it down:**
> - `grep` — a search tool that looks through text inside files
> - `-r` — "recursive" means it checks every file inside every subfolder too
> - `"error"` — the word we're searching for
> - `./logs/` — the folder to search in (the dot means "starting from where we are right now")
>
> **Want to keep going?** You could:
> - Try changing "error" to another word to search for something different
> - Ask me "teach me about regular expressions" to learn advanced search patterns

## Contributing

PRs welcome! If you have ideas for better analogies, additional trigger phrases, or new learning features, open an issue or submit a PR.

## License

MIT
