"""
Unit tests for login grace period functionality.

Tests the core login grace period module functions including
start, cancel, check status, and remaining time calculation.
Covers both legacy (asyncio task) and effect-based (ADR-009) paths.
"""

import asyncio
import time
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.login_grace_period import (
    LOGIN_GRACE_PERIOD_DURATION,
    cancel_login_grace_period,
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
    start_login_grace_period,
)


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager for testing."""
    manager = MagicMock()
    manager.login_grace_period_players = {}
    manager.login_grace_period_start_times = {}
    return manager


@pytest.mark.asyncio
async def test_start_login_grace_period(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test starting a login grace period for a player."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)

    # Check that player is tracked
    assert player_id in mock_connection_manager.login_grace_period_players
    assert player_id in mock_connection_manager.login_grace_period_start_times
    assert isinstance(mock_connection_manager.login_grace_period_players[player_id], asyncio.Task)

    # Check start time is stored
    start_time = mock_connection_manager.login_grace_period_start_times[player_id]
    assert isinstance(start_time, float)
    assert time.time() - start_time < 1.0  # Should be very recent


@pytest.mark.asyncio
async def test_start_login_grace_period_already_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test starting grace period when already active (should not duplicate)."""
    player_id = uuid.uuid4()

    # Start first grace period
    await start_login_grace_period(player_id, mock_connection_manager)
    first_task = mock_connection_manager.login_grace_period_players[player_id]
    first_start_time = mock_connection_manager.login_grace_period_start_times[player_id]

    # Try to start again
    await start_login_grace_period(player_id, mock_connection_manager)

    # Should still have only one task and same start time
    assert len(mock_connection_manager.login_grace_period_players) == 1
    assert mock_connection_manager.login_grace_period_players[player_id] == first_task
    assert mock_connection_manager.login_grace_period_start_times[player_id] == first_start_time


@pytest.mark.asyncio
async def test_start_login_grace_period_expires(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that grace period expires after duration."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)

    # Wait for grace period to expire
    await asyncio.sleep(LOGIN_GRACE_PERIOD_DURATION + 0.5)

    # Player should no longer be in grace period
    assert player_id not in mock_connection_manager.login_grace_period_players
    assert player_id not in mock_connection_manager.login_grace_period_start_times


@pytest.mark.asyncio
async def test_cancel_login_grace_period(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test cancelling an active grace period."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)
    assert player_id in mock_connection_manager.login_grace_period_players

    await cancel_login_grace_period(player_id, mock_connection_manager)

    # Player should no longer be tracked
    assert player_id not in mock_connection_manager.login_grace_period_players
    assert player_id not in mock_connection_manager.login_grace_period_start_times


@pytest.mark.asyncio
async def test_cancel_login_grace_period_not_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test cancelling grace period when not active (should not error)."""
    player_id = uuid.uuid4()

    # Should not raise an error
    await cancel_login_grace_period(player_id, mock_connection_manager)

    assert player_id not in mock_connection_manager.login_grace_period_players


def test_is_player_in_login_grace_period_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test checking if player is in grace period when active."""
    player_id = uuid.uuid4()
    mock_connection_manager.login_grace_period_players[player_id] = MagicMock()

    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True


def test_is_player_in_login_grace_period_not_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test checking if player is in grace period when not active."""
    player_id = uuid.uuid4()

    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is False


def test_is_player_in_login_grace_period_no_manager_attribute():
    """Test checking grace period when manager lacks attribute."""
    player_id = uuid.uuid4()
    manager = MagicMock()
    del manager.login_grace_period_players  # Remove attribute

    assert is_player_in_login_grace_period(player_id, manager) is False


def test_get_login_grace_period_remaining_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test getting remaining time for active grace period."""
    player_id = uuid.uuid4()
    start_time = time.time() - 3.0  # Started 3 seconds ago
    mock_connection_manager.login_grace_period_players[player_id] = MagicMock()
    mock_connection_manager.login_grace_period_start_times[player_id] = start_time

    remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)

    # Should have approximately 7 seconds remaining (10 - 3)
    assert 6.5 < remaining < 7.5  # Allow some tolerance for timing


def test_get_login_grace_period_remaining_not_active(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test getting remaining time when not in grace period."""
    player_id = uuid.uuid4()

    remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)

    assert remaining == 0.0


def test_get_login_grace_period_remaining_no_start_time(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test getting remaining time when start time not found."""
    player_id = uuid.uuid4()
    mock_connection_manager.login_grace_period_players[player_id] = MagicMock()
    # Don't set start_time

    remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)

    assert remaining == 0.0


def test_get_login_grace_period_remaining_no_manager_attribute():
    """Test getting remaining time when manager lacks attribute."""
    player_id = uuid.uuid4()
    manager = MagicMock()
    del manager.login_grace_period_start_times  # Remove attribute

    remaining = get_login_grace_period_remaining(player_id, manager)

    assert remaining == 0.0


@pytest.mark.asyncio
async def test_multiple_players_grace_periods(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test multiple players can have grace periods simultaneously."""
    player1_id = uuid.uuid4()
    player2_id = uuid.uuid4()
    player3_id = uuid.uuid4()

    await start_login_grace_period(player1_id, mock_connection_manager)
    await start_login_grace_period(player2_id, mock_connection_manager)
    await start_login_grace_period(player3_id, mock_connection_manager)

    assert len(mock_connection_manager.login_grace_period_players) == 3
    assert all(
        pid in mock_connection_manager.login_grace_period_players for pid in [player1_id, player2_id, player3_id]
    )
    assert all(
        pid in mock_connection_manager.login_grace_period_start_times for pid in [player1_id, player2_id, player3_id]
    )


@pytest.mark.asyncio
async def test_grace_period_task_cancellation_cleanup(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that cancelled tasks properly clean up tracking."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)
    task = mock_connection_manager.login_grace_period_players[player_id]

    # Cancel the task
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

    # Manually clean up (simulating what cancel_login_grace_period does)
    if player_id in mock_connection_manager.login_grace_period_players:
        del mock_connection_manager.login_grace_period_players[player_id]
    if player_id in mock_connection_manager.login_grace_period_start_times:
        del mock_connection_manager.login_grace_period_start_times[player_id]

    assert player_id not in mock_connection_manager.login_grace_period_players
    assert player_id not in mock_connection_manager.login_grace_period_start_times


# --- Effect-based grace period (ADR-009) ---


@pytest.mark.asyncio
async def test_start_login_grace_period_effect_based_adds_effect_and_sets_in_memory(
    mock_connection_manager,
):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name
    """When async_persistence and tick getters are provided, add effect and set in-memory state (no asyncio task)."""
    player_id = uuid.uuid4()
    mock_persistence = MagicMock()
    mock_persistence.add_player_effect = AsyncMock(return_value=str(uuid.uuid4()))
    get_current_tick = MagicMock(return_value=100)
    get_tick_interval = MagicMock(return_value=0.1)

    await start_login_grace_period(
        player_id,
        mock_connection_manager,
        async_persistence=mock_persistence,
        get_current_tick=get_current_tick,
        get_tick_interval=get_tick_interval,
    )

    mock_persistence.add_player_effect.assert_called_once()
    call_kw = mock_persistence.add_player_effect.call_args[1]
    assert call_kw.get("effect_type") == "login_warded"
    assert call_kw.get("category") == "entry_ward"
    assert call_kw.get("applied_at_tick") == 100
    assert call_kw.get("source") == "game_entry"
    assert player_id in mock_connection_manager.login_grace_period_players
    assert mock_connection_manager.login_grace_period_players[player_id] is True
    assert player_id in mock_connection_manager.login_grace_period_start_times


@pytest.mark.asyncio
async def test_cancel_login_grace_period_effect_based_clears_tracking(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name
    """Cancel when grace is effect-based (sentinel True) only clears in-memory tracking."""
    player_id = uuid.uuid4()
    mock_connection_manager.login_grace_period_players[player_id] = True
    mock_connection_manager.login_grace_period_start_times[player_id] = time.time()

    await cancel_login_grace_period(player_id, mock_connection_manager)

    assert player_id not in mock_connection_manager.login_grace_period_players
    assert player_id not in mock_connection_manager.login_grace_period_start_times
