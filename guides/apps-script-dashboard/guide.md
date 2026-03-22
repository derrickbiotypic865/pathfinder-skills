# Build Your First Dashboard — Self-Paced Guide

## What You'll Build

An interactive web dashboard that reads data from a Google Sheet and displays it as a clean, styled web page with a shareable URL. It looks like this:

- A professional table with your data
- Color-coded status badges (green, orange, red)
- Hover effects on rows
- A refresh button
- A URL you can share with anyone

## What You'll Learn

By the end of this guide, you'll know how to:

1. Open and use the Apps Script editor
2. Read data from a Google Sheet with code
3. Create an HTML web page
4. Connect the web page to your data
5. Deploy it as a web app with a URL
6. Add advanced services
7. Set up triggers (automatic schedules)
8. Use CLASP to work from your computer

## Time Needed

About 60-90 minutes. No rush — take breaks whenever you want. You can also stop after any step and come back later.

## Prerequisites

- A Google account
- Chrome browser
- No coding experience needed — we explain everything

---

## Step 1: Set Up Your Data (5 min)

1. Go to [sheets.google.com](https://sheets.google.com)
2. Click **Blank spreadsheet** to create a new one
3. Name it "My Dashboard" (click "Untitled spreadsheet" at the top left)
4. Right-click the sheet tab at the bottom (it probably says "Sheet1") and rename it to **Dashboard Data**
5. Type this data into the sheet:

| | A | B | C | D |
|:--|:--|:--|:--|:--|
| **1** | Team | Status | Score | Last Updated |
| **2** | Alpha | On Track | 87 | 2026-03-20 |
| **3** | Beta | At Risk | 62 | 2026-03-19 |
| **4** | Gamma | On Track | 91 | 2026-03-21 |
| **5** | Delta | Behind | 45 | 2026-03-18 |
| **6** | Echo | On Track | 78 | 2026-03-22 |

Done? Great — you have your data source.

---

## Step 2: Open the Apps Script Editor (3 min)

1. In your Google Sheet, click **Extensions** in the top menu bar
2. Click **Apps Script**
3. A new tab opens — this is the Apps Script editor

**What you see:**
- **Left sidebar**: Your files. Right now there's just `Code.gs`
- **Center**: The code editor. It has an empty function called `myFunction()`
- **Top toolbar**: The **Run** button (play icon), the **Save** button (floppy disk icon), and a dropdown to select which function to run

Don't worry if this looks unfamiliar. We'll explain everything as we go.

---

## Step 3: Your First Function (5 min)

Let's write code that does something — a popup message.

1. **Delete** everything in Code.gs (select all with Ctrl+A, then press Delete)
2. **Type** this code (don't copy-paste yet — typing helps you learn):

```javascript
// This function shows a popup message in our spreadsheet
// Think of it like creating a "hello world" greeting
function showMessage() {
  // SpreadsheetApp is the tool that connects us to Google Sheets
  // getUi() gets the "user interface" — the screen you see
  // alert() shows a popup box with our message
  SpreadsheetApp.getUi().alert('Hello! My first script is working!');
}
```

3. Click **Save** (Ctrl+S or the floppy disk icon)
4. Make sure `showMessage` is selected in the function dropdown (next to the Run button)
5. Click **Run** (the play/triangle button)

**First time running? You'll see a permission popup:**

6. A dialog says "Authorization required" — click **Review permissions**
7. Choose your Google account
8. You might see "Google hasn't verified this app" — this is normal for personal scripts
9. Click **Advanced** (small text at bottom left)
10. Click **Go to Untitled project (unsafe)** — it IS safe because YOU wrote this script
11. Review the permissions and click **Allow**

**You should see a popup in your spreadsheet with your message!**

Congratulations — you just ran code. Every developer in the world started exactly like this.

---

## Step 4: Read Data From Your Sheet (10 min)

Now let's read the data from your spreadsheet. This is how we'll get data into our dashboard.

1. Go back to the Apps Script tab
2. **Add this function** below your showMessage function (don't delete showMessage — just add below it):

```javascript
// This function reads all the data from our "Dashboard Data" sheet
// and shows it in the log so we can see what it looks like
function readDashboardData() {
  // Get the spreadsheet this script is attached to
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  // Find the sheet tab called "Dashboard Data"
  var sheet = spreadsheet.getSheetByName('Dashboard Data');

  // Get ALL the data from that sheet
  // getDataRange() = "grab everything that has data"
  // getValues() = "give me the actual values, not formulas"
  var allData = sheet.getDataRange().getValues();

  // Show the raw data in the log
  Logger.log('All data:');
  Logger.log(allData);

  // The first row (row 0) is the headers: Team, Status, Score, Last Updated
  var headers = allData[0];
  Logger.log('Headers: ' + headers);

  // Everything after row 0 is actual data
  var dataRows = allData.slice(1);
  Logger.log('Number of data rows: ' + dataRows.length);

  // Access specific data:
  // dataRows[0] = first data row (Alpha)
  // dataRows[0][0] = first column of first row (the team name)
  Logger.log('First team: ' + dataRows[0][0]);
  Logger.log('First team status: ' + dataRows[0][1]);
  Logger.log('First team score: ' + dataRows[0][2]);
}
```

3. **Save** (Ctrl+S)
4. Select `readDashboardData` in the function dropdown
5. Click **Run**
6. Look at the **Execution log** at the bottom of the screen

**What you see in the log:**
The data appears as a list of lists — like a grid. Each row is wrapped in square brackets.

**Key concept — Arrays:**
- An array is just a list of items: `['Alpha', 'On Track', 87, '2026-03-20']`
- Your spreadsheet data comes back as a list of lists (an array of arrays) — one list per row
- Computers start counting at 0, not 1. So `allData[0]` is the FIRST row (headers), `allData[1]` is the SECOND row (Alpha)
- `allData[1][0]` = row 1, column 0 = "Alpha"

If this feels confusing, that's normal. It clicks after you use it a few times.

---

## Step 5: Create the Dashboard HTML (15 min)

Now we'll create the web page that becomes our dashboard.

1. In the Apps Script editor, click **+** next to **Files** (in the left sidebar)
2. Select **HTML**
3. Name it `Dashboard` (just Dashboard, no .html)
4. A new file appears with some default HTML — **delete everything** in it
5. **Paste** this code (this one is long, so pasting is fine):

```html
<!DOCTYPE html>
<html>
<head>
  <!-- The title that appears in the browser tab -->
  <title>Team Dashboard</title>

  <style>
    /* ===== PAGE LAYOUT ===== */

    /* Set the background color and font for the whole page */
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

    /* Style the subtitle/timestamp */
    .subtitle {
      color: #888;
      font-size: 14px;
      margin-bottom: 20px;
    }

    /* ===== TABLE STYLES ===== */

    /* Make the table look professional */
    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      border-radius: 8px;
      overflow: hidden;
    }

    /* Style the header row (Team, Status, Score, Last Updated) */
    th {
      background-color: #4285f4;
      color: white;
      padding: 12px 16px;
      text-align: left;
      font-weight: 600;
    }

    /* Style each data cell */
    td {
      padding: 10px 16px;
      border-bottom: 1px solid #eee;
    }

    /* Highlight rows when you hover over them */
    tr:hover {
      background-color: #f0f7ff;
    }

    /* ===== STATUS COLORS ===== */

    /* Green for On Track */
    .on-track {
      color: #2e7d32;
      font-weight: bold;
    }

    /* Orange for At Risk */
    .at-risk {
      color: #f57c00;
      font-weight: bold;
    }

    /* Red for Behind */
    .behind {
      color: #c62828;
      font-weight: bold;
    }

    /* ===== BUTTONS AND MESSAGES ===== */

    /* Loading message */
    #loading {
      color: #888;
      font-style: italic;
      padding: 20px;
    }

    /* Refresh button */
    .refresh-btn {
      background-color: #4285f4;
      color: white;
      border: none;
      padding: 8px 16px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      margin-bottom: 16px;
    }

    .refresh-btn:hover {
      background-color: #3367d6;
    }
  </style>
</head>

<body>

  <!-- Page header -->
  <h1>Team Dashboard</h1>
  <p class="subtitle">Data pulled live from Google Sheets</p>

  <!-- Refresh button -->
  <button class="refresh-btn" onclick="loadData()">Refresh Data</button>

  <!-- This shows while data is loading -->
  <p id="loading">Loading data from spreadsheet...</p>

  <!-- This is our data table (hidden until data loads) -->
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
      <!-- JavaScript will fill this in with data from the spreadsheet -->
    </tbody>
  </table>

  <!-- Timestamp at the bottom -->
  <p class="subtitle" id="timestamp"></p>

  <script>
    // ===== LOAD DATA FROM THE SERVER =====

    // This runs when the page first opens
    document.addEventListener('DOMContentLoaded', function() {
      loadData();
    });

    // This function asks the server (Code.gs) for spreadsheet data
    function loadData() {
      document.getElementById('loading').style.display = 'block';
      document.getElementById('loading').textContent = 'Loading data...';

      // google.script.run calls a function in our Code.gs file
      // withSuccessHandler = "when the data arrives, run displayData"
      // withFailureHandler = "if something goes wrong, show the error"
      // getDashboardData = the function name in Code.gs
      google.script.run
        .withSuccessHandler(displayData)
        .withFailureHandler(function(error) {
          document.getElementById('loading').textContent = 'Error loading data: ' + error;
        })
        .getDashboardData();
    }

    // ===== DISPLAY DATA IN THE TABLE =====

    // This function runs when the data arrives from the server
    function displayData(data) {
      var tbody = document.getElementById('tableBody');
      var loading = document.getElementById('loading');
      var table = document.getElementById('dashboardTable');
      var timestamp = document.getElementById('timestamp');

      // Clear any existing rows (important for refresh)
      tbody.innerHTML = '';

      // Hide loading message, show the table
      loading.style.display = 'none';
      table.style.display = 'table';

      // Loop through each row of data
      for (var i = 0; i < data.length; i++) {
        var row = data[i];

        // Create a new table row
        var tr = document.createElement('tr');

        // Column 1: Team name
        var tdTeam = document.createElement('td');
        tdTeam.textContent = row[0];
        tr.appendChild(tdTeam);

        // Column 2: Status (with color coding)
        var tdStatus = document.createElement('td');
        tdStatus.textContent = row[1];
        // Add the right CSS class based on the status
        var statusText = String(row[1]).toLowerCase();
        if (statusText === 'on track') tdStatus.className = 'on-track';
        if (statusText === 'at risk') tdStatus.className = 'at-risk';
        if (statusText === 'behind') tdStatus.className = 'behind';
        tr.appendChild(tdStatus);

        // Column 3: Score
        var tdScore = document.createElement('td');
        tdScore.textContent = row[2];
        tr.appendChild(tdScore);

        // Column 4: Last Updated
        var tdUpdated = document.createElement('td');
        tdUpdated.textContent = row[3];
        tr.appendChild(tdUpdated);

        // Add the row to the table
        tbody.appendChild(tr);
      }

      // Show when the data was last refreshed
      timestamp.textContent = 'Last refreshed: ' + new Date().toLocaleString();
    }
  </script>
</body>
</html>
```

**What this does:**
- Creates a clean, styled web page with a table
- When the page loads, it calls `getDashboardData()` in your Code.gs
- When the data comes back, it fills in the table
- Status values get color-coded (green, orange, red)
- There's a Refresh button to reload data anytime

---

## Step 6: Connect the Dashboard to Your Data (10 min)

Go back to **Code.gs**. You can keep your earlier functions, but we need to add two new ones. Add these at the bottom:

```javascript
// ===== WEB APP FUNCTIONS =====

// This function runs when someone visits the web app URL
// It's like the "front door" of your dashboard
function doGet() {
  // Load our Dashboard.html file and serve it as a web page
  return HtmlService
    .createHtmlOutputFromFile('Dashboard')
    .setTitle('Team Dashboard');
}

// This function is called by the dashboard's JavaScript
// It reads the sheet data and sends it to the web page
function getDashboardData() {
  // Open the spreadsheet and find our data sheet
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('Dashboard Data');

  // Get all the data
  var allData = sheet.getDataRange().getValues();

  // Remove the header row (the dashboard already shows headers)
  var dataRows = allData.slice(1);

  // Clean up the data for the web page
  // Dates need special handling so they display correctly
  var cleanedData = dataRows.map(function(row) {
    return row.map(function(cell) {
      // If the cell is a Date object, convert it to a simple string
      if (cell instanceof Date) {
        return cell.toISOString().split('T')[0]; // Returns "2026-03-20"
      }
      return cell;
    });
  });

  return cleanedData;
}
```

**Save** (Ctrl+S).

**What we just did:**
- `doGet()` = the front door. When someone visits your URL, this runs and shows the Dashboard.html page
- `getDashboardData()` = the data supplier. The web page asks for data, this function reads the sheet and sends it back
- Think of it like a restaurant: `doGet()` is the host who seats you, `getDashboardData()` is the waiter who brings your food

---

## Step 7: Deploy as a Web App (5 min)

Time to make your dashboard live!

1. Click **Deploy** (top right of the editor)
2. Click **New deployment**
3. Click the **gear icon** next to "Select type"
4. Choose **Web app**
5. Fill in:
   - **Description**: "My first dashboard"
   - **Execute as**: "Me" (your email)
   - **Who has access**: Choose based on who should see it:
     - "Only myself" — just for testing
     - "Anyone within [your organization]" — for coworkers
     - "Anyone" — for the world
6. Click **Deploy**
7. **Copy the URL** that appears
8. Open it in a **new browser tab**

**You should see your dashboard with live data from your spreadsheet!**

You now have a live web app with a URL. Change the data in your spreadsheet, click Refresh in the dashboard, and the numbers update.

---

## Step 8: Make It Your Own (10 min)

Try any of these customizations:

**Change the colors:**
- Find the `.on-track` CSS class and change `#2e7d32` to any color
- Try: `#1565c0` (blue), `#6a1b9a` (purple), `#00695c` (teal)

**Add a new column:**
- Add a column E to your spreadsheet (e.g., "Owner")
- Add a new `<th>Owner</th>` in the HTML table header
- Add a new `td` block in the JavaScript for `row[4]`

**Change the title:**
- Find `<h1>Team Dashboard</h1>` and change it

**Add a summary row:**
- After the table, add: `<p>Total teams: <span id="count"></span></p>`
- In displayData(), add: `document.getElementById('count').textContent = data.length;`

After making changes, save and redeploy (Deploy > Manage deployments > pencil icon > New version > Deploy) to see them live.

---

## Step 9: Add Advanced Services (5 min)

So far we've used built-in services (SpreadsheetApp). Google offers dozens more you can unlock.

**How to add a service:**
1. In the Apps Script editor, look at the left sidebar
2. Click the **+** next to **Services**
3. A list of Google APIs appears
4. Find the one you want (e.g., **Sheets API**)
5. Click it to select it
6. Click **Add**

**When do you need advanced services?**
- Built-in services (`SpreadsheetApp`, `GmailApp`, `DriveApp`) handle most tasks
- Advanced services give you access to more powerful features
- Think of it like upgrading from basic cable to premium — more channels, more options

**Common advanced services:**
- **Sheets API** — batch updates, advanced formatting
- **Gmail API** — watching for new emails, batch operations
- **Calendar API** — advanced calendar operations
- **Drive API** — managing permissions, advanced file operations

---

## Step 10: Set Up Triggers (5 min)

Triggers make your code run automatically — like setting an alarm.

**Method 1 — From the menu (easiest):**
1. Click the **clock icon** in the left sidebar (Triggers)
2. Click **+ Add Trigger** (bottom right)
3. Choose:
   - **Function**: `getDashboardData`
   - **Event source**: Time-driven
   - **Type**: Hour timer (or Day timer, Minute timer, etc.)
   - **Interval**: Every hour (or every day, etc.)
4. Click **Save**

Your function now runs automatically on that schedule.

**Method 2 — In code (better for sharing):**

Add this function to your Code.gs:

```javascript
// Run this function ONCE to set up a daily automatic trigger
// After running it once, delete the trigger setup or it will create duplicates
function setupDailyTrigger() {
  // First, remove any existing triggers for this function
  // (prevents duplicate triggers if you run this more than once)
  var triggers = ScriptApp.getProjectTriggers();
  for (var i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'getDashboardData') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }

  // Create a new trigger: run getDashboardData every day at 8 AM
  ScriptApp.newTrigger('getDashboardData')
    .timeBased()
    .atHour(8)
    .everyDays(1)
    .create();

  Logger.log('Trigger created! Data will refresh every day at 8 AM.');
}
```

Run `setupDailyTrigger` once. Then check the clock icon — you'll see the trigger listed.

**To remove a trigger:**
1. Click the clock icon
2. Find the trigger
3. Click the three dots on the right
4. Click **Delete trigger**

---

## Step 11: Use CLASP (Optional — 15 min)

CLASP lets you work on Apps Script from your computer instead of the browser. This is optional but powerful.

**Why use CLASP?**
- Use any text editor (VS Code, Sublime, etc.) instead of the browser editor
- Track changes with git
- Collaborate with others
- Work offline

**Install CLASP:**

1. **Install Node.js** (if you don't have it):
   - Go to [nodejs.org](https://nodejs.org)
   - Download the **LTS** version
   - Run the installer — click Next through all steps
   - To verify: open a terminal and type `node --version`

2. **Install CLASP:**
   ```bash
   npm install -g @google/clasp
   ```

3. **Log in to Google:**
   ```bash
   clasp login
   ```
   A browser window opens — sign in and allow access.

**Pull your dashboard project:**

1. In the Apps Script editor, click the **gear icon** (Project Settings)
2. Copy the **Script ID**
3. In your terminal:
   ```bash
   mkdir my-dashboard
   cd my-dashboard
   clasp clone YOUR_SCRIPT_ID_HERE
   ```
4. Your files are now on your computer!

**Edit and push:**
```bash
# Edit files with any text editor
# Then push changes back to Google:
clasp push

# Open in browser to verify:
clasp open
```

**Useful CLASP commands:**

| Command | What it does |
|:--------|:-------------|
| `clasp pull` | Download latest code from Google |
| `clasp push` | Upload your local code to Google |
| `clasp push --watch` | Auto-upload every time you save |
| `clasp open` | Open the project in the browser |
| `clasp deployments` | List all deployments |

---

## Troubleshooting

| Error | What it means | What to do |
|:------|:-------------|:-----------|
| "Authorization required" | The script needs permission to access Google services | Click Review permissions > Advanced > Go to project > Allow |
| "TypeError: Cannot read properties of null" | Usually the sheet name doesn't match | Check that your tab is named exactly "Dashboard Data" (case-sensitive) |
| "Service invoked too many times" | Google rate limit hit | Wait a few minutes and try again |
| "doGet is not defined" | The function name is wrong or missing | Make sure you have a function called `doGet` (capital G) in Code.gs |
| Web app shows blank page | JavaScript error in the HTML | Press F12 in the browser, click Console, look for red error messages |
| "This app isn't verified" during deployment | Normal for personal scripts | Click Advanced > Go to project name (unsafe) > Allow |
| Changes don't appear in the web app | Need to redeploy | Deploy > Manage deployments > pencil icon > New version > Deploy |
| CLASP says "not logged in" | Session expired | Run `clasp login` again |

---

## Full Code Reference

Here's the complete, final code for both files. If you got lost anywhere, you can compare your code to this.

### Code.gs (complete)

```javascript
// ===== UTILITY FUNCTIONS =====

// Shows a popup message — your first script!
function showMessage() {
  SpreadsheetApp.getUi().alert('Hello! My first script is working!');
}

// Reads data from the sheet and shows it in the log
function readDashboardData() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('Dashboard Data');
  var allData = sheet.getDataRange().getValues();
  Logger.log('All data:');
  Logger.log(allData);
}

// ===== WEB APP FUNCTIONS =====

// The "front door" — runs when someone visits the web app URL
function doGet() {
  return HtmlService
    .createHtmlOutputFromFile('Dashboard')
    .setTitle('Team Dashboard');
}

// Called by the dashboard to get spreadsheet data
function getDashboardData() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('Dashboard Data');
  var allData = sheet.getDataRange().getValues();
  var dataRows = allData.slice(1);

  // Clean up dates for display
  var cleanedData = dataRows.map(function(row) {
    return row.map(function(cell) {
      if (cell instanceof Date) {
        return cell.toISOString().split('T')[0];
      }
      return cell;
    });
  });

  return cleanedData;
}

// ===== TRIGGER SETUP =====

// Run ONCE to set up automatic daily data refresh
function setupDailyTrigger() {
  // Remove existing triggers to prevent duplicates
  var triggers = ScriptApp.getProjectTriggers();
  for (var i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'getDashboardData') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }

  // Create daily trigger at 8 AM
  ScriptApp.newTrigger('getDashboardData')
    .timeBased()
    .atHour(8)
    .everyDays(1)
    .create();

  Logger.log('Trigger created! Data refreshes daily at 8 AM.');
}
```

### Dashboard.html (complete)

*(Same as the full HTML from Step 5 above — included in the facilitator guide)*

---

## What's Next?

You built a dashboard from scratch. Here are some ideas to keep going:

1. **Add charts**: Use Google Charts to visualize your data
2. **Add filtering**: Let users click a status to show only those teams
3. **Pull from multiple sheets**: Combine data from different tabs or spreadsheets
4. **Send email reports**: Use GmailApp to email the dashboard data weekly
5. **Add a form**: Let people submit updates through the dashboard
6. **Connect to APIs**: Pull data from external services

**Challenge:** Find one thing you do manually this week. Could Apps Script automate it?

**Resources:**
- [Apps Script documentation](https://developers.google.com/apps-script)
- The patterns-reference.md file in this repo — battle-tested code recipes
- Ask Claude Code with `/learn` mode for plain-English explanations

**Remember:** You're not someone who "can't code" anymore. You built a web app. You're a builder.
