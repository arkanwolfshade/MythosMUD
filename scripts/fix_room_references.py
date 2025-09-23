#!/usr/bin/env python3
"""
Fix room ID references in Arkham City northside area.

This script fixes the systematic issue where room files have the new ID format
(with "room_" prefix) but their exit references are still using the old format
(without "room_" prefix).

As noted in the Pnakotic Manuscripts, proper dimensional mapping is essential
for maintaining the integrity of our eldritch architecture.
"""

import json
from pathlib import Path


def load_room_file(file_path: Path) -> dict:
    """Load a room file safely."""
    try:
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise ValueError(f"Failed to load {file_path}: {e}") from e


def save_room_file(file_path: Path, room_data: dict) -> None:
    """Save a room file safely."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(room_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Failed to save {file_path}: {e}") from e


def fix_room_references(base_path: str = "./data/rooms/earth/arkhamcity/northside") -> None:
    """
    Fix room ID references in the northside area.

    Args:
        base_path: Path to the northside directory
    """
    base_path = Path(base_path)
    if not base_path.exists():
        print(f"Base path does not exist: {base_path}")
        return

    # Define the mapping from old IDs to new IDs
    room_id_mapping = {
        "earth_arkhamcity_northside_derby_st_001": "earth_arkhamcity_northside_room_derby_st_001",
        "earth_arkhamcity_northside_derby_st_002": "earth_arkhamcity_northside_room_derby_st_002",
        "earth_arkhamcity_northside_derby_st_003": "earth_arkhamcity_northside_room_derby_st_003",
        "earth_arkhamcity_northside_derby_st_004": "earth_arkhamcity_northside_room_derby_st_004",
        "earth_arkhamcity_northside_derby_st_005": "earth_arkhamcity_northside_room_derby_st_005",
        "earth_arkhamcity_northside_derby_st_006": "earth_arkhamcity_northside_room_derby_st_006",
        "earth_arkhamcity_northside_derby_st_007": "earth_arkhamcity_northside_room_derby_st_007",
        "earth_arkhamcity_northside_derby_st_008": "earth_arkhamcity_northside_room_derby_st_008",
        "earth_arkhamcity_northside_derby_st_009": "earth_arkhamcity_northside_room_derby_st_009",
        "earth_arkhamcity_northside_derby_st_010": "earth_arkhamcity_northside_room_derby_st_010",
        "earth_arkhamcity_northside_derby_st_011": "earth_arkhamcity_northside_room_derby_st_011",
        "earth_arkhamcity_northside_derby_st_012": "earth_arkhamcity_northside_room_derby_st_012",
        "earth_arkhamcity_northside_derby_st_013": "earth_arkhamcity_northside_room_derby_st_013",
        "earth_arkhamcity_northside_derby_st_014": "earth_arkhamcity_northside_room_derby_st_014",
    }

    files_fixed = []
    total_fixes = 0

    # Process all JSON files in the directory
    for file_path in base_path.glob("*.json"):
        if file_path.name.startswith("subzone_config"):
            continue

        try:
            room_data = load_room_file(file_path)
            file_modified = False

            # Check exits for old ID references
            if "exits" in room_data:
                for direction, target_id in room_data["exits"].items():
                    if target_id in room_id_mapping:
                        old_id = target_id
                        new_id = room_id_mapping[target_id]
                        room_data["exits"][direction] = new_id
                        print(f"  Fixed {direction} exit: {old_id} -> {new_id}")
                        file_modified = True
                        total_fixes += 1

            # Save the file if it was modified
            if file_modified:
                save_room_file(file_path, room_data)
                files_fixed.append(file_path.name)
                print(f"✓ Fixed {file_path.name}")

        except Exception as e:
            print(f"✗ Error processing {file_path.name}: {e}")

    print("\nSummary:")
    print(f"  Files fixed: {len(files_fixed)}")
    print(f"  Total fixes: {total_fixes}")

    if files_fixed:
        print("\nFixed files:")
        for filename in sorted(files_fixed):
            print(f"  - {filename}")


def main():
    """Main function."""
    print("Fixing room ID references in Arkham City northside area...")
    print("=" * 60)

    try:
        fix_room_references()
        print("\n✓ Room reference fixes completed successfully!")
    except Exception as e:
        print(f"\n✗ Error during room reference fixes: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
