"""Message creation and storage helpers for chat service."""

from typing import TYPE_CHECKING

from ..services.chat_logger import chat_logger

if TYPE_CHECKING:
    from .chat_message import ChatMessage


def create_and_log_chat_message(
    player_id: str, player_name: str, message: str, room_id: str | None, channel: str
) -> "ChatMessage":
    """Create chat message and log it."""
    from .chat_message import ChatMessage

    chat_message = ChatMessage(sender_id=player_id, sender_name=player_name, channel=channel, content=message.strip())
    chat_logger.log_chat_message(
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
    chat_message.log_message()
    return chat_message


def store_message_in_room_history(
    room_messages: dict[str, list["ChatMessage"]], chat_message: "ChatMessage", room_id: str, max_messages: int
) -> None:
    """Store message in room history with limit management."""
    if room_id not in room_messages:
        room_messages[room_id] = []
    room_messages[room_id].append(chat_message)
    if len(room_messages[room_id]) > max_messages:
        room_messages[room_id] = room_messages[room_id][-max_messages:]


def register_echo_suppression(message_id: str) -> None:
    """Register a chat message ID so the sender does not receive an echo."""
    try:
        from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
    except ImportError:
        return
    SUPPRESS_ECHO_MESSAGE_IDS.add(message_id)


def store_global_message_in_history(
    room_messages: dict[str, list["ChatMessage"]], chat_message: "ChatMessage", max_messages: int
) -> None:
    """Store global message in history."""
    if "global" not in room_messages:
        room_messages["global"] = []

    room_messages["global"].append(chat_message)

    if len(room_messages["global"]) > max_messages:
        room_messages["global"] = room_messages["global"][-max_messages:]
