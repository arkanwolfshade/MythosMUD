"""Unit tests for ConnectionManager class delegates and lazy __getattr__."""

from __future__ import annotations

import importlib
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.websockets import WebSocketState

from server.realtime.connection_manager import ConnectionManager


@pytest.fixture
def manager() -> ConnectionManager:
    with (
        patch("server.realtime.connection_manager.initialize_health_monitor"),
        patch("server.realtime.connection_manager.initialize_connection_cleaner"),
    ):
        return ConnectionManager()


def test_connection_manager_init_sets_components(manager: ConnectionManager) -> None:
    assert manager.sequence_counter >= 0
    assert manager.rate_limiter is not None
    assert manager.message_queue is not None


def test_websocket_lifecycle_helpers(manager: ConnectionManager) -> None:
    ws = MagicMock()
    ws.client_state = WebSocketState.CONNECTED
    assert manager._is_websocket_open(ws) is True
    manager.mark_websocket_closed(42)
    assert manager.is_websocket_closed(42) is True
    assert manager.get_closed_websockets_count() >= 1


@pytest.mark.asyncio
async def test_safe_close_websocket(manager: ConnectionManager) -> None:
    ws = MagicMock()
    ws.client_state = WebSocketState.CONNECTED
    ws.close = AsyncMock()
    await manager._safe_close_websocket(ws)
    ws.close.assert_awaited_once()


def test_player_connection_lookup_helpers(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    assert manager.get_player_websocket_connection_id(player_id) is None
    assert manager.has_websocket_connection(player_id) is False
    counts = manager.get_connection_count(player_id)
    assert isinstance(counts, dict)


@pytest.mark.asyncio
async def test_room_subscription_delegates(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    await manager.subscribe_to_room(player_id, "room_001")
    await manager.unsubscribe_from_room(player_id, "room_001")
    assert manager.canonical_room_id("room_001") is not None


def test_set_async_persistence_and_services(manager: ConnectionManager) -> None:
    persistence = MagicMock()
    manager.set_async_persistence(persistence)
    assert manager.async_persistence is persistence
    bus = MagicMock()
    manager.set_event_bus(bus)
    assert manager.event_bus is bus
    combat = MagicMock()
    manager.set_player_combat_service(combat)


@pytest.mark.asyncio
async def test_disconnect_and_session_delegates(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    await manager.disconnect_websocket(player_id)
    await manager.force_disconnect_player(player_id)
    assert manager.get_player_session(player_id) is None
    assert manager.get_session_connections("missing") == []
    assert manager.validate_session(player_id, "sess") is False


def test_stats_and_rate_limit_delegates(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    manager.mark_player_seen(player_id)
    assert isinstance(manager.get_rate_limit_info(player_id), dict)
    assert isinstance(manager.get_memory_stats(), dict)
    assert isinstance(manager.get_performance_stats(), dict)
    assert isinstance(manager.get_connection_health_stats(), dict)
    assert isinstance(manager.get_dual_connection_stats(), dict)
    assert isinstance(manager.get_memory_alerts(), list)
    assert isinstance(manager.get_error_statistics(), dict)
    assert isinstance(manager.get_presence_statistics(), dict)
    assert manager.get_active_connection_count() >= 0


@pytest.mark.asyncio
async def test_broadcast_and_health_delegates(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    event = {"type": "test"}
    await manager.broadcast_to_room("room_1", event)
    await manager.broadcast_global(event)
    await manager.broadcast_room_event("room_update", "room_1", {"x": 1})
    await manager.broadcast_global_event("global_update", {"y": 2})
    await manager.check_connection_health(player_id)
    await manager.cleanup_dead_connections(player_id)
    await manager.cleanup_orphaned_data()
    await manager.force_cleanup()


def test_presence_and_online_helpers(manager: ConnectionManager) -> None:
    player_id = uuid.uuid4()
    assert isinstance(manager.get_player_presence_info(player_id), dict)
    assert isinstance(manager.validate_player_presence(player_id), dict)
    assert isinstance(manager.get_online_players(), list)
    assert manager.get_online_player_by_display_name("Nobody") is None
    assert manager._get_next_sequence() >= 0


def test_connection_manager_getattr_lazy_api_exports() -> None:
    mod = importlib.import_module("server.realtime.connection_manager")
    assert callable(mod.__getattr__("send_game_event"))
    assert callable(mod.__getattr__("broadcast_game_event"))
    with pytest.raises(AttributeError):
        _ = mod.__getattr__("not_exported")
