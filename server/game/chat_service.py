"""
Chat service for MythosMUD.

This module provides chat functionality including message handling,
channel management, and real-time communication between players.
"""

import uuid
from datetime import datetime
from typing import Any

from ..logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.nats_service import nats_service
from ..services.rate_limiter import rate_limiter

logger = get_logger("communications.chat_service")


class ChatMessage:
    """Represents a chat message with metadata."""

    def __init__(self, sender_id: str, sender_name: str, channel: str, content: str):
        self.id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.channel = channel
        self.content = content
        self.timestamp = datetime.utcnow()

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for serialization."""
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }

    def log_message(self):
        """Log this chat message to the communications log."""
        logger.info(
            "CHAT MESSAGE",
            message_id=self.id,
            sender_id=self.sender_id,
            sender_name=self.sender_name,
            channel=self.channel,
            content=self.content,
            timestamp=self.timestamp.isoformat(),
        )


class ChatService:
    """
    Chat service for handling real-time communication between players.

    This service manages chat messages, channels, and player communication
            using direct WebSocket broadcasting for real-time message distribution.
    """

    def __init__(self, persistence, room_service, player_service):
        """
        Initialize chat service.

        Args:
            persistence: Database persistence layer
            room_service: Room management service
            player_service: Player management service
        """
        self.persistence = persistence
        self.room_service = room_service
        self.player_service = player_service

        # In-memory storage for recent messages (last 100 per room)
        self._room_messages: dict[str, list[ChatMessage]] = {}
        self._muted_channels: dict[str, dict[str, bool]] = {}
        self._muted_players: dict[str, list[str]] = {}

        # Message limits
        self._max_messages_per_room = 100

        # NATS service for real-time messaging
        self.nats_service = nats_service

        # Chat logger for AI processing and log shipping
        self.chat_logger = chat_logger

        # Rate limiter for message throttling
        self.rate_limiter = rate_limiter

        logger.info("ChatService initialized with NATS integration and AI-ready logging")

    async def send_say_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a say message to players in the same room.

        This method broadcasts the message directly via WebSocket, which will then
        be broadcast to all players in the room via WebSocket.

        Args:
            player_id: ID of the player sending the message
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.info("=== CHAT SERVICE DEBUG: send_say_message called ===", player_id=player_id, message=message)
        logger.debug("Processing say message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            logger.warning("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            logger.warning("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = self.player_service.get_player(player_id)
        if not player:
            logger.warning("Player not found for chat message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Check rate limits before allowing message
        if not self.rate_limiter.check_rate_limit(player_id, "say", player.name):
            logger.warning("Rate limit exceeded for say message", player_id=player_id, player_name=player.name)
            return {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another message.",
                "rate_limited": True,
            }

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id)
            return {"success": False, "error": "Player not in a room"}

        logger.info("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in say channel (synchronous for MVP)
        if self._muted_channels.get(player_id, {}).get("say", False):
            logger.warning("=== CHAT SERVICE DEBUG: Player is muted ===", player_id=player_id)
            return {"success": False, "error": "You are muted in the say channel"}

        # Create chat message
        chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="say", content=message.strip())

        # Log the chat message for AI processing
        self.chat_logger.log_chat_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "content": chat_message.content,
                "room_id": room_id,
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Record message for rate limiting
        self.rate_limiter.record_message(player_id, "say", player.name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.info("=== CHAT SERVICE DEBUG: Chat message created ===", message_id=chat_message.id)

        # Store message in room history
        if room_id not in self._room_messages:
            self._room_messages[room_id] = []

        self._room_messages[room_id].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages[room_id]) > self._max_messages_per_room:
            self._room_messages[room_id] = self._room_messages[room_id][-self._max_messages_per_room :]

        logger.info(
            "Say message created successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.info("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # Fallback to direct WebSocket broadcasting if NATS fails
            logger.warning("NATS publishing failed, falling back to direct WebSocket broadcasting")
            await self._broadcast_chat_message_directly(chat_message, room_id)
        logger.info("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def _publish_chat_message_to_nats(self, chat_message: ChatMessage, room_id: str) -> bool:
        """
        Publish a chat message to NATS for real-time distribution.

        This method publishes the message to the appropriate NATS subject
        for distribution to all subscribers.

        Args:
            chat_message: The chat message to publish
            room_id: The room ID for the message

        Returns:
            True if published successfully, False otherwise
        """
        try:
            # Check if NATS service is available and connected
            if not self.nats_service or not self.nats_service.is_connected():
                logger.warning("NATS service not available or not connected")
                return False

            # Create message data for NATS
            message_data = {
                "message_id": chat_message.id,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "channel": chat_message.channel,
                "content": chat_message.content,
                "timestamp": chat_message.timestamp.isoformat(),
                "room_id": room_id,
            }

            # Determine NATS subject based on channel
            subject = f"chat.{chat_message.channel}.{room_id}"

            # Publish to NATS
            success = await self.nats_service.publish(subject, message_data)
            if success:
                logger.info(
                    "Chat message published to NATS successfully",
                    message_id=chat_message.id,
                    subject=subject,
                    sender_id=chat_message.sender_id,
                    room_id=room_id,
                )
            else:
                logger.error(
                    "Failed to publish chat message to NATS",
                    message_id=chat_message.id,
                    subject=subject,
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing chat message to NATS",
                error=str(e),
                message_id=chat_message.id,
                room_id=room_id,
            )
            return False

    async def _broadcast_chat_message_directly(self, chat_message: ChatMessage, room_id: str):
        """
        Broadcast a chat message directly to all players in the room via WebSocket.

        This method replaces the Redis-based broadcasting with direct WebSocket
        broadcasting for immediate message delivery.

        Args:
            chat_message: The chat message to broadcast
            room_id: The room ID for the message
        """
        try:
            # Import required modules for direct broadcasting
            from ..realtime.connection_manager import connection_manager
            from ..realtime.envelope import build_event

            # Create WebSocket event for broadcasting
            chat_event = build_event(
                "chat_message",
                {
                    "sender_id": str(chat_message.sender_id),
                    "player_name": chat_message.sender_name,
                    "channel": chat_message.channel,
                    "message": chat_message.content,
                    "message_id": chat_message.id,
                    "timestamp": chat_message.timestamp.isoformat(),
                },
                player_id=str(chat_message.sender_id),
            )

            # Broadcast directly to room
            await connection_manager.broadcast_to_room(room_id, chat_event, exclude_player=chat_message.sender_id)

            logger.info(
                "Chat message broadcasted directly to room",
                message_id=chat_message.id,
                sender_id=chat_message.sender_id,
                player_name=chat_message.sender_name,
                room_id=room_id,
            )

        except Exception as e:
            logger.error(
                "Failed to broadcast chat message directly", error=str(e), message_id=chat_message.id, room_id=room_id
            )

    def mute_channel(self, player_id: str, channel: str) -> bool:
        """Mute a specific channel for a player."""
        if player_id not in self._muted_channels:
            self._muted_channels[player_id] = {}
        self._muted_channels[player_id][channel] = True

        # Log moderation event for AI processing
        self.chat_logger.log_player_muted(
            muter_id=player_id,
            target_id=player_id,
            target_name=player_id,  # We'll get actual name if needed
            mute_type=f"channel_{channel}",
            reason="Player self-muted channel",
        )

        logger.info("Player muted channel", player_id=player_id, channel=channel)
        return True

    def unmute_channel(self, player_id: str, channel: str) -> bool:
        """Unmute a specific channel for a player."""
        if player_id in self._muted_channels and channel in self._muted_channels[player_id]:
            self._muted_channels[player_id][channel] = False

            # Log moderation event for AI processing
            self.chat_logger.log_player_unmuted(
                unmuter_id=player_id,
                target_id=player_id,
                target_name=player_id,  # We'll get actual name if needed
                mute_type=f"channel_{channel}",
            )

            logger.info("Player unmuted channel", player_id=player_id, channel=channel)
            return True
        return False

    def is_channel_muted(self, player_id: str, channel: str) -> bool:
        """Check if a channel is muted for a player."""
        return self._muted_channels.get(player_id, {}).get(channel, False)

    def mute_player(self, muter_id: str, target_player_name: str) -> bool:
        """Mute a specific player for another player."""
        if muter_id not in self._muted_players:
            self._muted_players[muter_id] = []

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        if target_player["player_id"] not in self._muted_players[muter_id]:
            self._muted_players[muter_id].append(target_player["player_id"])

            # Log moderation event for AI processing
            self.chat_logger.log_player_muted(
                muter_id=muter_id,
                target_id=target_player["player_id"],
                target_name=target_player_name,
                mute_type="player",
                reason="Player muted by another player",
            )

            logger.info("Player muted another player", muter_id=muter_id, target=target_player_name)
            return True
        return False

    def unmute_player(self, muter_id: str, target_player_name: str) -> bool:
        """Unmute a specific player for another player."""
        if muter_id not in self._muted_players:
            return False

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        if target_player["player_id"] in self._muted_players[muter_id]:
            self._muted_players[muter_id].remove(target_player["player_id"])

            # Log moderation event for AI processing
            self.chat_logger.log_player_unmuted(
                unmuter_id=muter_id,
                target_id=target_player["player_id"],
                target_name=target_player_name,
                mute_type="player",
            )

            logger.info("Player unmuted another player", muter_id=muter_id, target=target_player_name)
            return True
        return False

    def is_player_muted(self, muter_id: str, target_player_id: str) -> bool:
        """Check if a player is muted by another player."""
        return target_player_id in self._muted_players.get(muter_id, [])

    def get_room_messages(self, room_id: str, limit: int = 50) -> list[dict[str, Any]]:
        """Get recent messages for a room."""
        messages = self._room_messages.get(room_id, [])
        return [msg.to_dict() for msg in messages[-limit:]]
