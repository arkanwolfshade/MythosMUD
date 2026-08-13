"""Unit tests for server.commands.inventory_get_command internal paths."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_get_command import (
    GetCommandRuntime,
    GetItemSpec,
    _container_transfer_messages,
    _get_from_container_path,
    _get_transfer_out_of_container,
    _handle_get_from_room,
    handle_get_command,
)
from server.models.player import Player

from .inventory_commands_test_support import PickupTestWiring, command_result_text


def test_container_transfer_messages() -> None:
    texts = _container_transfer_messages("Alice", "chest", 2, "coin")
    assert "chest" in texts["result"]
    assert "Alice" in texts["room_message"]


@pytest.mark.asyncio
async def test_get_transfer_out_of_container_error() -> None:
    player = MagicMock(spec=Player)
    player.name = "P"
    with patch(
        "server.commands.inventory_get_command.transfer_item_from_container",
        new_callable=AsyncMock,
        return_value={"error": "nope"},
    ):
        result = await _get_transfer_out_of_container(MagicMock(), MagicMock(), player, uuid.uuid4(), {}, 1, "bag")
    assert result == {"result": "nope"}


@pytest.mark.asyncio
async def test_get_transfer_out_of_container_success() -> None:
    player = MagicMock(spec=Player)
    player.name = "P"
    with patch(
        "server.commands.inventory_get_command.transfer_item_from_container",
        new_callable=AsyncMock,
        return_value={"success": True, "transfer_quantity": 1, "item_display_name": "coin"},
    ):
        result = await _get_transfer_out_of_container(MagicMock(), MagicMock(), player, uuid.uuid4(), {}, 1, "bag")
    assert "You get" in str(result["result"])
    assert result["game_log_channel"] == "game-log"


@pytest.mark.asyncio
async def test_get_transfer_out_of_container_not_success() -> None:
    player = MagicMock(spec=Player)
    with patch(
        "server.commands.inventory_get_command.transfer_item_from_container",
        new_callable=AsyncMock,
        return_value={"success": False},
    ):
        result = await _get_transfer_out_of_container(MagicMock(), MagicMock(), player, uuid.uuid4(), {}, 1, "bag")
    assert "Failed to transfer" in str(result["result"])


@pytest.mark.asyncio
async def test_handle_get_from_room_index_error() -> None:
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    player.name = "P"
    rm = MagicMock()
    rm.list_room_drops.return_value = []
    with patch(
        "server.commands.inventory_get_command.resolve_pickup_item_index",
        return_value=(None, None, {"result": "bad index"}),
    ):
        result = await _handle_get_from_room(MagicMock(), MagicMock(), player, "room_1", "coin", None, rm)
    assert result == {"result": "bad index"}


@pytest.mark.asyncio
async def test_handle_get_from_room_unresolved_index() -> None:
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    with patch(
        "server.commands.inventory_get_command.resolve_pickup_item_index",
        return_value=(None, None, None),
    ):
        result = await _handle_get_from_room(MagicMock(), MagicMock(), player, "room_1", "coin", None, MagicMock())
    assert "Could not resolve" in str(result["result"])


@pytest.mark.asyncio
async def test_handle_get_from_room_invalid_quantity() -> None:
    player = MagicMock(spec=Player)
    player.player_id = uuid.uuid4()
    rm = MagicMock()
    rm.list_room_drops.return_value = [{"quantity": 1}]
    with patch(
        "server.commands.inventory_get_command.resolve_pickup_item_index",
        return_value=(0, None, None),
    ):
        result = await _handle_get_from_room(MagicMock(), MagicMock(), player, "room_1", "coin", 0, rm)
    assert "positive" in str(result["result"]).lower()


@pytest.mark.asyncio
async def test_get_from_container_path_missing_container() -> None:
    player = MagicMock(spec=Player)
    player.current_room_id = "room_1"
    player.name = "P"
    rt = GetCommandRuntime(MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock())
    spec = GetItemSpec(player=player, item_name="coin", container_name="chest", quantity=1)
    with (
        patch("server.commands.inventory_get_command.find_container_in_room", return_value=(None, None)),
        patch(
            "server.commands.inventory_get_command.find_wearable_container",
            new_callable=AsyncMock,
            return_value=(None, None),
        ),
    ):
        result = await _get_from_container_path(rt, spec)
    assert "don't see" in str(result["result"]).lower()


@pytest.mark.asyncio
async def test_get_from_container_path_item_not_in_container() -> None:
    player = MagicMock(spec=Player)
    player.current_room_id = "room_1"
    player.name = "P"
    rt = GetCommandRuntime(MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock())
    spec = GetItemSpec(player=player, item_name="coin", container_name="chest", quantity=1)
    container_id = uuid.uuid4()
    with (
        patch(
            "server.commands.inventory_get_command.find_container_in_room",
            return_value=({"id": str(container_id)}, container_id),
        ),
        patch(
            "server.commands.inventory_get_command.parse_container_items",
            return_value=([{"item_name": "other"}], container_id),
        ),
        patch(
            "server.commands.inventory_get_command.find_item_in_container",
            return_value=(None, None),
        ),
    ):
        result = await _get_from_container_path(rt, spec)
    assert "don't see 'coin'" in str(result["result"])


@pytest.mark.asyncio
async def test_handle_get_command_player_not_found() -> None:
    with patch(
        "server.commands.inventory_get_command.resolve_state_and_player",
        new_callable=AsyncMock,
        return_value=(None, None, None, {"result": "missing"}),
    ):
        result = await handle_get_command({}, {"name": "X"}, MagicMock(), None, "X")
    assert result == {"result": "missing"}


@pytest.mark.asyncio
async def test_handle_get_command_uses_pickup_wiring() -> None:
    w = PickupTestWiring()
    stack = {"item_name": "coin", "quantity": 3}
    w.set_floor_stack(stack)
    with patch(
        "server.commands.inventory_get_command.validate_get_command_inputs",
        new_callable=AsyncMock,
        return_value=("coin", "room", None, MagicMock(), w.room_manager),
    ):
        with patch(
            "server.commands.inventory_get_command.complete_pickup_after_floor_extract",
            new_callable=AsyncMock,
            return_value={"result": "picked"},
        ):
            with patch(
                "server.commands.inventory_get_command.resolve_pickup_item_index",
                return_value=(0, None, None),
            ):
                result = await handle_get_command(
                    {"item": "coin", "container": "room"},
                    {"name": "TestPlayer"},
                    w.request,
                    None,
                    "TestPlayer",
                )
    assert command_result_text(result) == "picked"
