"""
ContainerService transfers as player-registry units of work (ADR-029 step 4b).

A real ContainerService and a real PlayerRegistry over the in-memory FakeDatabase: the player comes from the registry
(never from persistence), and the container write lands in the same transaction as the player's inventory write. The
container rows live in a small fake store; the patched container writer records what each transfer committed.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import cast

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import ActionRejectedError, ValidationError
from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry
from server.services.container_service import (
    ContainerCapacityError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
)
from server.services.inventory_service import InventoryService, InventoryStack
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

PID = uuid.uuid4()
CID = uuid.uuid4()
SLING: dict[str, object] = {"item_id": "sling", "item_name": "Sling", "slot_type": "backpack", "quantity": 1}


def _stack(item_id: str, quantity: int = 1) -> InventoryStack:
    return {
        "item_instance_id": f"{item_id}-1",
        "prototype_id": item_id,
        "item_id": item_id,
        "item_name": item_id.title(),
        "slot_type": "backpack",
        "quantity": quantity,
    }


@dataclass
class _Store:
    """The container rows persistence.get_container reads, updated by the (patched) transactional writer."""

    rows: dict[uuid.UUID, dict[str, object]] = field(default_factory=dict)

    async def get_container(self, container_id: uuid.UUID) -> dict[str, object] | None:
        row = self.rows.get(container_id)
        return dict(row) if row is not None else None

    def items(self, container_id: uuid.UUID = CID) -> list[dict[str, object]]:
        return cast(list[dict[str, object]], self.rows[container_id]["items_json"])


@dataclass
class _World:
    service: ContainerService
    registry: PlayerRegistry
    db: FakeDatabase
    store: _Store
    token: str

    def committed_carried(self) -> list[dict[str, object]]:
        write = self.db.last_inventory_write()
        assert write is not None, "no inventory write"
        return cast(list[dict[str, object]], json.loads(str(write["inventory_json"])))


def _world(
    monkeypatch: pytest.MonkeyPatch,
    *,
    carried: Sequence[Mapping[str, object]],
    container_items: Sequence[InventoryStack] = (),
    capacity: int = 5,
    db: FakeDatabase | None = None,
    max_slots: int = 20,
    player_exists: bool = True,
) -> _World:
    database = db or FakeDatabase()
    store = _Store(
        {
            CID: {
                "container_id": str(CID),
                "source_type": "environment",
                "capacity_slots": capacity,
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "lock_state": "unlocked",
                "items_json": [dict(item) for item in container_items],
                "metadata_json": {},
            }
        }
    )

    async def load(_session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        return aggregate(raw_row(player_id, inventory=json.dumps(list(carried)))) if player_exists else None

    async def write_items(session: object, container_id: uuid.UUID, items_json: Sequence[Mapping[str, object]]) -> None:
        _ = await cast(DbSession, session).execute("write_container_items", {"container_id": container_id})
        store.rows[container_id]["items_json"] = [dict(item) for item in items_json]

    monkeypatch.setattr("server.services.container_service_transfer_to.write_container_items_async", write_items)
    registry = PlayerRegistry(database.session, loader=load)
    service = ContainerService(
        persistence=cast(AsyncPersistenceLayer, cast(object, store)),
        inventory_service=InventoryService(max_slots=max_slots),
    )
    token = service.register_open_session(CID, PID)
    return _World(service, registry, database, store, token)


def _ref(item_id: str) -> InventoryStack:
    """What the GUI sends: only the stack's identity."""
    return cast(InventoryStack, cast(object, {"item_id": item_id, "item_instance_id": f"{item_id}-1"}))


def _names(stacks: Sequence[Mapping[str, object]]) -> list[tuple[object, object]]:
    return [(stack["item_id"], stack["quantity"]) for stack in stacks]


# ---- put (player -> container) ----


async def test_put_moves_the_stack_out_of_the_player_and_into_the_container_in_one_commit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    world = _world(monkeypatch, carried=[SLING, _stack("torch", 3)])

    result = await world.service.transfer_to_container(CID, PID, world.token, _ref("torch"), 2, registry=world.registry)

    assert result["quantity"] == 2
    assert _names(world.committed_carried()) == [("sling", 1), ("torch", 1)]
    assert _names(world.store.items()) == [("torch", 2)]
    assert world.db.commits == 1
    assert world.db.executed[-1] == {"container_id": CID}  # the container write is in the same transaction
    assert _names(cast(list[dict[str, object]], result["player_inventory"])) == [("sling", 1), ("torch", 1)]
    assert result["player_equipped"] == {}  # what the REST endpoint pushes to the client, with the carried stacks


async def test_put_moves_the_players_own_copy_not_what_the_caller_sent(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[_stack("torch", 3)])
    forged = {**_stack("torch", 99), "item_name": "Excalibur"}

    _ = await world.service.transfer_to_container(
        CID, PID, world.token, cast(InventoryStack, cast(object, forged)), None, registry=world.registry
    )

    assert world.store.items()[0]["item_name"] == "Torch"
    assert world.store.items()[0]["quantity"] == 3


async def test_put_never_moves_more_than_the_player_holds(monkeypatch: pytest.MonkeyPatch) -> None:
    """``remove_item_from_inventory`` used to pop a 3-stack while the container got the 5 asked for."""
    world = _world(monkeypatch, carried=[SLING, _stack("torch", 3)])

    result = await world.service.transfer_to_container(
        CID, PID, world.token, _stack("torch"), 5, registry=world.registry
    )

    assert result["quantity"] == 3
    assert _names(world.committed_carried()) == [("sling", 1)]
    assert _names(world.store.items()) == [("torch", 3)]


async def test_put_of_an_item_the_player_does_not_hold_changes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING])

    with pytest.raises(ActionRejectedError, match="don't have that item"):  # routine: logged at debug
        _ = await world.service.transfer_to_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )

    assert world.db.executed == []
    assert world.store.items() == []


async def test_put_into_a_full_container_changes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[_stack("torch")], container_items=[_stack("rope")], capacity=1)

    with pytest.raises(ContainerCapacityError):
        _ = await world.service.transfer_to_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )

    assert world.db.executed == []


# ---- get (container -> player) ----


async def test_get_keeps_everything_else_the_player_carries(monkeypatch: pytest.MonkeyPatch) -> None:
    """The ORM Player's inventory is a JSON string, so the old code built the new inventory from [] and saved the
    player holding only what they had just taken."""
    world = _world(monkeypatch, carried=[SLING], container_items=[_stack("torch", 3)])

    result = await world.service.transfer_from_container(
        CID, PID, world.token, _ref("torch"), None, registry=world.registry
    )

    assert result["quantity"] == 3
    assert _names(world.committed_carried()) == [("sling", 1), ("torch", 3)]
    assert world.store.items() == []
    assert world.db.commits == 1


async def test_a_stack_taken_from_a_container_is_carried_in_general_inventory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Like a floor pickup: the container's "backpack" label made `equip` put a sling in a "backpack" slot."""
    world = _world(monkeypatch, carried=[], container_items=[_stack("torch"), _stack("rope")])
    assert world.store.items()[0]["slot_type"] == "backpack"

    _ = await world.service.transfer_from_container(
        CID, PID, world.token, _ref("torch"), None, registry=world.registry
    )
    assert [stack["slot_type"] for stack in world.committed_carried()] == ["inventory"]

    _ = await world.service.loot_all(CID, PID, world.token, registry=world.registry)
    assert [stack["slot_type"] for stack in world.committed_carried()] == ["inventory", "inventory"]


async def test_get_part_of_a_stack_leaves_the_rest(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[], container_items=[_stack("torch", 3)])

    _ = await world.service.transfer_from_container(CID, PID, world.token, _stack("torch"), 1, registry=world.registry)

    assert _names(world.committed_carried()) == [("torch", 1)]
    assert _names(world.store.items()) == [("torch", 2)]


async def test_get_into_a_full_inventory_changes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING], container_items=[_stack("torch")], max_slots=1)

    with pytest.raises(ContainerCapacityError):
        _ = await world.service.transfer_from_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )

    assert world.db.executed == []
    assert _names(world.store.items()) == [("torch", 1)]


# ---- every transfer ----


async def test_a_second_transfer_in_one_session_is_not_mistaken_for_a_duplicate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The open session's token is the same for every transfer; the old guard dropped all but the first."""
    world = _world(monkeypatch, carried=[_stack("torch"), _stack("rope")])

    for item_id in ("torch", "rope"):
        _ = await world.service.transfer_to_container(
            CID, PID, world.token, _stack(item_id), 1, registry=world.registry
        )

    assert _names(world.store.items()) == [("torch", 1), ("rope", 1)]
    assert world.committed_carried() == []


async def test_a_failed_commit_leaves_the_player_as_they_were(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING], container_items=[_stack("torch")], db=FakeDatabase(fail_commits=1))

    with pytest.raises(RuntimeError, match="database unavailable"):
        _ = await world.service.transfer_from_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )

    assert world.db.rollbacks == 1
    view = await world.registry.get(PID)
    assert view is not None and _names(view.inventory.carried) == [("sling", 1)]


async def test_a_transfer_for_no_such_player_is_a_validation_error(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[], container_items=[_stack("torch")], player_exists=False)

    with pytest.raises(ValidationError, match="Player not found"):
        _ = await world.service.transfer_from_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )


async def test_a_transfer_from_a_vanished_container_changes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[_stack("torch")])
    del world.store.rows[CID]

    with pytest.raises(ContainerNotFoundError):
        _ = await world.service.transfer_to_container(
            CID, PID, world.token, _stack("torch"), 1, registry=world.registry
        )

    assert world.db.executed == []


async def test_a_transfer_needs_the_open_sessions_token(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[_stack("torch")])

    with pytest.raises(ContainerServiceError, match="Invalid mutation token"):
        _ = await world.service.transfer_to_container(
            CID, PID, "not-the-token", _stack("torch"), 1, registry=world.registry
        )

    assert world.db.executed == []


# ---- loot-all ----


async def test_loot_all_moves_every_stack_in_one_commit(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING], container_items=[_stack("torch", 2), _stack("rope")])

    result = await world.service.loot_all(CID, PID, world.token, registry=world.registry)

    assert result.items_looted == 2
    assert result.container.items == []
    assert result.player_equipped == {}
    assert _names(result.player_inventory) == [("sling", 1), ("torch", 2), ("rope", 1)]
    assert _names(world.committed_carried()) == [("sling", 1), ("torch", 2), ("rope", 1)]
    assert world.store.items() == []
    assert world.db.commits == 1


async def test_loot_all_stops_when_the_player_is_full(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING], container_items=[_stack("torch"), _stack("rope")], max_slots=2)

    result = await world.service.loot_all(CID, PID, world.token, registry=world.registry)

    assert result.items_looted == 1
    assert _names(world.committed_carried()) == [("sling", 1), ("torch", 1)]
    assert _names(world.store.items()) == [("rope", 1)]


async def test_loot_all_leaves_an_invalid_stack_behind(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[], container_items=[_stack("husk", 0), _stack("torch")])

    result = await world.service.loot_all(CID, PID, world.token, registry=world.registry)

    assert result.items_looted == 1
    assert _names(world.committed_carried()) == [("torch", 1)]
    assert _names(world.store.items()) == [("husk", 0)]


async def test_loot_all_of_an_empty_container_writes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    world = _world(monkeypatch, carried=[SLING])

    result = await world.service.loot_all(CID, PID, world.token, registry=world.registry)

    assert result.items_looted == 0
    assert world.db.executed == []
