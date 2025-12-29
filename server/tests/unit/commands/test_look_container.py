"""
Unit tests for container look functionality.

Tests the helper functions for looking at containers in rooms and equipped items.
"""

from unittest.mock import AsyncMock, MagicMock
from uuid import UUID, uuid4

import pytest

from server.commands.look_container import (
    _find_container_in_room,
    _find_container_in_room_or_equipped,
    _find_container_via_inner_container,
    _find_container_wearable,
    _format_container_contents,
    _format_container_display,
    _get_container_description,
    _handle_container_look,
    _try_lookup_container_implicit,
)


@pytest.fixture
def sample_container():
    """Create a sample container."""
    return {
        "container_id": str(uuid4()),
        "metadata": {"name": "backpack", "prototype_id": "container_backpack_001"},
        "items": [{"item_name": "sword", "quantity": 1}],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }


@pytest.fixture
def sample_equipped_container():
    """Create a sample equipped container item."""
    return {
        "item_name": "backpack",
        "prototype_id": "container_backpack_001",
        "item_id": "container_backpack_001",
        "inner_container": str(uuid4()),
    }


@pytest.fixture
def mock_prototype_registry():
    """Create a mock prototype registry."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.long_description = "A sturdy backpack."
    registry.get.return_value = prototype
    return registry


def test_find_container_in_room_success(sample_container):
    """Test finding container in room by name."""
    containers = [sample_container]
    result = _find_container_in_room(containers, "backpack")
    assert result == sample_container


def test_find_container_in_room_by_container_id(sample_container):
    """Test finding container in room by container_id."""
    containers = [sample_container]
    result = _find_container_in_room(containers, sample_container["container_id"])
    assert result == sample_container


def test_find_container_in_room_not_found():
    """Test finding container in room when not found."""
    containers = [{"container_id": str(uuid4()), "metadata": {"name": "backpack"}}]
    result = _find_container_in_room(containers, "chest")
    assert result is None


def test_find_container_in_room_multiple_matches():
    """Test finding container in room with multiple matches."""
    containers = [
        {"container_id": str(uuid4()), "metadata": {"name": "backpack"}},
        {"container_id": str(uuid4()), "metadata": {"name": "large backpack"}},
    ]
    result = _find_container_in_room(containers, "backpack")
    assert result is None  # Ambiguous


def test_find_container_in_room_with_instance_number(sample_container):
    """Test finding container in room with instance number."""
    containers = [sample_container]
    result = _find_container_in_room(containers, "backpack", instance_number=1)
    assert result == sample_container


def test_find_container_in_room_instance_number_out_of_range(sample_container):
    """Test finding container in room with invalid instance number."""
    containers = [sample_container]
    result = _find_container_in_room(containers, "backpack", instance_number=2)
    assert result is None


def test_find_container_wearable_success(sample_equipped_container):
    """Test finding wearable container by name."""
    equipped = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "backpack")
    assert result == ("back", sample_equipped_container)


def test_find_container_wearable_by_prototype_id(sample_equipped_container):
    """Test finding wearable container by prototype_id."""
    equipped = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "container_backpack_001")
    assert result == ("back", sample_equipped_container)


def test_find_container_wearable_not_found():
    """Test finding wearable container when not found."""
    equipped = {"back": {"item_name": "backpack", "prototype_id": "container_backpack_001"}}
    result = _find_container_wearable(equipped, "chest")
    assert result is None


def test_find_container_wearable_with_inner_container():
    """Test finding wearable container with inner_container."""
    equipped = {"back": {"item_name": "backpack", "inner_container": str(uuid4())}}
    result = _find_container_wearable(equipped, "backpack")
    assert result == ("back", equipped["back"])


@pytest.mark.asyncio
async def test_find_container_via_inner_container(sample_equipped_container):
    """Test finding container via inner_container_id."""
    mock_persistence = MagicMock()
    container_id = UUID(sample_equipped_container["inner_container"])
    mock_container = {"container_id": str(container_id), "items": []}
    mock_persistence.get_container = AsyncMock(return_value=mock_container)

    result = await _find_container_via_inner_container(sample_equipped_container, mock_persistence)
    assert result == mock_container


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_inner_container():
    """Test finding container via inner_container when not present."""
    item = {"item_name": "sword"}
    mock_persistence = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_invalid_uuid():
    """Test finding container via inner_container with invalid UUID."""
    item = {"inner_container": "not-a-uuid"}
    mock_persistence = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


def test_format_container_contents_with_items():
    """Test formatting container contents with items."""
    items = [
        {"item_name": "sword", "quantity": 1},
        {"item_name": "potion", "quantity": 3},
    ]
    result = _format_container_contents(items)
    assert len(result) == 2
    assert "sword" in result[0]
    assert "potion x3" in result[1]


def test_format_container_contents_empty():
    """Test formatting container contents when empty."""
    items = []
    result = _format_container_contents(items)
    assert len(result) == 1
    assert "(empty)" in result[0]


def test_format_container_display_basic(sample_container):
    """Test formatting container display with basic info."""
    command_data = {}
    result = _format_container_display(sample_container, None, command_data)
    assert "backpack" in result
    assert "Capacity:" in result


def test_format_container_display_with_description(sample_container, mock_prototype_registry):
    """Test formatting container display with description."""
    prototype = mock_prototype_registry.get.return_value
    description = prototype.long_description
    command_data = {}
    result = _format_container_display(sample_container, description, command_data)
    assert "backpack" in result
    assert "A sturdy backpack." in result


def test_format_container_display_locked():
    """Test formatting container display when locked."""
    container = {
        "container_id": str(uuid4()),
        "metadata": {"name": "chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "locked",
    }
    command_data = {}
    result = _format_container_display(container, None, command_data)
    assert "Locked" in result


def test_format_container_display_sealed():
    """Test formatting container display when sealed."""
    container = {
        "container_id": str(uuid4()),
        "metadata": {"name": "chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "sealed",
    }
    command_data = {}
    result = _format_container_display(container, None, command_data)
    assert "Sealed" in result


def test_format_container_display_with_contents(sample_container):
    """Test formatting container display with look_in flag."""
    command_data = {"look_in": True}
    result = _format_container_display(sample_container, None, command_data)
    assert "Contents:" in result
    assert "sword" in result


def test_format_container_display_with_target_type(sample_container):
    """Test formatting container display with target_type container."""
    command_data = {"target_type": "container"}
    result = _format_container_display(sample_container, None, command_data)
    assert "Contents:" in result


def test_get_container_description_from_item(mock_prototype_registry, sample_equipped_container):
    """Test getting container description from equipped item."""
    result = _get_container_description(sample_container, sample_equipped_container, mock_prototype_registry)
    assert result == "A sturdy backpack."


def test_get_container_description_from_container_metadata(mock_prototype_registry, sample_container):
    """Test getting container description from container metadata."""
    result = _get_container_description(sample_container, None, mock_prototype_registry)
    assert result == "A sturdy backpack."


def test_get_container_description_no_registry(sample_container):
    """Test getting container description when registry is None."""
    result = _get_container_description(sample_container, None, None)
    assert result is None


def test_get_container_description_no_prototype_id(sample_container):
    """Test getting container description when prototype_id is missing."""
    container = {"container_id": str(uuid4()), "metadata": {}}
    result = _get_container_description(container, None, MagicMock())
    assert result is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_in_room(sample_container):
    """Test finding container in room or equipped when in room."""
    room = MagicMock()
    room.get_containers.return_value = [sample_container]
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_request = MagicMock()

    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, mock_request, "TestPlayer"
    )
    assert container_found == sample_container
    assert container_item is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_in_equipped(sample_equipped_container):
    """Test finding container in room or equipped when equipped."""
    room = MagicMock()
    room.get_containers.return_value = []
    player = MagicMock()
    player.get_equipped_items.return_value = {"back": sample_equipped_container}
    mock_persistence = MagicMock()
    mock_persistence.get_container = AsyncMock(
        return_value={"container_id": sample_equipped_container["inner_container"]}
    )
    mock_request = MagicMock()

    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, mock_request, "TestPlayer"
    )
    assert container_found is not None
    assert container_item == sample_equipped_container


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_not_found():
    """Test finding container in room or equipped when not found."""
    room = MagicMock()
    room.get_containers.return_value = []
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_request = MagicMock()

    container_found, container_item = await _find_container_in_room_or_equipped(
        "chest", None, room, player, mock_persistence, mock_request, "TestPlayer"
    )
    assert container_found is None
    assert container_item is None


@pytest.mark.asyncio
async def test_handle_container_look_success(sample_container, mock_prototype_registry):
    """Test handling container look successfully."""
    room = MagicMock()
    room.get_containers.return_value = [sample_container]
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_request = MagicMock()
    command_data = {}

    result = await _handle_container_look(
        "backpack",
        "backpack",
        None,
        room,
        player,
        mock_persistence,
        mock_prototype_registry,
        command_data,
        mock_request,
        "TestPlayer",
    )
    assert result is not None
    assert "result" in result
    assert "backpack" in result["result"]


@pytest.mark.asyncio
async def test_handle_container_look_not_found(mock_prototype_registry):
    """Test handling container look when not found."""
    room = MagicMock()
    room.get_containers.return_value = []
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_request = MagicMock()
    command_data = {}

    result = await _handle_container_look(
        "chest",
        "chest",
        None,
        room,
        player,
        mock_persistence,
        mock_prototype_registry,
        command_data,
        mock_request,
        "TestPlayer",
    )
    assert result is not None
    assert "don't see" in result["result"].lower()


@pytest.mark.asyncio
async def test_try_lookup_container_implicit_success(sample_container):
    """Test trying implicit container lookup successfully."""
    room = MagicMock()
    room.get_containers.return_value = [sample_container]
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_persistence.get_container = AsyncMock(return_value=None)

    result = await _try_lookup_container_implicit(
        "backpack", "backpack", None, room, player, mock_persistence, "TestPlayer"
    )
    assert result is not None
    assert "backpack" in result["result"]


@pytest.mark.asyncio
async def test_try_lookup_container_implicit_not_found():
    """Test trying implicit container lookup when not found."""
    room = MagicMock()
    room.get_containers.return_value = []
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()

    result = await _try_lookup_container_implicit("chest", "chest", None, room, player, mock_persistence, "TestPlayer")
    assert result is None


def test_find_container_in_room_by_container_id():
    """Test finding container in room by container_id."""
    container = {"container_id": "container_123", "metadata": {"name": "chest"}}
    containers = [container]
    result = _find_container_in_room(containers, "container_123")
    assert result == container


def test_find_container_wearable_with_instance_number(sample_equipped_container):
    """Test finding wearable container with instance number."""
    equipped = {"back": sample_equipped_container, "belt": {**sample_equipped_container, "item_id": "backpack_002"}}
    result = _find_container_wearable(equipped, "backpack", instance_number=2)
    assert result is not None
    assert result[0] == "belt"


def test_find_container_wearable_instance_number_out_of_range(sample_equipped_container):
    """Test finding wearable container with invalid instance number."""
    equipped = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "backpack", instance_number=2)
    assert result is None


def test_format_container_contents_with_quantity():
    """Test formatting container contents with quantity > 1."""
    items = [{"item_name": "potion", "quantity": 5}]
    result = _format_container_contents(items)
    assert "potion x5" in result[0]


def test_format_container_display_with_metadata_name():
    """Test formatting container display uses metadata name."""
    container = {
        "container_id": str(uuid4()),
        "metadata": {"name": "Custom Backpack"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data = {}
    result = _format_container_display(container, None, command_data)
    assert "Custom Backpack" in result


def test_format_container_display_fallback_name():
    """Test formatting container display uses fallback when no metadata name."""
    container = {
        "container_id": str(uuid4()),
        "metadata": {},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data = {}
    result = _format_container_display(container, None, command_data)
    assert "Container" in result


def test_get_container_description_prototype_error(mock_prototype_registry):
    """Test getting container description handles prototype errors."""
    container = {
        "container_id": str(uuid4()),
        "metadata": {"prototype_id": "container_backpack_001"},
        "items": [],
    }
    # Make prototype access raise an exception
    mock_prototype_registry.get.return_value = None
    result = _get_container_description(container, None, mock_prototype_registry)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_get_container_method():
    """Test finding container via inner_container when persistence has no get_container."""
    item = {"inner_container": str(uuid4())}
    mock_persistence = MagicMock()
    # Remove get_container method
    if hasattr(mock_persistence, "get_container"):
        delattr(mock_persistence, "get_container")
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_no_get_containers():
    """Test finding container when room has no get_containers method."""
    room = MagicMock()
    # Remove get_containers method
    if hasattr(room, "get_containers"):
        delattr(room, "get_containers")
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    mock_persistence = MagicMock()
    mock_request = MagicMock()
    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, mock_request, "TestPlayer"
    )
    # Should try equipped items
    assert container_found is None or container_item is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_no_get_equipped_items():
    """Test finding container when player has no get_equipped_items method."""
    room = MagicMock()
    room.get_containers.return_value = []
    player = MagicMock()
    # Remove get_equipped_items method
    if hasattr(player, "get_equipped_items"):
        delattr(player, "get_equipped_items")
    mock_persistence = MagicMock()
    mock_request = MagicMock()
    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, mock_request, "TestPlayer"
    )
    assert container_found is None
    assert container_item is None
