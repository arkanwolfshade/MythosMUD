import json
import os
from typing import Any

from .logging_config import get_logger

logger = get_logger(__name__)

ROOMS_BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "rooms"))

# Try to import the shared schema validator
try:
    from schemas.validator import SchemaValidator, create_validator

    SCHEMA_VALIDATION_AVAILABLE = True
except ImportError:
    SCHEMA_VALIDATION_AVAILABLE = False
    logger.warning("Schema validation not available - schemas package not found")


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
        Hierarchical room ID (e.g., 'earth_arkham_city_northside_Derby_High')
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


def validate_room_data(
    room_data: dict[str, Any], file_path: str, validator: SchemaValidator | None = None, strict_validation: bool = False
) -> list[str]:
    """
    Validate room data against schema if validation is available.

    Args:
        room_data: Room data to validate
        file_path: Path to the room file for error reporting
        validator: Schema validator instance (creates one if None)
        strict_validation: If True, raises exceptions on validation errors

    Returns:
        List of validation error messages (empty if valid)
    """
    if not SCHEMA_VALIDATION_AVAILABLE:
        return []

    if validator is None:
        try:
            validator = create_validator("unified")
        except Exception as e:
            logger.warning(f"Could not create schema validator: {e}")
            return []

    try:
        errors = validator.validate_room(room_data, file_path)
        if errors and strict_validation:
            raise ValueError(f"Room validation failed: {'; '.join(errors)}")
        return errors
    except Exception as e:
        if strict_validation:
            raise
        logger.warning(f"Schema validation error for {file_path}: {e}")
        return [f"Validation error: {e}"]


def load_hierarchical_world(strict_validation: bool = False, enable_schema_validation: bool = True) -> dict[str, Any]:
    """
    Load the complete hierarchical world structure including zones, sub-zones, and rooms.

    Args:
        strict_validation: If True, raises exceptions on validation errors
        enable_schema_validation: If True, validates room data against schema

    Returns:
        Dictionary containing all world data with hierarchical structure
    """
    world_data = {
        "rooms": {},
        "zone_configs": {},
        "subzone_configs": {},
        "room_mappings": {},  # Maps old room IDs to new hierarchical IDs
        "validation_errors": {},  # Track validation errors by room ID
    }

    if not os.path.exists(ROOMS_BASE_PATH):
        return world_data

    # Create schema validator if validation is enabled
    validator = None
    if enable_schema_validation and SCHEMA_VALIDATION_AVAILABLE:
        try:
            validator = create_validator("unified")
        except Exception as e:
            logger.warning(f"Could not create schema validator: {e}")

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

                                    # Validate room data if schema validation is enabled
                                    if enable_schema_validation:
                                        validation_errors = validate_room_data(
                                            room_data, file_path, validator, strict_validation
                                        )
                                        if validation_errors:
                                            world_data["validation_errors"][new_room_id] = validation_errors
                                            if strict_validation:
                                                continue  # Skip invalid rooms in strict mode

                                    world_data["rooms"][new_room_id] = room_data

                                    old_room_id = room_data.get("id")
                                    if old_room_id and old_room_id != new_room_id:
                                        world_data["room_mappings"][old_room_id] = new_room_id

                                    room_data["id"] = new_room_id

                            except (OSError, json.JSONDecodeError) as e:
                                logger.warning(f"Could not load room file {file_path}: {e}")
                                continue

    except OSError as e:
        logger.warning(f"Could not access rooms directory {ROOMS_BASE_PATH}: {e}")

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


def load_rooms(strict_validation: bool = False, enable_schema_validation: bool = True) -> dict[str, Any]:
    """
    Load all rooms from the world structure.

    This function maintains backward compatibility with the original flat structure
    while also supporting the new hierarchical structure.

    Args:
        strict_validation: If True, raises exceptions on validation errors
        enable_schema_validation: If True, validates room data against schema

    Returns:
        Dictionary mapping room IDs to room data
    """
    world_data = load_hierarchical_world(strict_validation, enable_schema_validation)

    # Log validation errors if any
    if world_data.get("validation_errors"):
        error_count = len(world_data["validation_errors"])
        logger.warning(f"Found {error_count} rooms with validation errors")
        for room_id, errors in world_data["validation_errors"].items():
            for error in errors:
                logger.warning(f"Room {room_id}: {error}")

    return world_data["rooms"]


if __name__ == "__main__":
    from .logging_config import get_logger

    logger = get_logger(__name__)
    world_data = load_hierarchical_world()
    logger.info(f"Loaded {len(world_data['rooms'])} rooms:")
    for room_id, room in world_data["rooms"].items():
        env = room.get("resolved_environment", "unknown")
        logger.info(f"- {room_id}: {room['name']} (Environment: {env})")

    logger.info(f"Zone configurations: {len(world_data['zone_configs'])}")
    logger.info(f"Sub-zone configurations: {len(world_data['subzone_configs'])}")
    logger.info(f"Room mappings: {len(world_data['room_mappings'])}")

    if world_data.get("validation_errors"):
        logger.warning(f"Validation errors: {len(world_data['validation_errors'])}")
