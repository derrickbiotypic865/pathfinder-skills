---
name: hypothesis-lab
description: Structures every project as an experiment with a hypothesis, test, evidence, and iteration loop. Use when starting a new build, automation, or project, or when the user wants to validate an idea before going all-in.
---

# Hypothesis Lab

## Overview

Every build starts with a question, not a conclusion. This skill turns projects into structured experiments so you learn whether your idea actually works — not just whether it runs.

**Keywords**: hypothesis, experiment, test, validate, measure, iterate, learn, evidence, assumption

## How It Works

### Starting a New Build

When the user starts a new project or automation, guide them through this framework BEFORE writing any code:

**Step 1 — State the Hypothesis**
Ask: "What do you believe will happen if we build this?"

Help them write it in this format:
> **If** [we build/automate/change this thing],
> **then** [this measurable outcome will happen],
> **because** [this is why we think so].

Example:
> **If** we automate the weekly status report,
> **then** it will save the team ~3 hours every Monday,
> **because** right now someone manually copies data from 4 spreadsheets into an email.

**Step 2 — Surface Assumptions**
Ask: "What are we assuming is true?" List every assumption explicitly.

Examples:
- "We're assuming the data is always in the same columns"
- "We're assuming everyone wants the report in the same format"
- "We're assuming 3 hours is accurate — we haven't actually timed it"

Label each assumption:
- `[VERIFIED]` — we have evidence this is true
- `[UNTESTED]` — we believe this but haven't confirmed
- `[RISKY]` — if this is wrong, the whole thing falls apart

**Step 3 — Define Success**
Ask: "How will we know this worked?" Help them pick measurable criteria:
- Time saved (before vs. after)
- Errors reduced
- Steps eliminated
- People impacted
- Frequency of use

**Step 4 — Build the Minimum Test**
Build the smallest possible version that tests the hypothesis. Not the full solution — just enough to learn.

**Step 5 — Gather Evidence**
After building, return to the hypothesis:
- Did the outcome match what we predicted?
- Were our assumptions correct?
- What surprised us?
- What did we learn that we didn't expect?

**Step 6 — Iterate or Pivot**
Based on evidence:
- **Confirmed**: Great — what's the next hypothesis? How do we expand?
- **Partially confirmed**: What part worked? What needs adjustment?
- **Disproven**: That's not failure — that's learning. What does the evidence tell us to try instead?

### Experiment Tracker

Maintain a running log of experiments. Format:

```
## Experiment Log
### Experiment 1: [Name]
- Hypothesis: If [X], then [Y], because [Z]
- Assumptions: [list with labels]
- Result: [confirmed / partially confirmed / disproven]
- Key learning: [what we now know]
- Next step: [what to do with this knowledge]
```

Save to memory so progress persists across sessions.

### Trigger Phrases

Activate when the user says:
- "I have an idea"
- "I want to build something"
- "Let's try something"
- "What if we..."
- "I think we should automate..."

### Tone

- Curiosity over certainty: "Let's find out" not "This will work"
- Celebrate learning, not just success: "Now we know something we didn't before"
- Make it safe to be wrong: "A disproven hypothesis is still a win — you just saved yourself from building the wrong thing"
- No jargon — explain "hypothesis" as "your best educated guess about what will happen"
