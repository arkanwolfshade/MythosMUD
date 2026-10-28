"""
Unit tests for container WebSocket events.

Tests the container WebSocket event emission functions.
"""

import uuid
from datetime import UTC, datetime
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent
from server.services.container_websocket_events import (
    emit_container_closed,
    emit_container_created,
    emit_container_decayed,
    emit_container_opened,
    emit_container_opened_to_room,
    emit_container_updated,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def _async_attr(obj: MagicMock, name: str) -> AsyncMock:
    """Typed access to a MagicMock's async-mocked attribute (avoids reportAny at call sites)."""
    return cast(AsyncMock, getattr(obj, name))


@pytest.fixture
def mock_connection_manager() -> MagicMock:
    """Create mock connection manager."""
    manager = MagicMock()
    manager.sequence_counter = 0
    manager.send_personal_message = AsyncMock(return_value={"sent": True})
    manager.broadcast_to_room = AsyncMock(return_value={"sent": 5})
    manager.broadcast_room_event = AsyncMock(return_value={"sent": 5, "failed": 0})
    return manager


@pytest.fixture
def mock_container() -> ContainerComponent:
    """Create mock container, with a room_id so room-broadcast branches fire by default."""
    container = MagicMock(spec=ContainerComponent)
    container.container_id = "container_001"
    container.owner_id = None
    container.room_id = "room_001"
    container.model_dump = MagicMock(return_value={"container_id": "container_001", "capacity": 10})
    return cast(ContainerComponent, container)


@pytest.mark.asyncio
async def test_emit_container_opened(mock_connection_manager: MagicMock, mock_container: ContainerComponent) -> None:
    """Test emit_container_opened emits event to player."""
    player_id = uuid.uuid4()
    result = await emit_container_opened(
        mock_connection_manager,
        mock_container,
        player_id,
        "token_123",
        datetime.now(UTC),
    )
    assert isinstance(result, dict)
    _async_attr(mock_connection_manager, "send_personal_message").assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_opened_with_owner(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened handles container with owner."""
    mock_container.owner_id = uuid.uuid4()
    player_id = uuid.uuid4()
    result = await emit_container_opened(
        mock_connection_manager,
        mock_container,
        player_id,
        "token_123",
        datetime.now(UTC),
    )
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_emit_container_opened_to_room(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened_to_room broadcasts to room, without a mutation_token."""
    actor_id = uuid.uuid4()
    result = await emit_container_opened_to_room(
        mock_connection_manager,
        mock_container,
        "room_001",
        actor_id,
    )
    assert isinstance(result, dict)
    # Function uses broadcast_room_event, not broadcast_to_room
    broadcast = _async_attr(mock_connection_manager, "broadcast_room_event")
    broadcast.assert_awaited_once()
    call_args = broadcast.call_args
    assert call_args is not None
    data = cast(dict[str, object], call_args.kwargs["data"])
    assert "mutation_token" not in data
    assert "expires_at" not in data


@pytest.mark.asyncio
async def test_emit_container_closed(mock_connection_manager: MagicMock) -> None:
    """Test emit_container_closed emits close event."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    player_id = uuid.uuid4()
    result = await emit_container_closed(mock_connection_manager, container_id, room_id, player_id)
    assert isinstance(result, dict)
    # Function uses broadcast_room_event
    _async_attr(mock_connection_manager, "broadcast_room_event").assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_opened_with_owner_id(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened handles container with owner_id."""
    mock_container.owner_id = uuid.uuid4()
    player_id = uuid.uuid4()
    result = await emit_container_opened(
        mock_connection_manager, mock_container, player_id, "token_123", datetime.now(UTC)
    )
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_emit_container_opened_to_room_with_owner(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened_to_room handles container with owner."""
    mock_container.owner_id = uuid.uuid4()
    actor_id = uuid.uuid4()
    result = await emit_container_opened_to_room(mock_connection_manager, mock_container, "room_001", actor_id)
    assert isinstance(result, dict)
    _async_attr(mock_connection_manager, "broadcast_room_event").assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_updated(mock_connection_manager: MagicMock, mock_container: ContainerComponent) -> None:
    """Test emit_container_updated sends the full snapshot personally, and broadcasts to the room."""
    actor_id = uuid.uuid4()
    result = await emit_container_updated(mock_connection_manager, mock_container, actor_id)
    assert isinstance(result, dict)
    _async_attr(mock_connection_manager, "send_personal_message").assert_awaited_once()
    broadcast = _async_attr(mock_connection_manager, "broadcast_room_event")
    broadcast.assert_awaited_once()
    call_args = broadcast.call_args
    assert call_args is not None
    assert call_args.kwargs["event_type"] == "container.updated"
    assert call_args.kwargs["room_id"] == mock_container.room_id
    data = cast(dict[str, object], call_args.kwargs["data"])
    assert data["container_id"] == str(mock_container.container_id)
    assert data["container"] == mock_container.model_dump()
    assert data["actor_id"] == str(actor_id)


@pytest.mark.asyncio
async def test_emit_container_updated_no_room_id(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_updated stays personal-only for a container with no room_id (e.g. a worn container)."""
    mock_container.room_id = None
    actor_id = uuid.uuid4()
    result = await emit_container_updated(mock_connection_manager, mock_container, actor_id)
    assert isinstance(result, dict)
    _async_attr(mock_connection_manager, "send_personal_message").assert_awaited_once()
    _async_attr(mock_connection_manager, "broadcast_room_event").assert_not_awaited()


@pytest.mark.asyncio
async def test_emit_container_decayed(mock_connection_manager: MagicMock) -> None:
    """Test emit_container_decayed broadcasts decay event."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    result = await emit_container_decayed(mock_connection_manager, container_id, room_id)
    assert isinstance(result, dict)
    broadcast = _async_attr(mock_connection_manager, "broadcast_room_event")
    broadcast.assert_awaited_once()
    call_args = broadcast.call_args
    assert call_args is not None
    assert call_args.kwargs["event_type"] == "container.decayed"
    assert call_args.kwargs["room_id"] == room_id
    data = cast(dict[str, object], call_args.kwargs["data"])
    assert data["container_id"] == str(container_id)
    assert data["room_id"] == room_id


@pytest.mark.asyncio
async def test_emit_container_opened_returns_delivery_status(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened returns delivery status."""
    player_id = uuid.uuid4()
    delivery_status: dict[str, object] = {"sent": True, "failed": False}
    mock_connection_manager.send_personal_message = AsyncMock(return_value=delivery_status)
    result = await emit_container_opened(
        mock_connection_manager, mock_container, player_id, "token_123", datetime.now(UTC)
    )
    assert result == delivery_status


@pytest.mark.asyncio
async def test_emit_container_opened_to_room_returns_stats(
    mock_connection_manager: MagicMock, mock_container: ContainerComponent
) -> None:
    """Test emit_container_opened_to_room returns broadcast stats."""
    actor_id = uuid.uuid4()
    delivery_stats: dict[str, object] = {"sent": 3, "failed": 0}
    mock_connection_manager.broadcast_room_event = AsyncMock(return_value=delivery_stats)
    result = await emit_container_opened_to_room(mock_connection_manager, mock_container, "room_001", actor_id)
    assert result == delivery_stats


@pytest.mark.asyncio
async def test_emit_container_created(mock_connection_manager: MagicMock, mock_container: ContainerComponent) -> None:
    """Test emit_container_created broadcasts a fresh container (e.g. a corpse) to the room."""
    result = await emit_container_created(mock_connection_manager, mock_container, "room_001")
    assert isinstance(result, dict)
    broadcast = _async_attr(mock_connection_manager, "broadcast_room_event")
    broadcast.assert_awaited_once()
    call_args = broadcast.call_args
    assert call_args is not None
    assert call_args.kwargs["event_type"] == "container.created"
    assert call_args.kwargs["room_id"] == "room_001"
    data = cast(dict[str, object], call_args.kwargs["data"])
    assert data["container"] == mock_container.model_dump()


@pytest.mark.asyncio
async def test_emit_container_closed_returns_stats(mock_connection_manager: MagicMock) -> None:
    """Test emit_container_closed returns the personal delivery status."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    player_id = uuid.uuid4()
    delivery_status: dict[str, object] = {"sent": True}
    mock_connection_manager.send_personal_message = AsyncMock(return_value=delivery_status)
    result = await emit_container_closed(mock_connection_manager, container_id, room_id, player_id)
    assert result == delivery_status
    _async_attr(mock_connection_manager, "broadcast_room_event").assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_closed_no_room_id(mock_connection_manager: MagicMock) -> None:
    """Test emit_container_closed stays personal-only when room_id is None (e.g. a worn container)."""
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    result = await emit_container_closed(mock_connection_manager, container_id, None, player_id)
    assert isinstance(result, dict)
    _async_attr(mock_connection_manager, "send_personal_message").assert_awaited_once()
    _async_attr(mock_connection_manager, "broadcast_room_event").assert_not_awaited()


def _real_container_with_datetime() -> ContainerComponent:
    """A real (not mocked) component, so model_dump's serialization mode actually matters."""
    from server.models.container import ContainerLockState, ContainerSourceType

    return ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=datetime.now(UTC),
        items=[],
        metadata={},
    )


@pytest.mark.asyncio
async def test_emit_container_created_payload_is_json_serializable(mock_connection_manager: MagicMock) -> None:
    """Regression (#711): decay_at stayed a datetime and blew up json.dumps in the broadcaster.

    The failure surfaced as "Object of type datetime is not JSON serializable" from
    message_broadcaster, silently dropping every container.created broadcast.
    """
    import json

    _ = await emit_container_created(mock_connection_manager, _real_container_with_datetime(), "room_001")

    payload = cast(
        dict[str, dict[str, object]],
        _async_attr(mock_connection_manager, "broadcast_room_event").call_args.kwargs["data"],
    )
    _ = json.dumps(payload)  # must not raise
    assert isinstance(payload["container"]["decay_at"], str)
    assert isinstance(payload["container"]["container_id"], str)


@pytest.mark.asyncio
async def test_emit_container_updated_payload_is_json_serializable(mock_connection_manager: MagicMock) -> None:
    """Same serialization contract for the personal container.updated push."""
    import json

    container = _real_container_with_datetime()
    _ = await emit_container_updated(mock_connection_manager, container, uuid.uuid4())

    event = cast(
        dict[str, object],
        _async_attr(mock_connection_manager, "send_personal_message").call_args.args[1],
    )
    _ = json.dumps(event)  # must not raise
