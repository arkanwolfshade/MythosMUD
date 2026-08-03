"""Unit tests for inventory put command internals."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_put_command import (
    PutCommandRuntime,
    PutValidatedWork,
    _put_resolve_container_id,
    _put_run_validated,
    _put_transfer_finish,
    handle_put_command,
)
from server.models.player import Player

from .inventory_commands_test_support import command_result_text


@pytest.mark.asyncio
async def test_put_resolve_container_id_room_container() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    room_manager = MagicMock()
    container = {"container_id": str(uuid.uuid4())}
    with (
        patch(
            "server.commands.inventory_put_command.find_container_in_room",
            return_value=(container, container["container_id"]),
        ),
        patch(
            "server.commands.inventory_put_command.resolve_container_id",
            return_value=uuid.UUID(container["container_id"]),
        ),
    ):
        cid, err = await _put_resolve_container_id(MagicMock(), MagicMock(), player, room_manager, "room-1", "chest")
    assert err is None
    assert cid == uuid.UUID(container["container_id"])


@pytest.mark.asyncio
async def test_put_resolve_container_not_found() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    with (
        patch("server.commands.inventory_put_command.find_container_in_room", return_value=(None, None)),
        patch(
            "server.commands.inventory_put_command.find_wearable_container_for_put",
            new=AsyncMock(return_value=(None, None)),
        ),
    ):
        cid, err = await _put_resolve_container_id(MagicMock(), MagicMock(), player, MagicMock(), "room-1", "bag")
    assert cid is None
    assert err is not None
    assert "don't see" in command_result_text(err)


@pytest.mark.asyncio
async def test_put_resolve_container_missing_id() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    with (
        patch("server.commands.inventory_put_command.find_container_in_room", return_value=({"name": "chest"}, None)),
        patch("server.commands.inventory_put_command.resolve_container_id", return_value=None),
    ):
        cid, err = await _put_resolve_container_id(MagicMock(), MagicMock(), player, MagicMock(), "room-1", "chest")
    assert cid is None
    assert "no valid ID" in command_result_text(err)


@pytest.mark.asyncio
async def test_put_transfer_finish_error() -> None:
    player = MagicMock(spec=Player)
    with patch(
        "server.commands.inventory_put_command.transfer_item_to_container",
        new=AsyncMock(return_value={"error": "locked"}),
    ):
        result = await _put_transfer_finish(MagicMock(), MagicMock(), player, uuid.uuid4(), {}, 0, 1, "chest")
    assert command_result_text(result) == "locked"


@pytest.mark.asyncio
async def test_put_transfer_finish_not_success() -> None:
    player = MagicMock(spec=Player)
    with patch(
        "server.commands.inventory_put_command.transfer_item_to_container",
        new=AsyncMock(return_value={"success": False}),
    ):
        result = await _put_transfer_finish(MagicMock(), MagicMock(), player, uuid.uuid4(), {}, 0, 1, "chest")
    assert "Failed to transfer" in command_result_text(result)


@pytest.mark.asyncio
async def test_put_transfer_finish_success() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    item = {"item_name": "Coin", "item_id": "coin"}
    with (
        patch(
            "server.commands.inventory_put_command.transfer_item_to_container",
            new=AsyncMock(return_value={"success": True, "transfer_quantity": 2}),
        ),
        patch("server.commands.inventory_put_command.remove_item_from_inventory"),
        patch("server.commands.inventory_put_command.persist_player", new=AsyncMock(return_value=None)),
    ):
        result = await _put_transfer_finish(MagicMock(), MagicMock(), player, uuid.uuid4(), item, 0, 2, "chest")
    assert "You put 2x Coin into chest" in command_result_text(result)


@pytest.mark.asyncio
async def test_put_run_validated_container_error() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player.player_id = uuid.uuid4()
    player.current_room_id = "room-1"
    rt = PutCommandRuntime(MagicMock(), MagicMock(), MagicMock(), MagicMock())
    work = PutValidatedWork({}, player, "coin", "chest", 1, {"item_name": "Coin"}, 0)
    with patch(
        "server.commands.inventory_put_command._put_resolve_container_id",
        new=AsyncMock(return_value=(None, {"result": "missing"})),
    ):
        result = await _put_run_validated(rt, work)
    assert command_result_text(result) == "missing"


@pytest.mark.asyncio
async def test_handle_put_command_no_player() -> None:
    with patch(
        "server.commands.inventory_put_command.resolve_state_and_player",
        new=AsyncMock(return_value=(None, None, None, {"result": "not found"})),
    ):
        result = await handle_put_command({}, {}, MagicMock(), None, "Alice")
    assert command_result_text(result) == "not found"


@pytest.mark.asyncio
async def test_put_run_validated_success() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player.player_id = uuid.uuid4()
    player.current_room_id = "room-1"
    rt = PutCommandRuntime(MagicMock(), MagicMock(), MagicMock(), MagicMock())
    work = PutValidatedWork({}, player, "coin", "chest", 1, {"item_name": "Coin"}, 0)
    container_id = uuid.uuid4()
    with (
        patch(
            "server.commands.inventory_put_command._put_resolve_container_id",
            new=AsyncMock(return_value=(container_id, None)),
        ),
        patch(
            "server.commands.inventory_put_command._put_transfer_finish",
            new=AsyncMock(return_value={"result": "You put 1x Coin into chest."}),
        ),
    ):
        result = await _put_run_validated(rt, work)
    assert "You put" in command_result_text(result)


@pytest.mark.asyncio
async def test_handle_put_command_success() -> None:
    player = MagicMock(spec=Player)
    validation = ("coin", "chest", 1, MagicMock(), MagicMock(), {"item_name": "Coin"}, 0)
    with (
        patch(
            "server.commands.inventory_put_command.resolve_state_and_player",
            new=AsyncMock(return_value=(MagicMock(), MagicMock(), player, None)),
        ),
        patch(
            "server.commands.inventory_put_command.validate_put_command_inputs",
            new=AsyncMock(return_value=validation),
        ),
        patch(
            "server.commands.inventory_put_command._put_run_validated",
            new=AsyncMock(return_value={"result": "You put 1x Coin into chest."}),
        ),
    ):
        result = await handle_put_command({}, {}, MagicMock(), None, "Alice")
    assert "You put" in command_result_text(result)


@pytest.mark.asyncio
async def test_put_transfer_finish_persist_error() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    item = {"item_name": "Coin", "item_id": "coin"}
    with (
        patch(
            "server.commands.inventory_put_command.transfer_item_to_container",
            new=AsyncMock(return_value={"success": True, "transfer_quantity": 1}),
        ),
        patch("server.commands.inventory_put_command.remove_item_from_inventory"),
        patch(
            "server.commands.inventory_put_command.persist_player",
            new=AsyncMock(return_value={"result": "db error"}),
        ),
    ):
        result = await _put_transfer_finish(MagicMock(), MagicMock(), player, uuid.uuid4(), item, 0, 1, "chest")
    assert command_result_text(result) == "db error"


@pytest.mark.asyncio
async def test_handle_put_command_validation_error() -> None:
    player = MagicMock(spec=Player)
    with (
        patch(
            "server.commands.inventory_put_command.resolve_state_and_player",
            new=AsyncMock(return_value=(MagicMock(), MagicMock(), player, None)),
        ),
        patch(
            "server.commands.inventory_put_command.validate_put_command_inputs",
            new=AsyncMock(return_value={"result": "bad args"}),
        ),
    ):
        result = await handle_put_command({}, {}, MagicMock(), None, "Alice")
    assert command_result_text(result) == "bad args"
