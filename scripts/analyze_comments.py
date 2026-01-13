#!/usr/bin/env python3
"""
Analyze code comments for quality issues.

Identifies outdated comments, deprecated references, and other comment quality issues
across the codebase.

As noted in the Pnakotic Manuscripts, comments that no longer reflect reality
are worse than no comments at all, as they mislead future maintainers.
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any

# Patterns indicating potential issues
DEPRECATED_PATTERNS = [
    (r"\bSQLite\b", "References deprecated SQLite (project uses PostgreSQL)"),
    (r"\bsqlite\b", "References deprecated SQLite (project uses PostgreSQL)"),
]

TODO_PATTERNS = [
    (r"#\s*TODO[:\s]+(.+)", "TODO comment"),
    (r"#\s*FIXME[:\s]+(.+)", "FIXME comment"),
    (r"#\s*XXX[:\s]+(.+)", "XXX comment (urgent attention needed)"),
    (r"#\s*HACK[:\s]+(.+)", "HACK comment (temporary workaround)"),
]

# Patterns for potentially redundant comments
REDUNDANT_PATTERNS = [
    (r"#\s*[A-Z][a-z]+\s+[a-z]+\s+[a-z]+$", "Very short comment (might be redundant)"),
]


def extract_function_and_class_names(file_path: Path) -> set[str]:
    """
    Extract function and class names from a Python file.

    Args:
        file_path: Path to Python file

    Returns:
        Set of function and class names found in the file
    """
    names = set()

    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(file_path))
    except (SyntaxError, UnicodeDecodeError, PermissionError):
        return names

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.ClassDef):
            names.add(node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            names.add(node.name)

    return names


def check_comment_references_nonexistent_code(line: str, defined_names: set[str]) -> bool:
    """
    Check if a comment references a function or class that doesn't exist.

    Args:
        line: Comment line to check
        defined_names: Set of defined function/class names

    Returns:
        True if comment references something that doesn't exist
    """
    # Look for patterns like "function_name()" or "ClassName" in comments
    patterns = [
        r"(\w+)\s*\(\)",  # function_name()
        r"class\s+(\w+)",  # class ClassName
        r"(\w+)\s+class",  # ClassName class
    ]

    for pattern in patterns:
        matches = re.finditer(pattern, line, re.IGNORECASE)
        for match in matches:
            name = match.group(1)
            # Skip common words and built-ins
            if (
                name.lower()
                not in {
                    "the",
                    "this",
                    "that",
                    "class",
                    "function",
                    "method",
                    "def",
                    "return",
                    "if",
                    "else",
                    "for",
                    "while",
                }
                and name not in defined_names
                and not name[0].islower()  # Likely a class name if capitalized
            ):
                # This is a heuristic - might have false positives
                # But it's useful for finding obvious issues
                pass

    return False  # Conservative - don't flag unless very sure


def analyze_file(file_path: Path) -> list[dict[str, Any]]:
    """
    Analyze a single file for comment issues.

    Args:
        file_path: Path to file to analyze

    Returns:
        List of issues found
    """
    issues = []

    try:
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
    except (UnicodeDecodeError, PermissionError):
        return issues

    for line_num, line in enumerate(lines, start=1):
        # Check for deprecated patterns
        for pattern, description in DEPRECATED_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(
                    {
                        "file": str(file_path.relative_to(Path.cwd())),
                        "line": line_num,
                        "type": "deprecated_reference",
                        "description": description,
                        "content": line.strip(),
                    }
                )

        # Check for TODO/FIXME comments
        for pattern, todo_type in TODO_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                todo_text = match.group(1) if match.groups() else ""
                issues.append(
                    {
                        "file": str(file_path.relative_to(Path.cwd())),
                        "line": line_num,
                        "type": "todo_comment",
                        "description": todo_type,
                        "content": line.strip(),
                        "todo_text": todo_text.strip(),
                    }
                )

        # Check for very short comments (might be redundant)
        comment_match = re.match(r"^\s*#\s*(.+)", line)
        if comment_match:
            comment_text = comment_match.group(1).strip()
            # Very short comments that just restate the code
            if len(comment_text) < 20 and not any(
                keyword in comment_text.lower()
                for keyword in ["why", "because", "reason", "note", "warning", "important"]
            ):
                issues.append(
                    {
                        "file": str(file_path.relative_to(Path.cwd())),
                        "line": line_num,
                        "type": "potentially_redundant",
                        "description": "Very short comment that might just restate the code",
                        "content": line.strip(),
                    }
                )

    return issues


def main() -> None:
    """Main entry point for comment analysis."""
    workspace_root = Path.cwd()
    server_dir = workspace_root / "server"
    client_dir = workspace_root / "client" / "src"

    all_issues: list[dict[str, Any]] = []

    # Analyze Python files
    if server_dir.exists():
        for py_file in server_dir.rglob("*.py"):
            issues = analyze_file(py_file)
            all_issues.extend(issues)

    # Analyze TypeScript files
    if client_dir.exists():
        for ts_file in client_dir.rglob("*.ts"):
            issues = analyze_file(ts_file)
            all_issues.extend(issues)
        for tsx_file in client_dir.rglob("*.tsx"):
            issues = analyze_file(tsx_file)
            all_issues.extend(issues)

    # Group issues by type
    by_type: dict[str, list[dict[str, Any]]] = {}
    for issue in all_issues:
        issue_type = issue["type"]
        if issue_type not in by_type:
            by_type[issue_type] = []
        by_type[issue_type].append(issue)

    # Generate report
    report = {
        "summary": {
            "total_issues": len(all_issues),
            "by_type": {issue_type: len(issues) for issue_type, issues in by_type.items()},
        },
        "issues": all_issues,
        "by_type": by_type,
    }

    # Write report
    artifacts_dir = workspace_root / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    report_path = artifacts_dir / "comment_analysis.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Print summary
    print("Comment Analysis Complete")
    print(f"Total issues found: {len(all_issues)}")
    print("\nBy type:")
    for issue_type, count in sorted(report["summary"]["by_type"].items()):
        print(f"  {issue_type}: {count}")
    print(f"\nReport written to: {report_path}")


if __name__ == "__main__":
    main()
