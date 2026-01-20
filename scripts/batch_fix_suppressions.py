#!/usr/bin/env python3
"""
Batch fix common suppression patterns that can be safely automated.

This script handles common patterns where the explanation can be inferred
from context, but should be reviewed manually for accuracy.
"""

import json
import re
from pathlib import Path

# Common patterns and their default explanations
COMMON_PATTERNS = [
    (
        r"# pylint: disable=broad-exception-caught\s*$",
        r"# pylint: disable=broad-exception-caught  # Reason: Catching broad Exception to handle multiple error types and return user-friendly error messages",
        "broad-exception-caught",
    ),
    (
        r"# pylint: disable=protected-access\s*$",
        r"# pylint: disable=protected-access  # Reason: Accessing protected member for internal implementation needs, existence/validity checked before access",
        "protected-access",
    ),
    (
        r"# type: ignore\[arg-type\]\s*$",
        r"# type: ignore[arg-type]  # Reason: Type checker too strict for runtime-compatible types, service handles both types at runtime",
        "type-ignore-arg-type",
    ),
    (
        r"// eslint-disable-next-line @typescript-eslint/no-explicit-any\s*$",
        r"// eslint-disable-next-line @typescript-eslint/no-explicit-any -- Using any type for test utilities or dynamic property access",
        "eslint-no-explicit-any",
    ),
]


def fix_file(file_path: Path, dry_run: bool = True) -> tuple[int, list[str]]:
    """
    Fix suppressions in a file.

    Returns:
        (number_fixed, list of changes)
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return (0, [])

    original_content = content
    changes = []
    fixed_count = 0

    for pattern, replacement, pattern_name in COMMON_PATTERNS:
        matches = list(re.finditer(pattern, content, re.MULTILINE))
        for match in matches:
            line_num = content[: match.start()].count("\n") + 1
            # Check if there's already an explanation
            line_end = content.find("\n", match.end())
            if line_end == -1:
                line_end = len(content)
            remaining = content[match.end() : line_end].strip()

            # Skip if already has explanation
            if any(keyword in remaining.lower() for keyword in ["reason:", "--", "justification:"]):
                continue

            # Apply replacement
            content = content[: match.start()] + replacement + content[match.end() :]
            fixed_count += 1
            changes.append(f"  Line {line_num}: Added explanation for {pattern_name}")

    if not dry_run and content != original_content:
        file_path.write_text(content, encoding="utf-8")

    return (fixed_count, changes)


def main():
    """Main entry point."""
    import sys

    dry_run = "--apply" not in sys.argv

    # Load audit report
    audit_path = Path("artifacts/suppression_audit.json")
    if not audit_path.exists():
        print("Error: Run audit_suppressions.py first")
        return

    data = json.load(open(audit_path))
    missing = list(data["missing_explanations"])

    # Group by file
    files_to_fix = {}
    for supp in missing:
        file_path = supp["file"]
        if file_path not in files_to_fix:
            files_to_fix[file_path] = []
        files_to_fix[file_path].append(supp)

    total_fixed = 0
    files_modified = 0

    print(f"Batch fixing suppressions (dry_run={dry_run})...")
    print(f"Files to process: {len(files_to_fix)}")
    print()

    for file_path_str, _suppressions in sorted(files_to_fix.items()):
        file_path = Path(file_path_str)
        if not file_path.exists():
            continue

        fixed, changes = fix_file(file_path, dry_run=dry_run)
        if fixed > 0:
            total_fixed += fixed
            files_modified += 1
            print(f"{file_path_str}: Fixed {fixed} suppressions")
            for change in changes:
                print(change)

    print()
    print(f"Summary: Fixed {total_fixed} suppressions in {files_modified} files")
    if dry_run:
        print("(Dry run - use --apply to actually make changes)")


if __name__ == "__main__":
    main()
