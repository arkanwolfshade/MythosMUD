"""
Minimal Chat Service for Tracer Bullet Implementation.

This module provides basic chat functionality for the say channel MVP,
implementing room-based message delivery without Redis initially.
"""

from datetime import datetime
from typing import Any
from uuid import uuid4

from ..logging_config import get_logger

logger = get_logger(__name__)


class ChatMessage:
    """Represents a chat message in the system."""

    def __init__(self, sender_id: str, sender_name: str, channel: str, content: str):
        self.id = str(uuid4())
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.channel = channel
        self.content = content
        self.timestamp = datetime.now()
        self.filtered = False
        self.moderation_notes: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for serialization."""
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "filtered": self.filtered,
            "moderation_notes": self.moderation_notes,
        }


class ChatService:
    """
    Minimal Chat Service for room-based messaging.

    This is the tracer bullet implementation focusing on the say channel.
    Uses in-memory storage initially, with Redis integration planned for Phase 2.
    """

    def __init__(self, persistence, room_service, player_service):
        """
        Initialize the chat service.

        Args:
            persistence: The persistence layer for player/room data
            room_service: The room service for room operations
            player_service: The player service for player operations
        """
        self.persistence = persistence
        self.room_service = room_service
        self.player_service = player_service

        # In-memory storage for MVP (will be replaced with Redis in Phase 2)
        self._room_messages: dict[str, list[ChatMessage]] = {}  # room_id -> messages
        self._muted_channels: dict[str, set[str]] = {}  # player_id -> set of muted channels
        self._muted_players: dict[str, set[str]] = {}  # muter_id -> set of muted player_ids

        # Message history limit per room (for MVP)
        self._max_messages_per_room = 100

        logger.info("Chat service initialized for tracer bullet implementation")

    def send_say_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a say message to players in the same room.

        Args:
            player_id: The ID of the player sending the message
            message: The message content

        Returns:
            Dict containing success status and any error messages
        """
        logger.debug("Processing say message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = self.persistence.get_player(player_id)
        if not player:
            logger.warning("Say message failed - player not found", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Say message failed - player has no room", player_id=player_id)
            return {"success": False, "error": "You are not in a room"}

        # Check if player is muted in say channel (synchronous for MVP)
        if self._muted_channels.get(player_id, {}).get("say", False):
            return {"success": False, "error": "You are muted in the say channel"}

        # Create chat message
        chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="say", content=message.strip())

        # Store message in room history
        if room_id not in self._room_messages:
            self._room_messages[room_id] = []

        self._room_messages[room_id].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages[room_id]) > self._max_messages_per_room:
            self._room_messages[room_id] = self._room_messages[room_id][-self._max_messages_per_room :]

        logger.info(
            "Say message sent successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )

        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def get_room_messages(self, room_id: str, limit: int = 50) -> list[dict[str, Any]]:
        """
        Get recent messages for a room.

        Args:
            room_id: The room ID
            limit: Maximum number of messages to return

        Returns:
            List of message dictionaries
        """
        if room_id not in self._room_messages:
            return []

        messages = self._room_messages[room_id][-limit:]
        return [msg.to_dict() for msg in messages]

    async def get_room_participants(self, room_id: str) -> list[dict[str, Any]]:
        """
        Get list of players currently in a room.

        Args:
            room_id: The room ID

        Returns:
            List of player information dictionaries
        """
        room = self.room_service.get_room(room_id)
        if not room:
            return []

        participants = []
        for player_id in room.get("_players", []):
            player = self.persistence.get_player(player_id)
            if player:
                participants.append({"id": player_id, "name": player.name, "level": player.level})

        return participants

    async def mute_channel(self, player_id: str, channel: str) -> bool:
        """
        Mute a channel for a player.

        Args:
            player_id: The player ID
            channel: The channel to mute

        Returns:
            True if successful, False otherwise
        """
        if player_id not in self._muted_channels:
            self._muted_channels[player_id] = set()

        self._muted_channels[player_id].add(channel)
        logger.info("Channel muted", player_id=player_id, channel=channel)
        return True

    async def unmute_channel(self, player_id: str, channel: str) -> bool:
        """
        Unmute a channel for a player.

        Args:
            player_id: The player ID
            channel: The channel to unmute

        Returns:
            True if successful, False otherwise
        """
        if player_id in self._muted_channels:
            self._muted_channels[player_id].discard(channel)
            logger.info("Channel unmuted", player_id=player_id, channel=channel)
        return True

    async def is_channel_muted(self, player_id: str, channel: str) -> bool:
        """
        Check if a channel is muted for a player.

        Args:
            player_id: The player ID
            channel: The channel to check

        Returns:
            True if muted, False otherwise
        """
        return player_id in self._muted_channels and channel in self._muted_channels[player_id]

    async def mute_player(self, muter_id: str, target_id: str) -> bool:
        """
        Mute a player for another player.

        Args:
            muter_id: The player doing the muting
            target_id: The player being muted

        Returns:
            True if successful, False otherwise
        """
        # Check if target is an admin (basic protection for MVP)
        target_player = self.persistence.get_player(target_id)
        if target_player and hasattr(target_player, "is_admin") and target_player.is_admin:
            logger.warning("Attempted to mute admin player", muter_id=muter_id, target_id=target_id)
            return False

        if muter_id not in self._muted_players:
            self._muted_players[muter_id] = set()

        self._muted_players[muter_id].add(target_id)
        logger.info("Player muted", muter_id=muter_id, target_id=target_id)
        return True

    async def unmute_player(self, unmuter_id: str, target_id: str) -> bool:
        """
        Unmute a player for another player.

        Args:
            unmuter_id: The player doing the unmuting
            target_id: The player being unmuted

        Returns:
            True if successful, False otherwise
        """
        if unmuter_id in self._muted_players:
            self._muted_players[unmuter_id].discard(target_id)
            logger.info("Player unmuted", unmuter_id=unmuter_id, target_id=target_id)
        return True

    async def is_player_muted(self, player_id: str, by_player_id: str) -> bool:
        """
        Check if a player is muted by another player.

        Args:
            player_id: The player to check
            by_player_id: The player who might have muted them

        Returns:
            True if muted, False otherwise
        """
        return by_player_id in self._muted_players and player_id in self._muted_players[by_player_id]

    def get_muted_channels(self, player_id: str) -> list[str]:
        """
        Get list of channels muted by a player.

        Args:
            player_id: The player ID

        Returns:
            List of muted channel names
        """
        return list(self._muted_channels.get(player_id, set()))

    def get_muted_players(self, player_id: str) -> list[str]:
        """
        Get list of players muted by a player.

        Args:
            player_id: The player ID

        Returns:
            List of muted player IDs
        """
        return list(self._muted_players.get(player_id, set()))
