#!/usr/bin/env python3
"""
Fix Redundant Intersection Room IDs
Removes the redundant 'earth_arkham_city_' prefix from intersection room IDs
"""

import glob
import json
import os


def fix_redundant_intersection_ids():
    """Fix redundant intersection room IDs"""

    print("=== REDUNDANT INTERSECTION ID FIXER ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Processing {len(rooms)} room files...\n")

    # Find intersection rooms with redundant IDs
    redundant_fixes = []

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            room_id = data.get("id", "")

            # Check if this is a redundant intersection room ID
            # Pattern: earth_arkham_city_{subzone}_earth_arkham_city_intersection_{streets}
            if "_earth_arkham_city_intersection_" in room_id:
                # Extract subzone and intersection part
                parts = room_id.split("_earth_arkham_city_intersection_")
                if len(parts) == 2:
                    subzone_part = parts[0].replace("earth_arkham_city_", "")
                    intersection_part = parts[1]

                    # Create corrected room ID
                    corrected_id = f"earth_arkham_city_{subzone_part}_intersection_{intersection_part}"

                    redundant_fixes.append({"file": f, "old_id": room_id, "new_id": corrected_id})

                    print(f"Found redundant ID: {room_id} → {corrected_id}")

        except Exception as e:
            print(f"Error reading {f}: {e}")

    print(f"\nFound {len(redundant_fixes)} redundant intersection room IDs\n")

    # Apply fixes
    for fix in redundant_fixes:
        try:
            # Read current file
            with open(fix["file"], encoding="utf-8") as file:
                data = json.load(file)

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
    print(f"Fixed {len(redundant_fixes)} redundant intersection room IDs")


if __name__ == "__main__":
    fix_redundant_intersection_ids()
