#!/usr/bin/env python3
"""
Automatically fix common markdownlint issues in Markdown files.
"""

import re
import sys
from pathlib import Path


def fix_line_length(line: str, max_length: int = 80) -> str:
    """Break long lines at word boundaries."""
    if len(line) <= max_length:
        return line

    # Don't break code blocks, links, or special lines
    if line.strip().startswith("```") or line.strip().startswith("|"):
        return line
    if "://" in line or line.strip().startswith("http"):
        return line

    # Try to break at word boundaries
    words = line.split()
    if not words:
        return line

    result = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip() if current_line else word
        if len(test_line) <= max_length:
            current_line = test_line
        else:
            if current_line:
                result.append(current_line)
            current_line = word

    if current_line:
        result.append(current_line)

    return "\n".join(result) if result else line


def fix_blanks_around_lists(content: str) -> str:
    """Add blank lines before and after lists."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result.append(line)

        # Check if this is a list item
        if re.match(r"^[\s]*[-*+]\s", line) or re.match(r"^[\s]*\d+\.\s", line):
            # Check if previous line needs a blank line
            if i > 0 and lines[i - 1].strip() and not lines[i - 1].strip().startswith("-") and not lines[i - 1].strip().startswith("*") and not re.match(r"^\d+\.", lines[i - 1].strip()):
                # Insert blank line before list
                if result and result[-1] != "":
                    result.insert(-1, "")
                    i += 1
                    continue

            # Check if next line needs a blank line after list
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # If next line is not a list item and not blank
                if next_line.strip() and not re.match(r"^[\s]*[-*+]\s", next_line) and not re.match(r"^[\s]*\d+\.\s", next_line):
                    # Check if we're at the end of the list
                    if i + 2 >= len(lines) or not re.match(r"^[\s]*[-*+]\s", lines[i + 2]) and not re.match(r"^[\s]*\d+\.\s", lines[i + 2]):
                        result.append("")
                        i += 1
                        continue

        i += 1

    return "\n".join(result)


def fix_blanks_around_fences(content: str) -> str:
    """Add blank lines before and after fenced code blocks."""
    lines = content.split("\n")
    result = []
    i = 0
    in_code_block = False

    while i < len(lines):
        line = lines[i]
        is_fence = line.strip().startswith("```")

        if is_fence and not in_code_block:
            # Opening fence
            if i > 0 and lines[i - 1].strip():
                result.append("")
            result.append(line)
            in_code_block = True
        elif is_fence and in_code_block:
            # Closing fence
            result.append(line)
            in_code_block = False
            if i + 1 < len(lines) and lines[i + 1].strip():
                result.append("")
        else:
            result.append(line)

        i += 1

    return "\n".join(result)


def fix_fence_language(content: str) -> str:
    """Add language tags to fenced code blocks without them."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```") and line.strip() == "```":
            # Fence without language - try to infer or use 'text'
            result.append("```text")
        else:
            result.append(line)
        i += 1

    return "\n".join(result)


def fix_blanks_around_headings(content: str) -> str:
    """Add blank lines before and after headings."""
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        is_heading = re.match(r"^#+\s", line)

        if is_heading:
            # Add blank line before heading if needed
            if i > 0 and lines[i - 1].strip():
                result.append("")
            result.append(line)
            # Add blank line after heading if needed
            if i + 1 < len(lines) and lines[i + 1].strip():
                result.append("")
        else:
            result.append(line)

        i += 1

    return "\n".join(result)


def fix_trailing_punctuation_in_headings(content: str) -> str:
    """Remove trailing punctuation from headings."""
    lines = content.split("\n")
    result = []

    for line in lines:
        if re.match(r"^#+\s", line):
            # Remove trailing colons, periods, etc.
            line = re.sub(r"([:;.])$", "", line)
        result.append(line)

    return "\n".join(result)


def fix_file(file_path: Path) -> bool:
    """Fix markdownlint issues in a file."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original = content

        # Apply fixes
        content = fix_blanks_around_fences(content)
        content = fix_fence_language(content)
        content = fix_blanks_around_lists(content)
        content = fix_blanks_around_headings(content)
        content = fix_trailing_punctuation_in_headings(content)

        # Fix line length (more conservative - only break very long lines)
        lines = content.split("\n")
        fixed_lines = []
        for line in lines:
            if len(line) > 100:  # Only fix very long lines
                fixed_lines.append(fix_line_length(line))
            else:
                fixed_lines.append(line)
        content = "\n".join(fixed_lines)

        if content != original:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: fix_markdownlint.py <file1> [file2] ...")
        sys.exit(1)

    files_fixed = 0
    for file_path_str in sys.argv[1:]:
        file_path = Path(file_path_str)
        if file_path.exists() and file_path.suffix == ".md":
            if fix_file(file_path):
                print(f"Fixed: {file_path}")
                files_fixed += 1
        else:
            print(f"Skipping: {file_path} (not a markdown file or doesn't exist)")

    print(f"\nFixed {files_fixed} file(s)")


if __name__ == "__main__":
    main()
