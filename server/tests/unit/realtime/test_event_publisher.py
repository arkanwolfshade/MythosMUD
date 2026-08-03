"""
Unit tests for event publisher.

Tests the EventPublisher class.
"""

from unittest.mock import AsyncMock, MagicMock, patch

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


@pytest.mark.asyncio
async def test_publish_player_entered_event_with_metadata(event_publisher, mock_nats_service):
    """Test publish_player_entered_event() with additional metadata."""
    metadata = {"source": "test"}
    result = await event_publisher.publish_player_entered_event("player_001", "room_001", additional_metadata=metadata)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_entered_event_nats_error(event_publisher, mock_nats_service):
    """Test publish_player_entered_event() handles NATS errors."""
    mock_nats_service.publish = AsyncMock(side_effect=Exception("NATS error"))
    result = await event_publisher.publish_player_entered_event("player_001", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_publish_player_left_event_not_connected(event_publisher, mock_nats_service):
    """Test publish_player_left_event() when NATS is not connected."""
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await event_publisher.publish_player_left_event("player_001", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_publish_game_tick_event_not_connected(event_publisher, mock_nats_service):
    """Test publish_game_tick_event() when NATS is not connected."""
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await event_publisher.publish_game_tick_event(100)
    assert result is False


def test_get_next_sequence_number(event_publisher):
    """Test get_next_sequence_number() returns and increments sequence."""
    seq1 = event_publisher.get_next_sequence_number()
    seq2 = event_publisher.get_next_sequence_number()
    assert seq2 == seq1 + 1


def test_reset_sequence_number(event_publisher):
    """Test reset_sequence_number() resets sequence to 0."""
    event_publisher.get_next_sequence_number()
    event_publisher.reset_sequence_number()
    assert event_publisher.sequence_number == 0


def test_event_publisher_init_without_subject_manager(mock_nats_service):
    """Test EventPublisher initialization without subject manager."""
    publisher = EventPublisher(mock_nats_service, None)
    assert publisher.nats_service == mock_nats_service
    assert publisher.subject_manager is None


def test_event_publisher_init_with_initial_sequence(mock_nats_service, mock_subject_manager):
    """Test EventPublisher initialization with initial sequence."""
    publisher = EventPublisher(mock_nats_service, mock_subject_manager, initial_sequence=10)
    assert publisher.sequence_number == 10


@pytest.mark.asyncio
async def test_publish_player_entered_resolves_names_from_persistence(mock_nats_service, mock_subject_manager):
    """Persistence lookup should replace Player_/Room_ fallbacks in event data."""
    publisher = EventPublisher(mock_nats_service, mock_subject_manager)
    player = MagicMock()
    player.name = "Investigator"
    room = MagicMock()
    room.name = "Miskatonic Library"
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    persistence.get_room_by_id = MagicMock(return_value=room)
    publisher._async_persistence = persistence

    player_id = "11111111-1111-1111-1111-111111111111"
    result = await publisher.publish_player_entered_event(player_id, "room_001")
    assert result is True
    payload = mock_nats_service.publish.await_args.args[1]
    assert payload["data"]["player_name"] == "Investigator"
    assert payload["data"]["room_name"] == "Miskatonic Library"


@pytest.mark.asyncio
async def test_publish_player_left_resolves_names_from_persistence(mock_nats_service, mock_subject_manager):
    """Same persistence name resolution path for player_left."""
    publisher = EventPublisher(mock_nats_service, mock_subject_manager)
    player = MagicMock()
    player.name = "Cultist"
    room = MagicMock()
    room.name = "Wharf"
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    persistence.get_room_by_id = MagicMock(return_value=room)
    publisher._async_persistence = persistence

    player_id = "22222222-2222-2222-2222-222222222222"
    result = await publisher.publish_player_left_event(player_id, "room_002")
    assert result is True
    payload = mock_nats_service.publish.await_args.args[1]
    assert payload["data"]["player_name"] == "Cultist"
    assert payload["data"]["room_name"] == "Wharf"


@pytest.mark.asyncio
async def test_publish_uses_legacy_subjects_without_subject_manager(mock_nats_service):
    """Legacy subject strings when subject_manager is unset."""
    publisher = EventPublisher(mock_nats_service, None)
    assert await publisher.publish_player_entered_event("p1", "r1") is True
    assert mock_nats_service.publish.await_args.args[0] == "events.player_entered.r1"

    mock_nats_service.publish.reset_mock()
    assert await publisher.publish_player_left_event("p1", "r1") is True
    assert mock_nats_service.publish.await_args.args[0] == "events.player_left.r1"

    mock_nats_service.publish.reset_mock()
    assert await publisher.publish_game_tick_event() is True
    assert mock_nats_service.publish.await_args.args[0] == "events.game_tick"


@pytest.mark.asyncio
async def test_publish_game_tick_uses_metadata_tick_number(mock_nats_service, mock_subject_manager):
    """tick_number from additional_metadata should win over sequence."""
    publisher = EventPublisher(mock_nats_service, mock_subject_manager)
    result = await publisher.publish_game_tick_event(additional_metadata={"tick_number": 42})
    assert result is True
    payload = mock_nats_service.publish.await_args.args[1]
    assert payload["data"]["tick_number"] == 42


@pytest.mark.asyncio
async def test_publish_returns_false_when_nats_publish_fails(mock_nats_service, mock_subject_manager):
    """publish() returning False should surface as False from EventPublisher."""
    mock_nats_service.publish = AsyncMock(return_value=False)
    publisher = EventPublisher(mock_nats_service, mock_subject_manager)
    assert await publisher.publish_player_entered_event("p1", "r1") is False
    assert await publisher.publish_player_left_event("p1", "r1") is False
    assert await publisher.publish_game_tick_event() is False


def test_get_async_persistence_handles_container_failure(mock_nats_service, mock_subject_manager):
    """Container lookup failures should leave async_persistence unset."""
    publisher = EventPublisher(mock_nats_service, mock_subject_manager)
    publisher._async_persistence = None
    with patch(
        "server.container.ApplicationContainer.get_instance",
        side_effect=RuntimeError("no container"),
    ):
        assert publisher._get_async_persistence() is None
