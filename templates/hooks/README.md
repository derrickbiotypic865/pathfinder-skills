# Hook Templates

These are ready-to-use Claude Code hook configurations for the lesson/quirk workflow.

## Available Hooks

### `stop-auto-commit-quirks.json`
**Event:** Stop (fires when Claude Code session ends)

What it does:
1. Runs `generate-quirks.py` to extract quirks from lesson QUIRK markers
2. Stages any changed quirk/lesson files
3. If changes exist, commits and pushes to git
4. If no changes, exits silently

### `post-tool-regenerate-quirks.json`
**Event:** PostToolUse (fires after Write or Edit)

What it does:
1. Checks if the written/edited file is a lesson (path contains `/lessons/` and ends with `.md`)
2. If yes, runs `generate-quirks.py` to regenerate quirk tag files immediately
3. If not a lesson file, does nothing

## Setup

1. Open your `~/.claude/settings.json`
2. Copy the hook entries from the template JSON files into your `hooks` section
3. Update `/path/to/your/training-repo` to your actual repo path
4. Verify with `/hooks` in Claude Code

## How They Work Together

```
You debug something → create a lesson → QUIRK markers extracted
  → PostToolUse hook regenerates quirk files immediately
  → Session ends → Stop hook commits and pushes to git
```

The PostToolUse hook gives you instant feedback (quirks regenerate as you write).
The Stop hook handles the git commit/push so you don't have to.
