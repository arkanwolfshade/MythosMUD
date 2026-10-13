"""
Chat lines carry styled spans (#1036): an NPC speaker's name, and spans inside a narration line.

The formatted line is built from parts (``format_message_parts``), so the spans and the plain text come from one
template and cannot drift. Dampening rewrites words, so spans inside the content survive only while it is untouched;
the speaker's name is outside the content and always survives.
"""

# pyright: reportAny=false, reportPrivateUsage=false
# The handler, ChatService and NATS publisher are exercised through MagicMock/AsyncMock doubles, and several of the
# helpers under test are private by design; attribute access on those doubles is Any by construction.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.constants.message_segments import MessageSegment
from server.constants.npc_disposition import NpcDisposition
from server.game import chat_npc_system
from server.game.chat_message import ChatMessage
from server.game.chat_nats_publisher import _build_nats_message_data
from server.realtime.message_formatters import format_message_content, format_message_segments
from server.realtime.nats_message_handler import NATSMessageHandler

GHOUL = NpcDisposition.AGGRESSIVE_MOB
CHANNELS = ["say", "local", "global", "emote", "pose", "admin", "whisper", "party", "shout", "unknown_channel"]


@pytest.mark.parametrize("for_recipient", [False, True])
@pytest.mark.parametrize("channel", CHANNELS)
def test_spans_join_to_the_formatted_line_on_every_channel(channel: str, for_recipient: bool) -> None:
    """The speaker's name is the only styled span, and the spans always add up to the plain line."""
    segments = format_message_segments(
        channel, "Ghoul", "hello there", speaker_disposition=GHOUL, for_recipient=for_recipient
    )
    assert segments is not None
    line = format_message_content(channel, "Ghoul", "hello there", for_recipient=for_recipient)
    assert "".join(segment["text"] for segment in segments) == line
    assert [s for s in segments if "category" in s] == [{"text": "Ghoul", "category": "npc.aggressive_mob"}]


def test_the_system_channel_has_no_speaker_name_to_style() -> None:
    assert format_message_segments("system", "System", "hello", speaker_disposition=GHOUL) is None


def test_a_line_with_nothing_styled_has_no_segments() -> None:
    assert format_message_segments("say", "Alice", "hello") is None


def test_narration_content_spans_are_framed_by_the_channel_prefix() -> None:
    content: list[MessageSegment] = [
        {"text": "A "},
        {"text": "Shadow", "category": "npc.aggressive_mob"},
        {"text": " materializes before you!"},
    ]
    segments = format_message_segments(
        "system", "System", "A Shadow materializes before you!", content_segments=content
    )
    assert segments == [
        {"text": "[SYSTEM] A "},
        {"text": "Shadow", "category": "npc.aggressive_mob"},
        {"text": " materializes before you!"},
    ]


# --- the NATS event --------------------------------------------------------------------------------------------------


def _payload(**extra: object) -> dict[str, object]:
    return {
        "channel": "say",
        "room_id": "room-1",
        "sender_id": str(uuid.uuid4()),
        "sender_name": "Ghoul",
        "content": "Hello",
        "message_id": "msg-1",
        "timestamp": "2026-01-01T00:00:00Z",
        **extra,
    }


def _event(**extra: object) -> dict[str, object]:
    handler = NATSMessageHandler(connection_manager=MagicMock())
    payload = _payload(**extra)
    validated = handler._validate_chat_message_fields(handler._extract_chat_message_fields(payload), payload)
    return cast("dict[str, object]", handler._build_chat_event(validated, "formatted")["data"])


def test_an_npc_speaker_event_carries_the_styled_name() -> None:
    data = _event(speaker_kind="npc", speaker_disposition="aggressive_mob")
    assert data["segments"] == [{"text": "Ghoul", "category": "npc.aggressive_mob"}, {"text": " says: Hello"}]
    assert data["speaker_disposition"] == "aggressive_mob"


def test_a_player_speaker_event_has_no_segments() -> None:
    data = _event()
    assert "segments" not in data
    assert "speaker_disposition" not in data


def test_an_unrecognised_disposition_leaves_the_name_plain() -> None:
    assert "segments" not in _event(speaker_disposition="friendly")


def test_malformed_content_segments_are_ignored_not_trusted() -> None:
    assert "segments" not in _event(channel="system", content_segments=[{"text": 5}])
    assert "segments" not in _event(channel="system", content_segments="not a list")


# --- per-receiver rewrites under dampening ----------------------------------------------------------------------------


def _apply(event_data: dict[str, object], original: str, content: str) -> dict[str, object]:
    data: dict[str, object] = {"segments": [{"text": "stale"}]}
    NATSMessageHandler._apply_receiver_segments(data, event_data, "say", "Ghoul", original, content)
    return data


def test_the_speaker_name_survives_dampening_but_spans_inside_the_content_do_not() -> None:
    event_data: dict[str, object] = {
        "speaker_disposition": "aggressive_mob",
        "original_segments": [{"text": "Hello", "category": "npc.shopkeeper"}],
    }
    untouched = _apply(event_data, "Hello", "Hello")
    assert untouched["segments"] == [
        {"text": "Ghoul", "category": "npc.aggressive_mob"},
        {"text": " says: "},
        {"text": "Hello", "category": "npc.shopkeeper"},
    ]

    rewritten = _apply(event_data, "Hello", "H☁llo")
    assert rewritten["segments"] == [{"text": "Ghoul", "category": "npc.aggressive_mob"}, {"text": " says: H☁llo"}]


def test_a_receiver_copy_loses_stale_spans_when_nothing_is_styled_any_more() -> None:
    assert "segments" not in _apply({}, "Hello", "Hello")


# --- ChatMessage and the NATS payload ----------------------------------------------------------------------------------


def test_chat_message_and_payload_carry_the_two_inputs_only_when_set() -> None:
    plain = ChatMessage("s1", "Alice", "say", "hi")
    assert "speaker_disposition" not in plain.to_dict()
    assert "content_segments" not in _build_nats_message_data(plain, "room-1")

    npc = ChatMessage("npc-1", "Ghoul", "say", "hi")
    npc.speaker_disposition = "aggressive_mob"
    npc.content_segments = [{"text": "hi", "category": "npc.passive_mob"}]
    assert npc.to_dict()["speaker_disposition"] == "aggressive_mob"
    payload = _build_nats_message_data(npc, "room-1")
    assert payload["speaker_disposition"] == "aggressive_mob"
    assert payload["content_segments"] == [{"text": "hi", "category": "npc.passive_mob"}]


# --- producers --------------------------------------------------------------------------------------------------------


def _published(publish: AsyncMock) -> ChatMessage:
    """The ChatMessage handed to the NATS publisher on its last call."""
    args = publish.await_args
    assert args is not None
    message = args.args[0]
    assert isinstance(message, ChatMessage)
    return message


def _chat_service() -> MagicMock:
    return MagicMock(
        _room_messages={}, _max_messages_per_room=10, nats_service=MagicMock(), subject_manager=MagicMock()
    )


@pytest.mark.asyncio
async def test_npc_room_speech_is_tagged_with_the_speakers_disposition() -> None:
    publish = AsyncMock(return_value=True)
    with (
        patch.object(chat_npc_system, "publish_chat_message_to_nats", publish),
        patch.object(chat_npc_system, "get_npc_disposition_from_instance", return_value=NpcDisposition.QUEST_GIVER),
    ):
        result = await chat_npc_system.send_npc_say_to_room(
            _chat_service(), npc_id="npc-1", npc_name="Elder", room_id="room-1", message="Welcome."
        )
    assert result["success"] is True
    sent = _published(publish)
    assert sent.speaker_kind == "npc"
    assert sent.speaker_disposition == "quest_giver"


@pytest.mark.asyncio
async def test_a_fake_npc_whisper_stays_untagged() -> None:
    """#1034/ADR-024: a hallucinated whisper has no real NPC to take a disposition from, so it must not invent one."""
    publish = AsyncMock(return_value=True)
    with patch.object(chat_npc_system, "publish_chat_message_to_nats", publish):
        _ = await chat_npc_system.send_fake_npc_whisper(_chat_service(), uuid.uuid4(), "Ghost", "Boo.")
    assert _published(publish).speaker_disposition is None


@pytest.mark.asyncio
async def test_personal_system_narration_keeps_spans_only_if_they_describe_the_text() -> None:
    publish = AsyncMock(return_value=True)
    spans: list[MessageSegment] = [{"text": "A "}, {"text": "Shadow", "category": "npc.aggressive_mob"}]
    with patch.object(chat_npc_system, "publish_chat_message_to_nats", publish):
        _ = await chat_npc_system.send_personal_system_message(_chat_service(), uuid.uuid4(), "A Shadow", spans)
        assert _published(publish).content_segments == spans

        _ = await chat_npc_system.send_personal_system_message(_chat_service(), uuid.uuid4(), "A Wraith", spans)
        assert _published(publish).content_segments is None
