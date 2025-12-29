"""
Unit tests for corpse lifecycle service.

Tests the CorpseLifecycleService class.
"""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
    _get_enum_value,
)


def test_get_enum_value_enum():
    """Test _get_enum_value() with enum instance."""
    from enum import Enum

    class TestEnum(Enum):
        VALUE1 = "value1"

    result = _get_enum_value(TestEnum.VALUE1)
    assert result == "value1"


def test_get_enum_value_string():
    """Test _get_enum_value() with string."""
    result = _get_enum_value("test_string")
    assert result == "test_string"


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def corpse_service(mock_persistence):
    """Create a CorpseLifecycleService instance."""
    return CorpseLifecycleService(persistence=mock_persistence)


def test_corpse_lifecycle_service_init(corpse_service, mock_persistence):
    """Test CorpseLifecycleService initialization."""
    assert corpse_service.persistence == mock_persistence


def test_corpse_lifecycle_service_init_no_persistence():
    """Test CorpseLifecycleService initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        CorpseLifecycleService(persistence=None)


def test_corpse_service_error():
    """Test CorpseServiceError exception."""
    error = CorpseServiceError("Test error")
    assert str(error) == "Test error"


def test_corpse_not_found_error():
    """Test CorpseNotFoundError exception."""
    error = CorpseNotFoundError("Corpse not found")
    assert isinstance(error, CorpseServiceError)
    assert str(error) == "Corpse not found"


@pytest.mark.asyncio
async def test_create_corpse_on_death_success(corpse_service, mock_persistence):
    """Test create_corpse_on_death() successfully creates corpse."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory.return_value = [{"item_id": "item_001", "quantity": 1}]
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(
        return_value={"container_id": str(uuid.uuid4()), "room_id": room_id}
    )
    result = await corpse_service.create_corpse_on_death(player_id, room_id)
    assert isinstance(result, ContainerComponent)
    assert result.source_type == ContainerSourceType.CORPSE
    assert result.owner_id == player_id
    assert result.room_id == room_id
    mock_persistence.get_player_by_id.assert_awaited_once_with(player_id)
    mock_persistence.create_container.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_corpse_on_death_player_not_found(corpse_service, mock_persistence):
    """Test create_corpse_on_death() raises error when player not found."""
    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(CorpseServiceError, match="Player not found"):
        await corpse_service.create_corpse_on_death(player_id, "room_001")


@pytest.mark.asyncio
async def test_create_corpse_on_death_persistence_error(corpse_service, mock_persistence):
    """Test create_corpse_on_death() handles persistence errors."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.get_inventory.return_value = []
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(side_effect=Exception("Database error"))
    with pytest.raises(CorpseServiceError, match="Failed to create corpse container"):
        await corpse_service.create_corpse_on_death(player_id, "room_001")


def test_can_access_corpse_admin(corpse_service):
    """Test can_access_corpse() allows admin access."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=True)
    assert result is True


def test_can_access_corpse_owner(corpse_service):
    """Test can_access_corpse() allows owner access."""
    owner_id = uuid.uuid4()
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, owner_id, is_admin=False)
    assert result is True


def test_can_access_corpse_no_owner(corpse_service):
    """Test can_access_corpse() allows access when no owner."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=None,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


def test_can_access_corpse_grace_period_active(corpse_service):
    """Test can_access_corpse() blocks access during grace period."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    now = datetime.now(UTC)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={
            "grace_period_seconds": 300,
            "grace_period_start": now.isoformat(),
        },
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is False


def test_can_access_corpse_grace_period_expired(corpse_service):
    """Test can_access_corpse() allows access after grace period."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    past_time = datetime.now(UTC) - timedelta(seconds=400)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={
            "grace_period_seconds": 300,
            "grace_period_start": past_time.isoformat(),
        },
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is True


def test_can_access_corpse_invalid_grace_period(corpse_service):
    """Test can_access_corpse() handles invalid grace period gracefully."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_start": "invalid"},
    )
    # Should fail open and allow access
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


def test_is_corpse_decayed_not_decayed(corpse_service):
    """Test is_corpse_decayed() returns False for non-decayed corpse."""
    future_time = datetime.now(UTC) + timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=future_time,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is False


def test_is_corpse_decayed_decayed(corpse_service):
    """Test is_corpse_decayed() returns True for decayed corpse."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=past_time,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def test_is_corpse_decayed_no_decay_time(corpse_service):
    """Test is_corpse_decayed() returns False when no decay time."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=None,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is False


def test_is_corpse_decayed_with_time_service(corpse_service):
    """Test is_corpse_decayed() uses time service when available."""
    mock_time_service = MagicMock()
    mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC) + timedelta(hours=2)
    corpse_service.time_service = mock_time_service
    past_time = datetime.now(UTC) - timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=past_time,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True
    mock_time_service.get_current_mythos_datetime.assert_called_once()


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_empty(corpse_service, mock_persistence):
    """Test get_decayed_corpses_in_room() returns empty list when no containers."""
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    result = await corpse_service.get_decayed_corpses_in_room("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_with_decayed(corpse_service, mock_persistence):
    """Test get_decayed_corpses_in_room() returns decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "corpse",
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": past_time,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[container_data])
    result = await corpse_service.get_decayed_corpses_in_room("room_001")
    assert len(result) == 1
    assert result[0].source_type == ContainerSourceType.CORPSE


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_success(corpse_service, mock_persistence):
    """Test cleanup_decayed_corpse() successfully deletes corpse."""
    container_id = uuid.uuid4()
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data = {
        "container_id": str(container_id),
        "source_type": "corpse",
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": past_time,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.delete_container = AsyncMock()
    await corpse_service.cleanup_decayed_corpse(container_id)
    mock_persistence.delete_container.assert_awaited_once_with(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_not_found(corpse_service, mock_persistence):
    """Test cleanup_decayed_corpse() raises error when corpse not found."""
    container_id = uuid.uuid4()
    mock_persistence.get_container = AsyncMock(return_value=None)
    with pytest.raises(CorpseNotFoundError):
        await corpse_service.cleanup_decayed_corpse(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_not_corpse(corpse_service, mock_persistence):
    """Test cleanup_decayed_corpse() raises error when container is not a corpse."""
    container_id = uuid.uuid4()
    # Use a valid source_type that's not CORPSE
    from server.models.container import ContainerSourceType
    container_data = {
        "container_id": str(container_id),
        "source_type": ContainerSourceType.ENVIRONMENT.value,
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": None,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    with pytest.raises(CorpseServiceError, match="Container is not a corpse"):
        await corpse_service.cleanup_decayed_corpse(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_in_room(corpse_service, mock_persistence):
    """Test cleanup_decayed_corpses_in_room() cleans up multiple corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "corpse",
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": past_time,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[container_data])
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.delete_container = AsyncMock()
    result = await corpse_service.cleanup_decayed_corpses_in_room("room_001")
    assert result == 1
    mock_persistence.delete_container.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_all_decayed_corpses(corpse_service, mock_persistence):
    """Test get_all_decayed_corpses() returns all decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "corpse",
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": past_time,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_decayed_containers = AsyncMock(return_value=[container_data])
    result = await corpse_service.get_all_decayed_corpses()
    assert len(result) == 1
    assert result[0].source_type == ContainerSourceType.CORPSE


@pytest.mark.asyncio
async def test_cleanup_all_decayed_corpses(corpse_service, mock_persistence):
    """Test cleanup_all_decayed_corpses() cleans up all decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data = {
        "container_id": str(uuid.uuid4()),
        "source_type": "corpse",
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": past_time,
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_decayed_containers = AsyncMock(return_value=[container_data])
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.delete_container = AsyncMock()
    result = await corpse_service.cleanup_all_decayed_corpses()
    assert result == 1
    mock_persistence.delete_container.assert_awaited_once()
