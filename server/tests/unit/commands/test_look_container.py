"""
Unit tests for container look functionality.

Tests the helper functions for looking at containers in rooms and equipped items.
"""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests look_container helper functions.

from __future__ import annotations

from collections.abc import Mapping
from unittest.mock import AsyncMock, MagicMock
from uuid import UUID, uuid4

import pytest

from server.commands.look_container import (
    ContainerLookArgs,
    JsonMap,
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


def _result_text(response: Mapping[str, object]) -> str:
    raw = response["result"]
    assert isinstance(raw, str)
    return raw


@pytest.fixture
def sample_container() -> JsonMap:
    """Create a sample container."""
    return {
        "container_id": str(uuid4()),
        "metadata": {"name": "backpack", "prototype_id": "container_backpack_001"},
        "items": [{"item_name": "sword", "quantity": 1}],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }


@pytest.fixture
def sample_equipped_container() -> JsonMap:
    """Create a sample equipped container item."""
    return {
        "item_name": "backpack",
        "prototype_id": "container_backpack_001",
        "item_id": "container_backpack_001",
        "inner_container": str(uuid4()),
    }


@pytest.fixture
def mock_prototype_registry() -> MagicMock:
    """Create a mock prototype registry."""
    prototype: MagicMock = MagicMock()
    prototype.long_description = "A sturdy backpack."
    get_proto: MagicMock = MagicMock(return_value=prototype)
    registry: MagicMock = MagicMock()
    registry.get = get_proto
    return registry


def test_find_container_in_room_success(sample_container: JsonMap) -> None:
    """Test finding container in room by name."""
    containers: list[JsonMap] = [sample_container]
    result = _find_container_in_room(containers, "backpack")
    assert result == sample_container


def test_find_container_in_room_by_container_id(sample_container: JsonMap) -> None:
    """Test finding container in room by container_id."""
    containers: list[JsonMap] = [sample_container]
    result = _find_container_in_room(containers, str(sample_container["container_id"]))
    assert result == sample_container


def test_find_container_in_room_not_found() -> None:
    """Test finding container in room when not found."""
    containers: list[JsonMap] = [{"container_id": str(uuid4()), "metadata": {"name": "backpack"}}]
    result = _find_container_in_room(containers, "chest")
    assert result is None


def test_find_container_in_room_multiple_matches() -> None:
    """Test finding container in room with multiple matches."""
    containers: list[JsonMap] = [
        {"container_id": str(uuid4()), "metadata": {"name": "backpack"}},
        {"container_id": str(uuid4()), "metadata": {"name": "large backpack"}},
    ]
    result = _find_container_in_room(containers, "backpack")
    assert result is None  # Ambiguous


def test_find_container_in_room_with_instance_number(sample_container: JsonMap) -> None:
    """Test finding container in room with instance number."""
    containers: list[JsonMap] = [sample_container]
    result = _find_container_in_room(containers, "backpack", instance_number=1)
    assert result == sample_container


def test_find_container_in_room_instance_number_out_of_range(sample_container: JsonMap) -> None:
    """Test finding container in room with invalid instance number."""
    containers: list[JsonMap] = [sample_container]
    result = _find_container_in_room(containers, "backpack", instance_number=2)
    assert result is None


def test_find_container_wearable_success(sample_equipped_container: JsonMap) -> None:
    """Test finding wearable container by name."""
    equipped: dict[str, JsonMap] = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "backpack")
    assert result == ("back", sample_equipped_container)


def test_find_container_wearable_by_prototype_id(sample_equipped_container: JsonMap) -> None:
    """Test finding wearable container by prototype_id."""
    equipped: dict[str, JsonMap] = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "container_backpack_001")
    assert result == ("back", sample_equipped_container)


def test_find_container_wearable_not_found() -> None:
    """Test finding wearable container when not found."""
    equipped: dict[str, JsonMap] = {"back": {"item_name": "backpack", "prototype_id": "container_backpack_001"}}
    result = _find_container_wearable(equipped, "chest")
    assert result is None


def test_find_container_wearable_with_inner_container() -> None:
    """Test finding wearable container with inner_container."""
    equipped: dict[str, JsonMap] = {"back": {"item_name": "backpack", "inner_container": str(uuid4())}}
    result = _find_container_wearable(equipped, "backpack")
    assert result == ("back", equipped["back"])


@pytest.mark.asyncio
async def test_find_container_via_inner_container(sample_equipped_container: JsonMap) -> None:
    """Test finding container via inner_container_id."""
    inner = sample_equipped_container["inner_container"]
    assert isinstance(inner, str)
    mock_persistence: MagicMock = MagicMock()
    container_id = UUID(inner)
    mock_container: JsonMap = {"container_id": str(container_id), "items": []}
    get_container: AsyncMock = AsyncMock(return_value=mock_container)
    mock_persistence.get_container = get_container

    result = await _find_container_via_inner_container(sample_equipped_container, mock_persistence)
    assert result == mock_container


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_inner_container() -> None:
    """Test finding container via inner_container when not present."""
    item: JsonMap = {"item_name": "sword"}
    mock_persistence: MagicMock = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_invalid_uuid() -> None:
    """Test finding container via inner_container with invalid UUID."""
    item: JsonMap = {"inner_container": "not-a-uuid"}
    mock_persistence: MagicMock = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


def test_format_container_contents_with_items() -> None:
    """Test formatting container contents with items."""
    items: list[JsonMap] = [
        {"item_name": "sword", "quantity": 1},
        {"item_name": "potion", "quantity": 3},
    ]
    result = _format_container_contents(items)
    assert len(result) == 2
    assert "sword" in result[0]
    assert "potion x3" in result[1]


def test_format_container_contents_empty() -> None:
    """Test formatting container contents when empty."""
    items: list[JsonMap] = []
    result = _format_container_contents(items)
    assert len(result) == 1
    assert "(empty)" in result[0]


def test_format_container_display_basic(sample_container: JsonMap) -> None:
    """Test formatting container display with basic info."""
    command_data: JsonMap = {}
    result = _format_container_display(sample_container, None, command_data)
    assert "backpack" in result
    assert "Capacity:" in result


def test_format_container_display_with_description(sample_container: JsonMap) -> None:
    """Test formatting container display with description."""
    description = "A sturdy backpack."
    command_data: JsonMap = {}
    result = _format_container_display(sample_container, description, command_data)
    assert "backpack" in result
    assert "A sturdy backpack." in result


def test_format_container_display_locked() -> None:
    """Test formatting container display when locked."""
    container: JsonMap = {
        "container_id": str(uuid4()),
        "metadata": {"name": "chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "locked",
    }
    command_data: JsonMap = {}
    result = _format_container_display(container, None, command_data)
    assert "Locked" in result


def test_format_container_display_sealed() -> None:
    """Test formatting container display when sealed."""
    container: JsonMap = {
        "container_id": str(uuid4()),
        "metadata": {"name": "chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "sealed",
    }
    command_data: JsonMap = {}
    result = _format_container_display(container, None, command_data)
    assert "Sealed" in result


def test_format_container_display_with_contents(sample_container: JsonMap) -> None:
    """Test formatting container display with look_in flag."""
    command_data: JsonMap = {"look_in": True}
    result = _format_container_display(sample_container, None, command_data)
    assert "Contents:" in result
    assert "sword" in result


def test_format_container_display_with_target_type(sample_container: JsonMap) -> None:
    """Test formatting container display with target_type container."""
    command_data: JsonMap = {"target_type": "container"}
    result = _format_container_display(sample_container, None, command_data)
    assert "Contents:" in result


def test_get_container_description_from_item(
    mock_prototype_registry: MagicMock,
    sample_equipped_container: JsonMap,
    sample_container: JsonMap,
) -> None:
    """Test getting container description from equipped item."""
    result = _get_container_description(sample_container, sample_equipped_container, mock_prototype_registry)
    assert result == "A sturdy backpack."


def test_get_container_description_from_container_metadata(
    mock_prototype_registry: MagicMock, sample_container: JsonMap
) -> None:
    """Test getting container description from container metadata."""
    result = _get_container_description(sample_container, None, mock_prototype_registry)
    assert result == "A sturdy backpack."


def test_get_container_description_no_registry(sample_container: JsonMap) -> None:
    """Test getting container description when registry is None."""
    result = _get_container_description(sample_container, None, None)
    assert result is None


def test_get_container_description_no_prototype_id() -> None:
    """Test getting container description when prototype_id is missing."""
    container: JsonMap = {"container_id": str(uuid4()), "metadata": {}}
    result = _get_container_description(container, None, MagicMock())
    assert result is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_in_room(sample_container: JsonMap) -> None:
    """Test finding container in room or equipped when in room."""
    get_containers: MagicMock = MagicMock(return_value=[sample_container])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()

    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, None, "TestPlayer"
    )
    assert container_found == sample_container
    assert container_item is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_in_equipped(sample_equipped_container: JsonMap) -> None:
    """Test finding container in room or equipped when equipped."""
    get_containers: MagicMock = MagicMock(return_value=[])
    get_equipped_items: MagicMock = MagicMock(return_value={"back": sample_equipped_container})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()
    get_container: AsyncMock = AsyncMock(return_value={"container_id": sample_equipped_container["inner_container"]})
    mock_persistence.get_container = get_container

    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, None, "TestPlayer"
    )
    assert container_found is not None
    assert container_item == sample_equipped_container


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_not_found() -> None:
    """Test finding container in room or equipped when not found."""
    get_containers: MagicMock = MagicMock(return_value=[])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()

    container_found, container_item = await _find_container_in_room_or_equipped(
        "chest", None, room, player, mock_persistence, None, "TestPlayer"
    )
    assert container_found is None
    assert container_item is None


@pytest.mark.asyncio
async def test_handle_container_look_success(sample_container: JsonMap, mock_prototype_registry: MagicMock) -> None:
    """Test handling container look successfully."""
    get_containers: MagicMock = MagicMock(return_value=[sample_container])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()
    command_data: JsonMap = {}

    result = await _handle_container_look(
        ContainerLookArgs(
            target="backpack",
            target_lower="backpack",
            instance_number=None,
            room=room,
            player=player,
            persistence=mock_persistence,
            prototype_registry=mock_prototype_registry,
            command_data=command_data,
            request=None,
            player_name="TestPlayer",
        )
    )
    assert result is not None
    text = _result_text(result)
    assert "backpack" in text


@pytest.mark.asyncio
async def test_handle_container_look_not_found(mock_prototype_registry: MagicMock) -> None:
    """Test handling container look when not found."""
    get_containers: MagicMock = MagicMock(return_value=[])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()
    command_data: JsonMap = {}

    result = await _handle_container_look(
        ContainerLookArgs(
            target="chest",
            target_lower="chest",
            instance_number=None,
            room=room,
            player=player,
            persistence=mock_persistence,
            prototype_registry=mock_prototype_registry,
            command_data=command_data,
            request=None,
            player_name="TestPlayer",
        )
    )
    assert result is not None
    assert "don't see" in _result_text(result).lower()


@pytest.mark.asyncio
async def test_try_lookup_container_implicit_success(sample_container: JsonMap) -> None:
    """Test trying implicit container lookup successfully."""
    get_containers: MagicMock = MagicMock(return_value=[sample_container])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()
    get_container: AsyncMock = AsyncMock(return_value=None)
    mock_persistence.get_container = get_container

    result = await _try_lookup_container_implicit(
        "backpack", "backpack", None, room, player, mock_persistence, "TestPlayer"
    )
    assert result is not None
    assert "backpack" in _result_text(result)


@pytest.mark.asyncio
async def test_try_lookup_container_implicit_not_found() -> None:
    """Test trying implicit container lookup when not found."""
    get_containers: MagicMock = MagicMock(return_value=[])
    get_equipped_items: MagicMock = MagicMock(return_value={})
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()

    result = await _try_lookup_container_implicit("chest", "chest", None, room, player, mock_persistence, "TestPlayer")
    assert result is None


def test_find_container_wearable_with_instance_number(sample_equipped_container: JsonMap) -> None:
    """Test finding wearable container with instance number."""
    second: JsonMap = {**sample_equipped_container, "item_id": "backpack_002"}
    equipped: dict[str, JsonMap] = {"back": sample_equipped_container, "belt": second}
    result = _find_container_wearable(equipped, "backpack", instance_number=2)
    assert result is not None
    assert result[0] == "belt"


def test_find_container_wearable_instance_number_out_of_range(sample_equipped_container: JsonMap) -> None:
    """Test finding wearable container with invalid instance number."""
    equipped: dict[str, JsonMap] = {"back": sample_equipped_container}
    result = _find_container_wearable(equipped, "backpack", instance_number=2)
    assert result is None


def test_format_container_contents_with_quantity() -> None:
    """Test formatting container contents with quantity > 1."""
    items: list[JsonMap] = [{"item_name": "potion", "quantity": 5}]
    result = _format_container_contents(items)
    assert "potion x5" in result[0]


def test_format_container_display_with_metadata_name() -> None:
    """Test formatting container display uses metadata name."""
    container: JsonMap = {
        "container_id": str(uuid4()),
        "metadata": {"name": "Custom Backpack"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data: JsonMap = {}
    result = _format_container_display(container, None, command_data)
    assert "Custom Backpack" in result


def test_format_container_display_fallback_name() -> None:
    """Test formatting container display uses fallback when no metadata name."""
    container: JsonMap = {
        "container_id": str(uuid4()),
        "metadata": {},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data: JsonMap = {}
    result = _format_container_display(container, None, command_data)
    assert "Container" in result


def test_get_container_description_prototype_error(mock_prototype_registry: MagicMock) -> None:
    """Test getting container description handles prototype errors."""
    container: JsonMap = {
        "container_id": str(uuid4()),
        "metadata": {"prototype_id": "container_backpack_001"},
        "items": [],
    }
    get_proto: MagicMock = MagicMock(return_value=None)
    mock_prototype_registry.get = get_proto
    result = _get_container_description(container, None, mock_prototype_registry)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_get_container_method() -> None:
    """Test finding container via inner_container when persistence has no get_container."""
    item: JsonMap = {"inner_container": str(uuid4())}
    mock_persistence: MagicMock = MagicMock()
    if hasattr(mock_persistence, "get_container"):
        delattr(mock_persistence, "get_container")
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_no_get_containers() -> None:
    """Test finding container when room has no get_containers method."""
    room: MagicMock = MagicMock()
    if hasattr(room, "get_containers"):
        delattr(room, "get_containers")
    get_equipped_items: MagicMock = MagicMock(return_value={})
    player: MagicMock = MagicMock()
    player.get_equipped_items = get_equipped_items
    mock_persistence: MagicMock = MagicMock()
    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, None, "TestPlayer"
    )
    assert container_found is None or container_item is None


@pytest.mark.asyncio
async def test_find_container_in_room_or_equipped_no_get_equipped_items() -> None:
    """Test finding container when player has no get_equipped_items method."""
    get_containers: MagicMock = MagicMock(return_value=[])
    room: MagicMock = MagicMock()
    room.get_containers = get_containers
    player: MagicMock = MagicMock()
    if hasattr(player, "get_equipped_items"):
        delattr(player, "get_equipped_items")
    mock_persistence: MagicMock = MagicMock()
    container_found, container_item = await _find_container_in_room_or_equipped(
        "backpack", None, room, player, mock_persistence, None, "TestPlayer"
    )
    assert container_found is None
    assert container_item is None
