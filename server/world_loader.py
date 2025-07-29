import json
import os
from typing import Any

ROOMS_BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "rooms"))


def load_zone_config(zone_path: str) -> dict[str, Any] | None:
    """
    Load zone configuration from zone_config.json file.

    Args:
        zone_path: Path to the zone directory

    Returns:
        Zone configuration dictionary or None if not found
    """
    config_path = os.path.join(zone_path, "zone_config.json")

    try:
        with open(config_path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def load_subzone_config(subzone_path: str) -> dict[str, Any] | None:
    """
    Load sub-zone configuration from subzone_config.json file.

    Args:
        subzone_path: Path to the sub-zone directory

    Returns:
        Sub-zone configuration dictionary or None if not found
    """
    config_path = os.path.join(subzone_path, "subzone_config.json")

    try:
        with open(config_path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def generate_room_id(plane: str, zone: str, sub_zone: str, room_file: str) -> str:
    """
    Generate hierarchical room ID from components.

    Args:
        plane: Plane identifier (e.g., 'earth', 'yeng')
        zone: Zone identifier (e.g., 'arkham_city')
        sub_zone: Sub-zone identifier (e.g., 'french_hill')
        room_file: Room file name without extension (e.g., 'S_Garrison_St_001')

    Returns:
        Hierarchical room ID (e.g., 'earth_arkham_city_french_hill_S_Garrison_St_001')
    """
    components = [plane, zone, sub_zone, room_file]
    return "_".join(components)


def get_room_environment(
    room_data: dict[str, Any], subzone_config: dict[str, Any] | None, zone_config: dict[str, Any] | None
) -> str:
    """
    Determine room environment using inheritance chain.

    Priority order:
    1. Room-specific environment
    2. Sub-zone environment
    3. Zone environment
    4. Default to 'outdoors'

    Args:
        room_data: Room data dictionary
        subzone_config: Sub-zone configuration or None
        zone_config: Zone configuration or None

    Returns:
        Environment string ('indoors', 'outdoors', 'underwater')
    """
    # Check room-specific environment first
    if room_data.get("environment"):
        return room_data["environment"]

    # Check sub-zone environment
    if subzone_config and subzone_config.get("environment"):
        return subzone_config["environment"]

    # Check zone environment
    if zone_config and zone_config.get("environment"):
        return zone_config["environment"]

    # Default fallback
    return "outdoors"


def load_hierarchical_world() -> dict[str, Any]:
    """
    Load the complete hierarchical world structure including zones, sub-zones, and rooms.

    Returns:
        Dictionary containing all world data with hierarchical structure
    """
    world_data = {
        "rooms": {},
        "zone_configs": {},
        "subzone_configs": {},
        "room_mappings": {},  # Maps old room IDs to new hierarchical IDs
    }

    if not os.path.exists(ROOMS_BASE_PATH):
        return world_data

    try:
        for plane in os.listdir(ROOMS_BASE_PATH):
            plane_path = os.path.join(ROOMS_BASE_PATH, plane)
            if not os.path.isdir(plane_path):
                continue

            for zone in os.listdir(plane_path):
                zone_path = os.path.join(plane_path, zone)
                if not os.path.isdir(zone_path):
                    continue

                zone_config = load_zone_config(zone_path)
                if zone_config:
                    world_data["zone_configs"][f"{plane}/{zone}"] = zone_config

                for sub_zone in os.listdir(zone_path):
                    subzone_path = os.path.join(zone_path, sub_zone)
                    if not os.path.isdir(subzone_path):
                        continue

                    subzone_config = load_subzone_config(subzone_path)
                    if subzone_config:
                        config_key = f"{plane}/{zone}/{sub_zone}"
                        world_data["subzone_configs"][config_key] = subzone_config

                    for filename in os.listdir(subzone_path):
                        if filename.endswith(".json") and not filename.startswith("subzone_config"):
                            file_path = os.path.join(subzone_path, filename)
                            try:
                                with open(file_path, encoding="utf-8") as f:
                                    room_data = json.load(f)

                                    room_file_name = filename.replace(".json", "")
                                    new_room_id = generate_room_id(plane, zone, sub_zone, room_file_name)

                                    if "plane" not in room_data:
                                        room_data["plane"] = plane
                                    if "zone" not in room_data:
                                        room_data["zone"] = zone
                                    if "sub_zone" not in room_data:
                                        room_data["sub_zone"] = sub_zone

                                    room_data["resolved_environment"] = get_room_environment(
                                        room_data, subzone_config, zone_config
                                    )

                                    world_data["rooms"][new_room_id] = room_data

                                    old_room_id = room_data.get("id")
                                    if old_room_id and old_room_id != new_room_id:
                                        world_data["room_mappings"][old_room_id] = new_room_id

                                    room_data["id"] = new_room_id

                            except (OSError, json.JSONDecodeError) as e:
                                print(f"Warning: Could not load room file {file_path}: {e}")
                                continue

    except OSError as e:
        print(f"Warning: Could not access rooms directory {ROOMS_BASE_PATH}: {e}")

    return world_data


def resolve_room_reference(room_id: str, world_data: dict[str, Any] | None = None) -> str | None:
    """
    Resolve room references for both old and new formats.

    Args:
        room_id: Room ID to resolve
        world_data: World data dictionary (loads if not provided)

    Returns:
        Resolved room ID or None if not found
    """
    if world_data is None:
        world_data = load_hierarchical_world()

    # Check if it's already a hierarchical ID
    if room_id in world_data["rooms"]:
        return room_id

    # Check if it's an old ID that maps to a new one
    if room_id in world_data["room_mappings"]:
        return world_data["room_mappings"][room_id]

    return None


def load_rooms() -> dict[str, Any]:
    """
    Load all rooms from the world structure.

    This function maintains backward compatibility with the original flat structure
    while also supporting the new hierarchical structure.

    Returns:
        Dictionary mapping room IDs to room data
    """
    world_data = load_hierarchical_world()
    return world_data["rooms"]


if __name__ == "__main__":
    world_data = load_hierarchical_world()
    print(f"Loaded {len(world_data['rooms'])} rooms:")
    for room_id, room in world_data["rooms"].items():
        env = room.get("resolved_environment", "unknown")
        print(f"- {room_id}: {room['name']} (Environment: {env})")

    print(f"\nZone configurations: {len(world_data['zone_configs'])}")
    print(f"Sub-zone configurations: {len(world_data['subzone_configs'])}")
    print(f"Room mappings: {len(world_data['room_mappings'])}")
