"""
Unit tests for corpse lifecycle service.

Tests the CorpseLifecycleService class.
"""
# pylint: disable=redefined-outer-name,too-many-lines  # Reason: Pytest fixtures use fixture names as parameters. Comprehensive test file with many test cases.

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
    _get_enum_value,
)


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def corpse_service(mock_persistence):
    """Create a CorpseLifecycleService instance."""
    return CorpseLifecycleService(persistence=mock_persistence)


def test_get_enum_value_enum():
    """Test _get_enum_value() with enum instance."""
    from enum import Enum

    class TestEnum(Enum):
        """Test enum for _get_enum_value() tests."""

        VALUE1 = "value1"

    result = _get_enum_value(TestEnum.VALUE1)
    assert result == "value1"


def test_get_enum_value_string():
    """Test _get_enum_value() with string."""
    result = _get_enum_value("test_string")
    assert result == "test_string"


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
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    result = await corpse_service.create_corpse_on_death(player_id, room_id)
    assert isinstance(result, ContainerComponent)
    assert result.source_type == ContainerSourceType.CORPSE
    assert result.owner_id == player_id
    assert result.room_id == room_id
    mock_persistence.get_player_by_id.assert_awaited_once_with(player_id)
    mock_persistence.create_container.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_corpse_on_death_emits_container_created(mock_persistence: MagicMock) -> None:
    """create_corpse_on_death must broadcast container.created so room occupants see the corpse."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory = MagicMock(return_value=[{"item_id": "item_001", "quantity": 1}])
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    connection_manager = MagicMock()
    connection_manager.broadcast_room_event = AsyncMock(return_value={"sent": 1})
    service = CorpseLifecycleService(persistence=mock_persistence, connection_manager=connection_manager)

    corpse = await service.create_corpse_on_death(player_id, room_id)

    broadcast: AsyncMock = cast(AsyncMock, connection_manager.broadcast_room_event)
    broadcast.assert_awaited_once()
    call_args = broadcast.call_args
    assert call_args is not None
    assert call_args.kwargs["event_type"] == "container.created"
    assert call_args.kwargs["room_id"] == room_id
    data = cast(dict[str, object], call_args.kwargs["data"])
    container_payload = cast(dict[str, object], data["container"])
    # mode="json" so the payload is actually websocket-safe (UUID/datetime -> str); see #711.
    assert container_payload["container_id"] == str(corpse.container_id)


@pytest.mark.asyncio
async def test_create_corpse_on_death_no_connection_manager_skips_emit(mock_persistence: MagicMock) -> None:
    """No connection_manager configured must not raise; corpse creation still succeeds."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    service = CorpseLifecycleService(persistence=mock_persistence, connection_manager=None)

    result = await service.create_corpse_on_death(player_id, room_id)

    assert isinstance(result, ContainerComponent)


@pytest.mark.asyncio
async def test_create_corpse_on_death_emit_error_does_not_fail_creation(mock_persistence: MagicMock) -> None:
    """A broken connection_manager must not stop the corpse from being created."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    connection_manager = MagicMock()
    connection_manager.broadcast_room_event = AsyncMock(side_effect=RuntimeError("boom"))
    service = CorpseLifecycleService(persistence=mock_persistence, connection_manager=connection_manager)

    result = await service.create_corpse_on_death(player_id, room_id)

    assert isinstance(result, ContainerComponent)


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


def test_is_corpse_decayed_uses_real_time_not_mythos_time(corpse_service):
    """Test is_corpse_decayed() uses real UTC time, not Mythos time, even when time service is available."""
    mock_time_service = MagicMock()
    # Mock Mythos time to be far in the future (simulating accelerated time)
    mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC) + timedelta(days=10)
    corpse_service.time_service = mock_time_service

    # Corpse decay_at is 1 hour in the past (real time)
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

    # Should use real time, so corpse should be decayed (1 hour past)
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True

    # Verify time service was NOT called (we use real UTC time, not Mythos time)
    mock_time_service.get_current_mythos_datetime.assert_not_called()


def test_can_access_corpse_no_grace_period_start(corpse_service):
    """Test can_access_corpse() allows access when grace_period_start is missing."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_seconds": 300},  # No grace_period_start
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is True


def test_can_access_corpse_grace_period_type_error(corpse_service):
    """Test can_access_corpse() handles TypeError in grace period parsing."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_start": None},  # None causes TypeError
    )
    # Should fail open and allow access
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


@pytest.mark.asyncio
async def test_create_corpse_on_death_player_no_name(corpse_service, mock_persistence):
    """Test create_corpse_on_death() handles player without name attribute."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory.return_value = []
    # Player has no name attribute
    del mock_player.name
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    result = await corpse_service.create_corpse_on_death(player_id, room_id)
    assert isinstance(result, ContainerComponent)
    # Should use "Unknown" as default name
    assert result.metadata.get("player_name") == "Unknown"


@pytest.mark.asyncio
async def test_create_corpse_on_death_custom_grace_period(corpse_service, mock_persistence):
    """Test create_corpse_on_death() uses custom grace period."""
    player_id = uuid.uuid4()
    room_id = "room_001"
    mock_player = MagicMock()
    mock_player.get_inventory.return_value = []
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.create_container = AsyncMock(return_value={"container_id": str(uuid.uuid4()), "room_id": room_id})
    result = await corpse_service.create_corpse_on_death(player_id, room_id, grace_period_seconds=600, decay_hours=2)
    assert isinstance(result, ContainerComponent)
    assert result.metadata.get("grace_period_seconds") == 600
    assert result.decay_at is not None


def test_is_corpse_decayed_timezone_aware(corpse_service):
    """Test is_corpse_decayed() works correctly with timezone-aware datetimes."""
    # Create decay_at with timezone-aware UTC datetime
    decay_at = datetime.now(UTC) - timedelta(hours=1)
    assert decay_at.tzinfo is not None, "decay_at should be timezone-aware"

    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=decay_at,
    )

    # Should correctly identify as decayed
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def test_is_corpse_decayed_timezone_naive_vs_aware(corpse_service):
    """Test is_corpse_decayed() handles timezone-aware decay_at correctly."""
    # Even if decay_at is timezone-naive (edge case), comparison should work
    # This tests the robustness of the decay check

    # Create a timezone-naive datetime (shouldn't happen in practice, but test edge case)
    naive_decay_at = datetime.now(UTC).replace(tzinfo=None) - timedelta(hours=1)

    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=naive_decay_at,
    )

    # Should still work - datetime comparison handles naive vs aware
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def _corpse_component(room_id: str = "room_001") -> ContainerComponent:
    return ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id=room_id,
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=datetime.now(UTC) + timedelta(hours=1),
        items=[],
        metadata={"grace_period_seconds": 300, "player_name": "TestPlayer"},
    )


def test_register_corpse_on_room_adds_summary(mock_persistence: MagicMock) -> None:
    """#711: the owner is dead when container.created fires, so room_state must carry the corpse."""
    room = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    service = CorpseLifecycleService(persistence=mock_persistence)
    corpse = _corpse_component()

    service._register_corpse_on_room(corpse, "room_001")  # pyright: ignore[reportPrivateUsage]

    summary = cast(dict[str, object], cast(MagicMock, room.add_container).call_args.args[0])
    assert summary["container_id"] == str(corpse.container_id)
    assert summary["source_type"] == "corpse"
    assert summary["owner_id"] == str(corpse.owner_id)


def test_register_corpse_on_room_skips_async_room_lookup(mock_persistence: MagicMock) -> None:
    """An awaitable room means this layer is async-only here; skip rather than block."""
    awaitable_room = MagicMock()
    awaitable_room.__await__ = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=awaitable_room)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]

    cast(MagicMock, awaitable_room.add_container).assert_not_called()


def test_register_corpse_on_room_survives_missing_room(mock_persistence: MagicMock) -> None:
    """Registration is best-effort: a missing room must not fail corpse creation."""
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]


def test_unregister_corpse_from_room_removes_by_id(mock_persistence: MagicMock) -> None:
    """Decay cleanup drops the corpse from the in-memory room too."""
    room = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._unregister_corpse_from_room("c1", "room_001")  # pyright: ignore[reportPrivateUsage]

    cast(MagicMock, room.remove_container).assert_called_once_with("c1")


def test_live_room_returns_none_when_persistence_has_no_sync_lookup() -> None:
    """A persistence layer without get_room_by_id must not raise -- registration is best-effort.

    Guards the hasattr branch of _live_room (it resolves the lookup through the _SyncRoomLookup
    Protocol, so a missing attribute has to be checked before the cast).
    """

    class _NoRoomLookup:
        """Persistence double that deliberately exposes no room lookup."""

    service = CorpseLifecycleService(persistence=_NoRoomLookup())

    assert service._live_room("room_001") is None  # pyright: ignore[reportPrivateUsage]


def test_register_corpse_on_room_without_sync_lookup_is_a_noop() -> None:
    """The same gap seen from the caller: no lookup means no registration, and no exception."""

    class _NoRoomLookup:
        """Persistence double that deliberately exposes no room lookup."""

    service = CorpseLifecycleService(persistence=_NoRoomLookup())

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]
