#!/usr/bin/env python3
"""
Verify that inline suppressions are aligned between ruff and pylint.

This script scans Python files for inline suppressions (# pylint: disable and # noqa)
and identifies cases where:
1. A pylint suppression exists but no equivalent ruff suppression
2. A ruff suppression exists but no equivalent pylint suppression

It uses the rule mapping from docs/LINTING_RUFF_PYLINT_MAPPING.md to determine
which rules are equivalent.
"""

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Rule mappings: pylint rule -> ruff rule(s)
# Based on docs/LINTING_RUFF_PYLINT_MAPPING.md
PYLINT_TO_RUFF_MAPPING: dict[str, list[str]] = {
    # Convention
    "line-too-long": ["E501"],  # C0301
    "too-many-lines": [],  # C0302 - no ruff equivalent
    "invalid-name": [],  # C0103 - no ruff equivalent
    "missing-module-docstring": [],  # C0114 - no ruff equivalent
    "missing-function-docstring": [],  # C0116 - no ruff equivalent
    "wrong-import-position": ["E402"],  # C0413
    "import-outside-toplevel": [],  # C0415 - globally disabled, no ruff equivalent
    "use-implicit-booleaness-not-comparison-to-zero": [],  # C1805 - no ruff equivalent
    "use-implicit-booleaness-not-comparison-to-string": [],  # C1804 - no ruff equivalent
    "singleton-comparison": [],  # C0121 - no ruff equivalent
    # Errors
    "no-name-in-module": [],  # E0611 - no ruff equivalent (ruff doesn't check imports this way)
    "undefined-variable": ["F821"],  # E0602
    # Warnings
    "unused-import": ["F401"],  # W0611
    "unused-variable": ["F841"],  # W0612
    "unused-argument": [],  # W0613 - no ruff equivalent
    "redefined-outer-name": ["F811"],  # W0621
    "redefined-builtin": ["F811"],  # W0622
    "raise-missing-from": ["B904"],  # W0707 - similar but not identical
    "broad-exception-caught": ["B904"],  # W0701 - similar but not identical
    "global-statement": [],  # W0603 - no ruff equivalent
    "global-variable-not-assigned": [],  # W0602 - no ruff equivalent
    "protected-access": [],  # W0212 - no ruff equivalent
    # Refactor
    "too-many-instance-attributes": [],  # R0902 - no ruff equivalent
    "too-many-locals": [],  # R0914 - no ruff equivalent
    "too-many-arguments": [],  # R0913 - no ruff equivalent
    "too-many-positional-arguments": [],  # R0917 - no ruff equivalent
    "too-many-public-methods": [],  # R0904 - no ruff equivalent
    "too-many-statements": [],  # R0915 - no ruff equivalent
    "too-many-return-statements": [],  # R0911 - no ruff equivalent
    "too-many-branches": [],  # R0912 - no ruff equivalent
    "too-many-nested-blocks": [],  # R1702 - no ruff equivalent
    "no-else-return": [],  # R1705 - no ruff equivalent
    "no-else-raise": [],  # R1720 - no ruff equivalent
    "too-few-public-methods": [],  # R0903 - no ruff equivalent
    "consider-using-in": [],  # R1714 - no ruff equivalent
    # Other
    "no-member": [],  # E1101 - no ruff equivalent (type checking)
}

# Reverse mapping: ruff rule -> pylint rule(s)
RUFF_TO_PYLINT_MAPPING: dict[str, list[str]] = {}
for pylint_rule, ruff_rules in PYLINT_TO_RUFF_MAPPING.items():
    for ruff_rule in ruff_rules:
        if ruff_rule not in RUFF_TO_PYLINT_MAPPING:
            RUFF_TO_PYLINT_MAPPING[ruff_rule] = []
        RUFF_TO_PYLINT_MAPPING[ruff_rule].append(pylint_rule)


@dataclass
class Suppression:
    """Represents an inline suppression."""

    file_path: Path
    line_number: int
    tool: str  # 'pylint' or 'ruff'
    rules: list[str]
    full_line: str


def parse_pylint_suppression(line: str, file_path: Path, line_num: int) -> Suppression | None:
    """Parse a pylint disable comment."""
    # Pattern: # pylint: disable=rule1,rule2,rule3
    # Also handles: # pylint: disable=rule1  # Reason: ...
    pattern = r"#\s*pylint:\s*disable=([^\s#]+)"
    match = re.search(pattern, line)
    if not match:
        return None

    rules_str = match.group(1)
    rules = [r.strip() for r in rules_str.split(",") if r.strip()]

    return Suppression(
        file_path=file_path,
        line_number=line_num,
        tool="pylint",
        rules=rules,
        full_line=line.strip(),
    )


def parse_ruff_suppression(line: str, file_path: Path, line_num: int) -> Suppression | None:
    """Parse a ruff noqa comment.

    Pattern examples:
    - # noqa: E501,F401
    - # noqa: E501  # Reason: ...
    """
    pattern = r"#\s*noqa(?::\s*([A-Z0-9]+(?:,[A-Z0-9]+)*))?"
    match = re.search(pattern, line)
    if not match:
        return None

    rules_str = match.group(1) or ""
    if not rules_str:
        # # noqa without specific rules means "ignore all"
        return Suppression(
            file_path=file_path,
            line_number=line_num,
            tool="ruff",
            rules=["*"],  # Special marker for "all rules"
            full_line=line.strip(),
        )

    rules = [r.strip() for r in rules_str.split(",") if r.strip()]
    return Suppression(
        file_path=file_path,
        line_number=line_num,
        tool="ruff",
        rules=rules,
        full_line=line.strip(),
    )


def find_suppressions(file_path: Path) -> list[Suppression]:
    """Find all suppressions in a file."""
    suppressions: list[Suppression] = []

    try:
        with file_path.open(encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                # Check for pylint suppressions
                pylint_supp = parse_pylint_suppression(line, file_path, line_num)
                if pylint_supp:
                    suppressions.append(pylint_supp)

                # Check for ruff suppressions
                ruff_supp = parse_ruff_suppression(line, file_path, line_num)
                if ruff_supp:
                    suppressions.append(ruff_supp)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return suppressions


def _has_ruff_equivalent(ruff_supps: list[Suppression], ruff_equivalents: list[str]) -> bool:
    """Check if any ruff suppression covers the given rules."""
    for ruff_supp in ruff_supps:
        if "*" in ruff_supp.rules:
            return True
        if any(rule in ruff_supp.rules for rule in ruff_equivalents):
            return True
    return False


def _has_pylint_equivalent(pylint_supps: list[Suppression], pylint_equivalents: list[str]) -> bool:
    """Check if any pylint suppression covers the given rules."""
    for pylint_supp in pylint_supps:
        if any(rule in pylint_supp.rules for rule in pylint_equivalents):
            return True
    return False


def _check_pylint_suppressions(
    pylint_supps: list[Suppression],
    ruff_supps: list[Suppression],
    file_path: Path,
    line_num: int,
) -> list[dict[str, Any]]:
    """Check if pylint suppressions have ruff equivalents."""
    misaligned: list[dict[str, Any]] = []

    for pylint_supp in pylint_supps:
        for pylint_rule in pylint_supp.rules:
            ruff_equivalents = PYLINT_TO_RUFF_MAPPING.get(pylint_rule, [])

            if not ruff_equivalents:
                # No ruff equivalent - this is fine, just document it
                continue

            if not _has_ruff_equivalent(ruff_supps, ruff_equivalents):
                misaligned.append(
                    {
                        "file": str(file_path),
                        "line": line_num,
                        "issue": "missing_ruff",
                        "pylint_rule": pylint_rule,
                        "ruff_equivalents": ruff_equivalents,
                        "line_content": pylint_supp.full_line,
                    }
                )

    return misaligned


def _check_ruff_suppressions(
    ruff_supps: list[Suppression],
    pylint_supps: list[Suppression],
    file_path: Path,
    line_num: int,
) -> list[dict[str, Any]]:
    """Check if ruff suppressions have pylint equivalents."""
    misaligned: list[dict[str, Any]] = []

    for ruff_supp in ruff_supps:
        if "*" in ruff_supp.rules:
            # # noqa without specific rules - check if there's a pylint suppression
            if not pylint_supps:
                misaligned.append(
                    {
                        "file": str(file_path),
                        "line": line_num,
                        "issue": "missing_pylint_general",
                        "ruff_rule": "*",
                        "pylint_equivalents": [],
                        "line_content": ruff_supp.full_line,
                    }
                )
            continue

        for ruff_rule in ruff_supp.rules:
            pylint_equivalents = RUFF_TO_PYLINT_MAPPING.get(ruff_rule, [])

            if not pylint_equivalents:
                # No pylint equivalent - this is fine
                continue

            if not _has_pylint_equivalent(pylint_supps, pylint_equivalents):
                misaligned.append(
                    {
                        "file": str(file_path),
                        "line": line_num,
                        "issue": "missing_pylint",
                        "ruff_rule": ruff_rule,
                        "pylint_equivalents": pylint_equivalents,
                        "line_content": ruff_supp.full_line,
                    }
                )

    return misaligned


def check_alignment(suppressions: list[Suppression]) -> dict[str, Any]:
    """Check if suppressions are aligned between tools."""
    # Group by file and line
    by_location: dict[tuple[Path, int], list[Suppression]] = defaultdict(list)
    for supp in suppressions:
        by_location[(supp.file_path, supp.line_number)].append(supp)

    misaligned: list[dict[str, Any]] = []

    for (file_path, line_num), loc_suppressions in by_location.items():
        pylint_supps = [s for s in loc_suppressions if s.tool == "pylint"]
        ruff_supps = [s for s in loc_suppressions if s.tool == "ruff"]

        # Check each pylint suppression
        misaligned.extend(_check_pylint_suppressions(pylint_supps, ruff_supps, file_path, line_num))

        # Check each ruff suppression
        misaligned.extend(_check_ruff_suppressions(ruff_supps, pylint_supps, file_path, line_num))

    return {"misaligned": misaligned, "total_suppressions": len(suppressions)}


def _scan_files_for_suppressions(server_dir: Path) -> list[Suppression]:
    """Scan all Python files in server directory for suppressions."""
    all_suppressions: list[Suppression] = []

    # Find all Python files
    for py_file in server_dir.rglob("*.py"):
        # Skip test files for now (can add later)
        if "test" in str(py_file):
            continue

        suppressions = find_suppressions(py_file)
        all_suppressions.extend(suppressions)

    return all_suppressions


def _print_misaligned_summary(by_issue: dict[str, list[dict[str, Any]]]) -> None:
    """Print summary of misaligned suppressions to console."""
    print("\n=== MISALIGNED SUPPRESSIONS ===")
    for issue_type, items in sorted(by_issue.items()):
        print(f"\n{issue_type.upper().replace('_', ' ')} ({len(items)}):")
        for item in items[:20]:  # Show first 20
            print(f"  {item['file']}:{item['line']}")
            print(f"    {item['line_content']}")
            if item["issue"] == "missing_ruff":
                print(f"    Missing ruff: {', '.join(item['ruff_equivalents'])}")
            elif item["issue"] == "missing_pylint":
                print(f"    Missing pylint: {', '.join(item['pylint_equivalents'])}")
        if len(items) > 20:
            print(f"    ... and {len(items) - 20} more")


def _write_detailed_report(
    report_path: Path, results: dict[str, Any], by_issue: dict[str, list[dict[str, Any]]]
) -> None:
    """Write detailed report to file."""
    with report_path.open("w", encoding="utf-8") as f:
        f.write("LINTING SUPPRESSION ALIGNMENT REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total suppressions found: {results['total_suppressions']}\n")
        f.write(f"Misaligned suppressions: {len(results['misaligned'])}\n\n")

        for issue_type, items in sorted(by_issue.items()):
            f.write(f"\n{issue_type.upper().replace('_', ' ')} ({len(items)}):\n")
            f.write("-" * 80 + "\n")
            for item in items:
                f.write(f"{item['file']}:{item['line']}\n")
                f.write(f"  {item['line_content']}\n")
                if item["issue"] == "missing_ruff":
                    f.write(f"  Missing ruff rules: {', '.join(item['ruff_equivalents'])}\n")
                elif item["issue"] == "missing_pylint":
                    f.write(f"  Missing pylint rules: {', '.join(item['pylint_equivalents'])}\n")
                f.write("\n")


def main() -> None:
    """Main entry point."""
    server_dir = Path("server")
    if not server_dir.exists():
        print("Error: server/ directory not found")
        return

    print("Scanning for inline suppressions...")
    all_suppressions = _scan_files_for_suppressions(server_dir)

    print(f"Found {len(all_suppressions)} total suppressions")

    # Check alignment
    results = check_alignment(all_suppressions)

    misaligned = results["misaligned"]
    print(f"\nFound {len(misaligned)} misaligned suppressions")

    # Group by issue type
    by_issue = defaultdict(list)
    for item in misaligned:
        by_issue[item["issue"]].append(item)

    _print_misaligned_summary(by_issue)

    # Save detailed report
    report_path = Path("linting_suppression_alignment_report.txt")
    _write_detailed_report(report_path, results, by_issue)

    print(f"\nDetailed report saved to: {report_path}")


if __name__ == "__main__":
    main()
