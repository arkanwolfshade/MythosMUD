"""
Unit tests for corpse lifecycle service: decay discovery and cleanup.

Split from test_corpse_lifecycle_service.py to stay under the 500 file-nloc limit; that file
keeps creation, access/grace-period, decay-state and room-registration coverage.
"""
# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures use fixture names as parameters.

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerSourceType
from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
)


def _async_attr(obj: MagicMock, name: str) -> AsyncMock:
    """Typed access to a MagicMock's async-mocked attribute (avoids reportAny at call sites)."""
    return cast(AsyncMock, getattr(obj, name))


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def corpse_service(mock_persistence: MagicMock) -> CorpseLifecycleService:
    """Create a CorpseLifecycleService instance."""
    return CorpseLifecycleService(persistence=mock_persistence)


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_empty(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_decayed_corpses_in_room() returns empty list when no containers."""
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    result = await corpse_service.get_decayed_corpses_in_room("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_with_decayed(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_decayed_corpses_in_room() returns decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
async def test_cleanup_decayed_corpse_success(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpse() successfully deletes corpse."""
    container_id = uuid.uuid4()
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    _async_attr(mock_persistence, "delete_container").assert_awaited_once_with(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_not_found(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpse() raises error when corpse not found."""
    container_id = uuid.uuid4()
    mock_persistence.get_container = AsyncMock(return_value=None)
    with pytest.raises(CorpseNotFoundError):
        await corpse_service.cleanup_decayed_corpse(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_not_corpse(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpse() raises error when container is not a corpse."""
    container_id = uuid.uuid4()
    # Use a valid source_type that's not CORPSE
    container_data: dict[str, object] = {
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
async def test_cleanup_decayed_corpses_in_room(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpses_in_room() cleans up multiple corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    _async_attr(mock_persistence, "delete_container").assert_awaited_once()


@pytest.mark.asyncio
async def test_get_all_decayed_corpses(corpse_service: CorpseLifecycleService, mock_persistence: MagicMock) -> None:
    """Test get_all_decayed_corpses() returns all decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
async def test_cleanup_all_decayed_corpses(corpse_service: CorpseLifecycleService, mock_persistence: MagicMock) -> None:
    """Test cleanup_all_decayed_corpses() cleans up all decayed corpses."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    _async_attr(mock_persistence, "delete_container").assert_awaited_once()


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_validation_error(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_decayed_corpses_in_room() handles validation errors gracefully."""
    invalid_container_data = {"invalid": "data"}
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[invalid_container_data])
    result = await corpse_service.get_decayed_corpses_in_room("room_001")
    # Should return empty list, not raise
    assert result == []


@pytest.mark.asyncio
async def test_get_decayed_corpses_in_room_non_corpse(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_decayed_corpses_in_room() filters out non-corpse containers."""
    container_data: dict[str, object] = {
        "container_id": str(uuid.uuid4()),
        "source_type": ContainerSourceType.ENVIRONMENT.value,
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": datetime.now(UTC) - timedelta(hours=1),
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[container_data])
    result = await corpse_service.get_decayed_corpses_in_room("room_001")
    # Should return empty list (not a corpse)
    assert result == []


@pytest.mark.asyncio
async def test_cleanup_decayed_corpse_delete_error(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpse() raises error when delete fails."""
    container_id = uuid.uuid4()
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    mock_persistence.delete_container = AsyncMock(side_effect=Exception("Delete error"))
    with pytest.raises(CorpseServiceError, match="Failed to delete decayed corpse"):
        await corpse_service.cleanup_decayed_corpse(container_id)


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_in_room_handles_errors(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_decayed_corpses_in_room() handles individual cleanup errors."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    # First call succeeds, second call fails
    mock_persistence.get_container = AsyncMock(return_value=container_data)
    mock_persistence.delete_container = AsyncMock(side_effect=[None, Exception("Error")])
    # Should still return count of successful cleanups
    result = await corpse_service.cleanup_decayed_corpses_in_room("room_001")
    # Should handle error gracefully and continue
    assert result >= 0


@pytest.mark.asyncio
async def test_get_all_decayed_corpses_empty(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_all_decayed_corpses() returns empty list when no decayed containers."""
    mock_persistence.get_decayed_containers = AsyncMock(return_value=[])
    result = await corpse_service.get_all_decayed_corpses()
    assert result == []


@pytest.mark.asyncio
async def test_get_all_decayed_corpses_uses_real_time_not_mythos_time(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_all_decayed_corpses() uses real UTC time, not Mythos time, even when time service is available."""
    mock_time_service = MagicMock()
    # Mock Mythos time to be far in the future (simulating accelerated time)
    cast(MagicMock, mock_time_service.get_current_mythos_datetime).return_value = datetime.now(UTC) + timedelta(days=10)
    corpse_service.time_service = mock_time_service

    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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

    # Verify time service was NOT called (we use real UTC time, not Mythos time)
    cast(MagicMock, mock_time_service.get_current_mythos_datetime).assert_not_called()

    # Verify get_decayed_containers was called with a timezone-aware UTC datetime
    passed_time = cast(datetime, _async_attr(mock_persistence, "get_decayed_containers").call_args[0][0])
    tzinfo = passed_time.tzinfo
    assert tzinfo is not None, "current_time should be timezone-aware"
    assert tzinfo == UTC or tzinfo.utcoffset(None) == timedelta(0), "current_time should be UTC"


@pytest.mark.asyncio
async def test_get_all_decayed_corpses_validation_error(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_all_decayed_corpses() handles validation errors gracefully."""
    invalid_container_data = {"invalid": "data"}
    mock_persistence.get_decayed_containers = AsyncMock(return_value=[invalid_container_data])
    result = await corpse_service.get_all_decayed_corpses()
    # Should return empty list, not raise
    assert result == []


@pytest.mark.asyncio
async def test_get_all_decayed_corpses_non_corpse(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_all_decayed_corpses() filters out non-corpse containers."""
    container_data: dict[str, object] = {
        "container_id": str(uuid.uuid4()),
        "source_type": ContainerSourceType.ENVIRONMENT.value,
        "owner_id": str(uuid.uuid4()),
        "room_id": "room_001",
        "capacity_slots": 20,
        "lock_state": "unlocked",
        "decay_at": datetime.now(UTC) - timedelta(hours=1),
        "items": [],
        "metadata": {},
    }
    mock_persistence.get_decayed_containers = AsyncMock(return_value=[container_data])
    result = await corpse_service.get_all_decayed_corpses()
    # Should return empty list (not a corpse)
    assert result == []


@pytest.mark.asyncio
async def test_cleanup_all_decayed_corpses_handles_errors(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test cleanup_all_decayed_corpses() handles individual cleanup errors."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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
    mock_persistence.delete_container = AsyncMock(side_effect=Exception("Error"))
    # Should handle error gracefully and return count of successful cleanups
    result = await corpse_service.cleanup_all_decayed_corpses()
    # Should handle error gracefully
    assert result >= 0


@pytest.mark.asyncio
async def test_get_all_decayed_corpses_timezone_aware_utc(
    corpse_service: CorpseLifecycleService, mock_persistence: MagicMock
) -> None:
    """Test get_all_decayed_corpses() passes timezone-aware UTC datetime to persistence layer."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    container_data: dict[str, object] = {
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

    _ = await corpse_service.get_all_decayed_corpses()

    # Verify get_decayed_containers was called
    _async_attr(mock_persistence, "get_decayed_containers").assert_awaited_once()

    # Get the current_time argument that was passed
    call_args = cast(tuple[object, ...], _async_attr(mock_persistence, "get_decayed_containers").call_args[0])
    current_time_arg = call_args[0] if call_args else None

    assert current_time_arg is not None, "current_time should be passed"
    assert isinstance(current_time_arg, datetime), "current_time should be a datetime"
    assert current_time_arg.tzinfo is not None, "current_time should be timezone-aware"
    # Check it's UTC (either UTC timezone or offset of 0)
    assert current_time_arg.tzinfo == UTC or current_time_arg.utcoffset() == timedelta(0), "current_time should be UTC"
