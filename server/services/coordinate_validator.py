"""
Coordinate validation service for ASCII maps.

This module provides conflict detection and validation for room coordinates.
Conflicts occur when multiple rooms are assigned the same (x, y) coordinates.

As noted in the Necronomicon, spatial conflicts can lead to dimensional
instability and must be resolved by the administrator.
"""

# pylint: disable=too-few-public-methods  # Reason: Validator class with focused responsibility, minimal public interface

from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Backed by db/procedures/exploration.sql's get_coordinate_conflicts() and
# count_coordinated_rooms() (#633).
_CONFLICTS_QUERY = text(
    "SELECT room1_id, room1_name, room2_id, room2_name, map_x, map_y " + "FROM get_coordinate_conflicts(:pattern)"
)

_ROOM_COUNT_QUERY = text("SELECT count_coordinated_rooms(:pattern)")


def _zone_pattern(plane: str, zone: str, sub_zone: str | None) -> str:
    pattern = f"{plane}_{zone}"
    if sub_zone:
        return f"{pattern}_{sub_zone}"
    return pattern


def _conflict_from_row(row: Any) -> dict[str, Any]:
    return {
        "room1_id": row[0],
        "room1_name": row[1],
        "room2_id": row[2],
        "room2_name": row[3],
        "x": float(row[4]) if row[4] is not None else None,
        "y": float(row[5]) if row[5] is not None else None,
    }


class CoordinateValidator:  # pylint: disable=too-few-public-methods  # Reason: Validator class with focused responsibility, minimal public interface
    """
    Validates room coordinates and detects conflicts.

    A conflict occurs when multiple rooms have the same (x, y) coordinates
    within the same zone/subzone. Conflicts must be resolved manually by admins.
    """

    def __init__(self, session: AsyncSession) -> None:
        """
        Initialize coordinate validator.

        Args:
            session: Database session for coordinate queries
        """
        self._session = session

    async def _fetch_conflicts(self, pattern: str) -> list[dict[str, Any]]:
        result = await self._session.execute(_CONFLICTS_QUERY, {"pattern": pattern})
        return [_conflict_from_row(row) for row in result]

    async def _count_coordinated_rooms(self, pattern: str) -> int:
        count_result = await self._session.execute(_ROOM_COUNT_QUERY, {"pattern": pattern})
        return count_result.scalar_one() or 0

    async def validate_coordinates(self, plane: str, zone: str, sub_zone: str | None = None) -> dict[str, Any]:
        """
        Validate coordinates for rooms in a zone/subzone and detect conflicts.

        Args:
            plane: Plane name
            zone: Zone name
            sub_zone: Optional sub-zone name

        Returns:
            Dictionary with:
            - valid: bool indicating if coordinates are valid (no conflicts)
            - conflicts: list of conflict dictionaries with room details
            - total_rooms: total number of rooms checked
        """
        pattern = _zone_pattern(plane, zone, sub_zone)
        conflicts = await self._fetch_conflicts(pattern)
        total_rooms = await self._count_coordinated_rooms(pattern)

        if conflicts:
            logger.warning(
                "Coordinate conflicts detected",
                plane=plane,
                zone=zone,
                sub_zone=sub_zone,
                conflict_count=len(conflicts),
                total_rooms=total_rooms,
            )
        else:
            logger.debug(
                "No coordinate conflicts detected",
                plane=plane,
                zone=zone,
                sub_zone=sub_zone,
                total_rooms=total_rooms,
            )

        return {
            "valid": not conflicts,
            "conflicts": conflicts,
            "total_rooms": total_rooms,
            "conflict_count": len(conflicts),
        }
