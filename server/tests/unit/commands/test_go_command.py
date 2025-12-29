"""
Unit tests for go command handler.

Tests the go command for player movement.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.go_command import (
    _execute_movement,
    _setup_go_command,
    _validate_exit,
    _validate_player_posture,
    handle_go_command,
)


@pytest.mark.asyncio
async def test_setup_go_command_no_persistence():
    """Test _setup_go_command returns None when no persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await _setup_go_command(mock_request, {}, "testplayer")

    assert result is None


@pytest.mark.asyncio
async def test_setup_go_command_player_not_found():
    """Test _setup_go_command returns None when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await _setup_go_command(mock_request, {"username": "testuser"}, "testplayer")

    assert result is None


@pytest.mark.asyncio
async def test_setup_go_command_room_not_found():
    """Test _setup_go_command returns None when room not found."""
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await _setup_go_command(mock_request, {"username": "testuser"}, "testplayer")

    assert result is None


@pytest.mark.asyncio
async def test_setup_go_command_success():
    """Test _setup_go_command returns setup tuple on success."""
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_room = MagicMock()
    mock_room.id = "test_room"
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await _setup_go_command(mock_request, {"username": "testuser"}, "testplayer")

    assert result is not None
    app, persistence, player, room, room_id = result
    assert app == mock_app
    assert persistence == mock_persistence
    assert player == mock_player
    assert room == mock_room
    assert room_id == "test_room"


@pytest.mark.asyncio
async def test_setup_go_command_room_id_mismatch():
    """Test _setup_go_command corrects room ID mismatch."""
    mock_player = MagicMock()
    mock_player.current_room_id = "player_room_id"
    mock_room = MagicMock()
    mock_room.id = "room_object_id"
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await _setup_go_command(mock_request, {"username": "testuser"}, "testplayer")

    assert result is not None
    _, _, _, _, room_id = result
    assert room_id == "room_object_id"  # Should use room object's ID


def test_validate_player_posture_standing():
    """Test _validate_player_posture returns True for standing player."""
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})

    valid, message = _validate_player_posture(mock_player, "testplayer", "test_room")

    assert valid is True
    assert message == ""


def test_validate_player_posture_sitting():
    """Test _validate_player_posture returns False for sitting player."""
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})

    valid, message = _validate_player_posture(mock_player, "testplayer", "test_room")

    assert valid is False
    assert "stand up" in message.lower()


def test_validate_player_posture_lying():
    """Test _validate_player_posture returns False for lying player."""
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(return_value={"position": "lying"})

    valid, message = _validate_player_posture(mock_player, "testplayer", "test_room")

    assert valid is False
    assert "stand up" in message.lower()


def test_validate_player_posture_no_get_stats():
    """Test _validate_player_posture handles player without get_stats."""
    mock_player = MagicMock()
    del mock_player.get_stats

    valid, message = _validate_player_posture(mock_player, "testplayer", "test_room")

    assert valid is True  # Defaults to standing
    assert message == ""


def test_validate_player_posture_get_stats_error():
    """Test _validate_player_posture handles get_stats errors."""
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(side_effect=AttributeError("Test error"))

    valid, message = _validate_player_posture(mock_player, "testplayer", "test_room")

    assert valid is True  # Defaults to standing on error
    assert message == ""


def test_validate_exit_no_exits():
    """Test _validate_exit returns None when room has no exits."""
    mock_room = MagicMock()
    mock_room.exits = None
    mock_persistence = MagicMock()

    result = _validate_exit("north", mock_room, mock_persistence, "testplayer", "test_room")

    assert result is None


def test_validate_exit_direction_not_found():
    """Test _validate_exit returns None when direction not in exits."""
    mock_room = MagicMock()
    mock_room.exits = {"south": "south_room"}
    mock_persistence = MagicMock()

    result = _validate_exit("north", mock_room, mock_persistence, "testplayer", "test_room")

    assert result is None


def test_validate_exit_target_room_not_found():
    """Test _validate_exit returns None when target room doesn't exist."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "north_room"}
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=None)

    result = _validate_exit("north", mock_room, mock_persistence, "testplayer", "test_room")

    assert result is None


def test_validate_exit_success():
    """Test _validate_exit returns target room ID on success."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "north_room"}
    mock_target_room = MagicMock()
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_target_room)

    result = _validate_exit("north", mock_room, mock_persistence, "testplayer", "test_room")

    assert result == "north_room"


@pytest.mark.asyncio
async def test_execute_movement_success():
    """Test _execute_movement successfully moves player."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_movement_service = MagicMock()
    mock_movement_service.move_player = AsyncMock(return_value=True)

    mock_state = MagicMock()
    mock_state.container = MagicMock()
    mock_state.container.movement_service = mock_movement_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_persistence = MagicMock()

    result = await _execute_movement(
        mock_player, "test_room", "target_room", mock_app, mock_persistence, "testplayer", "north"
    )

    assert result["room_changed"] is True
    assert result["room_id"] == "target_room"
    assert "go north" in result["result"].lower()
    mock_movement_service.move_player.assert_awaited_once_with("test-player-id", "test_room", "target_room")


@pytest.mark.asyncio
async def test_execute_movement_failure():
    """Test _execute_movement handles movement failure."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_movement_service = MagicMock()
    mock_movement_service.move_player = AsyncMock(return_value=False)

    mock_state = MagicMock()
    mock_state.container = MagicMock()
    mock_state.container.movement_service = mock_movement_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_persistence = MagicMock()

    result = await _execute_movement(
        mock_player, "test_room", "target_room", mock_app, mock_persistence, "testplayer", "north"
    )

    assert "can't go that way" in result["result"].lower()


@pytest.mark.asyncio
async def test_execute_movement_error_handling():
    """Test _execute_movement handles errors gracefully."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    mock_movement_service = MagicMock()
    mock_movement_service.move_player = AsyncMock(side_effect=ValueError("Test error"))

    mock_state = MagicMock()
    mock_state.container = MagicMock()
    mock_state.container.movement_service = mock_movement_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_persistence = MagicMock()

    result = await _execute_movement(
        mock_player, "test_room", "target_room", mock_app, mock_persistence, "testplayer", "north"
    )

    assert "Error" in result["result"]


@pytest.mark.asyncio
async def test_execute_movement_fallback_service():
    """Test _execute_movement uses fallback service when container not available."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"

    mock_state = MagicMock()
    del mock_state.container  # No container
    mock_state.event_bus = MagicMock()
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_persistence = MagicMock()

    with patch("server.commands.go_command.MovementService") as mock_service_class:
        mock_service_instance = MagicMock()
        mock_service_instance.move_player = AsyncMock(return_value=True)
        mock_service_class.return_value = mock_service_instance

        result = await _execute_movement(
            mock_player, "test_room", "target_room", mock_app, mock_persistence, "testplayer", "north"
        )

        assert result["room_changed"] is True
        mock_service_class.assert_called_once()


@pytest.mark.asyncio
async def test_handle_go_command_no_direction():
    """Test handle_go_command returns error when no direction."""
    command_data = {}
    mock_request = MagicMock()

    result = await handle_go_command(command_data, {}, mock_request, None, "testplayer")

    assert "Go where" in result["result"]


@pytest.mark.asyncio
async def test_handle_go_command_setup_failure():
    """Test handle_go_command handles setup failure."""
    command_data = {"direction": "north"}
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_go_command(command_data, {}, mock_request, None, "testplayer")

    assert "can't go that way" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_go_command_invalid_posture():
    """Test handle_go_command blocks movement when player not standing."""
    command_data = {"direction": "north"}
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_room = MagicMock()
    mock_room.id = "test_room"
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await handle_go_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")

    assert "stand up" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_go_command_no_exit():
    """Test handle_go_command returns error when exit doesn't exist."""
    command_data = {"direction": "north"}
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})
    mock_room = MagicMock()
    mock_room.id = "test_room"
    mock_room.exits = {}
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await handle_go_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")

    assert "can't go that way" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_go_command_success():
    """Test handle_go_command successfully moves player."""
    command_data = {"direction": "north"}
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.player_id = "test-player-id"
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})
    mock_room = MagicMock()
    mock_room.id = "test_room"
    mock_room.exits = {"north": "north_room"}
    mock_target_room = MagicMock()
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(side_effect=lambda rid: mock_target_room if rid == "north_room" else mock_room)

    mock_movement_service = MagicMock()
    mock_movement_service.move_player = AsyncMock(return_value=True)
    mock_state = MagicMock()
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.movement_service = mock_movement_service
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app

    result = await handle_go_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")

    assert result["room_changed"] is True
    assert result["room_id"] == "north_room"
