import json
import os
from pathlib import Path
from typing import Any

from .exceptions import ValidationError
from .logging.enhanced_logging_config import get_logger
from .utils.enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


# Determine environment-aware rooms path
def _get_rooms_base_path() -> str:
    """
    Get the rooms base path based on the current environment.

    Uses LOGGING_ENVIRONMENT from Pydantic config to determine environment.
    """
    project_root = Path(__file__).parent.parent

    # Use LOGGING_ENVIRONMENT from Pydantic config, with fallback to legacy config path
    environment = os.getenv("LOGGING_ENVIRONMENT", "local")
    if not environment or environment not in ["local", "unit_test", "e2e_test", "production"]:
        # Fallback: try to extract from legacy config path
        config_path = os.getenv("MYTHOSMUD_CONFIG_PATH", "")
        if "unit_test" in config_path:
            environment = "unit_test"
        elif "e2e_test" in config_path:
            environment = "e2e_test"

    # Try environment-specific path first, fallback to generic data/rooms
    env_rooms_path = project_root / "data" / environment / "rooms"
    generic_rooms_path = project_root / "data" / "rooms"

    if env_rooms_path.exists():
        return str(env_rooms_path)
    else:
        return str(generic_rooms_path)


ROOMS_BASE_PATH = _get_rooms_base_path()

# Try to import the shared schema validator
try:
    import sys
    from pathlib import Path

    # Add the project root to the path to find the schemas package
    project_root = Path(__file__).parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Try importing with absolute path
    from schemas.validator import SchemaValidator, create_validator

    SCHEMA_VALIDATION_AVAILABLE = True

except ImportError as e:
    SCHEMA_VALIDATION_AVAILABLE = False
    logger.warning(f"Schema validation not available - schemas package not found: {e}")


def load_zone_config(zone_path: str) -> dict[str, Any] | None:
    """
    Load zone configuration from zone_config.json file.

    Args:
        zone_path: Path to the zone directory

    Returns:
        Zone configuration dictionary or None if not found
    """
    config_path = os.path.join(zone_path, "zone_config.json")
    context = create_error_context()
    context.metadata["operation"] = "load_zone_config"
    context.metadata["zone_path"] = zone_path
    context.metadata["config_path"] = config_path

    try:
        logger.debug("Loading zone configuration", config_path=config_path, zone_path=zone_path)
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
        logger.debug(
            "Zone configuration loaded successfully",
            config_path=config_path,
            config_keys=list(config.keys()) if isinstance(config, dict) else "non-dict",
        )
        return config
    except (OSError, json.JSONDecodeError) as e:
        logger.warning(
            "Could not load zone configuration",
            config_path=config_path,
            zone_path=zone_path,
            error=str(e),
            error_type=type(e).__name__,
        )
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
    context = create_error_context()
    context.metadata["operation"] = "load_subzone_config"
    context.metadata["subzone_path"] = subzone_path
    context.metadata["config_path"] = config_path

    try:
        with open(config_path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        logger.warning(
            "Could not load sub-zone configuration",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        return None


def generate_room_id(plane: str, zone: str, sub_zone: str, room_file: str) -> str:
    """
    Generate hierarchical room ID from components.

    Args:
        plane: Plane identifier (e.g., 'earth', 'yeng')
        zone: Zone identifier (e.g., 'arkhamcity')
        sub_zone: Sub-zone identifier (e.g., 'french_hill')
        room_file: Room file name without extension (e.g., 'S_Garrison_St_001')

    Returns:
        Hierarchical room ID (e.g., 'earth_arkhamcity_intersection_derby_high')
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
            context = create_error_context()
            context.metadata["operation"] = "validate_room_data"
            context.metadata["file_path"] = file_path
            context.metadata["validation_errors"] = errors
            log_and_raise_enhanced(
                ValidationError,
                f"Room validation failed: {'; '.join(errors)}",
                context=context,
                details={"file_path": file_path, "validation_errors": errors},
                user_friendly="Room data validation failed",
            )
        return errors
    except Exception as e:
        if strict_validation:
            context = create_error_context()
            context.metadata["operation"] = "validate_room_data"
            context.metadata["file_path"] = file_path
            context.metadata["error_type"] = type(e).__name__
            log_and_raise_enhanced(
                ValidationError,
                f"Schema validation error for {file_path}: {e}",
                context=context,
                details={"file_path": file_path, "error": str(e), "error_type": type(e).__name__},
                user_friendly="Room data validation failed",
            )
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

    rooms_path = Path(ROOMS_BASE_PATH)
    if not rooms_path.exists():
        return world_data

    # Create schema validator if validation is enabled
    validator = None
    if enable_schema_validation and SCHEMA_VALIDATION_AVAILABLE:
        try:
            validator = create_validator("unified")
        except Exception as e:
            logger.warning(f"Could not create schema validator: {e}")

    try:
        for plane_path in rooms_path.iterdir():
            if not plane_path.is_dir():
                continue
            plane = plane_path.name

            for zone_path in plane_path.iterdir():
                if not zone_path.is_dir():
                    continue
                zone = zone_path.name

                zone_config = load_zone_config(str(zone_path))
                if zone_config:
                    world_data["zone_configs"][f"{plane}/{zone}"] = zone_config

                for subzone_path in zone_path.iterdir():
                    if not subzone_path.is_dir():
                        continue
                    sub_zone = subzone_path.name

                    subzone_config = load_subzone_config(str(subzone_path))
                    if subzone_config:
                        config_key = f"{plane}/{zone}/{sub_zone}"
                        world_data["subzone_configs"][config_key] = subzone_config

                    for file_path in subzone_path.iterdir():
                        if file_path.suffix == ".json" and not file_path.stem.startswith("subzone_config"):
                            try:
                                with open(file_path, encoding="utf-8") as f:
                                    room_data = json.load(f)

                                    room_file_name = file_path.stem
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
                                            room_data, str(file_path), validator, strict_validation
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
                                context = create_error_context()
                                context.metadata["operation"] = "load_room_file"
                                context.metadata["file_path"] = str(file_path)
                                context.metadata["error_type"] = type(e).__name__
                                logger.warning(
                                    "Could not load room file",
                                    context=context.to_dict(),
                                    file_path=str(file_path),
                                    error=str(e),
                                    error_type=type(e).__name__,
                                )
                                continue

    except OSError as e:
        context = create_error_context()
        context.metadata["operation"] = "load_hierarchical_world"
        context.metadata["rooms_base_path"] = ROOMS_BASE_PATH
        logger.warning(
            "Could not access rooms directory",
            context=context.to_dict(),
            rooms_base_path=ROOMS_BASE_PATH,
            error=str(e),
            error_type=type(e).__name__,
        )

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
    logger.info(
        "Loading rooms from world structure",
        strict_validation=strict_validation,
        enable_schema_validation=enable_schema_validation,
    )

    world_data = load_hierarchical_world(strict_validation, enable_schema_validation)

    # Log validation errors if any
    if world_data.get("validation_errors"):
        error_count = len(world_data["validation_errors"])
        logger.warning(
            "Found rooms with validation errors",
            error_count=error_count,
            rooms_with_errors=list(world_data["validation_errors"].keys()),
        )
        for room_id, errors in world_data["validation_errors"].items():
            for error in errors:
                logger.warning("Room validation error", room_id=room_id, error=error)

    room_count = len(world_data["rooms"])
    logger.info(
        "Rooms loaded successfully",
        total_rooms=room_count,
        validation_errors=len(world_data.get("validation_errors", [])),
    )

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
