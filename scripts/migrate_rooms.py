#!/usr/bin/env python3
"""
Room Migration Script for MythosMUD

This script migrates existing flat room structure to the new hierarchical
format. Based on the dimensional mapping techniques described in the
Pnakotic Manuscripts.
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime


def load_existing_rooms(rooms_path: str) -> dict[str, dict]:
    """
    Load all existing room files from the flat structure.

    Args:
        rooms_path: Path to the rooms directory

    Returns:
        Dictionary mapping room IDs to room data
    """
    existing_rooms = {}

    if not os.path.exists(rooms_path):
        print(f"Warning: Rooms directory {rooms_path} does not exist")
        return existing_rooms

    try:
        for zone_dir in os.listdir(rooms_path):
            zone_path = os.path.join(rooms_path, zone_dir)
            if not os.path.isdir(zone_path):
                continue

            for filename in os.listdir(zone_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(zone_path, filename)
                    try:
                        with open(file_path, encoding="utf-8") as f:
                            room_data = json.load(f)
                            room_id = room_data.get("id")
                            if room_id:
                                existing_rooms[room_id] = room_data
                    except (OSError, json.JSONDecodeError) as e:
                        print(f"Warning: Could not load {file_path}: {e}")

    except OSError as e:
        print(f"Warning: Could not access rooms directory {rooms_path}: {e}")

    return existing_rooms


def create_zone_config(zone_name: str, zone_type: str = "city") -> dict:
    """
    Create a default zone configuration.

    Args:
        zone_name: Name of the zone
        zone_type: Type of zone (city, countryside, etc.)

    Returns:
        Zone configuration dictionary
    """
    return {
        "zone_type": zone_type,
        "environment": "outdoors",
        "description": f"A {zone_type} area in the MythosMUD world",
        "weather_patterns": ["fog", "rain", "overcast"],
        "special_rules": {
            "lucidity_drain_rate": 0.1,
            "npc_spawn_modifier": 1.0,
            "combat_modifier": 1.0,
            "exploration_bonus": 0.5,
        },
    }


def create_subzone_config(subzone_name: str) -> dict:
    """
    Create a default sub-zone configuration.

    Args:
        subzone_name: Name of the sub-zone

    Returns:
        Sub-zone configuration dictionary
    """
    return {
        "environment": "outdoors",
        "description": "A sub-zone within the MythosMUD world",
        "special_rules": {
            "lucidity_drain_rate": 0.05,
            "npc_spawn_modifier": 1.0,
            "combat_modifier": 1.0,
            "exploration_bonus": 0.3,
        },
    }


def determine_zone_type(zone_name: str) -> str:
    """
    Determine the zone type based on the zone name.

    Args:
        zone_name: Name of the zone

    Returns:
        Zone type string
    """
    zone_name_lower = zone_name.lower()

    if any(word in zone_name_lower for word in ["city", "town", "burg"]):
        return "city"
    elif any(word in zone_name_lower for word in ["forest", "woods", "grove"]):
        return "countryside"
    elif any(word in zone_name_lower for word in ["mountain", "peak", "ridge"]):
        return "mountains"
    elif any(word in zone_name_lower for word in ["swamp", "marsh", "bog"]):
        return "swamp"
    elif any(word in zone_name_lower for word in ["desert", "dune", "waste"]):
        return "desert"
    elif any(word in zone_name_lower for word in ["tundra", "ice", "frozen"]):
        return "tundra"
    else:
        return "city"  # Default


def _load_and_validate_rooms(rooms_path: str, messages: list[str]) -> dict[str, dict] | None:
    """Load existing rooms and validate."""
    existing_rooms = load_existing_rooms(rooms_path)
    if not existing_rooms:
        messages.append("No existing rooms found to migrate")
        return None

    messages.append(f"Found {len(existing_rooms)} rooms to migrate")
    return existing_rooms


def _create_backup(rooms_path: str, create_backup_flag: bool, dry_run: bool, messages: list[str]) -> None:
    """Create backup if requested."""
    if create_backup_flag and not dry_run:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"{rooms_path}_backup_{timestamp}"
        try:
            shutil.copytree(rooms_path, backup_dir)
            messages.append(f"Created backup at {backup_dir}")
        except OSError as e:
            messages.append(f"Warning: Could not create backup: {e}")


def _group_rooms_by_zone(existing_rooms: dict[str, dict]) -> dict[str, list[dict]]:
    """Group rooms by zone."""
    zones = {}
    for _room_id, room_info in existing_rooms.items():
        zone = room_info["zone"]
        if zone not in zones:
            zones[zone] = []
        zones[zone].append(room_info)
    return zones


def _create_zone_structure(zone_name: str, zone_type: str, rooms_path: str, dry_run: bool, messages: list[str]) -> str:
    """Create zone directory and config. Returns zone_path."""
    zone_path = os.path.join(rooms_path, "earth", zone_name)
    if not dry_run:
        os.makedirs(zone_path, exist_ok=True)

    zone_config = create_zone_config(zone_name, zone_type)
    zone_config_path = os.path.join(zone_path, "zone_config.json")

    if not dry_run:
        with open(zone_config_path, "w", encoding="utf-8") as f:
            json.dump(zone_config, f, indent=2)

    messages.append(f"Created zone config for {zone_name}")
    return zone_path


def _create_subzone_structure(zone_path: str, default_subzone: str, dry_run: bool, messages: list[str]) -> str:
    """Create sub-zone directory and config. Returns subzone_path."""
    subzone_path = os.path.join(zone_path, default_subzone)
    if not dry_run:
        os.makedirs(subzone_path, exist_ok=True)

    subzone_config = create_subzone_config(default_subzone)
    subzone_config_path = os.path.join(subzone_path, "subzone_config.json")

    if not dry_run:
        with open(subzone_config_path, "w", encoding="utf-8") as f:
            json.dump(subzone_config, f, indent=2)

    return subzone_path


def _migrate_room_file(
    room_info: dict, zone_name: str, default_subzone: str, subzone_path: str, dry_run: bool, messages: list[str]
) -> None:
    """Migrate a single room file."""
    old_room_id = room_info["id"]
    new_room_id = f"earth_{zone_name}_{default_subzone}_{old_room_id}"

    room_info["plane"] = "earth"
    room_info["sub_zone"] = default_subzone
    room_info["id"] = new_room_id

    if "environment" not in room_info:
        room_info["environment"] = "outdoors"

    new_filename = f"{old_room_id}.json"
    new_file_path = os.path.join(subzone_path, new_filename)

    if not dry_run:
        with open(new_file_path, "w", encoding="utf-8") as f:
            json.dump(room_info, f, indent=2)

    messages.append(f"Migrated {old_room_id} -> {new_room_id}")


def migrate_rooms(rooms_path: str, dry_run: bool = False, create_backup_flag: bool = True) -> tuple[bool, list[str]]:
    """
    Migrate existing rooms to the new hierarchical structure.

    Args:
        rooms_path: Path to the rooms directory
        dry_run: If True, don't actually perform the migration
        create_backup_flag: If True, create a backup before migration

    Returns:
        Tuple of (success, list of messages)
    """
    messages = []

    existing_rooms = _load_and_validate_rooms(rooms_path, messages)
    if existing_rooms is None:
        return False, messages

    _create_backup(rooms_path, create_backup_flag, dry_run, messages)

    zones = _group_rooms_by_zone(existing_rooms)
    messages.append(f"Found {len(zones)} zones to migrate")

    for zone_name, zone_rooms in zones.items():
        zone_type = determine_zone_type(zone_name)
        zone_path = _create_zone_structure(zone_name, zone_type, rooms_path, dry_run, messages)

        default_subzone = "main"
        subzone_path = _create_subzone_structure(zone_path, default_subzone, dry_run, messages)

        for room_info in zone_rooms:
            _migrate_room_file(room_info, zone_name, default_subzone, subzone_path, dry_run, messages)

    return True, messages


def main():
    """Main entry point for the migration script."""
    parser = argparse.ArgumentParser(description="Migrate MythosMUD rooms to hierarchical structure")
    parser.add_argument("rooms_path", help="Path to the rooms directory to migrate")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--no-backup", action="store_true", help="Don't create a backup before migration")

    args = parser.parse_args()

    # Resolve relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rooms_path = os.path.abspath(os.path.join(script_dir, args.rooms_path))

    print("Room Migration Script for MythosMUD")
    print(f"Rooms path: {rooms_path}")
    print(f"Dry run: {args.dry_run}")
    print(f"Create backup: {not args.no_backup}")
    print("-" * 50)

    success, messages = migrate_rooms(rooms_path, dry_run=args.dry_run, create_backup_flag=not args.no_backup)

    for message in messages:
        print(message)

    if success:
        print("\nMigration completed successfully!")
        if args.dry_run:
            print("This was a dry run - no changes were made.")
    else:
        print("\nMigration failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
