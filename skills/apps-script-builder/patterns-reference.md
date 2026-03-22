# Apps Script Patterns & Syntax Reference

A cheat sheet of real-world patterns extracted from production Apps Script projects. Reference this when building Apps Script projects to use proven, battle-tested approaches.

## Reading Spreadsheet Data

### Read all data as rows
```javascript
const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('MySheet');
const data = sheet.getDataRange().getValues();
const headers = data[0];
const rows = data.slice(1);
```

### Read data as objects (rows keyed by header)
```javascript
function readSheetAsObjects(sheetName) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  const data = sheet.getDataRange().getValues();
  const headers = data[0].map(h => String(h).trim());
  const rows = [];
  for (let i = 1; i < data.length; i++) {
    const row = {};
    for (let j = 0; j < headers.length; j++) {
      row[headers[j]] = data[i][j] !== undefined ? data[i][j] : '';
    }
    rows.push(row);
  }
  return rows;
}
```

### Find column index by header name (never hardcode column numbers)
```javascript
const colIndex = headers.indexOf('App Name');
if (colIndex === -1) throw new Error('Column "App Name" not found');
```

### Write data in batches (avoid timeout on large datasets)
```javascript
const BATCH_SIZE = 5000;
for (let i = 0; i < allData.length; i += BATCH_SIZE) {
  const batch = allData.slice(i, Math.min(i + BATCH_SIZE, allData.length));
  sheet.getRange(i + 2, 1, batch.length, headers.length).setValues(batch);
}
```

### Format headers
```javascript
const headerRange = sheet.getRange(1, 1, 1, headers.length);
headerRange.setFontWeight('bold').setBackground('#4285f4').setFontColor('#ffffff');
sheet.setFrozenRows(1);
```

### Conditional formatting with formulas
```javascript
const rule = SpreadsheetApp.newConditionalFormatRule()
  .whenFormulaSatisfied('=ISBLANK($A2)')
  .setBackground('#FFCCCC')
  .setRanges([sheet.getRange('A2:A')])
  .build();
sheet.setConditionalFormatRules([rule]);
```

---

## Sending Emails

### Basic HTML email
```javascript
GmailApp.sendEmail('recipient@example.com', 'Subject Line', '', {
  htmlBody: '<h1>Hello</h1><p>This is HTML email</p>',
  cc: 'cc@example.com'
});
```

### Email with HTML template
```javascript
const template = HtmlService.createTemplateFromFile('email-template');
template.name = 'John';
template.items = myDataArray;
const htmlBody = template.evaluate().getContent();

GmailApp.sendEmail(toEmail, subject, '', { htmlBody: htmlBody });
```

### Batch email splitting (stay under Gmail's 102KB clipping limit)
```javascript
const ITEMS_PER_EMAIL = 12;
const totalBatches = Math.ceil(allItems.length / ITEMS_PER_EMAIL);
for (let batch = 0; batch < totalBatches; batch++) {
  const batchItems = allItems.slice(batch * ITEMS_PER_EMAIL, (batch + 1) * ITEMS_PER_EMAIL);
  // send email with batchItems
}
```

### Search Gmail for attachments
```javascript
const searchQuery = `from:sender@example.com subject:"Report" has:attachment after:2026/01/01`;
const threads = GmailApp.search(searchQuery, 0, 1);
if (threads.length > 0) {
  const messages = threads[0].getMessages();
  const attachments = messages[messages.length - 1].getAttachments();
}
```

---

## Web Apps & Dashboards

### Basic web app with routing
```javascript
function doGet(e) {
  const page = e.parameter.page || 'main';
  if (page === 'dashboard') {
    return HtmlService.createTemplateFromFile('Dashboard').evaluate().setTitle('Dashboard');
  }
  if (page === 'admin') {
    return HtmlService.createTemplateFromFile('Admin').evaluate().setTitle('Admin');
  }
  return HtmlService.createTemplateFromFile('Index').evaluate().setTitle('Home');
}
```

### Client calls server function
```javascript
// In your HTML file:
google.script.run
  .withSuccessHandler(function(data) {
    // data is whatever the server function returned
    console.log('Got data:', data);
  })
  .withFailureHandler(function(error) {
    console.error('Error:', error);
  })
  .getMyData();  // calls the server-side function getMyData()
```

### Server function returns data to client
```javascript
// In Code.gs:
function getMyData() {
  const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName('Data');
  const values = sheet.getDataRange().getValues();
  // Clean data for JSON serialization (dates and nulls cause issues)
  return values.map(row => row.map(cell => {
    if (cell === null || cell === undefined) return '';
    if (cell instanceof Date) return cell.toISOString();
    return String(cell);
  }));
}
```

### Debounce button clicks (prevent double-clicks)
```javascript
let isProcessing = false;
function handleAction(action, param) {
  if (isProcessing) return;
  isProcessing = true;
  google.script.run
    .withSuccessHandler(function(result) {
      updateUI(result);
      isProcessing = false;
    })
    .withFailureHandler(function(err) {
      console.error(err);
      isProcessing = false;
    })
    [action](param);
}
```

### Real-time polling (sync multiple browser tabs)
```javascript
document.addEventListener('DOMContentLoaded', function() {
  google.script.run.withSuccessHandler(updateUI).getState();
  setInterval(function() {
    google.script.run.withSuccessHandler(updateUI).getState();
  }, 2000);  // Poll every 2 seconds
});
```

### State management with CacheService
```javascript
function getState() {
  const cache = CacheService.getScriptCache();
  const state = cache.get('appState');
  if (state) return JSON.parse(state);
  return { phase: 'start', score: 0 };  // default
}

function setState(state) {
  CacheService.getScriptCache().put('appState', JSON.stringify(state), 21600);  // 6 hours
}
```

---

## Drive Operations

### Recursive folder traversal
```javascript
function listAllFiles(folder, results) {
  const files = folder.getFiles();
  while (files.hasNext()) {
    const file = files.next();
    results.push({
      name: file.getName(),
      url: file.getUrl(),
      id: file.getId(),
      type: file.getMimeType(),
      modified: file.getLastUpdated()
    });
  }
  const subfolders = folder.getFolders();
  while (subfolders.hasNext()) {
    listAllFiles(subfolders.next(), results);  // recurse
  }
}
// Usage:
const results = [];
listAllFiles(DriveApp.getFolderById('FOLDER_ID'), results);
```

### Save file to Drive (overwrite if exists)
```javascript
const folder = DriveApp.getFolderById('FOLDER_ID');
const existingFiles = folder.getFilesByName('report.csv');
if (existingFiles.hasNext()) {
  existingFiles.next().setTrashed(true);  // delete old version
}
folder.createFile('report.csv', csvContent, 'text/csv');
```

### Convert Excel to Google Sheets
```javascript
function convertExcelToSheets(excelFileId) {
  const file = DriveApp.getFileById(excelFileId);
  const resource = {
    title: file.getName().replace(/\.xlsx$/i, ''),
    mimeType: 'application/vnd.google-apps.spreadsheet'
  };
  const converted = Drive.Files.insert(resource, file.getBlob());
  return SpreadsheetApp.openById(converted.id);
}
```

---

## Triggers

### Create a daily trigger
```javascript
ScriptApp.newTrigger('myDailyFunction')
  .timeBased()
  .atHour(9)        // 9 AM
  .everyDays(1)
  .create();
```

### Create a minute-based trigger
```javascript
ScriptApp.newTrigger('checkForUpdates')
  .timeBased()
  .everyMinutes(1)
  .create();
```

### Remove old triggers before creating new ones (prevent duplicates)
```javascript
ScriptApp.getProjectTriggers().forEach(function(trigger) {
  if (trigger.getHandlerFunction() === 'myDailyFunction') {
    ScriptApp.deleteTrigger(trigger);
  }
});
```

### Lazy sheet creation
```javascript
function getOrCreateSheet(spreadsheet, name) {
  const existing = spreadsheet.getSheetByName(name);
  return existing || spreadsheet.insertSheet(name);
}
```

---

## API & Caching Patterns

### People API directory lookup
```javascript
function lookupEmail(name) {
  try {
    const result = People.People.searchDirectoryPeople({
      query: name.trim(),
      readMask: 'names,emailAddresses',
      sources: ['DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE']
    });
    if (result.people && result.people.length > 0) {
      return result.people[0].emailAddresses[0].value;
    }
    return null;
  } catch (error) {
    Logger.log('Lookup failed for ' + name + ': ' + error);
    return null;
  }
}
```

### Persistent cache with PropertiesService
```javascript
// Save cache
function saveCache(key, data) {
  PropertiesService.getScriptProperties().setProperty(key, JSON.stringify(data));
}

// Load cache
function loadCache(key) {
  const raw = PropertiesService.getScriptProperties().getProperty(key);
  return raw ? JSON.parse(raw) : {};
}
```

### Chunked storage (for data > 9KB property limit)
```javascript
const CHUNK_SIZE = 8000;  // bytes, under 9KB limit
const jsonStr = JSON.stringify(data);
const chunks = [];
for (let i = 0; i < jsonStr.length; i += CHUNK_SIZE) {
  chunks.push(jsonStr.substring(i, i + CHUNK_SIZE));
}
chunks.forEach(function(chunk, index) {
  PropertiesService.getScriptProperties().setProperty('data_chunk_' + index, chunk);
});
PropertiesService.getScriptProperties().setProperty('data_chunk_count', String(chunks.length));
```

### Rate limiting with sleep
```javascript
for (let i = 0; i < names.length; i++) {
  const email = lookupEmail(names[i]);
  Utilities.sleep(1500);  // 1.5 seconds between API calls

  if ((i + 1) % 50 === 0) {
    Logger.log('Progress: ' + (i + 1) + '/' + names.length);
  }
}
```

### Time budget checking (avoid 6-minute timeout)
```javascript
const MAX_RUNTIME_MS = 5 * 60 * 1000;  // 5 minutes (leave 1 min buffer)
const startTime = Date.now();

for (let i = 0; i < items.length; i++) {
  if (Date.now() - startTime > MAX_RUNTIME_MS) {
    Logger.log('Time limit reached. Processed: ' + i + '/' + items.length);
    break;  // save progress and exit
  }
  // process item
}
```

---

## CSV Parsing

### Parse CSV with quoted fields (handles commas inside quotes)
```javascript
function parseCsv(csvString) {
  const rows = [];
  let currentRow = [];
  let currentField = '';
  let inQuotes = false;

  for (let i = 0; i < csvString.length; i++) {
    const char = csvString[i];
    if (char === '"') {
      if (inQuotes && csvString[i + 1] === '"') {
        currentField += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (!inQuotes && char === ',') {
      currentRow.push(currentField.trim());
      currentField = '';
    } else if (!inQuotes && (char === '\n' || char === '\r')) {
      if (currentField || currentRow.length > 0) {
        currentRow.push(currentField.trim());
        rows.push(currentRow);
        currentRow = [];
        currentField = '';
      }
    } else {
      currentField += char;
    }
  }
  if (currentField || currentRow.length > 0) {
    currentRow.push(currentField.trim());
    rows.push(currentRow);
  }
  return rows;
}
```

---

## Common Utilities

### HTML escaping (prevent XSS)
```javascript
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
```

### Column number to letter (for formula building)
```javascript
function columnToLetter(col) {
  let letter = '';
  while (col > 0) {
    const mod = (col - 1) % 26;
    letter = String.fromCharCode(65 + mod) + letter;
    col = Math.floor((col - 1) / 26);
  }
  return letter;
}
```

### Deduplication with Set
```javascript
const uniqueEmails = [...new Set(allEmails.map(e => e.toLowerCase().trim()))];
```

### Configuration block pattern
```javascript
const CONFIG = {
  SHEET_ID: '1abc123...',
  TAB_NAME: 'Data',
  EMAIL_FROM: 'reports@example.com',
  EMAIL_SUBJECT: 'Daily Report',
  SEARCH_DAYS: 2,
  BATCH_SIZE: 50
};
```

### Error handling with email notification
```javascript
try {
  runSync();
  Logger.log('Success');
} catch (error) {
  Logger.log('Error: ' + error.message);
  Logger.log('Stack: ' + error.stack);
  MailApp.sendEmail({
    to: Session.getActiveUser().getEmail(),
    subject: 'Script Failed',
    body: 'Error at ' + new Date() + '\n\n' + error.message
  });
  throw error;
}
```

### Logging with clear markers
```javascript
Logger.log('Starting sync...');
Logger.log('Step 1: Loading data...');
Logger.log('  Found ' + rows.length + ' rows');
Logger.log('Step 2: Processing...');
Logger.log('  Progress: ' + processed + '/' + total);
Logger.log('Complete! ' + processed + ' rows processed');
```
