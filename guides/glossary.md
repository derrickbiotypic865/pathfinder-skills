# Plain-English Glossary

A no-jargon reference for every technical term you'll encounter in the Pathfinder guides. Bookmark this page — come back whenever you hit a word you don't recognize.

---

## A

**API** — "Application Programming Interface." A way for two programs to talk to each other. Think of it like a drive-through window: you place an order in a specific format, and you get back exactly what you asked for. When you hear "call an API," it means "send a request to another system and get data back."

**Apps Script** — Google's built-in coding tool for automating Google Workspace (Sheets, Gmail, Calendar, Drive, etc.). It uses JavaScript and runs in the cloud — no software to install.

**Argument** — Extra information you give a command. In `claude -p "hello"`, the `"hello"` part is the argument. Think of it as filling in the blank: "Do this to ____."

**Array** — A list of items in code. Like a row in a spreadsheet: `["Apple", "Banana", "Cherry"]`. Each item has a position number starting at 0 (not 1). So "Apple" is at position 0, "Banana" at position 1.

## B

**Bash** — A program that runs text commands on your computer. When Claude Code runs a command, it's using Bash. Named after "Bourne Again SHell" — but you don't need to know that.

**Bookmark** — Saving a link (browser) or message (Slack) so you can find it quickly later. Like putting a sticky note on a page.

**Branch** — A copy of your work where you can try changes without affecting the original. Like making a photocopy before editing — if you mess up, the original is fine. Used in both git (code) and Claude Code (conversations).

## C

**Channel** — (Slack) A named group chat. Like a meeting room dedicated to a specific topic. `#marketing` is for marketing talk, `#project-x` is for that project.

**Checkpoint** — A saved point in your conversation or code that you can return to later. Like a save point in a video game.

**CLASP** — "Command Line Apps Script Projects." A tool that lets you write Google Apps Script code on your computer instead of in the browser. You edit locally and push changes to Google.

**CLI** — "Command Line Interface." Using your computer by typing text commands instead of clicking icons. The text-based way to control your computer.

**Code block** — A section of code displayed in a special formatted box. In markdown, it's surrounded by triple backticks (```). It just means "this is code, not regular text."

**Code editor** — A program for writing code. Like a Word document, but designed for programming. Examples: VS Code, the Apps Script editor, Notepad++.

**Collapse** — Hide something temporarily to reduce clutter. Like folding a section of a newspaper — it's still there, just tucked away. In Slack, you collapse channel groups. In Chrome, you collapse tab groups.

**Commit** — (Git) Saving a snapshot of your code changes. Like clicking "Save" but with a note about what you changed and why. Each commit is a checkpoint you can go back to.

**Comment** — Text in code that the computer ignores — it's there for humans to read. Starts with `//` in JavaScript. Like writing notes in the margins of a textbook.

**Configuration / Config** — Settings that control how a program behaves. A config file is just a file full of settings.

**Console** — (Browser) A hidden panel in your web browser (press F12) that shows errors and messages from web pages. Developers use it for debugging.

**Context** — (Claude Code) Everything Claude "remembers" during your conversation — messages, files read, code written. There's a limited amount of space (the "context window"), like a desk that can only hold so many papers at once.

**CSS** — "Cascading Style Sheets." The code that makes web pages look good — colors, fonts, spacing, layouts. HTML is the structure (walls and doors), CSS is the paint and furniture.

## D

**Dashboard** — A visual display that shows important information at a glance. Like the dashboard in a car — speed, fuel, temperature — but for data.

**Database** — A system for storing and organizing large amounts of data. Like a very powerful, searchable spreadsheet that can hold millions of rows.

**Deploy** — Making your code available for people to use. Like publishing a book — you wrote it, now you're putting it on the shelf for others. Deploying a web app means giving it a URL people can visit.

**Desktop** — The main screen you see when you start your computer. The background with icons on it.

**Diff** — A comparison showing what changed between two versions of a file. Green lines = added, red lines = removed. Like "track changes" in Word.

**Directory** — Another word for "folder." A place on your computer that holds files and other folders.

**Do Not Disturb** — A mode that pauses all notifications. You still receive messages — they just wait silently until you're ready.

**DOM** — "Document Object Model." The behind-the-scenes structure of a web page. You don't need to understand this deeply — just know it's how browsers organize page content.

**Downloads folder** — The default folder where your computer saves files when you download them from the internet.

## E

**Environment variable** — A setting stored at the system level that programs can read. Like a sticky note on your computer that says `API_KEY=abc123`. Programs check it instead of having the value hardcoded.

**Exit code** — A number a program returns when it finishes. 0 means "everything worked." Any other number means "something went wrong." You don't see these — they happen behind the scenes.

**Extension** — (File) The letters after the dot in a filename: `.docx`, `.pdf`, `.xlsx`, `.py`. Tells the computer what type of file it is and what program should open it. (Browser) An add-on that gives your browser new features.

## F

**Favicon** — The tiny icon that appears in a browser tab next to the page title. Like a logo for a website.

**File Explorer** — (Windows) The app you use to browse files and folders. The folder icon on your taskbar.

**File path** — The address of a file on your computer. Like a street address: `C:\Users\Documents\report.docx` tells the computer exactly where to find the file. The slashes separate folder names.

**Filter** — Narrowing down a list to show only items that match specific criteria. Like sorting through a deck of cards and pulling out only the hearts.

**Finder** — (Mac) The app you use to browse files and folders. The smiley face icon in your Dock.

**Flag** — An option you add to a command to change how it behaves. In `claude -p "hello"`, the `-p` is a flag. Think of it as a switch you flip when starting a command.

**Fork** — Making a copy of something so you can modify the copy without changing the original. Used in git (copy a repo), Claude Code (copy a conversation), and GitHub (copy someone's project).

**Function** — A reusable block of code that does one specific thing. Like a recipe — you define it once, then "call" it whenever you need that thing done. `showMessage()` is a function call.

## G

**Git** — A tool that tracks every change to your code over time. Like version history in Google Docs, but much more powerful. You can see who changed what, when, and go back to any previous version.

**GitHub** — A website where people store and share code using git. Like Google Drive but for code. Projects stored on GitHub are called "repositories" (repos).

**GitLab** — Similar to GitHub — a website for storing and sharing code. Some companies run their own private GitLab internally.

**Glob pattern** — A way to match multiple files using wildcards. `*.txt` means "all text files." `**/*.py` means "all Python files in any subfolder." The `*` is like a wildcard card in a card game.

## H

**Hidden files** — Files that don't show up in your file manager by default. On Mac/Linux, any file starting with a dot (`.config`, `.env`) is hidden. They're usually settings or system files that most people don't need to see.

**Hook** — (Claude Code) An automated action that triggers when something happens. Like a doorbell — when someone presses it (the event), the bell rings (the action). "When Claude edits a file, run the linter" is a hook.

**HTML** — "HyperText Markup Language." The code that creates the structure of web pages. It defines what's on the page: headings, paragraphs, images, links, tables. Think of it as the skeleton of a web page.

**HTTP** — "HyperText Transfer Protocol." The language your browser uses to request web pages from servers. When you type a URL, your browser sends an HTTP request. You don't need to think about this — it just works.

**Huddle** — (Slack) A lightweight audio call that happens right inside a Slack channel. Like tapping someone on the shoulder for a quick conversation.

## I

**Incognito / Private browsing** — A browser mode that doesn't save your history, cookies, or login sessions. When you close the window, it's like you were never there.

## J

**JavaScript** — A programming language used in web pages, Apps Script, and many other places. When you write Apps Script code, you're writing JavaScript.

**JSON** — "JavaScript Object Notation." A way to organize data that computers (and humans) can read. Looks like: `{"name": "Ben", "role": "builder"}`. Curly braces hold the data, colons separate names from values, commas separate items.

## K

**Keyboard shortcut** — A key combination that does something faster than clicking. Like `Ctrl+C` for copy or `Ctrl+Z` for undo. Saves time by skipping menus and mouse clicks.

## L

**Linter / Linting** — A tool that checks your code for common mistakes, style issues, and potential bugs. Like spell-check but for code. "Running the linter" means "checking the code for problems."

**Localhost** — Your own computer acting as a web server. When a URL says `localhost:3000`, it means "this web page is running on MY computer, port 3000." Only you can see it.

## M

**Markdown** — A simple way to format text using plain characters. `**bold**` makes bold, `# Heading` makes a heading, `- item` makes a bullet list. Files ending in `.md` are Markdown files. This glossary is written in Markdown.

**MCP** — "Model Context Protocol." A way to plug external tools into Claude Code — databases, APIs, file systems. Think of it as giving Claude new superpowers by connecting it to other services.

**Mention** — (Slack) Using `@someone` to specifically notify that person. They get a notification even if the channel is muted.

**Model** — (AI) The AI brain that processes your requests. Different models have different speeds and capabilities. Opus = smartest but slower, Sonnet = good balance, Haiku = fastest but simpler.

**Mute** — (Slack/notifications) Turn off alerts for something without leaving or deleting it. Like putting your phone on silent — messages still arrive, they just don't buzz.

## N

**Node.js** — A program that lets you run JavaScript on your computer (not just in a browser). Required for tools like CLASP and many developer tools.

**npm** — "Node Package Manager." A tool for downloading and installing JavaScript packages (pre-built code libraries). `npm install` downloads what you need.

**npx** — Like npm, but runs a package without permanently installing it. Think of it as "try this tool once" instead of "install this tool forever."

## P

**Package** — A bundle of pre-written code that does something useful. Like an app you install, but for code. Installed with npm.

**Path** — See "File path."

**Pin** — (Slack/Chrome) Mark something as important so it stays visible and easy to find. Like pinning a note to a bulletin board.

**Piping (`|`)** — Sending the output of one command into another. Like an assembly line: Step 1 produces something, the pipe (`|`) passes it to Step 2. Example: `cat file.txt | claude -p "summarize"` reads the file then sends its contents to Claude.

**Plugin** — (Claude Code) A pre-packaged extension you install with one command. Adds new skills and capabilities. Like installing an app on your phone.

**Port** — A numbered channel on your computer for network communication. Think of it like apartment numbers in a building — the building is your computer, port 3000 is apartment 3000.

**Print mode (`-p`)** — A Claude Code mode where you ask one question, get one answer, and exit. Like sending a text message instead of having a phone call.

**Prompt** — The text you type to ask Claude something. Your question or instruction.

**Push** — (Git) Sending your code changes to a remote server (like GitHub). Like uploading a file to Google Drive.

## Q

**Query** — A search or question. When you search in Slack or a database, you're running a query.

**Quick Access** — (Windows) A section in File Explorer's sidebar that shows your pinned and recent folders. One-click access to places you go often.

## R

**Rate limit** — A restriction on how many times you can do something in a given time period. Like "you can only make 100 API calls per minute." If you hit the limit, you have to wait.

**Recycle Bin** — (Windows) Where deleted files go before they're permanently removed. Like a trash can — you can pull things back out until you empty it.

**Regex** — "Regular Expression." A pattern-matching language for searching text. `\d+` means "one or more digits." It's powerful but complex — you don't need to learn it right away.

**Repo / Repository** — A project folder tracked by git. Contains all the files and the history of every change. Usually hosted on GitHub or GitLab.

**Resume** — (Claude Code) Pick up a previous conversation where you left off, with all context intact.

## S

**Scope** — Where something applies. "Project scope" means "only in this project." "User scope" means "everywhere you work." Like the difference between a rule for one classroom vs. a rule for the whole school.

**Script** — A file containing code that runs automatically when executed. Like a recipe the computer follows step by step.

**Search modifier** — A special keyword in a search that narrows results. In Slack: `from:@alice` finds messages from Alice. `has:link` finds messages with URLs.

**Session** — A conversation with Claude Code. Has history, context, and can be resumed. Like a chat thread.

**Settings** — Options that control how a program behaves. Preferences you configure.

**Sidebar** — The panel on the left side of an app (Slack, File Explorer, Finder) showing navigation options.

**Skill** — (Claude Code) A `.md` file that teaches Claude a new behavior or workflow. Creates a `/slash-command` you can invoke.

**Slash command** — A command that starts with `/` in Claude Code or Slack. Type `/help` to see available commands.

**Sort** — Arrange items in order — alphabetically, by date, by size, etc.

**Spotlight** — (Mac) The system-wide search. Press `Cmd+Space` and type to find anything on your Mac.

**Stdin** — "Standard input." The channel where a program receives data. When you pipe something, it arrives via stdin. Think of it as "the inbox."

**Stdout** — "Standard output." The channel where a program sends its results. Usually your screen. Think of it as "the outbox."

**String** — Text in code. `"Hello world"` is a string. It's wrapped in quotes to tell the computer "this is text, not a command."

## T

**Tab** — (Browser) An open page in your web browser. Each tab is a separate page you can switch between.

**Tab group** — (Chrome) A way to bundle related tabs together with a color and label. Like putting papers in colored folders.

**Terminal** — The app where you type commands. On Windows: Git Bash, PowerShell, or Command Prompt. On Mac: Terminal. On Linux: Terminal or Konsole.

**Thread** — (Slack) A side conversation attached to a specific message. Keeps responses organized under the original message instead of cluttering the main channel.

**Token** — (AI) A unit of text that AI models process. Roughly 3-4 characters or about 3/4 of a word. Context windows are measured in tokens. You don't need to count them — Claude handles this.

**Trash** — (Mac/Linux) Where deleted files go. Same concept as Windows' Recycle Bin.

**Trigger** — (Apps Script) An automatic schedule that runs your code without you clicking "Run." Like setting an alarm: "Run this function every morning at 8 AM."

## U

**Undo** — Reverse your last action. `Ctrl+Z` on Windows/Linux, `Cmd+Z` on Mac. Works almost everywhere — file managers, text editors, web browsers.

**URL** — "Uniform Resource Locator." A web address. `https://google.com` is a URL. When you deploy a web app, it gets a URL people can visit.

## V

**Variable** — A named container that holds a value. Like a labeled box: `teamName = "Alpha"` creates a box labeled "teamName" with "Alpha" inside. You can use the label later to get the value.

**Version control** — Tracking every change to your files over time, with the ability to go back to any previous version. Git is the most common version control tool. Like having infinite undo and a detailed history of every change.

## W

**Web app** — A program that runs in your web browser. You visit a URL and the app loads — no installing anything. Google Sheets, Gmail, and Slack in a browser are all web apps.

**Webhook** — An automatic message sent from one system to another when something happens. Like a doorbell for apps: "When someone submits a form, send a message to Slack."

**Wildcard (`*`)** — A symbol that matches "anything." In `*.txt`, the `*` means "any filename" — so it matches `report.txt`, `notes.txt`, everything ending in `.txt`. `**` means "anything in any subfolder."

**Workspace** — (Slack) Your company's Slack environment. Contains all the channels, people, and messages for your organization.

## Y

**YAML** — "YAML Ain't Markup Language." A data format like JSON but more readable. Uses indentation instead of braces. Used in configuration files. You'll see it in SKILL.md frontmatter between `---` markers.

**YYYY-MM-DD** — A date format: Year-Month-Day. `2026-03-23` means March 23, 2026. Used because it sorts correctly in alphabetical order — files named this way automatically line up in date order.
