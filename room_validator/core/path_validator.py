"""
Path validator for room connectivity analysis.

This module handles graph traversal algorithms to validate room connectivity,
find unreachable rooms, and detect dead ends in the dimensional architecture.
"""

from collections import defaultdict, deque


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
        """Extract target room ID from exit data."""
        if self.schema_validator:
            return self.schema_validator.get_exit_target(exit_data)

        # Fallback implementation
        if exit_data is None:
            return None
        elif isinstance(exit_data, str):
            return exit_data
        elif isinstance(exit_data, dict):
            return exit_data.get("target")
        else:
            return None

    def _is_one_way_exit(self, exit_data) -> bool:
        """Check if exit is marked as one-way."""
        if self.schema_validator:
            return self.schema_validator.is_one_way_exit(exit_data)

        # Fallback implementation
        if isinstance(exit_data, dict):
            return "one_way" in exit_data.get("flags", [])
        return False

    def find_unreachable_rooms(
        self, start_room_id: str = "earth_arkham_city_campus_E_College_St_003", room_database: dict[str, dict] = None
    ) -> set[str]:
        """
        Find rooms that cannot be reached from the starting room.

        Args:
            start_room_id: ID of the starting room for traversal
            room_database: Optional room database (uses self.graph if not provided)

        Returns:
            Set of unreachable room IDs
        """
        if room_database:
            self.build_graph(room_database)

        if start_room_id not in self.graph:
            # Starting room doesn't exist
            return set(self.graph.keys())

        # BFS to find all reachable rooms
        visited = set()
        queue = deque([start_room_id])
        visited.add(start_room_id)

        while queue:
            current_room = queue.popleft()

            for target in self.graph[current_room].values():
                if target not in visited:
                    visited.add(target)
                    queue.append(target)

        # Return rooms that weren't visited
        all_rooms = set(self.graph.keys())
        return all_rooms - visited

    def check_bidirectional_connections(self, room_database: dict[str, dict]) -> list[tuple[str, str, str, str]]:
        """
        Check for bidirectional connections between rooms.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of (room_a, direction_a, room_b, direction_b) tuples for missing return paths
        """
        self.build_graph(room_database)
        missing_returns = []

        for room_a, exits_a in self.graph.items():
            for direction_a, room_b in exits_a.items():
                # Skip if this is a one-way exit
                exit_data_a = room_database[room_a]["exits"].get(direction_a)
                if self._is_one_way_exit(exit_data_a):
                    continue

                # Check if room_b has a return path to room_a
                opposite_direction = self._get_opposite_direction(direction_a)
                if opposite_direction not in self.graph.get(room_b, {}):
                    missing_returns.append((room_a, direction_a, room_b, opposite_direction))
                elif self.graph[room_b][opposite_direction] != room_a:
                    # Return path exists but points to wrong room
                    missing_returns.append((room_a, direction_a, room_b, opposite_direction))

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
        self.build_graph(room_database)
        dead_ends = []

        for room_id, exits in self.graph.items():
            if not exits:
                dead_ends.append(room_id)

        return dead_ends

    def find_potential_dead_ends(self, room_database: dict[str, dict]) -> list[str]:
        """
        Find rooms with only one exit (potential dead ends).

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of room IDs with only one exit
        """
        self.build_graph(room_database)
        potential_dead_ends = []

        for room_id, exits in self.graph.items():
            if len(exits) == 1:
                potential_dead_ends.append(room_id)

        return potential_dead_ends

    def find_self_references(self, room_database: dict[str, dict]) -> list[tuple[str, str]]:
        """
        Find rooms that reference themselves.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of (room_id, direction) tuples for self-references
        """
        self_references = []

        for room_id, room_data in room_database.items():
            exits = room_data.get("exits", {})

            for direction, exit_data in exits.items():
                target = self._get_exit_target(exit_data)
                if target == room_id:
                    # Check if this is allowed
                    if not self._is_self_reference_allowed(exit_data):
                        self_references.append((room_id, direction))

        return self_references

    def _is_self_reference_allowed(self, exit_data) -> bool:
        """Check if self-reference is allowed for this exit."""
        if self.schema_validator:
            return self.schema_validator.is_self_reference_exit(exit_data)

        # Fallback implementation
        if isinstance(exit_data, dict):
            return "self_reference" in exit_data.get("flags", [])
        return False

    def find_cycles(self, room_database: dict[str, dict]) -> list[list[str]]:
        """
        Find cycles in the room graph.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            List of cycles (lists of room IDs)
        """
        self.build_graph(room_database)
        cycles = []
        visited = set()
        rec_stack = set()

        def dfs(room_id: str, path: list[str]):
            visited.add(room_id)
            rec_stack.add(room_id)
            path.append(room_id)

            for target in self.graph.get(room_id, {}).values():
                if target not in visited:
                    dfs(target, path.copy())
                elif target in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(target)
                    cycle = path[cycle_start:] + [target]
                    if cycle not in cycles:
                        cycles.append(cycle)

            rec_stack.remove(room_id)

        for room_id in self.graph:
            if room_id not in visited:
                dfs(room_id, [])

        return cycles

    def get_room_connectivity_stats(self, room_database: dict[str, dict]) -> dict:
        """
        Get comprehensive connectivity statistics.

        Args:
            room_database: Dictionary mapping room IDs to room data

        Returns:
            Dictionary with connectivity statistics
        """
        self.build_graph(room_database)

        total_rooms = len(self.graph)
        total_exits = sum(len(exits) for exits in self.graph.values())

        unreachable = self.find_unreachable_rooms(room_database=room_database)
        dead_ends = self.find_dead_ends(room_database)
        potential_dead_ends = self.find_potential_dead_ends(room_database)
        missing_returns = self.check_bidirectional_connections(room_database)
        self_references = self.find_self_references(room_database)
        cycles = self.find_cycles(room_database)

        return {
            "total_rooms": total_rooms,
            "total_exits": total_exits,
            "average_exits_per_room": total_exits / total_rooms if total_rooms > 0 else 0,
            "unreachable_rooms": len(unreachable),
            "dead_ends": len(dead_ends),
            "potential_dead_ends": len(potential_dead_ends),
            "missing_return_paths": len(missing_returns),
            "self_references": len(self_references),
            "cycles": len(cycles),
            "connectivity_score": self._calculate_connectivity_score(
                total_rooms, len(unreachable), len(dead_ends), len(missing_returns)
            ),
        }

    def _calculate_connectivity_score(
        self, total_rooms: int, unreachable: int, dead_ends: int, missing_returns: int
    ) -> float:
        """Calculate a connectivity score (0-100, higher is better)."""
        if total_rooms == 0:
            return 0.0

        # Penalize unreachable rooms heavily
        unreachable_penalty = (unreachable / total_rooms) * 50

        # Penalize dead ends moderately
        dead_end_penalty = (dead_ends / total_rooms) * 20

        # Penalize missing return paths slightly
        return_penalty = (missing_returns / total_rooms) * 10

        score = 100 - unreachable_penalty - dead_end_penalty - return_penalty
        return max(0.0, min(100.0, score))

    def generate_minimap_graph(self, room_database: dict[str, dict], max_depth: int = 3) -> dict:
        """
        Generate a simplified graph for mini-map display.

        Args:
            room_database: Dictionary mapping room IDs to room data
            max_depth: Maximum depth to traverse from starting room

        Returns:
            Dictionary with mini-map data including nodes, edges, and metadata
        """
        self.build_graph(room_database)

        start_room = "earth_arkham_city_campus_E_College_St_003"
        if start_room not in self.graph:
            return {"error": "Starting room not found", "nodes": [], "edges": []}

        # BFS to find reachable rooms within max_depth
        visited = set()
        queue = [(start_room, 0)]  # (room_id, depth)
        nodes = []
        edges = []

        while queue:
            current_room, depth = queue.pop(0)

            if current_room in visited or depth > max_depth:
                continue

            visited.add(current_room)

            # Get room data for display
            room_data = room_database.get(current_room, {})
            room_name = room_data.get("name", current_room)
            sub_zone = room_data.get("sub_zone", "unknown")

            # Add node
            nodes.append({
                "id": current_room,
                "name": room_name,
                "sub_zone": sub_zone,
                "depth": depth,
                "is_start": current_room == start_room
            })

            # Add edges to neighbors
            for direction, target in self.graph.get(current_room, {}).items():
                if target in room_database:
                    edges.append({
                        "from": current_room,
                        "to": target,
                        "direction": direction
                    })

                    # Add target to queue if not visited and within depth limit
                    if target not in visited and depth < max_depth:
                        queue.append((target, depth + 1))

        return {
            "nodes": nodes,
            "edges": edges,
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "max_depth": max_depth,
            "starting_room": start_room
        }
