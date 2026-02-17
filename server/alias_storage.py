"""Alias storage utilities for MythosMUD.

As noted in the restricted archives of Miskatonic University, this module
handles the persistence of player command aliases in JSON format, providing
a robust and extensible storage system for user-defined command shortcuts.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional, cast

from .models import Alias
from .structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

if TYPE_CHECKING:  # pragma: no cover - type checking only
    from schemas.validator import SchemaValidator


_ALIAS_VALIDATOR: Optional["SchemaValidator"] = None
_ALIAS_VALIDATOR_IMPORT_FAILED = False


def _get_alias_validator() -> Optional["SchemaValidator"]:
    """Lazily instantiate and cache the alias schema validator."""
    global _ALIAS_VALIDATOR, _ALIAS_VALIDATOR_IMPORT_FAILED  # pylint: disable=global-statement  # Reason: Singleton pattern for validator caching

    if _ALIAS_VALIDATOR is not None:
        return _ALIAS_VALIDATOR

    if _ALIAS_VALIDATOR_IMPORT_FAILED:
        return None

    try:
        from schemas.validator import create_validator
    except ImportError as exc:  # pragma: no cover - environment without schemas package
        logger.warning("Alias schema validator unavailable", error=str(exc))
        _ALIAS_VALIDATOR_IMPORT_FAILED = True
        return None

    try:
        _ALIAS_VALIDATOR = create_validator("alias")
    except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Validator creation errors unpredictable, must handle gracefully
        logger.warning("Alias schema validator creation failed", error=str(exc))
        _ALIAS_VALIDATOR = None

    return _ALIAS_VALIDATOR


class AliasStorage:
    """Manages player alias storage in JSON files.

    Each player's aliases are stored in a separate JSON file:
    data/players/aliases/{player_name}_aliases.json
    """

    def __init__(self, storage_dir: str | None = None) -> None:
        if storage_dir:
            self.storage_dir = Path(storage_dir)
        else:
            # AI Agent: Type narrowing - os.environ.get returns str | None
            aliases_dir = os.environ.get("ALIASES_DIR")
            if aliases_dir:
                self.storage_dir = Path(aliases_dir)
            else:
                raise ValueError(
                    "ALIASES_DIR environment variable must be set. See server/env.example for configuration template."
                )

        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def _get_alias_file_path(self, player_name: str) -> Path:
        """Get the file path for a player's aliases."""
        return self.storage_dir / f"{player_name}_aliases.json"

    def _load_alias_data(self, player_name: str) -> dict[str, Any]:
        """Load alias data from JSON file."""
        file_path = self._get_alias_file_path(player_name)

        if not file_path.exists():
            return {"version": "1.0", "aliases": []}

        try:
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)

            validation_errors = self._validate_alias_payload(data, file_path)
            if validation_errors:
                logger.error(
                    "Alias schema validation failed",
                    player_name=player_name,
                    file_path=str(file_path),
                    errors=validation_errors,
                )
                return {"version": "1.0", "aliases": []}

            return cast(dict[Any, Any], data)
        except (OSError, json.JSONDecodeError) as e:
            # Log error and return default structure
            logger.error("Error loading alias data", player_name=player_name, error=str(e))
            return {"version": "1.0", "aliases": []}

    def _save_alias_data(self, player_name: str, data: dict[str, Any]) -> bool:
        """Save alias data to JSON file."""
        file_path = self._get_alias_file_path(player_name)

        # Ensure directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        validation_errors = self._validate_alias_payload(data, file_path)
        if validation_errors:
            logger.error(
                "Aborting alias save due to schema validation failure",
                player_name=player_name,
                file_path=str(file_path),
                errors=validation_errors,
            )
            return False

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except OSError as e:
            logger.error("Error saving alias data", player_name=player_name, error=str(e))
            return False

    def get_player_aliases(self, player_name: str) -> list[Alias]:
        """Get all aliases for a player."""
        data = self._load_alias_data(player_name)
        aliases = []

        for alias_data in data.get("aliases", []):
            try:
                # Convert timestamp strings back to datetime objects
                # Handle both "Z" suffix and timezone-aware formats
                if "created_at" in alias_data:
                    ts_str = alias_data["created_at"]
                    # Remove "Z" and any timezone suffix, keep only naive datetime
                    ts_str = ts_str.replace("Z", "").split("+")[0]
                    alias_data["created_at"] = datetime.fromisoformat(ts_str)
                if "updated_at" in alias_data:
                    ts_str = alias_data["updated_at"]
                    ts_str = ts_str.replace("Z", "").split("+")[0]
                    alias_data["updated_at"] = datetime.fromisoformat(ts_str)

                alias = Alias(**alias_data)
                aliases.append(alias)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias parsing errors unpredictable, must continue processing
                logger.error("Error parsing alias data", error=str(e))
                continue

        return aliases

    def save_player_aliases(self, player_name: str, aliases: list[Alias]) -> bool:
        """Save aliases for a player."""
        # Convert aliases to JSON-serializable format
        alias_data = []
        for alias in aliases:
            alias_dict = alias.model_dump()
            alias_data.append(alias_dict)

        data = {"version": "1.0", "aliases": alias_data}

        return self._save_alias_data(player_name, data)

    def add_alias(self, player_name: str, alias: Alias) -> bool:
        """Add or update an alias for a player."""
        aliases = self.get_player_aliases(player_name)

        # Check if alias already exists
        existing_index = None
        for i, existing_alias in enumerate(aliases):
            if existing_alias.name.lower() == alias.name.lower():
                existing_index = i
                break

        if existing_index is not None:
            # Update existing alias
            aliases[existing_index] = alias
        else:
            # Add new alias
            aliases.append(alias)

        return self.save_player_aliases(player_name, aliases)

    def remove_alias(self, player_name: str, alias_name: str) -> bool:
        """Remove an alias for a player."""
        aliases = self.get_player_aliases(player_name)

        # Find and remove the alias
        for i, alias in enumerate(aliases):
            if alias.name.lower() == alias_name.lower():
                aliases.pop(i)
                return self.save_player_aliases(player_name, aliases)

        return False  # Alias not found

    def get_alias(self, player_name: str, alias_name: str) -> Alias | None:
        """Get a specific alias for a player."""
        aliases = self.get_player_aliases(player_name)

        for alias in aliases:
            if alias.name.lower() == alias_name.lower():
                return alias

        return None

    def clear_aliases(self, player_name: str) -> bool:
        """Clear all aliases for a player."""
        return self.save_player_aliases(player_name, [])

    def get_alias_count(self, player_name: str) -> int:
        """Get the number of aliases for a player."""
        aliases = self.get_player_aliases(player_name)
        return len(aliases)

    def validate_alias_name(self, alias_name: str) -> bool:
        """Validate alias name format."""
        if not alias_name or len(alias_name) > 20:
            return False

        # Check if it's a reserved command
        reserved_commands = {"alias", "aliases", "unalias", "help"}
        if alias_name.lower() in reserved_commands:
            return False

        # Check naming convention (alphanumeric + underscore, must start with letter)
        import re

        pattern = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        return bool(re.match(pattern, alias_name))

    def validate_alias_command(self, command: str) -> bool:
        """Validate alias command."""
        if not command or len(command) > 200:
            return False

        # Check if it's a reserved command
        reserved_commands = {"alias", "aliases", "unalias", "help"}
        first_word = command.strip().split()[0].lower() if command.strip() else ""
        if first_word in reserved_commands:
            return False

        return True

    def create_alias(self, player_name: str, name: str, command: str) -> Alias | None:
        """Create and save a new alias for a player."""
        # Validate inputs
        if not self.validate_alias_name(name):
            return None

        if not self.validate_alias_command(command):
            return None

        # Check alias limit (50 per player as per PLANNING_aliases.md)
        current_count = self.get_alias_count(player_name)
        if current_count >= 50:
            return None

        # Create new alias
        alias = Alias(name=name, command=command)

        # Save to storage
        if self.add_alias(player_name, alias):
            return alias

        return None

    def list_alias_files(self) -> list[str]:
        """List all alias files in the storage directory."""
        if not self.storage_dir.exists():
            return []

        files = []
        for file_path in self.storage_dir.glob("*_aliases.json"):
            # Extract player name from filename
            player_name = file_path.stem.replace("_aliases", "")
            files.append(player_name)

        return files

    def delete_player_aliases(self, player_name: str) -> bool:
        """Delete a player's alias file."""
        file_path = self._get_alias_file_path(player_name)

        if file_path.exists():
            try:
                file_path.unlink()
                return True
            except OSError as e:
                logger.error("Error deleting alias file", player_name=player_name, error=str(e))
                return False

        return True  # File doesn't exist, consider it "deleted"

    def backup_aliases(self, player_name: str, backup_dir: str | None = None) -> bool:
        """Create a backup of a player's aliases."""
        if backup_dir is None:
            backup_dir = str(self.storage_dir / "backups")

        backup_path = Path(backup_dir)
        backup_path.mkdir(parents=True, exist_ok=True)

        source_file = self._get_alias_file_path(player_name)
        if not source_file.exists():
            return False

        backup_file = backup_path / f"{player_name}_aliases_backup.json"

        try:
            import shutil

            shutil.copy2(source_file, backup_file)
            return True
        except OSError as e:
            logger.error("Error creating backup", player_name=player_name, error=str(e))
            return False

    def _validate_alias_payload(self, data: dict[str, Any], file_path: Path) -> list[str]:
        """
        Validate alias payload against the shared schema when available.

        Args:
            data: Alias payload to validate.
            file_path: Location of the payload for logging context.

        Returns:
            List of schema validation error strings. Empty if schema is unavailable or the data is valid.
        """
        validator = _get_alias_validator()
        if validator is None:
            return []
        return validator.validate_alias_bundle(data, str(file_path))
