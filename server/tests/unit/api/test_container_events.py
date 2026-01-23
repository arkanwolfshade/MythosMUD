"""
Unit tests for container event emission helpers.

Tests WebSocket event emission for container operations.
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api.container_events import (
    _emit_close_container_event,
    emit_container_opened_events,
    emit_loot_all_event,
    emit_transfer_event,
)
from server.api.container_models import LootAllRequest, TransferContainerRequest
from server.models.container import ContainerComponent, ContainerSourceType

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def sample_container_data():
    """Create sample container data for testing."""
    return {
        "container_id": str(uuid.uuid4()),
        "room_id": str(uuid.uuid4()),
        "source_type": ContainerSourceType.ENVIRONMENT.value,
        "capacity_slots": 10,
        "items": [],
    }


@pytest.fixture
def sample_container_component(sample_container_data):
    """Create a ContainerComponent from sample data."""
    return ContainerComponent.model_validate(sample_container_data)


class TestEmitContainerOpenedEvents:
    """Test emit_container_opened_events function."""

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_success(self, mock_connection_manager, sample_container_data):
        """Test emit_container_opened_events successfully emits events."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result = {
            "container": sample_container_data,
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.emit_container_opened", new_callable=AsyncMock) as mock_emit_opened:
            with patch(
                "server.api.container_events.emit_container_opened_to_room", new_callable=AsyncMock
            ) as mock_emit_room:
                await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
                mock_emit_opened.assert_awaited_once()
                mock_emit_room.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_no_connection_manager(self, sample_container_data):
        """Test emit_container_opened_events handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result = {
            "container": sample_container_data,
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.emit_container_opened", new_callable=AsyncMock) as mock_emit:
            await emit_container_opened_events(None, result, player_id, container_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_no_room_id(self, mock_connection_manager):
        """Test emit_container_opened_events handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Create container data with EQUIPMENT source type which allows room_id=None
        container_data = {
            "container_id": str(container_id),
            "source_type": ContainerSourceType.EQUIPMENT.value,
            "entity_id": str(uuid.uuid4()),  # EQUIPMENT containers require entity_id
            "capacity_slots": 10,
            "items": [],
            "room_id": None,  # EQUIPMENT containers can have None room_id
        }
        result = {
            "container": container_data,
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.emit_container_opened", new_callable=AsyncMock) as mock_emit_opened:
            with patch(
                "server.api.container_events.emit_container_opened_to_room", new_callable=AsyncMock
            ) as mock_emit_room:
                await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
                mock_emit_opened.assert_awaited_once()
                mock_emit_room.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_validation_error(self, mock_connection_manager):
        """Test emit_container_opened_events handles validation errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Invalid container data that will fail validation
        result = {
            "container": {"invalid": "data"},
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.logger") as mock_logger:
            await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_emission_error(self, mock_connection_manager, sample_container_data):
        """Test emit_container_opened_events handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result = {
            "container": sample_container_data,
            "mutation_token": "test_token",
        }

        with patch(
            "server.api.container_events.emit_container_opened",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
                mock_logger.warning.assert_called_once()


class TestEmitTransferEvent:
    """Test emit_transfer_event function."""

    @pytest.mark.asyncio
    async def test_emit_transfer_event_success(self, mock_connection_manager, sample_container_component):
        """Test emit_transfer_event successfully emits event."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        # Use model_dump with mode='json' to ensure proper serialization
        result = {"container": sample_container_component.model_dump(mode="json")}

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_connection_manager(self, sample_container_component):
        """Test emit_transfer_event handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result = {"container": sample_container_component.model_dump(mode="json")}

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(None, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_container_in_result(self, mock_connection_manager):
        """Test emit_transfer_event handles missing container in result."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result: dict = {}  # No container

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_room_id(self, mock_connection_manager):
        """Test emit_transfer_event handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Create container with EQUIPMENT source type which allows room_id=None
        container_without_room = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "source_type": ContainerSourceType.EQUIPMENT.value,
                "entity_id": str(uuid.uuid4()),  # EQUIPMENT containers require entity_id
                "capacity_slots": 10,
                "items": [],
                "room_id": None,  # EQUIPMENT containers can have None room_id
            }
        )
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result = {"container": container_without_room.model_dump(mode="json")}

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_validation_error(self, mock_connection_manager):
        """Test emit_transfer_event handles validation errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result = {"container": {"invalid": "data"}}

        with patch("server.api.container_events.logger") as mock_logger:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_emission_error(self, mock_connection_manager, sample_container_component):
        """Test emit_transfer_event handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result = {"container": sample_container_component.model_dump(mode="json")}

        with patch(
            "server.api.container_events.emit_container_updated",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
                mock_logger.warning.assert_called_once()


class TestEmitCloseContainerEvent:
    """Test _emit_close_container_event function."""

    @pytest.mark.asyncio
    async def test_emit_close_container_event_success(
        self, mock_connection_manager, mock_persistence, sample_container_data
    ):
        """Test _emit_close_container_event successfully emits event."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=sample_container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await _emit_close_container_event(mock_connection_manager, container_id, player_id, mock_persistence)
            mock_emit.assert_awaited_once()
            mock_persistence.get_container.assert_awaited_once_with(container_id)

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_connection_manager(self, mock_persistence, sample_container_data):
        """Test _emit_close_container_event handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=sample_container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await _emit_close_container_event(None, container_id, player_id, mock_persistence)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_container_data(self, mock_connection_manager, mock_persistence):
        """Test _emit_close_container_event handles None container data."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=None)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await _emit_close_container_event(mock_connection_manager, container_id, player_id, mock_persistence)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_room_id(self, mock_connection_manager, mock_persistence):
        """Test _emit_close_container_event handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Create container data with EQUIPMENT source type which allows room_id=None
        container_data = {
            "container_id": str(container_id),
            "source_type": ContainerSourceType.EQUIPMENT.value,
            "entity_id": str(uuid.uuid4()),  # EQUIPMENT containers require entity_id
            "capacity_slots": 10,
            "items": [],
            "room_id": None,  # EQUIPMENT containers can have None room_id
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await _emit_close_container_event(mock_connection_manager, container_id, player_id, mock_persistence)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_persistence_error(self, mock_connection_manager, mock_persistence):
        """Test _emit_close_container_event handles persistence errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(side_effect=RuntimeError("Persistence error"))

        with patch("server.api.container_events.logger") as mock_logger:
            await _emit_close_container_event(mock_connection_manager, container_id, player_id, mock_persistence)
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_emission_error(
        self, mock_connection_manager, mock_persistence, sample_container_data
    ):
        """Test _emit_close_container_event handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=sample_container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await _emit_close_container_event(mock_connection_manager, container_id, player_id, mock_persistence)
                mock_logger.warning.assert_called_once()


class TestEmitLootAllEvent:
    """Test emit_loot_all_event function."""

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_success(self, mock_connection_manager, sample_container_component):
        """Test emit_loot_all_event successfully emits event."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component
        original_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_no_connection_manager(self, sample_container_component):
        """Test emit_loot_all_event handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component
        original_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(None, request_data, final_container, player_id, original_container)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_no_room_id(self, mock_connection_manager):
        """Test emit_loot_all_event handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        # Create containers with EQUIPMENT source type which allows room_id=None
        entity_id = uuid.uuid4()
        final_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "source_type": ContainerSourceType.EQUIPMENT.value,
                "entity_id": str(entity_id),  # EQUIPMENT containers require entity_id
                "capacity_slots": 10,
                "items": [],
                "room_id": None,  # EQUIPMENT containers can have None room_id
            }
        )
        original_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "source_type": ContainerSourceType.EQUIPMENT.value,
                "entity_id": str(entity_id),  # EQUIPMENT containers require entity_id
                "capacity_slots": 10,
                "items": [],
                "room_id": None,  # EQUIPMENT containers can have None room_id
            }
        )

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_emission_error(self, mock_connection_manager, sample_container_component):
        """Test emit_loot_all_event handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component
        original_container = sample_container_component

        with patch(
            "server.api.container_events.emit_container_updated",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_loot_all_event(
                    mock_connection_manager, request_data, final_container, player_id, original_container
                )
                mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_calculates_items_removed(self, mock_connection_manager):
        """Test emit_loot_all_event correctly calculates items_removed in diff."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        # Original container has 5 items
        original_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )

        # Final container has 2 items (3 were removed)
        final_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
            mock_emit.assert_awaited_once()
            # Verify diff contains correct items_removed count
            call_args = mock_emit.await_args
            assert call_args is not None
            diff = call_args[1]["diff"]
            assert diff["items"]["items_removed"] == 3  # 5 - 2 = 3

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_all_items_removed(self, mock_connection_manager):
        """Test emit_loot_all_event handles case when all items are removed."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        # Original container has 3 items
        original_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )

        # Final container is empty
        final_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [],
            }
        )

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
            mock_emit.assert_awaited_once()
            call_args = mock_emit.await_args
            assert call_args is not None
            diff = call_args[1]["diff"]
            assert diff["items"]["items_removed"] == 3  # All 3 items removed

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_zero_items_removed(self, mock_connection_manager):
        """Test emit_loot_all_event handles case when no items are removed."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")

        # Both containers have same number of items (no items removed)
        original_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )

        final_container = ContainerComponent.model_validate(
            {
                "container_id": str(container_id),
                "room_id": str(uuid.uuid4()),
                "source_type": ContainerSourceType.ENVIRONMENT.value,
                "capacity_slots": 10,
                "items": [
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                    {"item_id": str(uuid.uuid4()), "quantity": 1},
                ],
            }
        )

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
            mock_emit.assert_awaited_once()
            call_args = mock_emit.await_args
            assert call_args is not None
            diff = call_args[1]["diff"]
            assert diff["items"]["items_removed"] == 0  # No items removed


class TestEmitTransferEventDirections:
    """Test emit_transfer_event with different transfer directions."""

    @pytest.mark.asyncio
    async def test_emit_transfer_event_to_player_direction(self, mock_connection_manager, sample_container_component):
        """Test emit_transfer_event with 'to_player' direction."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_player",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        result = {"container": sample_container_component.model_dump(mode="json")}

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()
            # Verify direction is passed correctly in diff
            call_args = mock_emit.await_args
            assert call_args is not None
            diff = call_args[1]["diff"]
            assert diff["items"]["direction"] == "to_player"
            assert diff["items"]["stack"] == request_data.stack
            assert diff["items"]["quantity"] == request_data.quantity

    @pytest.mark.asyncio
    async def test_emit_transfer_event_to_container_direction(
        self, mock_connection_manager, sample_container_component
    ):
        """Test emit_transfer_event with 'to_container' direction."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=5,
        )
        result = {"container": sample_container_component.model_dump(mode="json")}

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()
            # Verify direction is passed correctly in diff
            call_args = mock_emit.await_args
            assert call_args is not None
            diff = call_args[1]["diff"]
            assert diff["items"]["direction"] == "to_container"
            assert diff["items"]["stack"] == request_data.stack
            assert diff["items"]["quantity"] == 5


class TestEmitContainerOpenedEventsEdgeCases:
    """Test additional edge cases for emit_container_opened_events."""

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_missing_mutation_token(
        self, mock_connection_manager, sample_container_data
    ):
        """Test emit_container_opened_events handles missing mutation_token gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result = {
            "container": sample_container_data,
            # Missing mutation_token
        }

        with patch("server.api.container_events.logger") as mock_logger:
            # Should handle KeyError gracefully
            await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_room_emission_error(
        self, mock_connection_manager, sample_container_data
    ):
        """Test emit_container_opened_events handles room emission errors separately."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result = {
            "container": sample_container_data,
            "mutation_token": "test_token",
        }

        with (
            patch("server.api.container_events.emit_container_opened", new_callable=AsyncMock),
            patch(
                "server.api.container_events.emit_container_opened_to_room",
                new_callable=AsyncMock,
                side_effect=RuntimeError("Room emission error"),
            ),
            patch("server.api.container_events.logger") as mock_logger,
        ):
            await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
            # Should log warning for room emission error
            mock_logger.warning.assert_called_once()
