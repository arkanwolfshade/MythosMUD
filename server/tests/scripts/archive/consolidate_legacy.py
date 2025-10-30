#!/usr/bin/env python3
"""
Consolidate legacy test files into their primary test files.

This script helps identify and consolidate *_legacy.py files by:
1. Finding all legacy files
2. Identifying their target files
3. Analyzing for unique content
4. Optionally removing duplicates

Usage:
    python consolidate_legacy.py --list        # List all legacy files
    python consolidate_legacy.py --analyze     # Analyze for unique content
    python consolidate_legacy.py --remove-empty  # Remove empty/duplicate legacy files
"""

import argparse
import ast
import sys
from pathlib import Path

# Base path
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent


def list_legacy_files() -> list[Path]:
    """
    Find all legacy test files (excluding this script).

    Returns:
        List of legacy file paths
    """
    legacy_files = []
    for f in BASE.rglob("*_legacy.py"):
        # Exclude this script and non-test files
        if f.name != "consolidate_legacy.py" and f.parent.name != "scripts":
            legacy_files.append(f)
    return sorted(legacy_files)


def count_test_functions(file_path: Path) -> int:
    """
    Count test functions/classes in a file.

    Args:
        file_path: Path to test file

    Returns:
        Number of test functions and classes
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content)

        count = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
                count += 1
            elif isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                count += 1

        return count
    except Exception:
        return -1  # Indicates parsing error


def analyze_legacy_files() -> dict:
    """
    Analyze legacy files for content.

    Returns:
        Dictionary with analysis results
    """
    legacy_files = list_legacy_files()
    analysis: dict[str, int | list[dict] | list[str]] = {
        "total": len(legacy_files),
        "files": [],
        "empty": [],
        "has_tests": [],
        "parse_errors": [],
    }

    print(f"Analyzing {len(legacy_files)} legacy files...")
    print("=" * 70)

    for legacy_file in legacy_files:
        rel_path = legacy_file.relative_to(BASE)
        test_count = count_test_functions(legacy_file)

        file_info = {"path": str(rel_path), "test_count": test_count, "size": legacy_file.stat().st_size}

        analysis["files"].append(file_info)

        if test_count == 0:
            analysis["empty"].append(str(rel_path))
            print(f"  [EMPTY] {rel_path} - No tests found")
        elif test_count == -1:
            analysis["parse_errors"].append(str(rel_path))
            print(f"  [ERROR] {rel_path} - Parse error")
        else:
            analysis["has_tests"].append(str(rel_path))
            print(f"  [HAS TESTS] {rel_path} - {test_count} tests")

    return analysis


def remove_empty_legacy_files(dry_run: bool = False) -> int:
    """
    Remove legacy test files that have no tests.

    Args:
        dry_run: If True, show what would be removed without actually removing

    Returns:
        Number of files removed
    """
    legacy_files = list_legacy_files()
    removed = 0

    print(f"{'DRY RUN: ' if dry_run else ''}Removing empty legacy test files...")
    print("=" * 70)

    for legacy_file in legacy_files:
        test_count = count_test_functions(legacy_file)
        rel_path = legacy_file.relative_to(BASE)

        if test_count == 0:
            if dry_run:
                print(f"  [WOULD REMOVE] {rel_path}")
            else:
                legacy_file.unlink()
                print(f"  [REMOVED] {rel_path}")
            removed += 1

    print()
    print(f"{'Would remove' if dry_run else 'Removed'}: {removed} empty legacy files")
    print()

    return removed


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Consolidate legacy test files", formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--list", action="store_true", help="List all legacy test files")
    parser.add_argument("--analyze", action="store_true", help="Analyze legacy files for content")
    parser.add_argument("--remove-empty", action="store_true", help="Remove empty legacy test files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without doing it")

    args = parser.parse_args()

    if args.list:
        legacy_files = list_legacy_files()
        print(f"Found {len(legacy_files)} legacy test files:")
        print("=" * 70)
        for f in legacy_files:
            print(f"  {f.relative_to(BASE)}")
        print()
        return 0

    if args.analyze:
        analysis = analyze_legacy_files()
        print()
        print("=" * 70)
        print("ANALYSIS SUMMARY")
        print("=" * 70)
        print(f"Total legacy files: {analysis['total']}")
        print(f"Empty files (no tests): {len(analysis['empty'])}")
        print(f"Files with tests: {len(analysis['has_tests'])}")
        print(f"Parse errors: {len(analysis['parse_errors'])}")
        print()

        if analysis["empty"]:
            print("Empty files that can be safely removed:")
            for f in analysis["empty"]:
                print(f"  - {f}")
            print()

        if analysis["has_tests"]:
            print(f"Files with tests ({len(analysis['has_tests'])}) require manual review:")
            print("These should be consolidated with their primary test files.")
            print()

        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
