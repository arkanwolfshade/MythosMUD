"""
Player GUID Formatter for MythosMUD logging system.

This module provides a custom logging formatter that automatically converts
player GUIDs to display both player name and GUID in the format "<name>: <GUID>".
As noted in the Pnakotic Manuscripts, proper identification of entities is
crucial for understanding the flow of events through our eldritch systems.
"""

import logging
import re
from typing import Any

from .enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerGuidFormatter(logging.Formatter):
    """
    Custom formatter that converts player GUIDs to "<name>: <GUID>" format.

    This formatter enhances log readability by automatically detecting UUID-format
    player GUIDs in log messages and converting them to a more human-readable
    format that includes both the player name and the GUID.

    As noted in the Pnakotic Manuscripts, proper identification of entities
    is crucial for understanding the flow of events through our eldritch systems.
    """

    def __init__(self, player_service: Any, *args, **kwargs):
        """
        Initialize the PlayerGuidFormatter.

        Args:
            player_service: Service for accessing player data (PlayerService or PersistenceLayer)
            *args: Arguments passed to parent logging.Formatter
            **kwargs: Keyword arguments passed to parent logging.Formatter
        """
        super().__init__(*args, **kwargs)
        self.player_service = player_service

        # Compile UUID pattern for efficient matching
        # Matches standard UUID format: 8-4-4-4-12 hexadecimal digits
        # Uses negative lookbehind/lookahead to ensure we match complete UUIDs only
        self.uuid_pattern = re.compile(
            r"(?<![0-9a-f-])[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?![0-9a-f-])", re.IGNORECASE
        )

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record with enhanced player GUID display.

        Args:
            record: The log record to format

        Returns:
            Formatted log message with enhanced player GUIDs
        """
        # Get the original formatted message
        message = super().format(record)

        # Convert player GUIDs to enhanced format
        enhanced_message = self._convert_player_guids(message)

        return enhanced_message

    def _convert_player_guids(self, message: str) -> str:
        """
        Convert player GUIDs in message to enhanced format.

        Args:
            message: The log message to process

        Returns:
            Message with player GUIDs converted to "<name>: <GUID>" format
        """
        # Handle None or non-string input gracefully
        if message is None:
            return ""
        if not isinstance(message, str):
            return str(message)

        def replace_guid(match: re.Match) -> str:
            """Replace a single GUID with enhanced format."""
            guid = match.group(0)

            # Only process GUIDs that are likely to be player IDs
            if not self._is_likely_player_id(guid, message):
                return guid  # Return original GUID without processing

            player_name = self._get_player_name(guid)

            if player_name:
                return f"<{player_name}>: {guid}"
            else:
                # Log the lookup failure and return fallback format
                self._log_lookup_failure(guid)
                return f"<UNKNOWN>: {guid}"

        # Replace all UUID patterns in the message
        return self.uuid_pattern.sub(replace_guid, message)

    def _is_likely_player_id(self, guid: str, message: str) -> bool:
        """
        Determine if a GUID is likely to be a player ID based on context.

        Args:
            guid: The GUID to check
            message: The full log message for context

        Returns:
            True if the GUID is likely to be a player ID, False otherwise
        """
        # Skip GUIDs that are clearly not player IDs based on context
        # These are high-priority contexts that should override player contexts
        non_player_contexts = [
            "dead websocket",
            "closing websocket",
            "websocket connection",
            "connection manager",
            "realtime",
            "event",
            "broadcast",
            "user lookup",
            "user(id=",
            "user_id",
            "authentication",
            "auth.endpoints",
            "login",
            "logout",
            "message delivery status",
            "websocket",
            "connection",
            "session",
            "sse",
            "ws",
            "connection_id",
            "session_id",
            "websocket_id",
        ]

        message_lower = message.lower()

        # Special case: "Message delivery status for player" should be processed
        if "message delivery status for player" in message_lower:
            return True

        # Check for non-player contexts first (higher priority)
        for context in non_player_contexts:
            if context in message_lower:
                return False

        # Then check for player contexts (lower priority)
        player_contexts = [
            "player_id",
            "player moved",
            "player entered",
            "player left",
            "player joined",
            "player disconnected",
            "character",
            "avatar",
            "game state",
            "room occupants",
            "player service",
            "movement",
            "for player",
            "player:",
        ]

        for context in player_contexts:
            if context in message_lower:
                return True

        # Default to True for unknown contexts (conservative approach)
        # This ensures we don't miss legitimate player IDs
        return True

    def _get_player_name(self, guid: str) -> str | None:
        """
        Get player name for GUID from in-memory data.

        Args:
            guid: The player GUID to look up

        Returns:
            Player name if found, None otherwise
        """
        try:
            # Use the persistence layer directly to avoid async/sync mismatch
            # This is the primary method for player lookup in the formatter
            if hasattr(self.player_service, "persistence") and hasattr(self.player_service.persistence, "get_player"):
                player = self.player_service.persistence.get_player(guid)
                if player and hasattr(player, "name"):
                    return player.name
                # If persistence layer returns None, return None (no fallback)
                return None

            # If persistence layer is not available, return None
            # This ensures we don't fall back to async methods that cause issues
            return None

        except (AttributeError, KeyError, TypeError) as e:
            logger.error("Error during player lookup", error=str(e), error_type=type(e).__name__)
            # If any exception occurs during lookup, return None
            # This ensures logging continues even if player lookup fails
            return None

    def _log_lookup_failure(self, guid: str) -> None:
        """
        Log GUID lookup failure to errors.log.

        Args:
            guid: The GUID that failed to resolve
        """
        try:
            # Write directly to stderr to completely bypass the logging system
            # This prevents any formatter processing and infinite loops
            import sys
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"{timestamp} - errors - WARNING - Failed to resolve player name for GUID: {guid}\n"

            # Write directly to stderr without going through any logging system
            sys.stderr.write(error_message)
            sys.stderr.flush()

        except (OSError, UnicodeEncodeError):
            # If error logging itself fails, silently continue
            # This prevents infinite loops or system crashes
            pass
