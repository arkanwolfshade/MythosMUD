"""Tests for the posture command handlers (sit/stand/lie)."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.position_commands import (
    handle_lie_command,
    handle_sit_command,
    handle_stand_command,
)
from server.models.alias import Alias


@pytest.fixture
def mock_request():
    """Create a request object with mocked app state."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()

    connection_manager = MagicMock()
    connection_manager.broadcast_to_room = AsyncMock(return_value={})
    connection_manager.send_personal_message = AsyncMock(return_value={})
    connection_manager._get_next_sequence = MagicMock(return_value=1)
    connection_manager.online_players = {}
    connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)
    request.app.state.connection_manager = connection_manager
    return request


@pytest.fixture
def mock_player():
    """Create a mock player with baseline stats."""
    player = MagicMock()
    player.player_id = "player-123"
    player.name = "TestPlayer"
    player.current_room_id = "room-001"
    player.get_stats.return_value = {"position": "standing"}
    return player


@pytest.fixture
def baseline_alias_storage():
    """Provide an alias storage mock with no existing aliases."""
    alias_storage = MagicMock()
    alias_storage.get_alias.side_effect = [None, None, None]
    return alias_storage


@pytest.mark.asyncio
async def test_sit_command_updates_persistence_and_connection(mock_request, mock_player, baseline_alias_storage):
    """Sit command should persist position changes and update live tracking."""
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

    result = await handle_sit_command(
        command_data={"command_type": "sit", "args": []},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=baseline_alias_storage,
        player_name="TestPlayer",
    )

    mock_player.set_stats.assert_called_once()
    updated_stats = mock_player.set_stats.call_args.args[0]
    assert updated_stats["position"] == "sitting"
    mock_request.app.state.persistence.save_player.assert_called_once_with(mock_player)

    online_entry = mock_request.app.state.connection_manager.online_players["player-123"]
    assert online_entry["position"] == "sitting"

    assert result["result"] == "You settle into a seated position."
    assert result["position"] == "sitting"
    assert result["changed"] is True
    assert "seated" in (result["room_message"] or "")
    assert result["suppress_chat"] is True
    assert result["game_log_message"] == "You settle into a seated position."
    assert result["game_log_channel"] == "game-log"
    assert result["player_update"]["position"] == "sitting"
    assert result["player_update"]["previous_position"] == "standing"

    alias_calls = {call.args[1] for call in baseline_alias_storage.create_alias.call_args_list}
    assert alias_calls == {"sit", "stand", "lie"}
    alias_command_values = {call.args[2] for call in baseline_alias_storage.create_alias.call_args_list}
    assert alias_command_values == {"/sit", "/stand", "/lie"}

    broadcast_mock = mock_request.app.state.connection_manager.broadcast_to_room
    broadcast_mock.assert_awaited_once()
    room_arg, event_arg = broadcast_mock.await_args.args[:2]
    assert room_arg == "room-001"
    assert event_arg["event_type"] == "player_posture_change"
    assert event_arg["data"]["position"] == "sitting"
    assert "seated" in event_arg["data"]["message"]
    assert broadcast_mock.await_args.kwargs["exclude_player"] == "player-123"
    assert result["room_message"] == event_arg["data"]["message"]


@pytest.mark.asyncio
async def test_stand_command_no_change_skips_persistence(mock_request, mock_player):
    """Stand command should be a no-op when already standing."""
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

    alias_storage = MagicMock()
    alias_storage.get_alias.side_effect = [
        Alias(name="sit", command="/sit"),
        Alias(name="stand", command="/stand"),
        Alias(name="lie", command="/lie"),
    ]

    result = await handle_stand_command(
        command_data={"command_type": "stand", "args": []},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=alias_storage,
        player_name="TestPlayer",
    )

    mock_player.set_stats.assert_not_called()
    mock_request.app.state.persistence.save_player.assert_not_called()
    assert result["result"] == "You are already standing."
    assert result["position"] == "standing"
    assert result["changed"] is False
    assert result["room_message"] is None
    assert result["suppress_chat"] is True
    assert result["game_log_message"] == "You are already standing."
    assert result["game_log_channel"] == "game-log"
    assert result["player_update"] is None
    assert alias_storage.create_alias.call_count == 0
    broadcast_mock = mock_request.app.state.connection_manager.broadcast_to_room
    assert broadcast_mock.await_count == 0


@pytest.mark.asyncio
async def test_lie_command_accepts_down_modifier(mock_request, mock_player, baseline_alias_storage):
    """Lie command should accept the optional 'down' modifier."""
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.persistence.get_player_by_name.return_value = mock_player

    result = await handle_lie_command(
        command_data={"command_type": "lie", "args": ["down"], "modifier": "down"},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=baseline_alias_storage,
        player_name="TestPlayer",
    )

    mock_player.set_stats.assert_called()
    updated_stats = mock_player.set_stats.call_args.args[0]
    assert updated_stats["position"] == "lying"
    mock_request.app.state.persistence.save_player.assert_called_once_with(mock_player)
    assert result["result"] == "You stretch out and lie down."
    assert result["position"] == "lying"
    assert result["changed"] is True
    assert "lies" in (result["room_message"] or "")
    assert result["suppress_chat"] is True
    assert result["game_log_message"] == "You stretch out and lie down."
    assert result["game_log_channel"] == "game-log"
    assert result["player_update"]["position"] == "lying"
    assert result["player_update"]["previous_position"] == "standing"

    broadcast_mock = mock_request.app.state.connection_manager.broadcast_to_room
    broadcast_mock.assert_awaited_once()
    room_arg, event_arg = broadcast_mock.await_args.args[:2]
    assert room_arg == "room-001"
    assert event_arg["event_type"] == "player_posture_change"
    assert event_arg["data"]["position"] == "lying"
    assert "lies" in event_arg["data"]["message"]
    assert broadcast_mock.await_args.kwargs["exclude_player"] == "player-123"


@pytest.mark.asyncio
async def test_position_command_handles_missing_persistence(mock_request, baseline_alias_storage):
    """Commands should degrade gracefully when persistence is unavailable."""
    mock_request.app.state.persistence = None

    result = await handle_sit_command(
        command_data={"command_type": "sit", "args": []},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        alias_storage=baseline_alias_storage,
        player_name="TestPlayer",
    )

    assert result["result"] == "Position changes are currently unavailable."
    assert result["position"] == "sitting"
    assert result["changed"] is False
    assert result["room_message"] is None
    assert result["suppress_chat"] is True
    assert result["game_log_message"] == "Position changes are currently unavailable."
    assert result["game_log_channel"] == "game-log"
    assert result["player_update"] is None
    broadcast_mock = mock_request.app.state.connection_manager.broadcast_to_room
    assert broadcast_mock.await_count == 0
