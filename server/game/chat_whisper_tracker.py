"""
Chat whisper tracking utilities.

This module provides whisper tracking functionality to enable
reply functionality by tracking the last whisper sender for each player.
"""

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.chat_whisper_tracker")


class ChatWhisperTracker:
    """Tracks last whisper senders for reply functionality."""

    def __init__(self) -> None:
        """Initialize the whisper tracker."""
        self._last_senders: dict[str, str] = {}  # player_name -> last_sender_name

    def store_sender(self, receiver_name: str, sender_name: str) -> None:
        """
        Store the last whisper sender for a player.

        Args:
            receiver_name: Name of the player who received the whisper
            sender_name: Name of the player who sent the whisper
        """
        self._last_senders[receiver_name] = sender_name
        logger.debug("Stored last whisper sender", receiver=receiver_name, sender=sender_name)

    def get_sender(self, player_name: str) -> str | None:
        """
        Get the last whisper sender for a player.

        Args:
            player_name: Name of the player

        Returns:
            Name of the last whisper sender, or None if no whisper received
        """
        sender = self._last_senders.get(player_name)
        logger.debug("Retrieved last whisper sender", player=player_name, sender=sender)
        return sender

    def clear_sender(self, player_name: str) -> None:
        """
        Clear the last whisper sender for a player.

        Args:
            player_name: Name of the player
        """
        if player_name in self._last_senders:
            del self._last_senders[player_name]
            logger.debug("Cleared last whisper sender", player=player_name)

    def get_all_trackings(self) -> dict[str, str]:
        """
        Get all whisper trackings (for testing/debugging).

        Returns:
            Dictionary mapping receiver names to sender names
        """
        return self._last_senders.copy()
