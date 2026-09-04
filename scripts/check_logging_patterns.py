#!/usr/bin/env python3
"""
Pre-commit hook to detect f-string logging violations.

This script scans Python files for f-string usage in logger calls,
which destroys structured logging benefits and must be eliminated.

As noted in the Pnakotic Manuscripts, proper documentation of our
eldritch systems requires structured data for effective analysis.
"""

import ast
import sys
from pathlib import Path


class FStringLoggingDetector(ast.NodeVisitor):
    """AST visitor to detect f-string logging violations."""

    def __init__(self, file_path: Path, source_lines: list[str]):
        self.file_path = file_path
        self.source_lines = source_lines
        self.violations: list[tuple[int, str, str]] = []

    def visit_Call(self, node: ast.Call) -> None:
        """Check for f-string logging patterns."""
        # Check if this is a logger method call
        if isinstance(node.func, ast.Attribute):
            # Check if it's logger.info, logger.error, etc.
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "logger":
                if node.func.attr in ["info", "debug", "warning", "error", "critical", "exception"]:
                    # Check for f-string in first argument
                    if node.args and isinstance(node.args[0], ast.JoinedStr):
                        # This is an f-string - violation!
                        line_num = node.lineno
                        line_content = self.source_lines[line_num - 1].strip() if line_num <= len(self.source_lines) else ""

                        # Get method name for suggestion
                        method = node.func.attr
                        suggested_fix = (
                            f'logger.{method}("message", key=value)  '
                            f"# Replace f-string with structured logging"
                        )

                        self.violations.append((line_num, line_content, suggested_fix))

        self.generic_visit(node)


def find_fstring_logging_violations(file_path: Path) -> list[tuple[int, str, str]]:
    """
    Find f-string logging violations in a Python file using AST parsing.

    This method uses AST to detect f-strings in logger calls, which allows
    it to catch multi-line f-strings that regex patterns would miss.

    Args:
        file_path: Path to the Python file to scan

    Returns:
        List of tuples (line_number, line_content, suggested_fix)
    """
    violations = []

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
            source_lines = content.split("\n")
    except (UnicodeDecodeError, FileNotFoundError):
        return violations

    # Skip empty files
    if not content.strip():
        return violations

    # Skip test files and documentation examples
    file_path_str = str(file_path)
    if "test" in file_path_str or "docs/examples/logging" in file_path_str:
        return violations

    try:
        tree = ast.parse(content, filename=str(file_path))
    except SyntaxError:
        # Skip files with syntax errors (they'll be caught by other tools)
        return violations

    # Use AST visitor to detect violations
    detector = FStringLoggingDetector(file_path, source_lines)
    detector.visit(tree)

    return detector.violations


def format_violation_report(violations: list[tuple[str, list[tuple[int, str, str]]]]) -> str:
    """
    Format violation report for display.

    Args:
        violations: List of (file_path, violations) tuples

    Returns:
        Formatted report string
    """
    if not violations:
        return "No f-string logging violations found!"

    report = []
    report.append("F-STRING LOGGING VIOLATIONS DETECTED")
    report.append("=" * 50)
    report.append("")
    report.append("F-string logging destroys structured logging benefits:")
    report.append("- Breaks log aggregation and search")
    report.append("- Prevents automated alerting")
    report.append("- Reduces performance")
    report.append("- Makes debugging harder")
    report.append("")

    total_violations = 0
    for file_path, file_violations in violations:
        if file_violations:
            total_violations += len(file_violations)
            report.append(f"File: {file_path}")
            report.append("-" * 40)

            for line_num, line_content, suggestion in file_violations:
                report.append(f"  Line {line_num}: {line_content}")
                report.append(f"  Fix: {suggestion}")
                report.append("")

    report.append(f"Total violations: {total_violations}")
    report.append("")
    report.append("HOW TO FIX:")
    report.append("Replace f-strings with structured logging:")
    report.append("  WRONG: Using f-strings in logger calls")
    report.append('  CORRECT: logger.info("User action", user_id=user_id, action=action)')
    report.append("")
    report.append("See .cursorrules for complete examples and patterns.")

    return "\n".join(report)


def main():
    """Main function to scan files and report violations."""
    if len(sys.argv) < 2:
        print("Usage: python check_logging_patterns.py <file1> [file2] ...")
        sys.exit(1)

    files_to_scan = [Path(f) for f in sys.argv[1:]]
    all_violations = []

    for file_path in files_to_scan:
        if not file_path.exists():
            print(f"Warning: File {file_path} does not exist")
            continue

        if not file_path.suffix == ".py":
            continue

        violations = find_fstring_logging_violations(file_path)
        if violations:
            all_violations.append((str(file_path), violations))

    # Format and display report using console-safe encoding
    report = format_violation_report(all_violations)
    try:
        encoding = sys.stdout.encoding or "utf-8"
        sys.stdout.buffer.write((report + "\n").encode(encoding, errors="replace"))
    except Exception:
        # Fallback to ASCII-safe output
        print(report.encode("ascii", errors="replace").decode("ascii"))

    # Exit with error code if violations found
    if all_violations:
        print("\nPre-commit hook failed: F-string logging violations detected")
        print("Fix these violations before committing.")
        sys.exit(1)
    else:
        print("\nPre-commit hook passed: No f-string logging violations")
        sys.exit(0)


if __name__ == "__main__":
    main()
