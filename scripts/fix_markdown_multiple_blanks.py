#!/usr/bin/env python3
"""
Fix MD012: Multiple consecutive blank lines.

Replaces multiple consecutive blank lines with a single blank line.
"""

import re
from pathlib import Path


def fix_multiple_blanks(content: str) -> tuple[str, int]:
    """
    Fix multiple consecutive blank lines (MD012).

    Returns:
        (new_content, lines_removed)
    """
    lines = content.split("\n")
    new_lines = []
    lines_removed = 0
    prev_blank = False
    in_code_block = False

    for line in lines:
        # Track code block state
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            new_lines.append(line)
            prev_blank = False
            continue

        # Skip processing inside code blocks
        if in_code_block:
            new_lines.append(line)
            prev_blank = False
            continue

        # Check if current line is blank
        is_blank = not line.strip()

        if is_blank:
            # Only add blank line if previous line wasn't blank
            if not prev_blank:
                new_lines.append(line)
                prev_blank = True
            else:
                # Skip this blank line (it's a duplicate)
                lines_removed += 1
        else:
            new_lines.append(line)
            prev_blank = False

    return "\n".join(new_lines), lines_removed


def parse_markdownlint_output(output_file: Path) -> list[Path]:
    """Parse markdownlint output to get files with MD012 issues."""
    files_to_fix = set()

    try:
        with open(output_file, encoding="utf-16-le") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(output_file, encoding="utf-8") as f:
                content = f.read()
        except Exception:
            return []

    # Pattern for MD012 errors
    pattern = r"^([^:]+):\d+.*error\s+MD012"
    for line in content.split("\n"):
        match = re.match(pattern, line)
        if match:
            file_path = Path(match.group(1))
            files_to_fix.add(file_path)

    return list(files_to_fix)


def fix_markdown_file(file_path: Path) -> tuple[bool, int]:
    """
    Fix multiple blank lines in a single markdown file.

    Returns:
        (changed, lines_removed)
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            original_content = f.read()

        new_content, lines_removed = fix_multiple_blanks(original_content)

        if new_content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, lines_removed

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def main():  # noqa: C901
    """Main function to fix MD012 issues."""
    # Suppressed: Utility script with acceptable complexity for file processing logic
    project_root = Path(__file__).parent.parent

    # Parse markdownlint output to get files with MD012 issues
    output_file = None
    for filename in [
        "markdownlint-out-5.txt",
        "markdownlint-out-4.txt",
        "markdownlint-out-3.txt",
        "markdownlint-refined.txt",
        "markdownlint-after-md032.txt",
        "markdownlint-current.txt",
        "markdownlint-final.txt",
    ]:
        candidate = project_root / filename
        if candidate.exists():
            output_file = candidate
            break

    if output_file:
        print(f"Parsing markdownlint output from {output_file}...")
        files_with_issues = parse_markdownlint_output(output_file)
        print(f"Found {len(files_with_issues)} files with MD012 issues in output")

        # Process all markdown files to catch all cases
        print("Processing all markdown files to ensure complete coverage...")
        ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".venv-ci"}
        all_md_files = []
        for md_file in project_root.rglob("*.md"):
            if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
                continue
            all_md_files.append(md_file)

        # Always process all files to catch all cases (output might be stale)
        files_to_fix = all_md_files
    else:
        print("No markdownlint output file found.")
        print("Processing all markdown files...")
        # Fallback: process all markdown files
        ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".venv-ci"}
        files_to_fix = []
        for md_file in project_root.rglob("*.md"):
            if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
                continue
            files_to_fix.append(md_file)

    total_changed = 0
    total_lines_removed = 0

    for file_path in sorted(files_to_fix):
        # Make path absolute if relative
        if not file_path.is_absolute():
            file_path = project_root / file_path

        if not file_path.exists():
            print(f"Warning: {file_path} does not exist, skipping")
            continue

        changed, lines_removed = fix_markdown_file(file_path)
        if changed:
            total_changed += 1
            total_lines_removed += lines_removed
            print(f"[OK] {file_path.relative_to(project_root)} ({lines_removed} blank lines removed)")

    print(f"\nSummary: {total_changed} files changed, {total_lines_removed} total blank lines removed")


if __name__ == "__main__":
    main()
