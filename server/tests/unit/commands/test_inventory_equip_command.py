"""Unit tests for inventory equip command internals."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_equip_command import (
    EquipCommandInventoryStep,
    EquipCommandRuntime,
    EquipCommandWork,
    _equip_inventory_rollback_snapshot,
    _equip_persist_or_rollback,
    _equip_run_mutation,
    _equip_success_payload,
    _equip_target_slot_or_error,
    _equip_try_inventory_swap,
    handle_equip_command,
)
from server.models.player import Player
from server.services.equipment_service import SlotValidationError

from .inventory_commands_test_support import command_result_text


def test_equip_target_slot_explicit() -> None:
    slot, err = _equip_target_slot_or_error(MagicMock(), {"item_id": "x"}, "main_hand")
    assert slot == "main_hand"
    assert err is None


def test_equip_target_slot_inferred() -> None:
    request = MagicMock()
    stack = {"item_id": "sword", "slot_type": "inventory"}
    with patch(
        "server.commands.inventory_equip_command.infer_equip_slot_from_prototype",
        return_value="main_hand",
    ):
        slot, err = _equip_target_slot_or_error(request, stack, None)
    assert slot == "main_hand"
    assert err is None


def test_equip_target_slot_needs_specification() -> None:
    stack = {"item_id": "misc", "slot_type": "inventory"}
    with patch("server.commands.inventory_equip_command.infer_equip_slot_from_prototype", return_value=None):
        slot, err = _equip_target_slot_or_error(MagicMock(), stack, None)
    assert slot is None
    assert err is not None
    assert "Specify which slot" in command_result_text(err)


def test_equip_inventory_rollback_snapshot() -> None:
    player = MagicMock(spec=Player)
    player.get_inventory.return_value = [{"item_id": "a"}]
    player.get_equipped_items.return_value = {"ring": {"item_id": "r"}}
    inv, eq = _equip_inventory_rollback_snapshot(player)
    assert inv == [{"item_id": "a"}]
    assert "ring" in eq


@pytest.mark.asyncio
async def test_equip_persist_or_rollback_success() -> None:
    player = MagicMock(spec=Player)
    with patch("server.commands.inventory_equip_command.persist_player", new=AsyncMock(return_value=None)):
        result = await _equip_persist_or_rollback(
            player=player, persistence=MagicMock(), previous_inventory=[], previous_equipped={}
        )
    assert result is None


@pytest.mark.asyncio
async def test_equip_persist_or_rollback_failure() -> None:
    player = MagicMock(spec=Player)
    err = {"result": "save failed"}
    with patch("server.commands.inventory_equip_command.persist_player", new=AsyncMock(return_value=err)):
        result = await _equip_persist_or_rollback(
            player=player, persistence=MagicMock(), previous_inventory=[], previous_equipped={}
        )
    assert result == err
    player.set_inventory.assert_called_once()
    player.set_equipped_items.assert_called_once()


def test_equip_try_inventory_swap_success() -> None:
    work = _sample_work()
    work.equipment_service.equip_from_inventory.return_value = ([], {"main_hand": {"item_name": "Sword"}})
    result = _equip_try_inventory_swap(work)
    assert isinstance(result, tuple)


def test_equip_try_inventory_swap_rejected() -> None:
    work = _sample_work()
    work.equipment_service.equip_from_inventory.side_effect = SlotValidationError("bad slot")
    result = _equip_try_inventory_swap(work)
    assert isinstance(result, dict)
    assert "bad slot" in command_result_text(result)


@pytest.mark.asyncio
async def test_equip_run_mutation_suppressed() -> None:
    work = _sample_work()
    decision = MagicMock()
    decision.should_apply = False
    work.inventory_service.begin_mutation.return_value.__enter__ = MagicMock(return_value=decision)
    work.inventory_service.begin_mutation.return_value.__exit__ = MagicMock(return_value=False)
    result = await _equip_run_mutation(work)
    assert "already being processed" in command_result_text(result)


@pytest.mark.asyncio
async def test_equip_run_mutation_success() -> None:
    work = _sample_work()
    decision = MagicMock()
    decision.should_apply = True
    work.equipment_service.equip_from_inventory.return_value = (
        [{"item_id": "coin"}],
        {"main_hand": {"item_id": "sword", "item_name": "Sword"}},
    )
    ctx = MagicMock()
    ctx.__enter__ = MagicMock(return_value=decision)
    ctx.__exit__ = MagicMock(return_value=False)
    work.inventory_service.begin_mutation.return_value = ctx
    with (
        patch("server.commands.inventory_equip_command.persist_player", new=AsyncMock(return_value=None)),
        patch("server.commands.inventory_equip_command.normalize_inventory_slots"),
        patch("server.commands.inventory_equip_command.normalize_equipped_items", return_value={}),
    ):
        result = await _equip_run_mutation(work)
    assert result is None
    work.player.set_inventory.assert_called_once()


@pytest.mark.asyncio
async def test_equip_success_payload() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player.player_id = uuid.uuid4()
    player.get_equipped_items.return_value = {"main_hand": {"item_name": "Sword", "item_id": "sword"}}
    with (
        patch(
            "server.commands.inventory_equip_command.find_equipped_item_after_equip",
            return_value=("main_hand", {"item_name": "Sword", "item_id": "sword"}),
        ),
        patch("server.commands.inventory_equip_command.handle_wearable_container_on_equip", new=AsyncMock()),
        patch("server.commands.inventory_equip_command.build_and_broadcast_inventory_event", new=AsyncMock()),
    ):
        result = await _equip_success_payload(
            MagicMock(), MagicMock(), player, "room-1", "main_hand", {"item_id": "sword"}, None
        )
    assert "You equip Sword" in command_result_text(result)


@pytest.mark.asyncio
async def test_handle_equip_command_build_error() -> None:
    with patch(
        "server.commands.inventory_equip_command._equip_build_work",
        new=AsyncMock(return_value={"result": "no player"}),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert command_result_text(result) == "no player"


@pytest.mark.asyncio
async def test_handle_equip_command_mutation_error() -> None:
    work = _sample_work()
    with (
        patch("server.commands.inventory_equip_command._equip_build_work", new=AsyncMock(return_value=work)),
        patch(
            "server.commands.inventory_equip_command._equip_run_mutation",
            new=AsyncMock(return_value={"result": "blocked"}),
        ),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert command_result_text(result) == "blocked"


@pytest.mark.asyncio
async def test_handle_equip_command_success() -> None:
    work = _sample_work()
    with (
        patch("server.commands.inventory_equip_command._equip_build_work", new=AsyncMock(return_value=work)),
        patch("server.commands.inventory_equip_command._equip_run_mutation", new=AsyncMock(return_value=None)),
        patch(
            "server.commands.inventory_equip_command._equip_success_payload",
            new=AsyncMock(return_value={"result": "You equip Sword."}),
        ),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert "You equip Sword" in command_result_text(result)


@pytest.mark.asyncio
async def test_handle_equip_command_invalid_selected_stack() -> None:
    work = _sample_work()
    work.selected_stack = None
    with (
        patch("server.commands.inventory_equip_command._equip_build_work", new=AsyncMock(return_value=work)),
        patch("server.commands.inventory_equip_command._equip_run_mutation", new=AsyncMock(return_value=None)),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert "invalid" in command_result_text(result)


@pytest.mark.asyncio
async def test_equip_run_mutation_swap_error() -> None:
    work = _sample_work()
    decision = MagicMock()
    decision.should_apply = True
    work.equipment_service.equip_from_inventory.side_effect = SlotValidationError("nope")
    ctx = MagicMock()
    ctx.__enter__ = MagicMock(return_value=decision)
    ctx.__exit__ = MagicMock(return_value=False)
    work.inventory_service.begin_mutation.return_value = ctx
    result = await _equip_run_mutation(work)
    assert "nope" in command_result_text(result)


def test_equip_target_slot_none_stack() -> None:
    slot, err = _equip_target_slot_or_error(MagicMock(), None, None)
    assert slot is None
    assert err is None


def _sample_work() -> EquipCommandWork:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player.player_id = uuid.uuid4()
    player.get_equipped_items.return_value = {}
    player.get_inventory.return_value = []
    equipment_service = MagicMock()
    inventory_service = MagicMock()
    runtime = EquipCommandRuntime(
        persistence=MagicMock(),
        connection_manager=MagicMock(),
        player=player,
        room_id="room-1",
        inventory_service=inventory_service,
        equipment_service=equipment_service,
        mutation_token=None,
        command_data={"index": 1},
    )
    inv_step = EquipCommandInventoryStep(
        inventory=[{"item_id": "sword", "slot_type": "inventory"}],
        resolved_index_zero=0,
        selected_stack={"item_id": "sword", "slot_type": "inventory"},
        target_slot="main_hand",
        previous_inventory=[],
        previous_equipped={},
    )
    return EquipCommandWork(runtime=runtime, inv_step=inv_step)
