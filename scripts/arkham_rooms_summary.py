#!/usr/bin/env python3
"""
Arkham City Rooms Summary

This script analyzes all rooms in the Arkham City zone and generates
a comprehensive summary and statistics.
"""

import json
import os
from collections import defaultdict
from pathlib import Path


def load_room_data(zone_path: str) -> tuple[dict, dict, set]:
    """Load all room and intersection data from the zone directory."""
    rooms = {}
    intersections = {}
    connections = set()

    zone_dir = Path(zone_path)

    for subzone_dir in zone_dir.iterdir():
        if not subzone_dir.is_dir() or subzone_dir.name == "__pycache__":
            continue

        subzone = subzone_dir.name
        print(f"Processing subzone: {subzone}")

        for file_path in subzone_dir.glob("*.json"):
            if file_path.name == "subzone_config.json" or file_path.name == "zone_config.json":
                continue

            try:
                with open(file_path, encoding="utf-8") as f:
                    data = json.load(f)

                room_id = data["id"]
                room_name = data["name"]
                exits = data.get("exits", {})

                # Determine if this is an intersection or regular room
                if "intersection" in room_id:
                    intersections[room_id] = {"name": room_name, "subzone": subzone, "exits": exits}
                else:
                    rooms[room_id] = {"name": room_name, "subzone": subzone, "exits": exits}

                # Record connections
                for direction, target in exits.items():
                    if target:
                        connections.add((room_id, target, direction))

            except Exception as e:
                print(f"Error loading {file_path}: {e}")

    return rooms, intersections, connections


def analyze_connectivity(rooms: dict, intersections: dict, connections: set):
    """Analyze the connectivity of the rooms."""
    print("\n=== Connectivity Analysis ===")

    # Count connections by direction
    direction_counts = defaultdict(int)
    for _, _, direction in connections:
        direction_counts[direction] += 1

    print("Connections by Direction:")
    for direction, count in sorted(direction_counts.items()):
        print(f"  {direction.title()}: {count}")

    # Find isolated rooms (no connections)
    all_room_ids = set(rooms.keys()) | set(intersections.keys())
    connected_rooms = set()
    for source, target, _ in connections:
        connected_rooms.add(source)
        connected_rooms.add(target)

    isolated_rooms = all_room_ids - connected_rooms
    if isolated_rooms:
        print(f"\nIsolated Rooms ({len(isolated_rooms)}):")
        for room_id in sorted(isolated_rooms):
            if room_id in rooms:
                print(f"  - {rooms[room_id]['name']} ({room_id})")
            else:
                print(f"  - {intersections[room_id]['name']} ({room_id})")
    else:
        print("\nNo isolated rooms found - all rooms are connected!")


def print_detailed_statistics(rooms: dict, intersections: dict, connections: set):
    """Print detailed statistics about the room data."""
    print("\n=== Arkham City Zone Statistics ===")
    print(f"Total Rooms: {len(rooms)}")
    print(f"Total Intersections: {len(intersections)}")
    print(f"Total Connections: {len(connections)}")
    print(f"Total Locations: {len(rooms) + len(intersections)}")

    # Count by subzone
    subzone_rooms = defaultdict(int)
    subzone_intersections = defaultdict(int)

    for room_data in rooms.values():
        subzone_rooms[room_data["subzone"]] += 1

    for intersection_data in intersections.values():
        subzone_intersections[intersection_data["subzone"]] += 1

    print("\nBreakdown by Subzone:")
    all_subzones = set(subzone_rooms.keys()) | set(subzone_intersections.keys())
    for subzone in sorted(all_subzones):
        room_count = subzone_rooms[subzone]
        intersection_count = subzone_intersections[subzone]
        total = room_count + intersection_count
        print(f"  {subzone.title()}: {total} total ({room_count} rooms, {intersection_count} intersections)")


def print_room_listing(rooms: dict, intersections: dict):
    """Print a detailed listing of all rooms by subzone."""
    print("\n=== Detailed Room Listing ===")

    # Group by subzone
    subzone_rooms = defaultdict(list)
    subzone_intersections = defaultdict(list)

    for room_id, room_data in rooms.items():
        subzone_rooms[room_data["subzone"]].append((room_id, room_data))

    for intersection_id, intersection_data in intersections.items():
        subzone_intersections[intersection_data["subzone"]].append((intersection_id, intersection_data))

    # Print by subzone
    all_subzones = set(subzone_rooms.keys()) | set(subzone_intersections.keys())
    for subzone in sorted(all_subzones):
        print(f"\n{subzone.upper()}:")

        # Print rooms
        if subzone_rooms[subzone]:
            print("  Rooms:")
            for room_id, room_data in sorted(subzone_rooms[subzone]):
                print(f"    - {room_data['name']}")
                print(f"      ID: {room_id}")
                # Show exits
                exits = [f"{dir}: {target}" for dir, target in room_data["exits"].items() if target]
                if exits:
                    print(f"      Exits: {', '.join(exits)}")
                else:
                    print("      Exits: None")

        # Print intersections
        if subzone_intersections[subzone]:
            print("  Intersections:")
            for intersection_id, intersection_data in sorted(subzone_intersections[subzone]):
                print(f"    - {intersection_data['name']}")
                print(f"      ID: {intersection_id}")
                # Show exits
                exits = [f"{dir}: {target}" for dir, target in intersection_data["exits"].items() if target]
                if exits:
                    print(f"      Exits: {', '.join(exits)}")
                else:
                    print("      Exits: None")


def generate_dot_file(rooms: dict, intersections: dict, connections: set, output_path: str = "arkham_city_graph.dot"):
    """Generate a DOT file for visualization with Graphviz."""
    print(f"\nGenerating DOT file: {output_path}")

    with open(output_path, "w") as f:
        f.write("digraph ArkhamCity {\n")
        f.write("  rankdir=TB;\n")
        f.write("  node [shape=box, style=filled];\n\n")

        # Define subzone colors
        colors = {
            "campus": "lightgreen",
            "northside": "lightcoral",
            "downtown": "lightblue",
            "merchant": "orange",
            "lower_southside": "plum",
            "uptown": "lightyellow",
            "east_town": "pink",
            "river_town": "cyan",
            "french_hill": "gold",
        }

        # Add nodes
        for room_id, room_data in rooms.items():
            color = colors.get(room_data["subzone"], "white")
            f.write(f'  "{room_id}" [label="{room_data["name"]}", fillcolor="{color}"];\n')

        for intersection_id, intersection_data in intersections.items():
            color = colors.get(intersection_data["subzone"], "white")
            f.write(
                f'  "{intersection_id}" [label="{intersection_data["name"]}", fillcolor="{color}", shape=diamond];\n'
            )

        f.write("\n")

        # Add edges
        for source, target, direction in connections:
            f.write(f'  "{source}" -> "{target}" [label="{direction}"];\n')

        f.write("}\n")

    print(f"DOT file saved as {output_path}")
    print("You can visualize this with Graphviz: dot -Tpng arkham_city_graph.dot -o arkham_city_graph.png")


def main():
    """Main function to analyze the room data."""
    zone_path = "data/rooms/earth/arkham_city"

    if not os.path.exists(zone_path):
        print(f"Error: Zone path {zone_path} not found!")
        return

    print("Loading Arkham City room data...")
    rooms, intersections, connections = load_room_data(zone_path)

    print_detailed_statistics(rooms, intersections, connections)
    analyze_connectivity(rooms, intersections, connections)
    print_room_listing(rooms, intersections)
    generate_dot_file(rooms, intersections, connections)

    print("\n=== Summary ===")
    print(f"Arkham City now has {len(rooms) + len(intersections)} total locations")
    print(
        f"across {len({room['subzone'] for room in rooms.values()} | {intersection['subzone'] for intersection in intersections.values()})} subzones"
    )
    print(f"with {len(connections)} connections between them.")


if __name__ == "__main__":
    main()
