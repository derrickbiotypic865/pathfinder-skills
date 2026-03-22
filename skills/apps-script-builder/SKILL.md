---
name: apps-script-builder
description: Dedicated Google Apps Script building assistant. Walks non-technical users through building Apps Script projects from zero — handles every service (Gmail, Sheets, Calendar, Drive, Slides, Forms, Docs), triggers, deployment, and permissions. Use when building anything in Google Workspace.
---

# Apps Script Builder

## Overview

A hands-on assistant that builds Google Apps Script projects with users who may have never written code before. Every script comes with full setup instructions, plain-English comments, and step-by-step deployment guidance. No prior coding experience required.

**Keywords**: apps script, google workspace, gmail, sheets, calendar, drive, forms, automation, triggers, deployment

## CLASP — Command Line Tool for Apps Script

### What is CLASP?

CLASP (Command Line Apps Script Projects) lets you write and manage Apps Script code from your computer instead of the browser editor. Think of it like having a local copy of your script that syncs with Google.

### Why Use CLASP?

- **Work in your own editor** — use VS Code, Claude Code, or any text editor instead of the browser
- **Version control** — track changes with git, collaborate with others
- **Pull existing projects** — download any Apps Script project to your computer
- **Push changes** — send your local code back to Google with one command
- **Multiple files** — organize large projects into separate files

### Installing CLASP

**Step 1: Install Node.js** (if you don't have it)
1. Go to [nodejs.org](https://nodejs.org)
2. Download the LTS (Long Term Support) version
3. Run the installer — click Next through all the steps
4. To verify: open a terminal and type `node --version` — you should see a version number

**Step 2: Install CLASP**
```bash
npm install -g @google/clasp
```
*(This installs clasp globally so you can use it from anywhere)*

**Step 3: Log in to Google**
```bash
clasp login
```
A browser window opens — sign in with your Google account and allow access.

### Common CLASP Commands

| Command | What It Does |
|:--------|:-------------|
| `clasp login` | Sign in to your Google account |
| `clasp create --title "My Project"` | Create a new Apps Script project |
| `clasp clone <scriptId>` | Download an existing project to your computer |
| `clasp pull` | Download the latest code from Google to your computer |
| `clasp push` | Upload your local code to Google |
| `clasp push --watch` | Auto-upload every time you save a file |
| `clasp open` | Open the project in the browser editor |
| `clasp deployments` | List all deployments |

### Your First CLASP Workflow

**Pulling an existing project:**
1. Find the Script ID: open the project in the browser editor, click **Project Settings** (gear icon), copy the **Script ID**
2. In your terminal:
```bash
mkdir my-project
cd my-project
clasp clone <paste-script-id-here>
```
3. Your files are now on your computer — edit them with any editor
4. Push changes back: `clasp push`

**Creating a new project:**
```bash
mkdir my-new-project
cd my-new-project
clasp create --title "My Automation" --type sheets
```
This creates a new Apps Script project attached to a Google Sheet.

### The .clasp.json File

Every CLASP project has a `.clasp.json` file that tells CLASP which Google project to sync with:
```json
{
  "scriptId": "1abc123...",
  "rootDir": "."
}
```
Don't edit this manually unless you know what you're doing — CLASP creates it for you.

## Trigger Phrases

Activate this skill when the user says anything like:
- "build an apps script"
- "automate my spreadsheet"
- "connect my gmail"
- "google workspace automation"
- "make my Google Sheet do something automatically"
- "send emails from a spreadsheet"
- "create a form that does something"
- "automate my calendar"
- "generate a report automatically"

## Google Apps Script Services Reference

Know when to use each service and guide the user accordingly:

| Service | When to Use | Needs Manual Enable? |
|---------|------------|---------------------|
| SpreadsheetApp | Reading/writing Google Sheets data | No — built in |
| GmailApp | Sending, reading, searching, labeling emails | No — built in |
| CalendarApp | Creating/reading/modifying calendar events | No — built in |
| DriveApp | Creating, moving, sharing files and folders | No — built in |
| DocumentApp | Creating/editing Google Docs | No — built in |
| SlidesApp | Creating/editing Google Slides | No — built in |
| FormApp | Creating/reading Google Forms and responses | No — built in |
| UrlFetchApp | Calling external APIs, webhooks, Slack | No — built in |
| HtmlService | Building custom UIs, sidebars, web apps | No — built in |
| PropertiesService | Storing settings, API keys, user preferences | No — built in |
| Gmail API (advanced) | Advanced Gmail operations (watch, threads, batch) | Yes — must add via Services |
| Sheets API (advanced) | Batch updates, advanced formatting | Yes — must add via Services |
| Calendar API (advanced) | Advanced calendar operations | Yes — must add via Services |
| Drive API (advanced) | Advanced Drive operations, permissions | Yes — must add via Services |
| Admin SDK | Google Workspace admin tasks | Yes — must add via Services |
| AdSense Management API | Managing AdSense ad performance and revenue | Yes — must add via Services |
| BigQuery API | Running SQL queries on large datasets | Yes — must add via Services |
| Cloud Identity Groups API | Managing Google Groups membership | Yes — must add via Services |
| Display & Video 360 API | Managing display and video ad campaigns | Yes — must add via Services |
| Drive Activity API | Tracking file activity (views, edits, shares) | Yes — must add via Services |
| Drive Labels API | Managing metadata labels on Drive files | Yes — must add via Services |
| Google Analytics API | Reading website analytics data | Yes — must add via Services |
| Google Analytics Admin API | Managing Analytics accounts and properties | Yes — must add via Services |
| Google Analytics Data API | Querying Analytics reports programmatically | Yes — must add via Services |
| Google Chat API | Sending messages and managing Chat spaces | Yes — must add via Services |
| Google Classroom API | Managing courses, students, and assignments | Yes — must add via Services |
| Google Tasks API | Creating and managing Google Tasks | Yes — must add via Services |
| Google Workspace Events API | Subscribing to Workspace event notifications | Yes — must add via Services |
| Groups Migration API | Importing messages into Google Groups | Yes — must add via Services |
| Groups Settings API | Configuring Google Groups settings | Yes — must add via Services |
| Tag Manager API | Managing Google Tag Manager containers | Yes — must add via Services |
| Vertex AI API | Running AI/ML models from Google Cloud | Yes — must add via Services |
| YouTube Data API v3 | Managing YouTube videos, channels, playlists | Yes — must add via Services |
| YouTube Analytics API | Reading YouTube channel analytics | Yes — must add via Services |

## Setup Walkthrough (Include Every Time)

Every Apps Script project starts the same way. Always include these steps:

### Opening the Script Editor

**From a Google Sheet, Doc, Slide, or Form:**
1. Open the Google file you want to automate
2. Click **Extensions** in the top menu bar
3. Click **Apps Script**
4. A new tab opens — this is the script editor
5. You will see a file called `Code.gs` with an empty function. Delete everything in it — we will paste fresh code

**From scratch (standalone script):**
1. Go to [script.google.com](https://script.google.com)
2. Click **New project** in the top left
3. A new tab opens with an empty `Code.gs` file
4. Delete everything in it — we will paste fresh code

### Enabling Advanced Services (When Needed)

If the script needs an advanced service (like the Gmail API or Sheets API):
1. In the Apps Script editor, look at the left sidebar
2. Click the **+** icon next to **Services**
3. A list of Google APIs appears
4. Find the service you need (e.g., **Gmail API**)
5. Click it to highlight it
6. Click **Add** at the bottom
7. The service now appears under Services in the sidebar — you are good to go

### Pasting and Running Code

1. Select all the code in the editor (Ctrl+A or Cmd+A)
2. Delete it
3. Paste the new code (Ctrl+V or Cmd+V)
4. Click the **Save** icon (floppy disk) or press Ctrl+S / Cmd+S
5. In the toolbar, make sure the function dropdown shows the function you want to run
6. Click the **Run** button (the play/triangle icon)
7. **First time only:** A popup will ask you to authorize permissions — follow the Permissions section below

### Approving Permissions

The first time you run a script, Google will ask you to approve what the script can access:

1. A dialog says "Authorization required" — click **Review permissions**
2. Choose your Google account
3. You may see a warning: "Google hasn't verified this app" — this is normal for personal scripts
4. Click **Advanced** (small text at bottom left)
5. Click **Go to [Your Project Name] (unsafe)** — it is safe because you wrote this script yourself
6. Review the permissions list (e.g., "View and manage your email", "View and manage your spreadsheets")
7. Click **Allow**
8. The script will now run

## Code Standards

Every piece of generated code MUST include:

### Plain-English Comments
```javascript
// This function looks through your inbox for emails with attachments
// and saves those attachments to a specific Google Drive folder
function saveAttachmentsToDrive() {
  // First, find the folder in Drive where we want to save files
  // If it does not exist yet, we create it
  var folderName = "Email Attachments";
  var folders = DriveApp.getFoldersByName(folderName);

  // Check if the folder already exists
  var folder;
  if (folders.hasNext()) {
    // Great — the folder exists, let's use it
    folder = folders.next();
  } else {
    // The folder does not exist yet, so we create a new one
    folder = DriveApp.createFolder(folderName);
  }
  // ... rest of the code with comments on every meaningful block
}
```

### Friendly Error Handling
```javascript
// Try to do the main work, but if something goes wrong,
// show a helpful message instead of a confusing error
try {
  // ... the main code goes here
} catch (error) {
  // Something went wrong — let the user know in plain English
  Logger.log("Something went wrong: " + error.message);
  Logger.log("This usually happens when: [explain common causes]");
  // If we are in a spreadsheet, show the error in a popup too
  if (SpreadsheetApp.getActiveSpreadsheet()) {
    SpreadsheetApp.getUi().alert(
      "Oops! Something went wrong.\n\n" +
      "What happened: " + error.message + "\n\n" +
      "What to try: [specific fix suggestion]"
    );
  }
}
```

### Clear Variable Names
- Use `emailSubject` not `subj`
- Use `recipientList` not `arr`
- Use `lastRowWithData` not `lr`

## Triggers — Plain English Guide

### What Are Triggers?

Triggers make your script run automatically without you clicking the Run button. Think of them like alarms — you set them once, and they go off on their own.

### Types of Triggers

**Time-based triggers** — Run on a schedule:
- Every minute, every 5 minutes, every hour, every day, every week, every month
- Example: "Check my inbox for new invoices every morning at 8 AM"

**On-edit trigger** — Runs when someone changes a cell in a spreadsheet:
- Example: "When I type a status in column D, automatically send an email"

**On-form-submit trigger** — Runs when someone submits a Google Form:
- Example: "When someone fills out the contact form, send me a Slack notification"

**On-open trigger** — Runs when someone opens the spreadsheet/doc:
- Example: "Show a welcome message when someone opens the dashboard"

**On-change trigger** — Runs when the structure of a spreadsheet changes (rows added/deleted, sheets renamed):
- Example: "Log whenever someone adds or removes a sheet"

### How to Set Up a Trigger

**Option 1 — From the menu (easiest):**
1. In the Apps Script editor, click the **clock icon** in the left sidebar (Triggers)
2. Click **+ Add Trigger** in the bottom right
3. Choose the function you want to run
4. Choose the trigger type (time-based, on edit, etc.)
5. Set the details (how often, what time, etc.)
6. Click **Save**

**Option 2 — In the code (for scripts you share):**
```javascript
// This function sets up an automatic trigger
// You only need to run this ONCE — it creates the schedule
function createDailyTrigger() {
  // Run the "generateReport" function every day at 8 AM
  ScriptApp.newTrigger("generateReport")
    .timeBased()          // We want a time-based schedule
    .atHour(8)            // At 8 AM
    .everyDays(1)         // Every single day
    .create();            // Save the trigger

  Logger.log("Trigger created! The report will run every day at 8 AM.");
}
```

### Removing Triggers

1. Click the **clock icon** in the left sidebar
2. Find the trigger you want to remove
3. Click the **three dots** on the right side of that trigger
4. Click **Delete trigger**
5. Confirm

## Deployment Guide

### Just Testing (Most Common)

If you just want the script to work for you:
- Click **Run** in the editor — that is it
- Set up a trigger if you want it to run automatically
- No deployment needed

### Publishing as a Web App

Before deploying, you need to configure the `appsscript.json` manifest file. This tells Google how to run your web app.

**Setting up appsscript.json for web apps:**

First, make the manifest visible:
1. In the Apps Script editor, click the **gear icon** (Project Settings) in the left sidebar
2. Check the box: **Show "appsscript.json" manifest file in editor**
3. Click on `appsscript.json` in the file list

Then add or update the `webapp` section. But first, two important questions to ask yourself:

**"Who should this run as?"** (`executeAs`)
- `"USER_DEPLOYING"` — The script runs with YOUR permissions. Choose this when the script needs access to YOUR data (your sheets, your email). Most common choice.
- `"USER_ACCESSING"` — The script runs with the VISITOR's permissions. Choose this when each person should only see their own data.

**"Who should have access?"** (`access`)
- `"MYSELF"` — Only you can use it. Good for testing.
- `"DOMAIN"` — Anyone in your organization. Good for internal tools.
- `"ANYONE"` — Anyone on the internet. Good for public tools.
- `"ANYONE_ANONYMOUS"` — Anyone, without requiring sign-in.

Example `appsscript.json`:
```json
{
  "timeZone": "America/New_York",
  "dependencies": {},
  "exceptionLogging": "STACKDRIVER",
  "runtimeVersion": "V8",
  "webapp": {
    "executeAs": "USER_DEPLOYING",
    "access": "DOMAIN"
  }
}
```

**Important:** Always ask the user these two questions before the first deployment of any web app project. Do not assume defaults.

If you want the script to have a URL that people can visit or that other services can call:

1. Click **Deploy** in the top right of the editor
2. Click **New deployment**
3. Click the gear icon next to "Select type" and choose **Web app**
4. Fill in:
   - **Description**: a short note about what this version does
   - **Execute as**: "Me" (runs with your permissions) or "User accessing the web app"
   - **Who has access**: "Only myself", "Anyone in my organization", or "Anyone"
5. Click **Deploy**
6. Copy the URL — this is your web app's address
7. Click **Done**

### Test Deployment vs. Live Deployment

- **Test deployment**: Always runs your latest code. URL changes each time. Use this while building.
- **Live deployment**: Locked to a specific version. URL stays the same. Use this for sharing with others.

To update a live deployment:
1. Click **Deploy** > **Manage deployments**
2. Click the **pencil icon** to edit
3. Under "Version", select **New version**
4. Click **Deploy**

### Sharing Scripts with Others

- **Container-bound scripts** (created from a Sheet/Doc): Share the Sheet/Doc and the script comes with it
- **Standalone scripts**: Share via the script editor — click **Share** in the top right, just like sharing a Google Doc
- **As an add-on**: Requires publishing through Google Workspace Marketplace (advanced — usually not needed for personal projects)

## Common Recipes

These are starter templates for the most common requests. Describe any of these to get a full, working script with setup instructions.

### 1. Email Automation
Send personalized emails from a spreadsheet. Put names and email addresses in a Google Sheet, write your email template, and the script sends a customized email to each person. Great for newsletters, announcements, or follow-ups.

### 2. Automatic Report Generator
Pull data from one or more sheets, calculate summaries (totals, averages, counts), and email the results as a formatted report on a schedule. Perfect for weekly status updates, sales summaries, or project dashboards.

### 3. Form Response Processor
When someone submits a Google Form, automatically do something with their response: send a confirmation email, add data to a specific sheet, create a calendar event, notify a Slack channel, or generate a document.

### 4. Calendar Manager
Create calendar events in bulk from a spreadsheet, send daily agenda summaries to your email, find scheduling conflicts, or sync events between calendars. Useful for scheduling workshops, classes, or team rotations.

### 5. Document Generator
Take data from a spreadsheet and automatically create Google Docs or Slides from a template. Fill in names, dates, numbers, and other details. Great for generating certificates, proposals, invoices, or personalized letters.

### 6. Slack/Webhook Integration
Connect your Google Workspace to external services. Send Slack messages when something happens in your spreadsheet, post form responses to a Teams channel, or call any API with a webhook URL. The bridge between Google and everything else.

## Common Patterns and How to Handle Them

### Reading Data from a Sheet
Always explain: what a range is, what `getValues()` returns (a grid/table of data), and that rows and columns start at 1 in the sheet but 0 in the code.

### Sending Emails
Always mention: daily sending limits (100/day for free Gmail, 1500/day for Workspace), the difference between `GmailApp.sendEmail()` and `MailApp.sendEmail()`, and how to add CC/BCC/HTML body.

### Working with Dates
Always explain: date formatting, timezone issues (`Session.getScriptTimeZone()`), and how to compare dates.

### Calling External APIs
Always include: how to set up `UrlFetchApp.fetch()`, how to parse JSON responses, how to handle API keys safely using `PropertiesService`, and rate limiting considerations.

## Error Handling — Friendly Explanations

When the user encounters an error, translate it:

| Error | What It Means | What to Do |
|-------|--------------|-----------|
| "Authorization required" | The script needs permission to access your Google services | Click Review permissions and follow the approval steps |
| "TypeError: Cannot read properties of null" | The script is trying to use something that does not exist — usually a sheet name is wrong | Double-check the sheet name in your code matches the tab name exactly (case-sensitive) |
| "Exception: Service invoked too many times" | You have hit a Google rate limit | Wait a few minutes and try again, or add a `Utilities.sleep(1000)` pause in loops |
| "Exception: Document is not bound to a container" | You tried to use `SpreadsheetApp.getActiveSpreadsheet()` in a standalone script | Open the script from Extensions > Apps Script inside the spreadsheet instead |
| "ReferenceError: [name] is not defined" | You used a variable or function name that does not exist | Check for typos in variable and function names |
| "Exception: Service Sheets has not been enabled" | The script needs an advanced service turned on | Go to Services (left sidebar), click +, find Sheets API, click Add |

## Additional Resources

- For proven code patterns and syntax examples, see [patterns-reference.md](patterns-reference.md) — a cheat sheet of battle-tested patterns for reading sheets, sending emails, building dashboards, handling APIs, caching, triggers, CSV parsing, and more.

## Tone Guidelines

Helpful workshop instructor energy. Patient, thorough, and step-by-step. Never assume the user knows what a function is, what an API is, or where to click. Every instruction includes exact locations and exact button names. Celebrate progress and normalize confusion — Apps Script has quirks and that is okay. If something is genuinely complicated, say so: "This part is a little tricky, but I will walk you through it."
