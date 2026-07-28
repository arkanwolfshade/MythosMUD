"""NPC and personal system chat delivery via ChatService (issue #146 MVP).

# ponytail: synthetic NPC sender UUIDs; dedicated npc channel / mute rules if chat noise matters
# ponytail: every-tick quest progress for debug; milestones in follow-up #583
"""

from __future__ import annotations

import asyncio
import uuid
from typing import Any

from ..events.event_types import NPCSpoke
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_message import ChatMessage
from .chat_message_helpers import create_and_log_chat_message, store_message_in_room_history
from .chat_nats_publisher import publish_chat_message_to_nats

logger = get_logger("communications.chat_npc_system")

# Stable UUID namespace for non-player chat senders (not a real player row).
_NPC_SENDER_NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
_SYSTEM_SENDER_ID = str(uuid.UUID("00000000-0000-4000-8000-000000000001"))

_CHAT_SERVICE: Any | None = None


def set_chat_service_for_npc_system(chat_service: Any | None) -> None:
    """Wire ChatService once at app startup (optional for unit tests)."""
    global _CHAT_SERVICE  # pylint: disable=global-statement  # Reason: process-wide chat delivery hook
    _CHAT_SERVICE = chat_service


def npc_sender_id(npc_id: str) -> str:
    """Deterministic UUID string for an NPC chat sender."""
    return str(uuid.uuid5(_NPC_SENDER_NS, f"mythosmud:npc:{npc_id}"))


def schedule_coro(coro: Any) -> None:
    """Fire-and-forget a coroutine on the running loop when available."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        logger.debug("No running event loop; skipping async chat delivery")
        return
    loop.create_task(coro)


async def send_npc_say_to_room(
    chat_service: Any,
    *,
    npc_id: str,
    npc_name: str,
    room_id: str,
    message: str,
) -> dict[str, Any]:
    """Publish a say-shaped room message from an NPC via ChatService/NATS."""
    if not message or not message.strip():
        return {"success": False, "error": "Message cannot be empty"}
    if not room_id:
        return {"success": False, "error": "Room required"}

    sender_id = npc_sender_id(npc_id)
    chat_message = create_and_log_chat_message(sender_id, npc_name, message, room_id, "say")
    chat_message.speaker_kind = "npc"
    store_message_in_room_history(
        chat_service._room_messages,  # pylint: disable=protected-access  # Reason: reuse ChatService room history store
        chat_message,
        room_id,
        chat_service._max_messages_per_room,  # pylint: disable=protected-access
    )
    success = await publish_chat_message_to_nats(
        chat_message, room_id, chat_service.nats_service, chat_service.subject_manager
    )
    if not success:
        logger.error("NPC say NATS publish failed", npc_id=npc_id, room_id=room_id)
        return {"success": False, "error": "Chat system temporarily unavailable."}
    message_dict = chat_message.to_dict()
    return {"success": True, "message": message_dict, "room_id": room_id}


async def send_personal_system_message(chat_service: Any, player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
    """Send a system-channel message to one player (whisper subject)."""
    if not message or not message.strip():
        return {"success": False, "error": "Message cannot be empty"}
    player_id_str = str(player_id)
    chat_message = ChatMessage(
        sender_id=_SYSTEM_SENDER_ID,
        sender_name="System",
        channel="system",
        content=message.strip(),
        target_id=player_id_str,
    )
    chat_message.speaker_kind = "system"
    chat_message.log_message()
    success = await publish_chat_message_to_nats(
        chat_message, None, chat_service.nats_service, chat_service.subject_manager
    )
    if not success:
        logger.error("Personal system NATS publish failed", player_id=player_id_str)
        return {"success": False, "error": "Chat system temporarily unavailable."}
    return {"success": True, "message": chat_message.to_dict()}


async def deliver_npc_room_speech(
    *,
    npc_id: str,
    room_id: str,
    message: str,
    npc_name: str | None = None,
) -> dict[str, Any]:
    """Deliver NPC room speech using the wired ChatService, if any."""
    # Lazy import avoids chat_npc_system <-> npc package cycles at import time.
    from ..npc.npc_display_names import resolve_npc_display_name

    if _CHAT_SERVICE is None:
        logger.debug("ChatService not wired; NPC speech skipped", npc_id=npc_id)
        return {"success": False, "error": "ChatService unavailable"}
    name = resolve_npc_display_name(npc_id, npc_name)
    return await send_npc_say_to_room(_CHAT_SERVICE, npc_id=npc_id, npc_name=name, room_id=room_id, message=message)


async def deliver_personal_system(player_id: uuid.UUID | str, message: str) -> dict[str, Any]:
    """Deliver personal system chat using the wired ChatService, if any."""
    if _CHAT_SERVICE is None:
        logger.debug("ChatService not wired; system chat skipped", player_id=str(player_id))
        return {"success": False, "error": "ChatService unavailable"}
    return await send_personal_system_message(_CHAT_SERVICE, player_id, message)


def schedule_npc_room_speech(
    *,
    npc_id: str,
    room_id: str,
    message: str,
    npc_name: str | None = None,
) -> None:
    """Schedule NPC room speech from sync code (reactions, integration)."""
    schedule_coro(deliver_npc_room_speech(npc_id=npc_id, room_id=room_id, message=message, npc_name=npc_name))


def schedule_personal_system(player_id: uuid.UUID | str, message: str) -> None:
    """Schedule personal system chat from sync or async callers."""
    schedule_coro(deliver_personal_system(player_id, message))


_NPC_SPOKE_SUBSCRIBED = False


def _on_npc_spoke(event: Any) -> None:
    """Bridge NPCSpoke events into ChatService room say (say-shaped)."""
    channel = getattr(event, "channel", "local") or "local"
    if channel == "whisper":
        # ponytail: NPC whisper chat later if quest/dialogue needs it
        return
    room_id = getattr(event, "room_id", None) or ""
    message = getattr(event, "message", None) or ""
    npc_id = getattr(event, "npc_id", None) or ""
    if not room_id or not message or not npc_id or room_id == "unknown":
        return
    schedule_npc_room_speech(
        npc_id=npc_id,
        room_id=room_id,
        message=message,
        npc_name=getattr(event, "npc_name", None),
    )


def subscribe_npc_spoke_to_chat(event_bus: Any) -> None:
    """Subscribe once so NPCSpoke publishes become room chat lines."""
    global _NPC_SPOKE_SUBSCRIBED  # pylint: disable=global-statement  # Reason: one-shot EventBus subscription guard
    if event_bus is None or _NPC_SPOKE_SUBSCRIBED:
        return

    event_bus.subscribe(NPCSpoke, _on_npc_spoke, service_id="chat_npc_system")
    _NPC_SPOKE_SUBSCRIBED = True
    logger.info("NPCSpoke chat bridge subscribed")
