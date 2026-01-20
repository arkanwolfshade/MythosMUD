#!/usr/bin/env python3
"""
Fix markdown line length violations (MD013).

This script wraps long lines in markdown files to comply with the 120 character limit.
It intelligently handles:
- Code blocks (skips them)
- Links (preserves them)
- Lists (wraps appropriately)
- Headers (preserves them)
- Tables (preserves them)
"""

import re
from pathlib import Path

MAX_LINE_LENGTH = 120


def should_skip_line(line: str) -> bool:
    """Check if a line should be skipped (code blocks, tables, etc.)."""
    stripped = line.strip()

    # Skip code blocks
    if stripped.startswith("```"):
        return True

    # Skip table rows (contain |)
    if "|" in stripped and stripped.startswith("|"):
        return True

    # Skip horizontal rules
    if re.match(r"^[-*_]{3,}$", stripped):
        return True

    # Skip HTML comments
    if stripped.startswith("<!--") and stripped.endswith("-->"):
        return True

    return False


def is_in_code_block(lines: list[str], index: int) -> bool:
    """Check if we're currently inside a code block."""
    code_block_count = 0
    for i in range(index + 1):
        if lines[i].strip().startswith("```"):
            code_block_count += 1
    return code_block_count % 2 == 1


def wrap_line(line: str, max_length: int = MAX_LINE_LENGTH) -> list[str]:
    """
    Wrap a long line intelligently.

    Returns a list of wrapped lines.
    """
    # If line is short enough, return as-is
    if len(line) <= max_length:
        return [line]

    # If it's a header, try to wrap at word boundaries
    if line.strip().startswith("#"):
        return wrap_header(line, max_length)

    # If it's a list item, wrap with proper indentation
    list_match = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
    if list_match:
        indent = list_match.group(1)
        marker = list_match.group(2)
        content = list_match.group(3)
        return wrap_list_item(indent, marker, content, max_length)

    # If it's a link, try to preserve it
    if "[" in line and "](" in line:
        return wrap_line_with_links(line, max_length)

    # Default: wrap at word boundaries
    return wrap_plain_text(line, max_length)


def wrap_header(line: str, max_length: int) -> list[str]:
    """Wrap a header line."""
    # Headers shouldn't be wrapped, but if they're too long, we'll wrap the content
    header_match = re.match(r"^(#+\s+)(.*)$", line)
    if header_match:
        prefix = header_match.group(1)
        content = header_match.group(2)
        if len(line) <= max_length:
            return [line]
        # For very long headers, wrap the content part
        wrapped_content = wrap_plain_text(content, max_length - len(prefix))
        return [prefix + wrapped_content[0]] + [prefix.rstrip() + " " + w for w in wrapped_content[1:]]
    return [line]


def wrap_list_item(indent: str, marker: str, content: str, max_length: int) -> list[str]:
    """Wrap a list item with proper indentation."""
    first_line_prefix = indent + marker + " "
    continuation_prefix = indent + " " * (len(marker) + 1)
    available_width = max_length - len(first_line_prefix)

    if len(content) <= available_width:
        return [first_line_prefix + content]

    # Wrap the content
    wrapped = wrap_plain_text(content, available_width)
    result = [first_line_prefix + wrapped[0]]

    # Add continuation lines with proper indentation
    for w in wrapped[1:]:
        result.append(continuation_prefix + w)

    return result


def wrap_line_with_links(line: str, max_length: int) -> list[str]:
    """Wrap a line that contains markdown links."""
    # Try to preserve links, but wrap if necessary
    # This is complex, so we'll use a simpler approach: wrap at spaces but try to keep links together
    words = line.split(" ")
    result_lines = []
    current_line = ""

    for word in words:
        # Check if adding this word would exceed the limit
        test_line = current_line + (" " if current_line else "") + word
        if len(test_line) <= max_length:
            current_line = test_line
        else:
            if current_line:
                result_lines.append(current_line)
            current_line = word

    if current_line:
        result_lines.append(current_line)

    return result_lines if result_lines else [line]


def wrap_plain_text(line: str, max_length: int) -> list[str]:
    """Wrap plain text at word boundaries."""
    # Preserve leading whitespace
    leading_whitespace = len(line) - len(line.lstrip())
    indent = line[:leading_whitespace]
    content = line[leading_whitespace:]

    if len(line) <= max_length:
        return [line]

    # Split into words
    words = content.split(" ")
    result_lines = []
    current_line = indent

    for word in words:
        # Check if adding this word would exceed the limit
        test_line = current_line + (" " if current_line != indent else "") + word
        if len(test_line) <= max_length:
            current_line = test_line
        else:
            if current_line != indent:
                result_lines.append(current_line)
            current_line = indent + word

    if current_line != indent:
        result_lines.append(current_line)

    return result_lines if result_lines else [line]


def fix_markdown_file(file_path: Path) -> tuple[bool, int]:
    """
    Fix line length issues in a markdown file.

    Returns:
        (changed, lines_modified): Whether file was changed and how many lines
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            original_lines = f.readlines()

        new_lines = []
        in_code_block = False
        lines_modified = 0

        for _i, line in enumerate(original_lines):
            # Track code block state
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                new_lines.append(line)
                continue

            # Skip lines that shouldn't be wrapped
            if in_code_block or should_skip_line(line):
                new_lines.append(line)
                continue

            # Check if line needs wrapping
            if len(line.rstrip("\n\r")) > MAX_LINE_LENGTH:
                wrapped = wrap_line(line.rstrip("\n\r"), MAX_LINE_LENGTH)
                new_lines.extend([w + "\n" for w in wrapped])
                if len(wrapped) > 1:
                    lines_modified += len(wrapped) - 1
            else:
                new_lines.append(line)

        # Only write if content changed
        new_content = "".join(new_lines)
        original_content = "".join(original_lines)

        if new_content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, lines_modified

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def parse_markdownlint_output(output_file: Path) -> list[tuple[Path, int]]:
    """
    Parse markdownlint output file to get list of files with line length issues.

    Format: filename:line:column error MD013/line-length ...
    """
    issues = []

    try:
        with open(output_file, encoding="utf-16-le") as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try UTF-8
        with open(output_file, encoding="utf-8") as f:
            content = f.read()

    # Parse errors
    pattern = r"^([^:]+):(\d+):\d+\s+error\s+MD013/line-length"
    for line in content.split("\n"):
        match = re.match(pattern, line)
        if match:
            file_path = Path(match.group(1))
            line_num = int(match.group(2))
            issues.append((file_path, line_num))

    # Get unique files
    unique_files = {issue[0] for issue in issues}
    return list(unique_files)


def main():
    """Main function to fix markdown line length issues."""
    project_root = Path(__file__).parent.parent

    # Parse markdownlint output to get files with issues
    # Try newest output file first, then fall back to older ones
    output_file = None
    for filename in [
        "markdownlint-out-5.txt",
        "markdownlint-out-4.txt",
        "markdownlint-out-3.txt",
        "markdownlint-out-2.txt",
    ]:
        candidate = project_root / filename
        if candidate.exists():
            output_file = candidate
            break

    if output_file.exists():
        print(f"Parsing markdownlint output from {output_file}...")
        files_to_fix = parse_markdownlint_output(output_file)
        print(f"Found {len(files_to_fix)} files with line length issues")
    else:
        print(f"Warning: {output_file} not found. Processing all markdown files...")
        # Fallback: process all markdown files in common directories
        directories = [
            project_root / ".agent-os",
            project_root / "docs",
            project_root / "e2e-tests",
        ]
        files_to_fix = []
        for directory in directories:
            if directory.exists():
                files_to_fix.extend(directory.rglob("*.md"))

    total_changed = 0
    total_lines = 0

    for file_path in sorted(files_to_fix):
        # Make path absolute if relative
        if not file_path.is_absolute():
            file_path = project_root / file_path

        if not file_path.exists():
            print(f"Warning: {file_path} does not exist, skipping")
            continue

        changed, lines = fix_markdown_file(file_path)
        if changed:
            total_changed += 1
            total_lines += lines
            print(f"[OK] {file_path.relative_to(project_root)} ({lines} lines wrapped)")

    print(f"\nSummary: {total_changed} files changed, {total_lines} total lines wrapped")


if __name__ == "__main__":
    main()
