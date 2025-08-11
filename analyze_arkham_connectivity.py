#!/usr/bin/env python3
"""
Arkham City Connectivity Analyzer
Generates detailed statistics about room connectivity and distribution
"""

import glob
import json
import os
from collections import defaultdict


def analyze_arkham_connectivity():
    """Analyze room distribution and connectivity in Arkham City."""

    # Load all room files
    rooms = glob.glob(os.path.join('data/rooms/earth/arkham_city', '**/*.json'), recursive=True)

    print("=== ARKHAM CITY CONNECTIVITY ANALYSIS ===\n")
    print(f"Total JSON files found: {len(rooms)}")

    # Analyze by subzone
    subzones = defaultdict(int)
    room_data = []

    for f in rooms:
        try:
            with open(f, encoding='utf-8') as file:
                data = json.load(file)

            # Extract subzone from path
            parts = f.split(os.sep)
            if len(parts) >= 6:
                subzone = parts[5]
                subzones[subzone] += 1

            # Store room data for further analysis
            if 'id' in data:
                room_data.append({
                    'id': data['id'],
                    'subzone': subzone,
                    'exits': data.get('exits', {}),
                    'file': f
                })

        except Exception as e:
            print(f"Error loading {f}: {e}")

    print("\n=== SUBZONE DISTRIBUTION ===")
    for subzone, count in sorted(subzones.items()):
        print(f"{subzone}: {count} rooms")

    print("\n=== ROOM ID ANALYSIS ===")
    print(f"Rooms with valid IDs: {len(room_data)}")

    # Analyze exit patterns
    exit_analysis = defaultdict(int)
    null_exits = 0
    valid_exits = 0

    for room in room_data:
        for direction, target in room['exits'].items():
            if target is None:
                null_exits += 1
            else:
                valid_exits += 1
                exit_analysis[direction] += 1

    print(f"Total exits: {null_exits + valid_exits}")
    print(f"Null exits: {null_exits}")
    print(f"Valid exits: {valid_exits}")

    print("\n=== EXIT DIRECTION ANALYSIS ===")
    for direction, count in sorted(exit_analysis.items()):
        print(f"{direction}: {count} exits")

    # Analyze room ID patterns
    print("\n=== ROOM ID PATTERN ANALYSIS ===")
    id_patterns = defaultdict(int)
    for room in room_data:
        if 'room_' in room['id']:
            id_patterns['contains_room_prefix'] += 1
        if 'intersection_' in room['id']:
            id_patterns['intersection_rooms'] += 1
        if 'st_' in room['id']:
            id_patterns['street_rooms'] += 1
        if 'ave_' in room['id']:
            id_patterns['avenue_rooms'] += 1
        if 'ln_' in room['id']:
            id_patterns['lane_rooms'] += 1

    for pattern, count in id_patterns.items():
        print(f"{pattern}: {count} rooms")

    # Analyze connectivity issues
    print("\n=== CONNECTIVITY ISSUE ANALYSIS ===")

    # Find rooms that reference non-existent targets
    all_room_ids = {room['id'] for room in room_data}
    broken_connections = []

    for room in room_data:
        for direction, target in room['exits'].items():
            if target and target not in all_room_ids:
                broken_connections.append({
                    'from': room['id'],
                    'to': target,
                    'direction': direction
                })

    print(f"Broken connections found: {len(broken_connections)}")

    # Group broken connections by pattern
    broken_patterns = defaultdict(int)
    for conn in broken_connections:
        if 'downtown_derby_st_' in conn['to']:
            broken_patterns['downtown_derby_missing_room_prefix'] += 1
        elif 'campus_' in conn['to']:
            broken_patterns['campus_missing_room_prefix'] += 1
        else:
            broken_patterns['other_missing_rooms'] += 1

    for pattern, count in broken_patterns.items():
        print(f"{pattern}: {count} connections")

    # Show some examples of broken connections
    if broken_connections:
        print("\n=== EXAMPLES OF BROKEN CONNECTIONS ===")
        for i, conn in enumerate(broken_connections[:10]):  # Show first 10
            print(f"{i+1}. {conn['from']} -> {conn['to']} ({conn['direction']})")

    print("\n=== ANALYSIS COMPLETE ===")

if __name__ == "__main__":
    analyze_arkham_connectivity()
