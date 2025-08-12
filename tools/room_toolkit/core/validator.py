"""
Enhanced Room Validator

Unified validation engine with schema and connectivity validation.
Consolidates functionality from the original validator.
"""

from collections import deque
from typing import Any

from .schema_validator import SchemaValidator


class RoomValidator:
    """Enhanced validation engine with comprehensive checks"""

    def __init__(self):
        self.schema_validator = SchemaValidator("schemas/unified_room_schema.json")

    def validate_schema(self, room_database: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
        """Validate JSON schema for all rooms"""
        return self.schema_validator.validate_room_database(room_database)

    def validate_connectivity(
        self, room_database: dict[str, dict[str, Any]], start_room: str = None
    ) -> list[dict[str, Any]]:
        """Validate room connectivity and return comprehensive error list"""
        errors = []

        if not room_database:
            return errors

        # Use default start room if not specified
        if start_room is None:
            start_room = "earth_arkham_city_northside_intersection_derby_high"

        # Check for unreachable rooms
        unreachable = self._find_unreachable_rooms(start_room, room_database)
        for room_id in unreachable:
            errors.append(
                {
                    "type": "unreachable",
                    "room_id": room_id,
                    "message": f"No path from starting room {start_room}",
                    "suggestion": f"Add connection from {start_room} or another reachable room",
                }
            )

        # Check bidirectional connections
        missing_returns = self._check_bidirectional_connections(room_database)
        for room_a, direction_a, room_b, direction_b, is_zone_transition in missing_returns:
            error_type = "zone_transition" if is_zone_transition else "bidirectional"
            zone_a = room_database[room_a].get("_subzone", "unknown")
            zone_b = room_database[room_b].get("_subzone", "unknown")

            if is_zone_transition:
                message = f"Zone Transition: Exit '{direction_a}' → {room_b} ({zone_a} → {zone_b}), but {room_b} has no '{direction_b}' return"
            else:
                message = f"Exit '{direction_a}' → {room_b}, but {room_b} has no '{direction_b}' return"

            errors.append(
                {
                    "type": error_type,
                    "room_id": room_a,
                    "message": message,
                    "suggestion": f'Add "{direction_b}": "{room_a}" to {room_b} or flag as one_way',
                }
            )

        # Check for dead ends
        dead_ends = self._find_dead_ends(room_database)
        for room_id in dead_ends:
            errors.append(
                {
                    "type": "dead_end",
                    "room_id": room_id,
                    "message": "No exits (dead end)",
                    "suggestion": "Add at least one exit to this room",
                }
            )

        # Check for self-references
        self_references = self._find_self_references(room_database)
        for room_id, direction in self_references:
            errors.append(
                {
                    "type": "self_reference",
                    "room_id": room_id,
                    "message": f'Room references itself in direction "{direction}"',
                    "suggestion": 'Add "self_reference" flag or fix exit target',
                }
            )

        return errors

    def _find_unreachable_rooms(self, start_room: str, room_database: dict[str, dict[str, Any]]) -> set[str]:
        """Find rooms that cannot be reached from the start room"""
        if start_room not in room_database:
            return set(room_database.keys())

        visited = set()
        queue = deque([start_room])
        visited.add(start_room)

        while queue:
            current = queue.popleft()
            room = room_database[current]

            for _direction, target in room.get("exits", {}).items():
                if target and target in room_database and target not in visited:
                    visited.add(target)
                    queue.append(target)

        return set(room_database.keys()) - visited

    def _check_bidirectional_connections(
        self, room_database: dict[str, dict[str, Any]]
    ) -> list[tuple[str, str, str, str, bool]]:
        """Check for missing bidirectional connections"""
        missing_returns = []

        # Direction mapping for return directions
        return_directions = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
            "up": "down",
            "down": "up",
            "n": "s",
            "s": "n",
            "e": "w",
            "w": "e",
        }

        for room_id, room in room_database.items():
            exits = room.get("exits", {})

            for direction, target in exits.items():
                if not target or target not in room_database:
                    continue

                # Check if this is a zone transition
                room_subzone = room.get("_subzone", "unknown")
                target_subzone = room_database[target].get("_subzone", "unknown")
                is_zone_transition = room_subzone != target_subzone

                # Check for return direction
                return_direction = return_directions.get(direction)
                if return_direction:
                    target_exits = room_database[target].get("exits", {})
                    if return_direction not in target_exits or target_exits[return_direction] != room_id:
                        missing_returns.append((room_id, direction, target, return_direction, is_zone_transition))

        return missing_returns

    def _find_dead_ends(self, room_database: dict[str, dict[str, Any]]) -> set[str]:
        """Find rooms with no exits"""
        dead_ends = set()

        for room_id, room in room_database.items():
            exits = room.get("exits", {})
            if not exits or all(not target for target in exits.values()):
                dead_ends.add(room_id)

        return dead_ends

    def _find_self_references(self, room_database: dict[str, dict[str, Any]]) -> list[tuple[str, str]]:
        """Find rooms that reference themselves"""
        self_references = []

        for room_id, room in room_database.items():
            exits = room.get("exits", {})
            for direction, target in exits.items():
                if target == room_id:
                    self_references.append((room_id, direction))

        return self_references

    def validate_environment_types(self, room_database: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        """Validate environment type consistency"""
        errors = []
        valid_environments = {
            "indoors",
            "outdoors",
            "underwater",
            "street_paved",
            "street_cobblestone",
            "alley",
            "intersection",
            "plaza",
            "building_exterior",
            "building_interior",
            "institution",
            "residential",
            "commercial",
            "park",
            "cemetery",
            "waterfront",
            "hillside",
            "campus",
            "docks",
            "industrial",
            "abandoned",
        }

        for room_id, room in room_database.items():
            env = room.get("environment")
            if env and env not in valid_environments:
                errors.append(
                    {
                        "type": "invalid_environment",
                        "room_id": room_id,
                        "message": f"Invalid environment type: {env}",
                        "suggestion": f"Use one of: {', '.join(sorted(valid_environments))}",
                    }
                )

        return errors

    def validate_room_ids(self, room_database: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        """Validate room ID consistency and patterns"""
        errors = []

        for room_id, room in room_database.items():
            # Check for missing ID
            if not room.get("id"):
                errors.append(
                    {
                        "type": "missing_id",
                        "room_id": room_id,
                        "message": "Room has no ID field",
                        "suggestion": "Add 'id' field to room data",
                    }
                )
                continue

            # Check ID consistency
            if room.get("id") != room_id:
                errors.append(
                    {
                        "type": "id_mismatch",
                        "room_id": room_id,
                        "message": f"Room ID mismatch: file has '{room_id}' but data has '{room.get('id')}'",
                        "suggestion": "Ensure room ID in data matches filename",
                    }
                )

        return errors

    def generate_validation_summary(self, room_database: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Generate comprehensive validation summary"""
        schema_errors = self.validate_schema(room_database)
        connectivity_errors = self.validate_connectivity(room_database)
        environment_errors = self.validate_environment_types(room_database)
        id_errors = self.validate_room_ids(room_database)

        total_errors = (
            sum(len(errors) for errors in schema_errors.values())
            + len(connectivity_errors)
            + len(environment_errors)
            + len(id_errors)
        )

        return {
            "total_rooms": len(room_database),
            "total_errors": total_errors,
            "schema_errors": sum(len(errors) for errors in schema_errors.values()),
            "connectivity_errors": len(connectivity_errors),
            "environment_errors": len(environment_errors),
            "id_errors": len(id_errors),
            "success": total_errors == 0,
            "error_breakdown": {
                "schema": schema_errors,
                "connectivity": connectivity_errors,
                "environment": environment_errors,
                "ids": id_errors,
            },
        }
