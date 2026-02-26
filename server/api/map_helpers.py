"""
Map API helpers: room loading and zone pattern utilities.

Extracted from maps.py to keep endpoint module under nloc limit.
"""

from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def build_zone_pattern(plane: str, zone: str, sub_zone: str | None) -> str:
    """
    Build zone pattern for room query.

    Args:
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name

    Returns:
        Zone pattern string for SQL LIKE query
    """
    zone_pattern = f"{plane}_{zone}"
    if sub_zone:
        zone_pattern = f"{zone_pattern}_{sub_zone}"
    return zone_pattern


def build_room_dict(row: Any) -> dict[str, Any]:
    """
    Build room dictionary from database row.

    Args:
        row: Database row result

    Returns:
        Room dictionary with all room properties
    """
    attrs = row[3] if row[3] else {}
    return {
        "id": row[1],  # Use stable_id as id
        "uuid": str(row[0]),
        "stable_id": row[1],
        "name": row[2],
        "attributes": attrs,
        "map_x": float(row[4]) if row[4] is not None else None,
        "map_y": float(row[5]) if row[5] is not None else None,
        "map_origin_zone": bool(row[6]) if row[6] is not None else False,
        "map_symbol": row[7],
        "map_style": row[8],
        "environment": attrs.get("environment", "outdoors"),
        "exits": {},
    }


async def load_room_exits(session: AsyncSession, rooms: list[dict[str, Any]]) -> None:
    """
    Load exits for rooms and attach them to room dictionaries.

    Args:
        session: Database session
        rooms: List of room dictionaries to populate with exits
    """
    if not rooms:
        return

    stable_ids = [r["stable_id"] for r in rooms]
    exits_query = text("""
        SELECT r1.stable_id as from_stable_id, r2.stable_id as to_stable_id, rl.direction
        FROM room_links rl
        JOIN rooms r1 ON rl.from_room_id = r1.id
        JOIN rooms r2 ON rl.to_room_id = r2.id
        WHERE r1.stable_id = ANY(:stable_ids)
    """)
    exits_result = await session.execute(exits_query, {"stable_ids": stable_ids})

    exits_by_room: dict[str, dict[str, str]] = {}
    for row in exits_result:
        from_stable = row[0]
        to_stable = row[1]
        direction = row[2]
        if from_stable not in exits_by_room:
            exits_by_room[from_stable] = {}
        exits_by_room[from_stable][direction] = to_stable

    for room in rooms:
        room["exits"] = exits_by_room.get(room["stable_id"], {})


async def load_rooms_with_coordinates(
    session: AsyncSession, plane: str, zone: str, sub_zone: str | None
) -> list[dict[str, Any]]:
    """
    Load rooms with their coordinates and exits.

    Args:
        session: Database session
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name

    Returns:
        List of room dictionaries with coordinates and exits
    """
    zone_pattern = build_zone_pattern(plane, zone, sub_zone)

    query = text("""
        SELECT
            r.id,
            r.stable_id,
            r.name,
            r.attributes,
            r.map_x,
            r.map_y,
            r.map_origin_zone,
            r.map_symbol,
            r.map_style
        FROM rooms r
        JOIN subzones sz ON r.subzone_id = sz.id
        JOIN zones z ON sz.zone_id = z.id
        WHERE r.stable_id LIKE :pattern || '%'
    """)

    result = await session.execute(query, {"pattern": zone_pattern})
    rooms = [build_room_dict(row) for row in result]

    await load_room_exits(session, rooms)

    return rooms


async def load_single_room_with_coordinates(session: AsyncSession, stable_id: str) -> dict[str, Any] | None:
    """
    Load one room by exact stable_id with coordinates and exits.

    Used to ensure the player's current room is always in the minimap list
    when exploration filter would otherwise omit it (e.g. just entered zone).
    """
    query = text("""
        SELECT
            r.id,
            r.stable_id,
            r.name,
            r.attributes,
            r.map_x,
            r.map_y,
            r.map_origin_zone,
            r.map_symbol,
            r.map_style
        FROM rooms r
        JOIN subzones sz ON r.subzone_id = sz.id
        JOIN zones z ON sz.zone_id = z.id
        WHERE r.stable_id = :stable_id
    """)
    result = await session.execute(query, {"stable_id": stable_id})
    row = result.fetchone()
    if not row:
        return None
    room = build_room_dict(row)
    await load_room_exits(session, [room])
    return room
