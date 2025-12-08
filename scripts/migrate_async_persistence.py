#!/usr/bin/env python
"""
Async Persistence Migration Script.

This script automates the migration of synchronous persistence calls to async
versions across the codebase, following the Phase 2 remediation plan.

Usage:
    python scripts/migrate_async_persistence.py --dry-run  # Preview changes
    python scripts/migrate_async_persistence.py            # Apply changes
"""

import argparse
import re
from pathlib import Path
from typing import NamedTuple


class MigrationResult(NamedTuple):
    """Result of a file migration."""

    file_path: str
    instances_found: int
    instances_migrated: int
    methods_made_async: int
    errors: list[str]


def migrate_file(file_path: Path, dry_run: bool = False) -> MigrationResult:
    """
    Migrate a single file to use async persistence patterns.

    Args:
        file_path: Path to the file to migrate
        dry_run: If True, only preview changes without modifying file

    Returns:
        MigrationResult with migration statistics
    """
    errors = []
    instances_found = 0
    instances_migrated = 0
    methods_made_async = 0

    try:
        content = file_path.read_text(encoding="utf-8")
        original_content = content

        # Pattern 1: Find sync persistence calls in async contexts
        # self.persistence.get_something(...) → await asyncio.to_thread(self.persistence.get_something, ...)
        sync_patterns = [
            (
                r"(\s+)([a-z_]+)\s*=\s*self\.persistence\.(get_\w+|save_\w+|list_\w+|delete_\w+)\(([^)]+)\)",
                r'\1\2 = await asyncio.to_thread(self.persistence.\3, \4)',
            ),
            # Pattern for calls without assignment
            (
                r"(\s+)self\.persistence\.(get_\w+|save_\w+|list_\w+|delete_\w+)\(([^)]+)\)",
                r'\1await asyncio.to_thread(self.persistence.\2, \3)',
            ),
        ]

        for pattern, replacement in sync_patterns:
            matches = re.findall(pattern, content)
            instances_found += len(matches)
            if matches:
                content = re.sub(pattern, replacement, content)
                instances_migrated += len(matches)

        # Pattern 2: Make methods async if they now use await
        # def method_name( → async def method_name(
        if "await asyncio.to_thread" in content and "import asyncio" not in content:
            # Add import at top of file
            import_pattern = r"(from __future__ import annotations\n\n)"
            import_replacement = r"\1import asyncio\n"
            content = re.sub(import_pattern, import_replacement, content)

        # Find methods that need to be made async
        # Look for def that contain await calls
        method_pattern = r"(\s+)def (\w+)\(([^)]*)\)([^:]*):(\s+\"\"\"[^\"]*\"\"\")?(.*?)(?=\n\s+def |\n\nclass |\Z)"
        methods = list(re.finditer(method_pattern, content, re.DOTALL))

        for match in methods:
            method_body = match.group(6)
            if "await asyncio.to_thread" in method_body and not match.group(0).startswith("async "):
                # This method needs to be made async
                methods_made_async += 1
                # Replace def with async def
                old_signature = f"{match.group(1)}def {match.group(2)}({match.group(3)}){match.group(4)}:"
                new_signature = f"{match.group(1)}async def {match.group(2)}({match.group(3)}){match.group(4)}:"
                content = content.replace(old_signature, new_signature, 1)

        if content != original_content:
            if not dry_run:
                file_path.write_text(content, encoding="utf-8")
                print(f"✅ Migrated: {file_path}")
            else:
                print(f"📝 Would migrate: {file_path}")
                print(f"   - {instances_found} sync calls found")
                print(f"   - {instances_migrated} would be wrapped in asyncio.to_thread")
                print(f"   - {methods_made_async} methods would be made async")

    except Exception as e:
        errors.append(str(e))
        print(f"❌ Error migrating {file_path}: {e}")

    return MigrationResult(
        file_path=str(file_path),
        instances_found=instances_found,
        instances_migrated=instances_migrated,
        methods_made_async=methods_made_async,
        errors=errors,
    )


def main():
    """Main entry point."""
    parser = argparse.Parser(description="Migrate async persistence calls")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying files")
    parser.add_argument("--file", type=str, help="Migrate specific file only")
    args = parser.parse_args()

    # Files to migrate (from ASYNC_PERSISTENCE_MIGRATION_TRACKER.md)
    files_to_migrate = [
        "server/services/wearable_container_service.py",  # 7 instances
        "server/services/npc_combat_integration_service.py",  # 6 instances
        "server/services/user_manager.py",  # 5 instances
        "server/services/corpse_lifecycle_service.py",  # 4 instances
        "server/services/npc_startup_service.py",  # 3 instances
        "server/services/player_position_service.py",  # 2 instances
        "server/services/environmental_container_loader.py",  # 2 instances
        "server/services/player_death_service.py",  # 1 instance
        "server/services/player_combat_service.py",  # 1 instance
        "server/services/health_service.py",  # 1 instance
    ]

    project_root = Path(__file__).parent.parent
    results = []

    if args.file:
        # Migrate specific file
        file_path = project_root / args.file
        result = migrate_file(file_path, dry_run=args.dry_run)
        results.append(result)
    else:
        # Migrate all files
        for file_rel_path in files_to_migrate:
            file_path = project_root / file_rel_path
            if file_path.exists():
                result = migrate_file(file_path, dry_run=args.dry_run)
                results.append(result)
            else:
                print(f"⚠️  File not found: {file_path}")

    # Print summary
    print("\n" + "=" * 60)
    print("MIGRATION SUMMARY")
    print("=" * 60)

    total_found = sum(r.instances_found for r in results)
    total_migrated = sum(r.instances_migrated for r in results)
    total_async = sum(r.methods_made_async for r in results)
    total_errors = sum(len(r.errors) for r in results)

    print(f"Files processed: {len(results)}")
    print(f"Sync calls found: {total_found}")
    print(f"Calls migrated: {total_migrated}")
    print(f"Methods made async: {total_async}")
    print(f"Errors: {total_errors}")

    if args.dry_run:
        print("\n⚠️  DRY RUN - No files were modified")
        print("Run without --dry-run to apply changes")
    else:
        print("\n✅ Migration complete!")
        print("\nNext steps:")
        print("1. Run linter: make lint")
        print("2. Run tests: make test")
        print("3. Review changes: git diff")

    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    exit(main())
