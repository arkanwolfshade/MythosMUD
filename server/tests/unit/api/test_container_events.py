"""
Unit tests for container event emission helpers.

Tests WebSocket event emission for container open/close/transfer.
Loot-all coverage lives in test_container_events_loot.py (Lizard file-nloc).
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api.container_events import (
    emit_close_container_event,
    emit_container_opened_events,
    emit_transfer_event,
)
from server.api.container_models import TransferContainerRequest
from server.async_persistence import AsyncPersistenceLayer
from server.models.container import ContainerComponent, ContainerSourceType
from server.realtime.connection_manager import ConnectionManager

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


def _assert_warning_once(logger_mock: object) -> None:
    """Assert patched logger.warning was called once (typed for basedpyright)."""
    warning: MagicMock = cast(MagicMock, cast(MagicMock, logger_mock).warning)
    warning.assert_called_once()


def _diff_items_from_emit(mock_emit: AsyncMock) -> dict[str, object]:
    """Extract diff['items'] from emit_container_updated await kwargs."""
    call_args = mock_emit.await_args
    assert call_args is not None
    diff = cast(dict[str, object], call_args.kwargs["diff"])
    return cast(dict[str, object], diff["items"])


@pytest.fixture
def mock_connection_manager() -> ConnectionManager:
    """Create a mock connection manager."""
    return cast(ConnectionManager, MagicMock())


@pytest.fixture
def mock_persistence() -> AsyncMock:
    """Create a mock persistence layer."""
    return AsyncMock()


@pytest.fixture
def sample_container_data() -> dict[str, object]:
    """Create sample container data for testing."""
    items: list[object] = []
    return {
        "container_id": str(uuid.uuid4()),
        "room_id": str(uuid.uuid4()),
        "source_type": ContainerSourceType.ENVIRONMENT.value,
        "capacity_slots": 10,
        "items": items,
    }


@pytest.fixture
def sample_container_component(sample_container_data: dict[str, object]) -> ContainerComponent:
    """Create a ContainerComponent from sample data."""
    return ContainerComponent.model_validate(sample_container_data)


class TestEmitContainerOpenedEvents:
    """Test emit_container_opened_events function."""

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_success(
        self, mock_connection_manager: ConnectionManager, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_container_opened_events successfully emits events."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result: dict[str, object] = {
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
    async def test_emit_container_opened_events_no_connection_manager(
        self, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_container_opened_events handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result: dict[str, object] = {
            "container": sample_container_data,
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.emit_container_opened", new_callable=AsyncMock) as mock_emit:
            await emit_container_opened_events(None, result, player_id, container_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_no_room_id(self, mock_connection_manager: ConnectionManager) -> None:
        """Test emit_container_opened_events handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Create container data with EQUIPMENT source type which allows room_id=None
        items: list[object] = []
        container_data: dict[str, object] = {
            "container_id": str(container_id),
            "source_type": ContainerSourceType.EQUIPMENT.value,
            "entity_id": str(uuid.uuid4()),  # EQUIPMENT containers require entity_id
            "capacity_slots": 10,
            "items": items,
            "room_id": None,  # EQUIPMENT containers can have None room_id
        }
        result: dict[str, object] = {
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
    async def test_emit_container_opened_events_validation_error(
        self, mock_connection_manager: ConnectionManager
    ) -> None:
        """Test emit_container_opened_events handles validation errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Invalid container data that will fail validation
        result: dict[str, object] = {
            "container": {"invalid": "data"},
            "mutation_token": "test_token",
        }

        with patch("server.api.container_events.logger") as mock_logger:
            await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
            _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_emission_error(
        self, mock_connection_manager: ConnectionManager, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_container_opened_events handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result: dict[str, object] = {
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
                _assert_warning_once(mock_logger)


class TestEmitTransferEvent:
    """Test emit_transfer_event function."""

    @pytest.mark.asyncio
    async def test_emit_transfer_event_success(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, sample_container_component.model_dump(mode="json")),
        }

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_connection_manager(
        self, sample_container_component: ContainerComponent
    ) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, sample_container_component.model_dump(mode="json")),
        }

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(None, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_container_in_result(self, mock_connection_manager: ConnectionManager) -> None:
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
        result: dict[str, object] = {}  # No container

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_no_room_id(self, mock_connection_manager: ConnectionManager) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, container_without_room.model_dump(mode="json")),
        }

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_transfer_event_validation_error(self, mock_connection_manager: ConnectionManager) -> None:
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
        result: dict[str, object] = {"container": {"invalid": "data"}}

        with patch("server.api.container_events.logger") as mock_logger:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_transfer_event_emission_error(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, sample_container_component.model_dump(mode="json")),
        }

        with patch(
            "server.api.container_events.emit_container_updated",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
                _assert_warning_once(mock_logger)


class TestEmitCloseContainerEvent:
    """Test emit_close_container_event function."""

    @pytest.mark.asyncio
    async def test_emit_close_container_event_success(
        self,
        mock_connection_manager: ConnectionManager,
        mock_persistence: AsyncMock,
        sample_container_data: dict[str, object],
    ) -> None:
        """Test emit_close_container_event successfully emits event."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        get_container: AsyncMock = AsyncMock(return_value=sample_container_data)
        mock_persistence.get_container = get_container

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await emit_close_container_event(
                mock_connection_manager,
                container_id,
                player_id,
                cast(AsyncPersistenceLayer, mock_persistence),
            )
            mock_emit.assert_awaited_once()
            get_container.assert_awaited_once_with(container_id)

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_connection_manager(
        self, mock_persistence: AsyncMock, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_close_container_event handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=sample_container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await emit_close_container_event(
                None, container_id, player_id, cast(AsyncPersistenceLayer, mock_persistence)
            )
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_container_data(
        self, mock_connection_manager: ConnectionManager, mock_persistence: AsyncMock
    ) -> None:
        """Test emit_close_container_event handles None container data."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=None)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await emit_close_container_event(
                mock_connection_manager,
                container_id,
                player_id,
                cast(AsyncPersistenceLayer, mock_persistence),
            )
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_no_room_id(
        self, mock_connection_manager: ConnectionManager, mock_persistence: AsyncMock
    ) -> None:
        """Test emit_close_container_event handles container without room_id."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        # Create container data with EQUIPMENT source type which allows room_id=None
        items: list[object] = []
        container_data: dict[str, object] = {
            "container_id": str(container_id),
            "source_type": ContainerSourceType.EQUIPMENT.value,
            "entity_id": str(uuid.uuid4()),  # EQUIPMENT containers require entity_id
            "capacity_slots": 10,
            "items": items,
            "room_id": None,  # EQUIPMENT containers can have None room_id
        }
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed", new_callable=AsyncMock
        ) as mock_emit:
            await emit_close_container_event(
                mock_connection_manager,
                container_id,
                player_id,
                cast(AsyncPersistenceLayer, mock_persistence),
            )
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_close_container_event_persistence_error(
        self, mock_connection_manager: ConnectionManager, mock_persistence: AsyncMock
    ) -> None:
        """Test emit_close_container_event handles persistence errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(side_effect=RuntimeError("Persistence error"))

        with patch("server.api.container_events.logger") as mock_logger:
            await emit_close_container_event(
                mock_connection_manager,
                container_id,
                player_id,
                cast(AsyncPersistenceLayer, mock_persistence),
            )
            _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_close_container_event_emission_error(
        self,
        mock_connection_manager: ConnectionManager,
        mock_persistence: AsyncMock,
        sample_container_data: dict[str, object],
    ) -> None:
        """Test emit_close_container_event handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        mock_persistence.get_container = AsyncMock(return_value=sample_container_data)

        with patch(
            "server.services.container_websocket_events.emit_container_closed",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_close_container_event(
                    mock_connection_manager,
                    container_id,
                    player_id,
                    cast(AsyncPersistenceLayer, mock_persistence),
                )
                _assert_warning_once(mock_logger)


class TestEmitTransferEventDirections:
    """Test emit_transfer_event with different transfer directions."""

    @pytest.mark.asyncio
    async def test_emit_transfer_event_to_player_direction(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, sample_container_component.model_dump(mode="json")),
        }

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()
            # Verify direction is passed correctly in diff
            items_diff = _diff_items_from_emit(mock_emit)
            assert items_diff["direction"] == "to_player"
            assert items_diff["stack"] == request_data.stack
            assert items_diff["quantity"] == request_data.quantity

    @pytest.mark.asyncio
    async def test_emit_transfer_event_to_container_direction(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
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
        result: dict[str, object] = {
            "container": cast(object, sample_container_component.model_dump(mode="json")),
        }

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_transfer_event(mock_connection_manager, request_data, result, player_id)
            mock_emit.assert_awaited_once()
            # Verify direction is passed correctly in diff
            items_diff = _diff_items_from_emit(mock_emit)
            assert items_diff["direction"] == "to_container"
            assert items_diff["stack"] == request_data.stack
            assert items_diff["quantity"] == 5


class TestEmitContainerOpenedEventsEdgeCases:
    """Test additional edge cases for emit_container_opened_events."""

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_missing_mutation_token(
        self, mock_connection_manager: ConnectionManager, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_container_opened_events handles missing mutation_token gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result: dict[str, object] = {
            "container": sample_container_data,
            # Missing mutation_token
        }

        with patch("server.api.container_events.logger") as mock_logger:
            # Should handle KeyError gracefully
            await emit_container_opened_events(mock_connection_manager, result, player_id, container_id)
            _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_container_opened_events_room_emission_error(
        self, mock_connection_manager: ConnectionManager, sample_container_data: dict[str, object]
    ) -> None:
        """Test emit_container_opened_events handles room emission errors separately."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        result: dict[str, object] = {
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
            _assert_warning_once(mock_logger)
