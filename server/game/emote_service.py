"""
Emote Service for handling predefined emote actions and their messages.

This service manages a collection of predefined emotes that players can use
with simple commands like 'twibble' or 'dance', automatically expanding them
to appropriate messages for both the player and room occupants.
"""

import asyncio
import os
import threading
from typing import TYPE_CHECKING, Any, Optional

import asyncpg

from ..exceptions import ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

if TYPE_CHECKING:  # pragma: no cover - type checking only
    from schemas.validator import SchemaValidator


_EMOTE_VALIDATOR: Optional["SchemaValidator"] = None
_EMOTE_VALIDATOR_IMPORT_FAILED = False


def _get_emote_validator() -> Optional["SchemaValidator"]:
    """Lazily instantiate and cache the emote schema validator."""
    global _EMOTE_VALIDATOR, _EMOTE_VALIDATOR_IMPORT_FAILED

    if _EMOTE_VALIDATOR is not None:
        return _EMOTE_VALIDATOR

    if _EMOTE_VALIDATOR_IMPORT_FAILED:
        return None

    try:
        from schemas.validator import create_validator
    except ImportError as exc:  # pragma: no cover - environment without schemas package
        logger.warning("Emote schema validator unavailable", error=str(exc))
        _EMOTE_VALIDATOR_IMPORT_FAILED = True
        return None

    try:
        _EMOTE_VALIDATOR = create_validator("emote")
    except Exception as exc:  # pragma: no cover - defensive logging path
        logger.warning("Emote schema validator creation failed", error=str(exc))
        _EMOTE_VALIDATOR = None

    return _EMOTE_VALIDATOR


class EmoteService:
    """Service for managing predefined emote actions and their messages."""

    def __init__(self, emote_file_path: str | None = None):
        """
        Initialize the EmoteService.

        Args:
            emote_file_path: DEPRECATED - kept for backward compatibility only.
                            Emotes are now loaded from PostgreSQL database.
        """
        # Keep emote_file_path for backward compatibility but don't use it
        self.emote_file_path = emote_file_path
        self.emotes: dict[str, dict] = {}
        self.alias_to_emote: dict[str, str] = {}

        self._load_emotes()

    def _load_emotes(self) -> None:
        """Load emote definitions from PostgreSQL database."""
        result_container: dict[str, Any] = {"emotes": {}, "aliases": {}, "error": None}

        def run_async():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self._async_load_emotes(result_container))
            except Exception as e:
                # Catch exception and store in result_container instead of raising
                # This allows graceful degradation when database table doesn't exist
                result_container["error"] = e
            finally:
                new_loop.close()

        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join()

        error = result_container.get("error")
        if error is not None:
            # Log warning but don't raise - allow custom emotes to work even without database
            # This is important for tests and environments where the emotes table may not exist
            error_str = str(error)
            if "does not exist" in error_str or "relation" in error_str.lower():
                logger.warning(
                    "Emotes table not found in database - custom emotes will still work",
                    error=error_str,
                )
            else:
                logger.warning("Failed to load emotes from database - custom emotes will still work", error=error_str)
            # Continue with empty emotes - custom emotes don't need the database

        # Build emotes dictionary in expected format
        self.emotes = {}
        for stable_id, emote_data in result_container["emotes"].items():
            aliases = result_container["aliases"].get(stable_id, [])
            self.emotes[stable_id] = {
                "self_message": emote_data["self_message"],
                "other_message": emote_data["other_message"],
                "aliases": aliases,
            }

        # Build alias mapping
        self.alias_to_emote = {}
        for emote_name, emote_data in self.emotes.items():
            # The emote name itself is also an alias
            self.alias_to_emote[emote_name] = emote_name

            # Add explicit aliases
            aliases = emote_data.get("aliases", [])
            for alias in aliases:
                if alias in self.alias_to_emote:
                    logger.warning("Duplicate emote alias", alias=alias, existing_emote=self.alias_to_emote[alias])
                else:
                    self.alias_to_emote[alias] = emote_name

        logger.info("Loaded emotes from database", emote_count=len(self.emotes), alias_count=len(self.alias_to_emote))

    async def _async_load_emotes(self, result_container: dict[str, Any]) -> None:
        """Async helper to load emotes from PostgreSQL database."""
        try:
            # Get database URL from environment
            database_url = os.getenv("DATABASE_URL")
            if not database_url:
                raise ValueError("DATABASE_URL environment variable not set")

            # Convert SQLAlchemy-style URL to asyncpg-compatible format
            if database_url.startswith("postgresql+asyncpg://"):
                database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

            # Use asyncpg directly to avoid event loop conflicts
            conn = await asyncpg.connect(database_url)
            try:
                # Query emotes
                emotes_query = """
                    SELECT
                        stable_id,
                        self_message,
                        other_message
                    FROM emotes
                    ORDER BY stable_id
                """
                emote_rows = await conn.fetch(emotes_query)

                # Query emote aliases
                aliases_query = """
                    SELECT
                        e.stable_id,
                        ea.alias
                    FROM emote_aliases ea
                    JOIN emotes e ON ea.emote_id = e.id
                    ORDER BY e.stable_id, ea.alias
                """
                alias_rows = await conn.fetch(aliases_query)

                # Build emotes dictionary
                for row in emote_rows:
                    stable_id = row["stable_id"]
                    result_container["emotes"][stable_id] = {
                        "self_message": row["self_message"],
                        "other_message": row["other_message"],
                    }
                    result_container["aliases"][stable_id] = []

                # Build aliases dictionary
                for row in alias_rows:
                    stable_id = row["stable_id"]
                    alias = row["alias"]
                    if stable_id in result_container["aliases"]:
                        result_container["aliases"][stable_id].append(alias)
            finally:
                await conn.close()
        except Exception as e:
            # Store error in result_container - don't raise, let _load_emotes handle it
            result_container["error"] = e

    def is_emote_alias(self, command: str) -> bool:
        """
        Check if a command is an emote alias.

        Args:
            command: The command to check

        Returns:
            True if the command is an emote alias, False otherwise
        """
        return command.lower() in self.alias_to_emote

    def get_emote_definition(self, command: str) -> dict | None:
        """
        Get the emote definition for a command.

        Args:
            command: The command (emote name or alias)

        Returns:
            Emote definition dict or None if not found
        """
        emote_name = self.alias_to_emote.get(command.lower())
        if emote_name:
            return self.emotes.get(emote_name)
        return None

    def format_emote_messages(self, command: str, player_name: str) -> tuple[str, str]:
        """
        Format emote messages for the player and room occupants.

        Args:
            command: The emote command (e.g., 'twibble')
            player_name: Name of the player performing the emote

        Returns:
            Tuple of (self_message, other_message)

        Raises:
            ValueError: If the command is not a valid emote
        """
        emote_def = self.get_emote_definition(command)
        if not emote_def:
            context = create_error_context()
            context.metadata["command"] = command
            context.metadata["player_name"] = player_name
            context.metadata["operation"] = "format_emote_messages"
            log_and_raise(
                ValidationError,
                f"Unknown emote: {command}",
                context=context,
                details={"command": command, "player_name": player_name},
                user_friendly="Unknown emote command",
            )

        self_message = emote_def["self_message"]
        other_message = emote_def["other_message"].format(player_name=player_name)

        return self_message, other_message

    def list_available_emotes(self) -> dict[str, list]:
        """
        Get a list of all available emotes and their aliases.

        Returns:
            Dict mapping emote names to their aliases
        """
        result = {}
        for emote_name, emote_data in self.emotes.items():
            aliases = [emote_name] + emote_data.get("aliases", [])
            result[emote_name] = aliases
        return result

    def reload_emotes(self) -> None:
        """Reload emote definitions from the file."""
        logger.info("Reloading emote definitions")
        self._load_emotes()

    def _validate_emote_payload(self, data: dict) -> list[str]:
        """
        Validate emote definitions against the shared schema when available.

        Args:
            data: Emote payload to validate.

        Returns:
            List of schema validation errors. Empty if schema is unavailable or data is valid.
        """
        validator = _get_emote_validator()
        if validator is None:
            return []
        return validator.validate_emote_file(data, str(self.emote_file_path))
