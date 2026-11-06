"""
Unit tests for combat persistence handler - event publishing.

Tests DP update and correction event publishing functionality.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.combat_persistence_handler import CombatPersistenceHandler
from server.services.nats_exceptions import NATSError

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def persistence_handler(mock_combat_service):
    """Create CombatPersistenceHandler instance."""
    return CombatPersistenceHandler(mock_combat_service)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event(persistence_handler):
    """Test publish_player_dp_update_event publishes event."""
    player_id = uuid.uuid4()
    with patch.object(
        persistence_handler, "_publish_player_dp_update_event_impl", new_callable=AsyncMock
    ) as mock_publish:
        await persistence_handler.publish_player_dp_update_event(player_id, 50, 30, 100)
        mock_publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl publishes to event bus."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_no_event_bus(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles no event bus."""
    player_id = uuid.uuid4()
    mock_combat_service._event_bus = None
    # Should not raise, just log warning
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=ValueError("Event bus error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_with_nats(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl publishes to NATS when available."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_subject_manager = MagicMock()
    mock_subject_manager.build_subject = MagicMock(return_value="combat.dp_update.test")
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    mock_combat_service._combat_event_publisher = MagicMock()
    mock_combat_service._combat_event_publisher.subject_manager = mock_subject_manager
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_legacy_subject(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl uses legacy subject when subject_manager unavailable."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    mock_combat_service._combat_event_publisher = None  # No subject manager
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    # Should still publish to NATS with legacy subject
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_nats_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles NATS errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_nats_service.publish = AsyncMock(side_effect=ValueError("NATS error"))
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_no_nats(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles no NATS service."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = None
    # Should not raise, just log warning
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_all_parameters(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl with all optional parameters."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100, "combat_001", "room_001")
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_event_bus_publish_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles event bus publish error."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=NATSError("Event bus error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
