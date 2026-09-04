#!/usr/bin/env python3
"""
Fix common markdownlint issues automatically.

Handles:
- MD041: Add top-level heading to files that don't start with one
- MD036: Convert bold/italic used as headings to proper headings (context-aware)
- MD051: Fix invalid link fragments by generating proper anchors
"""

import re
from pathlib import Path


def generate_anchor(text: str) -> str:
    """Generate a markdown anchor from text."""
    # Remove markdown formatting
    text = re.sub(r"[#*_`]", "", text)
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and special chars with hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    # Remove leading/trailing hyphens
    text = text.strip("-")
    return text


def fix_first_line_heading(content: str, file_path: Path) -> tuple[str, bool]:
    """
    Fix MD041: Add top-level heading if file doesn't start with one.

    Returns: (new_content, changed)
    """
    lines = content.split("\n")
    if not lines:
        return content, False

    first_line = lines[0].strip()

    # If first line is already a heading, no change needed
    if first_line.startswith("#"):
        return content, False

    # If first line is empty, check second line
    if not first_line and len(lines) > 1:
        second_line = lines[1].strip()
        if second_line.startswith("#"):
            return content, False

    # Generate heading from filename or first non-empty line
    if first_line:
        # Use first line as heading text (remove markdown formatting)
        heading_text = re.sub(r"^[-*+\d.]\s*", "", first_line)  # Remove list markers
        heading_text = re.sub(r"[#*_`]", "", heading_text).strip()  # Remove formatting
        if not heading_text:
            heading_text = file_path.stem.replace("_", " ").replace("-", " ").title()
    else:
        # Use filename as heading
        heading_text = file_path.stem.replace("_", " ").replace("-", " ").title()

    # Add heading at the start
    new_lines = [f"# {heading_text}", ""]
    if first_line:
        new_lines.extend(lines)
    else:
        new_lines.extend(lines[1:])

    return "\n".join(new_lines), True


def fix_emphasis_as_heading(content: str) -> tuple[str, bool]:
    """
    Fix MD036: Convert bold/italic used as headings to proper headings.

    This is context-aware - only converts if the line appears to be a heading
    (followed by content, not part of a paragraph).
    """
    lines = content.split("\n")
    new_lines = []
    changed = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if line is bold or italic that might be a heading
        # Pattern: **text** or *text* at start of line (possibly with leading spaces)
        bold_match = re.match(r"^(\s*)\*\*(.+?)\*\*(\s*)$", stripped)
        italic_match = re.match(r"^(\s*)\*(.+?)\*(\s*)$", stripped)

        if bold_match or italic_match:
            # Check if next non-empty line is not a continuation of a paragraph
            # (i.e., it's a new paragraph, list, code block, or heading)
            is_heading_candidate = False
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # If next line is empty, or starts with list marker, code block, or heading
                if not next_line or next_line.startswith(("-", "*", "+", "`", "#")) or re.match(r"^\d+\.", next_line):
                    is_heading_candidate = True
            else:
                # Last line, could be a heading
                is_heading_candidate = True

            # Also check if previous line was empty (common for headings)
            if i > 0:
                prev_line = lines[i - 1].strip()
                if not prev_line:
                    is_heading_candidate = True

            if is_heading_candidate:
                if bold_match:
                    indent = bold_match.group(1)
                    text = bold_match.group(2)
                    # Use level 3 heading (###) for converted bold headings
                    new_lines.append(f"{indent}### {text}")
                    changed = True
                elif italic_match:
                    indent = italic_match.group(1)
                    text = italic_match.group(2)
                    # Use level 4 heading (####) for converted italic headings
                    new_lines.append(f"{indent}#### {text}")
                    changed = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

        i += 1

    return "\n".join(new_lines), changed


def fix_link_fragments(content: str) -> tuple[str, bool]:
    """
    Fix MD051: Fix invalid link fragments by generating proper anchors.

    Scans for headings and builds a map, then fixes links that don't match.
    """
    lines = content.split("\n")
    heading_map: dict[str, str] = {}  # anchor -> heading_text
    changed = False

    # First pass: collect all headings and their anchors
    for line in lines:
        heading_match = re.match(r"^(#+)\s+(.+)$", line.strip())
        if heading_match:
            text = heading_match.group(2).strip()
            anchor = generate_anchor(text)
            heading_map[anchor] = text

    # Second pass: fix links
    new_lines = []
    for line in lines:
        # Find all markdown links with fragments
        link_pattern = r"\[([^\]]+)\]\(#([^)]+)\)"

        def replace_link(match):
            link_text = match.group(1)
            fragment = match.group(2)

            # Check if fragment matches any heading anchor
            if fragment in heading_map:
                return match.group(0)  # Link is valid, no change

            # Try to find a matching heading (case-insensitive, with variations)
            fragment_lower = fragment.lower()
            for anchor, _heading_text in heading_map.items():
                if anchor.lower() == fragment_lower or anchor.lower().replace("-", "--") == fragment_lower:
                    return f"[{link_text}](#{anchor})"

            # If no match found, generate anchor from fragment and see if it matches
            generated = generate_anchor(fragment)
            if generated in heading_map:
                return f"[{link_text}](#{generated})"

            # No fix possible, return original
            return match.group(0)

        new_line = re.sub(link_pattern, replace_link, line)
        if new_line != line:
            changed = True
        new_lines.append(new_line)

    return "\n".join(new_lines), changed


def fix_markdown_file(file_path: Path) -> tuple[bool, list[str]]:
    """
    Fix common markdown issues in a file.

    Returns: (changed, list of fixes applied)
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content
        fixes_applied = []

        # Apply fixes in order
        content, changed1 = fix_first_line_heading(content, file_path)
        if changed1:
            fixes_applied.append("MD041: Added top-level heading")

        content, changed2 = fix_emphasis_as_heading(content)
        if changed2:
            fixes_applied.append("MD036: Converted emphasis to headings")

        content, changed3 = fix_link_fragments(content)
        if changed3:
            fixes_applied.append("MD051: Fixed link fragments")

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True, fixes_applied

        return False, []

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []


def parse_markdownlint_output(output_file: Path) -> list[Path]:
    """Parse markdownlint output to get files with fixable issues."""
    files_to_fix = set()

    try:
        with open(output_file, encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(output_file, encoding="utf-16-le") as f:
                content = f.read()
        except Exception:
            return []

    # Patterns for fixable issues
    patterns = [
        (r"^([^:]+):\d+.*error MD041/", "MD041"),
        (r"^([^:]+):\d+.*error MD036/", "MD036"),
        (r"^([^:]+):\d+:\d+.*error MD051/", "MD051"),
    ]

    for line in content.split("\n"):
        for pattern, _issue_type in patterns:
            match = re.match(pattern, line)
            if match:
                file_path = Path(match.group(1))
                files_to_fix.add(file_path)
                break

    return list(files_to_fix)


def main():
    """Main function."""
    project_root = Path(__file__).parent.parent

    # Parse markdownlint output
    output_file = None
    for filename in [
        "markdownlint-out-8.txt",
        "markdownlint-out-7.txt",
        "markdownlint-out-6.txt",
        "markdownlint-out-5.txt",
        "markdownlint-out-4.txt",
        "markdownlint-out-3.txt",
        "markdownlint-out-2.txt",
    ]:
        candidate = project_root / filename
        if candidate.exists():
            output_file = candidate
            break

    if output_file:
        print(f"Parsing markdownlint output from {output_file}...")
        files_to_fix = parse_markdownlint_output(output_file)
        print(f"Found {len(files_to_fix)} files with fixable issues")
    else:
        print("Warning: No markdownlint output file found.")
        return

    total_changed = 0

    for file_path in sorted(files_to_fix):
        # Make path absolute if relative
        if not file_path.is_absolute():
            file_path = project_root / file_path

        if not file_path.exists():
            print(f"Warning: {file_path} does not exist, skipping")
            continue

        changed, fixes = fix_markdown_file(file_path)
        if changed:
            total_changed += 1
            fixes_str = ", ".join(fixes)
            print(f"[OK] {file_path.relative_to(project_root)} ({fixes_str})")

    print(f"\nSummary: {total_changed} files changed")


if __name__ == "__main__":
    main()
