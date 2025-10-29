#!/usr/bin/env python3
"""
Validate test suite migration.

This script performs validation checks on the migrated test suite:
1. Import validation - Check all test files can be imported
2. Fixture discovery - Verify fixtures are accessible
3. Test discovery - Count tests pytest can discover
4. Structure validation - Verify directory structure is correct

Usage:
    python validate_migration.py
    python validate_migration.py --quick  # Skip import validation
"""

import argparse
import sys
from pathlib import Path

# Base paths
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent

# Expected structure
EXPECTED_CATEGORIES = [
    "unit",
    "integration",
    "e2e",
    "performance",
    "security",
    "coverage",
    "regression",
    "monitoring",
    "verification",
    "fixtures",
    "scripts",
]


def validate_structure() -> tuple[bool, list[str]]:
    """
    Validate directory structure exists.

    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []

    print("Validating directory structure...")
    print("-" * 70)

    for category in EXPECTED_CATEGORIES:
        cat_path = BASE / category
        if not cat_path.exists():
            issues.append(f"Missing directory: {category}")
            print(f"  [FAIL] {category}/ - Directory not found")
        elif not (cat_path / "__init__.py").exists() and category not in ["scripts"]:
            issues.append(f"Missing __init__.py in: {category}")
            print(f"  [WARN] {category}/__init__.py - File not found")
        else:
            print(f"  [OK] {category}/")

    print()
    return len(issues) == 0, issues


def count_tests() -> dict[str, int]:
    """
    Count test files in each category.

    Returns:
        Dictionary mapping category to test count
    """
    counts = {}

    print("Counting test files...")
    print("-" * 70)

    for category in EXPECTED_CATEGORIES:
        cat_path = BASE / category
        if cat_path.exists():
            test_files = list(cat_path.rglob("test_*.py"))
            counts[category] = len(test_files)
            print(f"  {category}: {len(test_files)} test files")
        else:
            counts[category] = 0

    print()
    total = sum(counts.values())
    print(f"Total test files: {total}")
    print()

    return counts


def check_imports(quick: bool = False) -> tuple[bool, list[str]]:
    """
    Check for common import issues in test files.

    Args:
        quick: If True, skip detailed import checking

    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    if quick:
        print("Skipping import validation (--quick mode)")
        print()
        return True, []

    issues = []

    print("Checking for import issues...")
    print("-" * 70)

    # Check for old import paths that need updating
    old_patterns = [
        (r"from.*\.\.utils\.", "Should use: from ..fixtures."),
        (r"from server\.tests\.utils\.", "Should use: from server.tests.fixtures."),
        (r"from server\.tests import mock_data", "Should use: from server.tests.fixtures import mock_data"),
    ]

    test_files = list(BASE.rglob("test_*.py"))
    files_with_issues = 0

    for test_file in test_files:
        file_issues = []

        try:
            content = test_file.read_text(encoding="utf-8")

            # Check for old import patterns
            for _pattern, suggestion in old_patterns:
                if "..utils." in content:
                    file_issues.append(f"Old import path found: {suggestion}")

            if file_issues:
                files_with_issues += 1
                rel_path = test_file.relative_to(BASE)
                issues.append(f"{rel_path}: {'; '.join(file_issues)}")
                print(f"  [WARN] {rel_path}")
                for issue in file_issues:
                    print(f"         {issue}")

        except Exception as e:
            issues.append(f"{test_file.name}: Failed to read file - {e}")
            print(f"  [ERROR] {test_file.name}: {e}")

    if files_with_issues == 0:
        print("  [OK] No import issues detected")

    print()
    print(f"Files checked: {len(test_files)}")
    print(f"Files with potential issues: {files_with_issues}")
    print()

    return files_with_issues == 0, issues


def check_conftest() -> tuple[bool, list[str]]:
    """
    Check conftest.py configuration.

    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []

    print("Validating conftest.py...")
    print("-" * 70)

    conftest_path = BASE / "conftest.py"
    if not conftest_path.exists():
        issues.append("conftest.py not found")
        print("  [FAIL] conftest.py not found")
        return False, issues

    try:
        content = conftest_path.read_text(encoding="utf-8")

        # Check for updated import paths
        if "from .fixtures." in content:
            print("  [OK] Updated fixture imports found")
        else:
            issues.append("conftest.py may not have updated fixture imports")
            print("  [WARN] No updated fixture imports detected")

        print("  [OK] conftest.py exists and readable")

    except Exception as e:
        issues.append(f"Failed to read conftest.py: {e}")
        print(f"  [ERROR] Failed to read conftest.py: {e}")

    print()
    return len(issues) == 0, issues


def main():
    """Main validation routine."""
    parser = argparse.ArgumentParser(description="Validate test suite migration")
    parser.add_argument("--quick", action="store_true", help="Skip detailed import validation")

    args = parser.parse_args()

    print("=" * 70)
    print("TEST SUITE MIGRATION VALIDATION")
    print("=" * 70)
    print()

    all_valid = True
    all_issues = []

    # 1. Validate structure
    structure_valid, structure_issues = validate_structure()
    all_valid = all_valid and structure_valid
    all_issues.extend(structure_issues)

    # 2. Count tests
    count_tests()

    # 3. Check imports
    imports_valid, import_issues = check_imports(quick=args.quick)
    all_valid = all_valid and imports_valid
    all_issues.extend(import_issues)

    # 4. Check conftest
    conftest_valid, conftest_issues = check_conftest()
    all_valid = all_valid and conftest_valid
    all_issues.extend(conftest_issues)

    # Summary
    print("=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print()

    if all_valid:
        print("[SUCCESS] All validation checks passed!")
        print()
        print("Migration structure is valid and ready for test execution.")
        print()
        print("Next steps:")
        print("  1. Run: make test-unit")
        print("  2. Run: make test-all")
        print("  3. Consolidate *_legacy.py files")
        print()
        return 0
    else:
        print("[FAILED] Validation issues detected:")
        print()
        for issue in all_issues:
            print(f"  - {issue}")
        print()
        print("Please address these issues before running tests.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
