"""Channel message senders (system, whisper, party, global)."""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Message sending handlers require multiple return statements for early validation returns (permission checks, validation, error handling). Message sending requires extensive handlers for multiple message types and delivery methods.

import uuid
from collections.abc import Mapping
from typing import Protocol, TypedDict

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_message import ChatMessage
from .chat_message_helpers import (
    create_and_log_chat_message,
    store_global_message_in_history,
)
from .chat_nats_publisher import publish_chat_message_to_nats
from .chat_validation_helpers import (
    check_channel_permissions,
    check_global_level_requirement,
    validate_global_message,
)

logger = get_logger("communications.chat_channel_message_senders")

_NATS_UNAVAILABLE = "Chat system temporarily unavailable. Please try again in a moment."

ChatResult = dict[str, object]


class ChatPlayerView(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player fields used by channel senders."""

    name: str
    level: int
    current_room_id: str | None


class ChatPlayerService(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player lookup used by channel senders."""

    async def get_player_by_id(self, player_id: object) -> ChatPlayerView | None:
        """Return the player view for player_id, or None."""


class ChatUserManager(Protocol):
    """Mute and admin checks used by channel senders."""

    def is_admin(self, player_id: str) -> bool:
        """Return True if the player has admin chat privileges."""

    def load_player_mutes(self, player_id: str) -> object:
        """Load mute state for the player."""

    def is_channel_muted(self, player_id: str, channel: str) -> bool:
        """Return True if the player is muted on this channel."""

    def is_globally_muted(self, player_id: str) -> bool:
        """Return True if the player is muted on all channels."""

    def can_send_message(self, player_id: str, channel: str = "") -> bool:
        """Return True if the player may send on this channel."""


class ChatRateLimiter(Protocol):
    """Per-channel chat rate limiting."""

    def check_rate_limit(self, player_id: str, channel: str, player_name: str) -> bool:
        """Return True if the player is within the channel rate limit."""

    def record_message(self, player_id: str, channel: str, player_name: str) -> None:
        """Record a sent message for rate limiting."""


class ChatLogger(Protocol):
    """Chat log sinks used by channel senders."""

    def log_chat_message(self, payload: Mapping[str, object]) -> None:
        """Write a generic chat log entry."""

    def log_system_channel_message(self, payload: Mapping[str, object]) -> None:
        """Write a system-channel log entry."""

    def log_whisper_channel_message(self, payload: Mapping[str, object]) -> None:
        """Write a whisper-channel log entry."""

    def log_global_channel_message(self, payload: Mapping[str, object]) -> None:
        """Write a global-channel log entry."""


class WhisperTracker(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Stores last whisper sender for reply routing."""

    def store_sender(self, target_name: str, sender_name: str) -> None:
        """Remember who last whispered to target_name."""


class ChatEmoteService(Protocol):
    """Predefined-emote lookup used by chat message senders (#624)."""

    def is_emote_alias(self, command: str) -> bool:
        """Return True if command is a predefined emote alias."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires a body on Protocol stubs

    def format_emote_messages(self, command: str, player_name: str) -> tuple[str, str]:
        """Return (self_message, other_message) for a predefined emote command."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires a body on Protocol stubs


class ChatSendServices(TypedDict):
    """Shared chat delivery services for channel senders."""

    player_service: ChatPlayerService
    user_manager: ChatUserManager
    rate_limiter: ChatRateLimiter
    chat_logger: ChatLogger
    room_messages: dict[str, list[ChatMessage]]
    max_messages_per_room: int
    nats_service: object | None
    subject_manager: object | None


def normalize_player_id(player_id: uuid.UUID | str) -> str:
    """Normalize player identifiers to string form."""
    return str(player_id)


def _system_message_input_error(message: str) -> ChatResult | None:
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
        return {"success": False, "error": "Message cannot be empty"}
    if len(message.strip()) > 2000:
        logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
        return {"success": False, "error": "Message too long (max 2000 characters)"}
    return None


def _whisper_message_input_error(message: str) -> ChatResult | None:
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty whisper message ===")
        return {"success": False, "error": "Message content cannot be empty"}
    if len(message.strip()) > 2000:
        logger.debug("=== CHAT SERVICE DEBUG: Whisper message too long ===")
        return {"success": False, "error": "Message too long (maximum 2000 characters)"}
    return None


def _append_channel_history(ctx: ChatSendServices, channel: str, chat_message: ChatMessage) -> None:
    history = ctx["room_messages"]
    if channel not in history:
        history[channel] = []
    history[channel].append(chat_message)
    limit = ctx["max_messages_per_room"]
    if len(history[channel]) > limit:
        history[channel] = history[channel][-limit:]


async def _publish_chat_or_unavailable(
    chat_message: ChatMessage,
    ctx: ChatSendServices,
    extra: dict[str, object],
) -> ChatResult | None:
    success = await publish_chat_message_to_nats(chat_message, None, ctx["nats_service"], ctx["subject_manager"])
    if success:
        return None
    logger.error("NATS publishing failed - NATS is mandatory for chat functionality", **extra)
    return {"success": False, "error": _NATS_UNAVAILABLE}


async def _authorize_system_sender(
    player_id: str, ctx: ChatSendServices
) -> tuple[ChatPlayerView | None, ChatResult | None]:
    player = await ctx["player_service"].get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for system message")
        return None, {"success": False, "error": "Player not found"}
    if not ctx["user_manager"].is_admin(player_id):
        logger.debug("=== CHAT SERVICE DEBUG: Player not admin ===")
        return None, {"success": False, "error": "You must be an admin to send system messages"}
    ctx["user_manager"].load_player_mutes(player_id)
    if not ctx["rate_limiter"].check_rate_limit(player_id, "system", player.name):
        logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
        return None, {"success": False, "error": "Rate limit exceeded for system messages", "rate_limited": True}
    return player, None


def _log_and_store_system_message(
    player_id: str, player: ChatPlayerView, chat_message: ChatMessage, ctx: ChatSendServices
) -> None:
    log_payload = {
        "message_id": chat_message.id,
        "channel": chat_message.channel,
        "sender_id": chat_message.sender_id,
        "sender_name": chat_message.sender_name,
        "content": chat_message.content,
        "room_id": None,
        "filtered": False,
        "moderation_notes": None,
    }
    ctx["chat_logger"].log_chat_message(log_payload)
    ctx["chat_logger"].log_system_channel_message(
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
    ctx["rate_limiter"].record_message(player_id, "system", player.name)
    chat_message.log_message()
    logger.debug("=== CHAT SERVICE DEBUG: System chat message created ===")
    _append_channel_history(ctx, "system", chat_message)
    logger.info(
        "System message created successfully",
        player_id=player_id,
        player_name=player.name,
        message_id=chat_message.id,
    )


async def send_system_message(
    player_id: uuid.UUID | str,
    message: str,
    ctx: ChatSendServices,
) -> ChatResult:
    """Send a system message to all players."""
    player_id = normalize_player_id(player_id)
    logger.debug("=== CHAT SERVICE DEBUG: send_system_message called ===", player_id=player_id, message=message)
    logger.debug("Processing system message")
    input_error = _system_message_input_error(message)
    if input_error:
        return input_error
    player, auth_error = await _authorize_system_sender(player_id, ctx)
    if auth_error or player is None:
        return auth_error or {"success": False, "error": "Player not found"}
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="system", content=message.strip())
    _log_and_store_system_message(player_id, player, chat_message, ctx)
    logger.debug("=== CHAT SERVICE DEBUG: About to publish system message to NATS ===")
    nats_error = await _publish_chat_or_unavailable(
        chat_message,
        ctx,
        {"player_id": player_id, "player_name": player.name, "message_id": chat_message.id},
    )
    if nats_error:
        return nats_error
    logger.debug("=== CHAT SERVICE DEBUG: System NATS publishing completed ===")
    return {"success": True, "message": chat_message.to_dict()}


async def _load_whisper_participants(
    sender_id: str, target_id: str, ctx: ChatSendServices
) -> tuple[ChatPlayerView | None, ChatPlayerView | None, ChatResult | None]:
    sender_obj = await ctx["player_service"].get_player_by_id(sender_id)
    if not sender_obj:
        logger.debug("=== CHAT SERVICE DEBUG: Sender not found ===")
        return None, None, {"success": False, "error": "Sender not found"}
    target_obj = await ctx["player_service"].get_player_by_id(target_id)
    if not target_obj:
        logger.debug("=== CHAT SERVICE DEBUG: Target not found ===")
        return None, None, {"success": False, "error": "You whisper into the aether."}
    sender_name = sender_obj.name
    if not ctx["rate_limiter"].check_rate_limit(sender_id, "whisper", sender_name):
        logger.debug("=== CHAT SERVICE DEBUG: Whisper rate limited ===")
        return (
            None,
            None,
            {
                "success": False,
                "error": "You are sending messages too quickly. Please wait a moment.",
            },
        )
    return sender_obj, target_obj, None


def _log_and_store_whisper_message(
    sender_id: str,
    target_id: str,
    sender_obj: ChatPlayerView,
    target_obj: ChatPlayerView,
    chat_message: ChatMessage,
    whisper_tracker: WhisperTracker,
    ctx: ChatSendServices,
) -> None:
    sender_name = sender_obj.name
    target_name = target_obj.name
    log_payload = {
        "message_id": chat_message.id,
        "channel": chat_message.channel,
        "sender_id": chat_message.sender_id,
        "sender_name": chat_message.sender_name,
        "target_id": chat_message.target_id,
        "target_name": chat_message.target_name,
        "content": chat_message.content,
        "room_id": None,
        "filtered": False,
        "moderation_notes": None,
    }
    ctx["chat_logger"].log_chat_message(log_payload)
    ctx["chat_logger"].log_whisper_channel_message(
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
    ctx["rate_limiter"].record_message(sender_id, "whisper", sender_name)
    whisper_tracker.store_sender(target_name, sender_name)
    chat_message.log_message()
    logger.debug("=== CHAT SERVICE DEBUG: Whisper chat message created ===", message_id=chat_message.id)
    _append_channel_history(ctx, "whisper", chat_message)
    logger.info(
        "Whisper message created successfully",
        sender_id=sender_id,
        target_id=target_id,
        sender_name=sender_name,
        target_name=target_name,
        message_id=chat_message.id,
    )


async def send_whisper_message(
    sender_id: uuid.UUID | str,
    target_id: uuid.UUID | str,
    message: str,
    ctx: ChatSendServices,
    whisper_tracker: WhisperTracker,
) -> ChatResult:
    """Send a whisper message from one player to another."""
    sender_id = normalize_player_id(sender_id)
    target_id = normalize_player_id(target_id)
    logger.debug("=== CHAT SERVICE DEBUG: send_whisper_message called ===", sender_id=sender_id, target_id=target_id)
    logger.debug("Processing whisper message", sender_id=sender_id, target_id=target_id, message_length=len(message))
    input_error = _whisper_message_input_error(message)
    if input_error:
        return input_error
    message = message.strip()
    sender_obj, target_obj, load_error = await _load_whisper_participants(sender_id, target_id, ctx)
    if load_error or sender_obj is None or target_obj is None:
        return load_error or {"success": False, "error": "Sender not found"}
    sender_name = sender_obj.name
    chat_message = ChatMessage(
        sender_id=sender_id,
        sender_name=sender_name,
        target_id=target_id,
        target_name=target_obj.name,
        channel="whisper",
        content=message,
    )
    _log_and_store_whisper_message(sender_id, target_id, sender_obj, target_obj, chat_message, whisper_tracker, ctx)
    logger.debug("=== CHAT SERVICE DEBUG: About to publish whisper message to NATS ===")
    nats_error = await _publish_chat_or_unavailable(
        chat_message,
        ctx,
        {"sender_id": sender_id, "sender_name": sender_name, "message_id": chat_message.id},
    )
    if nats_error:
        return nats_error
    logger.debug("=== CHAT SERVICE DEBUG: Whisper NATS publishing completed ===")
    return {"success": True, "message": chat_message.to_dict()}


async def send_party_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many parameters for context and routing
    player_id: uuid.UUID | str,
    message: str,
    party_id: str,
    player_service: ChatPlayerService,
    rate_limiter: ChatRateLimiter,
    chat_logger: ChatLogger,
    nats_service: object | None,
    subject_manager: object | None,
) -> ChatResult:
    """
    Send a party (ephemeral group) chat message to party members only.

    Message is published to NATS on chat.party.group.{party_id}; delivery to
    only current party members is enforced by PartyChannelStrategy. Rate limit
    uses the configured party channel limit (e.g. 30 msg/min).

    Args:
        player_id: ID of the sender
        message: Message content
        party_id: Party ID (sender must be in this party; caller validates)
        player_service: Player service instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    if not message or not message.strip():
        return {"success": False, "error": "Message cannot be empty"}
    if len(message.strip()) > 2000:
        return {"success": False, "error": "Message too long (max 2000 characters)"}

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for party message")
        return {"success": False, "error": "Player not found"}

    if not rate_limiter.check_rate_limit(player_id, "party", player.name):
        return {"success": False, "error": "Rate limit exceeded for party chat", "rate_limited": True}

    chat_message = ChatMessage(
        sender_id=player_id,
        sender_name=player.name,
        channel="party",
        content=message.strip(),
        party_id=party_id,
    )
    chat_logger.log_chat_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "room_id": None,
            "filtered": False,
            "moderation_notes": None,
        }
    )
    rate_limiter.record_message(player_id, "party", player.name)
    chat_message.log_message()

    success = await publish_chat_message_to_nats(chat_message, None, nats_service, subject_manager)
    if not success:
        logger.error(
            "NATS publishing failed for party message",
            player_id=player_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    return {"success": True, "message": chat_message.to_dict()}


async def _authorize_global_sender(
    player_id: str, ctx: ChatSendServices
) -> tuple[ChatPlayerView | None, ChatResult | None]:
    player = await ctx["player_service"].get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for global message")
        return None, {"success": False, "error": "Player not found"}
    level_error = check_global_level_requirement(player, player_id)
    if level_error:
        return None, level_error
    ctx["user_manager"].load_player_mutes(player_id)
    if not ctx["rate_limiter"].check_rate_limit(player_id, "global", player.name):
        logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
        return None, {"success": False, "error": "Rate limit exceeded for global chat", "rate_limited": True}
    perm_error = check_channel_permissions(ctx["user_manager"], player_id, "global")
    if perm_error:
        return None, perm_error
    return player, None


async def send_global_message(
    player_id: uuid.UUID | str,
    message: str,
    ctx: ChatSendServices,
) -> ChatResult:
    """Send a global message to all players."""
    player_id = normalize_player_id(player_id)
    logger.debug("=== CHAT SERVICE DEBUG: send_global_message called ===", player_id=player_id, message=message)
    logger.debug("Processing global message")
    error_result = validate_global_message(message)
    if error_result:
        return error_result
    player, auth_error = await _authorize_global_sender(player_id, ctx)
    if auth_error or player is None:
        return auth_error or {"success": False, "error": "Player not found"}
    chat_message = create_and_log_chat_message(player_id, player.name, message, None, "global")
    ctx["chat_logger"].log_global_channel_message(
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
    ctx["rate_limiter"].record_message(player_id, "global", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Global chat message created ===")
    store_global_message_in_history(ctx["room_messages"], chat_message, ctx["max_messages_per_room"])
    logger.info(
        "Global message created successfully",
        player_id=player_id,
        player_name=player.name,
        message_id=chat_message.id,
    )
    logger.debug("=== CHAT SERVICE DEBUG: About to publish global message to NATS ===")
    nats_error = await _publish_chat_or_unavailable(
        chat_message,
        ctx,
        {"player_id": player_id, "player_name": player.name, "message_id": chat_message.id},
    )
    if nats_error:
        return nats_error
    logger.debug("=== CHAT SERVICE DEBUG: Global NATS publishing completed ===")
    return {"success": True, "message": chat_message.to_dict()}
