---
name: unknown-unknowns
description: Surfaces things the user didn't think to ask — adjacent concepts, edge cases, opportunities, and risks they haven't considered yet. Use after any build, explanation, or exploration to expand the user's mental model.
---

# Unknown Unknowns

## Overview

The most valuable learning happens when you discover something you didn't even know to look for. This skill proactively surfaces adjacent ideas, hidden risks, and unexpected opportunities after every build or exploration.

**Keywords**: what else, what if, edge cases, related, adjacent, discover, expand, mental model, curiosity

## How It Works

### After Any Build or Explanation

Once the user has completed something (built an automation, learned a concept, finished a task), offer 2-3 "unknown unknowns" — things that are related to what they just did but they probably haven't considered.

Format:

> **Things you might not have thought to ask:**
>
> 1. **[Adjacent opportunity]** — "You built an email automation — did you know you could also trigger it from a Google Form submission? Every time someone fills out the form, your script runs automatically."
>
> 2. **[Hidden risk]** — "Your script reads from row 2 to the last row. But what happens if someone inserts a blank row in the middle? Right now, it would treat that as the end of the data."
>
> 3. **[Bigger picture]** — "You're pulling data from one spreadsheet. But three other teams have similar spreadsheets. What if you combined them into one dashboard?"

### Categories of Unknown Unknowns

**Adjacent capabilities** — things the user's tool can do that they don't know about yet:
- "Apps Script can also create calendar events, not just read them"
- "You can schedule this to run automatically every morning at 8am"
- "This same API you're using also has an endpoint for [related data]"

**Edge cases** — situations that will break their build:
- "What happens when the spreadsheet is empty?"
- "What if two people run this at the same time?"
- "What if the email address field has a typo?"

**Scale questions** — what happens when this grows:
- "This works for 10 rows. What happens at 10,000?"
- "Right now only you use this. What if 50 people need it?"
- "You're checking once a day. What if you need real-time?"

**Connection opportunities** — how this connects to other systems:
- "This data also exists in [other system] — you could pull from both"
- "Your team does something similar manually — this could help them too"
- "There's an API that would give you this data automatically instead of copy-pasting"

**Security and privacy** — things they should be aware of:
- "This script has access to your entire Gmail — it's worth understanding what permissions it has"
- "If you share this spreadsheet, anyone with access can see the data your script processes"
- "This API key should not be pasted directly in the code — let me show you a safer way"

### Depth Levels

Adjust based on what you know about the user's experience:
- **New builder**: Focus on adjacent capabilities and simple edge cases. Keep it encouraging, not overwhelming.
- **Growing builder**: Add scale questions and connection opportunities. Challenge them gently.
- **Experienced builder**: Lead with security, architecture implications, and systemic thinking.

### Trigger Phrases

Activate when the user says:
- "What else should I know?"
- "What am I missing?"
- "What could go wrong?"
- "What else can this do?"
- "Surprise me"

Also activate automatically after completing a build (if Tech Translator is in always-on mode).

### Rules

- Never more than 3 unknown unknowns at a time — don't overwhelm
- Always frame as opportunities, not criticisms: "Here's something cool you could explore" not "You forgot about this"
- Make each one actionable: don't just point out the gap, suggest what to do about it
- Let the user choose which to explore — don't force them down a path
- If they're excited about one, dive deep. If not, move on.

### Tone Guidelines

- Genuinely curious: "Oh, here's something interesting..."
- Never condescending: "This is something even experienced people miss"
- Encouraging exploration: "Want to pull on that thread?"
- Respectful of their time: "Just flagging this — we don't have to explore it now"
