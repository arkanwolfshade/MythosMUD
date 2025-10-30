#!/usr/bin/env python3
"""
Test Suite Migration Tracking Tool

This script helps track the progress of the test suite refactoring by:
- Counting tests in old vs new locations
- Validating that all tests are accounted for
- Generating progress reports
- Identifying missing or duplicate tests

Usage:
    python track_migration.py                    # Show summary
    python track_migration.py --detailed         # Show detailed file listing
    python track_migration.py --validate         # Validate migration completeness
    python track_migration.py --report          # Generate markdown report
"""

import argparse
import sys
from pathlib import Path
from typing import Any

# Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

# Test directories
OLD_TEST_DIR = PROJECT_ROOT / "server" / "tests"
NEW_TEST_ROOT = PROJECT_ROOT / "server" / "tests"

# Expected new structure
NEW_STRUCTURE = {
    "unit": [
        "api",
        "commands",
        "chat",
        "player",
        "npc",
        "world",
        "events",
        "auth",
        "infrastructure",
        "middleware",
        "models",
        "services",
        "realtime",
        "logging",
        "utilities",
    ],
    "integration": [
        "api",
        "commands",
        "chat",
        "events",
        "npc",
        "movement",
        "nats",
        "comprehensive",
    ],
    "e2e": [],
    "performance": [],
    "security": [],
    "coverage": [],
    "regression": [],
    "monitoring": [],
    "verification": [],
    "fixtures": [],
    "scripts": [],
}


def count_test_files(directory: Path, recursive: bool = True) -> int:
    """
    Count test files in a directory.

    Args:
        directory: Directory to search
        recursive: Whether to search recursively

    Returns:
        Number of test files found
    """
    if not directory.exists():
        return 0

    if recursive:
        return len(list(directory.rglob("test_*.py")))
    else:
        return len(list(directory.glob("test_*.py")))


def list_test_files(directory: Path, recursive: bool = True) -> list[Path]:
    """
    List all test files in a directory.

    Args:
        directory: Directory to search
        recursive: Whether to search recursively

    Returns:
        List of test file paths
    """
    if not directory.exists():
        return []

    if recursive:
        return sorted(directory.rglob("test_*.py"))
    else:
        return sorted(directory.glob("test_*.py"))


def get_old_structure_stats() -> dict[str, int]:
    """
    Get statistics about the old flat structure.

    Returns:
        Dictionary with test counts
    """
    stats = {
        "total": count_test_files(OLD_TEST_DIR, recursive=False),
        "in_utils": count_test_files(OLD_TEST_DIR / "utils", recursive=True),
        "in_scripts": count_test_files(OLD_TEST_DIR / "scripts", recursive=True),
    }
    stats["flat_structure"] = stats["total"]
    return stats


def get_new_structure_stats() -> dict[str, dict[str, Any]]:
    """
    Get statistics about the new hierarchical structure.

    Returns:
        Nested dictionary with test counts by category and subdirectory
    """
    from typing import Any
    
    stats: dict[str, dict[str, Any]] = {}

    for category, subdirs in NEW_STRUCTURE.items():
        category_path = NEW_TEST_ROOT / category
        category_stats: dict[str, Any] = {
            "total": count_test_files(category_path, recursive=True),
            "subdirs": {},
        }

        for subdir in subdirs:
            subdir_path = category_path / subdir
            category_stats["subdirs"][subdir] = count_test_files(subdir_path, recursive=True)

        stats[category] = category_stats

    return stats


def get_migration_progress() -> dict[str, Any]:
    """
    Calculate migration progress.

    Returns:
        Dictionary with progress metrics
    """
    old_stats = get_old_structure_stats()
    new_stats = get_new_structure_stats()

    # Count tests in new structure
    migrated_count = sum(cat["total"] for cat in new_stats.values())

    # Get tests still in old location (flat structure)
    remaining_old = count_test_files(OLD_TEST_DIR, recursive=False)

    # Calculate progress
    total_original = old_stats["flat_structure"]
    progress_pct = (migrated_count / total_original * 100) if total_original > 0 else 0

    return {
        "total_original": total_original,
        "migrated": migrated_count,
        "remaining": remaining_old,
        "progress_percentage": progress_pct,
        "old_stats": old_stats,
        "new_stats": new_stats,
    }


def print_summary(progress: dict[str, Any]) -> None:
    """
    Print a summary of migration progress.

    Args:
        progress: Progress data from get_migration_progress()
    """
    print("=" * 70)
    print("TEST SUITE MIGRATION PROGRESS")
    print("=" * 70)
    print()
    print(f"Total Original Tests:  {progress['total_original']}")
    print(f"Tests Migrated:        {progress['migrated']}")
    print(f"Tests Remaining:       {progress['remaining']}")
    print(f"Progress:              {progress['progress_percentage']:.1f}%")
    print()

    # Progress bar
    bar_length = 50
    filled = int(bar_length * progress["progress_percentage"] / 100)
    bar = "=" * filled + "-" * (bar_length - filled)
    print(f"[{bar}] {progress['progress_percentage']:.1f}%")
    print()

    # New structure breakdown
    print("=" * 70)
    print("NEW STRUCTURE BREAKDOWN")
    print("=" * 70)
    print()

    for category, stats in progress["new_stats"].items():
        print(f"{category.upper()}: {stats['total']} tests")
        if stats["subdirs"]:
            for subdir, count in stats["subdirs"].items():
                if count > 0:
                    print(f"  - {subdir}: {count}")
    print()


def print_detailed(progress: dict[str, Any]) -> None:
    """
    Print detailed file listings.

    Args:
        progress: Progress data from get_migration_progress()
    """
    print("=" * 70)
    print("DETAILED FILE LISTINGS")
    print("=" * 70)
    print()

    # Files still in old location
    print("FILES REMAINING IN OLD LOCATION:")
    print("-" * 70)
    old_files = list_test_files(OLD_TEST_DIR, recursive=False)
    if old_files:
        for f in old_files:
            print(f"  {f.name}")
    else:
        print("  (none)")
    print()

    # Files in new structure
    print("FILES IN NEW STRUCTURE:")
    print("-" * 70)
    for category in NEW_STRUCTURE.keys():
        category_path = NEW_TEST_ROOT / category
        if category_path.exists():
            files = list_test_files(category_path, recursive=True)
            if files:
                print(f"\n{category.upper()}:")
                for f in files:
                    rel_path = f.relative_to(NEW_TEST_ROOT)
                    print(f"  {rel_path}")
    print()


def validate_migration() -> tuple[bool, list[str]]:
    """
    Validate that migration is complete and correct.

    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []

    # Check if any tests remain in old location
    old_files = list_test_files(OLD_TEST_DIR, recursive=False)
    if old_files:
        # Exclude conftest.py and other setup files
        test_files = [f for f in old_files if f.name.startswith("test_")]
        if test_files:
            issues.append(f"Found {len(test_files)} test files still in old location")

    # Check for duplicate test names across new structure
    all_new_files = []
    for category in NEW_STRUCTURE.keys():
        category_path = NEW_TEST_ROOT / category
        if category_path.exists():
            all_new_files.extend(list_test_files(category_path, recursive=True))

    # Check for duplicates
    file_names = [f.name for f in all_new_files]
    duplicates = [name for name in set(file_names) if file_names.count(name) > 1]
    if duplicates:
        issues.append(f"Found duplicate test file names: {', '.join(duplicates)}")

    # Check that expected directories exist
    for category, subdirs in NEW_STRUCTURE.items():
        category_path = NEW_TEST_ROOT / category
        if not category_path.exists() and subdirs:  # Only if subdirs are expected
            issues.append(f"Expected directory does not exist: {category_path}")

    is_valid = len(issues) == 0
    return is_valid, issues


def generate_report(progress: dict[str, Any]) -> str:
    """
    Generate a markdown progress report.

    Args:
        progress: Progress data from get_migration_progress()

    Returns:
        Markdown formatted report
    """
    report = []
    report.append("# Test Suite Migration Progress Report")
    report.append("")
    report.append("## Summary")
    report.append("")
    report.append(f"- **Total Original Tests**: {progress['total_original']}")
    report.append(f"- **Tests Migrated**: {progress['migrated']}")
    report.append(f"- **Tests Remaining**: {progress['remaining']}")
    report.append(f"- **Progress**: {progress['progress_percentage']:.1f}%")
    report.append("")

    # Progress visualization
    bar_length = 50
    filled = int(bar_length * progress["progress_percentage"] / 100)
    bar = "=" * filled + "-" * (bar_length - filled)
    report.append(f"```\n[{bar}] {progress['progress_percentage']:.1f}%\n```")
    report.append("")

    # Breakdown by category
    report.append("## Migration Breakdown by Category")
    report.append("")
    report.append("| Category | Tests Migrated | Subdirectories |")
    report.append("|----------|----------------|----------------|")

    for category, stats in progress["new_stats"].items():
        subdirs = ", ".join(f"{name} ({count})" for name, count in stats["subdirs"].items() if count > 0)
        if not subdirs:
            subdirs = "-"
        report.append(f"| {category} | {stats['total']} | {subdirs} |")

    report.append("")

    # Validation
    is_valid, issues = validate_migration()
    report.append("## Validation")
    report.append("")
    if is_valid:
        report.append("✅ **Migration validation passed!**")
    else:
        report.append("❌ **Migration validation failed:**")
        report.append("")
        for issue in issues:
            report.append(f"- {issue}")
    report.append("")

    return "\n".join(report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Track test suite migration progress",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--detailed", action="store_true", help="Show detailed file listings")
    parser.add_argument("--validate", action="store_true", help="Validate migration completeness")
    parser.add_argument("--report", action="store_true", help="Generate markdown progress report")

    args = parser.parse_args()

    # Get progress data
    progress = get_migration_progress()

    if args.report:
        # Generate and print markdown report
        report = generate_report(progress)
        print(report)
    elif args.validate:
        # Validate migration
        is_valid, issues = validate_migration()
        if is_valid:
            print("✅ Migration validation passed!")
            print()
            print_summary(progress)
            sys.exit(0)
        else:
            print("❌ Migration validation failed:")
            print()
            for issue in issues:
                print(f"  - {issue}")
            print()
            sys.exit(1)
    elif args.detailed:
        # Show detailed listings
        print_summary(progress)
        print_detailed(progress)
    else:
        # Show summary only
        print_summary(progress)


if __name__ == "__main__":
    main()
