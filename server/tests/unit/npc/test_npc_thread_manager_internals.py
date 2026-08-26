"""
Unit tests for NPCThreadManager/NPCCommunicationBridge branches that
test_npc_threading_messages.py doesn't reach (its tests always patch
_npc_thread_worker/_process_wander_action away rather than exercising them).
"""

# pyright: reportPrivateUsage=false
# Reason: unit tests call NPCThreadManager's protected helpers directly.

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.npc import threading as npc_threading_module
from server.npc.threading import NPCCommunicationBridge, NPCThreadManager


@pytest.mark.asyncio
async def test_start_swallows_unexpected_exception() -> None:
    """start() catches an unexpected exception (e.g. logging failure) and returns False."""
    manager = NPCThreadManager()
    with patch.object(npc_threading_module.logger, "info", side_effect=RuntimeError("logger down")):
        assert await manager.start() is False


@pytest.mark.asyncio
async def test_stop_swallows_unexpected_exception() -> None:
    """stop() catches an unexpected exception and returns False."""
    manager = NPCThreadManager()
    manager.is_running = True
    with patch.object(npc_threading_module.logger, "info", side_effect=RuntimeError("logger down")):
        assert await manager.stop() is False


@pytest.mark.asyncio
async def test_stop_cancels_active_threads_via_gather() -> None:
    """stop() gathers _stop_npc_thread_internal() for every not-done active thread."""
    manager = NPCThreadManager()
    manager.is_running = True

    async def sleeper() -> None:
        await asyncio.sleep(5)

    task = asyncio.create_task(sleeper())
    manager.active_threads["npc-1"] = task
    manager.npc_definitions["npc-1"] = MagicMock()

    assert await manager.stop() is True
    assert manager.active_threads == {}
    assert manager.npc_definitions == {}


@pytest.mark.asyncio
async def test_stop_npc_thread_swallows_unexpected_exception() -> None:
    """stop_npc_thread() catches an unexpected exception from the internal stop and returns False."""
    manager = NPCThreadManager()
    with patch.object(manager, "_stop_npc_thread_internal", new_callable=AsyncMock, side_effect=RuntimeError("boom")):
        assert await manager.stop_npc_thread("npc-1") is False


@pytest.mark.asyncio
async def test_restart_npc_thread_swallows_unexpected_exception() -> None:
    """restart_npc_thread() catches an unexpected exception and returns False."""
    manager = NPCThreadManager()
    with patch.object(manager, "stop_npc_thread", new_callable=AsyncMock, side_effect=RuntimeError("boom")):
        assert await manager.restart_npc_thread("npc-1", MagicMock()) is False


@pytest.mark.asyncio
async def test_worker_processes_message_and_executes_behavior_then_stops() -> None:
    """_npc_thread_worker drains pending messages and calls _execute_npc_behavior each iteration."""
    manager = NPCThreadManager()
    manager.is_running = True
    manager.active_threads["npc-1"] = MagicMock()
    _ = manager.message_queue.add_message("npc-1", {"type": "test"})

    async def fake_execute_behavior(npc_id: str, definition: object) -> None:
        del npc_id, definition
        manager.is_running = False  # stop the loop after one iteration

    with (
        patch.object(manager, "_process_npc_message", new_callable=AsyncMock) as process_msg,
        patch.object(manager, "_execute_npc_behavior", side_effect=fake_execute_behavior) as execute_behavior,
    ):
        await manager._npc_thread_worker("npc-1", MagicMock())

    process_msg.assert_awaited_once()
    execute_behavior.assert_awaited_once()
    assert manager.message_queue.get_messages("npc-1") == []


@pytest.mark.asyncio
async def test_worker_handles_unexpected_exception() -> None:
    """_npc_thread_worker logs and exits gracefully on an unexpected exception."""
    manager = NPCThreadManager()
    manager.is_running = True
    manager.active_threads["npc-1"] = MagicMock()

    with patch.object(manager, "_execute_npc_behavior", new_callable=AsyncMock, side_effect=RuntimeError("boom")):
        await manager._npc_thread_worker("npc-1", MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_worker_stops_cleanly_on_cancellation() -> None:
    """_npc_thread_worker catches CancelledError and exits via its finally block."""
    manager = NPCThreadManager()
    manager.is_running = True
    manager.active_threads["npc-1"] = MagicMock()

    with patch.object(manager, "_execute_npc_behavior", new_callable=AsyncMock):
        task = asyncio.create_task(manager._npc_thread_worker("npc-1", MagicMock()))
        await asyncio.sleep(0)
        _ = task.cancel()
        await task  # the worker catches CancelledError internally and completes cleanly
    assert task.cancelled() is False


def test_resolve_wander_npc_no_instance_service() -> None:
    """_resolve_wander_npc returns None when the instance service is unavailable."""
    manager = NPCThreadManager()
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        assert manager._resolve_wander_npc("npc-1") is None


def test_resolve_wander_npc_not_in_active_npcs() -> None:
    """_resolve_wander_npc returns None when the NPC isn't tracked by the lifecycle manager."""
    manager = NPCThreadManager()
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        assert manager._resolve_wander_npc("npc-1") is None


def test_resolve_wander_npc_no_definition() -> None:
    """_resolve_wander_npc returns None when there's no tracked NPCDefinition for the id."""
    manager = NPCThreadManager()
    mock_instance = MagicMock()
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {"npc-1": mock_instance}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        assert manager._resolve_wander_npc("npc-1") is None


def test_resolve_wander_npc_success() -> None:
    """_resolve_wander_npc returns (instance, definition) when everything is resolvable."""
    manager = NPCThreadManager()
    mock_instance = MagicMock()
    mock_definition = MagicMock()
    manager.npc_definitions["npc-1"] = mock_definition
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {"npc-1": mock_instance}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        result = manager._resolve_wander_npc("npc-1")
    assert result == (mock_instance, mock_definition)


def test_parse_behavior_config_dict_attr() -> None:
    """_parse_behavior_config returns the dict attribute directly when it's already a dict."""
    instance = MagicMock()
    instance._behavior_config = {"wander_chance": 0.5}
    assert NPCThreadManager._parse_behavior_config(instance) == {"wander_chance": 0.5}


def test_parse_behavior_config_valid_json_string() -> None:
    """_parse_behavior_config parses a JSON-string attribute into a dict."""
    instance = MagicMock()
    instance._behavior_config = '{"wander_chance": 0.25}'
    assert NPCThreadManager._parse_behavior_config(instance) == {"wander_chance": 0.25}


def test_parse_behavior_config_invalid_json_string() -> None:
    """_parse_behavior_config returns {} for a malformed JSON string."""
    instance = MagicMock()
    instance._behavior_config = "{not valid json"
    assert NPCThreadManager._parse_behavior_config(instance) == {}


def test_parse_behavior_config_json_non_dict() -> None:
    """_parse_behavior_config returns {} when the JSON string decodes to a non-dict."""
    instance = MagicMock()
    instance._behavior_config = "[1, 2, 3]"
    assert NPCThreadManager._parse_behavior_config(instance) == {}


def test_execute_wander_movement_no_async_persistence_logs_and_returns() -> None:
    """_execute_wander_movement returns early when the container has no async_persistence."""
    manager = NPCThreadManager()
    mock_container = MagicMock()
    mock_container.async_persistence = None
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        manager._execute_wander_movement("npc-1", MagicMock(), MagicMock())  # must not raise


def test_execute_wander_movement_success_updates_last_movement_time() -> None:
    """_execute_wander_movement records the movement timestamp when the handler reports success."""
    manager = NPCThreadManager()
    mock_container = MagicMock()
    npc_instance = MagicMock()
    npc_instance._last_idle_movement_time = 0.0

    with (
        patch("server.container.ApplicationContainer.get_instance", return_value=mock_container),
        patch("server.npc.idle_movement.IdleMovementHandler") as handler_cls,
    ):
        handler_cls.return_value.execute_idle_movement.return_value = True
        manager._execute_wander_movement("npc-1", npc_instance, MagicMock())

    assert npc_instance._last_idle_movement_time > 0.0


def test_execute_wander_movement_no_movement_performed() -> None:
    """_execute_wander_movement logs (not raises) when the handler reports no movement occurred."""
    manager = NPCThreadManager()
    mock_container = MagicMock()

    with (
        patch("server.container.ApplicationContainer.get_instance", return_value=mock_container),
        patch("server.npc.idle_movement.IdleMovementHandler") as handler_cls,
    ):
        handler_cls.return_value.execute_idle_movement.return_value = False
        manager._execute_wander_movement("npc-1", MagicMock(), MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_process_wander_action_returns_early_when_unresolved() -> None:
    """_process_wander_action returns without executing movement when resolution fails."""
    manager = NPCThreadManager()
    with (
        patch.object(manager, "_resolve_wander_npc", return_value=None),
        patch.object(manager, "_execute_wander_movement") as execute_movement,
    ):
        await manager._process_wander_action("npc-1", {})
    execute_movement.assert_not_called()


@pytest.mark.asyncio
async def test_process_wander_action_handles_unexpected_exception() -> None:
    """_process_wander_action logs and swallows an unexpected exception from resolution."""
    manager = NPCThreadManager()
    with patch.object(manager, "_resolve_wander_npc", side_effect=RuntimeError("boom")):
        await manager._process_wander_action("npc-1", {})  # must not raise


@pytest.mark.asyncio
async def test_execute_npc_behavior_no_instance_service() -> None:
    """_execute_npc_behavior returns early when the instance service is unavailable."""
    manager = NPCThreadManager()
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        await manager._execute_npc_behavior("npc-1", MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_execute_npc_behavior_npc_not_active() -> None:
    """_execute_npc_behavior returns early when the NPC isn't in the lifecycle manager's active set."""
    manager = NPCThreadManager()
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        await manager._execute_npc_behavior("npc-1", MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_execute_npc_behavior_success() -> None:
    """_execute_npc_behavior awaits the resolved NPC instance's execute_behavior()."""
    manager = NPCThreadManager()
    npc_instance = MagicMock()
    npc_instance.execute_behavior = AsyncMock(return_value=None)
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {"npc-1": npc_instance}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        await manager._execute_npc_behavior("npc-1", MagicMock())
    npc_instance.execute_behavior.assert_awaited_once()


@pytest.mark.asyncio
async def test_execute_npc_behavior_swallows_inner_execute_error() -> None:
    """_execute_npc_behavior's inner try/except catches execute_behavior() raising."""
    manager = NPCThreadManager()
    npc_instance = MagicMock()
    npc_instance.execute_behavior = AsyncMock(side_effect=RuntimeError("behavior crashed"))
    mock_service = MagicMock()
    mock_service.lifecycle_manager.active_npcs = {"npc-1": npc_instance}
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=mock_service):
        await manager._execute_npc_behavior("npc-1", MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_execute_npc_behavior_swallows_outer_unexpected_exception() -> None:
    """_execute_npc_behavior's outer try/except catches a failure looking up the instance service."""
    manager = NPCThreadManager()
    with patch(
        "server.services.npc_instance_service.get_npc_instance_service", side_effect=RuntimeError("service down")
    ):
        await manager._execute_npc_behavior("npc-1", MagicMock())  # must not raise


@pytest.mark.asyncio
async def test_bridge_send_message_to_npc_swallows_exception() -> None:
    """send_message_to_npc() catches an exception (e.g. an immutable message) and returns False."""
    bridge = NPCCommunicationBridge()
    bad_message: MagicMock = MagicMock()
    bad_message.__setitem__ = MagicMock(side_effect=TypeError("immutable"))
    assert await bridge.send_message_to_npc("npc-1", bad_message) is False
