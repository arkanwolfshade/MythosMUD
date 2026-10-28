"""Unit tests for the bank commands: bank, deposit, withdraw (#977)."""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable, Generator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.bank_commands import handle_bank_command, handle_deposit_command, handle_withdraw_command
from server.commands.inventory_command_contracts import CommandResponse
from server.models.player import Player
from server.models.room import Room

from .inventory_commands_test_support import command_result_text

MODULE = "server.commands.bank_commands"
Handler = Callable[[dict[str, object], dict[str, object], object, None, str], Awaitable[CommandResponse]]


def _lamp(quantity: int = 1) -> dict[str, object]:
    return {"item_id": "lamp", "item_name": "Oil Lamp", "item_instance_id": "inst-lamp", "quantity": quantity}


def _coin(quantity: int = 5) -> dict[str, object]:
    return {"item_id": "coin", "quantity": quantity}


@dataclass
class Bank:
    """The patched world a bank command runs in."""

    player: Player
    box: dict[str, object]
    boxes_opened_for: list[uuid.UUID]  # owner of every get-or-create the command made

    @property
    def box_id(self) -> uuid.UUID:
        return uuid.UUID(str(self.box["container_id"]))


@contextmanager
def _bank_world(*, in_bank: bool = True, items: list[dict[str, object]] | None = None) -> Generator[Bank]:
    mock_player = MagicMock(spec=Player)
    mock_player.name = "Alice"
    mock_player.player_id = str(uuid.uuid4())
    mock_player.current_room_id = "bank_room" if in_bank else "street"
    player = cast(Player, mock_player)
    rooms = {
        "bank_room": Room({"id": "bank_room", "attributes": {"bank": True}}),
        "street": Room({"id": "street", "attributes": {"environment": "street_paved"}}),
    }
    persistence = MagicMock()
    persistence.get_room_by_id = MagicMock(side_effect=rooms.get)
    box: dict[str, object] = {
        "container_id": str(uuid.uuid4()),
        "capacity_slots": 100,
        "items_json": items or [],
    }
    opened_for: list[uuid.UUID] = []

    async def get_or_create(_persistence: object, owner_id: uuid.UUID) -> dict[str, object]:
        opened_for.append(owner_id)
        return box

    with (
        patch(
            f"{MODULE}.resolve_state_and_player",
            new=AsyncMock(return_value=(persistence, MagicMock(), player, None)),
        ),
        patch(f"{MODULE}.get_or_create_bank_box", new=get_or_create),
    ):
        yield Bank(player, box, opened_for)


async def _run(handler: Handler, command_data: dict[str, object] | None = None) -> CommandResponse:
    return await handler(command_data or {}, {"username": "alice"}, MagicMock(), None, "Alice")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("handler", "command_data"),
    [
        (handle_bank_command, {}),
        (handle_deposit_command, {"item": "lamp"}),
        (handle_withdraw_command, {"item": "lamp"}),
    ],
)
async def test_every_bank_command_refuses_outside_a_bank(handler: Handler, command_data: dict[str, object]) -> None:
    with _bank_world(in_bank=False) as world:
        result = await _run(handler, command_data)

    assert command_result_text(result) == "You must be at a bank to do that."
    assert world.boxes_opened_for == []  # nobody gets a box by typing a bank command on the street


@pytest.mark.asyncio
async def test_bank_reports_an_empty_box() -> None:
    with _bank_world():
        result = await _run(handle_bank_command)

    assert command_result_text(result) == "Your deposit box at Arkham Savings & Trust is empty."


@pytest.mark.asyncio
async def test_bank_lists_numbered_stacks_with_the_slot_count() -> None:
    with _bank_world(items=[_lamp(2), _coin(5)]):
        text = command_result_text(await _run(handle_bank_command))

    assert "(2/100)" in text
    assert "1. 2x Oil Lamp" in text
    assert "2. 5x coin" in text  # falls back to item_id when a stack has no name


@pytest.mark.asyncio
async def test_bank_shows_an_over_filled_box_honestly() -> None:
    """Flushed losses can push a box past capacity; the count must say so, not clamp."""
    stacks: list[dict[str, object]] = [
        {"item_id": f"item{n}", "item_name": f"Item {n}", "quantity": 1} for n in range(3)
    ]
    with _bank_world(items=stacks) as world:
        world.box["capacity_slots"] = 2
        text = command_result_text(await _run(handle_bank_command))

    assert "(3/2)" in text


@pytest.mark.asyncio
async def test_deposit_moves_the_item_into_the_players_own_box() -> None:
    item = _lamp(3)
    validated = ("lamp", "deposit box", None, MagicMock(name="container_service"), MagicMock(), item, 4)
    with (
        _bank_world() as world,
        patch(f"{MODULE}.validate_put_command_inputs", new=AsyncMock(return_value=validated)) as validate,
        patch(
            f"{MODULE}.transfer_item_to_container",
            new=AsyncMock(return_value={"success": True, "transfer_quantity": 2}),
        ) as transfer,
        patch(f"{MODULE}.remove_item_from_inventory") as remove,
        patch(f"{MODULE}.persist_player", new=AsyncMock(return_value=None)),
        patch(f"{MODULE}.emit_inventory_updated", new=AsyncMock()),
    ):
        result = await _run(handle_deposit_command, {"item": "lamp", "quantity": 2})

    assert command_result_text(result) == "The clerk files 2x Oil Lamp away in your deposit box."
    assert validate.await_args is not None
    assert validate.await_args.args[0]["container"] == "deposit box"  # the validators need a container name
    assert transfer.await_args is not None
    assert transfer.await_args.args[3] == world.box_id  # moved into this player's box, no other
    remove.assert_called_once_with(world.player, 4, 2)


@pytest.mark.asyncio
async def test_deposit_into_a_full_box_leaves_the_inventory_alone() -> None:
    validated = ("lamp", "deposit box", None, MagicMock(), MagicMock(), _lamp(), 0)
    with (
        _bank_world(),
        patch(f"{MODULE}.validate_put_command_inputs", new=AsyncMock(return_value=validated)),
        patch(f"{MODULE}.transfer_item_to_container", new=AsyncMock(return_value={"error": "Container is full"})),
        patch(f"{MODULE}.remove_item_from_inventory") as remove,
        patch(f"{MODULE}.persist_player", new=AsyncMock()) as persist,
    ):
        result = await _run(handle_deposit_command, {"item": "lamp"})

    assert command_result_text(result) == "Container is full"
    remove.assert_not_called()
    persist.assert_not_awaited()


@pytest.mark.asyncio
async def test_deposit_of_an_item_the_player_lacks_is_reported_by_the_validator() -> None:
    with (
        _bank_world(),
        patch(
            f"{MODULE}.validate_put_command_inputs",
            new=AsyncMock(return_value={"result": "You don't have 'sword' in your inventory."}),
        ),
        patch(f"{MODULE}.transfer_item_to_container", new=AsyncMock()) as transfer,
    ):
        result = await _run(handle_deposit_command, {"item": "sword"})

    assert command_result_text(result) == "You don't have 'sword' in your inventory."
    transfer.assert_not_awaited()


@pytest.mark.asyncio
async def test_withdraw_takes_the_named_stack_out_of_the_players_box() -> None:
    validated = ("lamp", "deposit box", 1, MagicMock(name="container_service"), MagicMock())
    with (
        _bank_world(items=[{**_coin(1), "item_name": "Coin"}, _lamp(3)]) as world,
        patch(f"{MODULE}.validate_get_command_inputs", new=AsyncMock(return_value=validated)),
        patch(
            f"{MODULE}.transfer_item_from_container",
            new=AsyncMock(return_value={"success": True, "transfer_quantity": 1, "item_display_name": "Oil Lamp"}),
        ) as transfer,
        patch(f"{MODULE}.emit_inventory_updated", new=AsyncMock()),
    ):
        result = await _run(handle_withdraw_command, {"item": "lamp", "quantity": 1})

    assert command_result_text(result) == "The clerk returns 1x Oil Lamp from your deposit box."
    assert transfer.await_args is not None
    assert transfer.await_args.args[3] == world.box_id
    assert transfer.await_args.args[4] == _lamp(3)  # the lamp stack, not the coin before it


@pytest.mark.asyncio
async def test_withdraw_of_something_not_in_the_box_says_so_and_moves_nothing() -> None:
    validated = ("sword", "deposit box", None, MagicMock(), MagicMock())
    with (
        _bank_world(items=[_lamp()]),
        patch(f"{MODULE}.validate_get_command_inputs", new=AsyncMock(return_value=validated)),
        patch(f"{MODULE}.transfer_item_from_container", new=AsyncMock()) as transfer,
    ):
        result = await _run(handle_withdraw_command, {"item": "sword"})

    assert command_result_text(result) == "You don't have 'sword' in your deposit box."
    transfer.assert_not_awaited()


@pytest.mark.asyncio
async def test_withdraw_surfaces_a_transfer_error() -> None:
    validated = ("lamp", "deposit box", None, MagicMock(), MagicMock())
    with (
        _bank_world(items=[_lamp()]),
        patch(f"{MODULE}.validate_get_command_inputs", new=AsyncMock(return_value=validated)),
        patch(
            f"{MODULE}.transfer_item_from_container",
            new=AsyncMock(return_value={"error": "Your inventory is full."}),
        ),
        patch(f"{MODULE}.emit_inventory_updated", new=AsyncMock()) as emit,
    ):
        result = await _run(handle_withdraw_command, {"item": "lamp"})

    assert command_result_text(result) == "Your inventory is full."
    emit.assert_not_awaited()
