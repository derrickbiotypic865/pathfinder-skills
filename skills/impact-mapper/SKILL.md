---
name: impact-mapper
description: Quantifies the impact of what the user built — time saved, errors reduced, people helped, ROI. Use before a build to estimate value, or after to measure actual results. Generates impact reports for leadership.
---

# Impact Mapper

## Overview

"I built a cool thing" doesn't move organizations. "I saved the team 12 hours a week and eliminated manual errors in our reporting pipeline" does. This skill helps users measure, articulate, and present the impact of what they build.

**Keywords**: impact, ROI, time saved, measure, value, metrics, business case, justify, leadership, outcomes

## How It Works

### Before a Build — Estimate Impact

When someone is about to build something, help them estimate the value FIRST.

Ask these questions:
1. **"How long does this take manually?"** Get a specific number. "About 20 minutes each time."
2. **"How often do you do it?"** Daily? Weekly? Monthly? "Every Monday and Thursday."
3. **"How many people are involved?"** Just you? A team of 5? "Three of us rotate."
4. **"What goes wrong when it's done manually?"** Wrong numbers, missed deadlines, duplicated work. "Sometimes we miss rows and the report is wrong."
5. **"What happens when it goes wrong?"** Rework, embarrassment, downstream impact. "We have to resend the report and people lose trust in the data."

Then calculate:
```
## Estimated Impact: [Name]

**Time per occurrence**: 20 minutes
**Frequency**: 2x per week
**People involved**: 3
**Current time cost**: 20 min x 2/week x 3 people = 2 hours/week

**Annual time cost**: 2 hours x 52 weeks = 104 hours/year
**Error rate**: ~1 in 10 reports has mistakes
**Rework time per error**: 30 minutes
**Annual rework**: 5.2 x 30 min = 2.6 hours/year

**Total annual cost**: ~107 hours/year of human time

**After automation**:
- Time per occurrence: ~30 seconds (just review the output)
- Error rate: near zero (no manual copying)
- Estimated savings: ~100 hours/year
```

### After a Build — Measure Actual Impact

Once the automation has been running, revisit the estimates:

```
## Actual Impact: [Name]
**Measurement period**: [2 weeks / 1 month / etc.]

| Metric | Estimated | Actual | Notes |
|:-------|:----------|:-------|:------|
| Time per run | 30 seconds | 45 seconds | Need to review output |
| Runs per week | 2 | 2 | As expected |
| Errors | 0 | 0 | No manual errors since launch |
| Time saved/week | 1.9 hours | 1.8 hours | Close to estimate |
| User satisfaction | High | High | Team loves it |

**Annualized savings**: ~94 hours/year
**Hypothesis confirmed**: Yes — automation saves meaningful time and eliminates errors
```

### Impact Categories

Help users think beyond just "time saved":

**Efficiency** — time and effort
- Hours saved per week/month/year
- Steps eliminated from a process
- Manual handoffs removed

**Quality** — accuracy and consistency
- Error rate before vs. after
- Rework eliminated
- Consistency of output

**Speed** — how fast things happen
- Turnaround time before vs. after
- How quickly people get what they need
- Response time improvements

**Scale** — what's now possible
- Can now handle 10x the volume
- Can now serve more teams/regions
- Removed a bottleneck that limited growth

**People** — human impact
- Freed people to do higher-value work
- Reduced frustration and tedium
- Enabled people who aren't technical to self-serve

**Risk** — what could have gone wrong
- Compliance or audit risk reduced
- Single point of failure removed
- Data accuracy improved

### Impact Report Generator

When the user says "generate impact report" or "help me show the ROI", create:

```
## Impact Report: [Name]
**Built by**: [name/team]
**Date launched**: [date]
**Measurement period**: [X weeks/months]

### Executive Summary
[2-3 sentences: what was built, what it does, and the headline impact number]

### The Problem
[What was happening before, in business terms]

### The Solution
[What was built, in plain English — no code, no jargon]

### Measured Impact
[Table of metrics: before, after, improvement]

### Qualitative Feedback
[Quotes or observations from people who use it]

### What's Next
[How this could be expanded, what adjacent opportunities exist]

### Replicability
[Could other teams use this? What would they need?]
```

## Trigger Phrases

- "What's the impact?"
- "How much time does this save?"
- "Help me measure this"
- "Generate impact report"
- "What's the ROI?"
- "Help me justify this"
- "Show the value"

## Rules

- Always use concrete numbers — avoid vague claims like "saves a lot of time"
- Help the user gather real data, not just estimates
- Frame impact in terms leadership cares about: time, money, risk, scale
- Be honest — if the impact is small, say so and help them find higher-impact opportunities
- Include qualitative impact too — "the team loves it" matters

## Tone Guidelines

- Business-minded but accessible
- Confident with data, humble about estimates: "This is our best estimate — we'll refine it with real data"
- Impact-focused: "Here's why this matters"
- Encouraging: "Even a small automation that saves 30 minutes a week adds up to 26 hours a year"
