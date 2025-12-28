"""
Unit tests for event publisher.

Tests the EventPublisher class.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.event_publisher import EventPublisher


@pytest.fixture
def mock_nats_service():
    """Create a mock NATS service."""
    service = MagicMock()
    service.is_connected = MagicMock(return_value=True)
    service.publish = AsyncMock(return_value=True)
    return service


@pytest.fixture
def mock_subject_manager():
    """Create a mock subject manager."""
    manager = MagicMock()
    manager.build_subject = MagicMock(return_value="chat.say.room.room_001")
    return manager


@pytest.fixture
def event_publisher(mock_nats_service, mock_subject_manager):
    """Create an EventPublisher instance."""
    return EventPublisher(mock_nats_service, mock_subject_manager)


def test_event_publisher_init(event_publisher, mock_nats_service, mock_subject_manager):
    """Test EventPublisher initialization."""
    assert event_publisher.nats_service == mock_nats_service
    assert event_publisher.subject_manager == mock_subject_manager
    assert event_publisher.sequence_number == 0


@pytest.mark.asyncio
async def test_publish_player_entered_event_success(event_publisher, mock_nats_service):
    """Test publish_player_entered_event() successfully publishes."""
    result = await event_publisher.publish_player_entered_event("player_001", "room_001")
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_entered_event_not_connected(event_publisher, mock_nats_service):
    """Test publish_player_entered_event() when NATS is not connected."""
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await event_publisher.publish_player_entered_event("player_001", "room_001")
    assert result is False
    mock_nats_service.publish.assert_not_awaited()


@pytest.mark.asyncio
async def test_publish_player_left_event_success(event_publisher, mock_nats_service):
    """Test publish_player_left_event() successfully publishes."""
    result = await event_publisher.publish_player_left_event("player_001", "room_001")
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_game_tick_event_success(event_publisher, mock_nats_service):
    """Test publish_game_tick_event() successfully publishes."""
    result = await event_publisher.publish_game_tick_event(100)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()
