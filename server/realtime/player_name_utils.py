"""
Player name extraction and validation utilities.

This module provides utilities for safely extracting and validating player names
from player objects, ensuring UUIDs are never used as names (security requirement).

As documented in "Identity Protection Protocols" - Dr. Armitage, 1928
"""

import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..logging.enhanced_logging_config import get_logger


class PlayerNameExtractor:
    """
    Utility class for extracting and validating player names.

    CRITICAL: NEVER uses UUID as fallback for player name - security issue.
    """

    def __init__(self) -> None:
        """Initialize the player name extractor."""
        self._logger = get_logger("PlayerNameExtractor")

    def _is_uuid_string(self, value: str) -> bool:
        """
        Check if a string looks like a UUID.

        Args:
            value: The string to check

        Returns:
            True if string matches UUID format, False otherwise
        """
        return len(value) == 36 and value.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in value)

    def _is_valid_name(self, name: Any) -> bool:
        """
        Check if a name is valid (non-empty string, not a UUID).

        Args:
            name: The name to validate

        Returns:
            True if name is valid, False otherwise
        """
        if not name or not isinstance(name, str) or not name.strip():
            return False
        return not self._is_uuid_string(name)

    def _is_valid_name_string(self, name: Any) -> bool:
        """
        Check if a name is a valid non-UUID string.

        Args:
            name: The name to validate

        Returns:
            True if name is valid, False otherwise
        """
        return name and isinstance(name, str) and not self._is_uuid_string(name)

    def _extract_initial_player_name(self, player: Any) -> str | None:
        """
        Extract initial player name from player object.

        Args:
            player: The player object

        Returns:
            Player name string or None if not found
        """
        if hasattr(player, "name"):
            return player.name
        return getattr(player, "name", None)

    def _try_player_username(self, player: Any) -> str | None:
        """
        Try to get username from player object.

        Args:
            player: The player object

        Returns:
            Username string or None if not found
        """
        if hasattr(player, "username"):
            username = player.username
            if self._is_valid_name_string(username):
                return username

        username = getattr(player, "username", None)
        if self._is_valid_name_string(username):
            return username

        return None

    def _get_name_from_user_object(self, user: Any) -> str | None:
        """
        Get name from user object (username or display_name).

        Args:
            user: The user object

        Returns:
            Name string or None if not found
        """
        # Try username first
        if hasattr(user, "username") and user.username:
            return user.username

        # Try display_name
        if hasattr(user, "display_name") and user.display_name:
            return user.display_name

        # Fallback to getattr
        return getattr(user, "username", None) or getattr(user, "display_name", None)

    def _try_user_object_name(self, player: Any) -> str | None:
        """
        Try to get name from related User object.

        Args:
            player: The player object

        Returns:
            Name string or None if not found
        """
        if not hasattr(player, "user"):
            return None

        try:
            user = getattr(player, "user", None)
            if not user:
                return None

            return self._get_name_from_user_object(user)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.debug("Error accessing user relationship", error=str(e))
            return None

    def _try_fallback_name_sources(self, player: Any, current_name: str | None) -> str | None:
        """
        Try to get player name from fallback sources (username, user object).

        Args:
            player: The player object
            current_name: Current name value (may be None or invalid)

        Returns:
            Player name string or None if not found
        """
        # If current name is valid, return it
        if self._is_valid_name_string(current_name):
            return current_name

        # Try username attribute (from User model)
        username = self._try_player_username(player)
        if username:
            return username

        # Try to get name from related User object
        return self._try_user_object_name(player)

    def _validate_name_basic(
        self, player_name: str | None, player_id_str: str, player_id_uuid: uuid.UUID, player: Any
    ) -> str | None:
        """
        Perform basic validation on player name (not None, is string, not empty).

        Args:
            player_name: The player name to validate
            player_id_str: The player's ID as string
            player_id_uuid: The player's UUID
            player: The player object for logging

        Returns:
            Validated and stripped player name string or None if invalid
        """
        # Check if None or empty
        if not player_name:
            self._logger.warning(
                "Player name is None or empty, skipping from occupants",
                player_id=player_id_str,
                player_id_uuid=str(player_id_uuid),
                has_name_attr=hasattr(player, "name"),
                player_type=type(player).__name__,
            )
            return None

        # Type system guarantees player_name is str at this point (str | None -> str after None check)
        # No need for isinstance check - mypy would flag it as unreachable

        # Strip whitespace and check if empty after stripping
        player_name = player_name.strip()
        if not player_name:
            self._logger.warning(
                "Player name is empty after stripping, skipping from occupants",
                player_id=player_id_str,
                player_id_uuid=str(player_id_uuid),
            )
            return None

        return player_name

    def _check_uuid_pattern_match(self, player_name: str) -> bool:
        """
        Check if player name matches UUID pattern.

        Args:
            player_name: The player name to check

        Returns:
            True if name matches UUID pattern, False otherwise
        """
        return (
            len(player_name) == 36
            and player_name.count("-") == 4
            and all(c in "0123456789abcdefABCDEF-" for c in player_name)
        )

    def _check_uuid_string_matches(self, player_name: str, player_id_str: str, player_id_uuid: uuid.UUID) -> bool:
        """
        Check if player name matches any UUID string representation.

        Args:
            player_name: The player name to check
            player_id_str: The player's ID as string
            player_id_uuid: The player's UUID

        Returns:
            True if name matches UUID string, False otherwise
        """
        uuid_str = str(player_id_uuid)
        return player_name == player_id_str or player_name == uuid_str or player_name.lower() == uuid_str.lower()

    def _log_uuid_validation_failure(
        self,
        player_name: str,
        player_id_str: str,
        player_id_uuid: uuid.UUID,
        player: Any,
        is_uuid_pattern: bool,
        is_critical: bool,
    ) -> None:
        """
        Log UUID validation failure with appropriate level and message.

        Args:
            player_name: The invalid player name
            player_id_str: The player's ID as string
            player_id_uuid: The player's UUID
            player: The player object for logging
            is_uuid_pattern: Whether name matches UUID pattern
            is_critical: Whether this is a critical error
        """
        if is_critical:
            self._logger.error(
                "CRITICAL: Attempted to add player with UUID as name - this should never happen",
                player_id=player_id_str,
                player_id_uuid=str(player_id_uuid),
                player_name=player_name,
            )
        elif is_uuid_pattern:
            self._logger.warning(
                "Player name appears to be UUID, skipping from occupants",
                player_id=player_id_str,
                player_id_uuid=str(player_id_uuid),
                player_name=player_name,
                player_type=type(player).__name__,
                has_name_attr=hasattr(player, "name"),
                name_value=getattr(player, "name", "NOT_FOUND"),
                is_exact_match=(player_name == player_id_str),
                is_uuid_pattern=is_uuid_pattern,
            )
        else:
            self._logger.warning(
                "Player name matches UUID string representation, skipping from occupants",
                player_id=player_id_str,
                player_id_uuid=str(player_id_uuid),
                player_name=player_name,
            )

    def _validate_name_not_uuid(
        self, player_name: str, player_id_str: str, player_id_uuid: uuid.UUID, player: Any
    ) -> bool:
        """
        Validate that player name is not a UUID string.

        Args:
            player_name: The player name to validate
            player_id_str: The player's ID as string
            player_id_uuid: The player's UUID
            player: The player object for logging

        Returns:
            True if name is valid (not a UUID), False otherwise
        """
        # Check UUID pattern
        is_uuid_pattern = self._check_uuid_pattern_match(player_name)

        # Check if name matches UUID string representations
        matches_uuid_string = self._check_uuid_string_matches(player_name, player_id_str, player_id_uuid)

        # If either check fails, log and return False
        if is_uuid_pattern or matches_uuid_string:
            uuid_str = str(player_id_uuid)
            is_critical = player_name == player_id_str or uuid_str == player_name
            self._log_uuid_validation_failure(
                player_name, player_id_str, player_id_uuid, player, is_uuid_pattern, is_critical
            )
            return False

        return True

    def extract_and_validate_player_name(
        self, player: Any, player_id_str: str, player_id_uuid: uuid.UUID
    ) -> str | None:
        """
        Extract and validate player name from player object.

        CRITICAL: NEVER use UUID as fallback for player name - security issue.

        Args:
            player: The player object
            player_id_str: The player's ID as string
            player_id_uuid: The player's UUID

        Returns:
            Valid player name string or None if invalid
        """
        # Extract initial player name
        player_name = self._extract_initial_player_name(player)

        # Try fallback sources if initial name is invalid
        player_name = self._try_fallback_name_sources(player, player_name)

        # Perform basic validation
        player_name = self._validate_name_basic(player_name, player_id_str, player_id_uuid, player)
        if not player_name:
            return None

        # Validate name is not a UUID
        if not self._validate_name_not_uuid(player_name, player_id_str, player_id_uuid, player):
            return None

        return player_name

    def extract_player_name(self, player: Any, player_id_uuid: uuid.UUID) -> str:
        """
        Extract player name from player object, with fallback to User object.

        CRITICAL: NEVER use UUID as fallback for player name - security issue.

        Args:
            player: The player object
            player_id_uuid: The player's UUID for logging

        Returns:
            Player name string (never a UUID)
        """
        # Try to get name from player object
        player_name = getattr(player, "name", None)
        if self._is_valid_name(player_name):
            # Type narrowing: _is_valid_name returns True only for non-empty strings
            assert isinstance(player_name, str), "player_name must be str if _is_valid_name returns True"
            return player_name

        # Try to get name from related User object
        if hasattr(player, "user"):
            try:
                user = getattr(player, "user", None)
                if user:
                    player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                    if self._is_valid_name(player_name):
                        # Type narrowing: _is_valid_name returns True only for non-empty strings
                        assert isinstance(player_name, str), "player_name must be str if _is_valid_name returns True"
                        return player_name
            except (AttributeError, TypeError) as e:
                self._logger.debug("Error accessing user relationship for player name", error=str(e))

        # If still no name, use placeholder (NEVER use UUID)
        self._logger.warning(
            "Player name not found, using placeholder",
            player_id=player_id_uuid,
            has_name_attr=hasattr(player, "name"),
            name_value=getattr(player, "name", "NOT_FOUND"),
        )
        return "Unknown Player"

    def validate_player_name_not_uuid(self, player_name: str, player_id_uuid: uuid.UUID, player: Any) -> str:
        """
        Validate that player name is not a UUID string and replace if necessary.

        Args:
            player_name: The player name to validate
            player_id_uuid: The player's UUID for logging
            player: The player object for logging

        Returns:
            Validated player name (never a UUID)
        """
        if isinstance(player_name, str) and self._is_uuid_string(player_name):
            self._logger.error(
                "CRITICAL: Player name is a UUID string, this should never happen",
                player_id=player_id_uuid,
                player_name=player_name,
                player_name_from_db=getattr(player, "name", "NOT_FOUND"),
            )
            return "Unknown Player"
        return player_name

    def is_valid_name_for_occupant(self, name: Any) -> bool:
        """
        Check if a name is valid for use as an occupant name.

        Args:
            name: The name to validate

        Returns:
            True if name is valid (non-empty string, not UUID), False otherwise
        """
        return name and isinstance(name, str) and not self._is_uuid_string(name)
