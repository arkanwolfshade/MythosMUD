#!/usr/bin/env python3
"""
Fix MD032: Add blank lines around lists.

Lists should be surrounded by blank lines according to markdownlint rules.
This script adds blank lines before and after lists where missing.
"""

import re
from pathlib import Path


def is_list_item(line: str) -> bool:
    """Check if a line is a list item."""
    stripped = line.strip()
    # Check for unordered list markers
    if re.match(r"^[-*+]\s+", stripped):
        return True
    # Check for ordered list markers
    if re.match(r"^\d+[.)]\s+", stripped):
        return True
    # Check for checklist items (may or may not have leading dash)
    if re.match(r"^(\s*[-*+]\s+)?\[[ xX]\]\s+", stripped):
        return True
    return False


def get_list_type(line: str) -> str:
    """Get the type of list item: 'unordered', 'ordered', 'checklist', or None."""
    stripped = line.strip()
    if re.match(r"^[-*+]\s+", stripped):
        return "unordered"
    if re.match(r"^\d+[.)]\s+", stripped):
        return "ordered"
    if re.match(r"^(\s*[-*+]\s+)?\[[ xX]\]\s+", stripped):
        return "checklist"
    return None


def is_code_block_delimiter(line: str) -> bool:
    """Check if a line is a code block delimiter."""
    return line.strip().startswith("```")


def is_table_row(line: str) -> bool:
    """Check if a line is a table row."""
    stripped = line.strip()
    # Table rows contain | characters
    if "|" in stripped and stripped.startswith("|") and stripped.endswith("|"):
        # But not if it's a separator row (all dashes/colons)
        if re.match(r"^\|[\s\-:|\|]+\|$", stripped):
            return False
        return True
    return False


def fix_blanks_around_lists(content: str) -> tuple[str, int]:  # noqa: C901
    """
    Add blank lines around lists where missing.

    Returns:
        (new_content, lines_added)
    """
    # Suppressed: Complex markdown parsing logic requires multiple conditional branches
    lines = content.split("\n")
    new_lines: list[str] = []
    lines_added = 0
    in_code_block = False
    in_table = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Track code block state
        if is_code_block_delimiter(line):
            in_code_block = not in_code_block
            new_lines.append(line)
            i += 1
            continue

        # Track table state (simple heuristic: consecutive | lines)
        if is_table_row(line):
            in_table = True
        elif in_table and not is_table_row(line) and line.strip():
            # End of table
            in_table = False

        # Skip processing inside code blocks or tables
        if in_code_block or in_table:
            new_lines.append(line)
            i += 1
            continue

        # Check if current line is a list item
        if is_list_item(line):
            current_list_type = get_list_type(line)
            # Find the last non-blank line (skip any blank lines we just added)
            prev_line = ""
            for j in range(len(new_lines) - 1, -1, -1):
                if new_lines[j].strip():
                    prev_line = new_lines[j]
                    break
            prev_list_type = get_list_type(prev_line) if prev_line.strip() else None

            # Check if we need a blank line before the list
            needs_blank_before = False

            # Check if there's already a blank line right before this line
            has_blank_before = new_lines and not new_lines[-1].strip()

            if has_blank_before:
                # Already has blank line, don't add another
                needs_blank_before = False
            elif prev_line and prev_line.strip():
                # Previous line exists and is not empty
                if not is_list_item(prev_line):
                    # Previous line is not a list item - need blank line
                    needs_blank_before = True
                elif prev_list_type and current_list_type and prev_list_type != current_list_type:
                    # Different list types - need blank line between them
                    needs_blank_before = True
                elif is_list_item(prev_line):
                    # Both are list items - check if same type and indentation
                    prev_indent = len(prev_line) - len(prev_line.lstrip())
                    curr_indent = len(line) - len(line.lstrip())
                    # If indentation changed significantly (more than 2 spaces), might be new list
                    if abs(curr_indent - prev_indent) > 2:
                        needs_blank_before = True
                    # If different list types, need blank line
                    elif prev_list_type != current_list_type:
                        needs_blank_before = True

            if needs_blank_before:
                new_lines.append("")
                lines_added += 1

            new_lines.append(line)

            # Check if we need a blank line after the list
            # Look ahead to find the end of the list
            j = i + 1
            list_ended = False

            while j < len(lines):
                next_line = lines[j]
                next_list_type = get_list_type(next_line)

                # If next line is also a list item
                if is_list_item(next_line):
                    # Check if it's a different list type
                    if next_list_type and current_list_type and next_list_type != current_list_type:
                        # Different list type - list has ended, need blank line
                        list_ended = True
                        break
                    # Same list type - check indentation
                    curr_indent = len(line) - len(line.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    # If indentation changed significantly, might be end of list
                    if abs(next_indent - curr_indent) > 2:
                        list_ended = True
                        break
                    # Continue in same list
                    j += 1
                    continue

                # If next line is empty, list has ended
                if not next_line.strip():
                    list_ended = True
                    break

                # If next line is a code block delimiter, list has ended
                if is_code_block_delimiter(next_line):
                    list_ended = True
                    break

                # If next line is a table row, list has ended
                if is_table_row(next_line):
                    list_ended = True
                    break

                # If next line is a heading, list has ended
                if next_line.strip().startswith("#"):
                    list_ended = True
                    break

                # If next line is not a list item and not empty, list has ended
                list_ended = True
                break

            # If list ended and next non-empty line needs a blank line before it
            if list_ended and j < len(lines):
                next_line = lines[j]
                # Check if there's already a blank line
                if j > i + 1 and not lines[j - 1].strip():
                    # Already has blank line, skip
                    pass
                elif next_line.strip():
                    # Add blank line after the list
                    new_lines.append("")
                    lines_added += 1

            i += 1
        else:
            # Not a list item, just append
            new_lines.append(line)
            i += 1

    return "\n".join(new_lines), lines_added


def parse_markdownlint_output(output_file: Path) -> list[Path]:
    """Parse markdownlint output to get files with MD032 issues."""
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

    # Pattern for MD032 errors
    pattern = r"^([^:]+):\d+.*error\s+MD032"
    for line in content.split("\n"):
        match = re.match(pattern, line)
        if match:
            file_path = Path(match.group(1))
            files_to_fix.add(file_path)

    return list(files_to_fix)


def fix_markdown_file(file_path: Path) -> tuple[bool, int]:
    """
    Fix blanks around lists in a single markdown file.

    Returns:
        (changed, lines_added)
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            original_content = f.read()

        new_content, lines_added = fix_blanks_around_lists(original_content)

        if new_content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, lines_added

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def main():  # noqa: C901
    """Main function to fix MD032 issues."""
    # Suppressed: Utility script with acceptable complexity for file processing logic
    project_root = Path(__file__).parent.parent

    # Parse markdownlint output to get files with MD032 issues
    output_file = None
    for filename in [
        "markdownlint-out-7.txt",
        "markdownlint-out-6.txt",
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
        print(f"Found {len(files_with_issues)} files with MD032 issues in output")

        # Process all markdown files to catch all cases
        # (Some issues might not be in the output if it's from a previous run)
        print("Processing all markdown files to ensure complete coverage...")
        ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".venv-ci"}
        all_md_files = []
        for md_file in project_root.rglob("*.md"):
            if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
                continue
            all_md_files.append(md_file)

        # Always process all files to catch all cases (output might be stale)
        files_to_fix = all_md_files
        print(f"Processing {len(files_to_fix)} files (found {len(files_with_issues)} with MD032 in output)")
    else:
        print("Warning: No markdownlint output file found.")
        print("Processing all markdown files...")
        # Fallback: process all markdown files
        ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".venv-ci"}
        files_to_fix = []
        for md_file in project_root.rglob("*.md"):
            if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
                continue
            files_to_fix.append(md_file)

    total_changed = 0
    total_lines_added = 0

    for file_path in sorted(files_to_fix):
        # Make path absolute if relative
        if not file_path.is_absolute():
            file_path = project_root / file_path

        if not file_path.exists():
            print(f"Warning: {file_path} does not exist, skipping")
            continue

        changed, lines_added = fix_markdown_file(file_path)
        if changed:
            total_changed += 1
            total_lines_added += lines_added
            print(f"[OK] {file_path.relative_to(project_root)} ({lines_added} blank lines added)")

    print(f"\nSummary: {total_changed} files changed, {total_lines_added} total blank lines added")


if __name__ == "__main__":
    main()
