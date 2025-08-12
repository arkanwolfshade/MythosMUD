#!/usr/bin/env python3
"""
Fix Intersection Room IDs
Adds missing subzone prefix to intersection room IDs to match validator schema
"""

import glob
import json
import os
import shutil


def fix_intersection_room_ids():
    """Fix intersection room IDs to include subzone prefix"""

    print("=== INTERSECTION ROOM ID FIXER ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Processing {len(rooms)} room files...\n")

    # Find intersection rooms that need fixing
    intersection_fixes = []

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            room_id = data.get("id", "")

            # Check if this is an intersection room that needs fixing
            if "intersection" in room_id and room_id.startswith("earth_arkham_city_intersection_"):
                # Extract subzone from file path
                path_parts = f.replace("\\", "/").split("/")
                subzone_index = path_parts.index("arkham_city") + 1
                if subzone_index < len(path_parts):
                    subzone = path_parts[subzone_index]

                    # Create corrected room ID
                    corrected_id = f"earth_arkham_city_{subzone}_{room_id}"

                    intersection_fixes.append(
                        {"file": f, "old_id": room_id, "new_id": corrected_id, "subzone": subzone}
                    )

                    print(f"Found intersection room needing fix: {room_id} → {corrected_id}")

        except Exception as e:
            print(f"Error reading {f}: {e}")

    print(f"\nFound {len(intersection_fixes)} intersection rooms needing ID fixes\n")

    # Apply fixes
    for fix in intersection_fixes:
        try:
            # Read current file
            with open(fix["file"], encoding="utf-8") as file:
                data = json.load(file)

            # Create backup
            backup_file = fix["file"] + ".backup"
            shutil.copy2(fix["file"], backup_file)

            # Update room ID
            data["id"] = fix["new_id"]

            # Update any exits that reference the old ID
            exits = data.get("exits", {})
            for direction, target_id in exits.items():
                if target_id == fix["old_id"]:
                    exits[direction] = fix["new_id"]

            # Write updated file
            with open(fix["file"], "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

            print(f"Fixed: {fix['old_id']} → {fix['new_id']}")

        except Exception as e:
            print(f"Error fixing {fix['file']}: {e}")

    print("\n=== FIX COMPLETE ===")
    print(f"Fixed {len(intersection_fixes)} intersection room IDs")


if __name__ == "__main__":
    fix_intersection_room_ids()
