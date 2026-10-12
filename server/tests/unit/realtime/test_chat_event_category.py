"""Wire-level tests: chat_message events and the room-name command_response carry a semantic category."""

# pyright: reportPrivateUsage=false, reportAny=false, reportUnknownMemberType=false
# Tests drive the handlers' underscore-prefixed builders and inspect dynamic event payloads.

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.constants.message_category import MessageCategory
from server.game.chat_message import ChatMessage
from server.game.chat_nats_publisher import publish_chat_message_to_nats
from server.game.chat_npc_system import send_fake_npc_whisper
from server.realtime.nats_message_handler import NATSMessageHandler
from server.realtime.player_event_handlers_room import PlayerRoomEventHandler


def _chat_event_data(handler: NATSMessageHandler, payload: dict[str, object]) -> dict[str, object]:
    """Run a NATS chat payload through the handler's extract -> validate -> build pipeline."""
    fields = handler._extract_chat_message_fields(payload)
    validated = handler._validate_chat_message_fields(fields, payload)
    event = handler._build_chat_event(validated, "formatted")
    return cast(dict[str, object], event["data"])


def _nats_payload(channel: str) -> dict[str, object]:
    return {
        "channel": channel,
        "room_id": "room_1",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "Morgan",
        "content": "Hello",
        "message_id": "msg_001",
        "timestamp": "2024-01-01T00:00:00Z",
    }


@pytest.mark.parametrize(
    ("channel", "expected"),
    [
        ("say", MessageCategory.CHAT_SAY),
        ("local", MessageCategory.CHAT_LOCAL),
        ("global", MessageCategory.CHAT_GLOBAL),
        ("party", MessageCategory.CHAT_PARTY),
        ("whisper", MessageCategory.CHAT_WHISPER),
        ("shout", MessageCategory.CHAT_SHOUT),
        ("emote", MessageCategory.CHAT_EMOTE),
        ("pose", MessageCategory.CHAT_EMOTE),
        ("admin", MessageCategory.CHAT_ADMIN),
        ("system", MessageCategory.SYSTEM_INFO),
    ],
)
def test_build_chat_event_tags_category_per_channel(
    nats_message_handler: NATSMessageHandler, channel: str, expected: MessageCategory
) -> None:
    """Each chat channel maps to its semantic category; the channel stays as conversation identity."""
    data = _chat_event_data(nats_message_handler, _nats_payload(channel))
    assert data["category"] == expected
    assert data["channel"] == channel


def test_build_chat_event_unknown_channel_has_no_category(nats_message_handler: NATSMessageHandler) -> None:
    """An unmapped channel is left untagged rather than guessed."""
    data = _chat_event_data(nats_message_handler, _nats_payload("mystery"))
    assert "category" not in data


class _CapturingNats:
    """Minimal NATS stand-in that records what the chat publisher puts on the wire."""

    def __init__(self) -> None:
        self.published: list[dict[str, object]] = []

    def is_connected(self) -> bool:
        return True

    async def publish(self, _subject: str, data: dict[str, object]) -> None:
        self.published.append(data)


@pytest.mark.asyncio
async def test_fake_npc_whisper_and_real_whisper_get_the_same_category(
    nats_message_handler: NATSMessageHandler,
) -> None:
    """ADR-024: a hallucinated NPC whisper is indistinguishable from a real one on the wire."""
    target = str(uuid.uuid4())
    nats = _CapturingNats()

    # Real whisper: the same ChatMessage -> NATS publish the whisper command's chat service uses.
    real = ChatMessage(
        sender_id=str(uuid.uuid4()), sender_name="Morgan", channel="whisper", content="They watch.", target_id=target
    )
    assert await publish_chat_message_to_nats(real, None, nats, None)

    chat_service = MagicMock()
    chat_service.nats_service = nats
    chat_service.subject_manager = None
    fake = await send_fake_npc_whisper(chat_service, target, "The Whisperer", "They watch.")
    assert fake["success"] is True
    assert len(nats.published) == 2

    real_data, fake_data = (_chat_event_data(nats_message_handler, payload) for payload in nats.published)
    assert real_data["category"] == fake_data["category"] == MessageCategory.CHAT_WHISPER
    assert real_data["channel"] == fake_data["channel"] == "whisper"


@pytest.mark.asyncio
async def test_send_room_name_message_is_tagged_room_name(player_room_event_handler: PlayerRoomEventHandler) -> None:
    """The room-name command_response carries room.name so the client need not guess from the text."""
    player_id = uuid.uuid4()
    send = AsyncMock()
    player_room_event_handler.connection_manager = MagicMock(send_personal_message=send)

    await player_room_event_handler._send_room_name_message(player_id, "room_001", "Test Room")

    send.assert_awaited_once()
    sent = cast(dict[str, object], send.await_args_list[0].args[1])
    data = cast(dict[str, object], sent["data"])
    assert sent["event_type"] == "command_response"
    assert data["result"] == "Test Room"
    assert data["category"] == MessageCategory.ROOM_NAME
