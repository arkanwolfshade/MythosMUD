"""
Path validator for room connectivity analysis.

This module handles graph traversal algorithms to validate room connectivity,
find unreachable rooms, and detect dead ends in the dimensional architecture.
"""

from collections import defaultdict


class PathValidator:
    """
    Validates room connectivity using graph traversal algorithms.

    Implements the dimensional mapping techniques described in the
    Pnakotic Manuscripts for analyzing eldritch architecture.
    """

    def __init__(self, schema_validator=None):
        """
        Initialize the path validator.

        Args:
            schema_validator: Optional schema validator for exit analysis
        """
        self.schema_validator = schema_validator
        self.graph: dict[str, dict[str, str]] = defaultdict(dict)
        self.reverse_graph: dict[str, dict[str, str]] = defaultdict(dict)

    def build_graph(self, room_database: dict[str, dict]) -> dict[str, dict[str, str]]:
        """
        Build adjacency graph from room database.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            Adjacency graph mapping room IDs to exit directions and targets
        """
        self.graph.clear()
        self.reverse_graph.clear()

        for room_id, room_data in room_database.items():
            exits = room_data.get("exits", {})

            for direction, exit_data in exits.items():
                target = self._get_exit_target(exit_data)
                if target and target in room_database:
                    self.graph[room_id][direction] = target
                    self.reverse_graph[target][direction] = room_id

        return dict(self.graph)

    def _get_exit_target(self, exit_data) -> str | None:
        """Get target room ID from exit data."""
        if isinstance(exit_data, str):
            return exit_data
        elif isinstance(exit_data, dict):
            return exit_data.get("target")
        return None

    def _is_one_way_exit(self, exit_data) -> bool:
        """Check if exit is marked as one-way."""
        if isinstance(exit_data, dict):
            return "one_way" in exit_data.get("flags", [])
        return False

    def _get_room_zone(self, room_id: str, room_database: dict[str, dict]) -> tuple[str, str]:
        """
        Extract zone and sub_zone from room data.

        Args:
            room_id: Room identifier
            room_database: Complete room database

        Returns:
            Tuple of (zone, sub_zone)
        """
        room_data = room_database.get(room_id, {})
        return (room_data.get("zone", ""), room_data.get("sub_zone", ""))

    def check_bidirectional_connections(self, room_database: dict[str, dict]) -> list[tuple[str, str, str, str, bool]]:
        """
        Check for bidirectional connections between rooms, accounting for zone transitions.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of (room_a, direction_a, room_b, direction_b, is_zone_transition) tuples for missing return paths
        """
        self.build_graph(room_database)
        missing_returns = []

        for room_a, exits_a in self.graph.items():
            zone_a, subzone_a = self._get_room_zone(room_a, room_database)

            for direction_a, room_b in exits_a.items():
                # Skip if this is a one-way exit
                exit_data_a = room_database[room_a]["exits"].get(direction_a)
                if self._is_one_way_exit(exit_data_a):
                    continue

                zone_b, subzone_b = self._get_room_zone(room_b, room_database)
                is_zone_transition = (zone_a != zone_b) or (subzone_a != subzone_b)

                # Check if room_b has a return path to room_a
                opposite_direction = self._get_opposite_direction(direction_a)
                if opposite_direction not in self.graph.get(room_b, {}):
                    missing_returns.append((room_a, direction_a, room_b, opposite_direction, is_zone_transition))
                elif self.graph[room_b][opposite_direction] != room_a:
                    # Return path exists but points to wrong room
                    missing_returns.append((room_a, direction_a, room_b, opposite_direction, is_zone_transition))

        return missing_returns

    def _get_opposite_direction(self, direction: str) -> str:
        """Get the opposite direction for bidirectional checking."""
        opposites = {"north": "south", "south": "north", "east": "west", "west": "east", "up": "down", "down": "up"}
        return opposites.get(direction, direction)

    def find_dead_ends(self, room_database: dict[str, dict]) -> list[str]:
        """
        Find rooms with no exits (dead ends).

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of room IDs that are dead ends
        """
        dead_ends = []
        for room_id, room_data in room_database.items():
            exits = room_data.get("exits", {})
            if not any(self._get_exit_target(exit_data) for exit_data in exits.values()):
                dead_ends.append(room_id)
        return dead_ends

    def find_unreachable_rooms(
        self, start_room_id: str = "earth_arkham_city_intersection_derby_high", room_database: dict[str, dict] = None
    ) -> set[str]:
        """
        Find rooms that cannot be reached from the start room.

        Args:
            start_room_id: Starting room for reachability analysis
            room_database: Complete room database

        Returns:
            Set of unreachable room IDs
        """
        if not room_database:
            return set()

        visited = set()
        queue = [start_room_id]
        all_rooms = set(room_database.keys())

        while queue:
            current = queue.pop(0)
            if current in visited:
                continue

            visited.add(current)
            for target in self.graph.get(current, {}).values():
                if target not in visited:
                    queue.append(target)

        return all_rooms - visited

    def find_self_references(self, room_database: dict[str, dict]) -> list[tuple[str, str]]:
        """
        Find rooms that reference themselves in exits.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of (room_id, direction) tuples for self-referencing exits
        """
        self_refs = []
        for room_id, room_data in room_database.items():
            exits = room_data.get("exits", {})
            for direction, exit_data in exits.items():
                target = self._get_exit_target(exit_data)
                if target == room_id:
                    # Check if self-reference is allowed
                    if isinstance(exit_data, dict) and "self_reference" in exit_data.get("flags", []):
                        continue
                    self_refs.append((room_id, direction))
        return self_refs
