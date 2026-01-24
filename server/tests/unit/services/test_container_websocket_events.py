"""
Unit tests for container WebSocket events.

Tests the container WebSocket event emission functions.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent
from server.services.container_websocket_events import (
    emit_container_closed,
    emit_container_decayed,
    emit_container_opened,
    emit_container_opened_to_room,
    emit_container_updated,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    manager = MagicMock()
    manager.send_personal_message = AsyncMock(return_value={"sent": True})
    manager.broadcast_to_room = AsyncMock(return_value={"sent": 5})
    manager.broadcast_room_event = AsyncMock(return_value={"sent": 5, "failed": 0})
    return manager


@pytest.fixture
def mock_container():
    """Create mock container."""
    container = MagicMock(spec=ContainerComponent)
    container.container_id = "container_001"
    container.owner_id = None
    container.model_dump = MagicMock(return_value={"container_id": "container_001", "capacity": 10})
    return container


@pytest.mark.asyncio
async def test_emit_container_opened(mock_connection_manager, mock_container):
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
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_opened_with_owner(mock_connection_manager, mock_container):
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
async def test_emit_container_opened_to_room(mock_connection_manager, mock_container):
    """Test emit_container_opened_to_room broadcasts to room."""
    actor_id = uuid.uuid4()
    result = await emit_container_opened_to_room(
        mock_connection_manager,
        mock_container,
        "room_001",
        actor_id,
        "token_123",
        datetime.now(UTC),
    )
    assert isinstance(result, dict)
    # Function uses broadcast_room_event, not broadcast_to_room
    mock_connection_manager.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_closed(mock_connection_manager):
    """Test emit_container_closed emits close event."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    player_id = uuid.uuid4()
    result = await emit_container_closed(mock_connection_manager, container_id, room_id, player_id)
    assert isinstance(result, dict)
    # Function uses broadcast_room_event
    mock_connection_manager.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_opened_with_owner_id(mock_connection_manager, mock_container):
    """Test emit_container_opened handles container with owner_id."""
    mock_container.owner_id = uuid.uuid4()
    player_id = uuid.uuid4()
    result = await emit_container_opened(
        mock_connection_manager, mock_container, player_id, "token_123", datetime.now(UTC)
    )
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_emit_container_opened_to_room_with_owner(mock_connection_manager, mock_container):
    """Test emit_container_opened_to_room handles container with owner."""
    mock_container.owner_id = uuid.uuid4()
    actor_id = uuid.uuid4()
    result = await emit_container_opened_to_room(
        mock_connection_manager, mock_container, "room_001", actor_id, "token_123", datetime.now(UTC)
    )
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_updated(mock_connection_manager):
    """Test emit_container_updated broadcasts update event."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    actor_id = uuid.uuid4()
    diff = {"items_added": ["item_001"], "items_removed": []}
    result = await emit_container_updated(mock_connection_manager, container_id, room_id, diff, actor_id)
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_room_event.assert_awaited_once()
    call_args = mock_connection_manager.broadcast_room_event.call_args
    assert call_args[1]["event_type"] == "container.updated"
    assert call_args[1]["room_id"] == room_id
    assert call_args[1]["data"]["container_id"] == str(container_id)
    assert call_args[1]["data"]["diff"] == diff
    assert call_args[1]["data"]["actor_id"] == str(actor_id)


@pytest.mark.asyncio
async def test_emit_container_updated_empty_diff(mock_connection_manager):
    """Test emit_container_updated handles empty diff."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    actor_id = uuid.uuid4()
    diff: dict[str, object] = {}
    result = await emit_container_updated(mock_connection_manager, container_id, room_id, diff, actor_id)
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_emit_container_decayed(mock_connection_manager):
    """Test emit_container_decayed broadcasts decay event."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    result = await emit_container_decayed(mock_connection_manager, container_id, room_id)
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_room_event.assert_awaited_once()
    call_args = mock_connection_manager.broadcast_room_event.call_args
    assert call_args[1]["event_type"] == "container.decayed"
    assert call_args[1]["room_id"] == room_id
    assert call_args[1]["data"]["container_id"] == str(container_id)
    assert call_args[1]["data"]["room_id"] == room_id


@pytest.mark.asyncio
async def test_emit_container_opened_returns_delivery_status(mock_connection_manager, mock_container):
    """Test emit_container_opened returns delivery status."""
    player_id = uuid.uuid4()
    delivery_status = {"sent": True, "failed": False}
    mock_connection_manager.send_personal_message = AsyncMock(return_value=delivery_status)
    result = await emit_container_opened(
        mock_connection_manager, mock_container, player_id, "token_123", datetime.now(UTC)
    )
    assert result == delivery_status


@pytest.mark.asyncio
async def test_emit_container_opened_to_room_returns_stats(mock_connection_manager, mock_container):
    """Test emit_container_opened_to_room returns broadcast stats."""
    actor_id = uuid.uuid4()
    delivery_stats = {"sent": 3, "failed": 0}
    mock_connection_manager.broadcast_room_event = AsyncMock(return_value=delivery_stats)
    result = await emit_container_opened_to_room(
        mock_connection_manager, mock_container, "room_001", actor_id, "token_123", datetime.now(UTC)
    )
    assert result == delivery_stats


@pytest.mark.asyncio
async def test_emit_container_closed_returns_stats(mock_connection_manager):
    """Test emit_container_closed returns broadcast stats."""
    container_id = uuid.uuid4()
    room_id = "room_001"
    player_id = uuid.uuid4()
    delivery_stats = {"sent": 2, "failed": 1}
    mock_connection_manager.broadcast_room_event = AsyncMock(return_value=delivery_stats)
    result = await emit_container_closed(mock_connection_manager, container_id, room_id, player_id)
    assert result == delivery_stats
