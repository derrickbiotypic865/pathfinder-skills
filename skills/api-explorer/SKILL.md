---
name: api-explorer
description: Demystifies APIs for non-technical people. Guides users through understanding and making their first API calls — from free public APIs to work APIs. Use when someone encounters an API for the first time or wants to connect systems.
---

# API Explorer

## Overview

A skill that turns the mysterious world of APIs into something approachable and even fun. Think of this as a patient tour guide for anyone who has heard "just use the API" and thought, "the what now?"

Let me show you around — APIs are friendlier than they look.

**Keywords**: API, connect, integration, request, response, JSON, REST, endpoint, webhook, authentication, API key, token, status code, HTTP, GET, POST

## The Core Analogy

Always lead with this when introducing APIs for the first time:

> **An API is like a drive-through window.** You pull up, place an order in a specific format (off the menu, not "surprise me"), and you get back exactly what you asked for. You don't need to know how the kitchen works. You just need to know what's on the menu and how to order.

Build from this analogy throughout. The menu = the API documentation. The order format = the request. The food handed back = the response. The intercom = the endpoint.

## What Is an API?

Explain APIs in layers, starting simple:

**Layer 1 — The one-liner:**
> An API is a way for two programs to talk to each other.

**Layer 2 — The analogy:**
> Imagine you're at a restaurant. You (the app) tell the waiter (the API) what you want. The waiter goes to the kitchen (the server), gets your food (the data), and brings it back to you. You never go into the kitchen yourself.

**Layer 3 — Why they exist:**
> APIs exist because programs need to share information without giving each other full access to everything. Your weather app doesn't contain every weather station's data — it asks a weather API, "What's the forecast for this zip code?" and gets an answer back.

## How APIs Work: Request and Response

Every API interaction has two parts:

### The Request (what you send)
> Think of this as filling out an order form. You need to include:
> - **Where to send it** (the URL/endpoint) — like the address of the drive-through
> - **What you want** (the method) — are you asking for information? Submitting something new?
> - **Your ID** (authentication) — proving you're allowed to order
> - **Any details** (parameters/body) — like saying "large, no pickles"

### The Response (what you get back)
> The API sends back:
> - **A status code** — a quick thumbs-up or thumbs-down (more on this below)
> - **The data** — the actual information you asked for, usually in JSON format
> - **Headers** — extra info, like "you have 98 requests left today"

## JSON: The Language APIs Speak

Explain JSON as:

> **JSON is a way of organizing data that computers can read — like a very structured form.**

Show a simple example:
```json
{
  "name": "Weather Report",
  "city": "Portland",
  "temperature": 62,
  "conditions": "partly cloudy",
  "is_raining": false
}
```

Walk through it:
> - Everything is in curly braces `{}` — think of these as the edges of a form
> - Each line has a **label** (on the left) and a **value** (on the right), separated by a colon
> - Text goes in quotes. Numbers and true/false don't.
> - Lines are separated by commas — just like items in a list

When users see nested JSON, compare it to a form that has sections:
> "It's like a form where one of the fields is another mini-form inside it."

## HTTP Methods: The Four Main Actions

Explain each method with a real-world analogy:

| Method | Analogy | What It Does |
|:-------|:--------|:-------------|
| **GET** | Asking a question | "What's the weather today?" Retrieves information. Nothing changes. |
| **POST** | Submitting a form | "Here's my new account info." Sends new data to be created. |
| **PUT** | Updating your address | "I moved — here's my new address." Replaces existing data with updated data. |
| **DELETE** | Canceling an order | "Never mind, remove that." Deletes something that exists. |

Key reassurance:
> **GET is always safe.** It just looks at things. It's the equivalent of window shopping — you can browse all day without buying anything.

## Status Codes: What the API Is Telling You

Present status codes as the API's facial expressions:

### The Good
| Code | Analogy | Meaning |
|:-----|:--------|:--------|
| **200** | Thumbs up | Everything worked. Here's what you asked for. |
| **201** | "Got it, it's done" | Your new thing was created successfully. |
| **204** | Nod of confirmation | Done. Nothing to send back, but it worked. |

### The "That's on You" Errors
| Code | Analogy | Meaning | How to Fix It |
|:-----|:--------|:--------|:--------------|
| **400** | "I can't read your handwriting" | The request was formatted wrong. | Check your spelling, missing fields, or wrong data types. |
| **401** | "You need to show your ID first" | You're not authenticated. | Add or fix your API key/token. |
| **403** | "You have an ID, but you're not on the list" | You're authenticated but not authorized for this. | Check your permissions or subscription level. |
| **404** | "That page doesn't exist" | The thing you asked for isn't there. | Check the URL — typo? Wrong ID? |
| **429** | "Slow down, you're ordering too fast" | You've hit the rate limit. | Wait a bit and try again. |

### The "That's on Them" Errors
| Code | Analogy | Meaning | How to Fix It |
|:-----|:--------|:--------|:--------------|
| **500** | "Something broke on their end, not yours" | The server had an internal error. | Wait and retry. If it persists, it's their problem to fix. |
| **502** | "The middleman couldn't reach the kitchen" | A gateway/proxy issue. | Usually temporary — try again in a few minutes. |
| **503** | "We're closed for maintenance" | The service is temporarily unavailable. | Wait and retry. Check their status page if they have one. |

## Authentication: Proving You're Allowed

### API Keys
> An API key is like a library card. You sign up, they give you a unique code, and you include it every time you make a request so they know it's you.

Explain where keys typically go:
- In the URL as a parameter: `?api_key=YOUR_KEY`
- In a header: `Authorization: Bearer YOUR_KEY`
- Important: "Treat API keys like passwords. Don't share them, don't put them in public code."

### Tokens (OAuth)
> A token is like a visitor badge at an office. You prove who you are at the front desk (login), they give you a badge (token), and you wear it to access things. The badge expires after a while, and you need to get a new one.

### No Authentication
> Some APIs are completely open — no key needed. Public APIs like joke generators or random facts are often like this. They're great for learning.

## Rate Limits: Why You Can't Ask Infinite Questions

> Rate limits are like a "please take only one" sign at a sample table. The API can only handle so many requests, so they limit how many you can make per minute/hour/day.

Explain what happens when you hit one:
- You'll get a **429 status code**
- The response usually tells you when you can try again
- Fix: slow down, add delays between requests, or upgrade your plan

## Your First API Call — Guided Walkthrough

Walk the user through a real API call step by step. Use a free, no-authentication API.

### Option A — A Random Joke (No signup needed)

> Let's make your first API call right now. We're going to ask the internet to tell us a joke.

**Step 1: The URL**
```
https://official-joke-api.appspot.com/random_joke
```
> This is the "drive-through window" we're pulling up to.

**Step 2: The Method**
> We're using GET — we're just asking a question: "Tell me a joke."

**Step 3: Make the Call**

In a browser:
> Just paste that URL into your browser's address bar and hit Enter. Seriously — that's an API call. Your browser just made a GET request.

In a terminal:
```bash
curl https://official-joke-api.appspot.com/random_joke
```
> `curl` is a tool that makes web requests from the command line. Think of it as a text-only web browser.

**Step 4: Read the Response**
```json
{
  "type": "general",
  "setup": "What do you call a fake noodle?",
  "punchline": "An impasta.",
  "id": 42
}
```
> That's JSON. The API sent back a structured response with a setup, punchline, type, and ID number. You just made your first API call.

### Option B — Weather Data (Free API key required)

> Ready for something more useful? Let's get real weather data. This one needs a free API key — think of it as signing up for a library card.

Walk through:
1. Sign up at a free weather API (like Open-Meteo, which needs no key, or OpenWeatherMap for the key experience)
2. Get the API key
3. Build the request URL with the key
4. Make the call
5. Read the response together

## Building Up: From Free APIs to Work APIs

### Level 1 — Free Public APIs (No auth or free signup)
> These are your training ground. Low stakes, no cost, immediate results.

Examples to try:
- **Jokes**: `official-joke-api.appspot.com` — random jokes, no key needed
- **Facts**: `uselessfacts.jsph.pl` — random facts, no key needed
- **Weather**: `open-meteo.com` — real weather data, no key needed
- **Quotes**: various free quote APIs — inspirational quotes on demand

> Start here. Make a few calls. Get comfortable with the rhythm: URL + method + send = response.

### Level 2 — Google APIs
> Google APIs are powerful but have more setup. Think of it as going from the drive-through to a sit-down restaurant — more steps, but more options.

Cover:
- Getting credentials from Google Cloud Console
- OAuth2 vs API keys (and when to use which)
- Common APIs: Sheets, Calendar, Gmail, Drive
- "The first time is the hardest. Once you've connected one Google API, the next one is much easier."

### Level 3 — Work APIs
> These are the APIs your company uses. Same concepts, just with workplace authentication.

Cover the common ones:
- **ServiceNow**: "Like submitting a help desk ticket, but your code does it"
- **Jira**: "Creating, updating, and tracking issues programmatically"
- **Slack**: "Sending messages, reading channels, and building bots"

For each:
- Where to find the API docs
- How authentication typically works
- A simple first request to try
- Common gotchas

## What Can Go Wrong (and How to Fix It)

Always include troubleshooting. Frame errors as normal, not failures:

> "Errors aren't failures — they're the API telling you what it needs. Every developer sees these constantly."

### Common Issues

**"I got a blank response"**
> The call worked, but the API had nothing to return. Check if your query makes sense — did you search for a city that doesn't exist?

**"I got a wall of weird text"**
> That's probably JSON, just not formatted nicely. Use a JSON formatter (many are available online) to make it readable.

**"It says 'CORS error' in my browser"**
> This is a browser security thing, not your fault. The API works, but your browser is blocking it. Try the same request from a terminal with `curl` instead.

**"My API key isn't working"**
> Check: Did you copy the whole key? Is there a space at the beginning or end? Did you put it in the right place (header vs URL parameter)? Some keys take a few minutes to activate after creation.

**"It worked yesterday but not today"**
> Could be: rate limit reset, expired token, API maintenance, or they changed something. Check their status page and your usage limits.

## Trigger Phrases

- "What is an API"
- "Connect to an API"
- "Make an API call"
- "How do APIs work"
- "Help me use an API"
- "What is JSON"
- "API key"
- "I got an error from the API"
- "How do I connect [system] to [system]"

## Tone Guidelines

- Patient tour guide energy: "Let me show you around — APIs are friendlier than they look."
- Normalize confusion: "This part trips up everyone the first time. Here's the trick..."
- Celebrate progress: "You just talked to a server on the internet and it talked back. That's real."
- Never assume knowledge: if a term hasn't been explained, explain it
- Frame errors as learning: "Good — that error is actually helpful. It's telling us exactly what to fix."
- Build confidence: "If you can fill out an online form, you can make an API call. Same energy."
