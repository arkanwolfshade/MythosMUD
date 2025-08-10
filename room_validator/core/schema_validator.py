"""
Schema validator for room definition files.

This module handles JSON schema validation of room definitions,
supporting both legacy string format and new object format for exits.
"""

import json
from pathlib import Path

from jsonschema import ValidationError, validate


class SchemaValidator:
    """
    Validates room definitions against JSON schema.

    Supports both legacy string format and new object format for exits,
    as documented in the restricted archives of dimensional mapping.
    """

    def __init__(self, schema_path: str = "./schemas/unified_room_schema.json"):
        """
        Initialize the schema validator.

        Args:
            schema_path: Path to the JSON schema file
        """
        self.schema_path = Path(schema_path)
        self.schema = None
        self._load_schema()

    def _load_schema(self) -> None:
        """Load and cache the JSON schema."""
        try:
            with open(self.schema_path, encoding="utf-8") as f:
                self.schema = json.load(f)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}") from exc
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid schema file: {e}") from e

    def validate_room(self, room_data: dict, file_path: str = "") -> list[str]:
        """
        Validate a single room against the schema.

        Args:
            room_data: Room data to validate
            file_path: Optional file path for error reporting

        Returns:
            List of validation error messages
        """
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

    def normalize_exits(self, room_data: dict) -> dict:
        """
        Convert legacy string format exits to new object format internally.

        This allows the validator to work with both formats while
        maintaining backward compatibility.

        Args:
            room_data: Room data with potentially legacy exit format

        Returns:
            Room data with normalized exit format
        """
        normalized = room_data.copy()
        exits = normalized.get("exits", {})
        normalized_exits = {}

        for direction, exit_data in exits.items():
            if exit_data is None:
                normalized_exits[direction] = None
            elif isinstance(exit_data, str):
                # Legacy format: convert to new format
                normalized_exits[direction] = {"target": exit_data, "flags": []}
            elif isinstance(exit_data, dict):
                # New format: ensure it has required fields
                if "target" in exit_data:
                    normalized_exits[direction] = {"target": exit_data["target"], "flags": exit_data.get("flags", [])}
                else:
                    normalized_exits[direction] = exit_data
            else:
                # Invalid format: preserve as-is for schema validation to catch
                normalized_exits[direction] = exit_data

        normalized["exits"] = normalized_exits
        return normalized

    def validate_room_file(self, file_path: Path) -> list[str]:
        """
        Validate a room file against the schema.

        Args:
            file_path: Path to the room JSON file

        Returns:
            List of validation error messages
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                room_data = json.load(f)

            return self.validate_room(room_data, str(file_path))

        except json.JSONDecodeError as e:
            return [f"{file_path}: Invalid JSON: {e}"]
        except Exception as e:
            return [f"{file_path}: Error reading file: {e}"]

    def validate_room_database(self, room_database: dict[str, dict]) -> dict[str, list[str]]:
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

    def get_exit_target(self, exit_data) -> str | None:
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

    def get_exit_flags(self, exit_data) -> list[str]:
        """
        Extract flags from exit data, handling both formats.

        Args:
            exit_data: Exit data in either string or object format

        Returns:
            List of exit flags
        """
        if isinstance(exit_data, dict):
            return exit_data.get("flags", [])
        else:
            return []

    def is_one_way_exit(self, exit_data) -> bool:
        """
        Check if an exit is marked as one-way.

        Args:
            exit_data: Exit data in either string or object format

        Returns:
            True if exit is marked as one-way
        """
        return "one_way" in self.get_exit_flags(exit_data)

    def is_self_reference_exit(self, exit_data) -> bool:
        """
        Check if an exit is marked as self-reference.

        Args:
            exit_data: Exit data in either string or object format

        Returns:
            True if exit is marked as self-reference
        """
        return "self_reference" in self.get_exit_flags(exit_data)

    def validate_subzone_config(self, config_data: dict, file_path: str = "") -> list[str]:
        """
        Validate a sub-zone configuration against its schema.

        Args:
            config_data: Sub-zone configuration data
            file_path: Optional file path for error reporting

        Returns:
            List of validation error messages
        """
        errors = []
        schema_path = Path(self.schema_path.parent, "subzone_schema.json")

        try:
            with open(schema_path, encoding="utf-8") as f:
                schema = json.load(f)

            validate(instance=config_data, schema=schema)
        except FileNotFoundError:
            errors.append(f"Sub-zone schema not found: {schema_path}")
        except ValidationError as e:
            path = " -> ".join(str(p) for p in e.path) if e.path else "root"
            error_msg = f"Schema validation failed at {path}: {e.message}"
            if file_path:
                error_msg = f"{file_path}: {error_msg}"
            errors.append(error_msg)
        except Exception as e:
            error_msg = f"Validation error: {e}"
            if file_path:
                error_msg = f"{file_path}: {error_msg}"
            errors.append(error_msg)

        return errors

    def validate_zone_config(self, config_data: dict, file_path: str = "") -> list[str]:
        """
        Validate a zone configuration against its schema.

        Args:
            config_data: Zone configuration data
            file_path: Optional file path for error reporting

        Returns:
            List of validation error messages
        """
        errors = []
        schema_path = Path(self.schema_path.parent, "zone_schema.json")

        try:
            with open(schema_path, encoding="utf-8") as f:
                schema = json.load(f)

            validate(instance=config_data, schema=schema)
        except FileNotFoundError:
            errors.append(f"Zone schema not found: {schema_path}")
        except ValidationError as e:
            path = " -> ".join(str(p) for p in e.path) if e.path else "root"
            error_msg = f"Schema validation failed at {path}: {e.message}"
            if file_path:
                error_msg = f"{file_path}: {error_msg}"
            errors.append(error_msg)
        except Exception as e:
            error_msg = f"Validation error: {e}"
            if file_path:
                error_msg = f"{file_path}: {error_msg}"
            errors.append(error_msg)

        return errors
