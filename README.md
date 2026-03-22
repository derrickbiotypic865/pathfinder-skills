# AI-Native Builder Skills

A collection of Claude Code skills designed to help non-technical people become builders — creating their own automations, apps, and agents.

> *"We are not caretakers of the past. We are obsessive learners, compulsive experimenters, and builders of what's next."*

Built for people who believe the AI-native future will be shaped not only by developers, but by business people who learn to build. These skills take someone from "I've never opened a terminal" to "I just built an agent that reimagined our workflow."

## The Skills (13)

### The On-Ramp
| Skill | What it does |
|:------|:-------------|
| **[tech-translator](skills/tech-translator/)** | Translates commands, errors, and code into plain, friendly language. Safety labels, difficulty ratings, quizzes, ELI5 mode, adaptive learning. The foundation skill. |
| **[courage-mode](skills/courage-mode/)** | For when you're stuck or afraid to try. Breaks scary tasks into tiny safe steps. Celebrates attempts, not just successes. |

### The Learning Loop
| Skill | What it does |
|:------|:-------------|
| **[hypothesis-lab](skills/hypothesis-lab/)** | Structures every project as an experiment — hypothesis, test, evidence, iterate. Because we begin with hypotheses, not certainties. |
| **[build-first-break-later](skills/build-first-break-later/)** | Gets a rough v1 working in minutes, then iterates. Anti-perfectionism by design. The first version is supposed to be ugly. |
| **[unknown-unknowns](skills/unknown-unknowns/)** | Surfaces things you didn't think to ask — adjacent opportunities, hidden risks, bigger picture connections. Expands your mental model. |
| **[iteration-journal](skills/iteration-journal/)** | Structured reflection: what you built, what broke, what you learned. Tracks growth over time. Weekly summaries and look-back features. |

### The Builder Tools
| Skill | What it does |
|:------|:-------------|
| **[workflow-detective](skills/workflow-detective/)** | Investigates your daily work to find the highest-value thing to automate. Scores opportunities by effort vs. impact. |
| **[apps-script-builder](skills/apps-script-builder/)** | Dedicated Google Apps Script assistant. Every service, trigger, and deployment pattern — with full setup walkthroughs for non-technical users. |
| **[api-explorer](skills/api-explorer/)** | Demystifies APIs. From "what is an API?" to making your first call to connecting work systems. Patient tour guide energy. |
| **[agent-architect](skills/agent-architect/)** | Guides you from simple automations to building your own agents. Six levels, each with a concrete project. |

### The Multipliers
| Skill | What it does |
|:------|:-------------|
| **[show-your-work](skills/show-your-work/)** | Generates shareable artifacts — impact summaries, how-to guides, before/after comparisons, presentation outlines. Turns builds into organizational knowledge. |
| **[teach-back](skills/teach-back/)** | Helps you teach what you built to others. Workshop plans, teaching guides, train-the-trainer kits. Knowledge grows when shared. |
| **[impact-mapper](skills/impact-mapper/)** | Quantifies what you built — time saved, errors reduced, ROI. Generates impact reports for leadership. "I saved the team 12 hours/week" beats "I built a cool thing." |

## The Journey

```
 courage-mode          "I'm scared to start"
      |
 tech-translator       "What does that mean?"
      |
 workflow-detective     "What should I build?"
      |
 hypothesis-lab         "What do I think will happen?"
      |
 build-first-break-later "Let's just build it"
      |
 unknown-unknowns       "What am I not seeing?"
      |
 iteration-journal      "What did I learn?"
      |
 apps-script-builder    "Let me build something real"
 api-explorer           "Let me connect systems"
      |
 agent-architect        "Let me build something smart"
      |
 show-your-work         "Let me share what I built"
 impact-mapper          "Let me prove the value"
      |
 teach-back             "Let me help others build too"
```

## Installation

### Option 1: Install all skills as a Plugin (recommended)

```bash
/plugin install ChewbaccaRoars/tech-translator
```

### Option 2: Install individual skills manually

```bash
# Replace <skill-name> with any skill from the list above
mkdir -p ~/.claude/skills/<skill-name>
cp skills/<skill-name>/SKILL.md ~/.claude/skills/<skill-name>/SKILL.md
```

### Option 3: Project-level (shared with your team via git)

```bash
# Copy all skills into your project
cp -r skills/ .claude/skills/
git add .claude/skills/
git commit -m "Add AI-native builder skills"
```

## Quick Start

1. Install the plugin (see above)
2. Start a new Claude Code session
3. Tech Translator will ask if you want it always-on, on-demand, or off
4. Say "what should I build?" to start with Workflow Detective
5. Say "let's build it" to jump into Build First, Break Later
6. Say "what did I learn?" at the end to reflect with Iteration Journal

## Trigger Phrases (all skills)

| Say this | Skill that activates |
|:---------|:---------------------|
| "explain that" / "what does that mean" | tech-translator |
| "I'm stuck" / "I'm scared" / "this is too hard" | courage-mode |
| "I have an idea" / "I want to build something" | hypothesis-lab |
| "let's just build it" / "start building" | build-first-break-later |
| "what am I missing?" / "what else?" | unknown-unknowns |
| "what should I build?" / "workflow audit" | workflow-detective |
| "build an apps script" / "automate my spreadsheet" | apps-script-builder |
| "what is an API?" / "connect to an API" | api-explorer |
| "build an agent" / "level up" | agent-architect |
| "help me share this" / "show my work" | show-your-work |
| "help me teach this" / "create a workshop" | teach-back |
| "what's the impact?" / "show the ROI" | impact-mapper |
| "journal" / "what did I learn today?" | iteration-journal |
| "quiz me" / "cheat sheet" / "ELI5" | tech-translator |

## Values

These skills are built on a set of beliefs:

- **Learning is not optional.** It's how we grow, adapt, and improve.
- **We learn by doing.** Not by reading. Not by watching. By building.
- **We begin with hypotheses, not certainties.** We test what we believe. We let evidence sharpen our thinking.
- **We respect the unknown.** The best discoveries come from questions we didn't know to ask.
- **We are teachers.** Knowledge grows when it's shared. People grow when they're believed in.
- **We seek transformative outcomes.** We're not here to preserve the status quo. We're here to create meaningful change.

## Contributing

PRs welcome! Whether it's better analogies, new skills, additional trigger phrases, or improvements to existing ones — open an issue or submit a PR.

## License

MIT
