"""
Unit tests for combat event publisher.

Tests the CombatEventPublisher class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.combat_event_publisher import CombatEventPublisher

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


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
    from typing import Any

    from server.events.combat_events import CombatStartedEvent

    combat_id = uuid.uuid4()
    room_id = "room_001"
    participants: dict[str, Any] = {"player_001": {}, "npc_001": {}}
    turn_order = ["player_001", "npc_001"]
    event = CombatStartedEvent(
        combat_id=combat_id,
        room_id=room_id,
        participants=participants,
        turn_order=turn_order,
    )
    result = await combat_event_publisher.publish_combat_started(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_started_not_connected(combat_event_publisher, mock_nats_service):
    """Test publish_combat_started() when NATS is not connected."""
    from server.events.combat_events import CombatStartedEvent

    combat_id = uuid.uuid4()
    event = CombatStartedEvent(
        combat_id=combat_id,
        room_id="room_001",
        participants={},
        turn_order=[],
    )
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await combat_event_publisher.publish_combat_started(event)
    assert result is False


def test_combat_event_publisher_initialization_with_nats_service():
    """Test CombatEventPublisher initializes with provided nats_service."""
    mock_nats = MagicMock()
    publisher = CombatEventPublisher(nats_service=mock_nats)
    assert publisher.nats_service is mock_nats


def test_combat_event_publisher_initialization_with_subject_manager():
    """Test CombatEventPublisher initializes with subject_manager."""
    mock_nats = MagicMock()
    mock_subject_manager = MagicMock()
    publisher = CombatEventPublisher(nats_service=mock_nats, subject_manager=mock_subject_manager)
    assert publisher.subject_manager is mock_subject_manager


def test_create_event_message_with_room_id(combat_event_publisher):
    """Test _create_event_message() includes room_id when provided."""
    message = combat_event_publisher._create_event_message("test_event", {"key": "value"}, room_id="room_001")
    assert message["room_id"] == "room_001"


def test_create_event_message_with_player_id(combat_event_publisher):
    """Test _create_event_message() includes player_id when provided."""
    message = combat_event_publisher._create_event_message("test_event", {"key": "value"}, player_id="player_001")
    assert message["player_id"] == "player_001"


def test_create_event_message_with_timestamp(combat_event_publisher):
    """Test _create_event_message() uses provided timestamp."""
    custom_timestamp = "2024-01-01T00:00:00Z"
    message = combat_event_publisher._create_event_message("test_event", {"key": "value"}, timestamp=custom_timestamp)
    assert message["timestamp"] == custom_timestamp


def test_create_event_message_with_all_optional_fields(combat_event_publisher):
    """Test _create_event_message() includes all optional fields."""
    message = combat_event_publisher._create_event_message(
        "test_event", {"key": "value"}, room_id="room_001", player_id="player_001", timestamp="2024-01-01T00:00:00Z"
    )
    assert message["room_id"] == "room_001"
    assert message["player_id"] == "player_001"
    assert message["timestamp"] == "2024-01-01T00:00:00Z"


@pytest.mark.asyncio
async def test_publish_combat_started_no_nats_service():
    """Test publish_combat_started() when NATS service is None."""
    from server.events.combat_events import CombatStartedEvent

    publisher = CombatEventPublisher(nats_service=None)
    combat_id = uuid.uuid4()
    event = CombatStartedEvent(
        combat_id=combat_id,
        room_id="room_001",
        participants={},
        turn_order=[],
    )
    result = await publisher.publish_combat_started(event)
    assert result is False


@pytest.mark.asyncio
async def test_publish_combat_started_nats_error(combat_event_publisher, mock_nats_service):
    """Test publish_combat_started() handles NATS publish error."""
    from server.events.combat_events import CombatStartedEvent
    from server.services.nats_exceptions import NATSPublishError

    combat_id = uuid.uuid4()
    event = CombatStartedEvent(
        combat_id=combat_id,
        room_id="room_001",
        participants={},
        turn_order=[],
    )
    mock_nats_service.publish = AsyncMock(side_effect=NATSPublishError("Publish failed"))
    result = await combat_event_publisher.publish_combat_started(event)
    assert result is False


@pytest.mark.asyncio
async def test_publish_combat_ended_success(combat_event_publisher, mock_nats_service):
    """Test publish_combat_ended() successfully publishes."""
    from server.events.combat_events import CombatEndedEvent

    combat_id = uuid.uuid4()
    event = CombatEndedEvent(
        combat_id=combat_id,
        room_id="room_001",
        reason="victory",
        duration_seconds=60,
        participants=[],  # type: ignore[arg-type]
    )
    result = await combat_event_publisher.publish_combat_ended(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_ended_not_connected(combat_event_publisher, mock_nats_service):
    """Test publish_combat_ended() when NATS is not connected."""
    from server.events.combat_events import CombatEndedEvent

    combat_id = uuid.uuid4()
    event = CombatEndedEvent(
        combat_id=combat_id,
        room_id="room_001",
        reason="victory",
        duration_seconds=60,
        participants=[],  # type: ignore[arg-type]
    )
    mock_nats_service.is_connected = MagicMock(return_value=False)
    result = await combat_event_publisher.publish_combat_ended(event)
    assert result is False


@pytest.mark.asyncio
async def test_publish_player_attacked_success(combat_event_publisher, mock_nats_service):
    """Test publish_player_attacked() successfully publishes."""
    from server.events.combat_events import PlayerAttackedEvent

    combat_id = uuid.uuid4()
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    event = PlayerAttackedEvent(
        combat_id=combat_id,
        room_id="room_001",
        attacker_id=attacker_id,
        attacker_name="Attacker",
        target_id=target_id,
        target_name="Target",
        damage=10,
        action_type="attack",
        target_current_dp=90,
        target_max_dp=100,
    )
    result = await combat_event_publisher.publish_player_attacked(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_attacked_success(combat_event_publisher, mock_nats_service):
    """Test publish_npc_attacked() successfully publishes."""
    from server.events.combat_events import NPCAttackedEvent

    combat_id = uuid.uuid4()
    attacker_id = uuid.uuid4()
    npc_id = "npc_001"
    event = NPCAttackedEvent(
        combat_id=combat_id,
        room_id="room_001",
        attacker_id=attacker_id,
        attacker_name="Attacker",
        npc_id=npc_id,  # type: ignore[arg-type]
        npc_name="NPC",
        damage=10,
        action_type="attack",
        target_current_dp=90,
        target_max_dp=100,
    )
    result = await combat_event_publisher.publish_npc_attacked(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_took_damage_success(combat_event_publisher, mock_nats_service):
    """Test publish_npc_took_damage() successfully publishes."""
    from server.events.combat_events import NPCTookDamageEvent

    combat_id = uuid.uuid4()
    npc_id = "npc_001"
    event = NPCTookDamageEvent(
        combat_id=combat_id,
        room_id="room_001",
        npc_id=npc_id,  # type: ignore[arg-type]
        npc_name="NPC",
        damage=10,
        current_dp=90,
        max_dp=100,
    )
    result = await combat_event_publisher.publish_npc_took_damage(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_died_success(combat_event_publisher, mock_nats_service):
    """Test publish_npc_died() successfully publishes."""
    from server.events.combat_events import NPCDiedEvent

    combat_id = uuid.uuid4()
    npc_id = "npc_001"
    event = NPCDiedEvent(combat_id=combat_id, room_id="room_001", npc_id=npc_id, npc_name="NPC", xp_reward=100)
    result = await combat_event_publisher.publish_npc_died(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_turn_advanced_success(combat_event_publisher, mock_nats_service):
    """Test publish_combat_turn_advanced() successfully publishes."""
    from server.events.combat_events import CombatTurnAdvancedEvent

    combat_id = uuid.uuid4()
    event = CombatTurnAdvancedEvent(
        combat_id=combat_id, room_id="room_001", current_turn=1, combat_round=1, next_participant="player_001"
    )
    result = await combat_event_publisher.publish_combat_turn_advanced(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_timeout_success(combat_event_publisher, mock_nats_service):
    """Test publish_combat_timeout() successfully publishes."""
    from server.events.combat_events import CombatTimeoutEvent

    combat_id = uuid.uuid4()
    event = CombatTimeoutEvent(
        combat_id=combat_id,
        room_id="room_001",
        timeout_minutes=5,
        last_activity=None,  # type: ignore[arg-type]
    )
    result = await combat_event_publisher.publish_combat_timeout(event)
    assert result is True
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_combat_ended_no_nats_service():
    """Test publish_combat_ended() when NATS service is None."""
    from server.events.combat_events import CombatEndedEvent

    publisher = CombatEventPublisher(nats_service=None)
    combat_id = uuid.uuid4()
    event = CombatEndedEvent(
        combat_id=combat_id,
        room_id="room_001",
        reason="victory",
        duration_seconds=60,
        participants=[],  # type: ignore[arg-type]
    )
    result = await publisher.publish_combat_ended(event)
    assert result is False


@pytest.mark.asyncio
async def test_publish_player_attacked_no_nats_service():
    """Test publish_player_attacked() when NATS service is None."""
    from server.events.combat_events import PlayerAttackedEvent

    publisher = CombatEventPublisher(nats_service=None)
    combat_id = uuid.uuid4()
    attacker_id = uuid.uuid4()
    target_id = uuid.uuid4()
    event = PlayerAttackedEvent(
        combat_id=combat_id,
        room_id="room_001",
        attacker_id=attacker_id,
        attacker_name="Attacker",
        target_id=target_id,
        target_name="Target",
        damage=10,
        action_type="attack",
        target_current_dp=90,
        target_max_dp=100,
    )
    result = await publisher.publish_player_attacked(event)
    assert result is False
