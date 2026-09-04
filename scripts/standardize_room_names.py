#!/usr/bin/env python3
"""
Standardize room and intersection filenames and IDs to lowercase.

This script renames all room and intersection files to lowercase and updates
their internal IDs to match. This eliminates case-sensitivity issues in
dimensional mapping.

As noted in the Pnakotic Manuscripts, consistency in naming conventions is
essential for maintaining the integrity of our eldritch architecture.
"""

import json
import os
import shutil
from pathlib import Path


def load_room_file(file_path: Path) -> dict:
    """Load a room file safely."""
    try:
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise ValueError(f"Could not load room file {file_path}: {e}") from e


def save_room_file(file_path: Path, room_data: dict) -> None:
    """Save a room file safely."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(room_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Could not save room file {file_path}: {e}") from e


def standardize_room_id(room_id: str) -> str:
    """Convert room ID to lowercase."""
    return room_id.lower()


def standardize_filename(filename: str) -> str:
    """Convert filename to lowercase."""
    return filename.lower()


def update_room_references(room_data: dict, old_id: str, new_id: str) -> dict:
    """Update all room references in exits to use the new lowercase ID."""
    updated_data = room_data.copy()

    if "exits" in updated_data:
        for direction, target_room in updated_data["exits"].items():
            if target_room and isinstance(target_room, str):
                # Convert the target room ID to lowercase
                updated_data["exits"][direction] = target_room.lower()

    return updated_data


def process_room_files(base_path: str = "data/rooms") -> None:
    """Process all room files to standardize names and IDs."""
    base_path = Path(base_path)

    if not base_path.exists():
        print(f"Base path {base_path} does not exist!")
        return

    processed_files = []
    renamed_files = []

    print("Standardizing room and intersection files...")
    print("=" * 60)

    # Walk through all directories
    for root, _dirs, files in os.walk(base_path):
        root_path = Path(root)

        for filename in files:
            if (
                filename.endswith(".json")
                and not filename.startswith("subzone_config")
                and not filename.startswith("zone_config")
            ):
                file_path = root_path / filename

                try:
                    # Load the room data
                    room_data = load_room_file(file_path)

                    # Get the old room ID
                    old_room_id = room_data.get("id", "")
                    if not old_room_id:
                        print(f"Warning: No ID found in {file_path}")
                        continue

                    # Generate new lowercase room ID
                    new_room_id = standardize_room_id(old_room_id)

                    # Generate new lowercase filename
                    new_filename = standardize_filename(filename)
                    new_file_path = root_path / new_filename

                    # Update room data
                    updated_room_data = update_room_references(room_data, old_room_id, new_room_id)
                    updated_room_data["id"] = new_room_id

                    # Track what we're doing
                    processed_files.append(
                        {
                            "old_path": str(file_path),
                            "new_path": str(new_file_path),
                            "old_id": old_room_id,
                            "new_id": new_room_id,
                        }
                    )

                    # Save the updated room data
                    save_room_file(file_path, updated_room_data)

                    # Rename the file if needed
                    if filename != new_filename:
                        shutil.move(str(file_path), str(new_file_path))
                        renamed_files.append((str(file_path), str(new_file_path)))
                        print(f"Renamed: {filename} -> {new_filename}")

                    print(f"Updated ID: {old_room_id} -> {new_room_id}")

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue

    print("\n" + "=" * 60)
    print("Processing complete!")
    print(f"Files processed: {len(processed_files)}")
    print(f"Files renamed: {len(renamed_files)}")

    # Generate a summary of changes
    print("\nSummary of changes:")
    print("-" * 40)
    for change in processed_files:
        print(f"File: {Path(change['old_path']).name}")
        print(f"  ID: {change['old_id']} -> {change['new_id']}")
        if change["old_path"] != change["new_path"]:
            print(f"  Path: {change['old_path']} -> {change['new_path']}")
        print()


def main():
    """Main function."""
    print("MythosMUD Room Standardization Script")
    print("=====================================")
    print()

    # Run automatically without confirmation
    print("Running standardization automatically...")

    try:
        process_room_files()
        print("\nStandardization complete! Please restart the server to apply changes.")
    except Exception as e:
        print(f"Error during standardization: {e}")


if __name__ == "__main__":
    main()
