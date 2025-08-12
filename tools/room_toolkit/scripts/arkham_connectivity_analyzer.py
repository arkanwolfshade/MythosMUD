#!/usr/bin/env python3
"""
Enhanced Arkham City Connectivity Analyzer

Integrates with the MythosMUD Room Toolkit to provide comprehensive
connectivity analysis with improved reporting and integration.
"""

import json
import sys
from pathlib import Path

# Add the toolkit to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.analyzer import RoomAnalyzer
from core.loader import RoomLoader


def analyze_arkham_connectivity(base_path: str = "./data/rooms", output_file: str = None):
    """Analyze room distribution and connectivity in Arkham City using the toolkit."""

    print("=== ARKHAM CITY CONNECTIVITY ANALYSIS ===\n")

    # Use the toolkit's loader
    loader = RoomLoader(base_path)
    analyzer = RoomAnalyzer()

    print("Loading room data...")
    room_database = loader.build_room_database(show_progress=True)

    if not room_database:
        print("❌ No valid rooms found")
        return

    print(f"Loaded {len(room_database)} rooms\n")

    # Filter for Arkham City only
    arkham_rooms = {
        rid: room for rid, room in room_database.items() if room.get("_zone") == "earth" and "arkham_city" in rid
    }

    print(f"Arkham City rooms: {len(arkham_rooms)}")

    # Use the toolkit's analyzer
    connectivity_analysis = analyzer.analyze_connectivity(arkham_rooms)
    environment_analysis = analyzer.analyze_environment_distribution(arkham_rooms)
    zone_analysis = analyzer.analyze_zone_structure(arkham_rooms)

    # Generate comprehensive report
    report = generate_arkham_report(arkham_rooms, connectivity_analysis, environment_analysis, zone_analysis)

    # Output results
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Detailed report saved to: {output_file}")

    # Print summary
    print_summary(report)


def generate_arkham_report(rooms, connectivity, environment, zones):
    """Generate comprehensive Arkham City analysis report."""

    # Subzone distribution
    subzone_distribution = {}
    for room in rooms.values():
        subzone = room.get("_subzone", "unknown")
        if subzone not in subzone_distribution:
            subzone_distribution[subzone] = 0
        subzone_distribution[subzone] += 1

    # Exit pattern analysis
    exit_analysis = {"total": 0, "null": 0, "valid": 0, "by_direction": {}}
    for room in rooms.values():
        exits = room.get("exits", {})
        for direction, target in exits.items():
            exit_analysis["total"] += 1
            if target is None:
                exit_analysis["null"] += 1
            else:
                exit_analysis["valid"] += 1
                if direction not in exit_analysis["by_direction"]:
                    exit_analysis["by_direction"][direction] = 0
                exit_analysis["by_direction"][direction] += 1

    # Room ID pattern analysis
    id_patterns = {
        "contains_room_prefix": 0,
        "intersection_rooms": 0,
        "street_rooms": 0,
        "avenue_rooms": 0,
        "lane_rooms": 0,
    }

    for room_id in rooms.keys():
        if "room_" in room_id:
            id_patterns["contains_room_prefix"] += 1
        if "intersection_" in room_id:
            id_patterns["intersection_rooms"] += 1
        if "_st_" in room_id:
            id_patterns["street_rooms"] += 1
        if "_ave_" in room_id:
            id_patterns["avenue_rooms"] += 1
        if "_ln_" in room_id:
            id_patterns["lane_rooms"] += 1

    # Connectivity issues
    all_room_ids = set(rooms.keys())
    broken_connections = []

    for room_id, room in rooms.items():
        exits = room.get("exits", {})
        for direction, target in exits.items():
            if target and target not in all_room_ids:
                broken_connections.append(
                    {"from": room_id, "to": target, "direction": direction, "subzone": room.get("_subzone", "unknown")}
                )

    # Categorize broken connections
    broken_patterns = {
        "downtown_derby_missing_room_prefix": 0,
        "campus_missing_room_prefix": 0,
        "other_missing_rooms": 0,
    }

    for conn in broken_connections:
        target = conn["to"]
        if "downtown_derby_st_" in target:
            broken_patterns["downtown_derby_missing_room_prefix"] += 1
        elif "campus_" in target:
            broken_patterns["campus_missing_room_prefix"] += 1
        else:
            broken_patterns["other_missing_rooms"] += 1

    return {
        "summary": {
            "total_rooms": len(rooms),
            "subzones": len(subzone_distribution),
            "broken_connections": len(broken_connections),
            "connectivity_score": connectivity["connectivity_stats"]["largest_component"] / len(rooms) if rooms else 0,
        },
        "subzone_distribution": subzone_distribution,
        "exit_analysis": exit_analysis,
        "id_patterns": id_patterns,
        "connectivity_analysis": connectivity,
        "environment_analysis": environment,
        "zone_analysis": zones,
        "broken_connections": {
            "total": len(broken_connections),
            "patterns": broken_patterns,
            "examples": broken_connections[:10],  # First 10 examples
        },
    }


def print_summary(report):
    """Print a formatted summary of the analysis."""

    print("\n=== ARKHAM CITY SUMMARY ===")
    print(f"Total Rooms: {report['summary']['total_rooms']}")
    print(f"Subzones: {report['summary']['subzones']}")
    print(f"Broken Connections: {report['summary']['broken_connections']}")
    print(f"Connectivity Score: {report['summary']['connectivity_score']:.2%}")

    print("\n=== SUBZONE DISTRIBUTION ===")
    for subzone, count in sorted(report["subzone_distribution"].items()):
        print(f"{subzone}: {count} rooms")

    print("\n=== EXIT ANALYSIS ===")
    exit_analysis = report["exit_analysis"]
    print(f"Total Exits: {exit_analysis['total']}")
    print(f"Valid Exits: {exit_analysis['valid']}")
    print(f"Null Exits: {exit_analysis['null']}")

    print("\nExit Directions:")
    for direction, count in sorted(exit_analysis["by_direction"].items()):
        print(f"  {direction}: {count}")

    print("\n=== ROOM ID PATTERNS ===")
    for pattern, count in report["id_patterns"].items():
        print(f"{pattern}: {count} rooms")

    print("\n=== CONNECTIVITY ISSUES ===")
    broken = report["broken_connections"]
    print(f"Total Broken Connections: {broken['total']}")
    for pattern, count in broken["patterns"].items():
        print(f"{pattern}: {count}")

    if broken["examples"]:
        print("\nExamples of Broken Connections:")
        for i, conn in enumerate(broken["examples"], 1):
            print(f"  {i}. {conn['from']} -> {conn['to']} ({conn['direction']})")

    print("\n=== ANALYSIS COMPLETE ===")


def main():
    """Main entry point for command-line usage."""
    import argparse

    parser = argparse.ArgumentParser(description="Analyze Arkham City connectivity")
    parser.add_argument("--base-path", default="./data/rooms", help="Base directory for room files")
    parser.add_argument("--output", help="Output file for detailed report")

    args = parser.parse_args()

    analyze_arkham_connectivity(args.base_path, args.output)


if __name__ == "__main__":
    main()
