"""Unit tests for handle_pickup_command (split from test_inventory_commands for Lizard limits)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_commands import handle_pickup_command
from server.services.inventory_service import InventoryService

from .inventory_commands_test_support import (
    PickupTestWiring,
    command_result_text,
    inventory_has_named_item,
    sample_floor_item_stack,
)


async def _pickup_with_persist_patch(
    w: PickupTestWiring,
    command_data: dict[str, object],
    mock_persist: AsyncMock,
) -> Mapping[str, object]:
    mock_inventory_service = InventoryService()
    with patch("server.commands.inventory_service_helpers.get_shared_services") as mock_get_services:
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), MagicMock())
        with patch("server.commands.inventory_pickup_command.persist_player", mock_persist):
            with patch(
                "server.commands.inventory_command_helpers.build_and_broadcast_inventory_event",
                new_callable=AsyncMock,
            ):
                return await handle_pickup_command(command_data, {"name": "TestPlayer"}, w.request, None, "TestPlayer")


@pytest.mark.asyncio
async def test_handle_pickup_command():
    """Test handle_pickup_command() picks up item by index."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)
    mock_persist = AsyncMock(return_value=None)
    result = await _pickup_with_persist_patch(w, {"index": 1}, mock_persist)

    assert "result" in result
    rt = command_result_text(result)
    assert "picks up" in rt or "pick up" in rt
    w.take_room_drop.assert_called_once_with("room_001", 0, 1)
    w.set_inventory.assert_called_once()
    inv_after = cast(object, w.set_inventory.call_args[0][0])
    assert inventory_has_named_item(inv_after, "sword"), "Pickup should merge the floor stack into player inventory"
    mock_persist.assert_awaited_once_with(w.persistence, w.player)


@pytest.mark.asyncio
async def test_handle_pickup_command_persist_failure_restores_drop_and_inventory():
    """On persist failure, floor stack is restored and inventory reverts (PR #461 rollback path)."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)
    persist_error = {"result": "Could not save inventory."}
    mock_persist = AsyncMock(return_value=persist_error)
    result = await _pickup_with_persist_patch(w, {"index": 1}, mock_persist)

    assert result == persist_error
    w.take_room_drop.assert_called_once_with("room_001", 0, 1)
    w.add_room_drop.assert_called_once()
    raw_drop = cast(tuple[object, object], tuple(w.add_room_drop.call_args[0]))
    drop_room_id: object = raw_drop[0]
    restored_stack: object = raw_drop[1]
    assert drop_room_id == "room_001"
    assert isinstance(restored_stack, dict)
    rs = cast(dict[str, object], restored_stack)
    assert rs.get("item_name") == "sword"
    assert rs.get("quantity") == 1
    assert w.set_inventory.call_count == 2
    inv_first = cast(object, w.set_inventory.call_args_list[0][0][0])
    inv_second = cast(object, w.set_inventory.call_args_list[1][0][0])
    assert inventory_has_named_item(inv_first, "sword")
    assert inv_second == []
    mock_persist.assert_awaited_once_with(w.persistence, w.player)


@pytest.mark.asyncio
async def test_handle_pickup_command_no_target():
    """Test handle_pickup_command() handles missing target."""
    w = PickupTestWiring()
    result = await handle_pickup_command({}, {"name": "TestPlayer"}, w.request, None, "TestPlayer")

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "usage" in rt or "pickup" in rt


@pytest.mark.asyncio
async def test_handle_pickup_command_no_room_manager():
    """Test handle_pickup_command() handles missing room manager."""
    w = PickupTestWiring()
    w.connection_manager.room_manager = None
    result = await handle_pickup_command({"index": 1}, {"name": "TestPlayer"}, w.request, None, "TestPlayer")

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "unavailable" in rt or "not available" in rt


@pytest.mark.asyncio
async def test_handle_pickup_command_invalid_index():
    """Test handle_pickup_command() handles invalid index."""
    w = PickupTestWiring()
    w.set_listed_drops([{"item_name": "sword"}])
    result = await handle_pickup_command({"index": 5}, {"name": "TestPlayer"}, w.request, None, "TestPlayer")

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "no such item" in rt or "not found" in rt


@pytest.mark.asyncio
async def test_handle_pickup_command_search_term_not_found():
    """Test handle_pickup_command() handles search term not found."""
    w = PickupTestWiring()
    w.set_listed_drops([{"item_name": "sword"}])
    result = await handle_pickup_command({"search_term": "bow"}, {"name": "TestPlayer"}, w.request, None, "TestPlayer")

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "no item" in rt or "matching" in rt


@pytest.mark.asyncio
async def test_handle_pickup_command_inventory_capacity_error():
    """Test handle_pickup_command() handles inventory capacity error."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)
    full_inventory = cast(
        list[dict[str, object]],
        [
            {
                "item_name": f"item_{i}",
                "item_id": f"item_{i}",
                "item_instance_id": str(uuid.uuid4()),
                "prototype_id": f"proto_{i}",
                "slot_type": "inventory",
                "quantity": 1,
            }
            for i in range(20)
        ],
    )
    w.set_player_inventory(full_inventory)

    mock_inventory_service = InventoryService()
    with patch("server.commands.inventory_service_helpers.get_shared_services") as mock_get_services:
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), MagicMock())
        result = await handle_pickup_command({"index": 1}, {"name": "TestPlayer"}, w.request, None, "TestPlayer")

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "cannot pick" in rt or "full" in rt or "capacity" in rt
    w.add_room_drop.assert_called_once()
