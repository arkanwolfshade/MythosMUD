#!/usr/bin/env python3
"""Analyze markdownlint output to show issue breakdown."""

import re
from collections import defaultdict
from pathlib import Path


def main():  # noqa: C901
    # Suppressed: Utility script with acceptable complexity for file fallback logic
    project_root = Path(__file__).parent.parent
    # Try most recent file first, then fall back to older ones
    output_file = project_root / "markdownlint-out-9.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-out-4.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-out-3.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-final-md032.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-refined.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-after-md032.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-current.txt"
    if not output_file.exists():
        output_file = project_root / "markdownlint-final.txt"

    if not output_file.exists():
        print(f"Error: {output_file} not found")
        return

    # Try UTF-16 LE first, then UTF-8
    try:
        with open(output_file, encoding="utf-16-le") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(output_file, encoding="utf-8") as f:
            content = f.read()

    lines = content.split("\n")
    error_lines = [line for line in lines if "error" in line]

    print(f"Total error lines: {len(error_lines)}")
    print("\nIssue breakdown by rule:")

    issues_by_rule = defaultdict(list)
    for line in error_lines:
        # Extract rule code (e.g., MD013, MD041, etc.)
        match = re.search(r"error\s+(MD\d+)", line)
        if match:
            rule = match.group(1)
            issues_by_rule[rule].append(line)

    for rule in sorted(issues_by_rule.keys()):
        print(f"  {rule}: {len(issues_by_rule[rule])} issues")

    print(
        f"\nTotal unique files with issues: {len({re.match(r'^([^:]+):', line).group(1) for line in error_lines if re.match(r'^([^:]+):', line)})}"
    )


if __name__ == "__main__":
    main()
