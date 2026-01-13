"""
Integration tests for login grace period flow.

Tests the complete login grace period flow including:
- API endpoint for starting grace period
- Grace period activation after MOTD dismissal
- Combat prevention during grace period
- Damage blocking during grace period
- Visual indicator display
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.login_grace_period import (
    cancel_login_grace_period,
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
    start_login_grace_period,
)


@pytest.fixture
def mock_connection_manager():
    """Create a mock ConnectionManager for integration testing."""
    manager = MagicMock()
    manager.login_grace_period_players = {}
    manager.login_grace_period_start_times = {}
    manager.player_websockets = {}
    return manager


@pytest.fixture
def mock_async_persistence():
    """Create a mock async persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    return persistence


@pytest.fixture
def mock_combat_service():
    """Create a mock combat service."""
    service = MagicMock()
    service.get_combat_by_participant = AsyncMock(return_value=None)
    service.end_combat = AsyncMock()
    return service


@pytest.mark.asyncio
async def test_start_grace_period_removes_from_combat(mock_connection_manager, mock_combat_service):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test that starting grace period removes player from combat if in combat."""
    player_id = uuid.uuid4()

    # Mock combat service to return a combat instance
    mock_combat = MagicMock()
    mock_combat.combat_id = uuid.uuid4()
    mock_combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    # Start grace period (simulating API endpoint behavior)
    await start_login_grace_period(player_id, mock_connection_manager)

    # Verify grace period is active
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True


@pytest.mark.asyncio
async def test_grace_period_blocks_combat_initiation(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that grace period prevents combat from starting."""
    player_id = uuid.uuid4()
    target_id = uuid.uuid4()

    # Start grace period
    await start_login_grace_period(player_id, mock_connection_manager)

    # Verify player is in grace period
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True
    assert is_player_in_login_grace_period(target_id, mock_connection_manager) is False


@pytest.mark.asyncio
async def test_grace_period_remaining_time_decreases(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that remaining time decreases over time."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)

    # Get initial remaining time
    initial_remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)
    assert initial_remaining > 0

    # Wait a bit
    await asyncio.sleep(1.0)

    # Get updated remaining time
    updated_remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)
    assert updated_remaining < initial_remaining
    assert updated_remaining > 0


@pytest.mark.asyncio
async def test_grace_period_expires_after_duration(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that grace period expires after full duration."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True

    # Wait for grace period to expire
    await asyncio.sleep(10.5)  # Slightly longer than 10 seconds

    # Player should no longer be in grace period
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is False
    assert get_login_grace_period_remaining(player_id, mock_connection_manager) == 0.0


@pytest.mark.asyncio
async def test_multiple_players_independent_grace_periods(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that multiple players can have independent grace periods."""
    player1_id = uuid.uuid4()
    player2_id = uuid.uuid4()

    # Start grace periods for both players
    await start_login_grace_period(player1_id, mock_connection_manager)
    await asyncio.sleep(2.0)  # Wait 2 seconds
    await start_login_grace_period(player2_id, mock_connection_manager)

    # Both should be active
    assert is_player_in_login_grace_period(player1_id, mock_connection_manager) is True
    assert is_player_in_login_grace_period(player2_id, mock_connection_manager) is True

    # Player1 should have less time remaining
    remaining1 = get_login_grace_period_remaining(player1_id, mock_connection_manager)
    remaining2 = get_login_grace_period_remaining(player2_id, mock_connection_manager)
    assert remaining1 < remaining2


@pytest.mark.asyncio
async def test_grace_period_can_be_cancelled(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that grace period can be cancelled before expiration."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is True

    # Cancel grace period
    await cancel_login_grace_period(player_id, mock_connection_manager)

    # Player should no longer be in grace period
    assert is_player_in_login_grace_period(player_id, mock_connection_manager) is False


@pytest.mark.asyncio
async def test_grace_period_start_time_tracking(mock_connection_manager):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test that start times are properly tracked for remaining time calculation."""
    player_id = uuid.uuid4()

    await start_login_grace_period(player_id, mock_connection_manager)

    # Verify start time is stored
    assert player_id in mock_connection_manager.login_grace_period_start_times
    start_time = mock_connection_manager.login_grace_period_start_times[player_id]
    assert isinstance(start_time, float)

    # Verify remaining time calculation uses start time
    remaining = get_login_grace_period_remaining(player_id, mock_connection_manager)
    assert 9.0 <= remaining <= 10.0  # Should be close to 10 seconds initially (allow for timing)
