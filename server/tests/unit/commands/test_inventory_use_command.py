"""Unit tests for the /use command handler (#870): consume one item, apply its effect."""

from __future__ import annotations

from collections.abc import Mapping
from types import SimpleNamespace
from typing import final
from unittest.mock import AsyncMock, patch
from uuid import UUID, uuid4

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands.inventory_use_command import handle_use_command
from server.game.items.item_effects import ITEM_EFFECTS, LUCIDITY_RECOVERY_TAG, ItemEffectResult, ItemUseContext
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.services.catatonia_state import CATATONIA_BLOCK_MESSAGE
from server.tests.fixtures.shared.player_registry import RegistryHarness, install_player_registry

TONIC_ID = "consumable.folk_tonic"
SWORD_ID = "weapon.sword"
OTHER_ID = "consumable.other"
OTHER_TAG = "component.other_effect"
MODULE = "server.commands.inventory_use_command"


@final
class FakePlayer:
    """The slice of Player the handler touches."""

    def __init__(self, inventory: list[dict[str, object]]) -> None:
        self.name = "Tester"
        self.player_id = uuid4()
        self.current_room_id = "room-1"
        self._inventory = inventory
        self._equipped: dict[str, object] = {}

    def get_inventory(self) -> list[dict[str, object]]:
        return [dict(stack) for stack in self._inventory]

    def set_inventory(self, inventory: list[dict[str, object]]) -> None:
        self._inventory = inventory

    def get_equipped_items(self) -> dict[str, object]:
        return dict(self._equipped)

    def set_equipped_items(self, equipped: Mapping[str, Mapping[str, object]]) -> None:
        self._equipped = dict(equipped)


def _stack(prototype_id: str, name: str, quantity: int = 1) -> dict[str, object]:
    return {
        "item_instance_id": str(uuid4()),
        "prototype_id": prototype_id,
        "item_id": prototype_id,
        "item_name": name,
        "slot_type": "inventory",
        "quantity": quantity,
    }


def _prototype(prototype_id: str, name: str, item_type: str, effect_components: list[str]) -> ItemPrototypeModel:
    return ItemPrototypeModel.model_validate(
        {
            "prototype_id": prototype_id,
            "name": name,
            "short_description": name.lower(),
            "long_description": f"A {name.lower()}.",
            "item_type": item_type,
            "weight": 1.0,
            "base_value": 1,
            "effect_components": effect_components,
        }
    )


@pytest.fixture
def request_obj() -> SimpleNamespace:
    registry = PrototypeRegistry(
        {
            TONIC_ID: _prototype(TONIC_ID, "Folk Tonic", "consumable", [LUCIDITY_RECOVERY_TAG]),
            SWORD_ID: _prototype(SWORD_ID, "Sword", "weapon", [LUCIDITY_RECOVERY_TAG]),
            "consumable.dud": _prototype("consumable.dud", "Dud", "consumable", ["component.durability"]),
            OTHER_ID: _prototype(OTHER_ID, "Other", "consumable", [OTHER_TAG]),
        },
        [],
    )
    return SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(prototype_registry=registry)))


@final
class EffectProbe:
    """Replaces the lucidity effect: records contexts and reports a scripted outcome."""

    def __init__(self, outcome: ItemEffectResult) -> None:
        self.outcome = outcome
        self.contexts: list[ItemUseContext] = []

    async def __call__(self, ctx: ItemUseContext) -> ItemEffectResult:
        self.contexts.append(ctx)
        return self.outcome


@pytest.fixture
def effect(monkeypatch: pytest.MonkeyPatch) -> EffectProbe:
    probe = EffectProbe(ItemEffectResult(ok=True, message="You swallow the folk tonic."))
    monkeypatch.setitem(ITEM_EFFECTS, LUCIDITY_RECOVERY_TAG, probe)
    return probe


async def _use(
    player: FakePlayer,
    request: SimpleNamespace,
    command_data: dict[str, object],
    monkeypatch: pytest.MonkeyPatch,
    *,
    fail_save: bool = False,
) -> tuple[dict[str, object], RegistryHarness, AsyncMock]:
    harness = install_player_registry(monkeypatch, player)
    if fail_save:
        harness.db.fail_commits = 1
        harness.db.commit_error = SQLAlchemyError("database unavailable")
    emit = AsyncMock()
    with (
        patch(f"{MODULE}.resolve_state_and_player", new=AsyncMock(return_value=("db", "cm", player, None))),
        patch(f"{MODULE}.emit_inventory_updated", new=emit),
    ):
        result = await handle_use_command(command_data, {"username": "tester"}, request, None, "Tester")
    return dict(result), harness, emit


def _quantities(stacks: list[dict[str, object]] | None) -> list[object]:
    return [stack["quantity"] for stack in stacks or []]


@pytest.mark.asyncio
async def test_use_decrements_a_stack_and_reports_to_player_and_room(
    request_obj: SimpleNamespace, effect: EffectProbe, monkeypatch: pytest.MonkeyPatch
) -> None:
    player = FakePlayer([_stack("misc.rock", "Rock"), _stack(TONIC_ID, "Folk Tonic", 2)])

    result, harness, emit = await _use(player, request_obj, {"search_term": "tonic"}, monkeypatch)

    assert result["result"] == "You swallow the folk tonic."
    assert result["room_message"] == "Tester drinks a folk tonic."
    assert [stack["quantity"] for stack in player.get_inventory()] == [1, 1]
    assert _quantities(harness.saved_carried()) == [1, 1]  # the decrement reached the inventory write
    emit.assert_awaited_once_with("cm", UUID(str(player.player_id)), player)
    [ctx] = effect.contexts
    assert (ctx.player_id, ctx.room_id, ctx.prototype.prototype_id) == (player.player_id, "room-1", TONIC_ID)


@pytest.mark.asyncio
async def test_use_by_index_removes_the_last_item_from_the_stack(
    request_obj: SimpleNamespace, effect: EffectProbe, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = effect
    player = FakePlayer([_stack(TONIC_ID, "Folk Tonic")])

    _result, harness, _emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert player.get_inventory() == []
    assert harness.saved_carried() == []


@pytest.mark.asyncio
async def test_a_refused_effect_keeps_the_item(
    request_obj: SimpleNamespace, effect: EffectProbe, monkeypatch: pytest.MonkeyPatch
) -> None:
    effect.outcome = ItemEffectResult(ok=False, message="You don't think you can stomach another tonic at this time.")
    player = FakePlayer([_stack(TONIC_ID, "Folk Tonic")])

    result, harness, emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert result == {"result": "You don't think you can stomach another tonic at this time."}
    assert [stack["quantity"] for stack in player.get_inventory()] == [1]
    assert harness.saved_carried() is None
    emit.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_failed_save_keeps_the_item_but_the_effect_stands(
    request_obj: SimpleNamespace, effect: EffectProbe, monkeypatch: pytest.MonkeyPatch
) -> None:
    _ = effect
    player = FakePlayer([_stack(TONIC_ID, "Folk Tonic", 2)])

    result, harness, emit = await _use(player, request_obj, {"index": 1}, monkeypatch, fail_save=True)

    assert result["result"] == "You swallow the folk tonic."
    view = harness.registry.peek(UUID(str(player.player_id)))
    assert view is not None and _quantities([dict(stack) for stack in view.inventory.carried]) == [2]  # rolled back
    emit.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("stack", "expected"),
    [
        (_stack(SWORD_ID, "Sword"), "You can't use that."),
        (_stack("missing.proto", "Mystery"), "You can't use that."),
        (_stack("consumable.dud", "Dud"), "Nothing happens."),
    ],
)
async def test_unusable_items_are_not_spent(
    request_obj: SimpleNamespace,
    effect: EffectProbe,
    stack: dict[str, object],
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    player = FakePlayer([stack])

    result, harness, _emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert result == {"result": expected}
    assert effect.contexts == []
    assert len(player.get_inventory()) == 1
    assert harness.saved_carried() is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("command_data", "expected"),
    [
        ({"index": 5}, "You do not have an item in that slot."),
        ({"search_term": "elixir"}, "You do not have an item matching 'elixir'."),
    ],
)
async def test_unresolvable_selectors_report_what_is_missing(
    request_obj: SimpleNamespace,
    effect: EffectProbe,
    command_data: dict[str, object],
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    player = FakePlayer([_stack(TONIC_ID, "Folk Tonic")])

    result, _harness, _emit = await _use(player, request_obj, command_data, monkeypatch)

    assert result == {"result": expected}
    assert effect.contexts == []


@pytest.mark.asyncio
async def test_player_resolution_errors_are_passed_through(request_obj: SimpleNamespace) -> None:
    with patch(
        f"{MODULE}.resolve_state_and_player",
        new=AsyncMock(return_value=("db", "cm", None, {"result": "Player information not found."})),
    ):
        result = await handle_use_command({"index": 1}, {"username": "tester"}, request_obj, None, "Tester")

    assert dict(result) == {"result": "Player information not found."}


# --- catatonia (#1148): the command gate lets `use` through; the item decides ------------------------------------


def _catatonic(monkeypatch: pytest.MonkeyPatch, *, catatonic: bool) -> AsyncMock:
    lookup = AsyncMock(return_value=catatonic)
    monkeypatch.setattr(f"{MODULE}.player_is_catatonic", lookup)
    return lookup


@pytest.mark.asyncio
async def test_a_catatonic_player_cannot_use_an_item_that_does_not_restore_lcd(
    request_obj: SimpleNamespace, monkeypatch: pytest.MonkeyPatch
) -> None:
    other = EffectProbe(ItemEffectResult(ok=True, message="You feel strange."))
    monkeypatch.setitem(ITEM_EFFECTS, OTHER_TAG, other)
    _ = _catatonic(monkeypatch, catatonic=True)
    player = FakePlayer([_stack(OTHER_ID, "Other")])

    result, harness, _emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert result == {"result": CATATONIA_BLOCK_MESSAGE}
    assert other.contexts == []
    assert [stack["quantity"] for stack in player.get_inventory()] == [1]
    assert harness.saved_carried() is None


@pytest.mark.asyncio
async def test_a_catatonic_player_can_use_an_item_that_restores_lcd(
    request_obj: SimpleNamespace, effect: EffectProbe, monkeypatch: pytest.MonkeyPatch
) -> None:
    lookup = _catatonic(monkeypatch, catatonic=True)
    player = FakePlayer([_stack(TONIC_ID, "Folk Tonic")])

    result, _harness, _emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert result["result"] == "You swallow the folk tonic."
    assert len(effect.contexts) == 1
    lookup.assert_not_awaited()  # an LCD item never needs the catatonia lookup


@pytest.mark.asyncio
async def test_an_item_that_does_not_restore_lcd_works_for_a_player_who_is_not_catatonic(
    request_obj: SimpleNamespace, monkeypatch: pytest.MonkeyPatch
) -> None:
    other = EffectProbe(ItemEffectResult(ok=True, message="You feel strange."))
    monkeypatch.setitem(ITEM_EFFECTS, OTHER_TAG, other)
    _ = _catatonic(monkeypatch, catatonic=False)
    player = FakePlayer([_stack(OTHER_ID, "Other")])

    result, _harness, _emit = await _use(player, request_obj, {"index": 1}, monkeypatch)

    assert result["result"] == "You feel strange."
    assert player.get_inventory() == []
