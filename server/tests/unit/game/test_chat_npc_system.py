"""Unit tests for NPC say and personal system chat (issue #146 MVP)."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import NPCSpoke
from server.game import chat_npc_system
from server.game.chat_message import ChatMessage
from server.game.chat_npc_system import (
    deliver_npc_room_speech,
    deliver_personal_system,
    npc_sender_id,
    send_npc_say_to_room,
    send_personal_system_message,
    set_chat_service_for_npc_system,
    subscribe_npc_spoke_to_chat,
)
from server.game.quest.quest_chat_notify import (
    emit_quest_npc_say,
    notify_quest_abandoned,
    notify_quest_completed,
    notify_quest_progress,
    notify_quest_started,
    quest_ask_npc_line,
    quest_turnin_npc_line,
    title_from_quest_result,
)
from server.npc.npc_display_names import register_npc_display_name, resolve_npc_display_name


@pytest.fixture(autouse=True)
def _reset_chat_npc_wiring():
    """Keep process-wide chat wiring isolated per test."""
    set_chat_service_for_npc_system(None)
    chat_npc_system._npc_spoke_subscribed = False  # pylint: disable=protected-access
    yield
    set_chat_service_for_npc_system(None)
    chat_npc_system._npc_spoke_subscribed = False  # pylint: disable=protected-access


def _mock_chat_service() -> MagicMock:
    chat_service = MagicMock()
    chat_service._room_messages = {}
    chat_service._max_messages_per_room = 50
    chat_service.nats_service = MagicMock()
    chat_service.subject_manager = MagicMock()
    return chat_service


@pytest.mark.asyncio
async def test_send_npc_say_to_room_publishes_say_with_npc_name():
    """NPC room say uses NPC display name and speaker_kind npc (not log-only)."""
    chat_service = _mock_chat_service()

    with patch(
        "server.game.chat_npc_system.publish_chat_message_to_nats",
        new_callable=AsyncMock,
        return_value=True,
    ) as publish:
        result = await send_npc_say_to_room(
            chat_service,
            npc_id="daisy_def",
            npc_name="Daisy",
            room_id="earth_arkhamcity_downtown_001",
            message="I have a task for you: Fetch the package.",
        )

    assert result["success"] is True
    assert result["message"]["sender_name"] == "Daisy"
    assert result["message"]["channel"] == "say"
    assert result["message"]["speaker_kind"] == "npc"
    assert result["message"]["sender_id"] == npc_sender_id("daisy_def")
    publish.assert_awaited_once()
    published_msg = publish.await_args.args[0]
    assert isinstance(published_msg, ChatMessage)
    assert published_msg.speaker_kind == "npc"


@pytest.mark.asyncio
async def test_send_npc_say_rejects_empty_message_and_room():
    """NPC say fails closed on empty content or missing room."""
    chat_service = _mock_chat_service()
    empty = await send_npc_say_to_room(chat_service, npc_id="n1", npc_name="N", room_id="r1", message="   ")
    assert empty["success"] is False
    no_room = await send_npc_say_to_room(chat_service, npc_id="n1", npc_name="N", room_id="", message="Hi")
    assert no_room["success"] is False


@pytest.mark.asyncio
async def test_send_npc_say_publish_failure():
    """NPC say reports failure when NATS publish returns False."""
    chat_service = _mock_chat_service()
    with patch(
        "server.game.chat_npc_system.publish_chat_message_to_nats",
        new_callable=AsyncMock,
        return_value=False,
    ):
        result = await send_npc_say_to_room(chat_service, npc_id="n1", npc_name="N", room_id="r1", message="Hi")
    assert result["success"] is False
    assert "unavailable" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_personal_system_message_targets_player():
    """Personal system chat sets channel system and target_id."""
    chat_service = _mock_chat_service()
    player_id = uuid.uuid4()

    with patch(
        "server.game.chat_npc_system.publish_chat_message_to_nats",
        new_callable=AsyncMock,
        return_value=True,
    ) as publish:
        result = await send_personal_system_message(chat_service, player_id, "Quest progress: Fetch")

    assert result["success"] is True
    assert result["message"]["channel"] == "system"
    assert result["message"]["target_id"] == str(player_id)
    assert result["message"]["speaker_kind"] == "system"
    publish.assert_awaited_once()
    assert publish.await_args.args[0].target_id == str(player_id)
    assert publish.await_args.args[1] is None  # no room for system


@pytest.mark.asyncio
async def test_send_personal_system_rejects_empty():
    """Personal system fails on empty message."""
    result = await send_personal_system_message(_mock_chat_service(), uuid.uuid4(), "")
    assert result["success"] is False


@pytest.mark.asyncio
async def test_deliver_when_chat_service_unwired():
    """Delivery helpers no-op when ChatService is not wired."""
    npc = await deliver_npc_room_speech(npc_id="n1", room_id="r1", message="Hi", npc_name="N")
    system = await deliver_personal_system(uuid.uuid4(), "Quest started: X")
    assert npc["success"] is False
    assert system["success"] is False


@pytest.mark.asyncio
async def test_deliver_npc_room_speech_uses_registered_name():
    """Wired delivery resolves registered NPC display name."""
    chat_service = _mock_chat_service()
    set_chat_service_for_npc_system(chat_service)
    register_npc_display_name("npc-42", "Morgan")

    with patch(
        "server.game.chat_npc_system.send_npc_say_to_room",
        new_callable=AsyncMock,
        return_value={"success": True},
    ) as send:
        await deliver_npc_room_speech(npc_id="npc-42", room_id="room-1", message="Hello")

    send.assert_awaited_once()
    assert send.await_args.kwargs["npc_name"] == "Morgan"


def test_npc_spoke_handler_schedules_room_speech():
    """NPCSpoke bridge schedules say-shaped room speech; skips whisper."""
    event = NPCSpoke(npc_id="n1", room_id="r1", message="Hi", channel="say", npc_name="N")
    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        chat_npc_system._on_npc_spoke(event)  # pylint: disable=protected-access
    schedule.assert_called_once_with(npc_id="n1", room_id="r1", message="Hi", npc_name="N")

    whisper = NPCSpoke(npc_id="n1", room_id="r1", message="Psst", channel="whisper")
    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        chat_npc_system._on_npc_spoke(whisper)  # pylint: disable=protected-access
    schedule.assert_not_called()


def test_subscribe_npc_spoke_to_chat_once():
    """NPCSpoke subscription is one-shot."""
    bus = MagicMock()
    subscribe_npc_spoke_to_chat(bus)
    subscribe_npc_spoke_to_chat(bus)
    bus.subscribe.assert_called_once()


def test_resolve_npc_display_name():
    """Display name registry prefers explicit, then registered, then Someone."""
    register_npc_display_name("id-a", "Alpha")
    assert resolve_npc_display_name("id-a", "Explicit") == "Explicit"
    assert resolve_npc_display_name("id-a") == "Alpha"
    assert resolve_npc_display_name("missing") == "Someone"


def test_notify_quest_lifecycle_schedules_personal_system():
    """Quest notify helpers schedule personal system chat with expected text."""
    player_id = uuid.uuid4()
    with patch("server.game.quest.quest_chat_notify.schedule_personal_system") as schedule:
        notify_quest_started(player_id, "Fetch")
        notify_quest_progress(player_id, "Fetch")
        notify_quest_completed(player_id, "Fetch")
        notify_quest_abandoned(player_id, "Fetch")
    assert schedule.call_args_list[0].args == (player_id, "Quest started: Fetch")
    assert schedule.call_args_list[1].args == (player_id, "Quest progress: Fetch")
    assert schedule.call_args_list[2].args == (player_id, "Quest completed: Fetch")
    assert schedule.call_args_list[3].args == (player_id, "Quest abandoned: Fetch")


def test_emit_quest_npc_say_and_templates():
    """Ask/turnin templates and emit path."""
    assert "task for you: Fetch" in quest_ask_npc_line("Fetch")
    assert "completed: Fetch" in quest_turnin_npc_line("Fetch")
    with patch("server.game.quest.quest_chat_notify.schedule_npc_room_speech") as schedule:
        emit_quest_npc_say(npc_id="n1", npc_name="Morgan", room_id="r1", line="Hi")
    schedule.assert_called_once_with(npc_id="n1", npc_name="Morgan", room_id="r1", message="Hi")


def test_title_from_quest_result_prefers_title_field():
    """Successful results expose title for NPC say templates."""
    assert title_from_quest_result({"success": True, "title": "Fetch"}, prefix="Quest started: ") == "Fetch"
    assert (
        title_from_quest_result({"success": True, "message": "Quest started: Fetch"}, prefix="Quest started: ")
        == "Fetch"
    )
    assert title_from_quest_result({"success": False, "message": "Nope"}, prefix="Quest started: ") is None


def test_chat_message_to_dict_includes_speaker_kind():
    """speaker_kind is serialized when set."""
    msg = ChatMessage(uuid.uuid4(), "Daisy", "say", "Hello")
    msg.speaker_kind = "npc"
    assert msg.to_dict()["speaker_kind"] == "npc"


@pytest.mark.asyncio
async def test_chat_service_npc_and_personal_wrappers():
    """ChatService delegates to chat_npc_system helpers."""
    from server.game.chat_service import ChatService

    service = ChatService(MagicMock(), MagicMock(), MagicMock())
    with patch(
        "server.game.chat_service.send_npc_say_to_room_helper",
        new_callable=AsyncMock,
        return_value={"success": True},
    ) as npc:
        await service.send_npc_say_to_room("n1", "N", "r1", "Hi")
    npc.assert_awaited_once()
    with patch(
        "server.game.chat_service.send_personal_system_message_helper",
        new_callable=AsyncMock,
        return_value={"success": True},
    ) as personal:
        await service.send_personal_system_message(uuid.uuid4(), "Quest started: X")
    personal.assert_awaited_once()
