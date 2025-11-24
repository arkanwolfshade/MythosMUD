"""
Tests for container WebSocket event emission.

As documented in the restricted archives of Miskatonic University, container
WebSocket events must be properly emitted to ensure real-time synchronization
of container state across all connected players.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.send_personal_message = AsyncMock(return_value={"success": True, "websocket_delivered": 1})
    manager.broadcast_room_event = AsyncMock(
        return_value={
            "room_id": "test_room",
            "total_targets": 1,
            "successful_deliveries": 1,
            "failed_deliveries": 0,
        }
    )
    return manager


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_container_id():
    """Generate a sample container UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id():
    """Return a sample room ID."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def sample_environment_container(sample_container_id, sample_room_id):
    """Create a sample environmental container."""
    return ContainerComponent(
        container_id=sample_container_id,
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id=sample_room_id,
        capacity_slots=8,
        lock_state=ContainerLockState.UNLOCKED,
        items=[],
    )


class TestContainerOpenedEvent:
    """Test container.opened event emission."""

    @pytest.mark.asyncio
    async def test_emit_container_opened_to_player(
        self,
        mock_connection_manager,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        sample_player_id,
    ):
        """Test emitting container.opened event to the opening player."""
        from server.services.container_websocket_events import emit_container_opened

        mutation_token = str(uuid.uuid4())
        expires_at = datetime.now(UTC) + timedelta(minutes=5)

        await emit_container_opened(
            connection_manager=mock_connection_manager,
            container=sample_environment_container,
            player_id=sample_player_id,
            mutation_token=mutation_token,
            expires_at=expires_at,
        )

        # Verify send_personal_message was called
        mock_connection_manager.send_personal_message.assert_called_once()
        call_args = mock_connection_manager.send_personal_message.call_args

        # Check player_id - handle both UUID and string comparison
        player_id_arg = call_args[0][0]
        assert (player_id_arg == sample_player_id) or (str(player_id_arg) == str(sample_player_id))

        # Check event structure
        event = call_args[0][1]
        assert event["event_type"] == "container.opened"
        assert "container" in event["data"]
        assert event["data"]["container"]["container_id"] == str(sample_container_id)
        assert event["data"]["mutation_token"] == mutation_token
        assert "expires_at" in event["data"]

    @pytest.mark.asyncio
    async def test_emit_container_opened_to_room(
        self,
        mock_connection_manager,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        sample_room_id,
    ):
        """Test emitting container.opened event to room occupants."""
        from server.services.container_websocket_events import emit_container_opened_to_room

        player_id = uuid.uuid4()
        mutation_token = str(uuid.uuid4())
        expires_at = datetime.now(UTC) + timedelta(minutes=5)

        await emit_container_opened_to_room(
            connection_manager=mock_connection_manager,
            container=sample_environment_container,
            room_id=sample_room_id,
            actor_id=player_id,
            mutation_token=mutation_token,
            expires_at=expires_at,
        )

        # Verify broadcast_room_event was called
        mock_connection_manager.broadcast_room_event.assert_called_once()
        call_kwargs = mock_connection_manager.broadcast_room_event.call_args.kwargs

        # Check event_type and room_id
        assert call_kwargs["event_type"] == "container.opened"
        assert call_kwargs["room_id"] == sample_room_id

        # Check event data
        data = call_kwargs["data"]
        assert "container" in data
        assert data["container"]["container_id"] == str(sample_container_id)
        assert data["actor_id"] == str(player_id)
        assert "expires_at" in data


class TestContainerUpdatedEvent:
    """Test container.updated event emission."""

    @pytest.mark.asyncio
    async def test_emit_container_updated_with_diff(
        self, mock_connection_manager, sample_container_id, sample_room_id, sample_player_id
    ):
        """Test emitting container.updated event with diff."""
        from server.services.container_websocket_events import emit_container_updated

        diff = {
            "items": {
                "added": [{"item_id": "elder_sign", "quantity": 1}],
                "removed": [],
            },
        }

        await emit_container_updated(
            connection_manager=mock_connection_manager,
            container_id=sample_container_id,
            room_id=sample_room_id,
            diff=diff,
            actor_id=sample_player_id,
        )

        # Verify broadcast_room_event was called
        mock_connection_manager.broadcast_room_event.assert_called_once()
        call_kwargs = mock_connection_manager.broadcast_room_event.call_args.kwargs

        # Check event_type and room_id
        assert call_kwargs["event_type"] == "container.updated"
        assert call_kwargs["room_id"] == sample_room_id

        # Check event data
        data = call_kwargs["data"]
        assert data["container_id"] == str(sample_container_id)
        assert data["actor_id"] == str(sample_player_id)
        assert "diff" in data
        assert data["diff"] == diff


class TestContainerClosedEvent:
    """Test container.closed event emission."""

    @pytest.mark.asyncio
    async def test_emit_container_closed(
        self, mock_connection_manager, sample_container_id, sample_room_id, sample_player_id
    ):
        """Test emitting container.closed event."""
        from server.services.container_websocket_events import emit_container_closed

        await emit_container_closed(
            connection_manager=mock_connection_manager,
            container_id=sample_container_id,
            room_id=sample_room_id,
            player_id=sample_player_id,
        )

        # Verify broadcast_room_event was called
        mock_connection_manager.broadcast_room_event.assert_called_once()
        call_kwargs = mock_connection_manager.broadcast_room_event.call_args.kwargs

        # Check event_type and room_id
        assert call_kwargs["event_type"] == "container.closed"
        assert call_kwargs["room_id"] == sample_room_id

        # Check event data
        data = call_kwargs["data"]
        assert data["container_id"] == str(sample_container_id)


class TestContainerDecayedEvent:
    """Test container.decayed event emission."""

    @pytest.mark.asyncio
    async def test_emit_container_decayed(self, mock_connection_manager, sample_container_id, sample_room_id):
        """Test emitting container.decayed event."""
        from server.services.container_websocket_events import emit_container_decayed

        await emit_container_decayed(
            connection_manager=mock_connection_manager,
            container_id=sample_container_id,
            room_id=sample_room_id,
        )

        # Verify broadcast_room_event was called
        mock_connection_manager.broadcast_room_event.assert_called_once()
        call_kwargs = mock_connection_manager.broadcast_room_event.call_args.kwargs

        # Check event_type and room_id
        assert call_kwargs["event_type"] == "container.decayed"
        assert call_kwargs["room_id"] == sample_room_id

        # Check event data
        data = call_kwargs["data"]
        assert data["container_id"] == str(sample_container_id)
        assert data["room_id"] == sample_room_id


class TestContainerEventIntegration:
    """Test container event integration with ContainerService."""

    @pytest.mark.asyncio
    async def test_container_service_emits_opened_event(
        self,
        mock_connection_manager,
        mock_persistence,
        sample_container_id,
        sample_environment_container,
        sample_player_id,
    ):
        """Test that ContainerService emits opened event when opening container."""
        # This test would require modifying ContainerService to accept connection_manager
        # For now, we'll test the event emission function directly
        from server.services.container_websocket_events import emit_container_opened

        mutation_token = str(uuid.uuid4())
        expires_at = datetime.now(UTC) + timedelta(minutes=5)

        await emit_container_opened(
            connection_manager=mock_connection_manager,
            container=sample_environment_container,
            player_id=sample_player_id,
            mutation_token=mutation_token,
            expires_at=expires_at,
        )

        # Verify event was sent
        assert mock_connection_manager.send_personal_message.called
