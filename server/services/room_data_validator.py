"""
Room data validation utilities for MythosMUD.

This module provides validation logic for room data structures,
ensuring data integrity and consistency across the synchronization system.
"""

import re
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomDataValidator:
    """Validates room data structure and content."""

    @staticmethod
    def validate_room_data(room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Validate room data structure and content.

        Args:
            room_data: Room data to validate

        Returns:
            Dict[str, Any]: Validation result with is_valid flag and errors list
        """
        errors = []

        try:
            # Validate required fields
            errors.extend(RoomDataValidator.validate_required_fields(room_data))

            # Validate field types
            errors.extend(RoomDataValidator.validate_field_types(room_data))

            # Validate occupant consistency
            errors.extend(RoomDataValidator.validate_occupant_consistency(room_data))

            # Validate room ID format
            if "id" in room_data and not RoomDataValidator.is_valid_room_id(room_data["id"]):
                errors.append(f"Invalid room ID format: {room_data['id']}")

            is_valid = len(errors) == 0

            logger.debug(
                "Room data validation completed",
                room_id=room_data.get("id"),
                is_valid=is_valid,
                error_count=len(errors),
            )

            return {"is_valid": is_valid, "errors": errors, "room_id": room_data.get("id")}

        except (AttributeError, TypeError) as e:
            logger.error("Error validating room data", error=str(e), exc_info=True)
            return {"is_valid": False, "errors": [f"Validation error: {str(e)}"], "room_id": room_data.get("id")}

    @staticmethod
    def validate_required_fields(room_data: dict[str, Any]) -> list[str]:
        """
        Validate that all required fields are present.

        Args:
            room_data: Room data to validate

        Returns:
            List[str]: List of validation errors
        """
        errors = []
        required_fields = ["id", "name", "description"]
        for field in required_fields:
            if field not in room_data or room_data[field] is None:
                errors.append(f"Missing required field: {field}")
        return errors

    @staticmethod
    def validate_field_types(room_data: dict[str, Any]) -> list[str]:
        """
        Validate field types.

        Args:
            room_data: Room data to validate

        Returns:
            List[str]: List of validation errors
        """
        errors = []
        field_validations: list[tuple[str, type[Any] | tuple[type[Any], ...], str]] = [
            ("id", str, "Field 'id' must be a string"),
            ("name", str, "Field 'name' must be a string"),
            ("description", str, "Field 'description' must be a string"),
            ("timestamp", (int, float), "Field 'timestamp' must be a number"),
        ]

        for field_name, expected_type, error_message in field_validations:
            if field_name in room_data and not isinstance(room_data[field_name], expected_type):
                errors.append(error_message)

        return errors

    @staticmethod
    def validate_occupant_consistency(room_data: dict[str, Any]) -> list[str]:
        """
        Validate occupant count consistency.

        Args:
            room_data: Room data to validate

        Returns:
            List[str]: List of validation errors
        """
        errors = []

        if "occupants" in room_data and "occupant_count" in room_data:
            occupants = room_data["occupants"]
            occupant_count = room_data["occupant_count"]

            if isinstance(occupants, list) and occupant_count != len(occupants):
                errors.append(f"Occupant count mismatch: expected {len(occupants)}, got {occupant_count}")

        return errors

    @staticmethod
    def is_valid_room_id(room_id: str) -> bool:
        """
        Validate room ID format.

        Args:
            room_id: Room ID to validate

        Returns:
            bool: True if room ID format is valid
        """
        try:
            # Basic validation - should not be empty and should contain valid characters
            if not room_id or not isinstance(room_id, str):
                return False

            # Room IDs should contain alphanumeric characters, underscores, and hyphens
            pattern = r"^[a-zA-Z0-9_-]+$"
            return bool(re.match(pattern, room_id))

        except (AttributeError, TypeError, re.error) as e:
            logger.warning(
                "Error validating room ID format", room_id=room_id, error=str(e), error_type=type(e).__name__
            )
            return False

    @staticmethod
    def check_occupant_count_consistency(room_data: dict[str, Any]) -> list[str]:
        """
        Check if occupant count matches the actual occupants list length.

        Args:
            room_data: Room data to check

        Returns:
            List[str]: List of inconsistency messages, empty if consistent
        """
        inconsistencies = []
        if "occupants" in room_data and "occupant_count" in room_data:
            occupants = room_data["occupants"]
            occupant_count = room_data["occupant_count"]

            if isinstance(occupants, list) and occupant_count != len(occupants):
                inconsistencies.append(f"Occupant count mismatch: expected {len(occupants)}, got {occupant_count}")

        return inconsistencies

    @staticmethod
    def check_duplicate_occupants(room_data: dict[str, Any]) -> list[str]:
        """
        Check for duplicate occupants in the room.

        Args:
            room_data: Room data to check

        Returns:
            List[str]: List of inconsistency messages, empty if consistent
        """
        inconsistencies = []
        if "occupants" in room_data and isinstance(room_data["occupants"], list):
            occupants = room_data["occupants"]
            if len(occupants) != len(set(occupants)):
                inconsistencies.append("Duplicate occupants found in room")

        return inconsistencies

    @staticmethod
    def check_empty_room_with_occupants(room_data: dict[str, Any]) -> list[str]:
        """
        Check if room has occupants but no name.

        Args:
            room_data: Room data to check

        Returns:
            List[str]: List of inconsistency messages, empty if consistent
        """
        inconsistencies = []
        if room_data.get("name", "").strip() == "" and room_data.get("occupant_count", 0) > 0:
            inconsistencies.append("Room has occupants but no name")

        return inconsistencies

    @staticmethod
    def validate_room_consistency(room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Validate room data consistency.

        Args:
            room_data: Room data to validate for consistency

        Returns:
            Dict[str, Any]: Consistency validation result
        """
        try:
            inconsistencies = []

            # Check occupant count consistency
            inconsistencies.extend(RoomDataValidator.check_occupant_count_consistency(room_data))

            # Check for duplicate occupants
            inconsistencies.extend(RoomDataValidator.check_duplicate_occupants(room_data))

            # Check for empty room with occupants
            inconsistencies.extend(RoomDataValidator.check_empty_room_with_occupants(room_data))

            is_consistent = len(inconsistencies) == 0

            logger.debug(
                "Room consistency validation completed",
                room_id=room_data.get("id"),
                is_consistent=is_consistent,
                inconsistency_count=len(inconsistencies),
            )

            return {"is_consistent": is_consistent, "inconsistencies": inconsistencies, "room_id": room_data.get("id")}

        except (AttributeError, TypeError) as e:
            logger.error("Error validating room consistency", error=str(e), exc_info=True)
            return {
                "is_consistent": False,
                "inconsistencies": [f"Consistency check error: {str(e)}"],
                "room_id": room_data.get("id"),
            }
