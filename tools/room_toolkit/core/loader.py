"""
Enhanced Room Loader

Unified room loading with caching, validation, and metadata support.
Consolidates functionality from the original room_loader and mapbuilder.
"""

import glob
import json
import os
from typing import Any

from .schema_validator import SchemaValidator


class RoomLoader:
    """Enhanced room loader with caching and metadata support"""

    def __init__(self, base_path: str):
        self.base_path = base_path
        self._room_cache: dict[str, dict[str, Any]] = {}
        self._parsing_errors: list[tuple[str, str]] = []
        self._schema_validator = SchemaValidator("schemas/unified_room_schema.json")

    def build_room_database(self, show_progress: bool = False) -> dict[str, dict[str, Any]]:
        """Build complete room database with metadata"""
        if self._room_cache:
            return self._room_cache

        rooms = {}
        room_files = self._discover_room_files()

        if show_progress:
            print(f"Loading {len(room_files)} room files...")

        for file_path in room_files:
            try:
                with open(file_path, encoding="utf-8") as f:
                    data = json.load(f)

                # Extract room ID
                room_id = data.get("id")
                if not room_id:
                    room_id = os.path.splitext(os.path.basename(file_path))[0]

                # Add metadata
                data["_file_path"] = file_path
                data["_subzone"] = self._extract_subzone_from_path(file_path)
                data["_zone"] = self._extract_zone_from_path(file_path)

                rooms[room_id] = data

            except Exception as e:
                self._parsing_errors.append((file_path, str(e)))

        self._room_cache = rooms
        return rooms

    def _discover_room_files(self) -> list[str]:
        """Discover all room JSON files recursively"""
        pattern = os.path.join(self.base_path, "**/*.json")
        files = glob.glob(pattern, recursive=True)

        # Filter out config files
        filtered_files = []
        for f in files:
            basename = os.path.basename(f)
            if basename not in ["zone_config.json", "subzone_config.json"]:
                filtered_files.append(f)

        return sorted(filtered_files)

    def _extract_subzone_from_path(self, file_path: str) -> str | None:
        """Extract subzone from file path"""
        path_parts = file_path.replace("\\", "/").split("/")
        try:
            # Look for pattern: .../zone/subzone/room.json
            zone_index = -1
            for i, part in enumerate(path_parts):
                if part in ["earth", "yeng"]:  # Known zones
                    zone_index = i
                    break

            if zone_index >= 0 and zone_index + 1 < len(path_parts):
                return path_parts[zone_index + 1]
        except Exception:
            pass
        return None

    def _extract_zone_from_path(self, file_path: str) -> str | None:
        """Extract zone from file path"""
        path_parts = file_path.replace("\\", "/").split("/")
        try:
            for part in path_parts:
                if part in ["earth", "yeng"]:  # Known zones
                    return part
        except Exception:
            pass
        return None

    def get_rooms_by_zone(self, zone: str) -> dict[str, dict[str, Any]]:
        """Get rooms filtered by zone"""
        rooms = self.build_room_database()
        return {rid: room for rid, room in rooms.items() if room.get("_zone") == zone}

    def get_rooms_by_subzone(self, subzone: str) -> dict[str, dict[str, Any]]:
        """Get rooms filtered by subzone"""
        rooms = self.build_room_database()
        return {rid: room for rid, room in rooms.items() if room.get("_subzone") == subzone}

    def get_zones(self) -> list[str]:
        """Get list of all zones"""
        rooms = self.build_room_database()
        zones = set()
        for room in rooms.values():
            zone = room.get("_zone")
            if zone:
                zones.add(zone)
        return sorted(zones)

    def get_subzones(self) -> list[str]:
        """Get list of all subzones"""
        rooms = self.build_room_database()
        subzones = set()
        for room in rooms.values():
            subzone = room.get("_subzone")
            if subzone:
                subzones.add(subzone)
        return sorted(subzones)

    def get_parsing_errors(self) -> list[tuple[str, str]]:
        """Get list of parsing errors"""
        return self._parsing_errors.copy()

    def clear_cache(self):
        """Clear the room cache"""
        self._room_cache.clear()
        self._parsing_errors.clear()

    def load_with_coordinates(
        self, start_room: str
    ) -> tuple[dict[str, dict[str, Any]], dict[str, tuple[int, int]], list[str]]:
        """Load rooms with coordinate inference (from mapbuilder)"""
        rooms = self.build_room_database()

        # Direction -> delta mapping
        direction_deltas = {
            "north": (0, -1),
            "n": (0, -1),
            "south": (0, 1),
            "s": (0, 1),
            "east": (1, 0),
            "e": (1, 0),
            "west": (-1, 0),
            "w": (-1, 0),
            "up": (0, -1),
            "down": (0, 1),
        }

        coords = {}
        messages = []

        # First, record explicit coords
        for rid, room in rooms.items():
            if room.get("coords"):
                coords[rid] = tuple(room["coords"])

        # BFS from start room
        if start_room not in rooms:
            messages.append(f"Start room {start_room} not found in rooms")
            return rooms, coords, messages

        from collections import deque

        queue = deque()
        if start_room in coords:
            queue.append(start_room)
        else:
            coords[start_room] = (0, 0)
            queue.append(start_room)

        visited = set(queue)

        while queue:
            cur = queue.popleft()
            cur_coord = coords[cur]
            room = rooms[cur]

            for direction, dest in room.get("exits", {}).items():
                if not dest or dest not in rooms:
                    if dest:
                        messages.append(f"Room {cur} has exit to unknown room id {dest}")
                    continue

                delta = direction_deltas.get(direction.lower())
                if delta is None:
                    messages.append(f"Unknown direction '{direction}' in room {cur}")
                    if dest not in coords:
                        coords[dest] = (cur_coord[0], cur_coord[1])
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)
                    continue

                nx = cur_coord[0] + delta[0]
                ny = cur_coord[1] + delta[1]
                new_coord = (nx, ny)

                if dest in coords:
                    if coords[dest] != new_coord:
                        messages.append(
                            f"Coordinate conflict for {dest}: existing {coords[dest]} vs computed {new_coord} from {cur}->{direction}"
                        )
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)
                    continue
                else:
                    holder = next((r for r, c in coords.items() if c == new_coord), None)
                    if holder is not None:
                        messages.append(
                            f"Spatial collision: {dest} would be placed at {new_coord}, but {holder} already occupies it"
                        )
                    coords[dest] = new_coord
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)

        # Check for disconnected rooms
        disconnected = [rid for rid in rooms.keys() if rid not in coords]
        if disconnected:
            messages.append(f"{len(disconnected)} rooms disconnected (no coords assigned). Example: {disconnected[:5]}")

        return rooms, coords, messages

    def validate_room_structure(self, room_data: dict[str, Any]) -> list[str]:
        """Validate individual room structure"""
        errors = []

        # Basic structure checks
        if not isinstance(room_data, dict):
            errors.append("Room data must be a dictionary")
            return errors

        if "id" not in room_data:
            errors.append("Missing required field: id")

        if "exits" not in room_data:
            errors.append("Missing required field: exits")
        elif not isinstance(room_data["exits"], dict):
            errors.append("Exits must be a dictionary")

        # Environment type validation
        if "environment" in room_data:
            env = room_data["environment"]
            valid_environments = [
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
            ]
            if env not in valid_environments:
                errors.append(f"Invalid environment type: {env}")

        return errors
