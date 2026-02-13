"""
Room loader for discovering and parsing room definition files.

This module handles the discovery of room files in the data/local/rooms directory
structure and provides utilities for loading and parsing room data.
"""

import json
import re
from pathlib import Path

import click
from tqdm import tqdm


class RoomLoader:
    """
    Handles discovery and loading of room definition files.

    As noted in the Pnakotic Manuscripts, proper cataloguing of dimensional
    locations is essential for maintaining the integrity of our eldritch
    architecture.
    """

    def __init__(self, base_path: str = "./data/local/rooms"):
        """
        Initialize the room loader.

        Args:
            base_path: Base directory containing room files organized by zones
        """
        self.base_path = Path(base_path)
        self.room_database: dict[str, dict] = {}
        self.parsing_errors: list[tuple[str, str]] = []

    def parse_room_filename(self, filename: str) -> dict[str, str | int] | None:
        """
        Parse room filename according to unified naming schema.

        Supports both old and new naming patterns:

        New Schema:
        - room_{street}_{number:03d}.json
        - intersection_{street_a}_{street_b}.json

        Old Schema (legacy support):
        - {Direction}_{StreetName}_{Number}.json
        - intersection_{StreetA}_{StreetB}.json

        Args:
            filename: Room filename to parse

        Returns:
            Dictionary with parsed components or None if invalid
        """
        if not filename.endswith(".json"):
            return None

        name = filename[:-5]  # Remove .json extension

        # New schema patterns
        room_pattern = r"^room_([a-z0-9_]+)_(\d{3})$"
        intersection_pattern = r"^intersection_([a-z0-9_]+)_([a-z0-9_]+)$"

        # Try new schema first
        room_match = re.match(room_pattern, name)
        if room_match:
            return {"type": "room", "street": room_match.group(1), "number": int(room_match.group(2))}

        intersection_match = re.match(intersection_pattern, name)
        if intersection_match:
            return {
                "type": "intersection",
                "street_a": intersection_match.group(1),
                "street_b": intersection_match.group(2),
            }

        # Legacy schema patterns
        legacy_room_pattern = r"^([NESW])_([A-Za-z0-9_]+)_(\d{3})$"
        legacy_intersection_pattern = r"^intersection_([A-Za-z0-9_]+)_([A-Za-z0-9_]+)$"

        legacy_room_match = re.match(legacy_room_pattern, name)
        if legacy_room_match:
            return {
                "type": "room",
                "direction": legacy_room_match.group(1),
                "street": legacy_room_match.group(2).lower(),
                "number": int(legacy_room_match.group(3)),
                "legacy": True,
            }

        legacy_intersection_match = re.match(legacy_intersection_pattern, name)
        if legacy_intersection_match:
            return {
                "type": "intersection",
                "street_a": legacy_intersection_match.group(1).lower(),
                "street_b": legacy_intersection_match.group(2).lower(),
                "legacy": True,
            }

        return None

    def generate_room_id(self, parsed_filename: dict, plane: str, zone: str, sub_zone: str) -> str:
        """
        Generate room ID from parsed filename and location data.

        Args:
            parsed_filename: Parsed filename data from parse_room_filename
            plane: Plane identifier
            zone: Zone identifier
            sub_zone: Sub-zone identifier

        Returns:
            Generated room ID
        """
        if parsed_filename["type"] == "room":
            if parsed_filename.get("legacy"):
                # Legacy format: earth_arkhamcity_northside_derby_st_001
                street_name = parsed_filename["street"].replace("_", " ")
                return f"{plane}_{zone}_{sub_zone}_{street_name}_{parsed_filename['number']:03d}"
            else:
                # New format: earth_arkhamcity_northside_room_derby_001
                return f"{plane}_{zone}_{sub_zone}_room_{parsed_filename['street']}_{parsed_filename['number']:03d}"
        else:  # intersection
            if parsed_filename.get("legacy"):
                # Legacy format: earth_arkhamcity_intersection_Derby_High
                street_a = parsed_filename["street_a"].replace("_", " ")
                street_b = parsed_filename["street_b"].replace("_", " ")
                return f"{plane}_{zone}_intersection_{street_a}_{street_b}"
            else:
                # New format: earth_arkhamcity_northside_intersection_derby_high
                return f"{plane}_{zone}_{sub_zone}_intersection_{parsed_filename['street_a']}_{parsed_filename['street_b']}"

    def discover_room_files(self, base_path: str | None = None) -> list[Path]:
        """
        Recursively scan directory for all room JSON files.

        Args:
            base_path: Optional override for base path

        Returns:
            List of Path objects for discovered room JSON files
            (excludes config files)
        """
        search_path = Path(base_path) if base_path else self.base_path

        if not search_path.exists():
            raise FileNotFoundError(f"Base path does not exist: {search_path}")

        json_files = []
        for file_path in search_path.rglob("*.json"):
            if file_path.is_file():
                # Skip configuration files - they are not room files
                config_files = ["subzone_config.json", "zone_config.json"]
                if file_path.name in config_files:
                    continue
                json_files.append(file_path)

        return sorted(json_files)

    def _validate_room_structure(self, room_data: dict) -> None:
        """Validate basic room structure."""
        if not isinstance(room_data, dict):
            raise ValueError("Room data must be a JSON object")

    def _extract_location_from_path(self, path_parts: tuple[str, ...]) -> tuple[str, str, str] | None:
        """Extract plane, zone, sub_zone from file path."""
        if len(path_parts) >= 4:
            return path_parts[-4], path_parts[-3], path_parts[-2]
        return None

    def _validate_or_update_room_id(
        self, room_data: dict, file_path: Path, parsed_filename: dict, location: tuple[str, str, str]
    ) -> None:
        """Validate or update room ID based on filename and location."""
        plane, zone, sub_zone = location
        expected_id = self.generate_room_id(parsed_filename, plane, zone, sub_zone)

        if "id" not in room_data:
            room_data["id"] = expected_id
        elif room_data["id"] != expected_id:
            self.parsing_errors.append(
                (str(file_path), f"Room ID mismatch: expected {expected_id}, got {room_data['id']}")
            )

    def _validate_required_fields(self, room_data: dict) -> None:
        """Validate required fields are present."""
        required_fields = ["id", "name", "description", "exits"]
        for field in required_fields:
            if field not in room_data:
                raise ValueError(f"Missing required field: {field}")

    def _add_location_fields(self, room_data: dict, path_parts: tuple[str, ...]) -> None:
        """Add location fields if missing."""
        if len(path_parts) >= 4:
            if "plane" not in room_data:
                room_data["plane"] = path_parts[-4]
            if "zone" not in room_data:
                room_data["zone"] = path_parts[-3]
            if "sub_zone" not in room_data:
                room_data["sub_zone"] = path_parts[-2]

    def load_room_data(self, file_path: Path) -> dict | None:
        """
        Parse a single room file with error handling.

        Args:
            file_path: Path to the room JSON file

        Returns:
            Parsed room data or None if parsing failed
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                room_data = json.load(f)

            self._validate_room_structure(room_data)

            parsed_filename = self.parse_room_filename(file_path.name)
            path_parts = file_path.parts

            if parsed_filename:
                location = self._extract_location_from_path(path_parts)
                if location:
                    self._validate_or_update_room_id(room_data, file_path, parsed_filename, location)

            self._validate_required_fields(room_data)
            self._add_location_fields(room_data, path_parts)

            return room_data

        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None
        except (OSError, ValueError) as e:
            # OSError covers FileNotFoundError, PermissionError, and other I/O errors
            # ValueError covers validation errors from _validate_room_structure and _validate_required_fields
            error_msg = f"Error loading room: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None

    def build_room_database(self, base_path: str | None = None, show_progress: bool = True) -> dict[str, dict]:
        """
        Create complete room index from all discovered files.

        Args:
            base_path: Optional override for base path
            show_progress: Whether to show progress bar

        Returns:
            Dictionary mapping room IDs to room data
        """
        search_path = Path(base_path) if base_path else self.base_path
        json_files = self.discover_room_files(str(search_path))

        if not json_files:
            click.secho(f"⚠️  No JSON files found in {search_path}", fg="yellow", err=True)
            return {}

        # Clear previous data
        self.room_database.clear()
        self.parsing_errors.clear()

        # Process files with optional progress bar
        if show_progress:
            files_to_process = tqdm(json_files, desc="Processing rooms")
        else:
            files_to_process = json_files

        for file_path in files_to_process:
            room_data = self.load_room_data(file_path)
            if room_data:
                room_id = room_data.get("id")
                if room_id:
                    self.room_database[room_id] = room_data
                else:
                    self.parsing_errors.append((str(file_path), "Missing room ID"))

        # Load referenced intersection files
        self._load_referenced_intersections(base_path)

        return self.room_database

    def _get_referenced_room_ids(self) -> set[str]:
        """Get all referenced room IDs from current database."""
        referenced_rooms = set()
        for room_data in self.room_database.values():
            exits = room_data.get("exits", {})
            for _direction, target_room in exits.items():
                if target_room and isinstance(target_room, str):
                    referenced_rooms.add(target_room)
        return referenced_rooms

    def _check_intersection_references_rooms(self, intersection_data: dict) -> bool:
        """Check if intersection references any rooms in our database."""
        exits = intersection_data.get("exits", {})
        for _direction, target_room in exits.items():
            if target_room and isinstance(target_room, str):
                if target_room in self.room_database:
                    return True
        return False

    def _add_intersection_to_database(self, intersection_data: dict) -> None:
        """Add intersection to database if it has a valid ID."""
        room_id = intersection_data.get("id")
        if room_id:
            self.room_database[room_id] = intersection_data

    def _load_referenced_intersections(self, base_path: str | None = None):
        """
        Load intersection files that are referenced by rooms in the database.

        Args:
            base_path: Optional override for base path
        """
        search_path = Path(base_path) if base_path else self.base_path

        intersection_dir = search_path / "intersections"
        if not intersection_dir.exists():
            return

        for intersection_file in intersection_dir.glob("*.json"):
            if intersection_file.name in ["subzone_config.json", "zone_config.json"]:
                continue

            intersection_data = self.load_room_data(intersection_file)
            if not intersection_data:
                continue

            if self._check_intersection_references_rooms(intersection_data):
                self._add_intersection_to_database(intersection_data)

    def get_zones(self) -> list[str]:
        """
        Return list of discovered zones.

        Returns:
            List of unique zone identifiers
        """
        zones = set()
        for room_data in self.room_database.values():
            zone = room_data.get("zone")
            if zone:
                zones.add(zone)
        return sorted(zones)

    def get_subzones(self) -> list[str]:
        """
        Return list of discovered sub-zones.

        Returns:
            List of unique sub-zone identifiers
        """
        subzones = set()
        for room_data in self.room_database.values():
            sub_zone = room_data.get("sub_zone")
            if sub_zone:
                subzones.add(sub_zone)
        return sorted(subzones)

    def count_config_subzones(self, base_path: str | None = None) -> int:
        """
        Count the number of sub-zone configuration files.

        Args:
            base_path: Optional override for base path

        Returns:
            Number of sub-zone configuration files found
        """
        config_files = self.discover_config_files(base_path)
        return len(config_files["subzone_config"])

    def get_rooms_by_zone(self, zone: str) -> dict[str, dict]:
        """
        Get all rooms belonging to a specific zone.

        Args:
            zone: Zone identifier

        Returns:
            Dictionary of rooms in the specified zone
        """
        zone_rooms = {}
        for room_id, room_data in self.room_database.items():
            if room_data.get("zone") == zone:
                zone_rooms[room_id] = room_data
        return zone_rooms

    def get_parsing_errors(self) -> list[tuple[str, str]]:
        """
        Get list of parsing errors encountered during loading.

        Returns:
            List of (file_path, error_message) tuples
        """
        return self.parsing_errors.copy()

    def validate_file_structure(self) -> list[str]:
        """
        Validate that room files follow expected naming convention.

        Returns:
            List of validation warnings
        """
        warnings = []
        json_files = self.discover_room_files()

        for file_path in json_files:
            # Check if filename matches expected pattern
            filename = file_path.stem
            if not filename or "_" not in filename:
                warnings.append(f"Unusual filename pattern: {file_path}")

            # Check if file is in appropriate zone directory
            zone_dir = file_path.parent.name
            if zone_dir == "rooms":
                warnings.append(f"Room file not in zone directory: {file_path}")

        return warnings

    def discover_config_files(self, base_path: str | None = None) -> dict[str, list[Path]]:
        """
        Discover configuration files (subzone_config.json, zone_config.json).

        Args:
            base_path: Optional override for base path

        Returns:
            Dictionary mapping config types to lists of file paths
        """
        search_path = Path(base_path) if base_path else self.base_path
        config_files: dict[str, list[Path]] = {"subzone_config": [], "zone_config": []}

        if not search_path.exists():
            return config_files

        for file_path in search_path.rglob("*.json"):
            if file_path.is_file():
                if file_path.name == "subzone_config.json":
                    config_files["subzone_config"].append(file_path)
                elif file_path.name == "zone_config.json":
                    config_files["zone_config"].append(file_path)

        return config_files

    def load_config_file(self, file_path: Path) -> dict | None:
        """
        Load a configuration file with error handling.

        Args:
            file_path: Path to the configuration JSON file

        Returns:
            Parsed configuration data or None if parsing failed
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                config_data = json.load(f)

            # Validate basic structure
            if not isinstance(config_data, dict):
                raise ValueError("Configuration data must be a JSON object")

            return config_data

        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None
        except (OSError, ValueError) as e:
            # OSError covers FileNotFoundError, PermissionError, and other I/O errors
            # ValueError covers validation errors from the isinstance check
            error_msg = f"Error loading config: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None
