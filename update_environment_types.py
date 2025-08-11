#!/usr/bin/env python3
"""
MythosMUD Environment Type Updater
Updates room environment types based on subzone and room ID patterns
"""

import glob
import json
import os
import shutil
from collections import defaultdict


def determine_environment_type(room_id: str, subzone: str) -> str:
    """Determine appropriate environment type based on room ID and subzone"""

    room_id_lower = room_id.lower()

    # Special cases first
    if "campus" in subzone:
        return "campus"

    if "waterfront" in subzone or "river_town" in subzone:
        if "dock" in room_id_lower:
            return "docks"
        else:
            return "waterfront"

    # Intersection rooms
    if "intersection" in room_id_lower:
        return "intersection"

    # Street rooms
    if any(pattern in room_id_lower for pattern in ["_st_", "_ave_", "_ln_"]):
        if "french_hill" in subzone:
            return "street_cobblestone"
        else:
            return "street_paved"

    # Building rooms (not streets or intersections)
    if "room_" in room_id_lower and "intersection" not in room_id_lower:
        if subzone in ["downtown", "merchant"]:
            return "commercial"
        elif subzone in ["french_hill", "northside", "east_town", "lower_southside", "uptown"]:
            return "residential"
        else:
            return "building_interior"

    # Default based on subzone
    subzone_defaults = {
        "downtown": "street_paved",
        "northside": "street_paved",
        "campus": "campus",
        "french_hill": "street_cobblestone",
        "waterfront": "waterfront",
        "merchant": "street_paved",
        "east_town": "street_paved",
        "lower_southside": "street_paved",
        "uptown": "street_paved",
        "river_town": "waterfront",
    }

    return subzone_defaults.get(subzone, "outdoors")


def update_environment_types():
    """Update environment types for all room files"""

    print("=== MYTHOSMUD ENVIRONMENT TYPE UPDATER ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)

    # Skip config files
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Found {len(rooms)} room files to process\n")

    # Process rooms
    updates_made = []
    environment_counts = defaultdict(int)

    for f in rooms:
        try:
            # Read current file
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            # Extract subzone from path
            parts = f.split(os.sep)
            subzone = parts[5] if len(parts) >= 6 else "unknown"

            # Get current and suggested environment
            current_env = data.get("environment", "none")
            room_id = data.get("id", "")
            suggested_env = determine_environment_type(room_id, subzone)

            # Check if update is needed
            if current_env != suggested_env:
                # Create backup
                backup_file = f + ".backup"
                shutil.copy2(f, backup_file)

                # Update environment
                data["environment"] = suggested_env

                # Write updated file
                with open(f, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

                updates_made.append(
                    {"file": f, "id": room_id, "subzone": subzone, "old_env": current_env, "new_env": suggested_env}
                )

                print(f"Updated {room_id}: {current_env} → {suggested_env}")

            # Count environments
            environment_counts[suggested_env] += 1

        except Exception as e:
            print(f"Error processing {f}: {e}")

    # Print summary
    print("\n=== UPDATE SUMMARY ===")
    print(f"Total files processed: {len(rooms)}")
    print(f"Updates made: {len(updates_made)}")

    print("\n=== NEW ENVIRONMENT DISTRIBUTION ===")
    for env, count in sorted(environment_counts.items()):
        print(f"{env}: {count} rooms")

    if updates_made:
        print("\n=== DETAILED UPDATE LOG ===")
        for update in updates_made:
            print(f"{update['id']} ({update['subzone']}): {update['old_env']} → {update['new_env']}")

    # Save update log
    if updates_made:
        log_file = "environment_update_log.json"
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "summary": {
                        "total_processed": len(rooms),
                        "updates_made": len(updates_made),
                        "environment_distribution": dict(environment_counts),
                    },
                    "updates": updates_made,
                },
                f,
                indent=2,
            )

        print(f"\nUpdate log saved to: {log_file}")

    print("\n=== UPDATE COMPLETE ===")


if __name__ == "__main__":
    update_environment_types()
