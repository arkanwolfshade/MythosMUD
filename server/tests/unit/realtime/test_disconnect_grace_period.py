"""
Unit tests for disconnect grace period management.

Tests the grace period system for unintentional disconnects, including
timer management, zombie state, and reconnection handling.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.disconnect_grace_period import (
    cancel_grace_period,
    is_player_in_grace_period,
    start_grace_period,
)


@pytest.fixture
def mock_manager():
    """Create a mock ConnectionManager."""
    manager = MagicMock()
    manager.grace_period_players = {}
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    manager._get_player = AsyncMock()  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    return manager


@pytest.mark.asyncio
async def test_start_grace_period_creates_task(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test start_grace_period() creates and stores a grace period task."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    mock_manager._get_player.return_value = mock_player  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation

    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="TestPlayer"):
        with patch(
            "server.realtime.disconnect_grace_period._collect_disconnect_keys",
            return_value=(set(), set()),
        ):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking"):
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast", new_callable=AsyncMock
                ):
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references"):
                        await start_grace_period(player_id, mock_manager)

                        assert player_id in mock_manager.grace_period_players
                        assert isinstance(mock_manager.grace_period_players[player_id], asyncio.Task)


@pytest.mark.asyncio
async def test_start_grace_period_already_in_grace_period(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test start_grace_period() does nothing if player already in grace period."""
    player_id = uuid.uuid4()
    existing_task = asyncio.create_task(asyncio.sleep(1))
    mock_manager.grace_period_players[player_id] = existing_task

    await start_grace_period(player_id, mock_manager)

    # Task should not be replaced
    assert mock_manager.grace_period_players[player_id] == existing_task


@pytest.mark.asyncio
async def test_start_grace_period_timer_expires(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test grace period task performs cleanup after timer expires."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    mock_manager._get_player.return_value = mock_player  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation

    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="TestPlayer"):
        with patch(
            "server.realtime.disconnect_grace_period._collect_disconnect_keys",
            return_value=(set(), set()),
        ):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking") as mock_remove:
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast", new_callable=AsyncMock
                ) as mock_broadcast:
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references") as mock_cleanup:
                        # Start grace period with shorter duration for testing
                        with patch("server.realtime.disconnect_grace_period.GRACE_PERIOD_DURATION", 0.1):
                            await start_grace_period(player_id, mock_manager)

                            # Wait for task to complete
                            await asyncio.sleep(0.2)

                            # Verify cleanup was called
                            mock_broadcast.assert_called_once()
                            mock_remove.assert_called_once()
                            mock_cleanup.assert_called_once()
                            assert player_id not in mock_manager.grace_period_players


@pytest.mark.asyncio
async def test_start_grace_period_reconnection_cancels(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test grace period is cancelled when player reconnects."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    mock_manager._get_player.return_value = mock_player  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation

    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="TestPlayer"):
        with patch(
            "server.realtime.disconnect_grace_period._collect_disconnect_keys",
            return_value=(set(), set()),
        ):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking"):
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast", new_callable=AsyncMock
                ):
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references"):
                        await start_grace_period(player_id, mock_manager)

                        # Cancel grace period (simulating reconnection)
                        await cancel_grace_period(player_id, mock_manager)

                        # Verify task was cancelled and removed
                        assert player_id not in mock_manager.grace_period_players


@pytest.mark.asyncio
async def test_cancel_grace_period_not_in_grace_period(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test cancel_grace_period() does nothing if player not in grace period."""
    player_id = uuid.uuid4()

    # Should not raise an error
    await cancel_grace_period(player_id, mock_manager)

    assert player_id not in mock_manager.grace_period_players


@pytest.mark.asyncio
async def test_cancel_grace_period_cancels_task(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test cancel_grace_period() cancels the grace period task."""
    player_id = uuid.uuid4()
    task = asyncio.create_task(asyncio.sleep(100))  # Long-running task
    mock_manager.grace_period_players[player_id] = task

    await cancel_grace_period(player_id, mock_manager)

    # Verify task was cancelled
    assert task.cancelled()
    assert player_id not in mock_manager.grace_period_players


def test_is_player_in_grace_period_true(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test is_player_in_grace_period() returns True when player is in grace period."""
    player_id = uuid.uuid4()
    # Use MagicMock instead of real task to avoid event loop requirement
    task = MagicMock()
    mock_manager.grace_period_players[player_id] = task

    result = is_player_in_grace_period(player_id, mock_manager)

    assert result is True


def test_is_player_in_grace_period_false(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test is_player_in_grace_period() returns False when player is not in grace period."""
    player_id = uuid.uuid4()

    result = is_player_in_grace_period(player_id, mock_manager)

    assert result is False


def test_is_player_in_grace_period_no_manager_attribute():
    """Test is_player_in_grace_period() returns False when manager has no grace_period_players."""
    player_id = uuid.uuid4()
    manager = MagicMock()
    del manager.grace_period_players  # Remove attribute

    result = is_player_in_grace_period(player_id, manager)

    assert result is False


@pytest.mark.asyncio
async def test_grace_period_handles_player_not_found(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test grace period handles case where player is not found during cleanup."""
    player_id = uuid.uuid4()
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    mock_manager._get_player.return_value = None  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation, player not found scenario

    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="Unknown Player"):
        with patch(
            "server.realtime.disconnect_grace_period._collect_disconnect_keys",
            return_value=(set(), set()),
        ):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking"):
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast", new_callable=AsyncMock
                ):
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references"):
                        with patch("server.realtime.disconnect_grace_period.GRACE_PERIOD_DURATION", 0.1):
                            await start_grace_period(player_id, mock_manager)

                            # Wait for task to complete
                            await asyncio.sleep(0.2)

                            # Should complete without error
                            assert player_id not in mock_manager.grace_period_players


@pytest.mark.asyncio
async def test_grace_period_handles_errors_gracefully(mock_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test grace period handles errors during cleanup gracefully."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation
    mock_manager._get_player.side_effect = Exception("Database error")  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to mock the method used by disconnect_grace_period implementation, error scenario

    with patch("server.realtime.disconnect_grace_period.extract_player_name", return_value="TestPlayer"):
        with patch(
            "server.realtime.disconnect_grace_period._collect_disconnect_keys",
            return_value=(set(), set()),
        ):
            with patch("server.realtime.disconnect_grace_period._remove_player_from_online_tracking"):
                with patch(
                    "server.realtime.disconnect_grace_period.handle_player_disconnect_broadcast", new_callable=AsyncMock
                ):
                    with patch("server.realtime.disconnect_grace_period._cleanup_player_references"):
                        with patch("server.realtime.disconnect_grace_period.GRACE_PERIOD_DURATION", 0.1):
                            await start_grace_period(player_id, mock_manager)

                            # Wait for task to complete
                            await asyncio.sleep(0.2)

                            # Should still clean up task even on error
                            assert player_id not in mock_manager.grace_period_players
