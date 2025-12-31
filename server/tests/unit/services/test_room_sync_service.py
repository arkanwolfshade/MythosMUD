"""
Unit tests for room sync service.

Tests the RoomSyncService class for room synchronization and event processing.
"""

import time
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_types import BaseEvent
from server.services.room_sync_service import RoomSyncService, get_room_sync_service


@pytest.fixture
def mock_room_service():
    """Create a mock room service."""
    service = MagicMock()
    service.get_room = AsyncMock()
    service.room_cache = MagicMock()
    service.room_cache.invalidate_room = MagicMock()
    return service


@pytest.fixture
def room_sync_service():
    """Create a RoomSyncService instance."""
    return RoomSyncService()


@pytest.fixture
def room_sync_service_with_room_service(mock_room_service):
    """Create a RoomSyncService instance with room service."""
    return RoomSyncService(room_service=mock_room_service)


@pytest.fixture
def sample_event():
    """Create a sample event."""
    event = MagicMock(spec=BaseEvent)
    event.room_id = "room_001"
    event.player_id = "player_001"
    event.timestamp = time.time()
    return event


def test_room_sync_service_init(room_sync_service):
    """Test RoomSyncService initialization."""
    assert room_sync_service._event_sequence_counter == 0
    assert room_sync_service._room_service is None
    assert room_sync_service._freshness_threshold_seconds == 5
    assert room_sync_service._room_data_cache is not None
    assert room_sync_service._validator is not None
    assert room_sync_service._fixer is not None


def test_room_sync_service_init_with_room_service(room_sync_service_with_room_service, mock_room_service):
    """Test RoomSyncService initialization with room service."""
    assert room_sync_service_with_room_service._room_service == mock_room_service


def test_set_room_service(room_sync_service, mock_room_service):
    """Test set_room_service() sets the room service."""
    room_sync_service.set_room_service(mock_room_service)
    assert room_sync_service._room_service == mock_room_service


def test_process_event_with_ordering(room_sync_service, sample_event):
    """Test process_event_with_ordering() adds sequence number to event."""
    result = room_sync_service.process_event_with_ordering(sample_event)
    assert result.sequence_number == 1
    assert room_sync_service._event_sequence_counter == 1


def test_process_event_with_ordering_increments_counter(room_sync_service, sample_event):
    """Test process_event_with_ordering() increments sequence counter."""
    room_sync_service.process_event_with_ordering(sample_event)
    room_sync_service.process_event_with_ordering(sample_event)
    assert room_sync_service._event_sequence_counter == 2


def test_process_event_with_ordering_tracks_last_processed(room_sync_service, sample_event):
    """Test process_event_with_ordering() tracks last processed events."""
    room_sync_service.process_event_with_ordering(sample_event)
    event_key = f"{sample_event.room_id}_{sample_event.player_id}"
    assert room_sync_service._last_processed_events[event_key] == 1


def test_process_event_with_ordering_handles_error(room_sync_service):
    """Test process_event_with_ordering() handles errors."""

    # Create an event object that raises an exception when sequence_number is assigned
    # This will trigger the exception handler in process_event_with_ordering
    class InvalidEvent:
        """Event class that raises exception on attribute assignment."""

        def __init__(self):
            self.room_id = "room_001"
            self.player_id = "player_001"
            self.timestamp = time.time()

        def __setattr__(self, name, value):
            if name == "sequence_number":
                raise TypeError("Cannot assign sequence_number")
            super().__setattr__(name, value)

    invalid_event = InvalidEvent()

    with pytest.raises(TypeError, match="Cannot assign sequence_number"):
        room_sync_service.process_event_with_ordering(invalid_event)


@pytest.mark.asyncio
async def test_process_room_update_with_validation_valid_data(room_sync_service_with_room_service):
    """Test _process_room_update_with_validation() processes valid room data."""
    room_data = {"id": "room_001", "name": "Test Room", "timestamp": time.time()}
    result = await room_sync_service_with_room_service._process_room_update_with_validation(room_data)
    assert result is not None
    assert "id" in result


@pytest.mark.asyncio
async def test_process_room_update_with_validation_invalid_data(room_sync_service_with_room_service):
    """Test _process_room_update_with_validation() fixes invalid room data."""
    invalid_room_data = {}  # Missing required fields
    result = await room_sync_service_with_room_service._process_room_update_with_validation(invalid_room_data)
    # Should return data (possibly fixed)
    assert result is not None


@pytest.mark.asyncio
async def test_process_room_update_with_validation_stale_data(room_sync_service_with_room_service, mock_room_service):
    """Test _process_room_update_with_validation() handles stale data."""
    stale_room_data = {"id": "room_001", "name": "Test Room", "timestamp": time.time() - 10}  # 10 seconds old
    fresh_room_data = {"id": "room_001", "name": "Test Room", "timestamp": time.time()}
    mock_room_service.get_room = AsyncMock(return_value=fresh_room_data)
    result = await room_sync_service_with_room_service._process_room_update_with_validation(stale_room_data)
    # Should handle stale data
    assert result is not None


@pytest.mark.asyncio
async def test_process_room_update_with_validation_handles_error(room_sync_service_with_room_service):
    """Test _process_room_update_with_validation() handles errors gracefully."""
    room_data = {"id": "room_001"}
    # Mock validator to raise error
    room_sync_service_with_room_service._validator.validate_room_data = MagicMock(side_effect=AttributeError("Error"))
    result = await room_sync_service_with_room_service._process_room_update_with_validation(room_data)
    # Should return original data on error
    assert result == room_data


def test_invalidate_stale_cache_success(room_sync_service_with_room_service, mock_room_service):
    """Test _invalidate_stale_cache() invalidates cache successfully."""
    result = room_sync_service_with_room_service._invalidate_stale_cache("room_001")
    assert result is True
    mock_room_service.room_cache.invalidate_room.assert_called_once_with("room_001")


def test_invalidate_stale_cache_no_room_service(room_sync_service):
    """Test _invalidate_stale_cache() returns False when room service unavailable."""
    result = room_sync_service._invalidate_stale_cache("room_001")
    assert result is False


def test_invalidate_stale_cache_error(room_sync_service_with_room_service, mock_room_service):
    """Test _invalidate_stale_cache() handles errors gracefully."""
    mock_room_service.room_cache.invalidate_room = MagicMock(side_effect=AttributeError("Error"))
    result = room_sync_service_with_room_service._invalidate_stale_cache("room_001")
    assert result is False


@pytest.mark.asyncio
async def test_fetch_fresh_room_data_success(room_sync_service_with_room_service, mock_room_service):
    """Test _fetch_fresh_room_data() fetches fresh room data."""
    fresh_data = {"id": "room_001", "name": "Test Room"}
    mock_room_service.get_room = AsyncMock(return_value=fresh_data)
    result = await room_sync_service_with_room_service._fetch_fresh_room_data("room_001")
    assert result is not None
    assert "timestamp" in result
    mock_room_service.get_room.assert_awaited_once_with("room_001")


@pytest.mark.asyncio
async def test_fetch_fresh_room_data_no_room_service(room_sync_service):
    """Test _fetch_fresh_room_data() returns None when room service unavailable."""
    result = await room_sync_service._fetch_fresh_room_data("room_001")
    assert result is None


@pytest.mark.asyncio
async def test_fetch_fresh_room_data_not_found(room_sync_service_with_room_service, mock_room_service):
    """Test _fetch_fresh_room_data() returns None when room not found."""
    mock_room_service.get_room = AsyncMock(return_value=None)
    result = await room_sync_service_with_room_service._fetch_fresh_room_data("room_001")
    assert result is None


@pytest.mark.asyncio
async def test_fetch_fresh_room_data_handles_error(room_sync_service_with_room_service, mock_room_service):
    """Test _fetch_fresh_room_data() handles errors."""
    mock_room_service.get_room = AsyncMock(side_effect=AttributeError("Error"))
    with pytest.raises(AttributeError):
        await room_sync_service_with_room_service._fetch_fresh_room_data("room_001")


@pytest.mark.asyncio
async def test_handle_stale_room_data_success(room_sync_service_with_room_service, mock_room_service):
    """Test _handle_stale_room_data() handles stale data successfully."""
    stale_data = {"id": "room_001", "timestamp": time.time() - 10}
    fresh_data = {"id": "room_001", "name": "Test Room", "timestamp": time.time()}
    mock_room_service.get_room = AsyncMock(return_value=fresh_data)
    result = await room_sync_service_with_room_service._handle_stale_room_data(stale_data)
    assert result["action_taken"] == "request_fresh_data"
    assert result.get("fresh_data_fetched") is True


@pytest.mark.asyncio
async def test_handle_stale_room_data_invalid_room_id(room_sync_service_with_room_service):
    """Test _handle_stale_room_data() handles invalid room_id."""
    invalid_data = {"id": None}  # Invalid room_id
    result = await room_sync_service_with_room_service._handle_stale_room_data(invalid_data)
    assert result["action_taken"] == "error"
    assert "invalid_room_id_type" in result["reason"]


@pytest.mark.asyncio
async def test_handle_stale_room_data_no_room_service(room_sync_service):
    """Test _handle_stale_room_data() handles missing room service."""
    stale_data = {"id": "room_001", "timestamp": time.time() - 10}
    result = await room_sync_service._handle_stale_room_data(stale_data)
    assert result["fresh_data_fetched"] is False
    assert "room_service_not_available" in result["reason"]


@pytest.mark.asyncio
async def test_process_room_transition_success(room_sync_service):
    """Test _process_room_transition() processes transition successfully."""
    transition_data = {"player_id": "player_001", "from_room": "room_001", "to_room": "room_002"}
    result = await room_sync_service._process_room_transition(transition_data)
    assert result["success"] is True
    assert result["player_id"] == "player_001"
    assert result["to_room"] == "room_002"


@pytest.mark.asyncio
async def test_process_room_transition_missing_data(room_sync_service):
    """Test _process_room_transition() handles missing data."""
    transition_data = {"player_id": "player_001"}  # Missing from_room and to_room
    result = await room_sync_service._process_room_transition(transition_data)
    assert result["success"] is False
    assert "errors" in result


@pytest.mark.asyncio
async def test_process_room_transition_handles_error(room_sync_service):
    """Test _process_room_transition() handles errors gracefully."""
    invalid_data = None  # Invalid input
    result = await room_sync_service._process_room_transition(invalid_data)
    assert result["success"] is False
    assert "errors" in result


def test_get_room_data_cache_stats(room_sync_service):
    """Test get_room_data_cache_stats() returns cache statistics."""
    stats = room_sync_service.get_room_data_cache_stats()
    assert "total_events_processed" in stats
    assert stats["total_events_processed"] == 0
    assert "active_update_locks" in stats


def test_get_room_data_cache_stats_with_events(room_sync_service, sample_event):
    """Test get_room_data_cache_stats() includes event count."""
    room_sync_service.process_event_with_ordering(sample_event)
    stats = room_sync_service.get_room_data_cache_stats()
    assert stats["total_events_processed"] == 1


def test_clear_cache_specific_room(room_sync_service):
    """Test clear_cache() clears specific room cache."""
    # Should not raise
    room_sync_service.clear_cache("room_001")


def test_clear_cache_all(room_sync_service):
    """Test clear_cache() clears all cache when room_id is None."""
    # Should not raise
    room_sync_service.clear_cache()


def test_get_room_sync_service_returns_singleton():
    """Test get_room_sync_service() returns singleton instance."""
    service1 = get_room_sync_service()
    service2 = get_room_sync_service()
    assert service1 is service2
