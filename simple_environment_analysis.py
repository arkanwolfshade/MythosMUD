#!/usr/bin/env python3
"""
Simple MythosMUD Environment Type Analysis
"""

import glob
import json
import os
from collections import defaultdict


def analyze_environments():
    """Analyze current environment types in room files"""

    print("=== MYTHOSMUD ENVIRONMENT ANALYSIS ===\n")

    # Load all room files
    rooms = glob.glob(os.path.join("data/rooms/earth/arkham_city", "**/*.json"), recursive=True)

    # Skip config files
    rooms = [f for f in rooms if os.path.basename(f) not in ["zone_config.json", "subzone_config.json"]]

    print(f"Found {len(rooms)} room files\n")

    # Analyze environments
    environment_counts = defaultdict(int)
    subzone_environments = defaultdict(lambda: defaultdict(int))
    room_examples = defaultdict(list)

    for f in rooms:
        try:
            with open(f, encoding="utf-8") as file:
                data = json.load(file)

            # Extract subzone from path
            parts = f.split(os.sep)
            subzone = parts[5] if len(parts) >= 6 else "unknown"

            # Get environment
            env = data.get("environment", "none")
            room_id = data.get("id", "unknown")

            # Count environments
            environment_counts[env] += 1
            subzone_environments[subzone][env] += 1

            # Store example
            if len(room_examples[env]) < 3:  # Keep up to 3 examples per environment
                room_examples[env].append({"id": room_id, "subzone": subzone, "name": data.get("name", ""), "file": f})

        except Exception as e:
            print(f"Error reading {f}: {e}")

    # Print results
    print("=== CURRENT ENVIRONMENT DISTRIBUTION ===")
    for env, count in sorted(environment_counts.items()):
        print(f"{env}: {count} rooms")

    print("\n=== ENVIRONMENT EXAMPLES ===")
    for env, examples in room_examples.items():
        print(f"\n{env}:")
        for example in examples:
            print(f"  - {example['id']} ({example['subzone']})")

    print("\n=== SUBZONE BREAKDOWN ===")
    for subzone, envs in sorted(subzone_environments.items()):
        print(f"\n{subzone}:")
        for env, count in sorted(envs.items()):
            print(f"  {env}: {count} rooms")

    # Suggest environment types based on subzone
    print("\n=== SUGGESTED ENVIRONMENT TYPES BY SUBZONE ===")

    subzone_suggestions = {
        "downtown": ["street_paved", "intersection", "commercial"],
        "northside": ["street_paved", "residential", "intersection"],
        "campus": ["campus", "institution", "park"],
        "french_hill": ["hillside", "residential", "cemetery"],
        "waterfront": ["waterfront", "docks", "industrial"],
        "merchant": ["commercial", "street_paved"],
        "east_town": ["residential", "street_paved"],
        "lower_southside": ["residential", "street_paved"],
        "uptown": ["residential", "street_paved"],
        "river_town": ["waterfront", "docks"],
    }

    for subzone, suggestions in subzone_suggestions.items():
        if subzone in subzone_environments:
            print(f"\n{subzone}:")
            current_envs = list(subzone_environments[subzone].keys())
            print(f"  Current: {', '.join(current_envs)}")
            print(f"  Suggested: {', '.join(suggestions)}")

    print("\n=== ANALYSIS COMPLETE ===")


if __name__ == "__main__":
    analyze_environments()
