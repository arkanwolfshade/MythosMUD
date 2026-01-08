"""
Integration tests for rest command and disconnect grace period.

Tests the integration between rest command, grace period system,
combat blocking, and visual indicators.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rest_command import (
    _cancel_rest_countdown,
    _start_rest_countdown,
    handle_rest_command,
)
from server.realtime.disconnect_grace_period import (
    cancel_grace_period,
    is_player_in_grace_period,
)
from server.realtime.player_presence_tracker import track_player_disconnected_impl


@pytest.fixture
def mock_app_with_services():
    """Create a mock app with all required services."""
    app = MagicMock()
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_connection_manager_full():
    """Create a fully configured mock connection manager."""
    manager = MagicMock()
    manager.grace_period_players = {}
    manager.resting_players = {}
    manager.intentional_disconnects = set()
    manager.disconnecting_players = set()
    manager.disconnect_lock = AsyncMock()
    manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    manager._get_player = AsyncMock()  # pylint: disable=protected-access
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access
    manager.force_disconnect_player = AsyncMock()
    manager.player_websockets = {}
    return manager


@pytest.fixture
def mock_persistence_full():
    """Create a fully configured mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.mark.asyncio
async def test_unintentional_disconnect_starts_grace_period(mock_connection_manager_full, mock_persistence_full):  # pylint: disable=redefined-outer-name
    """Test that unintentional disconnect starts grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_connection_manager_full._get_player.return_value = mock_player  # pylint: disable=protected-access
    mock_connection_manager_full.async_persistence = mock_persistence_full

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                with patch(
                    "server.realtime.player_presence_tracker._collect_disconnect_keys",
                    return_value=(set(), set()),
                ):
                    # Player NOT in intentional_disconnects (unintentional)
                    await track_player_disconnected_impl(player_id, mock_connection_manager_full, connection_type=None)

                    # Verify grace period was started
                    assert player_id in mock_connection_manager_full.grace_period_players


@pytest.mark.asyncio
async def test_intentional_disconnect_no_grace_period(mock_connection_manager_full, mock_persistence_full):  # pylint: disable=redefined-outer-name
    """Test that intentional disconnect does NOT start grace period."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by player_presence_tracker implementation
    mock_connection_manager_full._get_player.return_value = mock_player  # pylint: disable=protected-access
    mock_connection_manager_full.async_persistence = mock_persistence_full
    mock_connection_manager_full.intentional_disconnects.add(player_id)  # Mark as intentional

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                with patch(
                    "server.realtime.player_presence_tracker._collect_disconnect_keys",
                    return_value=(set(), set()),
                ):
                    with patch(
                        "server.realtime.player_presence_tracker.handle_player_disconnect_broadcast",
                        new_callable=AsyncMock,
                    ):
                        with patch("server.realtime.player_presence_tracker._remove_player_from_online_tracking"):
                            with patch("server.realtime.player_presence_tracker._cleanup_player_references"):
                                with patch(
                                    "server.realtime.disconnect_grace_period.start_grace_period", new_callable=AsyncMock
                                ) as mock_start_grace:
                                    await track_player_disconnected_impl(
                                        player_id, mock_connection_manager_full, connection_type=None
                                    )

                                    # Verify grace period was NOT started
                                    mock_start_grace.assert_not_called()


@pytest.mark.asyncio
async def test_rest_command_blocks_during_combat(  # pylint: disable=redefined-outer-name
    mock_app_with_services, mock_connection_manager_full, mock_persistence_full
):
    """Test that /rest command is blocked during combat."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "room_123"
    mock_persistence_full.get_player_by_name = AsyncMock(return_value=mock_player)

    # Mock combat service to return player in combat
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=MagicMock())  # Returns combat instance
    mock_app_with_services.state.combat_service = mock_combat_service
    mock_app_with_services.state.persistence = mock_persistence_full
    mock_app_with_services.state.connection_manager = mock_connection_manager_full

    mock_request = MagicMock()
    mock_request.app = mock_app_with_services

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "cannot rest during combat" in result["result"].lower() or "combat" in result["result"].lower()
    assert player_id not in mock_connection_manager_full.resting_players


@pytest.mark.asyncio
async def test_rest_command_starts_countdown_not_in_combat(  # pylint: disable=redefined-outer-name
    mock_app_with_services, mock_connection_manager_full, mock_persistence_full
):
    """Test that /rest command starts countdown when not in combat."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "room_123"
    mock_persistence_full.get_player_by_name = AsyncMock(return_value=mock_player)

    # Mock combat service to return player NOT in combat
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    mock_app_with_services.state.combat_service = mock_combat_service
    mock_app_with_services.state.persistence = mock_persistence_full
    mock_app_with_services.state.connection_manager = mock_connection_manager_full

    # Mock room is NOT a rest location
    mock_room = MagicMock()
    mock_room.rest_location = False
    mock_persistence_full.get_room_by_id = MagicMock(return_value=mock_room)

    # Mock position service
    with patch("server.commands.rest_command.PlayerPositionService") as mock_position_service_class:
        mock_position_service = MagicMock()
        mock_position_service_class.return_value = mock_position_service
        mock_position_service.change_position = AsyncMock(return_value={"success": True, "message": "Sitting"})

        mock_request = MagicMock()
        mock_request.app = mock_app_with_services

        result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

        # Verify countdown started
        assert player_id in mock_connection_manager_full.resting_players
        assert "result" in result
        assert "rest" in result["result"].lower() or "countdown" in result["result"].lower()


@pytest.mark.asyncio
async def test_rest_interrupts_combat_action(mock_connection_manager_full):  # pylint: disable=redefined-outer-name
    """Test that combat action interrupts rest countdown."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(10))
    mock_connection_manager_full.resting_players[player_id] = task

    # Simulate combat action interrupting rest
    await _cancel_rest_countdown(player_id, mock_connection_manager_full)

    # Verify rest was cancelled
    assert task.cancelled()
    assert player_id not in mock_connection_manager_full.resting_players


@pytest.mark.asyncio
async def test_reconnection_cancels_grace_period(mock_connection_manager_full):  # pylint: disable=redefined-outer-name
    """Test that reconnection cancels grace period."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(30))
    mock_connection_manager_full.grace_period_players[player_id] = task

    # Simulate reconnection
    await cancel_grace_period(player_id, mock_connection_manager_full)

    # Verify grace period was cancelled
    assert task.cancelled()
    assert player_id not in mock_connection_manager_full.grace_period_players


@pytest.mark.asyncio
async def test_grace_period_player_can_auto_attack(mock_connection_manager_full):  # pylint: disable=redefined-outer-name
    """Test that grace period player can auto-attack when attacked."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(30))
    mock_connection_manager_full.grace_period_players[player_id] = task

    # Verify player is in grace period
    assert is_player_in_grace_period(player_id, mock_connection_manager_full) is True

    # Note: Actual auto-attack behavior is tested in combat_turn_processor tests
    # This test verifies the state is correct for auto-attack to work


@pytest.mark.asyncio
async def test_grace_period_player_cannot_use_commands(mock_connection_manager_full):  # pylint: disable=redefined-outer-name
    """Test that grace period player cannot use commands."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(30))
    mock_connection_manager_full.grace_period_players[player_id] = task

    # Verify player is in grace period
    assert is_player_in_grace_period(player_id, mock_connection_manager_full) is True

    # Note: Command blocking is tested in command_handler_unified tests
    # This test verifies the state is correct for command blocking to work


@pytest.mark.asyncio
async def test_rest_location_instant_disconnect(  # pylint: disable=redefined-outer-name
    mock_app_with_services, mock_connection_manager_full, mock_persistence_full
):
    """Test that rest location provides instant disconnect when not in combat."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "room_123"
    mock_persistence_full.get_player_by_name = AsyncMock(return_value=mock_player)

    # Mock combat service to return player NOT in combat
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    mock_app_with_services.state.combat_service = mock_combat_service
    mock_app_with_services.state.persistence = mock_persistence_full
    mock_app_with_services.state.connection_manager = mock_connection_manager_full

    # Mock room IS a rest location
    mock_room = MagicMock()
    mock_room.rest_location = True
    mock_persistence_full.get_room_by_id = MagicMock(return_value=mock_room)

    mock_request = MagicMock()
    mock_request.app = mock_app_with_services

    with patch(
        "server.commands.rest_command._disconnect_player_intentionally", new_callable=AsyncMock
    ) as mock_disconnect:
        result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

        # Verify instant disconnect (no countdown)
        mock_disconnect.assert_called_once()
        assert player_id not in mock_connection_manager_full.resting_players  # No countdown started
        assert "result" in result
        assert "rest peacefully" in result["result"].lower() or "disconnect" in result["result"].lower()


@pytest.mark.asyncio
async def test_rest_location_blocked_during_combat(  # pylint: disable=redefined-outer-name
    mock_app_with_services, mock_connection_manager_full, mock_persistence_full
):
    """Test that /rest in rest location is still blocked during combat."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = str(player_id)
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "room_123"
    mock_persistence_full.get_player_by_name = AsyncMock(return_value=mock_player)

    # Mock combat service to return player IN combat
    mock_combat_service = MagicMock()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=MagicMock())  # Returns combat instance
    mock_app_with_services.state.combat_service = mock_combat_service
    mock_app_with_services.state.persistence = mock_persistence_full
    mock_app_with_services.state.connection_manager = mock_connection_manager_full

    # Mock room IS a rest location
    mock_room = MagicMock()
    mock_room.rest_location = True
    mock_persistence_full.get_room_by_id = MagicMock(return_value=mock_room)

    mock_request = MagicMock()
    mock_request.app = mock_app_with_services

    result = await handle_rest_command({}, {}, mock_request, None, "TestPlayer")

    # Verify command is blocked (combat check happens before rest location check)
    assert "result" in result
    assert "cannot rest during combat" in result["result"].lower() or "combat" in result["result"].lower()


@pytest.mark.asyncio
async def test_visual_indicator_in_grace_period(mock_connection_manager_full):  # pylint: disable=redefined-outer-name
    """Test that visual indicator (linkdead) is shown for grace period players."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(30))
    mock_connection_manager_full.grace_period_players[player_id] = task

    # Verify player is in grace period
    assert is_player_in_grace_period(player_id, mock_connection_manager_full) is True

    # Note: Actual visual indicator display is tested in visual_indicator tests
    # This test verifies the state is correct for visual indicator to work


@pytest.mark.asyncio
async def test_rest_countdown_completes_disconnect(mock_connection_manager_full, mock_persistence_full):  # pylint: disable=redefined-outer-name
    """Test that rest countdown completes and disconnects player."""
    player_id = uuid.uuid4()
    player_name = "TestPlayer"

    with patch(
        "server.commands.rest_command._disconnect_player_intentionally", new_callable=AsyncMock
    ) as mock_disconnect:
        with patch("server.commands.rest_countdown_task.REST_COUNTDOWN_DURATION", 0.1):
            await _start_rest_countdown(player_id, player_name, mock_connection_manager_full, mock_persistence_full)

            # Wait for countdown to complete
            await asyncio.sleep(0.2)

            # Verify disconnect was called
            mock_disconnect.assert_called_once_with(player_id, mock_connection_manager_full, mock_persistence_full)
            assert player_id not in mock_connection_manager_full.resting_players
