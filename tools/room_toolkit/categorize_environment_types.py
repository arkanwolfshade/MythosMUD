#!/usr/bin/env python3
"""
MythosMUD Environment Type Categorizer
Analyzes existing rooms and suggests appropriate environment types
"""

import glob
import json
import os
from collections import defaultdict


def analyze_room_environment(room_data: dict, subzone: str) -> str:
    """Analyze room data and suggest appropriate environment type"""

    # Extract key information
    name = room_data.get("name", "").lower()
    description = room_data.get("description", "").lower()
    room_id = room_data.get("id", "").lower()

    # Check for intersection rooms
    if "intersection" in room_id or "intersection" in name:
        return "intersection"

    # Check for street rooms
    if any(street in room_id for street in ["_st_", "_ave_", "_ln_"]):
        if "cobblestone" in description or "historic" in description:
            return "street_cobblestone"
        else:
            return "street_paved"

    # Check for building interiors
    if any(word in description for word in ["inside", "interior", "shop", "store", "office", "room"]):
        if "university" in description or "campus" in description:
            return "institution"
        elif "residential" in description or "home" in description:
            return "building_interior"
        else:
            return "commercial"

    # Check for campus areas
    if "campus" in subzone or "university" in description:
        return "campus"

    # Check for waterfront areas
    if "waterfront" in subzone or any(word in description for word in ["harbor", "river", "dock"]):
        return "waterfront"

    # Check for cemetery
    if "cemetery" in description or "burial" in description:
        return "cemetery"

    # Check for parks
    if "park" in description or "garden" in description:
        return "park"

    # Check for hillside areas
    if "french_hill" in subzone or "hillside" in description:
        return "hillside"

    # Check for industrial areas
    if any(word in description for word in ["factory", "warehouse", "industrial"]):
        return "industrial"

    # Check for abandoned areas
    if any(word in description for word in ["abandoned", "derelict", "ruined"]):
        return "abandoned"

    # Default based on subzone
    subzone_defaults = {
        "downtown": "street_paved",
        "northside": "residential",
        "campus": "campus",
        "french_hill": "hillside",
        "waterfront": "waterfront",
        "merchant": "commercial",
        "east_town": "residential",
        "lower_southside": "residential",
        "uptown": "residential",
        "river_town": "waterfront",
    }

    return subzone_defaults.get(subzone, "outdoors")


def categorize_rooms():
    """Categorize all rooms by environment type"""

    print("=== MYTHOSMUD ENVIRONMENT TYPE CATEGORIZATION ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)

    # Skip config files
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Analyzing {len(rooms)} room files...\n")

    # Categorize rooms
    categorized_rooms = []
    environment_counts = defaultdict(int)
    subzone_analysis = defaultdict(lambda: defaultdict(int))

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            # Extract subzone from path
            parts = f.split(os.sep)
            subzone = parts[5] if len(parts) >= 6 else "unknown"

            # Get current environment
            current_env = data.get("environment", "none")

            # Suggest new environment
            suggested_env = analyze_room_environment(data, subzone)

            # Store results
            room_info = {
                "file": f,
                "id": data.get("id", ""),
                "name": data.get("name", ""),
                "subzone": subzone,
                "current_environment": current_env,
                "suggested_environment": suggested_env,
                "needs_update": current_env != suggested_env,
            }

            categorized_rooms.append(room_info)
            environment_counts[suggested_env] += 1
            subzone_analysis[subzone][suggested_env] += 1

        except Exception as e:
            print(f"Error processing {f}: {e}")

    # Print summary statistics
    print("=== ENVIRONMENT TYPE DISTRIBUTION ===")
    for env, count in sorted(environment_counts.items()):
        print(f"{env}: {count} rooms")

    print("\n=== SUBZONE ANALYSIS ===")
    for subzone, envs in sorted(subzone_analysis.items()):
        print(f"\n{subzone}:")
        for env, count in sorted(envs.items()):
            print(f"  {env}: {count} rooms")

    # Show rooms that need updates
    rooms_needing_updates = [r for r in categorized_rooms if r["needs_update"]]

    print("\n=== ROOMS NEEDING ENVIRONMENT UPDATES ===")
    print(f"Total rooms needing updates: {len(rooms_needing_updates)}")

    if rooms_needing_updates:
        print("\nExamples of rooms needing updates:")
        for room in rooms_needing_updates[:10]:  # Show first 10
            print(f"  {room['id']}")
            print(f"    Current: {room['current_environment']}")
            print(f"    Suggested: {room['suggested_environment']}")
            print(f"    Subzone: {room['subzone']}")
            print()

    # Generate update recommendations
    print("=== UPDATE RECOMMENDATIONS ===")

    # Group by current environment
    current_env_groups = defaultdict(list)
    for room in rooms_needing_updates:
        current_env_groups[room["current_environment"]].append(room)

    for current_env, rooms in current_env_groups.items():
        print(f"\nRooms currently using '{current_env}':")
        suggested_counts = defaultdict(int)
        for room in rooms:
            suggested_counts[room["suggested_environment"]] += 1

        for suggested_env, count in sorted(suggested_counts.items()):
            print(f"  → {count} should be '{suggested_env}'")

    # Generate JSON update script
    print("\n=== JSON UPDATE SCRIPT ===")
    print("To update room environment types, you can use this pattern:")
    print()

    for room in rooms_needing_updates[:5]:  # Show first 5 as examples
        print(f"# Update {room['id']}")
        print(f"# Current: {room['current_environment']} → Suggested: {room['suggested_environment']}")
        print(f"# File: {room['file']}")
        print()

    # Save detailed results to file
    results_file = "environment_categorization_results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "summary": {
                    "total_rooms": len(categorized_rooms),
                    "rooms_needing_updates": len(rooms_needing_updates),
                    "environment_distribution": dict(environment_counts),
                    "subzone_analysis": {k: dict(v) for k, v in subzone_analysis.items()},
                },
                "detailed_results": categorized_rooms,
            },
            f,
            indent=2,
        )

    print(f"\nDetailed results saved to: {results_file}")
    print("\n=== CATEGORIZATION COMPLETE ===")


if __name__ == "__main__":
    categorize_rooms()
