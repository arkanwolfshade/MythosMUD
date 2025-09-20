"""
Chat service for MythosMUD.

This module provides chat functionality including message handling,
channel management, and real-time communication between players.
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from ..logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.rate_limiter import rate_limiter
from ..services.user_manager import user_manager

# NATS service import moved to constructor to avoid circular dependency issues

logger = get_logger("communications.chat_service")


class ChatMessage:
    """Represents a chat message with metadata."""

    def __init__(
        self,
        sender_id: str,
        sender_name: str,
        channel: str,
        content: str,
        target_id: str = None,
        target_name: str = None,
    ):
        self.id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.channel = channel
        self.content = content
        self.target_id = target_id
        self.target_name = target_name
        self.timestamp = datetime.now(UTC)

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for serialization."""
        result = {
            "id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }

        # Add target information for whisper messages
        if self.target_id:
            result["target_id"] = self.target_id
        if self.target_name:
            result["target_name"] = self.target_name

        return result

    def log_message(self):
        """Log this chat message to the communications log."""
        log_data = {
            "message_id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }

        # Add target information for whisper messages
        if self.target_id:
            log_data["target_id"] = self.target_id
        if self.target_name:
            log_data["target_name"] = self.target_name

        logger.info("CHAT MESSAGE", **log_data)


class ChatService:
    """
    Chat service for handling real-time communication between players.

    This service manages chat messages, channels, and player communication
    using NATS for real-time message distribution. NATS is mandatory for
    all chat functionality - no fallback to WebSocket broadcasting is provided.
    """

    def __init__(self, persistence, room_service, player_service, nats_service=None, user_manager_instance=None):
        """
        Initialize chat service.

        Args:
            persistence: Database persistence layer
            room_service: Room management service
            player_service: Player management service
            nats_service: NATS service instance (optional, defaults to global instance)
            user_manager_instance: Optional user manager instance (defaults to global instance)
        """
        self.persistence = persistence
        self.room_service = room_service
        self.player_service = player_service

        # In-memory storage for recent messages (last 100 per room)
        self._room_messages: dict[str, list[ChatMessage]] = {}

        # Message limits
        self._max_messages_per_room = 100

        # Last whisper tracking for reply functionality
        self._last_whisper_senders: dict[str, str] = {}  # player_name -> last_sender_name

        # NATS service for real-time messaging (use provided instance or fall back to global)
        from ..services.nats_service import nats_service as global_nats_service

        self.nats_service = nats_service or global_nats_service

        # Chat logger for AI processing and log shipping
        self.chat_logger = chat_logger

        # Rate limiter for message throttling
        self.rate_limiter = rate_limiter

        # User manager for muting and permissions
        self.user_manager = user_manager_instance or user_manager

        logger.info("ChatService initialized with NATS integration and AI-ready logging")

    async def send_say_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a say message to players in the same room.

        This method publishes the message to NATS for real-time distribution
        to all players in the room. NATS is mandatory for this functionality.

        Args:
            player_id: ID of the player sending the message
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: send_say_message called ===", player_id=player_id, message=message)
        logger.debug("Processing say message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for chat message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

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

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in say channel (synchronous for MVP)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===", player_id=player_id)
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===", player_id=player_id)
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===", player_id=player_id)
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="say", content=message.strip()
        )

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

        logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===", message_id=chat_message.id)

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
        logger.debug("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
        logger.debug(f"=== CHAT SERVICE DEBUG: NATS service object: {self.nats_service} ===")
        logger.debug(f"=== CHAT SERVICE DEBUG: NATS service type: {type(self.nats_service)} ===")
        if self.nats_service:
            logger.debug(f"=== CHAT SERVICE DEBUG: NATS service is_connected(): {self.nats_service.is_connected()} ===")
        else:
            logger.error("=== CHAT SERVICE DEBUG: NATS service is None ===")

        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def send_local_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a local message to players in the same sub-zone.

        This method publishes the message to NATS for real-time distribution
        to all players in the same sub-zone. NATS is mandatory for this functionality.

        Args:
            player_id: ID of the player sending the message
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: send_local_message called ===", player_id=player_id, message=message)
        logger.debug("Processing local message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for local message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing message
        if not self.rate_limiter.check_rate_limit(player_id, "local", player.name):
            logger.warning("Rate limit exceeded for local message", player_id=player_id, player_name=player.name)
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

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in local channel
        if self.user_manager.is_channel_muted(player_id, "local"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===", player_id=player_id)
            return {"success": False, "error": "You are muted in the local channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===", player_id=player_id)
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="local"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===", player_id=player_id)
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="local", content=message.strip()
        )

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
        self.rate_limiter.record_message(player_id, "local", player.name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===", message_id=chat_message.id)

        # Store message in room history
        if room_id not in self._room_messages:
            self._room_messages[room_id] = []

        self._room_messages[room_id].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages[room_id]) > self._max_messages_per_room:
            self._room_messages[room_id] = self._room_messages[room_id][-self._max_messages_per_room :]

        logger.info(
            "Local message created successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def send_global_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a global message to all players.

        This method publishes the global message to NATS for real-time distribution
        to all players. Global messages require level 1+ and are subject to rate limiting.

        Args:
            player_id: ID of the player sending the global message
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: send_global_message called ===", player_id=player_id)
        logger.debug("Processing global message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 1000:  # Limit for global messages
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 1000 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for global message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Check level requirement (minimum level 1 for global chat)
        if player.level < 1:
            logger.debug("=== CHAT SERVICE DEBUG: Player level too low ===", player_id=player_id, level=player.level)
            return {"success": False, "error": "You must be level 1 or higher to use global chat"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing global message
        if not self.rate_limiter.check_rate_limit(player_id, "global", player.name):
            logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===", player_id=player_id)
            return {"success": False, "error": "Rate limit exceeded for global chat", "rate_limited": True}

        # Check if player is muted from global channel
        if self.user_manager.is_channel_muted(player_id, "global"):
            logger.debug("=== CHAT SERVICE DEBUG: Player muted from global channel ===", player_id=player_id)
            return {"success": False, "error": "You are muted from global chat"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===", player_id=player_id)
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="global"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===", player_id=player_id)
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="global", content=message.strip()
        )

        # Log the chat message for AI processing
        self.chat_logger.log_chat_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "content": chat_message.content,
                "room_id": None,  # Global messages don't have a specific room
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Log to global channel specific log file
        self.chat_logger.log_global_channel_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "content": chat_message.content,
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Record message for rate limiting
        self.rate_limiter.record_message(player_id, "global", player.name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.debug("=== CHAT SERVICE DEBUG: Global chat message created ===", message_id=chat_message.id)

        # Store message in global history
        if "global" not in self._room_messages:
            self._room_messages["global"] = []

        self._room_messages["global"].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages["global"]) > self._max_messages_per_room:
            self._room_messages["global"] = self._room_messages["global"][-self._max_messages_per_room :]

        logger.info(
            "Global message created successfully",
            player_id=player_id,
            player_name=player.name,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish global message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, None)  # Global messages don't have room_id
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: Global NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_system_message(self, player_id: str, message: str) -> dict[str, Any]:
        """
        Send a system message to all players.

        This method publishes the system message to NATS for real-time distribution
        to all players. System messages require admin privileges and are subject to rate limiting.

        Args:
            player_id: ID of the player sending the system message
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: send_system_message called ===", player_id=player_id)
        logger.debug("Processing system message", player_id=player_id, message_length=len(message))

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 2000:  # Limit for system messages
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 2000 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for system message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Check admin requirement
        if not self.user_manager.is_admin(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player not admin ===", player_id=player_id)
            return {"success": False, "error": "You must be an admin to send system messages"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing system message
        if not self.rate_limiter.check_rate_limit(player_id, "system", player.name):
            logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===", player_id=player_id)
            return {"success": False, "error": "Rate limit exceeded for system messages", "rate_limited": True}

        # Note: Admins can send system messages even when globally muted
        # This ensures admins can always communicate important system information

        # Create chat message
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="system", content=message.strip()
        )

        # Log the chat message for AI processing
        self.chat_logger.log_chat_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "content": chat_message.content,
                "room_id": None,  # System messages don't have a specific room
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Log to system channel specific log file
        self.chat_logger.log_system_channel_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "content": chat_message.content,
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Record message for rate limiting
        self.rate_limiter.record_message(player_id, "system", player.name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.debug("=== CHAT SERVICE DEBUG: System chat message created ===", message_id=chat_message.id)

        # Store message in system history
        if "system" not in self._room_messages:
            self._room_messages["system"] = []

        self._room_messages["system"].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages["system"]) > self._max_messages_per_room:
            self._room_messages["system"] = self._room_messages["system"][-self._max_messages_per_room :]

        logger.info(
            "System message created successfully",
            player_id=player_id,
            player_name=player.name,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish system message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, None)  # System messages don't have room_id
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: System NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_whisper_message(self, sender_id: str, target_id: str, message: str) -> dict[str, Any]:
        """
        Send a whisper message from one player to another.

        This method publishes the whisper message to NATS for real-time distribution
        to the target player. Whisper messages are subject to rate limiting.

        Args:
            sender_id: ID of the player sending the whisper
            target_id: ID of the player receiving the whisper
            message: Message content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug(
            "=== CHAT SERVICE DEBUG: send_whisper_message called ===", sender_id=sender_id, target_id=target_id
        )
        logger.debug(
            "Processing whisper message", sender_id=sender_id, target_id=target_id, message_length=len(message)
        )

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty whisper message ===")
            return {"success": False, "error": "Message content cannot be empty"}

        # Strip whitespace
        message = message.strip()

        # Check message length
        if len(message) > 2000:
            logger.debug("=== CHAT SERVICE DEBUG: Whisper message too long ===")
            return {"success": False, "error": "Message too long (maximum 2000 characters)"}

        # Get sender player object
        sender_obj = self.player_service.get_player_by_id(sender_id)
        if not sender_obj:
            logger.debug("=== CHAT SERVICE DEBUG: Sender not found ===")
            return {"success": False, "error": "Sender not found"}

        # Get target player object
        target_obj = self.player_service.get_player_by_id(target_id)
        if not target_obj:
            logger.debug("=== CHAT SERVICE DEBUG: Target not found ===")
            return {"success": False, "error": "Target player not found"}

        # Check rate limiting
        sender_name = getattr(sender_obj, "name", "UnknownPlayer")
        if not self.rate_limiter.check_rate_limit(sender_id, "whisper", sender_name):
            logger.debug("=== CHAT SERVICE DEBUG: Whisper rate limited ===")
            return {"success": False, "error": "You are sending messages too quickly. Please wait a moment."}

        # Create chat message
        chat_message = ChatMessage(
            sender_id=str(sender_id),
            sender_name=sender_name,
            target_id=str(target_id),
            target_name=getattr(target_obj, "name", "UnknownPlayer"),
            channel="whisper",
            content=message,
        )

        # Log the whisper message for AI processing
        self.chat_logger.log_chat_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "target_id": chat_message.target_id,
                "target_name": chat_message.target_name,
                "content": chat_message.content,
                "room_id": None,  # Whisper messages don't have a specific room
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Log to whisper channel specific log file
        self.chat_logger.log_whisper_channel_message(
            {
                "message_id": chat_message.id,
                "channel": chat_message.channel,
                "sender_id": chat_message.sender_id,
                "sender_name": chat_message.sender_name,
                "target_id": chat_message.target_id,
                "target_name": chat_message.target_name,
                "content": chat_message.content,
                "filtered": False,
                "moderation_notes": None,
            }
        )

        # Record message for rate limiting
        self.rate_limiter.record_message(sender_id, "whisper", sender_name)

        # Store last whisper sender for reply functionality
        target_name = getattr(target_obj, "name", "UnknownPlayer")
        self.store_last_whisper_sender(target_name, sender_name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.debug("=== CHAT SERVICE DEBUG: Whisper chat message created ===", message_id=chat_message.id)

        # Store message in whisper history
        if "whisper" not in self._room_messages:
            self._room_messages["whisper"] = []

        self._room_messages["whisper"].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages["whisper"]) > self._max_messages_per_room:
            self._room_messages["whisper"] = self._room_messages["whisper"][-self._max_messages_per_room :]

        logger.info(
            "Whisper message created successfully",
            sender_id=sender_id,
            target_id=target_id,
            sender_name=sender_name,
            target_name=getattr(target_obj, "name", "UnknownPlayer"),
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish whisper message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, None)  # Whisper messages don't have room_id
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: Whisper NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_emote_message(self, player_id: str, action: str) -> dict[str, Any]:
        """
        Send an emote message to players in the same room.

        This method publishes the emote to NATS for real-time distribution
        to all players in the room. NATS is mandatory for this functionality.

        Args:
            player_id: ID of the player sending the emote
            action: Emote action content

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: send_emote_message called ===", player_id=player_id, action=action)
        logger.debug("Processing emote message", player_id=player_id, action_length=len(action))

        # Validate input
        if not action or not action.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty action ===")
            return {"success": False, "error": "Action cannot be empty"}

        if len(action.strip()) > 200:  # Limit for emote actions
            logger.debug("=== CHAT SERVICE DEBUG: Action too long ===")
            return {"success": False, "error": "Action too long (max 200 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for emote message", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Load player's mute data to ensure it's available for permission checks
        logger.debug(
            "=== CHAT SERVICE DEBUG: Loading sender's mute data ===",
            player_id=player_id,
            player_name=player.name,
        )
        mute_load_result = self.user_manager.load_player_mutes(player_id)
        logger.debug(
            "=== CHAT SERVICE DEBUG: Sender's mute data load result ===",
            player_id=player_id,
            player_name=player.name,
            mute_load_result=mute_load_result,
        )

        # Check rate limits before allowing emote
        if not self.rate_limiter.check_rate_limit(player_id, "emote", player.name):
            logger.warning("Rate limit exceeded for emote message", player_id=player_id, player_name=player.name)
            return {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another emote.",
                "rate_limited": True,
            }

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id)
            return {"success": False, "error": "Player not in a room"}

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in say channel (emotes use same channel as say)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===", player_id=player_id)
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===", player_id=player_id)
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===", player_id=player_id)
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message for emote
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="emote", content=action.strip()
        )

        # Log the emote message for AI processing
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
        self.rate_limiter.record_message(player_id, "emote", player.name)

        # Also log to communications log (existing behavior)
        chat_message.log_message()

        logger.debug("=== CHAT SERVICE DEBUG: Emote message created ===", message_id=chat_message.id)

        # Store message in room history
        if room_id not in self._room_messages:
            self._room_messages[room_id] = []

        self._room_messages[room_id].append(chat_message)

        # Maintain message history limit
        if len(self._room_messages[room_id]) > self._max_messages_per_room:
            self._room_messages[room_id] = self._room_messages[room_id][-self._max_messages_per_room :]

        logger.info(
            "Emote message created successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish emote message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    # In-memory storage for player poses (not persisted to database)
    _player_poses: dict[str, str] = {}

    async def set_player_pose(self, player_id: str, pose: str) -> dict[str, Any]:
        """
        Set a player's pose (temporary, in-memory only).

        Args:
            player_id: ID of the player setting the pose
            pose: Pose description

        Returns:
            Dictionary with success status and message details
        """
        logger.debug("=== CHAT SERVICE DEBUG: set_player_pose called ===", player_id=player_id, pose=pose)

        # Validate input
        if not pose or not pose.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty pose ===")
            return {"success": False, "error": "Pose cannot be empty"}

        if len(pose.strip()) > 100:  # Limit for poses
            logger.debug("=== CHAT SERVICE DEBUG: Pose too long ===")
            return {"success": False, "error": "Pose too long (max 100 characters)"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for pose", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id)
            return {"success": False, "error": "Player not in a room"}

        # Set the pose in memory
        self._player_poses[player_id] = pose.strip()

        # Create a chat message to notify room of pose change
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="pose", content=pose.strip()
        )

        logger.info(
            "Player pose set successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            pose=pose.strip(),
        )

        # Publish pose change to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish pose message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "pose": pose.strip(), "room_id": room_id}

    def get_player_pose(self, player_id: str) -> str:
        """
        Get a player's current pose.

        Args:
            player_id: ID of the player

        Returns:
            Current pose description or None if no pose set
        """
        return self._player_poses.get(player_id)

    def clear_player_pose(self, player_id: str) -> bool:
        """
        Clear a player's pose.

        Args:
            player_id: ID of the player

        Returns:
            True if pose was cleared, False if no pose was set
        """
        if player_id in self._player_poses:
            del self._player_poses[player_id]
            return True
        return False

    def get_room_poses(self, room_id: str) -> dict[str, str]:
        """
        Get all poses for players in a room.

        Args:
            room_id: ID of the room

        Returns:
            Dictionary mapping player names to their poses
        """
        poses = {}
        room_players = self.room_service.get_room_occupants(room_id)

        for player_id in room_players:
            pose = self._player_poses.get(player_id)
            if pose:
                player = self.player_service.get_player_by_id(player_id)
                if player:
                    poses[player.name] = pose

        return poses

    async def send_predefined_emote(self, player_id: str, emote_command: str) -> dict[str, Any]:
        """
        Send a predefined emote message using the EmoteService.

        This method uses predefined emote definitions to send formatted messages
        to both the player and room occupants.

        Args:
            player_id: ID of the player sending the emote
            emote_command: The emote command (e.g., 'twibble', 'dance')

        Returns:
            Dictionary with success status and message details
        """
        logger.debug(
            "=== CHAT SERVICE DEBUG: send_predefined_emote called ===", player_id=player_id, emote_command=emote_command
        )

        # Import EmoteService here to avoid circular imports
        from .emote_service import EmoteService

        # Initialize emote service
        emote_service = EmoteService()

        # Check if this is a valid emote command
        if not emote_service.is_emote_alias(emote_command):
            logger.warning("Invalid emote command", player_id=player_id, emote_command=emote_command)
            return {"success": False, "error": f"Unknown emote: {emote_command}"}

        # Get player information
        player = self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for predefined emote", player_id=player_id)
            return {"success": False, "error": "Player not found"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing emote
        if not self.rate_limiter.check_rate_limit(player_id, "emote", player.name):
            logger.warning("Rate limit exceeded for predefined emote", player_id=player_id, player_name=player.name)
            return {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another emote.",
                "rate_limited": True,
            }

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room", player_id=player_id)
            return {"success": False, "error": "Player not in a room"}

        # Check if player is muted in say channel (emotes use same channel as say)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===", player_id=player_id)
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===", player_id=player_id)
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===", player_id=player_id)
            return {"success": False, "error": "You cannot send messages at this time"}

        try:
            # Format the emote messages
            self_message, other_message = emote_service.format_emote_messages(emote_command, player.name)
        except ValueError as e:
            logger.error(
                "Failed to format emote messages", player_id=player_id, emote_command=emote_command, error=str(e)
            )
            return {"success": False, "error": str(e)}

        # Create chat message for the predefined emote
        chat_message = ChatMessage(
            sender_id=str(player_id), sender_name=player.name, channel="emote", content=other_message
        )

        # Log the emote message for AI processing
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

        logger.info(
            "Predefined emote message created successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            emote_command=emote_command,
            message_id=chat_message.id,
        )

        # Publish message to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish predefined emote message to NATS ===")
        success = await self._publish_chat_message_to_nats(chat_message, room_id)
        if not success:
            # NATS publishing failed - this should not happen as NATS is mandatory
            logger.error("NATS publishing failed - NATS is mandatory for chat functionality")
            return {"success": False, "error": "Chat system temporarily unavailable"}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {
            "success": True,
            "self_message": self_message,
            "other_message": other_message,
            "message": chat_message.to_dict(),
            "room_id": room_id,
        }

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
            logger.debug("=== CHAT SERVICE DEBUG: Checking NATS service ===")
            logger.debug(f"NATS service object: {self.nats_service}")
            logger.debug(f"NATS service type: {type(self.nats_service)}")
            if self.nats_service:
                logger.debug(f"NATS service is_connected(): {self.nats_service.is_connected()}")
            else:
                logger.debug("NATS service is None")

            if not self.nats_service or not self.nats_service.is_connected():
                logger.error("NATS service not available or not connected - NATS is mandatory for chat functionality")
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

            # Add target information for whisper messages
            if hasattr(chat_message, "target_id") and chat_message.target_id:
                message_data["target_id"] = chat_message.target_id
            if hasattr(chat_message, "target_name") and chat_message.target_name:
                message_data["target_name"] = chat_message.target_name

            # Determine NATS subject based on channel
            if chat_message.channel == "local":
                # For local channel, use sub-zone level subject
                from ..utils.room_utils import extract_subzone_from_room_id

                subzone = extract_subzone_from_room_id(room_id)
                if not subzone:
                    subzone = "unknown"
                subject = f"chat.local.subzone.{subzone}"
                logger.debug(f"=== CHAT SERVICE DEBUG: Local channel subject: {subject} ===")
            elif chat_message.channel == "global":
                # For global channel, use global subject
                subject = "chat.global"
                logger.debug(f"=== CHAT SERVICE DEBUG: Global channel subject: {subject} ===")
            elif chat_message.channel == "system":
                # For system channel, use system subject
                subject = "chat.system"
                logger.debug(f"=== CHAT SERVICE DEBUG: System channel subject: {subject} ===")
            elif chat_message.channel == "whisper":
                # For whisper channel, use whisper subject with target player
                target_id = getattr(chat_message, "target_id", None)
                if target_id:
                    subject = f"chat.whisper.{target_id}"
                else:
                    subject = "chat.whisper"
                logger.debug(f"=== CHAT SERVICE DEBUG: Whisper channel subject: {subject} ===")
            else:
                # For other channels, use room level subject
                subject = f"chat.{chat_message.channel}.{room_id}"
                logger.debug(f"=== CHAT SERVICE DEBUG: Other channel subject: {subject} ===")

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

    def mute_channel(self, player_id: str, channel: str) -> bool:
        """Mute a specific channel for a player."""
        # Get player name for logging
        player = self.player_service.get_player_by_id(player_id)
        player_name = player.name if player else player_id

        success = self.user_manager.mute_channel(player_id, player_name, channel)
        if success:
            logger.info("Player muted channel", player_id=player_id, channel=channel)
        return success

    def unmute_channel(self, player_id: str, channel: str) -> bool:
        """Unmute a specific channel for a player."""
        # Get player name for logging
        player = self.player_service.get_player_by_id(player_id)
        player_name = player.name if player else player_id

        success = self.user_manager.unmute_channel(player_id, player_name, channel)
        if success:
            logger.info("Player unmuted channel", player_id=player_id, channel=channel)
        return success

    def is_channel_muted(self, player_id: str, channel: str) -> bool:
        """Check if a channel is muted for a player."""
        return self.user_manager.is_channel_muted(player_id, channel)

    def mute_player(self, muter_id: str, target_player_name: str) -> bool:
        """Mute a specific player for another player."""
        # Get muter name for logging
        muter = self.player_service.get_player_by_id(muter_id)
        muter_name = muter.name if muter else muter_id

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        success = self.user_manager.mute_player(muter_id, muter_name, target_player.id, target_player_name)
        if success:
            logger.info("Player muted another player", muter_id=muter_id, target=target_player_name)
        return success

    def unmute_player(self, muter_id: str, target_player_name: str) -> bool:
        """Unmute a specific player for another player."""
        # Get muter name for logging
        muter = self.player_service.get_player_by_id(muter_id)
        muter_name = muter.name if muter else muter_id

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        success = self.user_manager.unmute_player(muter_id, muter_name, target_player.id, target_player_name)
        if success:
            logger.info("Player unmuted another player", muter_id=muter_id, target=target_player_name)
        return success

    def is_player_muted(self, muter_id: str, target_player_id: str) -> bool:
        """Check if a player is muted by another player."""
        return self.user_manager.is_player_muted(muter_id, target_player_id)

    def mute_global(
        self, muter_id: str, target_player_name: str, duration_minutes: int = None, reason: str = ""
    ) -> bool:
        """Apply a global mute to a player (cannot use any chat channels)."""
        # Get muter name for logging
        muter = self.player_service.get_player_by_id(muter_id)
        muter_name = muter.name if muter else muter_id

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        success = self.user_manager.mute_global(
            muter_id, muter_name, target_player.id, target_player_name, duration_minutes, reason
        )
        if success:
            logger.info(
                "Player globally muted", muter_id=muter_id, target=target_player_name, duration=duration_minutes
            )
        return success

    def unmute_global(self, unmuter_id: str, target_player_name: str) -> bool:
        """Remove a global mute from a player."""
        # Get unmuter name for logging
        unmuter = self.player_service.get_player_by_id(unmuter_id)
        unmuter_name = unmuter.name if unmuter else unmuter_id

        # Resolve target player name to ID
        target_player = self.player_service.resolve_player_name(target_player_name)
        if not target_player:
            return False

        success = self.user_manager.unmute_global(unmuter_id, unmuter_name, target_player.id, target_player_name)
        if success:
            logger.info("Player globally unmuted", unmuter_id=unmuter_id, target=target_player_name)
        return success

    def is_globally_muted(self, player_id: str) -> bool:
        """Check if a player is globally muted."""
        return self.user_manager.is_globally_muted(player_id)

    def add_admin(self, player_id: str) -> bool:
        """Add a player as an admin."""
        player = self.player_service.get_player_by_id(player_id)
        player_name = player.name if player else player_id

        self.user_manager.add_admin(player_id, player_name)
        logger.info("Player added as admin", player_id=player_id, player_name=player_name)
        return True

    def remove_admin(self, player_id: str) -> bool:
        """Remove a player's admin status."""
        player = self.player_service.get_player_by_id(player_id)
        player_name = player.name if player else player_id

        self.user_manager.remove_admin(player_id, player_name)
        logger.info("Player admin status removed", player_id=player_id, player_name=player_name)
        return True

    def is_admin(self, player_id: str) -> bool:
        """Check if a player is an admin."""
        return self.user_manager.is_admin(player_id)

    def can_send_message(self, sender_id: str, target_id: str = None, channel: str = None) -> bool:
        """Check if a player can send a message."""
        return self.user_manager.can_send_message(sender_id, target_id, channel)

    def get_player_mutes(self, player_id: str) -> dict[str, Any]:
        """Get all mutes applied by a player."""
        return self.user_manager.get_player_mutes(player_id)

    def get_user_management_stats(self) -> dict[str, Any]:
        """Get user management system statistics."""
        return self.user_manager.get_system_stats()

    def get_room_messages(self, room_id: str, limit: int = 50) -> list[dict[str, Any]]:
        """Get recent messages for a room."""
        messages = self._room_messages.get(room_id, [])
        return [msg.to_dict() for msg in messages[-limit:]]

    def get_mute_status(self, player_id: str) -> str:
        """
        Get comprehensive mute status for a player.

        Args:
            player_id: Player ID to get mute status for

        Returns:
            Formatted string with mute status information
        """
        try:
            # Get player name
            player = self.player_service.get_player_by_id(player_id)
            if not player:
                return "Player not found."

            player_name = player.name

            # Load player's mute data first
            self.user_manager.load_player_mutes(player_id)

            # Get mute information from UserManager
            mute_info = self.user_manager.get_player_mutes(player_id)

            # Check if player is admin
            is_admin = self.user_manager.is_admin(player_id)

            # Build status report
            status_lines = []
            status_lines.append(f"=== MUTE STATUS FOR {player_name.upper()} ===")

            if is_admin:
                status_lines.append("🔴 ADMIN STATUS: You are an admin (immune to all mutes)")

            status_lines.append("")

            # Personal mutes (players you have muted)
            personal_mutes = mute_info.get("player_mutes", {})
            if personal_mutes:
                status_lines.append("🔇 PLAYERS YOU HAVE MUTED:")
                for _target_id, mute_data in personal_mutes.items():
                    target_name = mute_data.get("target_name", "Unknown")
                    expires_at = mute_data.get("expires_at")
                    reason = mute_data.get("reason", "")

                    if expires_at:
                        # Calculate remaining time
                        from datetime import UTC, datetime

                        try:
                            if isinstance(expires_at, str):
                                expires_dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
                            else:
                                expires_dt = expires_at

                            now = datetime.now(UTC)
                            if expires_dt.tzinfo is None:
                                expires_dt = expires_dt.replace(tzinfo=UTC)

                            remaining = expires_dt - now
                            if remaining.total_seconds() > 0:
                                minutes_left = int(remaining.total_seconds() / 60)
                                duration_text = f" ({minutes_left} minutes remaining)"
                            else:
                                duration_text = " (EXPIRED)"
                        except Exception:
                            duration_text = ""
                    else:
                        duration_text = " (PERMANENT)"

                    reason_text = f" - {reason}" if reason else ""
                    status_lines.append(f"  • {target_name}{duration_text}{reason_text}")
            else:
                status_lines.append("🔇 PLAYERS YOU HAVE MUTED: None")

            status_lines.append("")

            # Global mutes (players you have globally muted)
            global_mutes = mute_info.get("global_mutes", {})
            if global_mutes:
                status_lines.append("🌐 PLAYERS YOU HAVE GLOBALLY MUTED:")
                for _target_id, mute_data in global_mutes.items():
                    target_name = mute_data.get("target_name", "Unknown")
                    expires_at = mute_data.get("expires_at")
                    reason = mute_data.get("reason", "")

                    if expires_at:
                        # Calculate remaining time
                        from datetime import UTC, datetime

                        try:
                            if isinstance(expires_at, str):
                                expires_dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
                            else:
                                expires_dt = expires_at

                            now = datetime.now(UTC)
                            if expires_dt.tzinfo is None:
                                expires_dt = expires_dt.replace(tzinfo=UTC)

                            remaining = expires_dt - now
                            if remaining.total_seconds() > 0:
                                minutes_left = int(remaining.total_seconds() / 60)
                                duration_text = f" ({minutes_left} minutes remaining)"
                            else:
                                duration_text = " (EXPIRED)"
                        except Exception:
                            duration_text = ""
                    else:
                        duration_text = " (PERMANENT)"

                    reason_text = f" - {reason}" if reason else ""
                    status_lines.append(f"  • {target_name}{duration_text}{reason_text}")
            else:
                status_lines.append("🌐 PLAYERS YOU HAVE GLOBALLY MUTED: None")

            status_lines.append("")

            # Note: We do not show if you are muted by others to prevent retaliation
            # This information is kept private for the protection of players who mute others

            return "\n".join(status_lines)

        except Exception as e:
            logger.error("Error getting mute status", error=str(e), player_id=player_id)
            return "Error retrieving mute status."

    def store_last_whisper_sender(self, receiver_name: str, sender_name: str) -> None:
        """
        Store the last whisper sender for a player to enable reply functionality.

        Args:
            receiver_name: Name of the player who received the whisper
            sender_name: Name of the player who sent the whisper
        """
        self._last_whisper_senders[receiver_name] = sender_name
        logger.debug("Stored last whisper sender", receiver=receiver_name, sender=sender_name)

    def get_last_whisper_sender(self, player_name: str) -> str | None:
        """
        Get the last whisper sender for a player.

        Args:
            player_name: Name of the player

        Returns:
            Name of the last whisper sender, or None if no whisper received
        """
        sender = self._last_whisper_senders.get(player_name)
        logger.debug("Retrieved last whisper sender", player=player_name, sender=sender)
        return sender

    def clear_last_whisper_sender(self, player_name: str) -> None:
        """
        Clear the last whisper sender for a player.

        Args:
            player_name: Name of the player
        """
        if player_name in self._last_whisper_senders:
            del self._last_whisper_senders[player_name]
            logger.debug("Cleared last whisper sender", player=player_name)
