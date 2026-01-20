#!/usr/bin/env python3
"""
Markdown formatting script to apply common formatting patterns.

This script applies formatting fixes based on the diff patterns:
1. Remove leading `-` from bold text items that aren't list items
2. Remove leading `-` from checkmark/status items
3. Add angle brackets around URLs
4. Fix code block spacing
5. Various other markdown formatting fixes
"""

import re
from pathlib import Path


def fix_bold_items_without_list_marker(content: str) -> str:
    """Remove leading `-` from bold text that isn't part of a list."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        prev_line = lines[i - 1] if i > 0 else ""
        next_line = lines[i + 1] if i < len(lines) - 1 else ""

        # Pattern: `- **Text**:` at start of line
        # Remove dash if:
        # 1. Previous line is empty, heading, or ends with `:`
        # 2. Next line doesn't start with `-` (not part of a list)
        if re.match(r"^(\s*)- (\*\*[^*]+\*\*:?)(.*)$", line):
            should_remove = False

            # Check if previous line suggests this isn't a list item
            if not prev_line.strip() or prev_line.strip().startswith("#") or prev_line.strip().endswith(":"):
                should_remove = True

            # Also check if next line doesn't start with `-` (not a list)
            if should_remove and next_line and not next_line.strip().startswith("-"):
                line = re.sub(r"^(\s*)- (\*\*[^*]+\*\*:?)(.*)$", r"\1\2\3", line)
            elif should_remove:
                # Even if next line has dash, if prev suggests non-list, remove it
                line = re.sub(r"^(\s*)- (\*\*[^*]+\*\*:?)(.*)$", r"\1\2\3", line)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_checkmark_items(content: str) -> str:
    """Remove leading `-` from checkmark/status items."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        prev_line = lines[i - 1] if i > 0 else ""

        # Pattern: `- ✅` or `- ❌` at start of line
        # Remove dash if previous line is heading, empty, or ends with `:`
        if re.match(r"^(\s*)- ([✅❌])(.*)$", line):
            if not prev_line.strip() or prev_line.strip().startswith("#") or prev_line.strip().endswith(":"):
                line = re.sub(r"^(\s*)- ([✅❌])(.*)$", r"\1\2\3", line)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_url_formatting(content: str) -> str:
    """Add angle brackets around bare URLs in markdown."""
    # Pattern: `**Text**: https://...` -> `**Text**: <https://...>`
    # Also: `2. **Text**: https://...` -> `2. **Text**: <https://...>`
    # But don't add if already has angle brackets

    # Pattern 1: After bold text with colon
    pattern1 = r"(\*\*[^*]+\*\*:\s*)(https?://[^\s\)<>]+)"
    content = re.sub(pattern1, r"\1<\2>", content)

    # Pattern 2: After numbered list with bold
    pattern2 = r"(\d+\.\s*\*\*[^*]+\*\*:\s*)(https?://[^\s\)<>]+)"
    content = re.sub(pattern2, r"\1<\2>", content)

    return content


def fix_code_block_spacing(content: str) -> str:
    """Fix spacing in code blocks (e.g., `@#` -> ` @#`)."""
    lines = content.split("\n")
    result_lines = []
    in_code_block = False

    for line in lines:
        # Track code block state
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            result_lines.append(line)
            continue

        if in_code_block:
            # Fix `@#` spacing - change `	@#` to ` @#` (tab to space)
            if line.startswith("\t@#"):
                line = line.replace("\t@#", " @#", 1)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_plain_text_after_colons(content: str) -> str:
    """Remove leading `-` from plain text items after lines ending with `:`."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        prev_line = lines[i - 1] if i > 0 else ""
        next_line = lines[i + 1] if i < len(lines) - 1 else ""

        # If previous line ends with `:` and this is a simple `- Text` line
        # (not bold, not a list item), remove the dash
        if prev_line.strip().endswith(":"):
            # Pattern: `- Text` (simple text, not bold, not checkbox)
            if re.match(r"^(\s*)- ([A-Z][^:]*)$", line):
                # Check if next line also starts with `-` - if not, probably not a list
                if not next_line.strip().startswith("-"):
                    line = re.sub(r"^(\s*)- ([A-Z][^:]*)$", r"\1\2", line)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_checklist_items(content: str) -> str:
    """Remove leading `-` from checklist items in certain contexts."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        prev_line = lines[i - 1] if i > 0 else ""

        # Pattern: `- [ ]` -> `[ ]` (remove dash from checklist items after headings)
        if re.match(r"^(\s*)- (\[ \])(.*)$", line):
            # If previous line is a heading (#### or ###), remove the dash
            if prev_line.strip().startswith("####") or prev_line.strip().startswith("###"):
                line = re.sub(r"^(\s*)- (\[ \])(.*)$", r"\1\2\3", line)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_heading_trailing_colons(content: str) -> str:
    """Remove trailing colons from headings."""
    lines = content.split("\n")
    result_lines = []

    for line in lines:
        # Pattern: `### Heading:` -> `### Heading`
        if re.match(r"^(#{1,6}\s+.+):\s*$", line):
            line = re.sub(r"^(#{1,6}\s+.+):\s*$", r"\1", line)
        result_lines.append(line)

    return "\n".join(result_lines)


def fix_items_after_headings(content: str) -> str:
    """Remove leading `-` from items that follow headings (not part of lists)."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        prev_line = lines[i - 1].strip() if i > 0 else ""
        prev_prev_line = lines[i - 2].strip() if i > 1 else ""

        # Check if previous line is a heading or if we're after a heading with blank line
        is_after_heading = prev_line.startswith("#") or (not prev_line and prev_prev_line.startswith("#"))

        if is_after_heading:
            # Pattern: `- Text` or `- ✅` or `- ❌` or `- **Text**` -> remove dash
            # Remove dash from items that follow headings
            if re.match(r"^(\s*)- (.+)$", line):
                line = re.sub(r"^(\s*)- (.+)$", r"\1\2", line)

        result_lines.append(line)

    return "\n".join(result_lines)


def fix_blank_lines_after_headings(content: str) -> str:
    """Add blank lines after headings when content follows."""
    lines = content.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        result_lines.append(line)

        # Check if current line is a heading
        if re.match(r"^#{1,6}\s+.+", line.strip()):
            # Check if next line exists and is not empty and not a heading
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # If next line is not empty and not a heading, and not already blank
                if next_line.strip() and not next_line.strip().startswith("#"):
                    # Only add blank line if there isn't already one
                    if result_lines and result_lines[-1] != "":
                        result_lines.append("")

    return "\n".join(result_lines)


def format_markdown_file(file_path: Path) -> tuple[bool, int]:
    """
    Format a single markdown file.

    Returns:
        (changed, lines_modified): Whether file was changed and how many lines
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            original_content = f.read()

        content = original_content

        # Apply all formatting fixes
        content = fix_bold_items_without_list_marker(content)
        content = fix_checkmark_items(content)
        content = fix_url_formatting(content)
        content = fix_code_block_spacing(content)
        content = fix_plain_text_after_colons(content)
        content = fix_checklist_items(content)
        content = fix_heading_trailing_colons(content)
        content = fix_items_after_headings(content)
        content = fix_blank_lines_after_headings(content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            # Count changed lines
            original_lines = original_content.split("\n")
            new_lines = content.split("\n")
            # Count differences, handling cases where line counts differ
            min_len = min(len(original_lines), len(new_lines))
            lines_changed = sum(1 for o, n in zip(original_lines[:min_len], new_lines[:min_len], strict=True) if o != n)
            # Add any extra lines
            lines_changed += abs(len(original_lines) - len(new_lines))

            return True, lines_changed

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def main():
    """Main function to process all markdown files."""
    # Get project root
    project_root = Path(__file__).parent.parent

    # Find all markdown files in the project
    # Exclude node_modules, .git, and other common ignore directories
    ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}

    markdown_files = []
    for md_file in project_root.rglob("*.md"):
        # Skip files in ignored directories
        if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
            continue
        markdown_files.append(md_file)

    print(f"Found {len(markdown_files)} markdown files to process")

    total_changed = 0
    total_lines = 0

    for file_path in sorted(markdown_files):
        changed, lines = format_markdown_file(file_path)
        if changed:
            total_changed += 1
            total_lines += lines
            print(f"[OK] {file_path.relative_to(project_root)} ({lines} lines)")

    print(f"\nSummary: {total_changed} files changed, {total_lines} total lines modified")


if __name__ == "__main__":
    main()
