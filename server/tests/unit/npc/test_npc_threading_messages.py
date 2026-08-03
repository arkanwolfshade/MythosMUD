"""Unit tests for NPC threading message serialization."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.npc.threading import (
    NPCActionMessage,
    NPCActionType,
    NPCCommunicationBridge,
    NPCMessageQueue,
    NPCThreadManager,
)


def test_npc_action_message_round_trip():
    msg = NPCActionMessage(
        action_type=NPCActionType.SPEAK,
        npc_id="npc-1",
        timestamp=123.456,
        message="Hello",
        channel="say",
    )
    data = msg.to_dict()
    restored = NPCActionMessage.from_dict(data)
    assert restored.action_type == NPCActionType.SPEAK
    assert restored.npc_id == "npc-1"
    assert restored.message == "Hello"
    assert restored.channel == "say"


def test_npc_action_message_json_round_trip():
    msg = NPCActionMessage(action_type=NPCActionType.IDLE, npc_id="npc-3", timestamp=2.0)
    restored = NPCActionMessage.from_json(msg.to_json())
    assert restored.action_type == NPCActionType.IDLE
    assert restored.npc_id == "npc-3"


def test_npc_action_message_to_dict_uses_enum_value():
    msg = NPCActionMessage(action_type=NPCActionType.MOVE, npc_id="npc-2", timestamp=1.0, target_room="room-1")
    data = msg.to_dict()
    assert data["action_type"] == "move"
    assert data["target_room"] == "room-1"


def test_npc_message_queue_add_get_clear():
    queue = NPCMessageQueue(max_messages_per_npc=2)
    assert queue.add_message("npc-1", {"type": "ping"}) is True
    assert queue.get_queue_size("npc-1") == 1
    messages = queue.get_messages("npc-1")
    assert messages[0]["type"] == "ping"
    assert "timestamp" in messages[0]
    assert queue.clear_messages("npc-1") is True
    assert queue.get_queue_size("npc-1") == 0


def test_npc_message_queue_trims_oldest():
    queue = NPCMessageQueue(max_messages_per_npc=2)
    queue.add_message("npc-1", {"type": "a"})
    queue.add_message("npc-1", {"type": "b"})
    queue.add_message("npc-1", {"type": "c"})
    messages = queue.get_messages("npc-1")
    assert len(messages) == 2
    assert messages[0]["type"] == "b"
    assert queue.get_total_queue_size() == 2


@pytest.mark.asyncio
async def test_npc_thread_manager_start_stop():
    manager = NPCThreadManager()
    assert await manager.start() is True
    assert manager.is_running is True
    assert await manager.start() is True
    assert await manager.stop() is True
    assert manager.is_running is False
    assert await manager.stop() is True
    assert manager.get_active_npc_threads() == []


@pytest.mark.asyncio
async def test_npc_communication_bridge_messages():
    bridge = NPCCommunicationBridge()
    assert await bridge.send_message_to_npc("npc-1", {"type": "order"}) is True
    incoming = await bridge.get_messages_for_npc("npc-1")
    assert incoming[0]["target_npc"] == "npc-1"
    assert await bridge.receive_message_from_npc("npc-1", {"type": "reply"}) is True
    pending = await bridge.get_pending_messages()
    assert pending[0]["source_npc"] == "npc-1"
    assert await bridge.broadcast_to_all_npcs({"type": "alert"}) is True


@pytest.mark.asyncio
async def test_npc_thread_manager_start_stop_npc_thread():
    manager = NPCThreadManager()
    definition = MagicMock()
    definition.name = "Guard"
    assert await manager.start_npc_thread("npc-1", definition) is False
    assert await manager.start() is True
    with patch.object(manager, "_npc_thread_worker", new_callable=AsyncMock):
        assert await manager.start_npc_thread("npc-1", definition) is True
        assert manager.get_npc_definition("npc-1") is definition
        assert "npc-1" in manager.get_active_npc_threads()
        assert await manager.start_npc_thread("npc-1", definition) is True
        assert await manager.stop_npc_thread("npc-1") is True
        assert await manager.stop_npc_thread("missing") is True


@pytest.mark.asyncio
async def test_npc_thread_manager_restart_npc_thread():
    manager = NPCThreadManager()
    definition = MagicMock()
    definition.name = "Guard"
    await manager.start()
    with patch.object(manager, "_npc_thread_worker", new_callable=AsyncMock):
        await manager.start_npc_thread("npc-2", definition)
        assert await manager.restart_npc_thread("npc-2", definition) is True


@pytest.mark.asyncio
async def test_npc_thread_manager_stop_cancels_running_task():
    manager = NPCThreadManager()
    await manager.start()

    async def sleeper() -> None:
        await asyncio.sleep(5)

    task = asyncio.create_task(sleeper())
    manager.active_threads["npc-x"] = task
    manager.npc_definitions["npc-x"] = MagicMock()
    assert await manager.stop_npc_thread("npc-x") is True
    assert task.cancelled() or task.done()


@pytest.mark.asyncio
async def test_process_npc_message_dispatches_wander():
    manager = NPCThreadManager()
    with patch.object(manager, "_process_wander_action", new_callable=AsyncMock) as wander:
        await manager._process_npc_message("npc-1", {"action_type": "wander"})
        wander.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_npc_message_handles_errors():
    manager = NPCThreadManager()
    with patch.object(manager, "_process_wander_action", new_callable=AsyncMock, side_effect=RuntimeError("bad")):
        await manager._process_npc_message("npc-1", {"action_type": "wander"})


def test_npc_message_queue_add_message_failure():
    queue = NPCMessageQueue()
    with patch.object(queue, "pending_messages", create=True) as pending:
        pending.__getitem__ = MagicMock(side_effect=RuntimeError("broken"))
        assert queue.add_message("npc-1", {"type": "fail"}) is False


def test_npc_message_queue_clear_messages_failure():
    queue = NPCMessageQueue()
    queue.pending_messages["npc-1"] = [{"type": "x"}]
    with patch.object(queue, "_lock") as lock:
        lock.__enter__ = MagicMock(side_effect=RuntimeError("boom"))
        assert queue.clear_messages("npc-1") is False


@pytest.mark.asyncio
async def test_bridge_receive_message_failure():
    bridge = NPCCommunicationBridge()
    bad_message = MagicMock()
    bad_message.__setitem__ = MagicMock(side_effect=TypeError("immutable"))
    assert await bridge.receive_message_from_npc("npc-1", bad_message) is False


@pytest.mark.asyncio
async def test_bridge_broadcast_failure():
    bridge = NPCCommunicationBridge()
    bad_message = MagicMock()
    bad_message.__setitem__ = MagicMock(side_effect=TypeError("immutable"))
    assert await bridge.broadcast_to_all_npcs(bad_message) is False
