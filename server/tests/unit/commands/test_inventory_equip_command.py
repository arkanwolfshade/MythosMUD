"""Unit tests for inventory equip command internals (the swap commits through the player registry, ADR-029 4a)."""

from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Mapping
from contextlib import asynccontextmanager
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands.inventory_equip_command import (
    EquipCommandInventoryStep,
    EquipCommandRuntime,
    EquipCommandWork,
    _equip_run_mutation,
    _equip_success_payload,
    _equip_target_slot_or_error,
    _equip_try_inventory_swap,
    handle_equip_command,
)
from server.models.player import Player
from server.services.equipment_service import SlotValidationError
from server.tests.fixtures.shared.player_registry import RegistryHarness, install_player_registry

from .inventory_commands_test_support import command_result_text

SWORD_INSTANCE = str(uuid.uuid4())
EQUIP_SWORD: dict[str, object] = {"index": 1, "target_slot": "main_hand"}


def _sword(slot_type: str) -> dict[str, object]:
    return {
        "item_instance_id": SWORD_INSTANCE,
        "prototype_id": "sword_proto",
        "item_id": "sword_001",
        "item_name": "Sword",
        "slot_type": slot_type,
        "quantity": 1,
    }


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


def _guard(should_apply: bool) -> MagicMock:
    """An inventory service whose async mutation guard decides ``should_apply``."""

    @asynccontextmanager
    async def begin(_player_id: object, _token: object) -> AsyncGenerator[MagicMock]:
        decision = MagicMock()
        decision.should_apply = should_apply
        yield decision

    service = MagicMock()
    service.begin_mutation = begin
    return service


def _registry_runtime(
    monkeypatch: pytest.MonkeyPatch, equip: MagicMock, *, should_apply: bool = True
) -> tuple[EquipCommandRuntime, RegistryHarness]:
    """A runtime whose equipment service swaps with ``equip``, over a real registry."""
    runtime = _sample_runtime(_stateful_player([_sword("inventory")]))
    runtime.inventory_service = _guard(should_apply)
    runtime.equipment_service = MagicMock(equip_from_inventory=equip)
    return runtime, install_player_registry(monkeypatch, runtime.player)


def _equips_the_sword() -> MagicMock:
    return MagicMock(return_value=([], {"main_hand": _sword("main_hand")}))


@pytest.mark.asyncio
async def test_equip_run_mutation_suppressed(monkeypatch: pytest.MonkeyPatch) -> None:
    runtime, harness = _registry_runtime(monkeypatch, _equips_the_sword(), should_apply=False)
    result = await _equip_run_mutation(MagicMock(), EQUIP_SWORD, runtime)
    assert isinstance(result, Mapping) and "already being processed" in command_result_text(result)
    assert harness.saved_equipped() is None


@pytest.mark.asyncio
async def test_equip_run_mutation_commits_the_swap(monkeypatch: pytest.MonkeyPatch) -> None:
    runtime, harness = _registry_runtime(monkeypatch, _equips_the_sword())

    result = await _equip_run_mutation(MagicMock(), EQUIP_SWORD, runtime)

    assert isinstance(result, EquipCommandWork) and result.target_slot == "main_hand"
    assert harness.saved_carried() == []
    assert (harness.saved_equipped() or {})["main_hand"] == _sword("main_hand")


@pytest.mark.asyncio
async def test_equip_run_mutation_swap_error_writes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    runtime, harness = _registry_runtime(monkeypatch, MagicMock(side_effect=SlotValidationError("nope")))
    result = await _equip_run_mutation(MagicMock(), EQUIP_SWORD, runtime)
    assert isinstance(result, Mapping) and "nope" in command_result_text(result)
    assert harness.saved_equipped() is None


@pytest.mark.asyncio
async def test_equip_run_mutation_failed_save_rolls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    runtime, harness = _registry_runtime(monkeypatch, _equips_the_sword())
    harness.db.fail_commits = 1
    harness.db.commit_error = SQLAlchemyError("database unavailable")

    result = await _equip_run_mutation(MagicMock(), EQUIP_SWORD, runtime)

    assert isinstance(result, Mapping)
    assert command_result_text(result) == "An error occurred while saving your inventory."
    view = harness.registry.peek(uuid.UUID(str(runtime.player.player_id)))
    assert view is not None and view.inventory.equipped == {}  # rolled back: still carried


@pytest.mark.asyncio
async def test_equip_success_payload() -> None:
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player_id: uuid.UUID = uuid.uuid4()
    player.player_id = player_id
    player.get_equipped_items.return_value = {"main_hand": {"item_name": "Sword", "item_id": "sword"}}
    connection_manager = MagicMock()
    with (
        patch(
            "server.commands.inventory_equip_command.find_equipped_item_after_equip",
            return_value=("main_hand", {"item_name": "Sword", "item_id": "sword"}),
        ),
        patch("server.commands.inventory_equip_command.handle_wearable_container_on_equip", new=AsyncMock()),
        patch("server.commands.inventory_equip_command.build_and_broadcast_inventory_event", new=AsyncMock()),
        patch("server.commands.inventory_equip_command.emit_inventory_updated", new_callable=AsyncMock) as mock_emit,
    ):
        result = await _equip_success_payload(
            MagicMock(), connection_manager, player, "room-1", "main_hand", {"item_id": "sword"}, None
        )
    assert "You equip Sword" in command_result_text(result)
    mock_emit.assert_awaited_once_with(connection_manager, player_id, player)


@pytest.mark.asyncio
async def test_handle_equip_command_build_error() -> None:
    with patch(
        "server.commands.inventory_equip_command._equip_build_runtime",
        new=AsyncMock(return_value={"result": "no player"}),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert command_result_text(result) == "no player"


@pytest.mark.asyncio
async def test_handle_equip_command_mutation_error() -> None:
    with (
        patch(
            "server.commands.inventory_equip_command._equip_build_runtime",
            new=AsyncMock(return_value=_sample_runtime(_stateful_player([]))),
        ),
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
        patch(
            "server.commands.inventory_equip_command._equip_build_runtime",
            new=AsyncMock(return_value=_sample_runtime(work.player)),
        ),
        patch("server.commands.inventory_equip_command._equip_run_mutation", new=AsyncMock(return_value=work)),
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
        patch(
            "server.commands.inventory_equip_command._equip_build_runtime",
            new=AsyncMock(return_value=_sample_runtime(work.player)),
        ),
        patch("server.commands.inventory_equip_command._equip_run_mutation", new=AsyncMock(return_value=work)),
    ):
        result = await handle_equip_command({}, {}, MagicMock(), None, "Alice")
    assert "invalid" in command_result_text(result)


def test_equip_target_slot_none_stack() -> None:
    slot, err = _equip_target_slot_or_error(MagicMock(), None, None)
    assert slot is None
    assert err is None


def _stateful_player(inventory: list[dict[str, object]]) -> MagicMock:
    """A Player mock whose setters change what its getters return, like the real Player."""
    player = MagicMock(spec=Player)
    player.name = "Alice"
    player.player_id = uuid.uuid4()
    player.current_room_id = "room-1"
    get_inventory = MagicMock(return_value=inventory)
    get_equipped = MagicMock(return_value={})

    def store_inventory(rows: object) -> None:
        get_inventory.return_value = [dict(stack) for stack in cast(list[Mapping[str, object]], rows)]

    def store_equipped(slots: object) -> None:
        get_equipped.return_value = dict(cast(Mapping[str, object], slots))

    player.get_inventory = get_inventory
    player.get_equipped_items = get_equipped
    player.set_inventory = MagicMock(side_effect=store_inventory)
    player.set_equipped_items = MagicMock(side_effect=store_equipped)
    return player


def _sample_runtime(player: Player) -> EquipCommandRuntime:
    return EquipCommandRuntime(
        persistence=MagicMock(),
        connection_manager=MagicMock(),
        player=player,
        room_id="room-1",
        inventory_service=MagicMock(),
        equipment_service=MagicMock(),
        mutation_token=None,
        command_data={"index": 1},
    )


def _sample_work() -> EquipCommandWork:
    inv_step = EquipCommandInventoryStep(
        inventory=[{"item_id": "sword", "slot_type": "inventory"}],
        resolved_index_zero=0,
        selected_stack={"item_id": "sword", "slot_type": "inventory"},
        target_slot="main_hand",
    )
    return EquipCommandWork(runtime=_sample_runtime(_stateful_player([])), inv_step=inv_step)
