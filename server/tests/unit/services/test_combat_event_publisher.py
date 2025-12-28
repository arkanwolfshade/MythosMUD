"""
Unit tests for combat event publisher.

Tests the CombatEventPublisher class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.combat_event_publisher import CombatEventPublisher


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
    return MagicMock()
    manager = MagicMock()
    manager.build_subject = MagicMock(return_value="combat.started.room.room_001")
    return manager


@pytest.fixture
def combat_event_publisher(mock_nats_service, mock_subject_manager):
    """Create a CombatEventPublisher instance."""
    return CombatEventPublisher(mock_nats_service, mock_subject_manager)


def test_combat_event_publisher_init(combat_event_publisher, mock_nats_service, mock_subject_manager):
    """Test CombatEventPublisher initialization."""
    assert combat_event_publisher.nats_service == mock_nats_service
    assert combat_event_publisher.subject_manager == mock_subject_manager


def test_create_event_message(combat_event_publisher):
    """Test _create_event_message() creates event message."""
    event_data = {"combat_id": "combat_001", "participants": ["player_001"]}
    result = combat_event_publisher._create_event_message("combat_started", event_data, room_id="room_001")
    assert "message_id" in result
    assert "timestamp" in result
    assert result["event_type"] == "combat_started"
    assert result["event_data"] == event_data
    assert result["room_id"] == "room_001"


@pytest.mark.asyncio
async def test_publish_combat_started_success(combat_event_publisher, mock_nats_service):
    """Test publish_combat_started() successfully publishes."""
    from server.events.combat_events import CombatStartedEvent

    combat_id = uuid.uuid4()
    room_id = "room_001"
    participants = ["player_001", "npc_001"]
    event = CombatStartedEvent(combat_id=combat_id, room_id=room_id, participants=participants, turn_order=participants)
    result = await combat_event_publisher.publish_combat_started(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_started_not_connected(combat_event_publisher, mock_nats_service):
    """Test publish_combat_started() when NATS is not connected."""
    from server.events.combat_events import CombatStartedEvent

    combat_id = uuid.uuid4()
    event = CombatStartedEvent(combat_id=combat_id, room_id="room_001", participants=[], turn_order=[])
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await combat_event_publisher.publish_combat_started(event)
    assert result is False
