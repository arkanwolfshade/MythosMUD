#!/usr/bin/env python3
"""
Enhanced Logging Pattern Linter

This script validates that all Python files use the enhanced logging system
and don't use deprecated logging patterns.

Usage:
    python scripts/lint_logging_patterns.py
"""

import ast
import sys
from pathlib import Path


class LoggingPatternLinter(ast.NodeVisitor):
    """AST visitor to detect deprecated logging patterns."""

    def __init__(self):
        self.errors: list[tuple[int, str]] = []
        self.imports = {}
        self.uses_enhanced_logging = False

    def visit_Import(self, node: ast.Import) -> None:
        """Check for deprecated logging imports."""
        for alias in node.names:
            if alias.name == "logging":
                self.errors.append((node.lineno, "FORBIDDEN: import logging - Use enhanced logging instead"))
            elif alias.name == "structlog" and not self.uses_enhanced_logging:
                self.errors.append((node.lineno, "FORBIDDEN: import structlog - Use enhanced logging instead"))

        self.imports[node.lineno] = [alias.name for alias in node.names]
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Check for deprecated logging imports."""
        if node.module == "logging":
            for alias in node.names:
                if alias.name in ["getLogger", "Logger"]:
                    self.errors.append(
                        (node.lineno, f"FORBIDDEN: from logging import {alias.name} - Use enhanced logging instead")
                    )
        elif node.module == "server.logging.enhanced_logging_config":
            self.uses_enhanced_logging = True
            for alias in node.names:
                if alias.name == "get_logger":
                    # This is good - using enhanced logging
                    pass

        self.imports[node.lineno] = [alias.name for alias in node.names]
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        """Check for deprecated logging patterns in function calls."""
        # Check for logging.getLogger() calls
        if isinstance(node.func, ast.Attribute):
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "logging"
                and node.func.attr == "getLogger"
            ):
                self.errors.append((node.lineno, "FORBIDDEN: logging.getLogger() - Use enhanced logging instead"))

        # Check for context parameter usage
        for keyword in node.keywords:
            if keyword.arg == "context":
                self.errors.append(
                    (node.lineno, "FORBIDDEN: context={'key': 'value'} parameter - Use direct key-value pairs instead")
                )

        # Check for string formatting in log calls
        if isinstance(node.func, ast.Attribute) and node.func.attr in ["debug", "info", "warning", "error", "critical"]:
            # Check for f-string formatting in arguments
            for arg in node.args:
                if isinstance(arg, ast.JoinedStr):  # f-string
                    self.errors.append(
                        (node.lineno, "FORBIDDEN: f-string formatting in log messages - Use structured logging instead")
                    )

            # Check for string formatting in keyword arguments
            for keyword in node.keywords:
                if isinstance(keyword.value, ast.JoinedStr):  # f-string
                    self.errors.append(
                        (node.lineno, "FORBIDDEN: f-string formatting in log messages - Use structured logging instead")
                    )

    def visit_FormattedValue(self, node: ast.FormattedValue) -> None:
        """Check for f-string usage in logging contexts."""
        # This is a simplified check - in practice, we'd need more context
        # to determine if this is in a logging call
        pass


def lint_file(file_path: Path) -> list[tuple[int, str]]:
    """Lint a single Python file for logging patterns."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        tree = ast.parse(content, filename=str(file_path))
        linter = LoggingPatternLinter()
        linter.visit(tree)

        return linter.errors
    except SyntaxError as e:
        return [(e.lineno or 0, f"Syntax error: {e.msg}")]
    except Exception as e:
        return [(0, f"Error parsing file: {e}")]


def main() -> int:
    """Main entry point for the logging pattern linter."""
    project_root = Path(__file__).parent.parent
    server_dir = project_root / "server"

    if not server_dir.exists():
        print("❌ Server directory not found")
        return 1

    errors_found = False

    # Find all Python files in the server directory
    python_files = list(server_dir.rglob("*.py"))

    print("Checking Python files for enhanced logging patterns...")

    for file_path in python_files:
        # Skip __pycache__, test files, and virtual environment files
        if (
            "__pycache__" in str(file_path)
            or "test" in str(file_path).lower()
            or ".venv" in str(file_path)
            or "site-packages" in str(file_path)
        ):
            continue

        errors = lint_file(file_path)

        if errors:
            errors_found = True
            print(f"\nFile: {file_path.relative_to(project_root)}")
            for line_num, error_msg in errors:
                print(f"  Line {line_num}: {error_msg}")

    if errors_found:
        print("\nERROR: Enhanced logging pattern violations found!")
        print("\nFor correct usage, see:")
        print("  - docs/LOGGING_BEST_PRACTICES.md")
        print("  - docs/LOGGING_QUICK_REFERENCE.md")
        print("  - docs/examples/logging/")
        print("\nCorrect usage example:")
        print("  from server.logging.enhanced_logging_config import get_logger")
        print("  logger = get_logger(__name__)")
        print("  logger.info('User action completed', user_id=user.id, action='login')")
        return 1
    else:
        print("SUCCESS: All Python files use enhanced logging patterns correctly!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
