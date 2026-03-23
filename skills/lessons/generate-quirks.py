#!/usr/bin/env python3
"""
Quirk Extractor — reads lessons/*.md, extracts technical patterns,
writes organized quirk files to quirks/.

Usage:
    python3 generate-quirks.py

    Run from your lessons directory, or place this script alongside your
    lessons/ folder. It will:
      1. Scan all .md files in lessons/ for QUIRK markers (structured extraction)
      2. Fall back to heuristic extraction from lesson structure if no markers found
      3. Group quirks by technology tag
      4. Write quirks/<tag>.md files and a quirks/_index.md summary

    To automate: set up a Claude Code PostToolUse hook on Write|Edit
    that runs this script whenever a lesson file is saved.

Extraction modes:
  1. Primary: Structured HTML comment markers (<!-- QUIRK: ... -->)
  2. Fallback: Heuristic extraction from "What Broke", "The Problem", etc.

Output: quirks/<tag>.md files + quirks/_index.md
"""

import os
import re
from pathlib import Path
from datetime import datetime

LESSONS_DIR = Path(__file__).parent / "lessons"
QUIRKS_DIR = Path(__file__).parent / "quirks"

# Tag detection — maps keywords found in lesson content to tag names
TAG_KEYWORDS = {
    "google-apps-script": [
        "apps script", "appsscript", ".gs", "clasp", "ScriptApp",
        "DriveApp", "DocumentApp", "SpreadsheetApp", "SlidesApp",
        "HtmlService", "PropertiesService", "UrlFetchApp", "google.script.run",
        "CardService", "Card Service", "workspace add-on", "workspace addon",
        "editor add-on"
    ],
    "google-card-service": [
        "CardService", "Card Service", "DecoratedText", "TextParagraph",
        "SelectionInput", "GridItem", "newGrid", "newCardBuilder",
        "setCollapsible", "setWrapText", "ActionResponse", "newNavigation",
        "setNotification"
    ],
    "google-drive-api": [
        "Drive API", "Drive.Files", "DriveApp", "drive.file", "drive.labels",
        "DriveLabels", "modifyLabels", "listLabels", "Drive Labels",
        "file properties", "document properties", "getFileById"
    ],
    "google-docs-api": [
        "Docs API", "Docs.Documents", "DocumentApp", "createHeader",
        "createFooter", "batchUpdate", "openById", "saveAndClose"
    ],
    "openshift": [
        "openshift", "oc ", "oc create", "oc port-forward", "kubernetes",
        "pod", "configmap", "namespace", "sandbox",
        "DeploymentConfig", "CronJob", "route"
    ],
    "python": [
        "python", "pip install", "urllib", "requests", "httpx",
        "ssl", "certifi", "json.loads", "venv"
    ],
    "rust-tauri": [
        "rust", "cargo", "tauri", "rustup", "MSVC", "MinGW",
        "toolchain", "link.exe", "kernel32", "windows-gnu", "windows-msvc"
    ],
    "llm-tool-calling": [
        "tool_calls", "tool calling", "granite", "qwen", "llama",
        "vLLM", "chat/completions", "function calling",
        "openai", "LLM"
    ],
    "node-express": [
        "express", "node", "npm", "middleware", "cors",
        "router", "app.use", "req", "res"
    ],
    "pii-detection": [
        "PII", "regex", "proximity", "false positive", "negative context",
        "context keywords", "sensitive data", "GDPR", "SSN"
    ]
}


def detect_tags(content: str) -> list[str]:
    """Detect technology tags from content keywords."""
    content_lower = content.lower()
    tags = []
    for tag, keywords in TAG_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in content_lower:
                tags.append(tag)
                break
    return tags or ["general"]


def strip_markdown(text: str) -> str:
    """Strip markdown formatting from text."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)  # italic
    text = re.sub(r'`(.+?)`', r'\1', text)  # inline code
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # images
    text = re.sub(r'\[(.+?)\]\(.*?\)', r'\1', text)  # links
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)  # headings
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)  # code blocks
    return text.strip()


def truncate_clean(text: str, max_len: int = 200) -> str:
    """Truncate text at max_len without cutting mid-word."""
    text = text.strip()
    if len(text) <= max_len:
        return text
    truncated = text[:max_len]
    last_space = truncated.rfind(' ')
    if last_space > max_len * 0.6:
        truncated = truncated[:last_space]
    return truncated.rstrip('.,;:- ')


def extract_structured_quirks(filepath: Path) -> list[dict]:
    """Extract quirks from <!-- QUIRK: ... --> HTML comment markers."""
    content = filepath.read_text(encoding="utf-8")
    quirks = []

    # Find all QUIRK marker blocks
    # Each block starts with <!-- QUIRK: title --> and contains WHEN, WRONG, RIGHT, WHY, TAGS
    pattern = re.compile(
        r'<!-- QUIRK:\s*(.+?)\s*-->\s*\n'
        r'(?:<!-- WHEN:\s*(.+?)\s*-->\s*\n)?'
        r'(?:<!-- WRONG:\s*(.+?)\s*-->\s*\n)?'
        r'(?:<!-- RIGHT:\s*(.+?)\s*-->\s*\n)?'
        r'(?:<!-- WHY:\s*(.+?)\s*-->\s*\n)?'
        r'(?:<!-- TAGS:\s*(.+?)\s*-->)?',
        re.MULTILINE
    )

    for match in pattern.finditer(content):
        title = match.group(1).strip()
        when = (match.group(2) or "").strip()
        wrong = (match.group(3) or "").strip()
        right = (match.group(4) or "").strip()
        why = (match.group(5) or "").strip()
        tags_str = (match.group(6) or "").strip()

        tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []

        quirks.append({
            "title": title,
            "when": when,
            "wrong": wrong,
            "right": right,
            "why": why,
            "tags": tags,
            "source": filepath.name,
            "structured": True
        })

    return quirks


def extract_heuristic_quirks(filepath: Path) -> list[dict]:
    """Fallback: extract quirks heuristically from lesson structure."""
    content = filepath.read_text(encoding="utf-8")
    tags = detect_tags(content)
    title = ""
    quirks = []

    # Get title from first heading
    title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()

    # Strategy 1: Extract from "What Broke" numbered sections
    broke_sections = re.findall(
        r"###\s+\d+\.\s+(.+?)\n"
        r"(?:\*\*What happened:\*\*\s*(.+?)\n)?"
        r"(?:\*\*Root cause:\*\*\s*(.+?)\n)?"
        r"(?:\*\*Fix:\*\*\s*(.+?)\n)?"
        r"(?:\*\*Lesson:\*\*\s*(.+?)(?:\n|$))?",
        content, re.DOTALL
    )
    for match in broke_sections:
        q_title, what, cause, fix, lesson = [s.strip() if s else "" for s in match]
        if q_title and (cause or fix or lesson):
            when_text = strip_markdown(what) if what else ""
            wrong_text = strip_markdown(cause) if cause and cause != what else ""
            right_text = strip_markdown(fix) if fix else ""
            why_text = strip_markdown(lesson) if lesson and lesson != cause else ""

            quirks.append({
                "title": strip_markdown(q_title),
                "when": truncate_clean(when_text),
                "wrong": truncate_clean(wrong_text),
                "right": truncate_clean(right_text),
                "why": truncate_clean(why_text),
                "tags": tags,
                "source": filepath.name,
                "structured": False
            })

    # Strategy 2: Extract from "## The Problem" / "## The Fix" pattern
    problem_match = re.search(r"##\s+The Problem\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    fix_match = re.search(r"##\s+(?:The Fix|The Workaround).*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL)

    if problem_match and fix_match and not broke_sections:
        problem_text = problem_match.group(1).strip()
        fix_text = fix_match.group(1).strip()

        # Extract code blocks for wrong/right
        wrong_code = ""
        right_code = ""
        wrong_blocks = re.findall(r"```.*?\n(.*?)```", problem_text, re.DOTALL)
        right_blocks = re.findall(r"```.*?\n(.*?)```", fix_text, re.DOTALL)
        if wrong_blocks:
            wrong_code = wrong_blocks[0].strip()
        if right_blocks:
            right_code = right_blocks[0].strip()

        # Clean problem text
        problem_clean = re.sub(r"```.*?```", "", problem_text, flags=re.DOTALL).strip()
        problem_clean = strip_markdown(problem_clean)
        problem_clean = truncate_clean(problem_clean)

        fix_clean = re.sub(r"```.*?```", "", fix_text, flags=re.DOTALL).strip()
        fix_clean = strip_markdown(fix_clean)
        fix_clean = truncate_clean(fix_clean)

        quirks.append({
            "title": strip_markdown(title),
            "when": problem_clean,
            "wrong": wrong_code or problem_clean,
            "right": right_code or fix_clean,
            "why": problem_clean if not wrong_code else "",
            "tags": tags,
            "source": filepath.name,
            "structured": False
        })

    # Strategy 3: Extract from tables with "Limitation | Impact" pattern
    table_rows = re.findall(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|", content)
    for row_key, row_val in table_rows:
        key = row_key.strip()
        if key.lower() in ("limitation", "---", "format", "field", "#", "metric", "feature"):
            continue
        if "|" in key:
            continue
        if any(word in row_val.lower() for word in ["fail", "can't", "don't", "error", "need", "must", "won't", "no "]):
            quirks.append({
                "title": strip_markdown(key),
                "when": "Working with " + ", ".join(tags),
                "wrong": "",
                "right": strip_markdown(truncate_clean(row_val.strip())),
                "why": "",
                "tags": tags,
                "source": filepath.name,
                "structured": False
            })

    # Strategy 4: Look for "## Other" sections with bullet quirks
    other_match = re.search(r"##\s+(?:Other|Common Causes).*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if other_match and not broke_sections:
        other_text = other_match.group(1).strip()
        bullets = re.findall(r"[-*]\s+\*\*(.+?)\*\*\s*[---]\s*(.+?)(?:\n|$)", other_text)
        for b_title, b_desc in bullets:
            quirks.append({
                "title": strip_markdown(b_title.strip()),
                "when": "Working with " + ", ".join(tags),
                "wrong": "",
                "right": strip_markdown(truncate_clean(b_desc.strip())),
                "why": "",
                "tags": tags,
                "source": filepath.name,
                "structured": False
            })

    return quirks


def extract_quirks_from_lesson(filepath: Path) -> list[dict]:
    """Extract quirks from a lesson file. Prefers structured markers, falls back to heuristic."""
    structured = extract_structured_quirks(filepath)
    if structured:
        return structured
    return extract_heuristic_quirks(filepath)


def format_quirk(q: dict) -> str:
    """Format a single quirk as markdown."""
    lines = [f"### {q['title']}"]
    if q.get("when"):
        lines.append(f"**When:** {q['when']}")
    if q.get("wrong"):
        wrong = q["wrong"]
        if '`' not in wrong and any(c in wrong for c in '(){}=.'):
            wrong = f"`{wrong}`"
        lines.append(f"**Wrong:** {wrong}")
    if q.get("right"):
        right = q["right"]
        if '`' not in right and any(c in right for c in '(){}=.'):
            right = f"`{right}`"
        lines.append(f"**Right:** {right}")
    if q.get("why"):
        lines.append(f"**Why:** {q['why']}")
    lines.append(f"*Source: {q.get('source', 'unknown')}*")
    lines.append("")
    return "\n".join(lines)


def write_quirk_files(all_quirks: list[dict], lesson_files: list[Path]):
    """Group quirks by tag and write to quirks/<tag>.md files."""
    QUIRKS_DIR.mkdir(exist_ok=True)

    # Group by tag
    tag_groups: dict[str, list[dict]] = {}
    for q in all_quirks:
        for tag in q["tags"]:
            if tag not in tag_groups:
                tag_groups[tag] = []
            tag_groups[tag].append(q)

    # Write per-tag files
    tag_files = {}
    for tag, quirks in sorted(tag_groups.items()):
        # Deduplicate by title
        seen = set()
        unique = []
        for q in quirks:
            if q["title"] not in seen:
                seen.add(q["title"])
                unique.append(q)

        triggers = TAG_KEYWORDS.get(tag, [tag])
        filename = f"{tag}.md"
        filepath = QUIRKS_DIR / filename

        lines = [
            f"# {tag.replace('-', ' ').title()} -- Technical Quirks",
            f"",
            f"triggers: [{', '.join(triggers[:10])}]",
            f"updated: {datetime.now().strftime('%Y-%m-%d')}",
            f"count: {len(unique)}",
            f"",
            f"---",
            f"",
        ]

        for q in unique:
            lines.append(format_quirk(q))

        filepath.write_text("\n".join(lines), encoding="utf-8")
        tag_files[tag] = {"file": filename, "count": len(unique), "triggers": triggers[:10]}
        print(f"  Wrote {filename} ({len(unique)} quirks)")

    # Write index
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    total_unique = len({q["title"] for q in all_quirks})

    # Gather lesson file info
    lesson_info = []
    for lf in sorted(lesson_files):
        mtime = datetime.fromtimestamp(lf.stat().st_mtime).strftime('%Y-%m-%d')
        lesson_info.append((lf.name, mtime))

    index_lines = [
        "# Quirks Index",
        "",
        f"Auto-generated: {now}",
        f"Total quirks: {total_unique}",
        f"Total tag files: {len(tag_files)}",
        f"Lessons processed: {len(lesson_files)}",
        "",
        "## Lessons",
        "",
        "| Lesson File | Last Modified |",
        "|---|---|",
    ]
    for name, mtime in lesson_info:
        index_lines.append(f"| {name} | {mtime} |")

    index_lines.extend([
        "",
        "## How to Use",
        "",
        "When working on code, check if your current task involves any of the",
        "trigger keywords listed below. If so, read the matching quirk file",
        "to avoid known pitfalls.",
        "",
        "## Tag Files",
        "",
        "| Tag | File | Quirks | Triggers |",
        "|---|---|---|---|",
    ])

    for tag, info in sorted(tag_files.items()):
        triggers_str = ", ".join(info["triggers"][:5])
        index_lines.append(f"| {tag} | [{info['file']}]({info['file']}) | {info['count']} | {triggers_str} |")

    index_lines.append("")
    (QUIRKS_DIR / "_index.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"  Wrote _index.md")


def main():
    print("Quirk Extractor")
    print(f"  Lessons dir: {LESSONS_DIR}")
    print(f"  Quirks dir: {QUIRKS_DIR}")
    print()

    lesson_files = sorted(LESSONS_DIR.glob("*.md"))
    print(f"Found {len(lesson_files)} lesson files:")
    for f in lesson_files:
        print(f"  - {f.name}")
    print()

    all_quirks = []
    for f in lesson_files:
        quirks = extract_quirks_from_lesson(f)
        structured_count = sum(1 for q in quirks if q.get("structured"))
        heuristic_count = len(quirks) - structured_count
        label = ""
        if structured_count and heuristic_count:
            label = f" ({structured_count} structured, {heuristic_count} heuristic)"
        elif structured_count:
            label = f" ({structured_count} structured)"
        elif heuristic_count:
            label = f" ({heuristic_count} heuristic)"
        print(f"  {f.name}: {len(quirks)} quirks{label}")
        all_quirks.extend(quirks)

    print(f"\nTotal quirks extracted: {len(all_quirks)}")
    print(f"\nWriting quirk files:")
    write_quirk_files(all_quirks, lesson_files)
    print(f"\nDone.")


if __name__ == "__main__":
    main()
