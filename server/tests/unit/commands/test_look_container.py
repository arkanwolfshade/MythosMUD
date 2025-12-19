"""
Tests for look container functionality.

This module tests container lookup functions including finding containers in rooms,
equipped items, formatting container displays, and handling container look requests.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.look_container import (
    _find_container_in_room,
    _find_container_in_room_or_equipped,
    _find_container_via_inner_container,
    _find_container_wearable,
    _format_container_contents,
    _format_container_display,
    _get_container_data_from_component,
    _get_container_description,
    _handle_container_look,
    _try_lookup_container_implicit,
)


class TestFindContainerInRoom:
    """Test _find_container_in_room function."""

    def test_find_container_in_room_by_name(self) -> None:
        """Test finding container by name from metadata."""
        containers = [{"container_id": "cont-1", "metadata": {"name": "backpack"}}]
        result = _find_container_in_room(containers, "backpack")
        assert result == containers[0]

    def test_find_container_in_room_by_container_id(self) -> None:
        """Test finding container by container_id."""
        containers = [{"container_id": "cont-123", "metadata": {}}]
        result = _find_container_in_room(containers, "cont-123")
        assert result == containers[0]

    def test_find_container_in_room_case_insensitive(self) -> None:
        """Test finding container case-insensitively."""
        containers = [{"container_id": "cont-1", "metadata": {"name": "Backpack"}}]
        result = _find_container_in_room(containers, "BACKPACK")
        assert result == containers[0]

    def test_find_container_in_room_partial_match(self) -> None:
        """Test finding container with partial name match."""
        containers = [{"container_id": "cont-1", "metadata": {"name": "leather backpack"}}]
        result = _find_container_in_room(containers, "backpack")
        assert result == containers[0]

    def test_find_container_in_room_not_found(self) -> None:
        """Test when container is not found."""
        containers = [{"container_id": "cont-1", "metadata": {"name": "backpack"}}]
        result = _find_container_in_room(containers, "chest")
        assert result is None

    def test_find_container_in_room_empty_list(self) -> None:
        """Test with empty containers list."""
        result = _find_container_in_room([], "backpack")
        assert result is None

    def test_find_container_in_room_with_instance_number(self) -> None:
        """Test finding container with instance number."""
        containers = [
            {"container_id": "cont-1", "metadata": {"name": "backpack"}},
            {"container_id": "cont-2", "metadata": {"name": "backpack"}},
        ]
        result = _find_container_in_room(containers, "backpack", instance_number=2)
        assert result == containers[1]

    def test_find_container_in_room_instance_number_out_of_range(self) -> None:
        """Test with instance number out of range."""
        containers = [{"container_id": "cont-1", "metadata": {"name": "backpack"}}]
        result = _find_container_in_room(containers, "backpack", instance_number=5)
        assert result is None

    def test_find_container_in_room_multiple_matches(self) -> None:
        """Test when multiple containers match (returns None for ambiguity)."""
        containers = [
            {"container_id": "cont-1", "metadata": {"name": "backpack"}},
            {"container_id": "cont-2", "metadata": {"name": "backpack"}},
        ]
        result = _find_container_in_room(containers, "backpack")
        assert result is None  # Ambiguous

    def test_find_container_in_room_no_metadata(self) -> None:
        """Test when container has no metadata."""
        containers = [{"container_id": "cont-123"}]
        result = _find_container_in_room(containers, "cont-123")
        assert result == containers[0]


class TestFindContainerWearable:
    """Test _find_container_wearable function."""

    def test_find_container_wearable_by_name(self) -> None:
        """Test finding wearable container by name."""
        equipped = {"backpack": {"item_name": "backpack", "inner_container": "cont-1"}}
        result = _find_container_wearable(equipped, "backpack")
        assert result == ("backpack", equipped["backpack"])

    def test_find_container_wearable_by_prototype_id(self) -> None:
        """Test finding wearable container by prototype_id."""
        equipped = {"backpack": {"prototype_id": "proto-123", "inner_container": "cont-1"}}
        result = _find_container_wearable(equipped, "proto-123")
        assert result == ("backpack", equipped["backpack"])

    def test_find_container_wearable_with_inner_container(self) -> None:
        """Test finding container with inner_container attribute."""
        equipped = {"backpack": {"item_name": "bag", "inner_container": "cont-1"}}
        result = _find_container_wearable(equipped, "bag")
        assert result == ("backpack", equipped["backpack"])

    def test_find_container_wearable_not_found(self) -> None:
        """Test when wearable container is not found."""
        equipped = {"hand": {"item_name": "sword", "item_id": "item-1"}}
        result = _find_container_wearable(equipped, "backpack")
        assert result is None

    def test_find_container_wearable_with_instance_number(self) -> None:
        """Test finding wearable container with instance number."""
        equipped = {
            "backpack": {"item_name": "backpack", "inner_container": "cont-1"},
            "belt": {"item_name": "backpack", "inner_container": "cont-2"},
        }
        result = _find_container_wearable(equipped, "backpack", instance_number=2)
        assert result == ("belt", equipped["belt"])

    def test_find_container_wearable_multiple_matches(self) -> None:
        """Test when multiple wearable containers match (returns None for ambiguity)."""
        equipped = {
            "backpack": {"item_name": "backpack", "inner_container": "cont-1"},
            "belt": {"item_name": "backpack", "inner_container": "cont-2"},
        }
        result = _find_container_wearable(equipped, "backpack")
        assert result is None  # Ambiguous


class TestFindContainerViaInnerContainer:
    """Test _find_container_via_inner_container function."""

    @pytest.mark.asyncio
    async def test_find_container_via_inner_container_success(self) -> None:
        """Test finding container via inner_container_id."""
        item = {"inner_container": str(uuid4())}
        mock_persistence = AsyncMock()
        mock_container = {"container_id": item["inner_container"], "items": []}
        mock_persistence.get_container.return_value = mock_container

        result = await _find_container_via_inner_container(item, mock_persistence)

        assert result == mock_container
        mock_persistence.get_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_find_container_via_inner_container_no_inner_container(self) -> None:
        """Test when item has no inner_container."""
        item = {"item_name": "sword"}
        mock_persistence = AsyncMock()

        result = await _find_container_via_inner_container(item, mock_persistence)

        assert result is None
        mock_persistence.get_container.assert_not_called()

    @pytest.mark.asyncio
    async def test_find_container_via_inner_container_invalid_uuid(self) -> None:
        """Test when inner_container is invalid UUID."""
        item = {"inner_container": "invalid-uuid"}
        mock_persistence = AsyncMock()

        result = await _find_container_via_inner_container(item, mock_persistence)

        assert result is None

    @pytest.mark.asyncio
    async def test_find_container_via_inner_container_no_get_container_method(self) -> None:
        """Test when persistence doesn't have get_container method."""
        item = {"inner_container": str(uuid4())}
        mock_persistence = MagicMock()
        delattr(mock_persistence, "get_container")

        result = await _find_container_via_inner_container(item, mock_persistence)

        assert result is None


class TestGetContainerDataFromComponent:
    """Test _get_container_data_from_component function."""

    @pytest.mark.asyncio
    async def test_get_container_data_from_component_success(self) -> None:
        """Test getting container data from component."""
        mock_component = MagicMock()
        mock_component.container_id = uuid4()
        mock_persistence = AsyncMock()
        mock_container = {"container_id": mock_component.container_id, "items": []}
        mock_persistence.get_container.return_value = mock_container

        result = await _get_container_data_from_component(mock_component, mock_persistence)

        assert result == mock_container
        mock_persistence.get_container.assert_called_once_with(mock_component.container_id)

    @pytest.mark.asyncio
    async def test_get_container_data_from_component_no_container_id(self) -> None:
        """Test when component has no container_id."""
        mock_component = MagicMock()
        mock_component.container_id = None
        mock_persistence = AsyncMock()

        result = await _get_container_data_from_component(mock_component, mock_persistence)

        assert result is None
        mock_persistence.get_container.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_container_data_from_component_no_get_container_method(self) -> None:
        """Test when persistence doesn't have get_container method."""
        mock_component = MagicMock()
        mock_component.container_id = uuid4()
        mock_persistence = MagicMock()
        delattr(mock_persistence, "get_container")

        result = await _get_container_data_from_component(mock_component, mock_persistence)

        assert result is None


class TestFormatContainerContents:
    """Test _format_container_contents function."""

    def test_format_container_contents_with_items(self) -> None:
        """Test formatting container with items."""
        items = [
            {"item_name": "sword", "quantity": 1},
            {"item_name": "potion", "quantity": 3},
        ]
        result = _format_container_contents(items)

        assert len(result) == 2
        assert "1. sword" in result[0]
        assert "2. potion x3" in result[1]

    def test_format_container_contents_empty(self) -> None:
        """Test formatting empty container."""
        result = _format_container_contents([])

        assert result == ["  (empty)"]

    def test_format_container_contents_uses_name_key(self) -> None:
        """Test formatting when items use 'name' key instead of 'item_name'."""
        items = [{"name": "sword", "quantity": 1}]
        result = _format_container_contents(items)

        assert "sword" in result[0]

    def test_format_container_contents_no_quantity(self) -> None:
        """Test formatting when quantity is missing (defaults to 1)."""
        items = [{"item_name": "sword"}]
        result = _format_container_contents(items)

        assert "1. sword" in result[0]
        assert "x" not in result[0]


class TestFormatContainerDisplay:
    """Test _format_container_display function."""

    def test_format_container_display_basic(self) -> None:
        """Test basic container display formatting."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Backpack"},
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        command_data: dict[str, Any] = {}

        result = _format_container_display(container_found, None, command_data)

        assert "Backpack" in result
        assert "Capacity: 0/10 slots" in result

    def test_format_container_display_with_description(self) -> None:
        """Test container display with description."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Backpack"},
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        command_data: dict[str, Any] = {}
        description = "A sturdy leather backpack."

        result = _format_container_display(container_found, description, command_data)

        assert "Backpack" in result
        assert description in result

    def test_format_container_display_locked(self) -> None:
        """Test container display when locked."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Chest"},
            "items": [],
            "capacity_slots": 5,
            "lock_state": "locked",
        }
        command_data: dict[str, Any] = {}

        result = _format_container_display(container_found, None, command_data)

        assert "Locked" in result

    def test_format_container_display_sealed(self) -> None:
        """Test container display when sealed."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Chest"},
            "items": [],
            "capacity_slots": 5,
            "lock_state": "sealed",
        }
        command_data: dict[str, Any] = {}

        result = _format_container_display(container_found, None, command_data)

        assert "Sealed" in result

    def test_format_container_display_with_contents(self) -> None:
        """Test container display with contents when look_in is True."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Backpack"},
            "items": [{"item_name": "sword", "quantity": 1}],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        command_data = {"look_in": True}

        result = _format_container_display(container_found, None, command_data)

        assert "Contents:" in result
        assert "sword" in result

    def test_format_container_display_with_target_type_container(self) -> None:
        """Test container display when target_type is container."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {"name": "Backpack"},
            "items": [{"item_name": "sword", "quantity": 1}],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        command_data = {"target_type": "container"}

        result = _format_container_display(container_found, None, command_data)

        assert "Contents:" in result

    def test_format_container_display_no_name_uses_container_id(self) -> None:
        """Test container display when name is missing (uses container_id)."""
        container_found = {
            "container_id": uuid4(),
            "metadata": {},
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        command_data: dict[str, Any] = {}

        result = _format_container_display(container_found, None, command_data)

        assert "Container" in result


class TestGetContainerDescription:
    """Test _get_container_description function."""

    def test_get_container_description_from_container_item(self) -> None:
        """Test getting description from container_item."""
        container_found = {"container_id": uuid4()}
        container_item = {"prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.long_description = "A sturdy backpack."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _get_container_description(container_found, container_item, mock_registry)

        assert result == "A sturdy backpack."

    def test_get_container_description_from_container_metadata(self) -> None:
        """Test getting description from container metadata."""
        container_found = {"container_id": uuid4(), "metadata": {"prototype_id": "proto-123"}}
        container_item = None
        mock_prototype = MagicMock()
        mock_prototype.long_description = "A sturdy backpack."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _get_container_description(container_found, container_item, mock_registry)

        assert result == "A sturdy backpack."

    def test_get_container_description_no_registry(self) -> None:
        """Test when prototype registry is None."""
        container_found = {"container_id": uuid4()}
        container_item = {"prototype_id": "proto-123"}

        result = _get_container_description(container_found, container_item, None)

        assert result is None

    def test_get_container_description_no_prototype_id(self) -> None:
        """Test when prototype_id is missing."""
        container_found = {"container_id": uuid4()}
        container_item: dict[str, Any] = {}
        mock_registry = MagicMock()

        result = _get_container_description(container_found, container_item, mock_registry)

        assert result is None

    def test_get_container_description_prototype_not_found(self) -> None:
        """Test when prototype is not found."""
        container_found = {"container_id": uuid4()}
        container_item = {"prototype_id": "proto-123"}
        mock_registry = MagicMock()
        mock_registry.get.return_value = None

        with patch("server.commands.look_container.logger"):
            result = _get_container_description(container_found, container_item, mock_registry)

            assert result is None

    def test_get_container_description_no_long_description(self) -> None:
        """Test when prototype has no long_description attribute."""
        container_found = {"container_id": uuid4()}
        container_item = {"prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        delattr(mock_prototype, "long_description")
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        with patch("server.commands.look_container.logger"):
            result = _get_container_description(container_found, container_item, mock_registry)

            assert result is None


class TestFindContainerInRoomOrEquipped:
    """Test _find_container_in_room_or_equipped function."""

    @pytest.mark.asyncio
    async def test_find_container_in_room_or_equipped_in_room(self) -> None:
        """Test finding container in room."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = [{"container_id": "cont-1", "metadata": {"name": "backpack"}}]
        mock_player = MagicMock()
        mock_persistence = AsyncMock()
        mock_request = MagicMock()

        result = await _find_container_in_room_or_equipped(
            "backpack", None, mock_room, mock_player, mock_persistence, mock_request, "testuser"
        )

        container_found, container_item = result
        assert container_found is not None
        assert container_item is None

    @pytest.mark.asyncio
    async def test_find_container_in_room_or_equipped_in_equipped_inner_container(self) -> None:
        """Test finding container via inner_container in equipped item."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = []
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {
            "backpack": {"item_name": "backpack", "inner_container": str(uuid4())}
        }
        mock_persistence = AsyncMock()
        mock_container = {"container_id": mock_player.get_equipped_items()["backpack"]["inner_container"]}
        mock_persistence.get_container.return_value = mock_container
        mock_request = MagicMock()

        result = await _find_container_in_room_or_equipped(
            "backpack", None, mock_room, mock_player, mock_persistence, mock_request, "testuser"
        )

        container_found, container_item = result
        assert container_found == mock_container
        assert container_item == mock_player.get_equipped_items()["backpack"]

    @pytest.mark.asyncio
    async def test_find_container_in_room_or_equipped_not_found(self) -> None:
        """Test when container is not found."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = []
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {}
        mock_persistence = AsyncMock()
        mock_request = MagicMock()

        result = await _find_container_in_room_or_equipped(
            "backpack", None, mock_room, mock_player, mock_persistence, mock_request, "testuser"
        )

        container_found, container_item = result
        assert container_found is None
        assert container_item is None


class TestHandleContainerLook:
    """Test _handle_container_look function."""

    @pytest.mark.asyncio
    async def test_handle_container_look_success(self) -> None:
        """Test successful container look."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = [
            {
                "container_id": uuid4(),
                "metadata": {"name": "Backpack"},
                "items": [],
                "capacity_slots": 10,
                "lock_state": "unlocked",
            }
        ]
        mock_player = MagicMock()
        mock_persistence = AsyncMock()
        mock_registry = MagicMock()
        mock_request = MagicMock()

        with patch(
            "server.commands.look_container._find_container_in_room_or_equipped",
            return_value=(
                mock_room.get_containers()[0],
                None,
            ),
        ):
            with patch("server.commands.look_container.logger"):
                result = await _handle_container_look(
                    "backpack",
                    "backpack",
                    None,
                    mock_room,
                    mock_player,
                    mock_persistence,
                    mock_registry,
                    {},
                    mock_request,
                    "testuser",
                )

                assert result is not None
                assert "Backpack" in result["result"]
                assert "Capacity:" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_container_look_not_found(self) -> None:
        """Test when container is not found."""
        mock_room = MagicMock()
        mock_player = MagicMock()
        mock_persistence = AsyncMock()
        mock_registry = MagicMock()
        mock_request = MagicMock()

        with patch("server.commands.look_container._find_container_in_room_or_equipped", return_value=(None, None)):
            with patch("server.commands.look_container.logger") as mock_logger:
                result = await _handle_container_look(
                    "backpack",
                    "backpack",
                    None,
                    mock_room,
                    mock_player,
                    mock_persistence,
                    mock_registry,
                    {},
                    mock_request,
                    "testuser",
                )

                assert result is not None
                assert "don't see any 'backpack'" in result["result"]
                mock_logger.debug.assert_called()


class TestTryLookupContainerImplicit:
    """Test _try_lookup_container_implicit function."""

    @pytest.mark.asyncio
    async def test_try_lookup_container_implicit_in_room(self) -> None:
        """Test implicit lookup in room."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = [
            {
                "container_id": uuid4(),
                "metadata": {"name": "Backpack"},
                "items": [],
                "capacity_slots": 10,
                "lock_state": "unlocked",
            }
        ]
        mock_player = MagicMock()
        mock_persistence = AsyncMock()

        with patch("server.commands.look_container.logger"):
            result = await _try_lookup_container_implicit(
                "backpack", "backpack", None, mock_room, mock_player, mock_persistence, "testuser"
            )

            assert result is not None
            assert "Backpack" in result["result"]
            assert "Capacity:" in result["result"]

    @pytest.mark.asyncio
    async def test_try_lookup_container_implicit_in_equipped(self) -> None:
        """Test implicit lookup in equipped items."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = []
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {
            "backpack": {"item_name": "backpack", "inner_container": str(uuid4())}
        }
        mock_persistence = AsyncMock()
        mock_container = {
            "container_id": mock_player.get_equipped_items()["backpack"]["inner_container"],
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }
        mock_persistence.get_container.return_value = mock_container

        with patch("server.commands.look_container.logger"):
            result = await _try_lookup_container_implicit(
                "backpack", "backpack", None, mock_room, mock_player, mock_persistence, "testuser"
            )

            assert result is not None
            assert "Container" in result["result"] or "backpack" in result["result"]
            assert "Capacity:" in result["result"]

    @pytest.mark.asyncio
    async def test_try_lookup_container_implicit_not_found(self) -> None:
        """Test implicit lookup when container is not found."""
        mock_room = MagicMock()
        mock_room.get_containers.return_value = []
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {}
        mock_persistence = AsyncMock()

        result = await _try_lookup_container_implicit(
            "backpack", "backpack", None, mock_room, mock_player, mock_persistence, "testuser"
        )

        assert result is None
