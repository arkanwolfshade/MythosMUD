#!/usr/bin/env python3
"""Pre-commit: forbid ``assert`` in production server Python (``server/`` excluding tests).

``assert`` is stripped when Python runs with ``-O``, so it must not enforce invariants in
runtime paths (see Codacy / security review on inventory commands).
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import override


def _excluded_server_module_filename(name: str) -> bool:
    return name.startswith("test_") or name.endswith("_test.py") or name == "conftest.py"


def _path_parts_indicate_production_server(parts: tuple[str, ...]) -> bool:
    if "server" not in parts:
        return False
    idx = parts.index("server")
    rest = parts[idx + 1 :]
    if not rest or rest[0] == "tests" or "__tests__" in parts:
        return False
    return not _excluded_server_module_filename(parts[-1])


def is_production_server_py(path: Path) -> bool:
    """True for MythosMUD backend modules under ``server/``, excluding tests and conftest."""
    if path.suffix != ".py":
        return False
    try:
        parts = path.resolve().parts
    except OSError:
        return False
    return _path_parts_indicate_production_server(parts)


class _AssertFinder(ast.NodeVisitor):
    """Collect line numbers of assert statements."""

    def __init__(self) -> None:
        self.lines: list[int] = []

    @override
    def visit_Assert(self, node: ast.Assert) -> None:
        self.lines.append(node.lineno)
        self.generic_visit(node)


def find_assert_line_numbers(file_path: Path) -> list[int]:
    """Return sorted unique line numbers of ``assert`` in file; empty if none or unreadable."""
    try:
        text = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    if not text.strip():
        return []
    try:
        tree = ast.parse(text, filename=str(file_path))
    except SyntaxError:
        return []
    finder = _AssertFinder()
    finder.visit(tree)
    return sorted(set(finder.lines))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(0)

    failures: list[tuple[str, list[int]]] = []
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.is_file():
            continue
        if not is_production_server_py(path):
            continue
        lines = find_assert_line_numbers(path)
        if lines:
            failures.append((str(path), lines))

    if not failures:
        sys.exit(0)

    print("ASSERT IN PRODUCTION SERVER CODE (use explicit checks + raise/log instead):", file=sys.stderr)
    print("", file=sys.stderr)
    for fp, lines in failures:
        print(f"  {fp}: lines {lines}", file=sys.stderr)
    print("", file=sys.stderr)
    print("``assert`` is not reliable under ``python -O``; use ``if ...: raise RuntimeError(...)``.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
