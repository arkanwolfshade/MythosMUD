#!/usr/bin/env python3
"""
Fix Intersection Exit References
Updates all exit references to use the corrected intersection room IDs
"""

import glob
import json
import os


def fix_intersection_exit_references():
    """Fix exit references to intersection rooms"""

    print("=== INTERSECTION EXIT REFERENCE FIXER ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Processing {len(rooms)} room files...\n")

    # Define the ID mappings (old -> new)
    id_mappings = {
        "earth_arkham_city_intersection_boundary_crane": "earth_arkham_city_campus_intersection_boundary_crane",
        "earth_arkham_city_intersection_curwen_garrison": "earth_arkham_city_downtown_intersection_curwen_garrison",
        "earth_arkham_city_intersection_derby_dyer": "earth_arkham_city_downtown_intersection_derby_dyer",
        "earth_arkham_city_intersection_derby_garrison": "earth_arkham_city_downtown_intersection_derby_garrison",
        "earth_arkham_city_intersection_derby_mass": "earth_arkham_city_downtown_intersection_derby_mass",
        "earth_arkham_city_intersection_derby_peabody": "earth_arkham_city_downtown_intersection_derby_peabody",
        "earth_arkham_city_intersection_derby_federal": "earth_arkham_city_east_town_intersection_derby_federal",
        "earth_arkham_city_intersection_derby_noyes": "earth_arkham_city_east_town_intersection_derby_noyes",
        "earth_arkham_city_intersection_peabody_pickman": "earth_arkham_city_lower_southside_intersection_peabody_pickman",
        "earth_arkham_city_intersection_apple_derby": "earth_arkham_city_northside_intersection_apple_derby",
        "earth_arkham_city_intersection_apple_high": "earth_arkham_city_northside_intersection_apple_high",
        "earth_arkham_city_intersection_brown_curwen": "earth_arkham_city_northside_intersection_brown_curwen",
        "earth_arkham_city_intersection_brown_derby": "earth_arkham_city_northside_intersection_brown_derby",
        "earth_arkham_city_intersection_curwen_gedney": "earth_arkham_city_northside_intersection_curwen_gedney",
        "earth_arkham_city_intersection_curwen_high": "earth_arkham_city_northside_intersection_curwen_high",
        "earth_arkham_city_intersection_curwen_jenkins": "earth_arkham_city_northside_intersection_curwen_jenkins",
        "earth_arkham_city_intersection_derby_gedney": "earth_arkham_city_northside_intersection_derby_gedney",
        "earth_arkham_city_intersection_derby_jenkins": "earth_arkham_city_northside_intersection_derby_jenkins",
        "earth_arkham_city_intersection_derby_halsey": "earth_arkham_city_uptown_intersection_derby_halsey",
    }

    # Process rooms and fix exit references
    fixes_made = []

    for f in rooms:
        try:
            # Read current file
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            room_id = data.get("id", "")
            exits = data.get("exits", {})
            needs_update = False

            # Check each exit
            for direction, target_id in exits.items():
                if target_id in id_mappings:
                    old_id = target_id
                    new_id = id_mappings[target_id]
                    exits[direction] = new_id
                    needs_update = True

                    fixes_made.append(
                        {"file": f, "room_id": room_id, "direction": direction, "old_id": old_id, "new_id": new_id}
                    )

                    print(f"Fixed exit: {room_id} -> {direction} -> {old_id} → {new_id}")

            # Write updated file if changes were made
            if needs_update:
                data["exits"] = exits
                with open(f, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"Error processing {f}: {e}")

    # Print summary
    print("\n=== FIX SUMMARY ===")
    print(f"Exit reference fixes made: {len(fixes_made)}")

    if fixes_made:
        print("\n=== DETAILED FIX LOG ===")
        for fix in fixes_made:
            print(f"{fix['room_id']} -> {fix['direction']} -> {fix['old_id']} → {fix['new_id']}")

    print("\n=== FIX COMPLETE ===")


if __name__ == "__main__":
    fix_intersection_exit_references()
