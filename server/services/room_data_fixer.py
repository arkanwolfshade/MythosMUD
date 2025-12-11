"""
Room data fixing utilities for MythosMUD.

This module provides automatic fixing logic for room data structures,
applying corrections when validation issues are detected.
"""

import time
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomDataFixer:
    """Applies automatic fixes to room data when validation issues are detected."""

    @staticmethod
    def fix_missing_name(fixed_data: dict[str, Any], errors: list[str]) -> None:
        """Fix missing name field."""
        if "Missing required field: name" in errors:
            fixed_data["name"] = f"Room {fixed_data.get('id', 'unknown')}"

    @staticmethod
    def fix_missing_description(fixed_data: dict[str, Any], errors: list[str]) -> None:
        """Fix missing description field."""
        if "Missing required field: description" in errors:
            fixed_data["description"] = "No description available"

    @staticmethod
    def fix_occupant_count_mismatch(fixed_data: dict[str, Any], errors: list[str]) -> None:
        """Fix occupant count mismatch."""
        has_mismatch = any("Occupant count mismatch" in error for error in errors)
        if has_mismatch and "occupants" in fixed_data and isinstance(fixed_data["occupants"], list):
            fixed_data["occupant_count"] = len(fixed_data["occupants"])

    @staticmethod
    def fix_missing_timestamp(fixed_data: dict[str, Any]) -> None:
        """Fix missing timestamp field."""
        if "timestamp" not in fixed_data:
            fixed_data["timestamp"] = time.time()

    @staticmethod
    def count_applied_fixes(errors: list[str]) -> int:
        """Count the number of fixes that were applied."""
        return len([e for e in errors if e.startswith("Missing") or "mismatch" in e])

    @staticmethod
    def apply_room_data_fixes(room_data: dict[str, Any], errors: list[str]) -> dict[str, Any]:
        """
        Apply automatic fixes to room data when possible.

        Args:
            room_data: Room data to fix
            errors: List of validation errors

        Returns:
            Dict[str, Any]: Fixed room data
        """
        try:
            fixed_data = room_data.copy()

            # Apply all fixes
            RoomDataFixer.fix_missing_name(fixed_data, errors)
            RoomDataFixer.fix_missing_description(fixed_data, errors)
            RoomDataFixer.fix_occupant_count_mismatch(fixed_data, errors)
            RoomDataFixer.fix_missing_timestamp(fixed_data)

            logger.info(
                "Applied room data fixes",
                room_id=fixed_data.get("id"),
                fixes_applied=RoomDataFixer.count_applied_fixes(errors),
            )

            return fixed_data

        except (AttributeError, TypeError) as e:
            logger.error("Error applying room data fixes", error=str(e), exc_info=True)
            return room_data
