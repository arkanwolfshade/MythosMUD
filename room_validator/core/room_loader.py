"""
Room loader for discovering and parsing room definition files.

This module handles the discovery of room files in the data/rooms directory
structure and provides utilities for loading and parsing room data.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from tqdm import tqdm


class RoomLoader:
    """
    Handles discovery and loading of room definition files.

    As noted in the Pnakotic Manuscripts, proper cataloguing of dimensional
    locations is essential for maintaining the integrity of our eldritch
    architecture.
    """

    def __init__(self, base_path: str = "./data/rooms"):
        """
        Initialize the room loader.

        Args:
            base_path: Base directory containing room files organized by zones
        """
        self.base_path = Path(base_path)
        self.room_database: Dict[str, Dict] = {}
        self.parsing_errors: List[Tuple[str, str]] = []

    def discover_room_files(self, base_path: Optional[str] = None) -> List[Path]:
        """
        Recursively scan directory for all room JSON files.

        Args:
            base_path: Optional override for base path

        Returns:
            List of Path objects for discovered JSON files
        """
        search_path = Path(base_path) if base_path else self.base_path

        if not search_path.exists():
            raise FileNotFoundError(f"Base path does not exist: {search_path}")

        json_files = []
        for file_path in search_path.rglob("*.json"):
            if file_path.is_file():
                json_files.append(file_path)

        return sorted(json_files)

    def load_room_data(self, file_path: Path) -> Optional[Dict]:
        """
        Parse a single room file with error handling.

        Args:
            file_path: Path to the room JSON file

        Returns:
            Parsed room data or None if parsing failed
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                room_data = json.load(f)

            # Validate basic structure
            if not isinstance(room_data, dict):
                raise ValueError("Room data must be a JSON object")

            required_fields = ['id', 'name', 'description', 'zone', 'exits']
            for field in required_fields:
                if field not in room_data:
                    raise ValueError(f"Missing required field: {field}")

            return room_data

        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None
        except Exception as e:
            error_msg = f"Error loading room: {e}"
            self.parsing_errors.append((str(file_path), error_msg))
            return None

    def build_room_database(self, base_path: Optional[str] = None,
                           show_progress: bool = True) -> Dict[str, Dict]:
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
            print(f"⚠️  No JSON files found in {search_path}")
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
                room_id = room_data.get('id')
                if room_id:
                    self.room_database[room_id] = room_data
                else:
                    self.parsing_errors.append((str(file_path), "Missing room ID"))

        return self.room_database

    def get_zones(self) -> List[str]:
        """
        Return list of discovered zones.

        Returns:
            List of unique zone identifiers
        """
        zones = set()
        for room_data in self.room_database.values():
            zone = room_data.get('zone')
            if zone:
                zones.add(zone)
        return sorted(list(zones))

    def get_rooms_by_zone(self, zone: str) -> Dict[str, Dict]:
        """
        Get all rooms belonging to a specific zone.

        Args:
            zone: Zone identifier

        Returns:
            Dictionary of rooms in the specified zone
        """
        zone_rooms = {}
        for room_id, room_data in self.room_database.items():
            if room_data.get('zone') == zone:
                zone_rooms[room_id] = room_data
        return zone_rooms

    def get_parsing_errors(self) -> List[Tuple[str, str]]:
        """
        Get list of parsing errors encountered during loading.

        Returns:
            List of (file_path, error_message) tuples
        """
        return self.parsing_errors.copy()

    def validate_file_structure(self) -> List[str]:
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
            if not filename or '_' not in filename:
                warnings.append(f"Unusual filename pattern: {file_path}")

            # Check if file is in appropriate zone directory
            zone_dir = file_path.parent.name
            if zone_dir == 'rooms':
                warnings.append(f"Room file not in zone directory: {file_path}")

        return warnings
