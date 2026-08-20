"""
Emote Service for handling predefined emote actions and their messages.

This service manages a collection of predefined emotes that players can use
with simple commands like 'twibble' or 'dance', automatically expanding them
to appropriate messages for both the player and room occupants.
"""

from typing import TYPE_CHECKING, TypedDict

from ..exceptions import ValidationError
from ..persistence.repositories.emote_repository import EmoteRepository
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)

if TYPE_CHECKING:  # pragma: no cover - type checking only
    from schemas.validator import SchemaValidator


_emote_validator: "SchemaValidator | None" = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, not a constant
_emote_validator_import_failed = False  # pylint: disable=invalid-name  # Reason: Private module-level cache flag, not a constant


def _get_emote_validator() -> "SchemaValidator | None":
    """Lazily instantiate and cache the emote schema validator."""
    global _emote_validator, _emote_validator_import_failed  # pylint: disable=global-statement  # Reason: Singleton pattern for validator caching

    if _emote_validator is not None:
        return _emote_validator

    if _emote_validator_import_failed:
        return None

    try:
        from schemas.validator import create_validator
    except ImportError as exc:  # pragma: no cover - environment without schemas package
        logger.warning("Emote schema validator unavailable", error=str(exc))
        _emote_validator_import_failed = True
        return None

    try:
        _emote_validator = create_validator("emote")
    except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging path  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Validator creation errors unpredictable, must handle gracefully
        logger.warning("Emote schema validator creation failed", error=str(exc))
        _emote_validator = None

    return _emote_validator


class EmoteDefinition(TypedDict):
    """Public emote payload returned by EmoteService lookups."""

    self_message: str
    other_message: str
    aliases: list[str]


class EmoteService:
    """Service for managing predefined emote actions and their messages.

    Construction is synchronous and does not load anything; call `await load_emotes()` once after
    construction (see server/container/bundles/game.py, matching SpellRegistry's pattern) before
    relying on emote lookups. This replaces the previous synchronous constructor's
    thread+new-event-loop workaround for the sync/async boundary (#624) -- construction no longer
    needs a workaround because it no longer does any I/O itself.
    """

    def __init__(self, emote_repository: EmoteRepository, emote_file_path: str | None = None) -> None:
        """
        Initialize the EmoteService.

        Args:
            emote_repository: Repository used by load_emotes() to fetch predefined emotes/aliases.
            emote_file_path: DEPRECATED - kept for backward compatibility only. Used solely as a
                            label in schema-validation error messages for custom emotes; unrelated
                            to predefined-emote loading.
        """
        self._emote_repository = emote_repository
        self.emote_file_path: str | None = emote_file_path
        self.emotes: dict[str, EmoteDefinition] = {}
        self.alias_to_emote: dict[str, str] = {}

    async def load_emotes(self) -> None:
        """Load predefined emote definitions from the database via the injected repository.

        Errors (including a missing emotes table) are logged and swallowed, not raised -- this
        allows custom emotes to keep working, and tests/environments without the emotes table to
        still function, matching the previous behavior.
        """
        try:
            emote_rows = await self._emote_repository.get_emotes()
            alias_rows = await self._emote_repository.get_emote_aliases()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Emote loading errors unpredictable, must allow graceful degradation
            error_str = str(e)
            if "does not exist" in error_str or "relation" in error_str.lower():
                logger.warning(
                    "Emotes table not found in database - custom emotes will still work",
                    error=error_str,
                )
            else:
                logger.warning("Failed to load emotes from database - custom emotes will still work", error=error_str)
            self.emotes = {}
            self.alias_to_emote = {}
            return

        aliases_by_stable_id: dict[str, list[str]] = {}
        for row in alias_rows:
            aliases_by_stable_id.setdefault(row["stable_id"], []).append(row["alias"])

        emotes: dict[str, EmoteDefinition] = {}
        for row in emote_rows:
            stable_id = row["stable_id"]
            emotes[stable_id] = {
                "self_message": row["self_message"],
                "other_message": row["other_message"],
                "aliases": aliases_by_stable_id.get(stable_id, []),
            }
        self.emotes = emotes

        # Build alias mapping
        alias_to_emote: dict[str, str] = {}
        for emote_name, emote_data in self.emotes.items():
            # The emote name itself is also an alias
            alias_to_emote[emote_name] = emote_name

            # Add explicit aliases
            for alias in emote_data.get("aliases", []):
                if alias in alias_to_emote:
                    logger.warning("Duplicate emote alias", alias=alias, existing_emote=alias_to_emote[alias])
                else:
                    alias_to_emote[alias] = emote_name
        self.alias_to_emote = alias_to_emote

        logger.info("Loaded emotes from database", emote_count=len(self.emotes), alias_count=len(self.alias_to_emote))

    def is_emote_alias(self, command: str) -> bool:
        """
        Check if a command is an emote alias.

        Args:
            command: The command to check

        Returns:
            True if the command is an emote alias, False otherwise
        """
        return command.lower() in self.alias_to_emote

    def get_emote_definition(self, command: str) -> EmoteDefinition | None:
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
            log_and_raise(
                ValidationError,
                f"Unknown emote: {command}",
                operation="format_emote_messages",
                command=command,
                player_name=player_name,
                details={"command": command, "player_name": player_name},
                user_friendly="Unknown emote command",
            )

        self_message = emote_def["self_message"]
        other_message = emote_def["other_message"].format(player_name=player_name)

        return self_message, other_message

    def list_available_emotes(self) -> dict[str, list[str]]:
        """
        Get a list of all available emotes and their aliases.

        Returns:
            Dict mapping emote names to their aliases
        """
        result: dict[str, list[str]] = {}
        for emote_name, emote_data in self.emotes.items():
            aliases = [emote_name] + emote_data.get("aliases", [])
            result[emote_name] = aliases
        return result

    async def reload_emotes(self) -> None:
        """Reload predefined emote definitions from the database."""
        logger.info("Reloading emote definitions")
        await self.load_emotes()

    def _validate_emote_payload(self, data: dict[str, object]) -> list[str]:
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
