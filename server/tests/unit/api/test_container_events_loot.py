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
        original_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(
                mock_connection_manager, request_data, final_container, player_id, original_container
            )
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
        original_container = sample_container_component

        with patch("server.api.container_events.emit_container_updated", new_callable=AsyncMock) as mock_emit:
            await emit_loot_all_event(None, request_data, final_container, player_id, original_container)
            mock_emit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_no_room_id(self, mock_connection_manager: ConnectionManager) -> None:
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
    async def test_emit_loot_all_event_emission_error(
        self, mock_connection_manager: ConnectionManager, sample_container_component: ContainerComponent
    ) -> None:
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
                _assert_warning_once(mock_logger)

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_calculates_items_removed(
        self, mock_connection_manager: ConnectionManager
    ) -> None:
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
            items_diff = _diff_items_from_emit(mock_emit)
            assert items_diff["items_removed"] == 3  # 5 - 2 = 3

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_all_items_removed(self, mock_connection_manager: ConnectionManager) -> None:
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
            items_diff = _diff_items_from_emit(mock_emit)
            assert items_diff["items_removed"] == 3  # All 3 items removed

    @pytest.mark.asyncio
    async def test_emit_loot_all_event_zero_items_removed(self, mock_connection_manager: ConnectionManager) -> None:
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
            items_diff = _diff_items_from_emit(mock_emit)
            assert items_diff["items_removed"] == 0  # No items removed
