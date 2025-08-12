#!/usr/bin/env python3
"""
Room ID Mismatch Fixer
Fixes room ID mismatches in exit references by adding missing "room_" prefixes
"""

import glob
import json
import os
import shutil


def fix_room_id_mismatches():
    """Fix room ID mismatches in exit references"""

    print("=== ROOM ID MISMATCH FIXER ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Processing {len(rooms)} room files...\n")

    # Build room ID database
    room_ids = set()

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(f)

            room_id = data.get("id", "")
            if room_id:
                room_ids.add(room_id)

        except Exception as e:
            print(f"Error reading {f}: {e}")

    print(f"Found {len(room_ids)} unique room IDs\n")

    # Process rooms and fix mismatches
    fixes_made = []
    total_exits_checked = 0

    for f in rooms:
        try:
            # Read current file
            with open(f, encoding="utf-8") as file:
                data = json.load(f)

            room_id = data.get("id", "")
            exits = data.get("exits", {})
            needs_update = False

            # Check each exit
            for direction, target_id in exits.items():
                total_exits_checked += 1

                if target_id and target_id not in room_ids:
                    # Try to fix by adding "room_" prefix
                    if target_id.startswith("earth_arkham_city_"):
                        parts = target_id.split("_")
                        if len(parts) >= 4:
                            subzone = parts[3]
                            room_part = "_".join(parts[4:])

                            # Check if adding "room_" prefix would fix it
                            corrected_id = f"earth_arkham_city_{subzone}_room_{room_part}"
                            if corrected_id in room_ids:
                                # Fix the exit
                                exits[direction] = corrected_id
                                needs_update = True

                                fixes_made.append(
                                    {
                                        "file": f,
                                        "room_id": room_id,
                                        "direction": direction,
                                        "old_id": target_id,
                                        "new_id": corrected_id,
                                    }
                                )

                                print(f"Fixed: {room_id} -> {direction} -> {target_id} → {corrected_id}")

            # Write updated file if changes were made
            if needs_update:
                # Create backup
                backup_file = f + ".backup"
                shutil.copy2(f, backup_file)

                # Update the exits in the data
                data["exits"] = exits

                # Write updated file
                with open(f, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"Error processing {f}: {e}")

    # Print summary
    print("\n=== FIX SUMMARY ===")
    print(f"Total exits checked: {total_exits_checked}")
    print(f"Fixes made: {len(fixes_made)}")

    if fixes_made:
        print("\n=== DETAILED FIX LOG ===")
        for fix in fixes_made:
            print(f"{fix['room_id']} -> {fix['direction']} -> {fix['old_id']} → {fix['new_id']}")

        # Save fix log
        log_file = "room_id_fix_log.json"
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "summary": {"total_exits_checked": total_exits_checked, "fixes_made": len(fixes_made)},
                    "fixes": fixes_made,
                },
                f,
                indent=2,
            )

        print(f"\nFix log saved to: {log_file}")
    else:
        print("No fixes were needed!")

    print("\n=== FIX COMPLETE ===")


if __name__ == "__main__":
    fix_room_id_mismatches()
