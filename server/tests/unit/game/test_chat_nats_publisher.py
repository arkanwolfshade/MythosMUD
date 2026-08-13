"""Unit tests for chat NATS publishing helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.chat_message import ChatMessage
from server.game.chat_nats_publisher import (
    _build_legacy_subject,
    _build_nats_message_data,
    _extract_subzone_from_room,
    _nats_service_ready,
    build_nats_subject,
    publish_chat_message_to_nats,
)
from server.services.nats_exceptions import NATSPublishError


def _message(channel: str = "say", content: str = "Hello", **kwargs) -> ChatMessage:
    return ChatMessage(uuid.uuid4(), "TestPlayer", channel, content, **kwargs)


def test_extract_subzone_from_room_none_returns_unknown():
    assert _extract_subzone_from_room(None) == "unknown"


def test_build_legacy_subject_say_includes_room():
    room_id = "earth_arkham_downtown_001"
    subject = build_nats_subject(_message("say"), room_id)
    assert subject == f"chat.say.{room_id}"


def test_build_legacy_subject_local_uses_subzone():
    subject = build_nats_subject(_message("local"), "earth_arkham_downtown_001")
    assert subject.startswith("chat.local.subzone.")


def test_build_legacy_subject_global():
    assert _build_legacy_subject(_message("global"), None) == "chat.global"


def test_build_legacy_subject_whisper_with_target():
    target_id = str(uuid.uuid4())
    message = _message("whisper", target_id=target_id)
    assert _build_legacy_subject(message, None) == f"chat.whisper.player.{target_id}"


def test_build_legacy_subject_party_without_id():
    assert _build_legacy_subject(_message("party"), None) == "chat.party.group.unknown"


def test_build_nats_subject_uses_subject_manager_when_available():
    subject_manager = MagicMock()
    subject_manager.build_subject.return_value = "chat.say.room.test"
    subject = build_nats_subject(_message("say"), "room_1", subject_manager)
    assert subject == "chat.say.room.test"
    subject_manager.build_subject.assert_called_once_with("chat_say_room", room_id="room_1")


def test_build_nats_message_data_includes_optional_fields():
    target_id = uuid.uuid4()
    message = _message("whisper", target_id=target_id, target_name="Other")
    message.party_id = "party-42"
    message.speaker_kind = "npc"
    data = _build_nats_message_data(message, "room_1")
    assert data["target_id"] == str(target_id)
    assert data["target_name"] == "Other"
    assert data["party_id"] == "party-42"
    assert data["speaker_kind"] == "npc"


def test_nats_service_ready_false_when_missing():
    assert _nats_service_ready(None, _message(), "room") is False


def test_nats_service_ready_false_when_disconnected():
    nats = MagicMock()
    nats.is_connected.return_value = False
    assert _nats_service_ready(nats, _message(), "room") is False


def test_nats_service_ready_false_when_pool_not_initialized():
    nats = MagicMock()
    nats.is_connected.return_value = True
    nats._pool_initialized = False
    assert _nats_service_ready(nats, _message(), "room") is False


@pytest.mark.asyncio
async def test_publish_chat_message_to_nats_success():
    nats = MagicMock()
    nats.is_connected.return_value = True
    nats.publish = AsyncMock()
    result = await publish_chat_message_to_nats(_message(), "room_1", nats)
    assert result is True
    nats.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_chat_message_to_nats_validation_failure():
    nats = MagicMock()
    result = await publish_chat_message_to_nats(_message("say", "   "), "room_1", nats)
    assert result is False
    nats.publish.assert_not_called()


@pytest.mark.asyncio
async def test_publish_chat_message_to_nats_room_access_failure():
    nats = MagicMock()
    nats.is_connected.return_value = True
    message = _message()
    message.sender_id = ""
    result = await publish_chat_message_to_nats(message, "room_1", nats)
    assert result is False


@pytest.mark.asyncio
async def test_publish_chat_message_to_nats_unexpected_error():
    nats = MagicMock()
    nats.is_connected.return_value = True
    nats.publish = AsyncMock(side_effect=RuntimeError("boom"))
    result = await publish_chat_message_to_nats(_message(), "room_1", nats)
    assert result is False


def test_build_legacy_subject_system_without_target():
    assert _build_legacy_subject(_message("system"), None) == "chat.system"


def test_build_legacy_subject_system_with_target():
    target_id = str(uuid.uuid4())
    message = _message("system", target_id=target_id)
    assert _build_legacy_subject(message, None) == f"chat.whisper.player.{target_id}"


def test_build_legacy_subject_party_with_id():
    message = _message("party")
    message.party_id = "party-9"
    assert _build_legacy_subject(message, None) == "chat.party.group.party-9"


def test_build_nats_subject_standardized_channels():
    subject_manager = MagicMock()
    subject_manager.build_subject.side_effect = lambda key, **kwargs: f"std.{key}"

    assert build_nats_subject(_message("local"), "room_1", subject_manager).startswith("std.chat_local")
    assert build_nats_subject(_message("global"), None, subject_manager) == "std.chat_global"
    assert build_nats_subject(_message("emote"), "room_1", subject_manager) == "std.chat_emote_room"
    assert build_nats_subject(_message("pose"), "room_1", subject_manager) == "std.chat_pose_room"

    whisper = _message("whisper", target_id=uuid.uuid4())
    assert build_nats_subject(whisper, None, subject_manager) == "std.chat_whisper_player"

    party = _message("party")
    party.party_id = "party-1"
    assert build_nats_subject(party, None, subject_manager) == "std.chat_party_group"

    system = _message("system", target_id=uuid.uuid4())
    assert build_nats_subject(system, None, subject_manager) == "std.chat_whisper_player"


def test_build_nats_subject_standardized_whisper_without_target():
    subject_manager = MagicMock()
    assert build_nats_subject(_message("whisper"), None, subject_manager) == "chat.whisper"


def test_build_nats_subject_standardized_party_without_id():
    subject_manager = MagicMock()
    party_subject = build_nats_subject(_message("party"), None, subject_manager)
    assert party_subject == "chat.party.group.unknown"


@pytest.mark.asyncio
async def test_publish_chat_message_to_nats_handles_publish_error():
    nats = MagicMock()
    nats.is_connected.return_value = True
    nats.publish = AsyncMock(side_effect=NATSPublishError("fail", subject="chat.say.room"))
    result = await publish_chat_message_to_nats(_message(), "room_1", nats)
    assert result is False
