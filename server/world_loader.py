"""World loader utilities for room ID generation and schema validation.

This module provides functions for generating room IDs and loading world data
with optional schema validation support.
"""

from pathlib import Path
from typing import Any

from .exceptions import ValidationError
from .structured_logging.enhanced_logging_config import get_logger
from .utils.enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)

# Try to import the shared schema validator
try:
    import sys
    # Path is imported at module level (line 1)

    # Add the project root to the path to find the schemas package
    project_root = Path(__file__).parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Try importing with absolute path
    from schemas.validator import SchemaValidator, create_validator

    SCHEMA_VALIDATION_AVAILABLE = True

except ImportError as e:
    SCHEMA_VALIDATION_AVAILABLE = False
    logger.warning("Schema validation not available - schemas package not found", error=str(e))


def generate_room_id(plane: str, zone: str, sub_zone: str, room_file: str) -> str:
    """
    Generate hierarchical room ID from components.

    Args:
        plane: Plane identifier (e.g., 'earth', 'yeng')
        zone: Zone identifier (e.g., 'arkhamcity')
        sub_zone: Sub-zone identifier (e.g., 'french_hill')
        room_file: Room file name without extension (e.g., 'S_Garrison_St_001')

    Returns:
        Hierarchical room ID (e.g., 'earth_arkhamcity_northside_intersection_derby_garrison')
    """
    components = [plane, zone, sub_zone, room_file]
    return "_".join(components)


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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Validator creation errors unpredictable, must handle gracefully
            logger.warning("Could not create schema validator", error=str(e))
            return []

    try:
        errors = validator.validate_room(room_data, file_path)
        if errors and strict_validation:
            log_and_raise_enhanced(
                ValidationError,
                f"Room validation failed: {'; '.join(errors)}",
                operation="validate_room_data",
                file_path=file_path,
                validation_errors=errors,
                details={"file_path": file_path, "validation_errors": errors},
                user_friendly="Room data validation failed",
            )
        if not isinstance(errors, list):
            raise TypeError("validation errors must be a list")
        return errors
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Validation errors unpredictable, must handle gracefully
        if strict_validation:
            log_and_raise_enhanced(
                ValidationError,
                f"Schema validation error for {file_path}: {e}",
                operation="validate_room_data",
                file_path=file_path,
                error_type=type(e).__name__,
                details={"file_path": file_path, "error": str(e), "error_type": type(e).__name__},
                user_friendly="Room data validation failed",
            )
        logger.warning("Schema validation error", file_path=file_path, error=str(e))
        return [f"Validation error: {e}"]


# DEPRECATED: JSON file loading functions have been removed.
# All game data (rooms, zones, subzones) now loads from PostgreSQL.
# These functions are kept for backward compatibility in tests only.
# Production code should use PersistenceLayer or AsyncPersistenceLayer to load from database.
