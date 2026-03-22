# Apps Script Workshop — Facilitator Guide

## Overview

- **Title**: Build Your First Dashboard with Google Apps Script
- **Duration**: 90 minutes
- **Audience**: Mixed — some have never coded, some have basic experience
- **What they'll build**: An interactive web dashboard that reads data from a Google Sheet
- **What they'll walk away with**: Ability to open Apps Script, create projects, deploy web apps, use CLASP, add services, and set up triggers

## Pre-Work (send 1-2 days before)

Send this to participants:

> **What to bring:** A laptop with Chrome and your Google account signed in.
>
> **Optional (for the advanced section):** Install Node.js from [nodejs.org](https://nodejs.org) — download the LTS version and run the installer. Then open a terminal and run: `npm install -g @google/clasp`
>
> **Mindset:** You don't need to be a developer. You need to be curious.
>
> **Teaser:** By the end of this workshop, you'll have a live dashboard with a URL you can share.

## Room Setup

- Everyone needs a laptop with Chrome
- Project your screen so they can follow along
- Have the finished dashboard URL ready to show as a demo at the start
- Share the self-paced guide link as backup for anyone who falls behind
- If virtual: use screen share and ask people to keep cameras on

## Sample Sheet Data

Have everyone create a Google Sheet with this data in a tab named "Dashboard Data":

| Team | Status | Score | Last Updated |
|:-----|:-------|:------|:-------------|
| Alpha | On Track | 87 | 2026-03-20 |
| Beta | At Risk | 62 | 2026-03-19 |
| Gamma | On Track | 91 | 2026-03-21 |
| Delta | Behind | 45 | 2026-03-18 |
| Echo | On Track | 78 | 2026-03-22 |

**Tip:** Share a pre-made copy of this sheet so they can just "File > Make a copy" instead of typing.

---

## Agenda (90 minutes)

### 1. Welcome + Why This Matters (5 min)

**What to say:**
- Share YOUR story — why you learned Apps Script, what problem it solved for you
- "Today we're going to build something real. Not a toy example — an actual dashboard with a URL you can share with anyone."

**What to show:**
- Open the finished dashboard in a browser tab — let them see the end result
- "By the end of today, you'll have built this yourself."

**Facilitator tip:** Keep this short and high-energy. The wow moment is seeing the finished product.

---

### 2. What is Apps Script? (5 min)

**What to say:**
- "Apps Script is a way to make Google Sheets, Gmail, Calendar, and Drive do things automatically."
- "If Google Workspace is a kitchen, Apps Script is the recipe book that tells the appliances what to do."
- "It uses JavaScript — one of the most popular programming languages in the world. But you don't need to know JavaScript to start. We'll learn as we go."

**What to show:**
- Open a Google Sheet
- Click **Extensions > Apps Script**
- Point out: the file list on the left, the code editor in the middle, the Run button at the top

**Facilitator tip:** Don't go deep on JavaScript. Just plant the seed that they're learning a real language.

---

### 3. Opening the Editor + First Script (10 min)

**What to say:**
- "Let's write our first line of code together. Everyone open your Google Sheet and go to Extensions > Apps Script."

**What to do (LIVE, together):**
1. Delete everything in Code.gs
2. Type together (don't paste — typing builds muscle memory):

```javascript
// This function shows a popup message in our spreadsheet
function showMessage() {
  // SpreadsheetApp connects to our Google Sheet
  // getUi() gets the user interface (the screen you see)
  // alert() shows a popup with our message
  SpreadsheetApp.getUi().alert('Hello! My first script is working!');
}
```

3. Click **Save** (Ctrl+S)
4. Make sure `showMessage` is selected in the function dropdown
5. Click **Run** (the play button)
6. Walk through the permission popup:
   - "Authorization required" — click **Review permissions**
   - Choose your account
   - "Google hasn't verified this app" — click **Advanced** > **Go to Untitled project (unsafe)**
   - Click **Allow**
7. The popup appears!

**What to celebrate:** "You just ran code. Every developer in the world started exactly like this."

**Facilitator tip:** WAIT for everyone. Walk around. The permission popup is where people get lost. Walk through EACH click. If someone is stuck, go to their screen.

---

### 4. Reading Data from a Sheet (10 min)

**What to say:**
- "Now let's read the data from our spreadsheet. This is how we'll get data into our dashboard."

**What to do (LIVE, together):**

```javascript
// This function reads all the data from our "Dashboard Data" sheet
function readDashboardData() {
  // Open the spreadsheet this script is attached to
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  // Find the sheet tab called "Dashboard Data"
  var sheet = spreadsheet.getSheetByName('Dashboard Data');

  // Get ALL the data from that sheet (every row and column that has content)
  var allData = sheet.getDataRange().getValues();

  // Show it in the log so we can see what we got
  Logger.log(allData);

  // The first row is the headers (Team, Status, Score, Last Updated)
  var headers = allData[0];
  Logger.log('Headers: ' + headers);

  // Everything after the first row is the actual data
  var dataRows = allData.slice(1);
  Logger.log('Number of data rows: ' + dataRows.length);
  Logger.log('First team: ' + dataRows[0][0]);
}
```

- Run it
- Show the **Execution log** (View > Execution log or the log panel at the bottom)
- Explain what they see: "It's a list of lists — like a grid. Each row is a list of values."

**Key concept to explain:**
- `getValues()` returns a grid — rows and columns
- Row 0 is the first row (headers), Row 1 is the second row (first data), etc.
- "Computers count from 0, not 1. It's weird, but you'll get used to it."

**Facilitator tip:** This is where beginners can get lost. Go SLOW. Point at the Logger output and map it back to the spreadsheet. "See? Row 0 is [Team, Status, Score, Last Updated] — that's our header row."

---

### 5. Building the Dashboard HTML (15 min)

**What to say:**
- "Now we're going to create a web page that displays our data. This will be our dashboard."

**What to do (LIVE, together):**

1. In the Apps Script editor, click **+** next to Files
2. Select **HTML**
3. Name it `Dashboard`
4. Delete everything and type together:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Team Dashboard</title>
  <style>
    /* Make the page look clean and modern */
    body {
      font-family: Arial, sans-serif;
      background-color: #f5f5f5;
      padding: 20px;
      margin: 0;
    }

    /* Style the main heading */
    h1 {
      color: #333;
      border-bottom: 3px solid #4285f4;
      padding-bottom: 10px;
    }

    /* Make the table look professional */
    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Style the header row */
    th {
      background-color: #4285f4;
      color: white;
      padding: 12px;
      text-align: left;
    }

    /* Style the data cells */
    td {
      padding: 10px 12px;
      border-bottom: 1px solid #eee;
    }

    /* Highlight rows when you hover over them */
    tr:hover { background-color: #f0f7ff; }

    /* Color-coded status badges */
    .on-track { color: #2e7d32; font-weight: bold; }
    .at-risk { color: #f57c00; font-weight: bold; }
    .behind { color: #c62828; font-weight: bold; }

    /* Loading message */
    #loading { color: #888; font-style: italic; }
  </style>
</head>
<body>

  <h1>Team Dashboard</h1>
  <p id="loading">Loading data from spreadsheet...</p>
  <table id="dashboardTable" style="display:none;">
    <thead>
      <tr>
        <th>Team</th>
        <th>Status</th>
        <th>Score</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody id="tableBody">
      <!-- Data will be inserted here by JavaScript -->
    </tbody>
  </table>

  <script>
    // When the page loads, ask the server for data
    document.addEventListener('DOMContentLoaded', function() {
      // google.script.run calls a function in our Code.gs file
      // withSuccessHandler says "when you get the data, run displayData"
      // getDashboardData is the function name in Code.gs we'll create next
      google.script.run
        .withSuccessHandler(displayData)
        .withFailureHandler(function(error) {
          document.getElementById('loading').textContent = 'Error: ' + error;
        })
        .getDashboardData();
    });

    // This function runs when the data arrives from the server
    function displayData(data) {
      var tbody = document.getElementById('tableBody');
      var loading = document.getElementById('loading');
      var table = document.getElementById('dashboardTable');

      // Hide the loading message, show the table
      loading.style.display = 'none';
      table.style.display = 'table';

      // Loop through each row of data and add it to the table
      for (var i = 0; i < data.length; i++) {
        var row = data[i];
        var tr = document.createElement('tr');

        // Team name
        var tdTeam = document.createElement('td');
        tdTeam.textContent = row[0];
        tr.appendChild(tdTeam);

        // Status with color coding
        var tdStatus = document.createElement('td');
        tdStatus.textContent = row[1];
        var statusLower = row[1].toLowerCase().replace(' ', '-');
        if (statusLower === 'on-track') tdStatus.className = 'on-track';
        if (statusLower === 'at-risk') tdStatus.className = 'at-risk';
        if (statusLower === 'behind') tdStatus.className = 'behind';
        tr.appendChild(tdStatus);

        // Score
        var tdScore = document.createElement('td');
        tdScore.textContent = row[2];
        tr.appendChild(tdScore);

        // Last Updated
        var tdUpdated = document.createElement('td');
        tdUpdated.textContent = row[3];
        tr.appendChild(tdUpdated);

        tbody.appendChild(tr);
      }
    }
  </script>
</body>
</html>
```

5. Now go back to Code.gs and add the server functions:

```javascript
// This function runs when someone visits the web app URL
// It serves our Dashboard.html file
function doGet() {
  return HtmlService
    .createHtmlOutputFromFile('Dashboard')
    .setTitle('Team Dashboard');
}

// This function is called by the dashboard web page
// It reads the data from the spreadsheet and sends it back
function getDashboardData() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('Dashboard Data');
  var allData = sheet.getDataRange().getValues();

  // Remove the header row — the dashboard already has headers
  var dataRows = allData.slice(1);

  // Clean up dates so they display nicely
  var cleanedData = dataRows.map(function(row) {
    return row.map(function(cell) {
      if (cell instanceof Date) {
        return cell.toISOString().split('T')[0]; // Just the date part
      }
      return cell;
    });
  });

  return cleanedData;
}
```

**What to explain:**
- doGet() = "This is the front door of your web app. When someone visits the URL, this runs."
- google.script.run = "This is how the web page talks to the server to get data."
- "The HTML is the face (what people see). Code.gs is the brain (where the data comes from)."

**Facilitator tip:** This is the longest section. Type the HTML slowly. Pause after the CSS to explain what each style does. Let people catch up.

---

### 6. Deploying as a Web App (10 min)

**What to do (LIVE, together):**

1. Click **Deploy** (top right)
2. Click **New deployment**
3. Click the gear icon next to "Select type"
4. Choose **Web app**
5. Fill in:
   - **Description**: "First version of my dashboard"
   - **Execute as**: Me (your email)
   - **Who has access**: "Anyone within [your organization]" or "Anyone"
6. Click **Deploy**
7. Copy the URL
8. Open in a new tab — the dashboard appears!

**What to say:**
- "You now have a live dashboard. That URL is yours. You can share it with anyone."
- Walk through the appsscript.json manifest for those who want to understand the config

**What to celebrate:** This is the BIG moment. Let people react. Let them share their URLs with each other.

**Facilitator tip:** Permission popups will confuse people again here. Walk through each step. If someone gets "This app isn't verified", walk them through Advanced > Go to project.

---

### 7. Adding Services (5 min)

**What to say:**
- "So far we've used built-in services like SpreadsheetApp. But Google has dozens of advanced services you can unlock."

**What to show:**
1. In the Apps Script editor, look at the left sidebar
2. Click **+** next to **Services**
3. A list appears — scroll through and show some: Gmail API, Calendar API, Sheets API
4. Click **Sheets API** > click **Add**
5. "Now you have access to advanced spreadsheet features."

**What to explain:**
- Built-in services (SpreadsheetApp, GmailApp) work out of the box
- Advanced services need to be turned on — just click + and Add
- "It's like unlocking extra features in a video game"

---

### 8. Triggers (5 min)

**What to say:**
- "Right now your dashboard shows data when you visit it. But what if you want code to run automatically — like refreshing data every hour?"
- "Triggers are like alarms for your code. Set it once, it runs on its own."

**What to show:**
1. Click the **clock icon** in the left sidebar (Triggers)
2. Click **+ Add Trigger** (bottom right)
3. Walk through the options:
   - Function: `getDashboardData`
   - Event source: Time-driven
   - Type: Hour timer
   - Interval: Every hour
4. Click **Save**

**Also show creating a trigger in code:**
```javascript
// Run this ONCE to set up an automatic daily refresh
function setupDailyTrigger() {
  ScriptApp.newTrigger('getDashboardData')
    .timeBased()
    .atHour(8)
    .everyDays(1)
    .create();
  Logger.log('Trigger created! Data will refresh every day at 8 AM.');
}
```

---

### 9. CLASP — Working From Your Computer (10 min)

**What to say:**
- "This section is for those who want to level up. CLASP lets you work on your scripts from your own computer instead of the browser."
- "Beginners — you can watch and try this later. Advanced folks — follow along."

**What to show:**
1. Open a terminal
2. `clasp login` — sign in to Google
3. `clasp clone <script-id>` — explain where to find the Script ID (Project Settings > Script ID)
4. Show the files on their computer — same Code.gs and Dashboard.html
5. Edit a file (change the dashboard title)
6. `clasp push` — changes go live
7. `clasp open` — opens in the browser to verify

**What to explain:**
- "CLASP is the bridge between your computer and Google's servers"
- "You can use any text editor — VS Code, Notepad, whatever you like"
- "Version control with git means you can track every change and collaborate with others"

---

### 10. Customize + Show and Tell (10 min)

**Challenge to the room:**
- "Add something to your dashboard. Ideas:"
  - Change the colors
  - Add a new column from the spreadsheet
  - Add a title or description
  - Change the status labels
  - Add a "last refreshed" timestamp
- Walk around and help
- After 7 minutes: "Who wants to share what they changed?"
- 2-3 volunteers share their screen

**Facilitator tip:** This is where the magic happens. People start making it their own. Encourage every attempt.

---

### 11. What's Next (5 min)

**What to say:**
- "You just built a dashboard from scratch. From a blank screen to a live web app in 90 minutes."
- "Here's what you can do next:"
  - Follow the self-paced guide to go deeper
  - Check out the patterns reference for code recipes
  - Find one thing you do manually this week and think about automating it
  - "If you get stuck, ask for help — that's how everyone learns"

**Resources to share:**
- Self-paced guide (link)
- Patterns reference (link)
- Apps Script documentation: [developers.google.com/apps-script](https://developers.google.com/apps-script)

**Close with:**
- "You're not someone who 'can't code' anymore. You built a web app today. You're a builder."

---

## Facilitator Tips (General)

- **Go slower than you think.** When you think you're going slow enough, go slower.
- **Ask "Is everyone with me?"** and ACTUALLY WAIT for responses. Count to 5 silently.
- **Walk to screens.** When someone is stuck, go to their laptop. Don't shout instructions across the room.
- **Celebrate everything.** First popup? Celebrate. First log output? Celebrate. First deployment? Big celebrate.
- **Normalize confusion.** "If this feels confusing right now, that's totally normal. Everyone feels this way the first time."
- **Mixed levels:** Give beginners extra attention during Steps 3-5. Give advanced folks the CLASP section to explore while beginners catch up.
- **Have the self-paced guide ready.** If someone falls behind, they can continue at their own pace after the workshop.

## Common Issues & Fixes

| Issue | Fix |
|:------|:----|
| "Authorization required" popup | Walk through step by step — Review permissions > Advanced > Go to project > Allow |
| Function doesn't show in dropdown | Make sure they saved (Ctrl+S) and the function has no syntax errors |
| "I don't see Extensions in the menu" | They might be in the wrong app — make sure they're in Google Sheets |
| Web app shows an error | Check that doGet() exists and returns HtmlService output |
| Web app shows blank page | Check browser console (F12) for JavaScript errors |
| CLASP says not logged in | Run `clasp login` again |
| "I changed the code but the web app didn't update" | They need to create a new deployment (Deploy > New Deployment) or use the test deployment URL |
| Data shows as "[object Date]" | Need the date cleaning code in getDashboardData() |
