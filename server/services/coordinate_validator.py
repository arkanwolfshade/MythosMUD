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
        # Build query to find coordinate conflicts
        zone_pattern = f"{plane}_{zone}"
        if sub_zone:
            zone_pattern = f"{zone_pattern}_{sub_zone}"

        query = text("""
            SELECT
                r1.stable_id as room1_id,
                r1.name as room1_name,
                r2.stable_id as room2_id,
                r2.name as room2_name,
                r1.map_x,
                r1.map_y
            FROM rooms r1
            JOIN rooms r2 ON r1.map_x = r2.map_x AND r1.map_y = r2.map_y
            JOIN subzones sz1 ON r1.subzone_id = sz1.id
            JOIN zones z1 ON sz1.zone_id = z1.id
            JOIN subzones sz2 ON r2.subzone_id = sz2.id
            JOIN zones z2 ON sz2.zone_id = z2.id
            WHERE r1.stable_id LIKE :pattern || '%'
            AND r2.stable_id LIKE :pattern || '%'
            AND r1.id < r2.id
            AND r1.map_x IS NOT NULL
            AND r1.map_y IS NOT NULL
            AND r2.map_x IS NOT NULL
            AND r2.map_y IS NOT NULL
        """)

        result = await self._session.execute(query, {"pattern": zone_pattern})
        conflicts = []
        for row in result:
            conflicts.append(
                {
                    "room1_id": row[0],
                    "room1_name": row[1],
                    "room2_id": row[2],
                    "room2_name": row[3],
                    "x": float(row[4]) if row[4] is not None else None,
                    "y": float(row[5]) if row[5] is not None else None,
                }
            )

        # Count total rooms with coordinates
        count_query = text("""
            SELECT COUNT(*)
            FROM rooms r
            JOIN subzones sz ON r.subzone_id = sz.id
            JOIN zones z ON sz.zone_id = z.id
            WHERE r.stable_id LIKE :pattern || '%'
            AND r.map_x IS NOT NULL
            AND r.map_y IS NOT NULL
        """)
        count_result = await self._session.execute(count_query, {"pattern": zone_pattern})
        total_rooms = count_result.scalar_one() or 0

        is_valid = not conflicts

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
            "valid": is_valid,
            "conflicts": conflicts,
            "total_rooms": total_rooms,
            "conflict_count": len(conflicts),
        }
