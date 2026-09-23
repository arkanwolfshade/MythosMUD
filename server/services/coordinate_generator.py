"""
Coordinate generation service for ASCII maps.

This module provides hierarchical coordinate generation for rooms based on
exit relationships. Coordinates are generated using a zone/subzone grouping
approach combined with a simple directional grid system.

As documented in the Pnakotic Manuscripts, proper spatial mapping is essential
for understanding the eldritch architecture of our dimensional spaces.
"""

# pylint: disable=too-few-public-methods,too-many-locals  # Reason: Coordinate generator class with focused responsibility, minimal public interface, and complex coordinate generation logic

import json
from collections import deque
from typing import Any

from sqlalchemy import bindparam, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CoordinateGenerator:
    """
    Generates map coordinates for rooms using hierarchical grouping and directional grid.

    Algorithm:
    1. Group rooms by zone and sub_zone
    2. For each zone/subzone group:
       - Find origin room (map_origin_zone=true or first room)
       - Use BFS from origin; any room left unreached (a separate connected component)
         seeds a fresh BFS at a new origin, offset clear of rooms already placed
       - Apply directional grid: north=-y, south=+y, east=+x, west=-x
       - Resolve collisions by displacing a room to the nearest free cell
    3. Store coordinates in map_x/map_y
    4. Verify no conflicts remain (should always be empty; kept as a safety net)
    """

    def __init__(self, session: AsyncSession) -> None:
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

    def _rooms_query_and_pattern(
        self, plane: str, zone: str, sub_zone: str | None
    ) -> tuple[Select[Any], dict[str, str]]:
        zone_pattern = f"{plane}_{zone}"
        pattern = f"{zone_pattern}_{sub_zone}" if sub_zone else zone_pattern
        rooms = func.get_rooms_for_coordinate_generation(bindparam("pattern")).table_valued(
            "id",
            "stable_id",
            "name",
            "attributes",
            "map_x",
            "map_y",
            "map_origin_zone",
            "map_symbol",
            "map_style",
            "zone_stable_id",
            "subzone_stable_id",
        )
        return select(rooms), {"pattern": pattern}

    def _room_dict_from_row(self, row: Any) -> dict[str, Any]:
        stable_id = row[1]
        raw_attrs = row[3]
        attrs = raw_attrs if isinstance(raw_attrs, dict) else {}
        room_dict = {
            "id": stable_id,
            "uuid": str(row[0]),
            "stable_id": stable_id,
            "name": row[2],
            "attributes": attrs,
            "map_x": float(row[4]) if row[4] is not None else None,
            "map_y": float(row[5]) if row[5] is not None else None,
            "map_origin_zone": bool(row[6]) if row[6] is not None else False,
            "map_symbol": row[7],
            "map_style": row[8],
            "zone": row[9].split("_", 1)[1] if "_" in str(row[9]) else str(row[9]),
            "sub_zone": row[10] if row[10] else None,
        }
        room_dict["environment"] = attrs.get("environment") or "outdoors"
        return room_dict

    async def _attach_room_exits(self, rooms: list[dict[str, Any]]) -> None:
        if not rooms:
            return
        room_uuids = [room["uuid"] for room in rooms]
        exits = func.get_room_exits_for_coordinate_generation(bindparam("room_uuids")).table_valued(
            "from_stable_id",
            "to_stable_id",
            "direction",
        )
        exits_result = await self._session.execute(select(exits), {"room_uuids": room_uuids})
        exits_by_room: dict[str, dict[str, str]] = {}
        for row in exits_result:
            from_stable = row[0]
            if from_stable not in exits_by_room:
                exits_by_room[from_stable] = {}
            exits_by_room[from_stable][row[2]] = row[1]
        for room in rooms:
            room["exits"] = exits_by_room.get(room["stable_id"], {})

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
        query, params = self._rooms_query_and_pattern(plane, zone, sub_zone)
        result = await self._session.execute(query, params)
        rooms = [self._room_dict_from_row(row) for row in result]
        await self._attach_room_exits(rooms)
        return rooms

    def _find_origin_room(self, rooms: list[dict[str, Any]]) -> dict[str, Any] | None:
        """Find the origin room (map_origin_zone=true, or first room)."""
        for room in rooms:
            if room.get("map_origin_zone"):
                return room
        return rooms[0] if rooms else None

    def _build_adjacency_list(self, rooms: list[dict[str, Any]]) -> dict[str, list[tuple[str, str]]]:
        """Build adjacency list from room exits."""
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
        return adjacency

    def _nearest_free_cell(self, x: int, y: int, occupied: dict[tuple[int, int], str]) -> tuple[int, int]:
        """Find the nearest unoccupied cell to (x, y), preferring (x, y) itself.

        # ponytail: greedy nearest-free-cell search, not a real layout algorithm -- fine
        # for the occasional collision a cycle produces; swap for a force-directed/
        # constraint layout if large exits-authored zones end up looking scrambled.
        """
        if (x, y) not in occupied:
            return (x, y)
        visited: set[tuple[int, int]] = {(x, y)}
        queue: deque[tuple[int, int]] = deque([(x, y)])
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):  # north, south, east, west
                candidate = (cx + dx, cy + dy)
                if candidate in visited:
                    continue
                visited.add(candidate)
                if candidate not in occupied:
                    return candidate
                queue.append(candidate)
        raise AssertionError("Unreachable: an infinite grid always has a free cell")

    def _assign_coordinates_bfs(
        self, origin_id: str, adjacency: dict[str, list[tuple[str, str]]]
    ) -> dict[str, tuple[int, int]]:
        """Assign coordinates using BFS starting from origin.

        Every room in `adjacency` gets a cell, not just the origin's connected component:
        once a BFS from a seed is exhausted, the next unplaced room seeds a fresh BFS at a
        new origin offset clear of everything already placed. Collisions (a cycle whose
        direction vectors don't sum to zero, or an up/down exit that doesn't move x/y) are
        resolved on the spot by displacing to the nearest free cell, so every returned
        coordinate is unique.
        """
        coords: dict[str, tuple[int, int]] = {}
        occupied: dict[tuple[int, int], str] = {}
        visited: set[str] = set()

        def place(room_id: str, x: int, y: int) -> tuple[int, int]:
            cell = self._nearest_free_cell(x, y, occupied)
            coords[room_id] = cell
            occupied[cell] = room_id
            visited.add(room_id)
            return cell

        seeds = [origin_id, *(room_id for room_id in adjacency if room_id != origin_id)]
        for seed_id in seeds:
            if seed_id in visited:
                continue
            if coords:
                seed_x = max(cx for cx, _cy in coords.values()) + 2
                seed_y = 0
            else:
                seed_x, seed_y = 0, 0
            sx, sy = place(seed_id, seed_x, seed_y)
            queue: deque[tuple[str, int, int]] = deque([(seed_id, sx, sy)])

            while queue:
                room_id, x, y = queue.popleft()
                for next_room_id, direction in adjacency.get(room_id, []):
                    if next_room_id not in visited:
                        new_x, new_y = self._get_next_coordinates(x, y, direction)
                        nx, ny = place(next_room_id, new_x, new_y)
                        queue.append((next_room_id, nx, ny))

        return coords

    def _detect_coordinate_conflicts(self, coords: dict[str, tuple[int, int]]) -> list[tuple[str, str, int, int]]:
        """Detect conflicts (multiple rooms at same x,y coordinates).

        `_assign_coordinates_bfs` resolves collisions as it places rooms, so this should
        always return an empty list; kept as a safety net and to power the admin-facing
        conflict report (`CoordinateValidator`, backed by `get_coordinate_conflicts`).
        """
        conflicts: list[tuple[str, str, int, int]] = []
        coord_to_rooms: dict[tuple[int, int], list[str]] = {}
        for room_id, (cx, cy) in coords.items():
            if (cx, cy) not in coord_to_rooms:
                coord_to_rooms[(cx, cy)] = []
            coord_to_rooms[(cx, cy)].append(room_id)

        for (cx, cy), room_ids in coord_to_rooms.items():
            if len(room_ids) > 1:
                # Multiple rooms at same position - conflict
                for i, room_id1 in enumerate(room_ids):
                    for room_id2 in room_ids[i + 1 :]:
                        conflicts.append((room_id1, room_id2, cx, cy))
                        logger.warning(
                            "Coordinate conflict detected",
                            room1=room_id1,
                            room2=room_id2,
                            x=cx,
                            y=cy,
                        )

        return conflicts

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

        # Find origin room
        origin_room = self._find_origin_room(rooms)
        if not origin_room:
            return {}, [], None

        origin_id = origin_room["id"]
        logger.debug("Using origin room", origin_id=origin_id, origin_name=origin_room.get("name"))

        # Build adjacency list from exits
        adjacency = self._build_adjacency_list(rooms)

        # BFS to assign coordinates
        coords = self._assign_coordinates_bfs(origin_id, adjacency)

        # Detect conflicts (multiple rooms at same x,y)
        conflicts = self._detect_coordinate_conflicts(coords)

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
        if direction == "south":
            return (x, y + 1)
        if direction == "east":
            return (x + 1, y)
        if direction == "west":
            return (x - 1, y)
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

        # Bulk update via a single procedure call (one round-trip for the whole zone)
        positions = json.dumps(
            [
                {"stable_id": stable_id, "map_x": float(x), "map_y": float(y)}
                for stable_id, (x, y) in coordinates.items()
            ]
        )
        update_query = select(func.update_room_map_positions(bindparam("positions")))
        await self._session.execute(update_query, {"positions": positions})

        await self._session.commit()
        logger.info("Stored coordinates", room_count=len(coordinates))
