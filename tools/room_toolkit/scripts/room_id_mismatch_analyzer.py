#!/usr/bin/env python3
"""
Enhanced Room ID Mismatch Analyzer

Integrates with the MythosMUD Room Toolkit to provide comprehensive
ID mismatch analysis with improved reporting and integration.
"""

import json
import sys
from pathlib import Path

# Add the toolkit to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.loader import RoomLoader


def analyze_room_id_mismatches(base_path: str = "./data/rooms", output_file: str = None):
    """Analyze room ID mismatches using the toolkit."""

    print("=== ROOM ID MISMATCH ANALYSIS ===\n")

    # Use the toolkit's loader
    loader = RoomLoader(base_path)

    print("Loading room data...")
    room_database = loader.build_room_database(show_progress=True)

    if not room_database:
        print("❌ No valid rooms found")
        return

    print(f"Analyzing {len(room_database)} rooms for ID mismatches...\n")

    # Get all room IDs
    room_ids = set(room_database.keys())
    print(f"Found {len(room_ids)} unique room IDs\n")

    # Analyze exit references
    mismatches = []
    null_exits = []
    valid_exits = []

    for room_id, room in room_database.items():
        exits = room.get("exits", {})

        for direction, target_id in exits.items():
            if target_id is None:
                null_exits.append(
                    {"source_room": room_id, "direction": direction, "file": room.get("_file_path", "unknown")}
                )
            elif target_id in room_ids:
                valid_exits.append({"source_room": room_id, "target_room": target_id, "direction": direction})
            else:
                # This is a mismatch
                mismatches.append(
                    {
                        "source_room": room_id,
                        "target_id": target_id,
                        "direction": direction,
                        "file": room.get("_file_path", "unknown"),
                        "subzone": room.get("_subzone", "unknown"),
                    }
                )

    # Categorize mismatches
    mismatch_patterns = categorize_mismatches(mismatches, room_ids)

    # Generate comprehensive report
    report = generate_mismatch_report(room_database, valid_exits, null_exits, mismatches, mismatch_patterns)

    # Output results
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Detailed report saved to: {output_file}")

    # Print summary
    print_mismatch_summary(report)


def categorize_mismatches(mismatches, room_ids):
    """Categorize mismatches by pattern."""
    patterns = {
        "missing_room_prefix": [],
        "extra_room_prefix": [],
        "intersection_pattern": [],
        "street_pattern": [],
        "unknown_pattern": [],
    }

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
                    patterns["missing_room_prefix"].append(
                        {
                            "source": source_id,
                            "incorrect": target_id,
                            "correct": corrected_id,
                            "direction": mismatch["direction"],
                            "file": mismatch["file"],
                            "subzone": mismatch["subzone"],
                        }
                    )
                    continue

                # Check if removing "room_" prefix would fix it
                if room_part.startswith("room_"):
                    corrected_id = f"earth_arkham_city_{subzone}_{room_part[5:]}"
                    if corrected_id in room_ids:
                        patterns["extra_room_prefix"].append(
                            {
                                "source": source_id,
                                "incorrect": target_id,
                                "correct": corrected_id,
                                "direction": mismatch["direction"],
                                "file": mismatch["file"],
                                "subzone": mismatch["subzone"],
                            }
                        )
                        continue

        # Check for other patterns
        if "intersection" in target_id:
            patterns["intersection_pattern"].append(mismatch)
        elif any(street in target_id for street in ["_st_", "_ave_", "_ln_"]):
            patterns["street_pattern"].append(mismatch)
        else:
            patterns["unknown_pattern"].append(mismatch)

    return patterns


def generate_mismatch_report(room_database, valid_exits, null_exits, mismatches, patterns):
    """Generate comprehensive mismatch analysis report."""

    # Calculate statistics
    total_exits = len(valid_exits) + len(mismatches) + len(null_exits)

    # Subzone analysis
    subzone_mismatches = {}
    for mismatch in mismatches:
        subzone = mismatch["subzone"]
        if subzone not in subzone_mismatches:
            subzone_mismatches[subzone] = 0
        subzone_mismatches[subzone] += 1

    return {
        "summary": {
            "total_rooms": len(room_database),
            "unique_room_ids": len(set(room_database.keys())),
            "total_exits": total_exits,
            "valid_exits": len(valid_exits),
            "null_exits": len(null_exits),
            "mismatches": len(mismatches),
            "mismatch_rate": len(mismatches) / total_exits if total_exits > 0 else 0,
        },
        "mismatch_patterns": {
            pattern: {
                "count": len(items),
                "examples": items[:5],  # First 5 examples
            }
            for pattern, items in patterns.items()
        },
        "subzone_analysis": subzone_mismatches,
        "null_exits": null_exits,
        "valid_exits": valid_exits,
        "all_mismatches": mismatches,
    }


def print_mismatch_summary(report):
    """Print a formatted summary of the mismatch analysis."""

    print("=== MISMATCH ANALYSIS RESULTS ===\n")

    summary = report["summary"]
    print(f"Total Rooms: {summary['total_rooms']}")
    print(f"Unique Room IDs: {summary['unique_room_ids']}")
    print(f"Total Exits: {summary['total_exits']}")
    print(f"Valid Exits: {summary['valid_exits']}")
    print(f"Null Exits: {summary['null_exits']}")
    print(f"ID Mismatches: {summary['mismatches']}")
    print(f"Mismatch Rate: {summary['mismatch_rate']:.2%}")

    print("\n=== MISMATCH PATTERNS ===")
    patterns = report["mismatch_patterns"]
    for pattern, data in patterns.items():
        if data["count"] > 0:
            print(f"\n{pattern.upper()}: {data['count']} mismatches")
            for item in data["examples"]:
                if pattern == "missing_room_prefix":
                    print(f"  {item['source']} -> {item['direction']} -> {item['incorrect']}")
                    print(f"    Should be: {item['correct']}")
                elif pattern == "extra_room_prefix":
                    print(f"  {item['source']} -> {item['direction']} -> {item['incorrect']}")
                    print(f"    Should be: {item['correct']}")
                else:
                    print(f"  {item['source_room']} -> {item['direction']} -> {item['target_id']}")

    print("\n=== SUBZONE ANALYSIS ===")
    for subzone, count in sorted(report["subzone_analysis"].items()):
        print(f"{subzone}: {count} mismatches")

    # Generate fix recommendations
    print("\n=== FIX RECOMMENDATIONS ===")

    if patterns["missing_room_prefix"]["count"] > 0:
        print(f"\n1. ADD 'room_' PREFIX ({patterns['missing_room_prefix']['count']} fixes):")
        for item in patterns["missing_room_prefix"]["examples"][:3]:
            print(f"   {item['incorrect']} → {item['correct']}")

    if patterns["extra_room_prefix"]["count"] > 0:
        print(f"\n2. REMOVE 'room_' PREFIX ({patterns['extra_room_prefix']['count']} fixes):")
        for item in patterns["extra_room_prefix"]["examples"][:3]:
            print(f"   {item['incorrect']} → {item['correct']}")

    print("\n=== ANALYSIS COMPLETE ===")


def main():
    """Main entry point for command-line usage."""
    import argparse

    parser = argparse.ArgumentParser(description="Analyze room ID mismatches")
    parser.add_argument("--base-path", default="./data/rooms", help="Base directory for room files")
    parser.add_argument("--output", help="Output file for detailed report")

    args = parser.parse_args()

    analyze_room_id_mismatches(args.base_path, args.output)


if __name__ == "__main__":
    main()
