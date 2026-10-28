"""Unit tests for handle_pickup_command (split from test_inventory_commands for Lizard limits)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands.inventory_commands import handle_pickup_command
from server.services.inventory_service import InventoryService
from server.tests.fixtures.shared.player_registry import RegistryHarness

from .inventory_commands_test_support import (
    PickupTestWiring,
    command_result_text,
    inventory_has_named_item,
    sample_floor_item_stack,
)


async def _pickup(
    w: PickupTestWiring,
    command_data: dict[str, object],
    monkeypatch: pytest.MonkeyPatch,
    *,
    fail_save: bool = False,
) -> tuple[Mapping[str, object], RegistryHarness]:
    """Pick up through the real player registry (ADR-029 step 4a); ``fail_save`` makes its commit fail."""
    harness = w.install_registry(monkeypatch)
    if fail_save:
        harness.db.fail_commits = 1
        harness.db.commit_error = SQLAlchemyError("database unavailable")
    with patch("server.commands.inventory_service_helpers.get_shared_services") as mock_get_services:
        mock_get_services.return_value = (InventoryService(), MagicMock(), MagicMock())
        with patch(
            "server.commands.inventory_command_helpers.build_and_broadcast_inventory_event",
            new_callable=AsyncMock,
        ):
            result = await handle_pickup_command(command_data, {"name": "TestPlayer"}, w.request, None, "TestPlayer")
    return result, harness


@pytest.mark.asyncio
async def test_handle_pickup_command(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test handle_pickup_command() picks up item by index and commits it through the registry."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)

    result, harness = await _pickup(w, {"index": 1}, monkeypatch)

    assert "result" in result
    rt = command_result_text(result)
    assert "picks up" in rt or "pick up" in rt
    w.take_room_drop.assert_called_once_with("room_001", 0, 1)
    assert inventory_has_named_item(harness.saved_carried(), "sword"), "the floor stack reached the inventory write"


@pytest.mark.asyncio
async def test_handle_pickup_command_emits_inventory_updated(monkeypatch: pytest.MonkeyPatch) -> None:
    """A successful pickup pushes inventory_updated so a GUI inventory panel stays in sync."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)
    with patch("server.commands.inventory_pickup_command.emit_inventory_updated", new_callable=AsyncMock) as mock_emit:
        result, _harness = await _pickup(w, {"index": 1}, monkeypatch)

    assert "result" in result
    mock_emit.assert_awaited_once_with(w.connection_manager, w.player_id, w.player)


@pytest.mark.asyncio
async def test_handle_pickup_command_save_failure_restores_the_drop_and_rolls_back(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """On a failed save the floor stack goes back to the room and the registry keeps the old inventory."""
    stack = sample_floor_item_stack()
    w = PickupTestWiring()
    w.set_floor_stack(stack)

    result, harness = await _pickup(w, {"index": 1}, monkeypatch, fail_save=True)

    assert command_result_text(result) == "An error occurred while saving your inventory."
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
    view = harness.registry.peek(w.player_id)
    assert view is not None and list(view.inventory.carried) == []  # rolled back


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
async def test_handle_pickup_command_inventory_capacity_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """A full inventory refuses the stack, puts it back on the floor, and writes nothing."""
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

    result, harness = await _pickup(w, {"index": 1}, monkeypatch)

    assert "result" in result
    rt = command_result_text(result).lower()
    assert "cannot pick" in rt or "full" in rt or "capacity" in rt
    w.add_room_drop.assert_called_once()
    assert harness.saved_carried() is None
