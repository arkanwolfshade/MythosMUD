#!/usr/bin/env python3
"""
Migration script to rename room files from old naming schema to new unified schema.

This script performs the following transformations:

Old Schema -> New Schema:
- W_Derby_St_001.json -> room_derby_001.json
- E_Derby_St_003.json -> room_derby_003.json
- intersection_Derby_High.json -> intersection_derby_high.json

Usage:
    python scripts/migrate_room_filenames.py [--dry-run] [--backup]
"""

import argparse
import json
import re
import shutil
from pathlib import Path


class RoomFilenameMigrator:
    """Handles migration of room filenames from old to new schema."""

    def __init__(self, base_path: str = "./data/rooms"):
        """Initialize the migrator."""
        self.base_path = Path(base_path)
        self.migrations: list[tuple[Path, Path]] = []
        self.errors: list[str] = []

    def parse_old_filename(self, filename: str) -> dict | None:
        """Parse old filename format to extract components."""
        if not filename.endswith(".json"):
            return None

        name = filename[:-5]  # Remove .json extension

        # Old room pattern: {Direction}_{StreetName}_{Number}.json
        room_pattern = r"^([NESW])_([A-Za-z0-9_]+)_(\d{3})$"
        room_match = re.match(room_pattern, name)
        if room_match:
            direction = room_match.group(1)
            street_name = room_match.group(2)
            number = room_match.group(3)

            # Convert street name to lowercase and remove common suffixes
            street_clean = re.sub(r"_St$|_Street$|_Lane$|_Ave$|_Avenue$", "", street_name.lower())
            street_clean = re.sub(r"[^a-z0-9_]", "_", street_clean)

            return {
                "type": "room",
                "direction": direction,
                "street": street_clean,
                "number": number,
                "new_name": f"room_{street_clean}_{number}.json",
            }

        # Old intersection pattern: intersection_{StreetA}_{StreetB}.json
        # Only process if it's not already in lowercase (new format)
        intersection_pattern = r"^intersection_([A-Z][a-zA-Z0-9_]*)_([A-Z][a-zA-Z0-9_]*)$"
        intersection_match = re.match(intersection_pattern, name)
        if intersection_match:
            street_a = intersection_match.group(1)
            street_b = intersection_match.group(2)

            # Convert to lowercase and clean
            street_a_clean = re.sub(r"[^a-z0-9_]", "_", street_a.lower())
            street_b_clean = re.sub(r"[^a-z0-9_]", "_", street_b.lower())

            return {
                "type": "intersection",
                "street_a": street_a_clean,
                "street_b": street_b_clean,
                "new_name": f"intersection_{street_a_clean}_{street_b_clean}.json",
            }

        return None

    def discover_room_files(self) -> list[Path]:
        """Discover all room files that need migration."""
        room_files = []

        for file_path in self.base_path.rglob("*.json"):
            if file_path.is_file():
                # Skip configuration files
                if file_path.name in ["subzone_config.json", "zone_config.json"]:
                    continue

                # Check if this is an old format file
                parsed = self.parse_old_filename(file_path.name)
                if parsed:
                    room_files.append(file_path)

        return sorted(room_files)

    def plan_migrations(self) -> list[tuple[Path, Path]]:
        """Plan all file migrations without executing them."""
        migrations = []

        for file_path in self.discover_room_files():
            parsed = self.parse_old_filename(file_path.name)
            if parsed:
                new_path = file_path.parent / parsed["new_name"]

                # Check for conflicts - only if the target is different from source
                if new_path != file_path and new_path.exists():
                    self.errors.append(f"Conflict: {file_path} -> {new_path} (target exists)")
                elif new_path != file_path:
                    migrations.append((file_path, new_path))

        return migrations

    def update_room_id(self, file_path: Path, new_filename: str) -> bool:
        """Update the room ID in the JSON file to match new naming schema."""
        try:
            with open(file_path, encoding="utf-8") as f:
                room_data = json.load(f)

            # Extract location from file path
            path_parts = file_path.parts
            if len(path_parts) >= 4:
                plane = path_parts[-4]
                zone = path_parts[-3]
                sub_zone = path_parts[-2]

                # Parse new filename to generate correct ID
                parsed = self.parse_old_filename(file_path.name)
                if parsed:
                    if parsed["type"] == "room":
                        new_id = f"{plane}_{zone}_{sub_zone}_room_{parsed['street']}_{parsed['number']}"
                    else:  # intersection
                        new_id = f"{plane}_{zone}_{sub_zone}_intersection_{parsed['street_a']}_{parsed['street_b']}"

                    room_data["id"] = new_id

                    # Write back the updated data
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(room_data, f, indent=2, ensure_ascii=False)

                    return True

            return False

        except Exception as e:
            self.errors.append(f"Failed to update room ID in {file_path}: {e}")
            return False

    def migrate(self, dry_run: bool = False, create_backup: bool = False) -> bool:
        """Execute the migration."""
        print(f"🔍 Scanning {self.base_path} for room files...")

        migrations = self.plan_migrations()

        if not migrations:
            print("✅ No files need migration")
            return True

        print(f"📋 Found {len(migrations)} files to migrate:")

        for old_path, new_path in migrations:
            print(f"  {old_path.name} -> {new_path.name}")

        if self.errors:
            print("\n❌ Errors found:")
            for error in self.errors:
                print(f"  {error}")
            return False

        if dry_run:
            print("\n🔍 Dry run - no files will be modified")
            return True

        print("\n🚀 Starting migration...")

        success_count = 0
        for old_path, new_path in migrations:
            try:
                # Create backup if requested
                if create_backup:
                    backup_path = old_path.with_suffix(".backup.json")
                    shutil.copy2(old_path, backup_path)
                    print(f"  📦 Created backup: {backup_path.name}")

                # Update room ID in the file
                if self.update_room_id(old_path, new_path.name):
                    # Rename the file
                    old_path.rename(new_path)
                    print(f"  ✅ {old_path.name} -> {new_path.name}")
                    success_count += 1
                else:
                    print(f"  ❌ Failed to update room ID in {old_path.name}")

            except Exception as e:
                self.errors.append(f"Failed to migrate {old_path}: {e}")
                print(f"  ❌ {old_path.name}: {e}")

        print(f"\n📊 Migration complete: {success_count}/{len(migrations)} files migrated")

        if self.errors:
            print(f"❌ {len(self.errors)} errors occurred")
            return False

        return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Migrate room filenames to new unified schema")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be migrated without making changes")
    parser.add_argument("--backup", action="store_true", help="Create backup files before migration")
    parser.add_argument("--base-path", default="./data/rooms", help="Base directory containing room files")

    args = parser.parse_args()

    migrator = RoomFilenameMigrator(args.base_path)

    if migrator.migrate(dry_run=args.dry_run, create_backup=args.backup):
        print("🎉 Migration completed successfully!")
        return 0
    else:
        print("💥 Migration failed!")
        return 1


if __name__ == "__main__":
    exit(main())
