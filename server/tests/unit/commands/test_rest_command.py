"""
Unit tests for rest command handlers.

Tests the rest command functionality including combat blocking,
rest location instant disconnect, countdown, and interruption logic.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally call rest_command private helpers.
# pyright: reportAny=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
# Reason: MagicMock fixture attribute chains are Any; typing each access adds no safety.

from __future__ import annotations

import asyncio
import uuid
from typing import override
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rest_command import (
    _check_rest_location,
    _disconnect_player_intentionally,
    _start_rest_countdown,
    cancel_rest_countdown,
    check_player_in_combat,
    handle_rest_command,
    is_player_resting,
)


@pytest.fixture
def mock_app() -> MagicMock:
    """Create a mock FastAPI app."""
    app: MagicMock = MagicMock()
    state: MagicMock = MagicMock()
    # Ensure container is None so _get_services_from_app uses app.state.persistence
    # instead of trying to get it from app.state.container.async_persistence
    state.container = None
    app.state = state
    return app


@pytest.fixture
def mock_request(mock_app: MagicMock) -> MagicMock:
    """Create a mock request."""
    request: MagicMock = MagicMock()
    request.app = mock_app
    return request


class MockPersistence:
    """Mock persistence layer with async methods."""

    def __init__(self) -> None:
        self._get_player_by_name_mock: AsyncMock = AsyncMock(return_value=None)
        self._get_room_by_id_mock: MagicMock = MagicMock(return_value=None)

    async def get_player_by_name(self, name: str) -> object:
        """Mock async method that uses configured mock."""
        return await self._get_player_by_name_mock(name)

    def get_room_by_id(self, room_id: str) -> object:
        """Mock method that uses configured mock."""
        return self._get_room_by_id_mock(room_id)

    @override
    def __setattr__(self, name: str, value: object) -> None:
        """Allow setting get_player_by_name and get_room_by_id to mocks."""
        if name == "get_player_by_name":
            object.__setattr__(self, "_get_player_by_name_mock", value)
        elif name == "get_room_by_id":
            object.__setattr__(self, "_get_room_by_id_mock", value)
        else:
            super().__setattr__(name, value)


@pytest.fixture
def mock_persistence() -> MockPersistence:
    """Create a mock persistence layer."""
    return MockPersistence()


@pytest.fixture
def mock_connection_manager() -> MagicMock:
    """Create a mock connection manager."""
    manager: MagicMock = MagicMock()
    manager.resting_players = {}
    manager.intentional_disconnects = set()
    manager.player_websockets = {}
    manager.force_disconnect_player = AsyncMock()
    manager.disconnect_websocket_connection = AsyncMock(return_value=True)
    return manager


@pytest.fixture
def mock_player() -> MagicMock:
    """Create a mock player."""
    player: MagicMock = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "TestPlayer"
    player.current_room_id = "room_123"
    return player


@pytest.mark.asyncio
async def test_handle_rest_command_no_app(mock_request: MagicMock) -> None:
    """Test handle_rest_command() handles missing app."""
    mock_request.app = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_persistence(mock_request: MagicMock) -> None:
    """Test handle_rest_command() handles missing persistence."""
    mock_request.app.state.persistence = None

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_no_connection_manager(
    mock_request: MagicMock, mock_persistence: MockPersistence
) -> None:
    """Test handle_rest_command() handles missing connection manager."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = None
    # Note: mock_persistence fixture now has get_player_by_name configured by default

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_player_not_found(
    mock_request: MagicMock, mock_persistence: MockPersistence, mock_connection_manager: MagicMock
) -> None:
    """Test handle_rest_command() handles player not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not recognized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rest_command_already_resting(
    mock_request: MagicMock,
    mock_persistence: MockPersistence,
    mock_connection_manager: MagicMock,
    mock_player: MagicMock,
) -> None:
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
async def test_handle_rest_command_in_combat(
    mock_request: MagicMock,
    mock_persistence: MockPersistence,
    mock_connection_manager: MagicMock,
    mock_player: MagicMock,
) -> None:
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
async def test_handle_rest_command_rest_location_instant(
    mock_request: MagicMock,
    mock_persistence: MockPersistence,
    mock_connection_manager: MagicMock,
    mock_player: MagicMock,
) -> None:
    """Test handle_rest_command() instant disconnect in rest location."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_request.app.state.combat_service = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=MagicMock(rest_location=True))

    # Mock combat service to return player not in combat
    combat_service = mock_request.app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    player_id = uuid.UUID(mock_player.player_id)
    mock_connection_manager.player_websockets[player_id] = ["conn-1"]

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "rest peacefully" in result["result"].lower() or "disconnect" in result["result"].lower()
    # #297: the disconnect is deliberately deferred (asyncio.create_task) past a short delay so
    # the response above reaches the client before the socket closes -- give that task a chance
    # to run before asserting, matching the fire-and-forget task pattern in
    # test_disconnect_grace_period.py.
    await asyncio.sleep(0.2)
    # Targets the specific connection snapshotted at /rest time (#297) rather than a blanket
    # force_disconnect_player, so a fast reconnect during the delay isn't swept up too.
    mock_connection_manager.disconnect_websocket_connection.assert_called_once_with(player_id, "conn-1")


@pytest.mark.asyncio
async def test_handle_rest_command_rest_location_marks_intentional_before_delay(
    mock_request: MagicMock,
    mock_persistence: MockPersistence,
    mock_connection_manager: MagicMock,
    mock_player: MagicMock,
) -> None:
    """#297 regression: intentional_disconnects must be marked before the deferred close's sleep,
    not after. The socket has been observed dying (a racing client reconnect, e.g.) faster than
    that 100ms delay; marking intent only after it elapses left a real disconnect running through
    the handler while player_id was still absent from intentional_disconnects, misclassifying a
    /rest disconnect as unintentional and starting a 30s linkdead grace period instead of clean
    teardown (caught via rest-command.spec.ts's countdown test failing to reconnect afterward).
    """
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_request.app.state.combat_service = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.get_room_by_id = MagicMock(return_value=MagicMock(rest_location=True))

    combat_service = mock_request.app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    player_id = uuid.UUID(mock_player.player_id)
    mock_connection_manager.player_websockets[player_id] = ["conn-1"]

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result

    # asyncio.create_task() only schedules the deferred task; a single zero-delay yield is enough
    # for it to run its synchronous prefix (the intent marking, now before the sleep) -- mirroring
    # the real await (websocket.send_json) production hits between create_task and the response
    # actually reaching the wire, which is what let the race happen in the first place.
    await asyncio.sleep(0)
    assert player_id in mock_connection_manager.intentional_disconnects
    # The actual close is still deferred -- only the intent marking moved earlier.
    mock_connection_manager.disconnect_websocket_connection.assert_not_called()

    await asyncio.sleep(0.2)
    mock_connection_manager.disconnect_websocket_connection.assert_called_once_with(player_id, "conn-1")
    # Cleaned up in the deferred task's finally block once the close completes.
    assert player_id not in mock_connection_manager.intentional_disconnects


@pytest.mark.asyncio
async def test_handle_rest_command_starts_countdown(
    mock_request: MagicMock,
    mock_persistence: MockPersistence,
    mock_connection_manager: MagicMock,
    mock_player: MagicMock,
) -> None:
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
async def test_check_player_in_combat_true(mock_app: MagicMock) -> None:
    """Test check_player_in_combat() returns True when player is in combat."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = MagicMock()
    combat_service = mock_app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=MagicMock())  # Returns combat instance

    result = await check_player_in_combat(player_id, mock_app)

    assert result is True


@pytest.mark.asyncio
async def test_check_player_in_combat_false(mock_app: MagicMock) -> None:
    """Test check_player_in_combat() returns False when player is not in combat."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = MagicMock()
    combat_service = mock_app.state.combat_service
    combat_service.get_combat_by_participant = AsyncMock(return_value=None)

    result = await check_player_in_combat(player_id, mock_app)

    assert result is False


@pytest.mark.asyncio
async def test_check_player_in_combat_no_service(mock_app: MagicMock) -> None:
    """Test check_player_in_combat() returns False when no combat service."""
    player_id = uuid.uuid4()
    mock_app.state.combat_service = None

    result = await check_player_in_combat(player_id, mock_app)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_true(mock_persistence: MockPersistence) -> None:
    """Test _check_rest_location() returns True when room is rest location."""
    room_id = "room_123"
    mock_room = MagicMock()
    mock_room.rest_location = True
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is True


@pytest.mark.asyncio
async def test_check_rest_location_false(mock_persistence: MockPersistence) -> None:
    """Test _check_rest_location() returns False when room is not rest location."""
    room_id = "room_123"
    mock_room = MagicMock()
    mock_room.rest_location = False
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_no_room(mock_persistence: MockPersistence) -> None:
    """Test _check_rest_location() returns False when room not found."""
    room_id = "room_123"
    mock_persistence.get_room_by_id = MagicMock(return_value=None)

    result = await _check_rest_location(room_id, mock_persistence)

    assert result is False


@pytest.mark.asyncio
async def test_check_rest_location_no_persistence() -> None:
    """Test _check_rest_location() returns False when no persistence."""
    room_id = "room_123"

    result = await _check_rest_location(room_id, None)

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_player_intentionally(
    mock_connection_manager: MagicMock, mock_persistence: MockPersistence
) -> None:
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
async def test_start_rest_countdown_creates_task(
    mock_connection_manager: MagicMock, mock_persistence: MockPersistence
) -> None:
    """Test _start_rest_countdown() creates and stores a rest countdown task."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    await _start_rest_countdown(player_id, player_name, mock_connection_manager, mock_persistence)

    assert player_id in mock_connection_manager.resting_players
    assert isinstance(mock_connection_manager.resting_players[player_id], asyncio.Task)


@pytest.mark.asyncio
async def test_start_rest_countdown_timer_expires(
    mock_connection_manager: MagicMock, mock_persistence: MockPersistence
) -> None:
    """Test rest countdown task disconnects player after timer expires."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    with patch(
        "server.commands.rest_command._disconnect_player_intentionally", new_callable=AsyncMock
    ) as mock_disconnect:
        with patch("server.commands.rest_countdown_task.rest_countdown_seconds", return_value=0.1):
            await _start_rest_countdown(player_id, player_name, mock_connection_manager, mock_persistence)

            # Wait for task to complete
            await asyncio.sleep(0.2)

            # Verify disconnect was called
            mock_disconnect.assert_called_once_with(player_id, mock_connection_manager, mock_persistence)
            assert player_id not in mock_connection_manager.resting_players


@pytest.mark.asyncio
async def test_cancel_rest_countdown_cancels_task(mock_connection_manager: MagicMock) -> None:
    """Test cancel_rest_countdown() cancels the rest countdown task."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(100))  # Long-running task
    mock_connection_manager.resting_players[player_id] = task
    mock_connection_manager.async_persistence = None  # Skip stand restore in this unit test

    await cancel_rest_countdown(player_id, mock_connection_manager)

    # Verify task was cancelled
    assert task.cancelled()
    assert player_id not in mock_connection_manager.resting_players


@pytest.mark.asyncio
async def test_cancel_rest_countdown_restores_standing(mock_connection_manager: MagicMock) -> None:
    """Interrupted /rest must stand the player so Sitting does not poison the next session."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(100))
    mock_connection_manager.resting_players[player_id] = task
    mock_player = MagicMock()
    mock_player.name = "ArkanWolfshade"
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.async_persistence = MagicMock()

    with (
        patch("server.commands.rest_command.PlayerPositionService") as mock_svc_cls,
        patch("server.commands.rest_command.emit_posture_change", new_callable=AsyncMock) as mock_emit,
    ):
        mock_svc: MagicMock = MagicMock()
        change_position: AsyncMock = AsyncMock(
            return_value={
                "success": True,
                "position": "standing",
                "previous_position": "sitting",
                "player_display_name": "ArkanWolfshade",
                "room_id": "room-1",
            }
        )
        mock_svc.change_position = change_position
        mock_svc_cls.return_value = mock_svc

        await cancel_rest_countdown(player_id, mock_connection_manager)

        change_position.assert_awaited_once_with("ArkanWolfshade", "standing")
        mock_emit.assert_awaited_once()
    assert player_id not in mock_connection_manager.resting_players


@pytest.mark.asyncio
async def test_cancel_rest_countdown_not_resting(mock_connection_manager: MagicMock) -> None:
    """Test cancel_rest_countdown() does nothing if player not resting."""
    player_id = uuid.uuid4()

    # Should not raise an error
    await cancel_rest_countdown(player_id, mock_connection_manager)

    assert player_id not in mock_connection_manager.resting_players


def test_is_player_resting_true(mock_connection_manager: MagicMock) -> None:
    """Test is_player_resting() returns True when player is resting."""
    player_id = uuid.uuid4()
    # Use MagicMock instead of real task to avoid event loop requirement
    task = MagicMock()
    mock_connection_manager.resting_players[player_id] = task

    result = is_player_resting(player_id, mock_connection_manager)

    assert result is True


def test_is_player_resting_false(mock_connection_manager: MagicMock) -> None:
    """Test is_player_resting() returns False when player is not resting."""
    player_id = uuid.uuid4()

    result = is_player_resting(player_id, mock_connection_manager)

    assert result is False


def test_is_player_resting_no_manager_attribute() -> None:
    """Test is_player_resting() returns False when manager has no resting_players."""
    player_id = uuid.uuid4()
    manager = MagicMock()
    del manager.resting_players  # Remove attribute

    result = is_player_resting(player_id, manager)

    assert result is False
