#!/usr/bin/env python3
"""
Room ID Mismatch Analyzer
Identifies and categorizes room ID mismatches in exit references
"""

import glob
import json
import os
from collections import defaultdict


def analyze_room_id_mismatches():
    """Analyze room ID mismatches in exit references"""

    print("=== ROOM ID MISMATCH ANALYSIS ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Analyzing {len(rooms)} room files for ID mismatches...\n")

    # Build room ID database
    room_ids = set()
    room_files = {}

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(f)

            room_id = data.get("id", "")
            if room_id:
                room_ids.add(room_id)
                room_files[room_id] = f

        except Exception as e:
            print(f"Error reading {f}: {e}")

    print(f"Found {len(room_ids)} unique room IDs\n")

    # Analyze exit references
    mismatches = []
    null_exits = []
    valid_exits = []

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            room_id = data.get("id", "")
            exits = data.get("exits", {})

            for direction, target_id in exits.items():
                if target_id is None:
                    null_exits.append({"source_room": room_id, "direction": direction, "file": f})
                elif target_id in room_ids:
                    valid_exits.append({"source_room": room_id, "target_room": target_id, "direction": direction})
                else:
                    # This is a mismatch
                    mismatches.append(
                        {"source_room": room_id, "target_id": target_id, "direction": direction, "file": f}
                    )

        except Exception as e:
            print(f"Error analyzing {f}: {e}")

    # Categorize mismatches
    mismatch_patterns = defaultdict(list)

    for mismatch in mismatches:
        target_id = mismatch["target_id"]
        source_id = mismatch["source_room"]

        # Try to identify the pattern
        if target_id.startswith("earth_arkham_city_"):
            # Extract the subzone and room part
            parts = target_id.split("_")
            if len(parts) >= 4:
                subzone = parts[3]  # e.g., "downtown", "northside"
                room_part = "_".join(parts[4:])  # e.g., "derby_st_002"

                # Check if adding "room_" prefix would fix it
                corrected_id = f"earth_arkham_city_{subzone}_room_{room_part}"
                if corrected_id in room_ids:
                    mismatch_patterns["missing_room_prefix"].append(
                        {
                            "source": source_id,
                            "incorrect": target_id,
                            "correct": corrected_id,
                            "direction": mismatch["direction"],
                            "file": mismatch["file"],
                        }
                    )
                    continue

                # Check if removing "room_" prefix would fix it
                if room_part.startswith("room_"):
                    corrected_id = f"earth_arkham_city_{subzone}_{room_part[5:]}"
                    if corrected_id in room_ids:
                        mismatch_patterns["extra_room_prefix"].append(
                            {
                                "source": source_id,
                                "incorrect": target_id,
                                "correct": corrected_id,
                                "direction": mismatch["direction"],
                                "file": mismatch["file"],
                            }
                        )
                        continue

        # Check for other patterns
        if "intersection" in target_id:
            mismatch_patterns["intersection_pattern"].append(mismatch)
        elif any(street in target_id for street in ["_st_", "_ave_", "_ln_"]):
            mismatch_patterns["street_pattern"].append(mismatch)
        else:
            mismatch_patterns["unknown_pattern"].append(mismatch)

    # Print results
    print("=== MISMATCH ANALYSIS RESULTS ===\n")

    print(f"Total exits analyzed: {len(valid_exits) + len(mismatches) + len(null_exits)}")
    print(f"Valid exits: {len(valid_exits)}")
    print(f"Null exits: {len(null_exits)}")
    print(f"ID mismatches: {len(mismatches)}")

    print("\n=== MISMATCH PATTERNS ===")

    for pattern, items in mismatch_patterns.items():
        print(f"\n{pattern.upper()}: {len(items)} mismatches")
        for item in items[:5]:  # Show first 5 examples
            if pattern == "missing_room_prefix":
                print(f"  {item['source']} -> {item['direction']} -> {item['incorrect']}")
                print(f"    Should be: {item['correct']}")
            elif pattern == "extra_room_prefix":
                print(f"  {item['source']} -> {item['direction']} -> {item['incorrect']}")
                print(f"    Should be: {item['correct']}")
            else:
                print(f"  {item['source_room']} -> {item['direction']} -> {item['target_id']}")

    # Generate fix recommendations
    print("\n=== FIX RECOMMENDATIONS ===")

    if mismatch_patterns["missing_room_prefix"]:
        print(f"\n1. ADD 'room_' PREFIX ({len(mismatch_patterns['missing_room_prefix'])} fixes):")
        for item in mismatch_patterns["missing_room_prefix"][:3]:
            print(f"   {item['incorrect']} → {item['correct']}")

    if mismatch_patterns["extra_room_prefix"]:
        print(f"\n2. REMOVE 'room_' PREFIX ({len(mismatch_patterns['extra_room_prefix'])} fixes):")
        for item in mismatch_patterns["extra_room_prefix"][:3]:
            print(f"   {item['incorrect']} → {item['correct']}")

    # Save detailed results
    results = {
        "summary": {
            "total_rooms": len(rooms),
            "unique_room_ids": len(room_ids),
            "valid_exits": len(valid_exits),
            "null_exits": len(null_exits),
            "mismatches": len(mismatches),
        },
        "mismatch_patterns": dict(mismatch_patterns),
        "null_exits": null_exits,
        "valid_exits": valid_exits,
    }

    with open("room_id_mismatch_analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\nDetailed analysis saved to: room_id_mismatch_analysis.json")
    print("\n=== ANALYSIS COMPLETE ===")


if __name__ == "__main__":
    analyze_room_id_mismatches()
