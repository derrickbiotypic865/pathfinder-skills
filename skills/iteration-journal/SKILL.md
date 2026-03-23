---
name: iteration-journal
description: A structured reflection skill that captures what you built, what broke, what you learned, and what you'll try next. Run at the end of a coding session or week to track growth over time.
---

# Iteration Journal

## Overview

A structured reflection skill that captures what you built, what broke, what you learned, and what you'll try next. Run at the end of a coding session or week to track your growth as a builder over time.

**Keywords**: reflection, journal, learning, growth, confidence, session review, weekly summary, retrospective

## Trigger Phrases

- "journal"
- "reflect"
- "what did I learn today"
- "end of session"
- "weekly summary"
- "look back"

## Behavior

When the user triggers a reflection (via "journal", "reflect", "what did I learn today", or "end of session"), prompt them through a quick structured journal entry. The tone should be thoughtful, reflective, and celebratory of growth. Open with something like: "Let's capture what you learned before it fades."

### Journal Entry Format

Collect the following fields for each entry:

1. **Date** — today's date, filled in automatically
2. **What I built / worked on** — a brief description of the session's focus
3. **What worked** — things that went well or clicked
4. **What broke or surprised me** — unexpected failures, bugs, or surprises
5. **What I learned** — the single key insight from the session
6. **My hypothesis for next time** — what the user plans to try or change next
7. **Confidence level (1-5)** — how comfortable the user feels with the topic (1 = lost, 5 = solid)

Walk through each field conversationally rather than dumping the whole template at once. If the user gives short answers, that is fine — brevity is welcome.

### Quirk Extraction

After collecting "What broke or surprised me", extract technical quirks and add structured HTML comment markers to the lesson file. For EACH technical failure, bug, or gotcha discussed, add a marker block:

```html
<!-- QUIRK: Short descriptive title -->
<!-- WHEN: Situation where this applies -->
<!-- WRONG: Code or approach that fails -->
<!-- RIGHT: Code or approach that works -->
<!-- WHY: One-sentence root cause -->
<!-- TAGS: comma-separated technology tags -->
```

**Rules for quirk markers:**
- Only extract TECHNICAL patterns (API quirks, code gotchas, platform constraints)
- Do NOT create quirks for impact estimates, confidence levels, hypotheses, or reflections
- Place markers immediately AFTER the relevant section in the lesson
- Tags should describe the technology (e.g., google-apps-script, python, openshift, rust)
- Create new tags if the technology doesn't fit existing ones
- Each marker should be self-contained — someone reading ONLY the marker should understand the pattern

**After saving the lesson file**, the Claude Code PostToolUse hook will automatically run `generate-quirks.py` to regenerate the quirk files from all markers.

### Saving Entries

Save the completed journal entry (with quirk markers embedded) to your lessons directory using a descriptive filename like `topic-name.md`. The file persists across sessions and feeds into the quirks extraction system.

### Weekly Summary

When the user says "weekly summary", aggregate all journal entries from the past seven days and surface patterns:

- Topics the user spent the most time on
- Confidence trend per topic (e.g., "You've been working with APIs a lot — your confidence went from 2 to 4 this week")
- Recurring struggles or breakthroughs
- A short encouraging note on visible progress

### Growth Visualization

Track confidence levels over time and organize entries by topic. When asked, show:

- Confidence trajectory for a given topic across sessions
- Topics mastered (consistently rated 4-5)
- Topics still developing (rated 1-3 or fluctuating)
- Total number of sessions logged

### Look Back

When the user says "look back" or asks something like "show me what I was working on a month ago", retrieve entries from the requested time period and present a summary. Highlight growth by comparing past confidence levels and hypotheses against current state. This demonstrates how far the user has come.

## Example Interaction

**User:** "reflect"

**Assistant:** "Let's capture what you learned before it fades. What did you build or work on today?"

**User:** "I set up a REST API with authentication middleware."

**Assistant:** "Nice. What worked well?"

**User:** "Token validation clicked once I understood the middleware chain."

**Assistant:** "Good insight. What broke or surprised you?"

**User:** "CORS errors — took me an hour to figure out it was a missing header."

**Assistant:** "Classic. What's the key thing you learned from today?"

**User:** "Middleware order matters more than I expected."

**Assistant:** "Solid takeaway. What's your hypothesis for next time?"

**User:** "I'll set up CORS first before writing any route logic."

**Assistant:** "Smart. Last one — confidence level on APIs and middleware, 1 to 5?"

**User:** "3"

**Assistant:** "Logged. Let me extract the technical quirk from that CORS issue..."

*Claude adds to the lesson file:*
```
<!-- QUIRK: CORS errors from missing header -->
<!-- WHEN: Setting up Express middleware for a REST API -->
<!-- WRONG: Writing route handlers before configuring CORS — requests fail silently -->
<!-- RIGHT: Set up CORS middleware first: `app.use(cors())` before any route definitions -->
<!-- WHY: Middleware order matters — CORS headers must be set before the request reaches route handlers -->
<!-- TAGS: node, express, rest-api -->
```

**Assistant:** "Quirk captured. You're building real intuition here — three sessions ago you rated this a 1. That's real progress."

## Tone Guidelines

- Thoughtful and reflective — treat each session as meaningful, no matter how small
- Celebrate growth and progress without being over-the-top or performative
- Patient and encouraging — if the user struggles to articulate what they learned, help them find it
- Never judgmental about mistakes or low confidence ratings — frame struggles as part of the process
- Warm but concise — keep prompts short so the reflection feels lightweight, not like homework
