"""
Unit tests for rest command handlers.

Tests the rest command functionality including combat blocking,
rest location instant disconnect, countdown, and interruption logic.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rest_command import (
    _cancel_rest_countdown,
    _check_player_in_combat,
    _check_rest_location,
    _disconnect_player_intentionally,
    _start_rest_countdown,
    handle_rest_command,
    is_player_resting,
)


@pytest.fixture
def mock_app():
    """Create a mock FastAPI app."""
    app = MagicMock()
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_request(mock_app):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Create a mock request."""
    request = MagicMock()
    request.app = mock_app
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.resting_players = {}
    manager.intentional_disconnects = set()
    manager.force_disconnect_player = AsyncMock()
    return manager


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "TestPlayer"
    player.current_room_id = "room_123"
    return player


@pytest.mark.asyncio
async def test_handle_rest_command_no_app(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test handle_rest_command() handles missing app."""
    mock_request.app = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_persistence(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test handle_rest_command() handles missing persistence."""
    mock_request.app.state.persistence = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_connection_manager(mock_request, mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test handle_rest_command() handles missing connection manager."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_player_not_found(mock_request, mock_persistence, mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test handle_rest_command() handles player not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not recognized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_already_resting(  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    mock_request, mock_persistence, mock_connection_manager, mock_player
):
    """Test handle_rest_command() handles player already resting."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    player_id = uuid.UUID(mock_player.player_id)
    mock_connection_manager.resting_players[player_id] = asyncio.create_task(asyncio.sleep(10))

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "already resting" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_in_combat(mock_request, mock_persistence, mock_connection_manager, mock_player):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test handle_rest_command() blocks when player is in combat."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_request.app.state.combat_service = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    # Mock combat service to return player in combat
    combat_service = mock_request.app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=MagicMock())  # Returns combat instance

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "cannot rest during combat" in result["result"].lower() or "combat" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_rest_location_instant(  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    mock_request, mock_persistence, mock_connection_manager, mock_player
):
    """Test handle_rest_command() instant disconnect in rest location."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_request.app.state.combat_service = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=MagicMock(rest_location=True))

    # Mock combat service to return player not in combat
    combat_service = mock_request.app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    with patch(
        "server.commands.rest_command._disconnect_player_intentionally", new_callable=AsyncMock
    ) as mock_disconnect:
        result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

        assert "result" in result
        assert "rest peacefully" in result["result"].lower() or "disconnect" in result["result"].lower()
        mock_disconnect.assert_called_once()


@pytest.mark.asyncio
async def test_handle_rest_command_starts_countdown(  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    mock_request, mock_persistence, mock_connection_manager, mock_player
):
    """Test handle_rest_command() starts countdown when not in rest location."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_request.app.state.combat_service = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=MagicMock(rest_location=False))

    # Mock combat service to return player not in combat
    combat_service = mock_request.app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    # Mock position service
    with patch("server.commands.rest_command.PlayerPositionService") as mock_position_service_class:
        mock_position_service = MagicMock()
        mock_position_service_class.return_value = mock_position_service
        mock_position_service.change_position = AsyncMock(return_value={"success": True, "message": "Sitting"})

        with patch(
            "server.commands.rest_command._start_rest_countdown", new_callable=AsyncMock
        ) as mock_start_countdown:
            result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

            assert "result" in result
            assert "rest" in result["result"].lower() or "countdown" in result["result"].lower()
            mock_start_countdown.assert_called_once()


@pytest.mark.asyncio
async def test_check_player_in_combat_true(mock_app):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_player_in_combat() returns True when player is in combat."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = MagicMock()
    combat_service = mock_app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=MagicMock())  # Returns combat instance

    result = await _check_player_in_combat(player_id, mock_app)

    assert result is True


@pytest.mark.asyncio
async def test_check_player_in_combat_false(mock_app):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_player_in_combat() returns False when player is not in combat."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = MagicMock()
    combat_service = mock_app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    result = await _check_player_in_combat(player_id, mock_app)

    assert result is False


@pytest.mark.asyncio
async def test_check_player_in_combat_no_service(mock_app):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_player_in_combat() returns False when no combat service."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = None

    result = await _check_player_in_combat(player_id, mock_app)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_true(mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_rest_location() returns True when room is rest location."""
    room_id = "room_123"
    mock_room = MagicMock()
    mock_room.rest_location = True
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is True


@pytest.mark.asyncio
async def test_check_rest_location_false(mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_rest_location() returns False when room is not rest location."""
    room_id = "room_123"
    mock_room = MagicMock()
    mock_room.rest_location = False
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_no_room(mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _check_rest_location() returns False when room not found."""
    room_id = "room_123"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_no_persistence():
    """Test _check_rest_location() returns False when no persistence."""
    room_id = "room_123"

    result = await _check_rest_location(room_id, None)

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_player_intentionally(mock_connection_manager, mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test _disconnect_player_intentionally() marks disconnect as intentional."""
    player_id = uuid.uuid4()
    # The function calls force_disconnect_player
    mock_connection_manager.force_disconnect_player = AsyncMock()
    mock_connection_manager.intentional_disconnects = set()

    await _disconnect_player_intentionally(player_id, mock_connection_manager, mock_persistence)

    # Verify player was added to intentional_disconnects (and removed in finally block)
    # Verify force_disconnect_player was called
    mock_connection_manager.force_disconnect_player.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_start_rest_countdown_creates_task(mock_connection_manager, mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test _start_rest_countdown() creates and stores a rest countdown task."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    await _start_rest_countdown(player_id, player_name, mock_connection_manager, mock_persistence)

    assert player_id in mock_connection_manager.resting_players
    assert isinstance(mock_connection_manager.resting_players[player_id], asyncio.Task)


@pytest.mark.asyncio
async def test_start_rest_countdown_timer_expires(mock_connection_manager, mock_persistence):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test rest countdown task disconnects player after timer expires."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    with patch(
        "server.commands.rest_command._disconnect_player_intentionally", new_callable=AsyncMock
    ) as mock_disconnect:
        with patch("server.commands.rest_countdown_task.REST_COUNTDOWN_DURATION", 0.1):
            await _start_rest_countdown(player_id, player_name, mock_connection_manager, mock_persistence)

            # Wait for task to complete
            await asyncio.sleep(0.2)

            # Verify disconnect was called
            mock_disconnect.assert_called_once_with(player_id, mock_connection_manager, mock_persistence)
            assert player_id not in mock_connection_manager.resting_players


@pytest.mark.asyncio
async def test_cancel_rest_countdown_cancels_task(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _cancel_rest_countdown() cancels the rest countdown task."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(100))  # Long-running task
    mock_connection_manager.resting_players[player_id] = task

    await _cancel_rest_countdown(player_id, mock_connection_manager)

    # Verify task was cancelled
    assert task.cancelled()
    assert player_id not in mock_connection_manager.resting_players


@pytest.mark.asyncio
async def test_cancel_rest_countdown_not_resting(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test _cancel_rest_countdown() does nothing if player not resting."""
    player_id = uuid.uuid4()

    # Should not raise an error
    await _cancel_rest_countdown(player_id, mock_connection_manager)

    assert player_id not in mock_connection_manager.resting_players


def test_is_player_resting_true(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test is_player_resting() returns True when player is resting."""
    player_id = uuid.uuid4()
    # Use MagicMock instead of real task to avoid event loop requirement
    task = MagicMock()
    mock_connection_manager.resting_players[player_id] = task

    result = is_player_resting(player_id, mock_connection_manager)

    assert result is True


def test_is_player_resting_false(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test is_player_resting() returns False when player is not resting."""
    player_id = uuid.uuid4()

    result = is_player_resting(player_id, mock_connection_manager)

    assert result is False


def test_is_player_resting_no_manager_attribute():
    """Test is_player_resting() returns False when manager has no resting_players."""
    player_id = uuid.uuid4()
    manager = MagicMock()
    del manager.resting_players  # Remove attribute

    result = is_player_resting(player_id, manager)

    assert result is False
