#!/usr/bin/env python3
"""
Automatically fix misaligned inline suppressions between ruff and pylint.

This script reads the suppression alignment report and automatically adds
missing suppressions while preserving existing comments and reasons.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# Mapping: pylint rule -> ruff rule
COMMON_MAPPINGS = {
    "broad-exception-caught": "B904",
    "redefined-outer-name": "F811",
    "wrong-import-position": "E402",
    "unused-import": "F401",
    "unused-variable": "F841",
}

# Reverse mapping for the other direction
RUFF_TO_PYLINT = {
    "B904": "broad-exception-caught",
    "F811": "redefined-outer-name",
    "E402": "wrong-import-position",
    "F401": "unused-import",
    "F841": "unused-variable",
}


def _parse_issue_type_header(line: str) -> str | None:
    """Parse issue type header (MISSING RUFF or MISSING PYLINT)."""
    if line.startswith("MISSING"):
        if "RUFF" in line:
            return "missing_ruff"
        if "PYLINT" in line:
            return "missing_pylint"
    return None


def _parse_file_line_pattern(line: str) -> tuple[str, int] | None:
    """Parse file:line pattern from a line. Returns (file, line) or None."""
    if ":" not in line or line.startswith("  "):
        return None

    parts = line.split(":")
    if len(parts) < 2:
        return None

    try:
        potential_file = parts[0]
        potential_line = int(parts[1])
        # Validate that it looks like a file path (ends with .py)
        if potential_file.endswith(".py"):
            return (potential_file, potential_line)
    except (ValueError, IndexError):
        pass

    return None


def _parse_missing_rules(
    line: str, current_file: str | None, current_line: int | None, current_issue: str | None
) -> dict[str, Any] | None:
    """Parse missing rules from a line. Returns misaligned dict or None."""
    if not line.startswith("Missing") or not current_file or not current_line:
        return None

    line_lower = line.lower()
    if "ruff" in line_lower:
        # Extract ruff rules
        match = re.search(r"ruff rules?:\s*([A-Z0-9,]+)", line)
        if match:
            ruff_rules = [r.strip() for r in match.group(1).split(",")]
            return {
                "file": current_file,
                "line": current_line,
                "issue": current_issue,
                "missing_rules": ruff_rules,
            }
    elif "pylint" in line_lower:
        # Extract pylint rules
        match = re.search(r"pylint rules?:\s*([a-z-]+(?:,[a-z-]+)*)", line)
        if match:
            pylint_rules = [r.strip() for r in match.group(1).split(",")]
            return {
                "file": current_file,
                "line": current_line,
                "issue": current_issue,
                "missing_rules": pylint_rules,
            }

    return None


def parse_alignment_report(report_path: Path) -> list[dict[str, Any]]:
    """Parse the alignment report to extract misaligned suppressions."""
    misaligned: list[dict[str, Any]] = []

    if not report_path.exists():
        print(f"Error: Report file not found: {report_path}")
        return misaligned

    current_issue = None
    current_file = None
    current_line = None

    with report_path.open(encoding="utf-8") as f:
        for _line_num, line in enumerate(f, 1):
            line = line.strip()

            # Check for issue type header
            issue_type = _parse_issue_type_header(line)
            if issue_type:
                current_issue = issue_type
                continue

            # Check for file:line pattern
            file_line = _parse_file_line_pattern(line)
            if file_line:
                current_file, current_line = file_line
                continue

            # Check for missing rules
            missing_entry = _parse_missing_rules(line, current_file, current_line, current_issue)
            if missing_entry:
                misaligned.append(missing_entry)

    return misaligned


def add_ruff_suppression(line: str, ruff_rules: list[str]) -> str:
    """Add ruff noqa comment to a line that has pylint disable."""
    # Check if line already has noqa
    if "# noqa" in line.lower():
        # Check if the rules are already there
        noqa_match = re.search(r"#\s*noqa(?::\s*([A-Z0-9,]+))?", line, re.IGNORECASE)
        if noqa_match:
            existing_rules_str = noqa_match.group(1) or ""
            existing_rules = [r.strip() for r in existing_rules_str.split(",") if r.strip()]
            # Add missing rules
            all_rules = set(existing_rules) | set(ruff_rules)
            if all_rules == set(existing_rules):
                # All rules already present
                return line

            # Replace existing noqa
            new_rules_str = ",".join(sorted(all_rules))
            return re.sub(
                r"#\s*noqa(?::\s*[A-Z0-9,]+)?",
                f"# noqa: {new_rules_str}",
                line,
                flags=re.IGNORECASE,
            )

    # Add new noqa comment
    ruff_rules_str = ",".join(sorted(ruff_rules))
    # Try to preserve existing comments
    if "# Reason:" in line or "# pragma:" in line:
        # Insert before reason/pragma
        return re.sub(
            r"(#\s*(?:Reason|pragma):)",
            f"# noqa: {ruff_rules_str}  \\1",
            line,
        )
    else:
        # Append at the end
        return f"{line.rstrip()}  # noqa: {ruff_rules_str}"


def add_pylint_suppression(line: str, pylint_rules: list[str]) -> str:
    """Add pylint disable comment to a line that has noqa."""
    # Check if line already has pylint disable
    if "# pylint:" in line.lower():
        # Check if the rules are already there
        pylint_match = re.search(r"#\s*pylint:\s*disable=([^\s#]+)", line, re.IGNORECASE)
        if pylint_match:
            existing_rules_str = pylint_match.group(1)
            existing_rules = [r.strip() for r in existing_rules_str.split(",") if r.strip()]
            # Add missing rules
            all_rules = set(existing_rules) | set(pylint_rules)
            if all_rules == set(existing_rules):
                # All rules already present
                return line

            # Replace existing pylint disable
            new_rules_str = ",".join(sorted(all_rules))
            return re.sub(
                r"#\s*pylint:\s*disable=[^\s#]+",
                f"# pylint: disable={new_rules_str}",
                line,
                flags=re.IGNORECASE,
            )

    # Add new pylint disable comment
    pylint_rules_str = ",".join(sorted(pylint_rules))
    # Try to preserve existing comments
    if "# Reason:" in line or "# pragma:" in line:
        # Insert before reason/pragma
        return re.sub(
            r"(#\s*(?:Reason|pragma):)",
            f"# pylint: disable={pylint_rules_str}  \\1",
            line,
        )
    else:
        # Append at the end
        return f"{line.rstrip()}  # pylint: disable={pylint_rules_str}"


def _group_fixes_by_line(fixes: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    """Group fixes by line number."""
    fixes_by_line: dict[int, list[dict[str, Any]]] = {}
    for fix in fixes:
        line_num = fix["line"]
        if line_num not in fixes_by_line:
            fixes_by_line[line_num] = []
        fixes_by_line[line_num].append(fix)
    return fixes_by_line


def _apply_fixes_to_line(line: str, fixes: list[dict[str, Any]]) -> str:
    """Apply all fixes for a single line."""
    for fix in fixes:
        if fix["issue"] == "missing_ruff":
            missing_rules = fix["missing_rules"]
            line = add_ruff_suppression(line, missing_rules)
        elif fix["issue"] == "missing_pylint":
            missing_rules = fix["missing_rules"]
            line = add_pylint_suppression(line, missing_rules)
    return line


def fix_file(file_path: Path, fixes: list[dict[str, Any]]) -> bool:
    """Apply fixes to a file."""
    if not file_path.exists():
        print(f"Warning: File not found: {file_path}")
        return False

    # Read file
    try:
        with file_path.open(encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # Group fixes by line number
    fixes_by_line = _group_fixes_by_line(fixes)

    # Apply fixes (process in reverse order to preserve line numbers)
    modified = False
    for line_num in sorted(fixes_by_line.keys(), reverse=True):
        if line_num > len(lines):
            print(f"Warning: Line {line_num} out of range in {file_path}")
            continue

        original_line = lines[line_num - 1]  # Convert to 0-based index
        line = _apply_fixes_to_line(original_line, fixes_by_line[line_num])

        if line != original_line:
            lines[line_num - 1] = line
            modified = True

    # Write file if modified
    if modified:
        try:
            with file_path.open("w", encoding="utf-8") as f:
                f.writelines(lines)
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False

    return False


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Automatically fix misaligned inline suppressions")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation and proceed automatically")
    args = parser.parse_args()

    report_path = Path("linting_suppression_alignment_report.txt")
    if not report_path.exists():
        print("Error: Alignment report not found. Run verify_linting_parity.py first.")
        sys.exit(1)

    print("Parsing alignment report...")
    misaligned = parse_alignment_report(report_path)

    if not misaligned:
        print("No misaligned suppressions found.")
        return

    print(f"Found {len(misaligned)} misaligned suppressions")

    # Group by file
    fixes_by_file: dict[str, list[dict[str, Any]]] = {}
    for item in misaligned:
        file_path = item["file"]
        if file_path not in fixes_by_file:
            fixes_by_file[file_path] = []
        fixes_by_file[file_path].append(item)

    print(f"\nWill fix {len(fixes_by_file)} files")

    # Ask for confirmation unless --yes flag is set
    if not args.yes:
        try:
            response = input("\nProceed with automatic fixes? (yes/no): ").strip().lower()
            if response not in ("yes", "y"):
                print("Aborted.")
                return
        except EOFError:
            print("\nNo input available. Use --yes flag to proceed automatically.")
            sys.exit(1)

    # Apply fixes
    fixed_count = 0
    for file_path_str, fixes in fixes_by_file.items():
        file_path = Path(file_path_str)
        if fix_file(file_path, fixes):
            fixed_count += 1
            print(f"Fixed: {file_path}")

    print(f"\nFixed {fixed_count} files")
    print("Please run verify_linting_parity.py again to verify fixes.")


if __name__ == "__main__":
    main()
