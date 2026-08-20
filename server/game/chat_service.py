"""
Chat service for MythosMUD.

This module provides chat functionality including message handling,
channel management, and real-time communication between players.
"""

# pylint: disable=too-many-return-statements,too-many-lines,too-many-public-methods  # Reason: Chat service methods require multiple return statements for early validation returns (permission checks, validation, error handling). Chat service requires extensive functionality for comprehensive chat system management. Chat service legitimately requires many public methods for comprehensive chat operations.

import uuid
from typing import TYPE_CHECKING, cast

from ..services.chat_logger import chat_logger
from ..services.rate_limiter import rate_limiter
from ..services.user_manager import user_manager
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_channel_message_senders import (
    ChatEmoteService,
    ChatLogger,
    ChatPlayerService,
    ChatRateLimiter,
    ChatSendServices,
    ChatUserManager,
    WhisperTracker,
)
from .chat_message import ChatMessage
from .chat_message_helpers import (
    create_and_log_chat_message,
    create_and_log_say_message,
    store_message_in_room_history,
)
from .chat_message_senders import (
    send_global_message as send_global_message_helper,
)
from .chat_message_senders import (
    send_local_message as send_local_message_helper,
)
from .chat_message_senders import (
    send_party_message as send_party_message_helper,
)
from .chat_message_senders import (
    send_predefined_emote as send_predefined_emote_helper,
)
from .chat_message_senders import (
    send_system_message as send_system_message_helper,
)
from .chat_message_senders import (
    send_whisper_message as send_whisper_message_helper,
)
from .chat_moderation import ChatModeration
from .chat_nats_publisher import publish_chat_message_to_nats
from .chat_npc_system import (
    send_npc_say_to_room as send_npc_say_to_room_helper,
)
from .chat_npc_system import (
    send_personal_system_message as send_personal_system_message_helper,
)
from .chat_pose_helpers import (
    clear_player_pose,
    get_player_pose,
    get_room_poses,
    set_player_pose,
)
from .chat_pose_manager import ChatPoseManager
from .chat_validation_helpers import (
    check_channel_permissions,
    check_say_permissions,
    validate_emote_action,
    validate_say_message,
)
from .chat_whisper_tracker import ChatWhisperTracker
from .player_service import PlayerService

if TYPE_CHECKING:
    from .chat_moderation import (
        PlayerServiceProtocol,
        UserManagerProtocol,  # noqa: F401  # pylint: disable=unused-import  # Reason: Imported for type checking only
    )
# NATS service import moved to constructor to avoid circular dependency issues

logger = get_logger("communications.chat_service")

_NATS_UNAVAILABLE = "Chat system temporarily unavailable. Please try again in a moment."


def _rate_limit_result() -> dict[str, object]:
    return {
        "success": False,
        "error": "Rate limit exceeded. Please wait before sending another message.",
        "rate_limited": True,
    }


def _register_echo_suppression(message_id: str) -> None:
    # Inline import: message_filtering imports chat types and would cycle this module.
    try:
        from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
    except ImportError as import_error:  # pragma: no cover
        logger.debug(
            "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
            error=str(import_error),
            message_id=message_id,
        )
        return
    SUPPRESS_ECHO_MESSAGE_IDS.add(message_id)
    logger.debug(
        "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
        message_id=message_id,
        token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
    )


async def _publish_room_chat(
    chat_message: ChatMessage,
    room_id: str,
    nats_service: object,
    subject_manager: object,
    player_id: str,
    player_name: str,
) -> dict[str, object] | None:
    success = await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager)
    if success:
        return None
    logger.error(
        "NATS publishing failed - NATS is mandatory for chat functionality",
        player_id=player_id,
        player_name=player_name,
        room_id=room_id,
        message_id=chat_message.id,
    )
    return {"success": False, "error": _NATS_UNAVAILABLE}


class ChatService:  # pylint: disable=too-many-instance-attributes  # Reason: Chat service requires many configuration and state tracking attributes
    """
    Chat service for handling real-time communication between players.

    This service manages chat messages, channels, and player communication
    using NATS for real-time message distribution. NATS is mandatory for
    all chat functionality - no fallback to WebSocket broadcasting is provided.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Chat service initialization requires many dependencies and configuration parameters
        self,
        persistence: object,
        room_service: object,
        player_service: PlayerService,
        nats_service: object | None = None,
        user_manager_instance: object | None = None,
        subject_manager: object | None = None,
        emote_service: object | None = None,
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
            emote_service: Container-loaded EmoteService (server/container/bundles/game.py),
                          used by send_predefined_emote (#624). Optional so the 12+ existing
                          positional test constructions of ChatService are unaffected.
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
        self.user_manager = cast(ChatUserManager, user_manager_instance or user_manager)
        self._moderation = ChatModeration(
            cast("PlayerServiceProtocol", cast(object, self.player_service)),
            cast("UserManagerProtocol", cast(object, self.user_manager)),
        )

        # NATS service for real-time messaging (use provided instance or fall back to global)
        from ..services.nats_service import nats_service as global_nats_service

        self.nats_service = nats_service or global_nats_service

        # NATSSubjectManager for standardized subject patterns (optional)
        self.subject_manager = subject_manager

        # Chat logger for AI processing and log shipping
        self.chat_logger = chat_logger

        # Rate limiter for message throttling
        self.rate_limiter = rate_limiter

        # Predefined-emote lookup, container-loaded (#624)
        self.emote_service = emote_service

        logger.info("ChatService initialized with NATS integration and AI-ready logging")

    @staticmethod
    def _normalize_player_id(player_id: uuid.UUID | str) -> str:
        """Normalize player identifiers to string form."""
        return str(player_id)

    def _chat_send_services(self) -> ChatSendServices:
        return {
            "player_service": cast(ChatPlayerService, cast(object, self.player_service)),
            "user_manager": self.user_manager,
            "rate_limiter": cast(ChatRateLimiter, cast(object, self.rate_limiter)),
            "chat_logger": cast(ChatLogger, cast(object, self.chat_logger)),
            "room_messages": self._room_messages,
            "max_messages_per_room": self._max_messages_per_room,
            "nats_service": self.nats_service,
            "subject_manager": self.subject_manager,
        }

    async def send_say_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, object]:
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
        error_result = validate_say_message(message)
        if error_result:
            return error_result
        player = await self.player_service.get_player_by_id(uuid.UUID(str(player_id)))
        if not player:
            return {"success": False, "error": "Player not found"}
        self.user_manager.load_player_mutes(player_id)
        if not self.rate_limiter.check_rate_limit(player_id, "say", player.name):
            return _rate_limit_result()
        room_id = player.current_room_id
        if not room_id:
            return {"success": False, "error": "Player not in a room"}
        error_result = check_say_permissions(self.user_manager, player_id)
        if error_result:
            return error_result
        chat_message = create_and_log_say_message(player_id, player.name, message, room_id)
        self.rate_limiter.record_message(player_id, "say", player.name)
        store_message_in_room_history(self._room_messages, chat_message, room_id, self._max_messages_per_room)
        nats_error = await _publish_room_chat(
            chat_message, room_id, self.nats_service, self.subject_manager, player_id, player.name
        )
        if nats_error:
            return nats_error
        chat_message.echo_sent = True
        _register_echo_suppression(chat_message.id)
        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def send_local_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, object]:
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
        return await send_local_message_helper(
            player_id,
            message,
            cast(ChatPlayerService, cast(object, self.player_service)),
            self.user_manager,
            cast(ChatRateLimiter, cast(object, self.rate_limiter)),
            self._room_messages,
            self._max_messages_per_room,
            self.nats_service,
            self.subject_manager,
        )

    async def send_global_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, object]:
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
        return await send_global_message_helper(player_id, message, self._chat_send_services())

    async def send_party_message(self, player_id: uuid.UUID | str, message: str, party_id: str) -> dict[str, object]:
        """
        Send a party (ephemeral group) chat message. Only current party members
        receive it; delivery is enforced by PartyChannelStrategy. Caller must
        ensure the sender is in the given party.

        Args:
            player_id: ID of the sender
            message: Message content
            party_id: Party ID

        Returns:
            Dictionary with success status and message details
        """
        return await send_party_message_helper(
            player_id,
            message,
            party_id,
            cast(ChatPlayerService, cast(object, self.player_service)),
            cast(ChatRateLimiter, cast(object, self.rate_limiter)),
            cast(ChatLogger, cast(object, self.chat_logger)),
            self.nats_service,
            self.subject_manager,
        )

    async def send_system_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, object]:
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
        return await send_system_message_helper(player_id, message, self._chat_send_services())

    async def send_npc_say_to_room(self, npc_id: str, npc_name: str, room_id: str, message: str) -> dict[str, object]:
        """Publish a say-shaped room message from an NPC (no player lookup)."""
        return await send_npc_say_to_room_helper(
            self, npc_id=npc_id, npc_name=npc_name, room_id=room_id, message=message
        )

    async def send_personal_system_message(self, player_id: uuid.UUID | str, message: str) -> dict[str, object]:
        """Send a system-channel message to one player (quest lifecycle, etc.)."""
        return await send_personal_system_message_helper(self, player_id, message)

    async def send_whisper_message(
        self, sender_id: uuid.UUID | str, target_id: uuid.UUID | str, message: str
    ) -> dict[str, object]:
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
        return await send_whisper_message_helper(
            sender_id,
            target_id,
            message,
            self._chat_send_services(),
            cast(WhisperTracker, cast(object, self._whisper_tracker)),
        )

    async def send_emote_message(self, player_id: uuid.UUID | str, action: str) -> dict[str, object]:
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
        error_result = validate_emote_action(action)
        if error_result:
            return error_result
        player = await self.player_service.get_player_by_id(uuid.UUID(str(player_id)))
        if not player:
            return {"success": False, "error": "Player not found"}
        self.user_manager.load_player_mutes(player_id)
        if not self.rate_limiter.check_rate_limit(player_id, "emote", player.name):
            return {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another emote.",
                "rate_limited": True,
            }
        room_id = player.current_room_id
        if not room_id:
            return {"success": False, "error": "Player not in a room"}
        error_result = check_channel_permissions(self.user_manager, player_id, "say")
        if error_result:
            return error_result
        chat_message = create_and_log_chat_message(player_id, player.name, action, room_id, "emote")
        self.rate_limiter.record_message(player_id, "emote", player.name)
        store_message_in_room_history(self._room_messages, chat_message, room_id, self._max_messages_per_room)
        nats_error = await _publish_room_chat(
            chat_message, room_id, self.nats_service, self.subject_manager, player_id, player.name
        )
        if nats_error:
            return nats_error
        chat_message.echo_sent = True
        _register_echo_suppression(chat_message.id)
        return {"success": True, "message": chat_message.to_dict(), "room_id": room_id}

    async def set_player_pose(self, player_id: uuid.UUID | str, pose: str) -> dict[str, object]:
        """
        Set a player's pose (temporary, in-memory only).

        Args:
            player_id: ID of the player setting the pose
            pose: Pose description

        Returns:
            Dictionary with success status and message details
        """
        return await set_player_pose(
            player_id,
            pose,
            self.player_service,
            self._pose_manager,
            self.nats_service,
            self.subject_manager,
        )

    def get_player_pose(self, player_id: uuid.UUID | str) -> str | None:
        """
        Get a player's current pose.

        Args:
            player_id: ID of the player

        Returns:
            Current pose description or None if no pose set
        """
        return get_player_pose(player_id, self._pose_manager)

    def clear_player_pose(self, player_id: uuid.UUID | str) -> bool:
        """
        Clear a player's pose.

        Args:
            player_id: ID of the player

        Returns:
            True if pose was cleared, False if no pose was set
        """
        return clear_player_pose(player_id, self._pose_manager)

    async def get_room_poses(self, room_id: str) -> dict[str, str]:
        """
        Get all poses for players in a room.

        Args:
            room_id: ID of the room

        Returns:
            Dictionary mapping player names to their poses
        """
        return await get_room_poses(room_id, self.room_service, self.player_service, self._pose_manager)

    async def send_predefined_emote(self, player_id: uuid.UUID | str, emote_command: str) -> dict[str, object]:
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
        return await send_predefined_emote_helper(
            player_id,
            emote_command,
            cast(ChatPlayerService, cast(object, self.player_service)),
            self.user_manager,
            cast(ChatRateLimiter, cast(object, self.rate_limiter)),
            cast(ChatLogger, cast(object, self.chat_logger)),
            self.nats_service,
            self.subject_manager,
            cast(ChatEmoteService | None, self.emote_service),
        )

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

    def get_player_mutes(self, player_id: uuid.UUID | str) -> dict[str, object]:
        """Get all mutes applied by a player."""
        return self._moderation.get_player_mutes(player_id)

    def get_user_management_stats(self) -> dict[str, object]:
        """Get user management system statistics."""
        return self._moderation.get_user_management_stats()

    def get_room_messages(self, room_id: str, limit: int = 50) -> list[dict[str, object]]:
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
