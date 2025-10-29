#!/usr/bin/env python3
"""Count test methods in legacy files."""

import ast
from pathlib import Path

base = Path(__file__).parent.parent
legacy_files = sorted(base.rglob("*_legacy.py"))

print("Legacy File Analysis - Detailed Test Count")
print("=" * 80)
total = 0
for f in legacy_files:
    if "scripts" not in str(f):
        content = f.read_text(encoding="utf-8")
        tree = ast.parse(content)
        test_methods = sum(
            1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
        )
        test_classes = sum(
            1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and node.name.startswith("Test")
        )
        rel = f.relative_to(base)
        print(f"{str(rel):70} {test_methods:3} methods, {test_classes:2} classes")
        total += test_methods

print("=" * 80)
print(f"TOTAL: {total} test methods across {len([f for f in legacy_files if 'scripts' not in str(f)])} files")
