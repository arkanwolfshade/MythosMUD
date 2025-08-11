"""
Shared schema validator for room definition files.

This module provides JSON schema validation functionality that can be used
by both the room validator tool and the server for validating room data.
"""

import json
import re
from pathlib import Path
from typing import Any

try:
    from jsonschema import ValidationError, validate

    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    ValidationError = Exception


class SchemaValidator:
    """
    Validates room definitions against JSON schema.

    This validator can be used by both the room validator tool and the server
    to ensure consistent validation of room data.
    """

    def __init__(self, schema_path: str | None = None):
        """
        Initialize the schema validator.

        Args:
            schema_path: Path to the JSON schema file. If None, uses the default
                        unified room schema from the schemas directory.
        """
        if schema_path is None:
            # Use the default unified schema from the schemas directory
            schema_path = Path(__file__).parent / "unified_room_schema.json"

        self.schema_path = Path(schema_path)
        self.schema = None
        self._load_schema()

    def _load_schema(self) -> None:
        """Load and cache the JSON schema."""
        if not JSONSCHEMA_AVAILABLE:
            raise ImportError("jsonschema library is required for schema validation")

        try:
            with open(self.schema_path, encoding="utf-8") as f:
                self.schema = json.load(f)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}") from exc
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid schema file: {e}") from e

    def validate_room(self, room_data: dict[str, Any], file_path: str = "") -> list[str]:
        """
        Validate a single room against the schema.

        Args:
            room_data: Room data to validate
            file_path: Optional file path for error reporting

        Returns:
            List of validation error messages (empty if valid)
        """
        if not JSONSCHEMA_AVAILABLE:
            return [f"{file_path}: Schema validation not available (jsonschema not installed)"]

        errors = []

        try:
            validate(instance=room_data, schema=self.schema)
        except ValidationError as e:
            # Format validation error for better readability
            path = " -> ".join(str(p) for p in e.path) if e.path else "root"
            error_msg = f"Schema validation failed at {path}: {e.message}"
            if file_path:
                error_msg = f"{file_path}: {error_msg}"
            errors.append(error_msg)

        return errors

    def validate_room_file(self, file_path: Path) -> list[str]:
        """
        Validate a room file against the schema.

        Args:
            file_path: Path to the room JSON file

        Returns:
            List of validation error messages (empty if valid)
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                room_data = json.load(f)

            return self.validate_room(room_data, str(file_path))

        except json.JSONDecodeError as e:
            return [f"{file_path}: Invalid JSON: {e}"]
        except Exception as e:
            return [f"{file_path}: Error reading file: {e}"]

    def validate_room_database(self, room_database: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
        """
        Validate all rooms in a database against the schema.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            Dictionary mapping room IDs to lists of validation errors
        """
        validation_results = {}

        for room_id, room_data in room_database.items():
            errors = self.validate_room(room_data, f"Room {room_id}")
            if errors:
                validation_results[room_id] = errors

        return validation_results

    def get_exit_target(self, exit_data: Any) -> str | None:
        """
        Extract target room ID from exit data, handling both formats.

        Args:
            exit_data: Exit data in either string or object format

        Returns:
            Target room ID or None if invalid
        """
        if exit_data is None:
            return None
        elif isinstance(exit_data, str):
            return exit_data
        elif isinstance(exit_data, dict):
            return exit_data.get("target")
        else:
            return None

    def get_exit_flags(self, exit_data: Any) -> list[str]:
        """
        Extract flags from exit data, handling both formats.

        Args:
            exit_data: Exit data in either string or object format

        Returns:
            List of exit flags
        """
        if exit_data is None:
            return []
        elif isinstance(exit_data, str):
            return []
        elif isinstance(exit_data, dict):
            return exit_data.get("flags", [])
        else:
            return []

    def is_room_id_valid(self, room_id: str) -> bool:
        """
        Check if a room ID follows the unified naming schema.

        Args:
            room_id: Room ID to validate

        Returns:
            True if the room ID is valid, False otherwise
        """
        # Regular room pattern: {plane}_{zone}_{sub_zone}_room_{street}_{number:03d}
        room_pattern = r"^[a-z0-9_]+_room_[a-z0-9_]+_[0-9]{3}$"

        # Intersection pattern: {plane}_{zone}_{sub_zone}_intersection_{street_a}_{street_b}
        intersection_pattern = r"^[a-z0-9_]+_intersection_[a-z0-9_]+_[a-z0-9_]+$"

        return bool(re.match(room_pattern, room_id) or re.match(intersection_pattern, room_id))


def create_validator(schema_name: str = "unified") -> SchemaValidator:
    """
    Create a schema validator with the specified schema.

    Args:
        schema_name: Name of the schema to use ("unified", "room", or "intersection")

    Returns:
        SchemaValidator instance
    """
    schemas_dir = Path(__file__).parent

    if schema_name == "unified":
        schema_path = schemas_dir / "unified_room_schema.json"
    elif schema_name == "room":
        schema_path = schemas_dir / "room_schema.json"
    elif schema_name == "intersection":
        schema_path = schemas_dir / "intersection_schema.json"
    else:
        raise ValueError(f"Unknown schema name: {schema_name}")

    return SchemaValidator(str(schema_path))
