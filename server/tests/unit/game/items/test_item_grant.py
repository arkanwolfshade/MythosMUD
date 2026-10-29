"""
Unit tests for ItemGranter: giving a player a new item through the player registry (ADR-029 step 4c-i).

A real ItemFactory over a small prototype store, and a real PlayerRegistry over the in-memory FakeDatabase, so each
test reads back what was committed.
"""

from __future__ import annotations

import json
import uuid
from types import SimpleNamespace
from typing import cast

import pytest

from server.game.items.item_factory import ItemFactory, ItemFactoryError
from server.game.items.item_grant import ItemGranter
from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from server.game.player_registry import DbSession, PlayerAggregate, PlayerNotFoundError, PlayerRegistry
from server.services.inventory_service import InventoryCapacityError, InventoryService
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

LANTERN = "pack_victorian.light.lantern"


class _Prototypes:
    """The PrototypeRegistry.get the factory calls."""

    def get(self, prototype_id: str) -> SimpleNamespace:
        if prototype_id != LANTERN:
            raise PrototypeRegistryError(f"unknown prototype {prototype_id}")
        return SimpleNamespace(
            prototype_id=LANTERN, name="Hurricane Lantern", wear_slots=["main_hand"], metadata={}, flags=[]
        )


@pytest.fixture(autouse=True)
def _no_components(monkeypatch: pytest.MonkeyPatch) -> None:
    def no_components(*_args: object, **_kwargs: object) -> None:
        return None

    monkeypatch.setattr("server.game.items.item_factory.initialize_components", no_components)


def _granter(
    carried: list[dict[str, object]] | None = None, *, with_factory: bool = True, max_slots: int = 20
) -> tuple[ItemGranter, FakeDatabase, uuid.UUID]:
    """``carried=None`` means there is no such player."""
    db = FakeDatabase()
    player_id = uuid.uuid4()

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate | None:
        return None if carried is None else aggregate(raw_row(pid, inventory=json.dumps(carried)))

    factory = ItemFactory(cast(PrototypeRegistry, cast(object, _Prototypes())))
    granter = ItemGranter(
        PlayerRegistry(db.session, loader=load),
        lambda: factory if with_factory else None,
        InventoryService(max_slots=max_slots),
    )
    return granter, db, player_id


def _committed(db: FakeDatabase) -> list[dict[str, object]]:
    write = db.last_inventory_write()
    assert write is not None, "nothing was committed"
    return cast(list[dict[str, object]], json.loads(str(write["inventory_json"])))


async def test_grant_adds_a_factory_built_item_carried_in_general_inventory() -> None:
    granter, db, player_id = _granter([])

    await granter.grant(player_id, LANTERN, 2, origin={"source": "quest_reward", "quest_id": "q1"})

    [stack] = _committed(db)
    assert stack["prototype_id"] == LANTERN
    assert stack["item_name"] == "Hurricane Lantern"  # the prototype's name, not its id
    assert stack["quantity"] == 2
    assert stack["item_instance_id"]  # a real instance
    # Carried, not equipped: equip then infers main_hand from the prototype (wear_slots).
    assert stack["slot_type"] == "inventory"
    assert stack["origin"] == {"source": "quest_reward", "quest_id": "q1"}
    assert db.commits == 1


async def test_grant_keeps_what_the_player_already_carries() -> None:
    sling: dict[str, object] = {"item_id": "sling", "item_name": "Sling", "slot_type": "inventory", "quantity": 1}
    granter, db, player_id = _granter([sling])

    await granter.grant(player_id, LANTERN, origin={"source": "spell_create_object"})

    assert [stack["item_name"] for stack in _committed(db)] == ["Sling", "Hurricane Lantern"]


async def test_a_full_inventory_writes_nothing() -> None:
    sling: dict[str, object] = {"item_id": "sling", "item_name": "Sling", "slot_type": "inventory", "quantity": 1}
    granter, db, player_id = _granter([sling], max_slots=1)

    assert await granter.has_free_slot(player_id) is False
    with pytest.raises(InventoryCapacityError):
        await granter.grant(player_id, LANTERN, origin={"source": "spell_create_object"})

    assert db.executed == []


async def test_an_unknown_prototype_or_no_item_system_writes_nothing() -> None:
    granter, db, player_id = _granter([])
    with pytest.raises(ItemFactoryError, match="not found"):
        await granter.grant(player_id, "no.such.thing", origin={"source": "spell_create_object"})

    no_factory, no_factory_db, other_id = _granter([], with_factory=False)
    with pytest.raises(ItemFactoryError, match="not available"):
        await no_factory.grant(other_id, LANTERN, origin={"source": "spell_create_object"})

    assert db.executed == [] and no_factory_db.executed == []


async def test_no_such_player() -> None:
    granter, db, player_id = _granter(None)

    assert await granter.has_free_slot(player_id) is False
    with pytest.raises(PlayerNotFoundError):
        await granter.grant(player_id, LANTERN, origin={"source": "spell_create_object"})
    assert db.executed == []
