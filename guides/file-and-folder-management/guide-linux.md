# Get Your Files Under Control — Linux Edition

> New to technical terms? See the [Plain-English Glossary](../glossary.md) for jargon-free definitions.

## The Problem

Your Desktop has 87 files on it. Your Downloads folder is a graveyard of things you opened once. You saved that important document somewhere, but you can't remember where. You have three copies of "Final Report" and none of them are actually final. Sound familiar?

This guide gives you a simple system to organize your files so you can find anything in seconds. No extra apps to install — just the features already built into your Linux desktop.

## What You'll Learn

1. How to find any file instantly (without digging through folders)
2. A simple folder structure that actually works
3. Naming files so you can find them later
4. Keyboard shortcuts that save time every day
5. Cleaning up the mess you already have
6. Habits to keep things organized going forward

## Time Needed

About 30-40 minutes. You'll do some actual organizing as you go, so your files will be cleaner by the time you're done.

---

## Part 1: Find Any File Instantly

Before we organize anything, let's learn how to find files fast. Even if your files are a mess right now, these tricks work.

### Desktop Search (the fastest way)

**GNOME (Ubuntu, Fedora Workstation):**
1. Press the **Super key** (the key with the logo between Ctrl and Alt)
2. Start typing the name of a file
3. Results appear — files, folders, apps
4. Click the one you want

**KDE (Kubuntu, Fedora KDE):**
1. Press **Alt+F2** or click the search icon in the taskbar
2. Start typing the name of a file
3. Results appear instantly

That's it. You don't need to know WHERE a file is. Just press the Super key and type.

### File Manager Search

For searching within a specific folder:
1. Open your file manager (**Files** on GNOME, **Dolphin** on KDE)
2. Navigate to the folder you want to search
3. Press **Ctrl+F** to open the search bar
4. Type your search — it searches that folder and everything inside it

### Terminal Search (for power users)

If you want to get comfortable with the terminal, these are useful:
- `find ~/Documents -name "*budget*"` — search for files with "budget" in the name
- `locate budget` — instant search across the whole system (may need to run `sudo updatedb` first)
- `grep -r "compliance" ~/Documents/` — search for the word "compliance" inside files

Don't worry if the terminal feels intimidating — the file manager search does the same thing. The terminal is just faster once you're used to it.

### Recent Files

Can't remember the name but you know you opened it recently?
1. Open your file manager
2. Look for **Recent** in the left sidebar
3. Recently opened files appear sorted by date

---

## Part 2: A Simple Folder Structure That Works

The goal isn't to create the perfect system. It's to create a system that's good enough that you can find things without thinking.

### The Starter Structure

Open your file manager and go to your **Home** folder. Inside Documents (or your Home folder if you prefer), create these folders:

```
Documents/
├── Work/
│   ├── Projects/
│   ├── Reports/
│   ├── Meetings/
│   └── Templates/
├── Personal/
│   ├── Finance/
│   ├── Medical/
│   └── Important/
├── Learning/
│   └── (courses, notes, guides)
└── Archive/
    └── (old stuff you might need someday)
```

**How to create a folder:**
- In your file manager: right-click in an empty space > **New Folder**
- Or press **Ctrl+Shift+N** to create a new folder instantly
- Or in the terminal: `mkdir -p ~/Documents/Work/Projects`

**Try it now:** Create the top-level folders (Work, Personal, Learning, Archive). You can add subfolders as needed over time.

### The Rules

**Rule 1: Everything gets a home.**
Every file goes in a folder. Nothing lives loose in Documents or on the Desktop. If you don't know where something goes, put it in the most relevant top-level folder and move on.

**Rule 2: Go wide, not deep.**
Don't create folders inside folders inside folders. Three levels deep is the max:
- Good: `Documents/Work/Projects/Dashboard-Q3`
- Too deep: `Documents/Work/2026/Q3/Projects/Active/Dashboard/Version2`

**Rule 3: When in doubt, search.**
You don't need a perfect structure. You need a good-enough structure plus search. If something is in any of your organized folders, search will find it.

**Rule 4: The Desktop is not a filing cabinet.**
The Desktop is a workspace — a place for things you're actively using RIGHT NOW. When you're done with something, move it to its folder. Aim for fewer than 10 items on your Desktop.

---

## Part 3: Naming Files So You Can Find Them

A file named "Document1.docx" is useless. A file named "Q3-Budget-Proposal-2026.docx" tells you exactly what it is without opening it.

### The Simple Formula

**[What it is]-[Detail]-[Date or Version]**

Examples:
- `Meeting-Notes-Team-Standup-2026-03-22.docx`
- `Budget-Proposal-Q3-2026.xlsx`
- `Project-Plan-Dashboard-v2.pptx`
- `Invoice-Vendor-ABC-March-2026.pdf`

### Naming Rules

**Use dashes or underscores, not spaces.**
- Good: `Budget-Report-Q3.xlsx` or `Budget_Report_Q3.xlsx`
- Avoid: `Budget Report Q3.xlsx`
- Why: Spaces cause problems in the terminal and with many tools. Dashes and underscores always work everywhere. This matters more on Linux than other systems.

**Put dates in YYYY-MM-DD format.**
- Good: `Notes-2026-03-22.docx`
- Bad: `Notes-3-22-26.docx` or `Notes-March-22.docx`
- Why: YYYY-MM-DD sorts correctly in alphabetical order. Files automatically line up in date order. This also matches the `date +%F` format in the terminal.

**Be specific, not clever.**
- Good: `Q3-Sales-Report-2026.xlsx`
- Bad: `FINAL-report-v3-REAL-final-USE-THIS.xlsx`
- Why: Your future self won't remember what "USE THIS" means.

**Never use "Final" in a filename.**
- Instead, use version numbers: `Proposal-v1.docx`, `Proposal-v2.docx`
- Or dates: `Proposal-2026-03-20.docx`, `Proposal-2026-03-22.docx`
- The word "Final" is a lie. There's always one more revision.

---

## Part 4: Essential Keyboard Shortcuts

These work in most Linux file managers (Nautilus/Files, Dolphin, Thunar, Nemo). Pick 2-3 to start using today.

### File Manager Shortcuts

| Shortcut | What it does |
|:---------|:-------------|
| `Ctrl+N` | **Open a new file manager window** |
| `Ctrl+Shift+N` | **Create a new folder** |
| `Ctrl+C` | Copy selected files |
| `Ctrl+X` | Cut selected files (move them) |
| `Ctrl+V` | Paste files |
| `Ctrl+Z` | **Undo** (works in most file managers) |
| `Ctrl+A` | Select all files in the current folder |
| `F2` | **Rename** the selected file |
| `Delete` | Move to Trash |
| `Shift+Delete` | Permanently delete (skip Trash — use with caution) |
| `Alt+Up Arrow` | Go up one folder level |
| `Ctrl+F` | Search in the current folder |
| `Ctrl+L` | **Edit the path bar** (type a folder path directly — very useful) |
| `Ctrl+H` | **Show/hide hidden files** (files and folders starting with a dot) |

### The Big Three (start with these)

| Shortcut | What it does |
|:---------|:-------------|
| `Super key` then type | Find any file, app, or setting instantly |
| `Ctrl+Shift+N` | Create a new folder |
| `Ctrl+Z` | Undo your last action (the universal panic button) |

**Try this now:** Open your file manager. Press `Ctrl+Shift+N` to create a folder. Type "Test" and press Enter. Press `Ctrl+Z` — the folder disappears. That's undo.

### Linux-Specific Tips

**Hidden files:** On Linux, any file or folder starting with a dot (like `.config`, `.bashrc`, `.ssh`) is hidden by default. Press `Ctrl+H` in your file manager to toggle hidden files visible. This is useful when you need to find configuration files.

**Path bar:** Press `Ctrl+L` to type a path directly. Instead of clicking through five folders, just type `~/Documents/Work/Projects` and press Enter. Much faster.

**Open a terminal here:** In most file managers, right-click in a folder and choose "Open Terminal Here" to drop into a terminal already in that directory.

### Selecting Multiple Files

- **Click one file, then Shift+Click another** — selects everything between them
- **Hold Ctrl and click individual files** — selects specific files (skip ones in between)
- **Ctrl+A** — selects everything in the folder

**Try it now:** Open your Downloads folder. Hold Ctrl and click 3 files scattered around. Now press Delete. You just deleted exactly the files you wanted.

---

## Part 5: Clean Up the Mess You Already Have

You probably have files everywhere — Desktop, Downloads, home folder, random directories. Here's a realistic plan to clean up without spending your whole day on it.

### Phase 1: The Desktop (10 minutes)

1. Look at everything on your Desktop
2. For each item, ask:
   - **Am I using this right now?** → Leave it for now
   - **Is this important but I'm done with it?** → Move it to the right folder in Documents
   - **I have no idea what this is** → Open it, decide if you need it, delete or file it
3. Goal: Get down to 10 or fewer items on the Desktop

**Quick move trick:** Select files, press `Ctrl+X` (cut), navigate to the destination folder, press `Ctrl+V` (paste). Done.

### Phase 2: The Downloads Folder (10 minutes)

The Downloads folder is where files go to be forgotten. Let's fix that.

1. Open your Downloads folder
2. Click the **Date modified** column header to sort by newest first
3. **Last 7 days:** Keep what you need, move important files to Documents folders
4. **Last 30 days:** Anything you haven't touched in a month probably isn't urgent — scan and delete what you don't need
5. **Older than 30 days:** Be ruthless. If you haven't needed it in a month, you probably won't. Delete it. If it was important, you can re-download it.

**Terminal power move:** To see your largest files in Downloads, open a terminal and run:
```bash
ls -lhS ~/Downloads | head -20
```
This shows the 20 biggest files. Often the biggest ones are old installers or archives you don't need anymore.

### Phase 3: Duplicates and Old Versions (5 minutes)

Search for common duplicate patterns:
1. Open your file manager, go to Documents
2. Search for `copy` — find files with "Copy" in the name, delete the duplicates
3. Search for `final` — find all the "Final" and "FINAL FINAL" versions, keep the newest, delete the rest
4. Search for `(1)` or `(2)` — auto-renamed duplicates from downloading the same file twice

### Don't Try to Do Everything at Once

This cleanup doesn't have to happen in one sitting. Spend 10 minutes today, 10 minutes tomorrow. The goal is progress, not perfection.

---

## Part 6: Habits to Keep Things Organized

The cleanup only matters if you maintain it. These small habits take seconds and prevent the mess from coming back.

### The 2-Minute Rule

When you save or download a file, take 2 seconds to:
1. Give it a clear name (not "Untitled" or "Document1")
2. Save it in the right folder (not the Desktop or Downloads)

It's faster to file it correctly now than to find it later in a pile.

### The Friday Sweep (5 minutes)

Every Friday (or whenever works for you):
1. Clear your Desktop — move or delete everything you're not actively using
2. Empty your Downloads folder — file the keepers, delete the rest
3. Empty your Trash (open Trash in the file manager > click **Empty Trash**, or right-click the Trash icon)

Five minutes once a week keeps things permanently clean.

### Save-As Smarter

When saving a file for the first time:
1. **Don't just click Save** — click **Save As** (or File > Save As)
2. Navigate to the right folder FIRST
3. Type a clear name BEFORE saving
4. Then click Save

This takes 5 extra seconds and saves you 5 minutes of searching later.

### Bookmark Your Important Folders

You can bookmark frequently-used folders for one-click access:

1. Open your file manager
2. Navigate to a folder you use often
3. Drag it to the sidebar, or right-click > **Add to Bookmarks** (GNOME) or **Add to Places** (KDE)

Now it's always visible in the left sidebar — no navigating required.

**Try it now:** Bookmark your `Documents/Work` folder so it's always one click away.

---

## Quick Reference Card

### Finding Files

| What you want | How to do it |
|:-------------|:-------------|
| Find any file by name | Press `Super key`, start typing |
| Search inside a folder | `Ctrl+F` in file manager |
| See recent files | File manager sidebar > Recent |
| Search by content (terminal) | `grep -r "search term" ~/Documents/` |
| Search by name (terminal) | `find ~/Documents -name "*keyword*"` |

### Managing Files

| What you want | How to do it |
|:-------------|:-------------|
| Create a new folder | `Ctrl+Shift+N` |
| Rename a file | Select it, press `F2` |
| Undo a mistake | `Ctrl+Z` |
| Move files | `Ctrl+X` then `Ctrl+V` in destination |
| Copy files | `Ctrl+C` then `Ctrl+V` in destination |
| Select multiple files | Hold `Ctrl` and click each one |
| Select a range of files | Click first, `Shift+Click` last |
| Show hidden files | `Ctrl+H` |
| Type a path directly | `Ctrl+L` |

### The System

| Habit | When |
|:------|:-----|
| Name files clearly | Every time you save |
| Save to the right folder | Every time you save |
| Clear your Desktop | When it gets crowded |
| Clean Downloads | Weekly |
| Empty Trash | Weekly |

### Naming Formula

`[What]-[Detail]-[Date or Version]`

- Use dashes, not spaces (especially important on Linux)
- Dates in YYYY-MM-DD format
- Never use "Final" — use version numbers instead

---

## You're Done!

You now have a system for keeping your files organized. The key isn't the perfect folder structure — it's the habits. Name files clearly when you save them, put them in the right place, and do a quick cleanup once a week. That's it.

Start with the Big Three shortcuts (`Super key` to search, `Ctrl+Shift+N` for new folders, `Ctrl+Z` to undo) and the 2-minute rule (name it and file it when you save). Everything else can come over time.

Your future self — the one who needs to find that important document at 4:59 PM on a Friday — will thank you.
