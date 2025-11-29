#!/usr/bin/env python3
"""
Enhanced Logging Compliance Verification Script

This script verifies that all server production code uses the enhanced logging system
as required by .cursor/rules/structlog.mdc and the project's logging standards.

As documented in the restricted archives of Miskatonic University, proper logging
is the foundation upon which all system observability and debugging capabilities rest.
"""

import ast
import re
import sys
from pathlib import Path

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


class LoggingComplianceChecker(ast.NodeVisitor):
    """AST visitor to check logging compliance."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.violations: list[tuple[int, str, str]] = []  # (line, type, message)
        self.uses_enhanced_logging = False
        self.has_logger = False
        self.imports_logging = False

    def visit_Import(self, node: ast.Import) -> None:
        """Check for deprecated logging imports."""
        for alias in node.names:
            if alias.name == "logging":
                # Check if this is an allowed exception (logging module itself or formatter)
                if "logging" not in str(self.file_path):
                    # Only violation if not in logging module directory
                    self.violations.append(
                        (
                            node.lineno,
                            "FORBIDDEN_IMPORT",
                            "Found 'import logging' - Use 'from server.logging.enhanced_logging_config import get_logger' instead",
                        )
                    )
                    self.imports_logging = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Check for deprecated logging imports and verify enhanced logging usage."""
        if node.module == "logging":
            # Direct imports from logging module (forbidden)
            if "logging" not in str(self.file_path):
                self.violations.append(
                    (
                        node.lineno,
                        "FORBIDDEN_IMPORT",
                        "Found 'from logging import ...' - Use 'from server.logging.enhanced_logging_config import get_logger' instead",
                    )
                )
                self.imports_logging = True
        elif node.module and "enhanced_logging_config" in node.module:
            # Check if importing get_logger
            for alias in node.names:
                if alias.name == "get_logger":
                    self.uses_enhanced_logging = True
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        """Check for deprecated logging.getLogger() calls and f-string logging."""
        # Check for logging.getLogger() calls
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "logging":
                if node.func.attr == "getLogger":
                    if "logging" not in str(self.file_path) and "test" not in str(self.file_path):
                        self.violations.append(
                            (
                                node.lineno,
                                "FORBIDDEN_GETLOGGER",
                                "Found 'logging.getLogger()' - Use 'get_logger()' from enhanced_logging_config instead",
                            )
                        )

        # Check for f-string logging patterns
        if isinstance(node.func, ast.Attribute) and node.func.attr in [
            "info",
            "debug",
            "warning",
            "error",
            "critical",
            "exception",
        ]:
            # Check if this is a logger call
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "logger":
                # Check for f-string in first argument
                if node.args and isinstance(node.args[0], ast.JoinedStr):
                    self.violations.append(
                        (
                            node.lineno,
                            "FSTRING_LOGGING",
                            "Found f-string in logger call - Use structured logging with key-value pairs instead",
                        )
                    )

        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        """Check for logger assignment patterns."""
        # Check if assigning logger = logging.getLogger(...)
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "logger":
                self.has_logger = True
                if isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Attribute):
                        if (
                            isinstance(node.value.func.value, ast.Name)
                            and node.value.func.value.id == "logging"
                            and node.value.func.attr == "getLogger"
                        ):
                            if "logging" not in str(self.file_path) and "test" not in str(self.file_path):
                                self.violations.append(
                                    (
                                        node.lineno,
                                        "FORBIDDEN_LOGGER_ASSIGNMENT",
                                        "Found 'logger = logging.getLogger(...)' - Use 'logger = get_logger(__name__)' instead",
                                    )
                                )
        self.generic_visit(node)


def check_file(file_path: Path) -> tuple[bool, list[tuple[int, str, str]]]:
    """
    Check a single file for logging compliance.

    Args:
        file_path: Path to the Python file to check

    Returns:
        Tuple of (is_compliant, violations)
    """
    # Skip test files and logging infrastructure
    if "test" in str(file_path) or "__pycache__" in str(file_path):
        return True, []

    # Skip if file doesn't exist or isn't Python
    if not file_path.exists() or file_path.suffix != ".py":
        return True, []

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return True, []

    # Skip empty files
    if not content.strip():
        return True, []

    try:
        tree = ast.parse(content, filename=str(file_path))
    except SyntaxError:
        # Skip files with syntax errors (they'll be caught by other tools)
        return True, []

    checker = LoggingComplianceChecker(file_path)
    checker.visit(tree)

    # Additional regex checks for patterns AST might miss
    lines = content.split("\n")
    for line_num, line in enumerate(lines, 1):
        # Check for f-string logging patterns
        if re.search(r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']', line):
            if "logging/README.md" not in str(file_path):  # Skip README examples
                checker.violations.append(
                    (
                        line_num,
                        "FSTRING_LOGGING",
                        f"Found f-string in logger call: {line.strip()[:80]}",
                    )
                )

    return len(checker.violations) == 0, checker.violations


def main():
    """Main function to check all server files for logging compliance."""
    project_root = Path(__file__).parent.parent
    server_dir = project_root / "server"

    if not server_dir.exists():
        print(f"{RED}Error: server directory not found at {server_dir}{RESET}")
        sys.exit(1)

    print(f"{BOLD}Enhanced Logging Compliance Verification{RESET}")
    print("=" * 60)
    print()

    # Find all Python files in server directory (excluding tests)
    python_files = []
    for py_file in server_dir.rglob("*.py"):
        # Skip test files
        if "test" in str(py_file) or "__pycache__" in str(py_file):
            continue
        python_files.append(py_file)

    print(f"Checking {len(python_files)} production files...")
    print()

    all_violations: dict[Path, list[tuple[int, str, str]]] = {}
    compliant_files = 0

    for file_path in sorted(python_files):
        is_compliant, violations = check_file(file_path)
        if violations:
            all_violations[file_path] = violations
        else:
            compliant_files += 1

    # Report results
    if all_violations:
        print(f"{RED}{BOLD}VIOLATIONS FOUND{RESET}")
        print("=" * 60)
        print()

        total_violations = sum(len(v) for v in all_violations.values())
        print(f"Found {total_violations} violation(s) in {len(all_violations)} file(s):")
        print()

        for file_path, violations in sorted(all_violations.items()):
            rel_path = file_path.relative_to(project_root)
            print(f"{YELLOW}File: {rel_path}{RESET}")
            print("-" * 60)

            # Group violations by type
            by_type: dict[str, list[tuple[int, str, str]]] = {}
            for line_num, violation_type, message in violations:
                if violation_type not in by_type:
                    by_type[violation_type] = []
                by_type[violation_type].append((line_num, violation_type, message))

            for violation_type in sorted(by_type.keys()):
                print(f"  {RED}{violation_type}:{RESET}")
                for line_num, _, message in by_type[violation_type]:
                    print(f"    Line {line_num}: {message}")
            print()

        print(f"{RED}COMPLIANCE FAILED{RESET}")
        print(f"Compliant files: {compliant_files}/{len(python_files)}")
        print()
        print("HOW TO FIX:")
        print("1. Replace 'import logging' with 'from server.logging.enhanced_logging_config import get_logger'")
        print("2. Replace 'logging.getLogger(__name__)' with 'get_logger(__name__)'")
        print("3. Replace f-string logging with structured key-value pairs")
        print("   WRONG: logger.info(f\"User {user_id} performed {action}\")")
        print("   RIGHT: logger.info(\"User action\", user_id=user_id, action=action)")
        print()
        print("See .cursor/rules/structlog.mdc and docs/LOGGING_BEST_PRACTICES.md for details.")
        sys.exit(1)
    else:
        print(f"{GREEN}{BOLD}ALL FILES COMPLIANT{RESET}")
        print("=" * 60)
        print()
        print(f"All {compliant_files} production files use enhanced logging system")
        print()
        sys.exit(0)


if __name__ == "__main__":
    main()
