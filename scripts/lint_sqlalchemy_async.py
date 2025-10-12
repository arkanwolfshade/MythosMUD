#!/usr/bin/env python3
"""
SQLAlchemy Async Pattern Linter

This script checks for raw SQL strings being passed to async SQLAlchemy execute()
methods without proper text() wrapping, which causes ObjectNotExecutableError.

Usage:
    python scripts/lint_sqlalchemy_async.py [file_or_directory]

Examples:
    python scripts/lint_sqlalchemy_async.py
    python scripts/lint_sqlalchemy_async.py server/database.py
    python scripts/lint_sqlalchemy_async.py server/
"""

import ast
import sys
from pathlib import Path


class SQLAlchemyAsyncLinter(ast.NodeVisitor):
    """
    AST visitor to detect problematic SQLAlchemy async patterns.

    Detects patterns like:
    - await conn.execute("raw SQL string")  # BAD
    - await session.execute("raw SQL string")  # BAD

    Should be:
    - await conn.execute(text("raw SQL string"))  # GOOD
    - await session.execute(text("raw SQL string"))  # GOOD
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.violations: list[tuple[int, str, str]] = []
        self.has_sqlalchemy_import = False
        self.has_text_import = False

    def visit_Import(self, node: ast.Import) -> None:
        """Check for SQLAlchemy imports."""
        for alias in node.names:
            if alias.name.startswith("sqlalchemy"):
                self.has_sqlalchemy_import = True
            if alias.name == "sqlalchemy" and alias.asname == "sa":
                # Check for 'from sqlalchemy import text' pattern
                pass
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Check for SQLAlchemy text import."""
        if node.module == "sqlalchemy":
            self.has_sqlalchemy_import = True
            for alias in node.names:
                if alias.name == "text":
                    self.has_text_import = True
        elif node.module and node.module.startswith("sqlalchemy"):
            self.has_sqlalchemy_import = True
        self.generic_visit(node)

    def visit_Await(self, node: ast.Await) -> None:
        """Check for problematic await patterns."""
        if isinstance(node.value, ast.Call):
            self._check_execute_call(node.value)
        self.generic_visit(node)

    def _check_execute_call(self, call_node: ast.Call) -> None:
        """Check if this is a problematic execute() call."""
        if not isinstance(call_node.func, ast.Attribute):
            return

        # Check if this is an execute() call
        if call_node.func.attr != "execute":
            return

        # Check if the object being called is likely a SQLAlchemy connection/session
        if isinstance(call_node.func.value, ast.Name):
            obj_name = call_node.func.value.id
            # Only check SQLAlchemy connections, not aiosqlite or other database libraries
            if obj_name in ["conn", "session", "connection"] and self.has_sqlalchemy_import:
                # Check if first argument is a raw string
                if call_node.args and isinstance(call_node.args[0], ast.Constant):
                    if isinstance(call_node.args[0].value, str):
                        # This is a raw SQL string - check if it's wrapped in text()
                        if not self._is_wrapped_in_text(call_node):
                            self.violations.append(
                                (
                                    call_node.lineno,
                                    f"Raw SQL string passed to {obj_name}.execute() without text() wrapper",
                                    f"Use: {obj_name}.execute(text('{call_node.args[0].value}'))",
                                )
                            )

    def _is_wrapped_in_text(self, call_node: ast.Call) -> bool:
        """Check if the argument is wrapped in text()."""
        if not call_node.args:
            return False

        arg = call_node.args[0]
        if isinstance(arg, ast.Call):
            if isinstance(arg.func, ast.Name):
                return arg.func.id == "text"
            elif isinstance(arg.func, ast.Attribute):
                # Handle cases like sa.text() or sqlalchemy.text()
                return arg.func.attr == "text"

        return False


def lint_file(file_path: Path) -> list[tuple[str, int, str, str]]:
    """
    Lint a single Python file for SQLAlchemy async issues.

    Returns:
        List of (filename, line_number, message, suggestion) tuples
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        tree = ast.parse(content, filename=str(file_path))
        linter = SQLAlchemyAsyncLinter(str(file_path))
        linter.visit(tree)

        return [(str(file_path), line_no, message, suggestion) for line_no, message, suggestion in linter.violations]
    except SyntaxError as e:
        return [(str(file_path), e.lineno or 0, f"Syntax error: {e.msg}", "Fix syntax error")]
    except Exception as e:
        return [(str(file_path), 0, f"Error parsing file: {e}", "Check file format")]


def lint_directory(directory: Path) -> list[tuple[str, int, str, str]]:
    """
    Lint all Python files in a directory recursively.

    Returns:
        List of (filename, line_number, message, suggestion) tuples
    """
    violations = []

    for py_file in directory.rglob("*.py"):
        # Skip __pycache__ and other hidden directories
        if any(part.startswith(".") for part in py_file.parts):
            continue

        violations.extend(lint_file(py_file))

    return violations


def main():
    """Main entry point for the linter."""
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
    else:
        target = Path("server")

    if not target.exists():
        print(f"Error: {target} does not exist")
        sys.exit(1)

    if target.is_file():
        violations = lint_file(target)
    else:
        violations = lint_directory(target)

    if not violations:
        print("[OK] No SQLAlchemy async violations found!")
        return 0

    print(f"[ERROR] Found {len(violations)} SQLAlchemy async violations:")
    print()

    for filename, line_no, message, suggestion in violations:
        print(f"[FILE] {filename}:{line_no}")
        print(f"   [ERROR] {message}")
        print(f"   [SUGGESTION] {suggestion}")
        print()

    print("[FIX] To fix these issues:")
    print("   1. Add 'from sqlalchemy import text' to imports")
    print("   2. Wrap raw SQL strings with text() function")
    print("   3. Example: await conn.execute(text('PRAGMA foreign_keys = ON'))")

    return 1


if __name__ == "__main__":
    sys.exit(main())
