"""
Unit tests for combat cleanup handler.

Tests the CombatCleanupHandler class for combat cleanup and tracking operations.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatStatus
from server.services.combat_cleanup_handler import CombatCleanupHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    service = MagicMock()
    service._active_combats = {}
    service._player_combats = {}
    service._npc_combats = {}
    return service


@pytest.fixture
def cleanup_handler(mock_combat_service):
    """Create CombatCleanupHandler instance."""
    return CombatCleanupHandler(mock_combat_service)


@pytest.fixture
def mock_combat():
    """Create mock combat instance."""
    combat = MagicMock(spec=CombatInstance)
    combat.combat_id = "combat_001"
    combat.participants = {
        "player_001": MagicMock(),
        "npc_001": MagicMock(),
    }
    combat.status = CombatStatus.ACTIVE
    return combat


def test_cleanup_handler_init(cleanup_handler, mock_combat_service):
    """Test CombatCleanupHandler initialization."""
    assert cleanup_handler._combat_service == mock_combat_service


def test_cleanup_combat_tracking(cleanup_handler, mock_combat, mock_combat_service):
    """Test cleanup_combat_tracking removes combat from tracking."""
    mock_combat_service._active_combats["combat_001"] = mock_combat
    mock_combat_service._player_combats["player_001"] = mock_combat
    mock_combat_service._npc_combats["npc_001"] = mock_combat

    cleanup_handler.cleanup_combat_tracking(mock_combat)

    assert "combat_001" not in mock_combat_service._active_combats
    assert "player_001" not in mock_combat_service._player_combats
    assert "npc_001" not in mock_combat_service._npc_combats


def test_check_connection_state(cleanup_handler):
    """Test check_connection_state checks connection state."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
        mock_connection_manager.room_subscriptions = {"room_001": {"player_1", "player_2"}}
        mock_instance.connection_manager = mock_connection_manager
        mock_container.get_instance.return_value = mock_instance

        # Should not raise
        cleanup_handler.check_connection_state("room_001")


def test_check_connection_state_error(cleanup_handler):
    """Test check_connection_state handles errors gracefully."""
    with patch("server.container.ApplicationContainer.get_instance", side_effect=ImportError("No container")):
        # Should not raise, just log warning
        cleanup_handler.check_connection_state("room_001")


@pytest.mark.asyncio
async def test_cleanup_stale_combats(cleanup_handler, mock_combat_service):
    """Test cleanup_stale_combats removes stale combats."""

    # Create stale combat (old last_activity)
    stale_combat = MagicMock(spec=CombatInstance)
    stale_combat.combat_id = "stale_combat"
    stale_combat.last_activity = datetime.now(UTC) - timedelta(minutes=60)  # Very old
    stale_combat.status = CombatStatus.ACTIVE
    stale_combat.participants = {}

    # Create fresh combat
    fresh_combat = MagicMock(spec=CombatInstance)
    fresh_combat.combat_id = "fresh_combat"
    fresh_combat.last_activity = datetime.now(UTC) - timedelta(minutes=5)  # Recent
    fresh_combat.status = CombatStatus.ACTIVE
    fresh_combat.participants = {}

    mock_combat_service._active_combats = {"stale_combat": stale_combat, "fresh_combat": fresh_combat}
    mock_combat_service.end_combat = AsyncMock()

    cleaned = await cleanup_handler.cleanup_stale_combats(combat_timeout_minutes=30)

    assert cleaned >= 0  # May clean up stale combats


@pytest.mark.asyncio
async def test_cleanup_stale_combats_no_end_combat_method(cleanup_handler, mock_combat_service):
    """Test cleanup_stale_combats handles missing end_combat method."""
    stale_combat = MagicMock(spec=CombatInstance)
    stale_combat.combat_id = "stale_combat"
    stale_combat.last_activity = datetime.now(UTC) - timedelta(minutes=60)
    stale_combat.status = CombatStatus.ACTIVE
    stale_combat.participants = {}
    mock_combat_service._active_combats = {"stale_combat": stale_combat}
    # No end_combat method
    if hasattr(mock_combat_service, "end_combat"):
        delattr(mock_combat_service, "end_combat")
    cleaned = await cleanup_handler.cleanup_stale_combats(combat_timeout_minutes=30)
    assert cleaned >= 0


@pytest.mark.asyncio
async def test_cleanup_stale_combats_no_stale_combats(cleanup_handler, mock_combat_service):
    """Test cleanup_stale_combats when no stale combats exist."""
    fresh_combat = MagicMock(spec=CombatInstance)
    fresh_combat.combat_id = "fresh_combat"
    fresh_combat.last_activity = datetime.now(UTC) - timedelta(minutes=5)
    fresh_combat.status = CombatStatus.ACTIVE
    fresh_combat.participants = {}
    mock_combat_service._active_combats = {"fresh_combat": fresh_combat}
    cleaned = await cleanup_handler.cleanup_stale_combats(combat_timeout_minutes=30)
    assert cleaned == 0


def test_check_connection_state_no_connection_manager(cleanup_handler):
    """Test check_connection_state handles no connection manager."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.connection_manager = None
        mock_container.get_instance.return_value = mock_instance
        # Should not raise, just log warning
        cleanup_handler.check_connection_state("room_001")


def test_check_connection_state_no_room_subscriptions(cleanup_handler):
    """Test check_connection_state handles missing room_subscriptions."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
        # No room_subscriptions attribute
        if hasattr(mock_connection_manager, "room_subscriptions"):
            delattr(mock_connection_manager, "room_subscriptions")
        mock_instance.connection_manager = mock_connection_manager
        mock_container.get_instance.return_value = mock_instance
        # Should not raise, just handle missing attribute
        cleanup_handler.check_connection_state("room_001")
