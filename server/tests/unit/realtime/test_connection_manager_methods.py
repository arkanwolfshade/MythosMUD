"""Unit tests for connection_manager_methods wrappers."""

# pyright: reportAny=false
# Reason: MagicMock fixture and nested mock attribute access; production code is Protocol-typed.

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.websockets import WebSocketState

from server.realtime import connection_manager_methods as cm_methods
from server.realtime import connection_websocket_close as ws_close


@pytest.fixture
def mock_manager() -> MagicMock:
    # ponytail: only stubs tests assert; async paths patch delegates themselves
    manager: MagicMock = MagicMock()
    manager.active_websockets = {"conn1": MagicMock(), "conn2": MagicMock()}
    manager.statistics_aggregator.get_memory_stats.return_value = {"total": 2}
    manager.statistics_aggregator.get_connection_stats.return_value = {"ws": 2}
    manager.statistics_aggregator.get_connection_health_stats.return_value = {"healthy": 2}
    manager.statistics_aggregator.get_memory_alerts.return_value = []
    manager.performance_tracker.get_stats.return_value = {"latency": 1}
    manager.error_handler = MagicMock()
    manager.error_handler.get_error_statistics.return_value = {"errors": 0}
    manager.rate_limiter.get_rate_limit_info.return_value = {"remaining": 10}
    return manager


def test_get_active_connection_count_impl(mock_manager: MagicMock) -> None:
    assert cm_methods.get_active_connection_count_impl(mock_manager) == 2


def test_get_memory_stats_impl(mock_manager: MagicMock) -> None:
    result = cm_methods.get_memory_stats_impl(mock_manager)
    assert result == {"total": 2}


def test_is_websocket_open_impl(mock_manager: MagicMock) -> None:
    ws: MagicMock = MagicMock()
    ws.application_state = WebSocketState.CONNECTED
    assert ws_close.is_websocket_open_impl(mock_manager, ws) is True
    ws.application_state = WebSocketState.DISCONNECTED
    assert ws_close.is_websocket_open_impl(mock_manager, ws) is False


def test_get_rate_limit_info_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    result = cm_methods.get_rate_limit_info_impl(mock_manager, player_id)
    assert result == {"remaining": 10}


def test_get_dual_connection_stats_impl(mock_manager: MagicMock) -> None:
    result = cm_methods.get_dual_connection_stats_impl(mock_manager)
    assert result == {"ws": 2}


def test_get_error_statistics_impl_no_handler() -> None:
    manager: MagicMock = MagicMock()
    manager.error_handler = None
    assert cm_methods.get_error_statistics_impl(manager) == {}


def test_get_performance_stats_impl(mock_manager: MagicMock) -> None:
    assert cm_methods.get_performance_stats_impl(mock_manager) == {"latency": 1}


def test_get_connection_health_stats_impl(mock_manager: MagicMock) -> None:
    assert cm_methods.get_connection_health_stats_impl(mock_manager) == {"healthy": 2}


def test_get_memory_alerts_impl(mock_manager: MagicMock) -> None:
    assert cm_methods.get_memory_alerts_impl(mock_manager) == []


def test_get_message_delivery_stats_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    get_delivery_stats: MagicMock = MagicMock(return_value={"sent": 1})
    personal_message_sender: MagicMock = MagicMock()
    personal_message_sender.get_delivery_stats = get_delivery_stats
    mock_manager.personal_message_sender = personal_message_sender
    mock_manager.player_websockets = {}
    result = cm_methods.get_message_delivery_stats_impl(mock_manager, player_id)
    assert result == {"sent": 1}


def test_get_player_presence_info_method(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.online_players = {player_id: {"player_id": str(player_id)}}
    mock_manager.player_websockets = {player_id: ["conn1"]}
    mock_manager.player_sessions = {player_id: "sess-1"}
    result = cm_methods.get_player_presence_info_method(mock_manager, player_id)
    assert str(result["player_id"]) == str(player_id)


def test_get_connection_count_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: ["conn1", "conn2"]}
    assert cm_methods.get_connection_count_impl(mock_manager, player_id) == {"websocket": 2, "total": 2}


def test_has_websocket_connection_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: ["conn1"]}
    assert cm_methods.has_websocket_connection_impl(mock_manager, player_id) is True
    assert cm_methods.has_websocket_connection_impl(mock_manager, uuid.uuid4()) is False


def test_get_next_sequence_impl(mock_manager: MagicMock) -> None:
    mock_manager.sequence_counter = 41
    assert cm_methods.get_next_sequence_impl(mock_manager) == 42


def test_get_pending_messages_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    get_messages: MagicMock = MagicMock(return_value=[{"text": "hi"}])
    message_queue: MagicMock = MagicMock()
    message_queue.get_messages = get_messages
    mock_manager.message_queue = message_queue
    assert cm_methods.get_pending_messages_impl(mock_manager, player_id) == [{"text": "hi"}]


def test_validate_session_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.player_sessions = {player_id: "sess-1"}
    assert cm_methods.validate_session_impl(mock_manager, player_id, "sess-1") is True
    assert cm_methods.validate_session_impl(mock_manager, player_id, "other") is False


def test_stop_health_checks_impl() -> None:
    stop_periodic_checks: MagicMock = MagicMock()
    health_monitor: MagicMock = MagicMock()
    health_monitor.stop_periodic_checks = stop_periodic_checks
    manager: MagicMock = MagicMock()
    manager.health_monitor = health_monitor
    cm_methods.stop_health_checks_impl(manager)
    stop_periodic_checks.assert_called_once()


def test_get_player_websocket_connection_id_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: ["ws-conn"]}
    assert cm_methods.get_player_websocket_connection_id_impl(mock_manager, player_id) == "ws-conn"


def test_get_online_players_impl_with_data(mock_manager: MagicMock) -> None:
    mock_manager.online_players = {uuid.uuid4(): {"name": "A"}}
    assert len(cm_methods.get_online_players_impl(mock_manager)) == 1


def test_get_player_session_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.player_sessions = {player_id: "sess-9"}
    assert cm_methods.get_player_session_impl(mock_manager, player_id) == "sess-9"


def test_convert_uuids_to_strings_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    result = cm_methods.convert_uuids_to_strings_impl(mock_manager, {"id": player_id})
    assert result == {"id": str(player_id)}


def test_get_session_connections_impl(mock_manager: MagicMock) -> None:
    mock_manager.session_connections = {"sess-1": ["c1", "c2"]}
    assert cm_methods.get_session_connections_impl(mock_manager, "sess-1") == ["c1", "c2"]


def test_validate_player_presence_method(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    with patch(
        "server.realtime.connection_manager_methods.validate_player_presence_impl",
        return_value={"valid": True},
    ):
        result = cm_methods.validate_player_presence_method(mock_manager, player_id)
    assert result == {"valid": True}


def test_get_online_player_by_display_name_method(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_manager_methods.get_online_player_by_display_name_impl",
        return_value={"name": "Alice"},
    ):
        result = cm_methods.get_online_player_by_display_name_method(mock_manager, "Alice")
    assert result == {"name": "Alice"}


@pytest.mark.asyncio
async def test_broadcast_to_room_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_delegates.delegate_message_broadcaster",
        new_callable=AsyncMock,
        return_value={"successful_deliveries": 1},
    ) as mock_delegate:
        result = await cm_methods.broadcast_to_room_impl(mock_manager, "room-1", {"type": "test"}, exclude_player=None)
    assert result == {"successful_deliveries": 1}
    mock_delegate.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_global_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_delegates.delegate_message_broadcaster",
        new_callable=AsyncMock,
        return_value={"total_players": 2},
    ):
        result = await cm_methods.broadcast_global_impl(mock_manager, {"type": "test"})
    assert result == {"total_players": 2}


@pytest.mark.asyncio
async def test_broadcast_room_event_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_manager_methods.broadcast_to_room_impl",
        new_callable=AsyncMock,
        return_value={"successful_deliveries": 1},
    ):
        result = await cm_methods.broadcast_room_event_impl(mock_manager, "room_update", "room-1", {"x": 1})
    assert result == {"successful_deliveries": 1}


@pytest.mark.asyncio
async def test_broadcast_global_event_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_manager_methods.broadcast_global_impl",
        new_callable=AsyncMock,
        return_value={"total_players": 3},
    ):
        result = await cm_methods.broadcast_global_event_impl(mock_manager, "global_update", {"x": 1})
    assert result == {"total_players": 3}


@pytest.mark.asyncio
async def test_disconnect_websocket_connection_impl_success(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    metadata: MagicMock = MagicMock(player_id=player_id, connection_type="websocket")
    mock_manager.connection_metadata = {"conn-1": metadata}
    mock_manager.disconnect_connection_by_id = AsyncMock(return_value=True)
    assert await cm_methods.disconnect_websocket_connection_impl(mock_manager, player_id, "conn-1") is True


@pytest.mark.asyncio
async def test_check_connection_health_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    check_player_connection_health: AsyncMock = AsyncMock(return_value={"ok": True})
    health_monitor: MagicMock = MagicMock()
    health_monitor.check_player_connection_health = check_player_connection_health
    mock_manager.health_monitor = health_monitor
    result = await cm_methods.check_connection_health_impl(mock_manager, player_id)
    assert result == {"ok": True}


@pytest.mark.asyncio
async def test_check_all_connections_health_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_delegates.delegate_health_monitor",
        new_callable=AsyncMock,
    ) as mock_delegate:
        await cm_methods.check_all_connections_health_impl(mock_manager)
    mock_delegate.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_personal_message_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    with patch(
        "server.realtime.connection_delegates.delegate_personal_message_sender",
        new_callable=AsyncMock,
        return_value={"success": True},
    ):
        result = await cm_methods.send_personal_message_impl(mock_manager, player_id, {"type": "msg"})
    assert result == {"success": True}


@pytest.mark.asyncio
async def test_get_player_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    player: MagicMock = MagicMock()
    with patch(
        "server.realtime.connection_delegates.delegate_game_state_provider",
        new_callable=AsyncMock,
        return_value=player,
    ):
        result = await cm_methods.get_player_impl(mock_manager, player_id)
    assert result is player


def test_start_health_checks_impl() -> None:
    manager: MagicMock = MagicMock()
    manager.health_monitor = MagicMock()
    with patch("server.realtime.connection_delegates.delegate_health_monitor_sync") as mock_sync:
        cm_methods.start_health_checks_impl(manager)
    mock_sync.assert_called_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_events_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_event_helpers.subscribe_to_room_events_impl",
        new_callable=AsyncMock,
    ) as mock_sub:
        await cm_methods.subscribe_to_room_events_impl(mock_manager)
    mock_sub.assert_awaited_once_with(mock_manager)


def test_get_npcs_batch_impl(mock_manager: MagicMock) -> None:
    mock_manager.game_state_provider = MagicMock()
    with patch(
        "server.realtime.connection_delegates.delegate_game_state_provider_sync",
        return_value={"npc_1": "Guard"},
    ):
        result = cm_methods.get_npcs_batch_impl(mock_manager, ["npc_1"])
    assert result == {"npc_1": "Guard"}


@pytest.mark.asyncio
async def test_get_room_occupants_impl(mock_manager: MagicMock) -> None:
    mock_manager.game_state_provider = MagicMock()
    mock_manager.online_players = {}
    with patch(
        "server.realtime.connection_delegates.delegate_game_state_provider",
        new_callable=AsyncMock,
        return_value=[{"player_name": "Alice"}],
    ):
        result = await cm_methods.get_room_occupants_impl(mock_manager, "room-1")
    assert result == [{"player_name": "Alice"}]


@pytest.mark.asyncio
async def test_get_players_batch_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_manager.game_state_provider = MagicMock()
    with patch(
        "server.realtime.connection_delegates.delegate_game_state_provider",
        new_callable=AsyncMock,
        return_value={player_id: MagicMock()},
    ):
        result = await cm_methods.get_players_batch_impl(mock_manager, [player_id])
    assert player_id in result


def test_get_connection_id_from_websocket_impl(mock_manager: MagicMock) -> None:
    ws: MagicMock = MagicMock()
    mock_manager.active_websockets = {"conn-abc": ws}
    assert cm_methods.get_connection_id_from_websocket_impl(mock_manager, ws) == "conn-abc"
    assert cm_methods.get_connection_id_from_websocket_impl(mock_manager, MagicMock()) is None


def test_get_error_statistics_impl_with_handler(mock_manager: MagicMock) -> None:
    result = cm_methods.get_error_statistics_impl(mock_manager)
    assert result == {"errors": 0}


@pytest.mark.asyncio
async def test_safe_close_websocket_impl(mock_manager: MagicMock) -> None:
    ws: AsyncMock = AsyncMock()
    ws.application_state = WebSocketState.CONNECTED
    is_websocket_closed: MagicMock = MagicMock(return_value=False)
    mock_manager.is_websocket_closed = is_websocket_closed
    await ws_close.safe_close_websocket_impl(mock_manager, ws, code=1000, reason="bye")
    ws.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_to_room_impl(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    subscribe_to_room: MagicMock = MagicMock(return_value=True)
    room_manager: MagicMock = MagicMock()
    room_manager.subscribe_to_room = subscribe_to_room
    canonical_room_id: MagicMock = MagicMock(return_value="room-1")
    mock_manager.canonical_room_id = canonical_room_id
    mock_manager.room_manager = room_manager
    await cm_methods.subscribe_to_room_impl(mock_manager, player_id, "room-1")
    subscribe_to_room.assert_called_once_with(str(player_id), "room-1")


@pytest.mark.asyncio
async def test_unsubscribe_from_room_events_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_event_helpers.unsubscribe_from_room_events_impl",
        new_callable=AsyncMock,
    ) as mock_unsub:
        await cm_methods.unsubscribe_from_room_events_impl(mock_manager)
    mock_unsub.assert_awaited_once_with(mock_manager)


@pytest.mark.asyncio
async def test_handle_player_entered_room_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_delegates.delegate_room_event_handler",
        new_callable=AsyncMock,
    ) as mock_handler:
        await cm_methods.handle_player_entered_room_impl(mock_manager, {"room_id": "room-1"})
    mock_handler.assert_awaited_once()


@pytest.mark.asyncio
async def test_periodic_health_check_impl(mock_manager: MagicMock) -> None:
    with patch(
        "server.realtime.connection_delegates.delegate_health_monitor",
        new_callable=AsyncMock,
    ) as mock_delegate:
        await cm_methods.periodic_health_check_impl(mock_manager)
    mock_delegate.assert_awaited_once()
