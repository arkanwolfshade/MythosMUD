"""Unit tests for change_inventory: a command's inventory read-modify-write as one registry unit (ADR-029 4a)."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast

import pytest

from server.commands.inventory_command_contracts import CommandResponse
from server.commands.inventory_command_helpers import change_inventory
from server.models.player import Player
from server.tests.fixtures.shared.player_registry import RegistryHarness, install_player_registry

SLING: dict[str, object] = {
    "item_instance_id": str(uuid.uuid4()),
    "prototype_id": "sling_proto",
    "item_id": "sling",
    "item_name": "Sling",
    "slot_type": "inventory",
    "quantity": 1,
}


class StubPlayer:
    """The slice of Player change_inventory touches: an id, a name, and inventory getters and setters."""

    def __init__(self, carried: list[dict[str, object]]) -> None:
        self.player_id: str = str(uuid.uuid4())
        self.name: str = "Tester"
        self.carried: list[dict[str, object]] = carried
        self.equipped: dict[str, object] = {}

    def get_inventory(self) -> list[dict[str, object]]:
        return [dict(stack) for stack in self.carried]

    def set_inventory(self, inventory: list[Mapping[str, object]]) -> None:
        self.carried = [dict(stack) for stack in inventory]

    def get_equipped_items(self) -> dict[str, object]:
        return dict(self.equipped)

    def set_equipped_items(self, equipped: Mapping[str, Mapping[str, object]]) -> None:
        self.equipped = dict(equipped)


def _as_player(stub: StubPlayer) -> Player:
    return cast(Player, cast(object, stub))


async def _loaded(monkeypatch: pytest.MonkeyPatch, stub: StubPlayer) -> RegistryHarness:
    """A registry that has already loaded ``stub``'s current inventory."""
    harness = install_player_registry(monkeypatch, stub)
    _ = await harness.registry.get(uuid.UUID(stub.player_id))
    return harness


@pytest.mark.asyncio
async def test_the_change_sees_the_live_inventory_not_the_copy_the_command_loaded(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stub = StubPlayer([SLING])
    harness = await _loaded(monkeypatch, stub)
    stub.carried = []  # the command's copy is stale: it was loaded before another change
    seen: list[list[dict[str, object]]] = []

    async def change() -> CommandResponse | None:
        seen.append(stub.get_inventory())
        stub.set_inventory([{**SLING, "quantity": 2}])
        return None

    assert await change_inventory(_as_player(stub), change) is None
    assert seen == [[SLING]]
    assert harness.saved_carried() == [{**SLING, "quantity": 2}]


@pytest.mark.asyncio
async def test_a_reply_from_the_change_aborts_without_writing(monkeypatch: pytest.MonkeyPatch) -> None:
    stub = StubPlayer([SLING])
    harness = install_player_registry(monkeypatch, stub)

    async def change() -> CommandResponse | None:
        stub.set_inventory([])
        return {"result": "You cannot do that."}

    assert await change_inventory(_as_player(stub), change) == {"result": "You cannot do that."}
    assert harness.saved_carried() is None
    view = harness.registry.peek(uuid.UUID(stub.player_id))
    assert view is not None and list(view.inventory.carried) == [SLING]


@pytest.mark.asyncio
async def test_an_invalid_inventory_is_refused_and_nothing_is_written(monkeypatch: pytest.MonkeyPatch) -> None:
    stub = StubPlayer([SLING])
    harness = install_player_registry(monkeypatch, stub)

    async def change() -> CommandResponse | None:
        stub.set_inventory([{"item_name": "no ids or quantity"}])
        return None

    reply = await change_inventory(_as_player(stub), change)

    assert reply == {"result": "Inventory data rejected by schema validation."}
    assert harness.saved_carried() is None
    view = harness.registry.peek(uuid.UUID(stub.player_id))
    assert view is not None and list(view.inventory.carried) == [SLING]


@pytest.mark.asyncio
async def test_a_player_the_registry_cannot_load_gets_an_error_reply(monkeypatch: pytest.MonkeyPatch) -> None:
    stub = StubPlayer([SLING])
    harness = install_player_registry(monkeypatch, stub)

    async def no_player(_session: object, _player_id: uuid.UUID) -> None:
        return None

    monkeypatch.setattr(harness.registry, "_loader", no_player)

    async def change() -> CommandResponse | None:
        raise AssertionError("the change must not run without a player")

    reply = await change_inventory(_as_player(stub), change)

    assert reply is not None and "error occurred while saving your inventory" in str(reply.get("result"))
