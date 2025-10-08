"""
Room fixer for automatic issue resolution.

This module handles automatic fixing of common room validation issues,
implementing the corrective techniques described in the Pnakotic Manuscripts.
"""

import json
import shutil
from datetime import datetime
from pathlib import Path


class RoomFixer:
    """
    Automatically fixes common room validation issues.

    Implements safe correction techniques for dimensional mapping
    inconsistencies while preserving the integrity of eldritch architecture.
    """

    def __init__(self, base_path: str = "./data/local/rooms"):
        """
        Initialize the room fixer.

        Args:
            base_path: Base directory for room files
        """
        self.base_path = Path(base_path)
        self.fixes_applied = []
        self.fixes_failed = []

    def create_backup(self, file_path: Path) -> Path:
        """
        Create a backup of a room file.

        Args:
            file_path: Path to the file to backup

        Returns:
            Path to the backup file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_suffix(f".backup_{timestamp}.json")
        shutil.copy2(file_path, backup_path)
        return backup_path

    def load_room_file(self, file_path: Path) -> dict:
        """
        Load a room file safely.

        Args:
            file_path: Path to the room file

        Returns:
            Room data dictionary
        """
        try:
            with open(file_path, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            raise ValueError(f"Failed to load {file_path}: {e}") from e

    def save_room_file(self, file_path: Path, room_data: dict) -> None:
        """
        Save a room file safely.

        Args:
            file_path: Path to the room file
            room_data: Room data to save
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(room_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise ValueError(f"Failed to save {file_path}: {e}") from e

    def fix_bidirectional_connections(
        self,
        room_database: dict[str, dict],
        missing_returns: list[tuple[str, str, str, str]],
        create_backups: bool = False,
    ) -> list[str]:
        """
        Fix missing bidirectional connections.

        Args:
            room_database: Complete room database
            missing_returns: List of missing return paths
            create_backups: Whether to create backups before fixing

        Returns:
            List of fixed room IDs
        """
        fixed_rooms = []

        for room_a, _, room_b, direction_b in missing_returns:
            try:
                # Find the file for room_b
                room_b_data = room_database[room_b]
                zone = room_b_data.get("zone", "unknown")
                room_file = self.base_path / "rooms" / zone / f"{room_b}.json"

                if not room_file.exists():
                    self.fixes_failed.append(f"Could not find file for {room_b}")
                    continue

                # Create backup if requested
                if create_backups:
                    backup_path = self.create_backup(room_file)
                    self.fixes_applied.append(f"Created backup: {backup_path}")

                # Load and fix the room data
                room_data = self.load_room_file(room_file)

                # Add the missing return path
                if "exits" not in room_data:
                    room_data["exits"] = {}

                room_data["exits"][direction_b] = room_a

                # Save the fixed room
                self.save_room_file(room_file, room_data)

                fixed_rooms.append(room_b)
                self.fixes_applied.append(f"Added {direction_b} exit to {room_b} → {room_a}")

            except Exception as e:
                self.fixes_failed.append(f"Failed to fix {room_b}: {e}")

        return fixed_rooms

    def fix_self_references(
        self, room_database: dict[str, dict], self_references: list[tuple[str, str]], create_backups: bool = False
    ) -> list[str]:
        """
        Fix self-references by adding proper flags.

        Args:
            room_database: Complete room database
            self_references: List of self-reference issues
            create_backups: Whether to create backups before fixing

        Returns:
            List of fixed room IDs
        """
        fixed_rooms = []

        for room_id, direction in self_references:
            try:
                # Find the file for the room
                room_data = room_database[room_id]
                zone = room_data.get("zone", "unknown")
                room_file = self.base_path / "rooms" / zone / f"{room_id}.json"

                if not room_file.exists():
                    self.fixes_failed.append(f"Could not find file for {room_id}")
                    continue

                # Create backup if requested
                if create_backups:
                    backup_path = self.create_backup(room_file)
                    self.fixes_applied.append(f"Created backup: {backup_path}")

                # Load and fix the room data
                room_data = self.load_room_file(room_file)

                # Convert exit to new format with self_reference flag
                exit_data = room_data["exits"].get(direction)
                if isinstance(exit_data, str) and exit_data == room_id:
                    room_data["exits"][direction] = {"target": room_id, "flags": ["self_reference"]}
                elif isinstance(exit_data, dict):
                    if "flags" not in exit_data:
                        exit_data["flags"] = []
                    if "self_reference" not in exit_data["flags"]:
                        exit_data["flags"].append("self_reference")

                # Save the fixed room
                self.save_room_file(room_file, room_data)

                fixed_rooms.append(room_id)
                self.fixes_applied.append(f"Added self_reference flag to {room_id} {direction} exit")

            except Exception as e:
                self.fixes_failed.append(f"Failed to fix {room_id}: {e}")

        return fixed_rooms

    def fix_schema_issues(
        self, room_database: dict[str, dict], schema_errors: dict[str, list[str]], create_backups: bool = False
    ) -> list[str]:
        """
        Fix basic schema issues.

        Args:
            room_database: Complete room database
            schema_errors: Dictionary of room_id -> error messages
            create_backups: Whether to create backups before fixing

        Returns:
            List of fixed room IDs
        """
        fixed_rooms = []

        for room_id, errors in schema_errors.items():
            try:
                # Find the file for the room
                room_data = room_database[room_id]
                zone = room_data.get("zone", "unknown")
                room_file = self.base_path / "rooms" / zone / f"{room_id}.json"

                if not room_file.exists():
                    self.fixes_failed.append(f"Could not find file for {room_id}")
                    continue

                # Create backup if requested
                if create_backups:
                    backup_path = self.create_backup(room_file)
                    self.fixes_applied.append(f"Created backup: {backup_path}")

                # Load the room data
                room_data = self.load_room_file(room_file)

                # Apply fixes based on error types
                fixed = False

                for error in errors:
                    if "missing required field" in error.lower():
                        if "exits" not in room_data:
                            room_data["exits"] = {
                                "north": None,
                                "south": None,
                                "east": None,
                                "west": None,
                                "up": None,
                                "down": None,
                            }
                            fixed = True

                        if "field1" not in room_data:
                            room_data["field1"] = None
                            fixed = True

                        if "field2" not in room_data:
                            room_data["field2"] = None
                            fixed = True

                        if "field3" not in room_data:
                            room_data["field3"] = None
                            fixed = True

                if fixed:
                    # Save the fixed room
                    self.save_room_file(room_file, room_data)

                    fixed_rooms.append(room_id)
                    self.fixes_applied.append(f"Fixed schema issues in {room_id}")

            except Exception as e:
                self.fixes_failed.append(f"Failed to fix {room_id}: {e}")

        return fixed_rooms

    def get_fix_summary(self) -> dict:
        """
        Get a summary of applied fixes.

        Returns:
            Dictionary with fix statistics
        """
        return {
            "fixes_applied": len(self.fixes_applied),
            "fixes_failed": len(self.fixes_failed),
            "applied_fixes": self.fixes_applied,
            "failed_fixes": self.fixes_failed,
        }
