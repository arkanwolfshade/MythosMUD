#!/usr/bin/env python3
"""
Automatically merge legacy test files into their primary files.

This script appends the content of legacy files to their primary files
with clear demarcation, then deletes the legacy files.
"""

import sys
from pathlib import Path

# Base path
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent

# Mapping of primary file -> legacy file(s)
MERGE_MAP = {
    "unit/player/test_player_service.py": ["unit/player/test_player_service_layer_legacy.py"],
    "unit/events/test_event_handler.py": ["unit/events/test_event_handler_broadcasting_legacy.py"],
    "integration/events/test_event_flow_integration.py": ["integration/events/test_real_event_flow_legacy.py"],
    "unit/chat/test_emote_filtering.py": ["unit/chat/test_emote_types_filtering_legacy.py"],
    "unit/commands/test_command_handler.py": ["unit/commands/test_unified_command_handler_legacy.py"],
    # Separate test_command_handler_v2_legacy - has significant content
}


def merge_file(primary_path: str, legacy_paths: list[str], dry_run: bool = False) -> bool:
    """
    Merge legacy file(s) into primary file.

    Args:
        primary_path: Path to primary file
        legacy_paths: List of paths to legacy files
        dry_run: If True, don't actually merge

    Returns:
        True if successful
    """
    primary_file = BASE / primary_path

    if not primary_file.exists():
        print(f"  [SKIP] Primary file not found: {primary_path}")
        return False

    for legacy_path in legacy_paths:
        legacy_file = BASE / legacy_path

        if not legacy_file.exists():
            print(f"  [SKIP] Legacy file not found: {legacy_path}")
            continue

        if dry_run:
            print(f"  [WOULD MERGE] {legacy_path}")
            print(f"            ->  {primary_path}")
            continue

        try:
            # Read both files
            primary_content = primary_file.read_text(encoding="utf-8")
            legacy_content = legacy_file.read_text(encoding="utf-8")

            # Extract just the test classes/functions from legacy (skip imports/docstring)
            lines = legacy_content.split("\n")

            # Find where the actual test code starts (after imports)
            start_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("class Test") or (line.startswith("def test_") and not line.strip().startswith("#")):
                    start_idx = i
                    break

            if start_idx == 0:
                # No test code found
                print(f"  [SKIP] No test code found in {legacy_path}")
                continue

            # Get the test content
            test_content = "\n".join(lines[start_idx:])

            # Append to primary file with demarcation
            legacy_name = Path(legacy_path).name
            merged_content = (
                primary_content.rstrip()
                + "\n\n\n# "
                + "=" * 76
                + f"\n# Tests merged from {legacy_name}\n# "
                + "=" * 76
                + "\n\n\n"
                + test_content
                + "\n"
            )

            # Write back
            primary_file.write_text(merged_content, encoding="utf-8")

            # Delete legacy file
            legacy_file.unlink()

            print(f"  [MERGED] {legacy_path}")
            print(f"        -> {primary_path}")

        except Exception as e:
            print(f"  [ERROR] Failed to merge {legacy_path}: {e}")
            return False

    return True


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Auto-merge legacy test files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be merged")
    parser.add_argument("--all", action="store_true", help="Merge all mapped files")

    args = parser.parse_args()

    print("=" * 80)
    print(f"{'DRY RUN: ' if args.dry_run else ''}Auto-merging legacy test files")
    print("=" * 80)
    print()

    if not args.all:
        print("Use --all to merge all files, or --dry-run to preview")
        return 1

    total = 0
    for primary, legacies in MERGE_MAP.items():
        if merge_file(primary, legacies, dry_run=args.dry_run):
            total += len(legacies)

    print()
    print(f"{'Would merge' if args.dry_run else 'Merged'}: {total} legacy files")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
