"""Alias storage utilities for MythosMUD.

As noted in the restricted archives of Miskatonic University, this module
handles the persistence of player command aliases in JSON format, providing
a robust and extensible storage system for user-defined command shortcuts.
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, TypeAlias, cast

from .models.alias import Alias
from .structured_logging.enhanced_logging_config import get_logger
from .validators.security_validator import validate_player_name

logger = get_logger(__name__)

if TYPE_CHECKING:  # pragma: no cover - type checking only
    from schemas.validator import SchemaValidator

# JSON alias bundle / record shapes (no typing.Any — basedpyright reportExplicitAny).
# TypeAlias (not PEP 695 `type`) so older AST parsers (Codacy) accept the module.
# noqa UP040: PEP 695 `type` is a syntax error for Codacy's Python parser.
AliasPayload: TypeAlias = dict[str, object]  # noqa: UP040
AliasRecord: TypeAlias = dict[str, object]  # noqa: UP040


class _AliasValidatorCache:  # pylint: disable=too-few-public-methods  # Reason: private holder for lazy schema validator state
    """Mutable cache for the lazy schema validator (avoids redefining module constants)."""

    __slots__: tuple[str, ...] = ("import_failed", "validator")

    def __init__(self) -> None:
        self.validator: SchemaValidator | None = None
        self.import_failed: bool = False


_alias_validator_cache = _AliasValidatorCache()


def _empty_alias_payload() -> AliasPayload:
    return {"version": "1.0", "aliases": []}


def _as_alias_payload(raw: object) -> AliasPayload | None:
    """Narrow json.load output to a string-keyed object map."""
    if not isinstance(raw, dict):
        return None
    return cast(AliasPayload, raw)


def _as_alias_record(raw: object) -> AliasRecord | None:
    if not isinstance(raw, dict):
        return None
    return cast(AliasRecord, raw)


def _parse_alias_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    ts_str = value.replace("Z", "").split("+")[0]
    return datetime.fromisoformat(ts_str)


def _apply_alias_timestamps(record: AliasRecord) -> None:
    """Normalize created_at/updated_at JSON strings to naive datetime in place."""
    for key in ("created_at", "updated_at"):
        parsed = _parse_alias_timestamp(record.get(key))
        if parsed is not None:
            record[key] = parsed


def _get_alias_validator() -> "SchemaValidator | None":
    """Lazily instantiate and cache the alias schema validator."""
    cache = _alias_validator_cache

    if cache.validator is not None:
        return cache.validator

    if cache.import_failed:
        return None

    try:
        from schemas.validator import create_validator
    except ImportError as exc:  # pragma: no cover - environment without schemas package
        logger.warning("Alias schema validator unavailable", error=str(exc))
        cache.import_failed = True
        return None

    try:
        cache.validator = create_validator("alias")
    except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Validator creation errors unpredictable, must handle gracefully
        logger.warning("Alias schema validator creation failed", error=str(exc))
        cache.validator = None

    return cache.validator


class AliasStorage:
    """Manages player alias storage in JSON files.

    Each player's aliases are stored in a separate JSON file:
    data/players/aliases/{player_name}_aliases.json
    """

    storage_dir: Path

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

    def get_alias_file_path(self, player_name: str) -> Path:
        """Get the file path for a player's aliases.

        Human: reject path separators / traversal in player_name before touching disk.
        AI: CodeQL py/path-injection — basename + realpath/commonpath containment (recognized barriers).
        """
        if not player_name:
            raise ValueError("Player name is required for alias storage path")
        safe_name = validate_player_name(player_name)
        # Drop any directory components; CodeQL treats basename as a path sanitizer.
        safe_name = os.path.basename(safe_name)
        if ".." in safe_name or os.sep in safe_name or (os.altsep is not None and os.altsep in safe_name):
            raise ValueError("Invalid player name for alias path")
        base_dir = os.path.realpath(str(self.storage_dir))
        candidate = os.path.realpath(os.path.join(base_dir, f"{safe_name}_aliases.json"))
        if os.path.commonpath([base_dir, candidate]) != base_dir:
            raise ValueError("Alias path escapes storage directory")
        return Path(candidate)

    def _resolved_alias_open_path(self, player_name: str) -> str:
        """Absolute str path for open(); re-checks containment at the open site.

        Human: CodeQL taints path from player_name through load/save; barrier must be
        adjacent to open() on a realpath str, not only in the Path builder.
        AI: Keep this as a named defense-in-depth step immediately before every open.
        """
        base = os.path.realpath(str(self.storage_dir))
        path = os.path.realpath(str(self.get_alias_file_path(player_name)))
        if os.path.commonpath([base, path]) != base:
            raise ValueError("Alias path escapes storage directory")
        return path

    def _load_alias_data(self, player_name: str) -> AliasPayload:
        """Load alias data from JSON file."""
        # Re-assert containment at open site (CodeQL py/path-injection barrier).
        open_path = self._resolved_alias_open_path(player_name)
        file_path = Path(open_path)

        if not file_path.exists():
            return _empty_alias_payload()

        try:
            with open(open_path, encoding="utf-8") as f:
                raw: object = cast(object, json.load(f))

            data = _as_alias_payload(raw)
            if data is None:
                logger.error(
                    "Alias file root is not an object",
                    player_name=player_name,
                    file_path=open_path,
                )
                return _empty_alias_payload()

            validation_errors = self._validate_alias_payload(data, file_path)
            if validation_errors:
                logger.error(
                    "Alias schema validation failed",
                    player_name=player_name,
                    file_path=open_path,
                    errors=validation_errors,
                )
                return _empty_alias_payload()

            return data
        except (OSError, json.JSONDecodeError) as e:
            # Log error and return default structure
            logger.error("Error loading alias data", player_name=player_name, error=str(e))
            return _empty_alias_payload()

    def _save_alias_data(self, player_name: str, data: AliasPayload) -> bool:
        """Save alias data to JSON file."""
        # Re-assert containment at open site (CodeQL py/path-injection barrier).
        open_path = self._resolved_alias_open_path(player_name)
        file_path = Path(open_path)

        # Ensure directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        validation_errors = self._validate_alias_payload(data, file_path)
        if validation_errors:
            logger.error(
                "Aborting alias save due to schema validation failure",
                player_name=player_name,
                file_path=open_path,
                errors=validation_errors,
            )
            return False

        try:
            with open(open_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except OSError as e:
            logger.error("Error saving alias data", player_name=player_name, error=str(e))
            return False

    def get_player_aliases(self, player_name: str) -> list[Alias]:
        """Get all aliases for a player."""
        data = self._load_alias_data(player_name)
        aliases: list[Alias] = []

        raw_aliases: object = data.get("aliases", [])
        if not isinstance(raw_aliases, list):
            return aliases

        for raw_entry in cast(list[object], raw_aliases):
            alias_data = _as_alias_record(raw_entry)
            if alias_data is None:
                continue
            try:
                # Convert timestamp strings back to datetime objects
                # Handle both "Z" suffix and timezone-aware formats
                record: AliasRecord = dict(alias_data)
                _apply_alias_timestamps(record)
                alias = Alias.model_validate(record)
                aliases.append(alias)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias parsing errors unpredictable, must continue processing
                logger.error("Error parsing alias data", error=str(e))
                continue

        return aliases

    def save_player_aliases(self, player_name: str, aliases: list[Alias]) -> bool:
        """Save aliases for a player."""
        # Convert aliases to JSON-serializable format
        alias_data: list[AliasRecord] = []
        for alias in aliases:
            alias_dict = cast(AliasRecord, cast(object, alias.model_dump()))
            alias_data.append(alias_dict)

        data: AliasPayload = {"version": "1.0", "aliases": alias_data}

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
                del aliases[i]
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

        files: list[str] = []
        for file_path in self.storage_dir.glob("*_aliases.json"):
            # Extract player name from filename
            player_name = file_path.stem.replace("_aliases", "")
            files.append(player_name)

        return files

    def delete_player_aliases(self, player_name: str) -> bool:
        """Delete a player's alias file."""
        file_path = self.get_alias_file_path(player_name)

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

        source_file = self.get_alias_file_path(player_name)
        if not source_file.exists():
            return False

        backup_file = backup_path / f"{player_name}_aliases_backup.json"

        try:
            _ = shutil.copy2(source_file, backup_file)
            return True
        except OSError as e:
            logger.error("Error creating backup", player_name=player_name, error=str(e))
            return False

    def _validate_alias_payload(self, data: AliasPayload, file_path: Path) -> list[str]:
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
        # SchemaValidator.validate_alias_bundle is typed with dict[str, Any] for JSON generality.
        return validator.validate_alias_bundle(data, str(file_path))
