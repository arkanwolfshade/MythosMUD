"""
Unit tests for emit_loot_all_event.

Split from test_container_events.py to keep Lizard file-nloc under limit.
"""
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api.container_events import emit_loot_all_event
from server.api.container_models import LootAllRequest
from server.models.container import ContainerComponent, ContainerSourceType
from server.realtime.connection_manager import ConnectionManager

# pylint: disable=protected-access  # Reason: unit tests may access protected members


def _assert_warning_once(logger_mock: object) -> None:
    """Assert patched logger.warning was called once (typed for basedpyright)."""
    warning: MagicMock = cast(MagicMock, cast(MagicMock, logger_mock).warning)
    warning.assert_called_once()


def _items_removed_from_log(logger_mock: object) -> object:
    """Extract the items_removed kwarg from the logger.info call emit_loot_all_event makes."""
    info: MagicMock = cast(MagicMock, cast(MagicMock, logger_mock).info)
    info.assert_called_once()
    call_args = info.call_args
    assert call_args is not None
    kwargs = cast(dict[str, object], call_args.kwargs)
    return kwargs["items_removed"]


@pytest.fixture
def mock_connection_manager() -> ConnectionManager:
    """Create a mock connection manager."""
    return cast(ConnectionManager, MagicMock())


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


class TestEmitLootAllEvent:
    """Test emit_loot_all_event function."""

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_success(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
        """Test emit_loot_all_event successfully emits event."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(mock_connection_manager, request_data, final_container, player_id, 0)
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_no_connection_manager(
        self, sample_container_component: ContainerComponent
    ) -> None:
        """Test emit_loot_all_event handles None connection_manager."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(None, request_data, final_container, player_id, 0)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_no_room_id(self, mock_connection_manager: ConnectionManager) -> None:
        """Test emit_loot_all_event still emits personally for a container without room_id (wearables)."""
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

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(mock_connection_manager, request_data, final_container, player_id, 0)
            mock_emit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_emission_error(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
        """Test emit_loot_all_event handles emission errors gracefully."""
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = LootAllRequest(container_id=container_id, mutation_token="token")
        final_container = sample_container_component

        with patch(
            "server.api.container_events.emit_container_updated",
            new_callable=AsyncMock,
            side_effect=RuntimeError("Emission error"),
        ):
            with patch("server.api.container_events.logger") as mock_logger:
                await emit_loot_all_event(mock_connection_manager, request_data, final_container, player_id, 0)
                _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_logs_the_count_it_is_given(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
        """The loot itself counts what moved (ContainerService.loot_all); the event only reports it."""
        request_data = LootAllRequest(container_id=uuid.uuid4(), mutation_token="token")

        with (
            patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit,
            patch("server.api.container_events.logger") as mock_logger,
        ):
            await emit_loot_all_event(
                mock_connection_manager, request_data, sample_container_component, uuid.uuid4(), 3
            )
            mock_emit.assert_awaited_once()
            assert _items_removed_from_log(mock_logger) == 3
