"""
Chat service for MythosMUD.

This module provides chat functionality including message handling,
channel management, and real-time communication between players.
"""

import uuid
from typing import TYPE_CHECKING, Any, cast

from ..services.chat_logger import chat_logger
from ..services.rate_limiter import rate_limiter
from ..services.user_manager import user_manager
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_message import ChatMessage
from .chat_moderation import ChatModeration

if TYPE_CHECKING:
    from .chat_moderation import UserManagerProtocol  # noqa: F401
from .chat_nats_publisher import publish_chat_message_to_nats
from .chat_pose_manager import ChatPoseManager
from .chat_whisper_tracker import ChatWhisperTracker

# NATS service import moved to constructor to avoid circular dependency issues

logger = get_logger("communications.chat_service")


class ChatService:
    """
    Chat service for handling real-time communication between players.

    This service manages chat messages, channels, and player communication
    using NATS for real-time message distribution. NATS is mandatory for
    all chat functionality - no fallback to WebSocket broadcasting is provided.
    """

    def __init__(
        self,
        persistence: Any,
        room_service: Any,
        player_service: Any,
        nats_service: Any | None = None,
        user_manager_instance: Any | None = None,
        subject_manager: Any | None = None,
    ) -> None:
        """
        Initialize chat service.

        Args:
            persistence: Database persistence layer
            room_service: Room management service
            player_service: Player management service
            nats_service: NATS service instance (optional, defaults to global instance)
            user_manager_instance: Optional user manager instance (defaults to global instance)
            subject_manager: NATSSubjectManager instance (optional, for standardized subject patterns)
        """
        self.persistence = persistence
        self.room_service = room_service
        self.player_service = player_service

        # In-memory storage for recent messages (last 100 per room)
        self._room_messages: dict[str, list[ChatMessage]] = {}

        # Message limits
        self._max_messages_per_room = 100

        # Pose and whisper tracking managers
        self._pose_manager = ChatPoseManager()
        self._whisper_tracker = ChatWhisperTracker()

        # User manager for muting and permissions
        self.user_manager = user_manager_instance or user_manager

        # Moderation handler (must be after user_manager is set)
        # Cast to UserManagerProtocol for type checking - runtime type is compatible with protocol
        self._moderation = ChatModeration(self.player_service, cast("UserManagerProtocol", self.user_manager))

        # NATS service for real-time messaging (use provided instance or fall back to global)
        from ..services.nats_service import nats_service as global_nats_service

        self.nats_service = nats_service or global_nats_service

        # NATSSubjectManager for standardized subject patterns (optional)
        self.subject_manager = subject_manager

        # Chat logger for AI processing and log shipping
        self.chat_logger = chat_logger

        # Rate limiter for message throttling
        self.rate_limiter = rate_limiter

        logger.info("ChatService initialized with NATS integration and AI-ready logging")

    @staticmethod
    def _normalize_player_id(player_id: Any) -> str:
        """Normalize player identifiers to string form."""
        return str(player_id)

    async def send_say_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
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

        player_id = self._normalize_player_id(player_id)
        logger.debug("=== CHAT SERVICE DEBUG: send_say_message called ===", player_id=player_id, message=message)
        logger.debug("Processing say message")

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for chat message")
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
            logger.warning("Player not in a room")
            return {"success": False, "error": "Player not in a room"}

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in say channel (synchronous for MVP)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        # ChatMessage accepts UUID | str and converts internally
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

        logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===")

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
        logger.debug(
            "Chat service NATS service status",
            nats_service_object=self.nats_service,
            nats_service_type=type(self.nats_service).__name__,
            nats_connected=self.nats_service.is_connected() if self.nats_service else False,
        )

        success = await publish_chat_message_to_nats(chat_message, room_id, self.nats_service, self.subject_manager)
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                room_id=room_id,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        chat_message.echo_sent = True
        message_dict = chat_message.to_dict()

        try:
            from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
        except ImportError as import_error:  # pragma: no cover - defensive against circular import edge cases
            logger.debug(
                "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
                error=str(import_error),
                message_id=chat_message.id,
            )
        else:
            SUPPRESS_ECHO_MESSAGE_IDS.add(chat_message.id)
            logger.debug(
                "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
                message_id=chat_message.id,
                token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
            )

        return {"success": True, "message": message_dict, "room_id": room_id}

    async def send_local_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
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
        player_id = self._normalize_player_id(player_id)
        logger.debug(
            "=== CHAT SERVICE DEBUG: send_local_message called ===",
            player_id=player_id,
            message=message,
        )
        logger.debug("Processing local message")

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 500:  # Reasonable limit for MVP
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 500 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for local message")
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
            logger.warning("Player not in a room")
            return {"success": False, "error": "Player not in a room"}

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in local channel
        if self.user_manager.is_channel_muted(player_id, "local"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
            return {"success": False, "error": "You are muted in the local channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="local"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(
            sender_id=player_id, sender_name=player.name, channel="local", content=message.strip()
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

        logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===")

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
        success = await publish_chat_message_to_nats(chat_message, room_id, self.nats_service, self.subject_manager)
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                room_id=room_id,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        chat_message.echo_sent = True
        message_dict = chat_message.to_dict()
        message_dict["echo_sent"] = True
        logger.debug(
            "=== CHAT SERVICE DEBUG: Emote message response payload ===",
            payload_keys=list(message_dict.keys()),
        )
        # Register the message ID so the broadcasting layer can suppress duplicate echoes when no recipients exist.
        try:
            from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
        except ImportError as import_error:  # pragma: no cover - defensive guard for import cycles
            logger.debug(
                "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
                error=str(import_error),
                message_id=chat_message.id,
            )
        else:
            SUPPRESS_ECHO_MESSAGE_IDS.add(chat_message.id)
            logger.debug(
                "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
                message_id=chat_message.id,
                token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
            )

        return {"success": True, "message": message_dict, "room_id": room_id}

    async def send_global_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
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
        player_id = self._normalize_player_id(player_id)
        logger.debug("=== CHAT SERVICE DEBUG: send_global_message called ===", player_id=player_id, message=message)
        logger.debug("Processing global message")

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 1000:  # Limit for global messages
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 1000 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for global message")
            return {"success": False, "error": "Player not found"}

        # Check level requirement (minimum level 1 for global chat)
        if player.level < 1:
            logger.debug(
                "=== CHAT SERVICE DEBUG: Player level too low ===",
                player_id=player_id,
                level=player.level,
            )
            return {"success": False, "error": "You must be level 1 or higher to use global chat"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing global message
        if not self.rate_limiter.check_rate_limit(player_id, "global", player.name):
            logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
            return {"success": False, "error": "Rate limit exceeded for global chat", "rate_limited": True}

        # Check if player is muted from global channel
        if self.user_manager.is_channel_muted(player_id, "global"):
            logger.debug("=== CHAT SERVICE DEBUG: Player muted from global channel ===", player_id=player_id)
            return {"success": False, "error": "You are muted from global chat"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="global"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(
            sender_id=player_id, sender_name=player.name, channel="global", content=message.strip()
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

        logger.debug("=== CHAT SERVICE DEBUG: Global chat message created ===")

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
        success = await publish_chat_message_to_nats(
            chat_message, None, self.nats_service, self.subject_manager
        )  # Global messages don't have room_id
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: Global NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_system_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
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
        player_id = self._normalize_player_id(player_id)
        logger.debug("=== CHAT SERVICE DEBUG: send_system_message called ===", player_id=player_id, message=message)
        logger.debug("Processing system message")

        # Validate input
        if not message or not message.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
            return {"success": False, "error": "Message cannot be empty"}

        if len(message.strip()) > 2000:  # Limit for system messages
            logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
            return {"success": False, "error": "Message too long (max 2000 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for system message")
            return {"success": False, "error": "Player not found"}

        # Check admin requirement
        if not self.user_manager.is_admin(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player not admin ===")
            return {"success": False, "error": "You must be an admin to send system messages"}

        # Load player's mute data to ensure it's available for permission checks
        self.user_manager.load_player_mutes(player_id)

        # Check rate limits before allowing system message
        if not self.rate_limiter.check_rate_limit(player_id, "system", player.name):
            logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
            return {"success": False, "error": "Rate limit exceeded for system messages", "rate_limited": True}

        # Note: Admins can send system messages even when globally muted
        # This ensures admins can always communicate important system information

        # Create chat message
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(
            sender_id=player_id, sender_name=player.name, channel="system", content=message.strip()
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

        logger.debug("=== CHAT SERVICE DEBUG: System chat message created ===")

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
        success = await publish_chat_message_to_nats(
            chat_message, None, self.nats_service, self.subject_manager
        )  # System messages don't have room_id
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: System NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_whisper_message(
        self, sender_id: uuid.UUID | str, target_id: uuid.UUID | str, message: str
    ) -> dict[str, Any]:
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
        sender_id = self._normalize_player_id(sender_id)
        target_id = self._normalize_player_id(target_id)

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
        sender_obj = await self.player_service.get_player_by_id(sender_id)
        if not sender_obj:
            logger.debug("=== CHAT SERVICE DEBUG: Sender not found ===")
            return {"success": False, "error": "Sender not found"}

        # Get target player object
        target_obj = await self.player_service.get_player_by_id(target_id)
        if not target_obj:
            logger.debug("=== CHAT SERVICE DEBUG: Target not found ===")
            return {"success": False, "error": "You whisper into the aether."}

        # Check rate limiting
        sender_name = getattr(sender_obj, "name", "UnknownPlayer")
        if not self.rate_limiter.check_rate_limit(sender_id, "whisper", sender_name):
            logger.debug("=== CHAT SERVICE DEBUG: Whisper rate limited ===")
            return {"success": False, "error": "You are sending messages too quickly. Please wait a moment."}

        # Create chat message
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(
            sender_id=sender_id,
            sender_name=sender_name,
            target_id=target_id,
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
        self._whisper_tracker.store_sender(target_name, sender_name)

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
        success = await publish_chat_message_to_nats(
            chat_message, None, self.nats_service, self.subject_manager
        )  # Whisper messages don't have room_id
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                sender_id=sender_id,
                sender_name=sender_name,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: Whisper NATS publishing completed ===")

        return {"success": True, "message": chat_message.to_dict()}

    async def send_emote_message(self, player_id: uuid.UUID | str, action: str) -> dict[str, Any]:
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
        player_id = self._normalize_player_id(player_id)
        logger.debug("=== CHAT SERVICE DEBUG: send_emote_message called ===", player_id=player_id, action=action)
        logger.debug("Processing emote message")

        # Validate input
        if not action or not action.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty action ===")
            return {"success": False, "error": "Action cannot be empty"}

        if len(action.strip()) > 200:  # Limit for emote actions
            logger.debug("=== CHAT SERVICE DEBUG: Action too long ===")
            return {"success": False, "error": "Action too long (max 200 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for emote message")
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
            logger.warning("Player not in a room")
            return {"success": False, "error": "Player not in a room"}

        logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

        # Check if player is muted in say channel (emotes use same channel as say)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
            return {"success": False, "error": "You cannot send messages at this time"}

        # Create chat message for emote
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(
            sender_id=player_id, sender_name=player.name, channel="emote", content=action.strip()
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
        success = await publish_chat_message_to_nats(chat_message, room_id, self.nats_service, self.subject_manager)
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                room_id=room_id,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        chat_message.echo_sent = True
        message_dict = chat_message.to_dict()

        try:
            from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
        except ImportError as import_error:  # pragma: no cover - defensive against circular import edge cases
            logger.debug(
                "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
                error=str(import_error),
                message_id=chat_message.id,
            )
        else:
            SUPPRESS_ECHO_MESSAGE_IDS.add(chat_message.id)
            logger.debug(
                "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
                message_id=chat_message.id,
                token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
            )

        return {"success": True, "message": message_dict, "room_id": room_id}

    async def set_player_pose(self, player_id: uuid.UUID | str, pose: str) -> dict[str, Any]:
        """
        Set a player's pose (temporary, in-memory only).

        Args:
            player_id: ID of the player setting the pose
            pose: Pose description

        Returns:
            Dictionary with success status and message details
        """
        player_id = self._normalize_player_id(player_id)
        logger.debug("=== CHAT SERVICE DEBUG: set_player_pose called ===", player_id=player_id, pose=pose)

        # Validate input
        if not pose or not pose.strip():
            logger.debug("=== CHAT SERVICE DEBUG: Empty pose ===")
            return {"success": False, "error": "Pose cannot be empty"}

        if len(pose.strip()) > 100:  # Limit for poses
            logger.debug("=== CHAT SERVICE DEBUG: Pose too long ===")
            return {"success": False, "error": "Pose too long (max 100 characters)"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for pose")
            return {"success": False, "error": "Player not found"}

        # Get player's current room
        room_id = player.current_room_id
        if not room_id:
            logger.warning("Player not in a room")
            return {"success": False, "error": "Player not in a room"}

        # Set the pose in memory
        self._pose_manager.set_pose(player_id, pose)

        # Create a chat message to notify room of pose change
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="pose", content=pose.strip())

        logger.info(
            "Player pose set successfully",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            pose=pose.strip(),
        )

        # Publish pose change to NATS for real-time distribution
        logger.debug("=== CHAT SERVICE DEBUG: About to publish pose message to NATS ===")
        success = await publish_chat_message_to_nats(chat_message, room_id, self.nats_service, self.subject_manager)
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                room_id=room_id,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {"success": True, "pose": pose.strip(), "room_id": room_id}

    def get_player_pose(self, player_id: uuid.UUID | str) -> str | None:
        """
        Get a player's current pose.

        Args:
            player_id: ID of the player

        Returns:
            Current pose description or None if no pose set
        """
        return self._pose_manager.get_pose(player_id)

    def clear_player_pose(self, player_id: uuid.UUID | str) -> bool:
        """
        Clear a player's pose.

        Args:
            player_id: ID of the player

        Returns:
            True if pose was cleared, False if no pose was set
        """
        return self._pose_manager.clear_pose(player_id)

    async def get_room_poses(self, room_id: str) -> dict[str, str]:
        """
        Get all poses for players in a room.

        Args:
            room_id: ID of the room

        Returns:
            Dictionary mapping player names to their poses
        """
        poses = {}
        room_players = await self.room_service.get_room_occupants(room_id)

        for player_id in room_players:
            pose = self._pose_manager.get_pose(player_id)
            if pose:
                player = await self.player_service.get_player_by_id(player_id)
                if player:
                    poses[player.name] = pose

        return poses

    async def send_predefined_emote(self, player_id: uuid.UUID | str, emote_command: str) -> dict[str, Any]:
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
        player_id = self._normalize_player_id(player_id)
        logger.debug(
            "=== CHAT SERVICE DEBUG: send_predefined_emote called ===", player_id=player_id, emote_command=emote_command
        )

        # Import EmoteService here to avoid circular imports
        from .emote_service import EmoteService

        # Initialize emote service
        emote_service = EmoteService()

        # Check if this is a valid emote command
        if not emote_service.is_emote_alias(emote_command):
            logger.warning("Invalid emote command")
            return {"success": False, "error": f"Unknown emote: {emote_command}"}

        # Get player information
        player = await self.player_service.get_player_by_id(player_id)
        if not player:
            logger.warning("Player not found for predefined emote")
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
            logger.warning("Player not in a room")
            return {"success": False, "error": "Player not in a room"}

        # Check if player is muted in say channel (emotes use same channel as say)
        if self.user_manager.is_channel_muted(player_id, "say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
            return {"success": False, "error": "You are muted in the say channel"}

        # Check if player is globally muted
        if self.user_manager.is_globally_muted(player_id):
            logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
            return {"success": False, "error": "You are globally muted and cannot send messages"}

        # Check if player can send messages (admin check, etc.)
        if not self.user_manager.can_send_message(player_id, channel="say"):
            logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
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
        # ChatMessage accepts UUID | str and converts internally
        chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="emote", content=other_message)

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
        success = await publish_chat_message_to_nats(chat_message, room_id, self.nats_service, self.subject_manager)
        if not success:
            # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
            logger.error(
                "NATS publishing failed - NATS is mandatory for chat functionality",
                player_id=player_id,
                player_name=player.name,
                room_id=room_id,
                message_id=chat_message.id,
            )
            return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
        logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

        return {
            "success": True,
            "self_message": self_message,
            "other_message": other_message,
            "message": chat_message.to_dict(),
            "room_id": room_id,
        }

    async def mute_channel(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Mute a specific channel for a player."""
        return await self._moderation.mute_channel(player_id, channel)

    async def unmute_channel(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Unmute a specific channel for a player."""
        return await self._moderation.unmute_channel(player_id, channel)

    def is_channel_muted(self, player_id: uuid.UUID | str, channel: str) -> bool:
        """Check if a channel is muted for a player."""
        return self._moderation.is_channel_muted(player_id, channel)

    async def mute_player(self, muter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Mute a specific player for another player."""
        return await self._moderation.mute_player(muter_id, target_player_name)

    async def unmute_player(self, muter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Unmute a specific player for another player."""
        return await self._moderation.unmute_player(muter_id, target_player_name)

    def is_player_muted(self, muter_id: uuid.UUID | str, target_player_id: uuid.UUID | str) -> bool:
        """Check if a player is muted by another player."""
        return self._moderation.is_player_muted(muter_id, target_player_id)

    async def mute_global(
        self, muter_id: uuid.UUID | str, target_player_name: str, duration_minutes: int | None = None, reason: str = ""
    ) -> bool:
        """Apply a global mute to a player (cannot use any chat channels)."""
        return await self._moderation.mute_global(muter_id, target_player_name, duration_minutes, reason)

    async def unmute_global(self, unmuter_id: uuid.UUID | str, target_player_name: str) -> bool:
        """Remove a global mute from a player."""
        return await self._moderation.unmute_global(unmuter_id, target_player_name)

    def is_globally_muted(self, player_id: uuid.UUID | str) -> bool:
        """Check if a player is globally muted."""
        return self._moderation.is_globally_muted(player_id)

    async def add_admin(self, player_id: uuid.UUID | str) -> bool:
        """Add a player as an admin."""
        return await self._moderation.add_admin(player_id)

    async def remove_admin(self, player_id: uuid.UUID | str) -> bool:
        """Remove a player's admin status."""
        return await self._moderation.remove_admin(player_id)

    def is_admin(self, player_id: uuid.UUID | str) -> bool:
        """Check if a player is an admin."""
        return self._moderation.is_admin(player_id)

    def can_send_message(self, sender_id: str, target_id: str | None = None, channel: str | None = None) -> bool:
        """Check if a player can send a message."""
        return self._moderation.can_send_message(sender_id, target_id, channel)

    def get_player_mutes(self, player_id: uuid.UUID | str) -> dict[str, Any]:
        """Get all mutes applied by a player."""
        return self._moderation.get_player_mutes(player_id)

    def get_user_management_stats(self) -> dict[str, Any]:
        """Get user management system statistics."""
        return self._moderation.get_user_management_stats()

    def get_room_messages(self, room_id: str, limit: int = 50) -> list[dict[str, Any]]:
        """Get recent messages for a room."""
        messages = self._room_messages.get(room_id, [])
        return [msg.to_dict() for msg in messages[-limit:]]

    async def get_mute_status(self, player_id: uuid.UUID | str) -> str:
        """
        Get comprehensive mute status for a player.

        Args:
            player_id: Player ID to get mute status for

        Returns:
            Formatted string with mute status information
        """
        return await self._moderation.get_mute_status(player_id)

    def store_last_whisper_sender(self, receiver_name: str, sender_name: str) -> None:
        """
        Store the last whisper sender for a player to enable reply functionality.

        Args:
            receiver_name: Name of the player who received the whisper
            sender_name: Name of the player who sent the whisper
        """
        self._whisper_tracker.store_sender(receiver_name, sender_name)

    def get_last_whisper_sender(self, player_name: str) -> str | None:
        """
        Get the last whisper sender for a player.

        Args:
            player_name: Name of the player

        Returns:
            Name of the last whisper sender, or None if no whisper received
        """
        return self._whisper_tracker.get_sender(player_name)

    def clear_last_whisper_sender(self, player_name: str) -> None:
        """
        Clear the last whisper sender for a player.

        Args:
            player_name: Name of the player
        """
        self._whisper_tracker.clear_sender(player_name)
