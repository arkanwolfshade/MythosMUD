#!/usr/bin/env python3
"""
Audit tool suppressions across the codebase.

Scans all Python and TypeScript files for tool suppressions (pylint, mypy, eslint, etc.)
and identifies which ones have explanations and which ones don't.

As documented in the restricted archives of Miskatonic University, proper documentation
of code suppressions is essential for maintaining code quality and understanding
technical debt.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# Python suppression patterns
PYTHON_PATTERNS = [
    (r"#\s*pylint:\s*disable[=:]\s*([^\n#]+)", "pylint"),
    (r"#\s*type:\s*ignore", "mypy"),
    (r"#\s*type:\s*ignore\[([^\]]+)\]", "mypy"),
    (r"#\s*noqa(?::\s*([^\n#]+))?", "ruff"),
    (r"#\s*mypy:\s*([^\n#]+)", "mypy"),
    (r"#\s*ruff:\s*([^\n#]+)", "ruff"),
]

# TypeScript suppression patterns
TYPESCRIPT_PATTERNS = [
    (r"//\s*eslint-disable(?:-next-line)?(?:\s+([^\n]+))?", "eslint"),
    (r"//\s*@ts-ignore", "typescript"),
    (r"//\s*@ts-expect-error", "typescript"),
]

# Patterns that indicate an explanation exists
EXPLANATION_PATTERNS = [
    r"#\s*Reason:",
    r"#\s*JUSTIFICATION:",
    r"--\s*[A-Z]",  # TypeScript: -- followed by capital letter (common pattern)
    r"#\s*[A-Z][a-z]+",  # Python: # followed by capital letter (likely explanation)
]


def has_explanation(line: str, suppression_end: int) -> bool:
    """
    Check if a suppression line has an explanation.

    Args:
        line: The full line containing the suppression
        suppression_end: Index where the suppression pattern ends

    Returns:
        True if an explanation is found, False otherwise
    """
    remaining = line[suppression_end:].strip()

    # Check for explicit explanation markers
    for pattern in EXPLANATION_PATTERNS:
        if re.search(pattern, remaining, re.IGNORECASE):
            return True

    # Check if there's substantial text after the suppression
    # (more than just whitespace or closing characters)
    text_after = remaining.lstrip("#").lstrip("/").strip()
    if len(text_after) > 10:  # Substantial explanation likely
        return True

    return False


def find_suppressions(file_path: Path, patterns: list[tuple[str, str]]) -> list[dict[str, Any]]:
    """
    Find all suppressions in a file.

    Args:
        file_path: Path to the file to scan
        patterns: List of (pattern, tool_name) tuples

    Returns:
        List of suppression dictionaries
    """
    suppressions = []

    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return suppressions

    for line_num, line in enumerate(content.splitlines(), start=1):
        for pattern, tool_name in patterns:
            for match in re.finditer(pattern, line):
                suppression_end = match.end()
                has_expl = has_explanation(line, suppression_end)

                suppressions.append(
                    {
                        "file": str(file_path.relative_to(Path.cwd())),
                        "line": line_num,
                        "tool": tool_name,
                        "suppression": match.group(0),
                        "has_explanation": has_expl,
                        "full_line": line.strip(),
                    }
                )

    return suppressions


def scan_all_files(workspace_root: Path) -> list[dict[str, Any]]:
    """
    Scan all Python and TypeScript files for suppressions.

    Args:
        workspace_root: Root directory of the workspace

    Returns:
        List of all suppressions found
    """
    server_dir = workspace_root / "server"
    client_dir = workspace_root / "client" / "src"
    all_suppressions: list[dict[str, Any]] = []

    # Scan Python files
    if server_dir.exists():
        for py_file in server_dir.rglob("*.py"):
            suppressions = find_suppressions(py_file, PYTHON_PATTERNS)
            all_suppressions.extend(suppressions)

    # Scan TypeScript files
    if client_dir.exists():
        for ts_file in client_dir.rglob("*.ts"):
            suppressions = find_suppressions(ts_file, TYPESCRIPT_PATTERNS)
            all_suppressions.extend(suppressions)
        for tsx_file in client_dir.rglob("*.tsx"):
            suppressions = find_suppressions(tsx_file, TYPESCRIPT_PATTERNS)
            all_suppressions.extend(suppressions)

    return all_suppressions


def calculate_statistics(all_suppressions: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate summary statistics from suppressions.

    Args:
        all_suppressions: List of all suppressions

    Returns:
        Dictionary with summary statistics
    """
    total = len(all_suppressions)
    with_explanation = sum(1 for s in all_suppressions if s["has_explanation"])
    without_explanation = total - with_explanation

    return {
        "total_suppressions": total,
        "with_explanation": with_explanation,
        "without_explanation": without_explanation,
        "coverage_percent": round((with_explanation / total * 100) if total > 0 else 0, 2),
    }


def group_by_file(all_suppressions: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """
    Group suppressions by file path.

    Args:
        all_suppressions: List of all suppressions

    Returns:
        Dictionary mapping file paths to lists of suppressions
    """
    by_file: dict[str, list[dict[str, Any]]] = {}
    for supp in all_suppressions:
        file_path = supp["file"]
        if file_path not in by_file:
            by_file[file_path] = []
        by_file[file_path].append(supp)
    return by_file


def group_by_tool(all_suppressions: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    """
    Group suppressions by tool and calculate statistics.

    Args:
        all_suppressions: List of all suppressions

    Returns:
        Dictionary mapping tool names to statistics
    """
    by_tool: dict[str, dict[str, int]] = {}
    for supp in all_suppressions:
        tool = supp["tool"]
        if tool not in by_tool:
            by_tool[tool] = {"total": 0, "with_explanation": 0, "without_explanation": 0}
        by_tool[tool]["total"] += 1
        if supp["has_explanation"]:
            by_tool[tool]["with_explanation"] += 1
        else:
            by_tool[tool]["without_explanation"] += 1
    return by_tool


def write_report_file(workspace_root: Path, report: dict[str, Any]) -> Path:
    """
    Write the report to a JSON file.

    Args:
        workspace_root: Root directory of the workspace
        report: Report dictionary to write

    Returns:
        Path to the written report file
    """
    artifacts_dir = workspace_root / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    report_path = artifacts_dir / "suppression_audit.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report_path


def print_summary_report(report: dict[str, Any], report_path: Path) -> None:
    """
    Print the summary report to stdout.

    Args:
        report: Report dictionary
        report_path: Path to the report file
    """
    summary = report["summary"]
    print("Suppression Audit Complete")
    print(f"Total suppressions: {summary['total_suppressions']}")
    print(f"With explanation: {summary['with_explanation']} ({summary['coverage_percent']}%)")
    print(f"Without explanation: {summary['without_explanation']}")
    print(f"\nReport written to: {report_path}")
    print("\nBy tool:")
    for tool, stats in sorted(report["by_tool"].items()):
        print(
            f"  {tool}: {stats['total']} total, {stats['with_explanation']} explained, {stats['without_explanation']} missing"
        )


def main() -> None:
    """Main entry point for the suppression audit."""
    workspace_root = Path.cwd()

    # Scan all files
    all_suppressions = scan_all_files(workspace_root)

    # Calculate statistics and group suppressions
    summary = calculate_statistics(all_suppressions)
    by_file = group_by_file(all_suppressions)
    by_tool = group_by_tool(all_suppressions)

    # Generate report
    report = {
        "summary": summary,
        "by_tool": by_tool,
        "by_file": by_file,
        "missing_explanations": [s for s in all_suppressions if not s["has_explanation"]],
    }

    # Write and print report
    report_path = write_report_file(workspace_root, report)
    print_summary_report(report, report_path)


if __name__ == "__main__":
    main()
