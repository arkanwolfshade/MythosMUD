"""
Coordinate generation service for ASCII maps.

This module provides hierarchical coordinate generation for rooms based on
exit relationships. Coordinates are generated using a zone/subzone grouping
approach combined with a simple directional grid system.

As documented in the Pnakotic Manuscripts, proper spatial mapping is essential
for understanding the eldritch architecture of our dimensional spaces.
"""

from collections import deque
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CoordinateGenerator:
    """
    Generates map coordinates for rooms using hierarchical grouping and directional grid.

    Algorithm:
    1. Group rooms by zone and sub_zone
    2. For each zone/subzone group:
       - Find origin room (map_origin_zone=true or first room)
       - Use BFS from origin
       - Apply directional grid: north=-y, south=+y, east=+x, west=-x
    3. Store coordinates in map_x/map_y
    4. Detect conflicts and warn (don't auto-resolve)
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize coordinate generator.

        Args:
            session: Database session for coordinate updates
        """
        self._session = session

    async def generate_coordinates_for_zone(self, plane: str, zone: str, sub_zone: str | None = None) -> dict[str, Any]:
        """
        Generate coordinates for all rooms in a zone/subzone.

        Args:
            plane: Plane name
            zone: Zone name
            sub_zone: Optional sub-zone name

        Returns:
            Dictionary with:
            - coordinates: dict mapping room_id to (x, y)
            - conflicts: list of conflict tuples (room_id1, room_id2, x, y)
            - origin_room: room_id of origin room used
        """
        # Load rooms and exits for this zone/subzone
        rooms_data = await self._load_rooms_data(plane, zone, sub_zone)
        if not rooms_data:
            logger.warning("No rooms found for coordinate generation", plane=plane, zone=zone, sub_zone=sub_zone)
            return {"coordinates": {}, "conflicts": [], "origin_room": None}

        # Group by sub_zone (each sub_zone gets its own coordinate space)
        grouped_rooms: dict[str, list[dict[str, Any]]] = {}
        for room in rooms_data:
            room_subzone = room.get("sub_zone") or "default"
            if room_subzone not in grouped_rooms:
                grouped_rooms[room_subzone] = []
            grouped_rooms[room_subzone].append(room)

        all_coordinates: dict[str, tuple[int, int]] = {}
        all_conflicts: list[tuple[str, str, int, int]] = []

        # Generate coordinates for each subzone group
        for subzone_key, rooms in grouped_rooms.items():
            logger.debug("Generating coordinates for subzone", subzone=subzone_key, room_count=len(rooms))
            coords, conflicts, origin = await self._generate_for_subzone(rooms)
            all_coordinates.update(coords)
            all_conflicts.extend(conflicts)
            logger.info(
                "Generated coordinates for subzone",
                subzone=subzone_key,
                rooms_positioned=len(coords),
                conflicts=len(conflicts),
                origin_room=origin,
            )

        # Store coordinates in database
        if all_coordinates:
            await self._store_coordinates(all_coordinates)

        return {
            "coordinates": all_coordinates,
            "conflicts": all_conflicts,
            "origin_room": None,  # Could return per-subzone origins if needed
        }

    async def _load_rooms_data(self, plane: str, zone: str, sub_zone: str | None) -> list[dict[str, Any]]:
        """
        Load rooms and their exits from database.

        Args:
            plane: Plane name
            zone: Zone name
            sub_zone: Optional sub-zone name

        Returns:
            List of room dictionaries with exits
        """
        # Build query to get rooms with their exits
        # Use stable_id matching pattern: rooms have stable_id like "plane_zone_subzone_roomname"
        zone_pattern = f"{plane}_{zone}"
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
                r.map_style,
                z.stable_id as zone_stable_id,
                sz.stable_id as subzone_stable_id
            FROM rooms r
            JOIN subzones sz ON r.subzone_id = sz.id
            JOIN zones z ON sz.zone_id = z.id
            WHERE r.stable_id LIKE :pattern || '%'
        """)

        params = {"pattern": zone_pattern}
        if sub_zone:
            subzone_pattern = f"{zone_pattern}_{sub_zone}"
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
                    r.map_style,
                    z.stable_id as zone_stable_id,
                    sz.stable_id as subzone_stable_id
                FROM rooms r
                JOIN subzones sz ON r.subzone_id = sz.id
                JOIN zones z ON sz.zone_id = z.id
                WHERE r.stable_id LIKE :pattern || '%'
            """)
            params["pattern"] = subzone_pattern

        result = await self._session.execute(query, params)
        rooms = []
        for row in result:
            # Use stable_id as the room identifier (not UUID)
            stable_id = row[1]
            room_dict = {
                "id": stable_id,  # Use stable_id as id for coordinate generation
                "uuid": str(row[0]),  # Keep UUID for database operations
                "stable_id": stable_id,
                "name": row[2],
                "attributes": row[3] if row[3] else {},
                "map_x": float(row[4]) if row[4] is not None else None,
                "map_y": float(row[5]) if row[5] is not None else None,
                "map_origin_zone": bool(row[6]) if row[6] is not None else False,
                "map_symbol": row[7],
                "map_style": row[8],
                "zone": row[9].split("_", 1)[1] if "_" in str(row[9]) else str(row[9]),
                "sub_zone": row[10] if row[10] else None,
            }
            # Extract environment from attributes
            attrs = room_dict.get("attributes", {})
            room_dict["environment"] = attrs.get("environment") or "outdoors"
            rooms.append(room_dict)

        # Load exits for these rooms
        if rooms:
            # Map stable_ids to UUIDs for query
            stable_to_uuid: dict[str, str] = {r["stable_id"]: r["uuid"] for r in rooms}
            room_uuids = list(stable_to_uuid.values())

            exits_query = text("""
                SELECT r1.stable_id as from_stable_id, r2.stable_id as to_stable_id, rl.direction
                FROM room_links rl
                JOIN rooms r1 ON rl.from_room_id = r1.id
                JOIN rooms r2 ON rl.to_room_id = r2.id
                WHERE rl.from_room_id = ANY(:room_uuids)
            """)
            exits_result = await self._session.execute(exits_query, {"room_uuids": room_uuids})

            # Build exits dict using stable_ids
            exits_by_room: dict[str, dict[str, str]] = {}
            for row in exits_result:
                from_stable = row[0]
                to_stable = row[1]
                direction = row[2]
                if from_stable not in exits_by_room:
                    exits_by_room[from_stable] = {}
                exits_by_room[from_stable][direction] = to_stable

            # Add exits to rooms
            for room in rooms:
                room["exits"] = exits_by_room.get(room["stable_id"], {})

        return rooms

    async def _generate_for_subzone(
        self, rooms: list[dict[str, Any]]
    ) -> tuple[dict[str, tuple[int, int]], list[tuple[str, str, int, int]], str | None]:
        """
        Generate coordinates for rooms in a single subzone.

        Args:
            rooms: List of room dictionaries with exits

        Returns:
            Tuple of (coordinates dict, conflicts list, origin_room_id)
        """
        if not rooms:
            return {}, [], None

        # Find origin room (map_origin_zone=true, or first room)
        origin_room = None
        for room in rooms:
            if room.get("map_origin_zone"):
                origin_room = room
                break

        if not origin_room:
            origin_room = rooms[0]

        origin_id = origin_room["id"]
        logger.debug("Using origin room", origin_id=origin_id, origin_name=origin_room.get("name"))

        # Build adjacency list from exits
        adjacency: dict[str, list[tuple[str, str]]] = {}
        for room in rooms:
            room_id = room["id"]
            if room_id not in adjacency:
                adjacency[room_id] = []

            for direction, target_id in room.get("exits", {}).items():
                # Only include exits to rooms in this subzone
                target_room = next((r for r in rooms if r["id"] == target_id), None)
                if target_room:
                    adjacency[room_id].append((target_id, direction.lower()))

                    # Add reverse direction
                    if target_id not in adjacency:
                        adjacency[target_id] = []
                    reverse_dir = self._reverse_direction(direction.lower())
                    adjacency[target_id].append((room_id, reverse_dir))

        # BFS to assign coordinates
        coords: dict[str, tuple[int, int]] = {}
        visited: set[str] = set()
        queue: deque[tuple[str, int, int]] = deque([(origin_id, 0, 0)])

        coords[origin_id] = (0, 0)
        visited.add(origin_id)

        while queue:
            room_id, x, y = queue.popleft()

            if room_id in adjacency:
                for next_room_id, direction in adjacency[room_id]:
                    if next_room_id not in visited:
                        new_x, new_y = self._get_next_coordinates(x, y, direction)
                        coords[next_room_id] = (new_x, new_y)
                        visited.add(next_room_id)
                        queue.append((next_room_id, new_x, new_y))

        # Detect conflicts (multiple rooms at same x,y)
        conflicts: list[tuple[str, str, int, int]] = []
        coord_to_rooms: dict[tuple[int, int], list[str]] = {}
        for room_id, (cx, cy) in coords.items():
            if (cx, cy) not in coord_to_rooms:
                coord_to_rooms[(cx, cy)] = []
            coord_to_rooms[(cx, cy)].append(room_id)

        for (cx, cy), room_ids in coord_to_rooms.items():
            if len(room_ids) > 1:
                # Multiple rooms at same position - conflict
                for i in range(len(room_ids)):
                    for j in range(i + 1, len(room_ids)):
                        conflicts.append((room_ids[i], room_ids[j], cx, cy))
                        logger.warning(
                            "Coordinate conflict detected",
                            room1=room_ids[i],
                            room2=room_ids[j],
                            x=cx,
                            y=cy,
                        )

        return coords, conflicts, origin_id

    def _get_next_coordinates(self, x: int, y: int, direction: str) -> tuple[int, int]:
        """
        Calculate next coordinates based on direction.

        Args:
            x: Current x coordinate
            y: Current y coordinate
            direction: Direction (north, south, east, west)

        Returns:
            New (x, y) coordinates
        """
        direction = direction.lower()
        if direction == "north":
            return (x, y - 1)
        elif direction == "south":
            return (x, y + 1)
        elif direction == "east":
            return (x + 1, y)
        elif direction == "west":
            return (x - 1, y)
        else:
            # up/down don't change 2D coordinates
            return (x, y)

    def _reverse_direction(self, direction: str) -> str:
        """
        Reverse a direction.

        Args:
            direction: Original direction

        Returns:
            Reversed direction
        """
        direction_map = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
            "up": "down",
            "down": "up",
        }
        return direction_map.get(direction.lower(), direction)

    async def _store_coordinates(self, coordinates: dict[str, tuple[int, int]]) -> None:
        """
        Store coordinates in database.

        Args:
            coordinates: Dictionary mapping room stable_id to (x, y) tuple
        """
        if not coordinates:
            return

        # Batch update coordinates using stable_id
        update_query = text("""
            UPDATE rooms
            SET map_x = :map_x, map_y = :map_y
            WHERE stable_id = :stable_id
        """)

        for stable_id, (x, y) in coordinates.items():
            await self._session.execute(
                update_query,
                {"stable_id": stable_id, "map_x": float(x), "map_y": float(y)},
            )

        await self._session.commit()
        logger.info("Stored coordinates", room_count=len(coordinates))
