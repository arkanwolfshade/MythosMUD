"""Unit tests for E2ePlayerSupport: the e2e harness's resets, placement and state read, as registry units."""

from __future__ import annotations

import uuid
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime, timedelta

import pytest

from server.constants.instance_rooms import PENDING_INSTANCE_ID
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM
from server.game.player_registry import (
    DbSession,
    EffectData,
    LucidityData,
    PlayerAggregate,
    PlayerCooldownsPart,
    PlayerEffectsPart,
    PlayerRegistry,
    QuestInstanceData,
)
from server.game.player_registry.player_quests import DELETE_QUEST_INSTANCES_SQL
from server.services.e2e_player_support import (
    E2ePlayerSupport,
    UnknownPlayerError,
    UnknownRoomError,
)
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

BANK_ID = uuid.uuid4()
CHEST_ID = uuid.uuid4()
ELSEWHERE = "earth_arkhamcity_downtown_room_arkham_savings_001"
T0 = datetime(2026, 11, 11, 12, 0, tzinfo=UTC)


class _Named:
    def __init__(self, player_id: uuid.UUID) -> None:
        self.player_id: uuid.UUID = player_id


class _FakePersistence:
    """Names to ids, one bank box holding a coin, and the foyer's lost-and-found chest and an unrelated crate."""

    def __init__(self, ids: Mapping[str, uuid.UUID]) -> None:
        self.ids: Mapping[str, uuid.UUID] = ids
        self.emptied: list[uuid.UUID] = []

    async def get_player_by_name(self, name: str) -> _Named | None:
        player_id = self.ids.get(name)
        return _Named(player_id) if player_id is not None else None

    async def get_bank_container(self, owner_id: uuid.UUID) -> Mapping[str, object] | None:
        _ = owner_id
        return {"container_id": str(BANK_ID), "items_json": [{"item_name": "Silver Coin"}, {"item_name": "Ring"}]}

    async def get_containers_by_room_id(self, room_id: str) -> Sequence[Mapping[str, object]]:
        assert room_id == DEFAULT_RESPAWN_ROOM
        return [
            {"container_id": str(CHEST_ID), "metadata_json": {"role": "lost_and_found"}},
            {"container_id": str(uuid.uuid4()), "metadata_json": {"role": "decoration"}},
            {"container_id": str(uuid.uuid4()), "metadata_json": None},
        ]

    async def update_container(
        self, container_id: uuid.UUID, items_json: list[dict[str, object]] | None = None
    ) -> object:
        assert items_json == []
        self.emptied.append(container_id)
        return None


class _FakeRooms:
    async def get_room(self, room_id: str) -> Mapping[str, object] | None:
        return {"id": room_id} if room_id in {ELSEWHERE, DEFAULT_RESPAWN_ROOM} else None


class _Loader:
    """Loads each player with a quest, a poison and a ward effect, a tonic cooldown, and low lucidity."""

    def __init__(self, rows: Mapping[uuid.UUID, Mapping[str, object]]) -> None:
        self.rows: Mapping[uuid.UUID, Mapping[str, object]] = rows

    async def __call__(self, _session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        row = self.rows.get(player_id)
        if row is None:
            return None
        quest = QuestInstanceData(uuid.uuid4(), "leave_the_tutorial", "active", {}, T0, None)
        effects = PlayerEffectsPart(
            player_id,
            [
                EffectData(uuid.uuid4(), "poison", "debuff", 30, {}),
                EffectData(uuid.uuid4(), "login_warded", "buff", 30, {}),
            ],
        )
        cooldowns = PlayerCooldownsPart(
            player_id, {"folk_tonic": T0 + timedelta(minutes=30), "debrief_pending": T0 + timedelta(hours=1)}
        )
        return aggregate(row, [quest], LucidityData(lcd=-40, tier="uneasy"), cooldowns=cooldowns, effects=effects)


def _harness(**overrides: object) -> tuple[E2ePlayerSupport, PlayerRegistry, FakeDatabase, _FakePersistence, uuid.UUID]:
    """Three characters with the same row; the id returned is E2ETutorial's."""
    ids = {name: uuid.uuid4() for name in ("Ithaqua", "ArkanWolfshade", "E2ETutorial")}
    rows = {pid: raw_row(pid, current_room_id=ELSEWHERE, **overrides) for pid in ids.values()}
    db = FakeDatabase()
    registry = PlayerRegistry(db.session, loader=_Loader(rows))
    persistence = _FakePersistence(ids)
    return E2ePlayerSupport(registry, persistence, _FakeRooms()), registry, db, persistence, ids["E2ETutorial"]


async def test_reset_shared_players_returns_them_to_the_default_room_standing_at_fifty_dp() -> None:
    support, registry, db, persistence, tutorial_id = _harness(
        stats={"current_dp": 7, "max_dp": 100, "position": "sitting"}
    )

    await support.reset_shared_players()

    for name in ("Ithaqua", "ArkanWolfshade"):
        view = registry.peek(persistence.ids[name])
        assert view is not None
        assert view.row.current_room_id == DEFAULT_RESPAWN_ROOM
        assert view.row.stats["current_dp"] == 50 and view.row.stats["position"] == "standing"
        assert view.cooldowns.expires_at("folk_tonic") is None
        assert view.cooldowns.expires_at("debrief_pending") is not None  # only the tonic is forgotten
    assert registry.peek(tutorial_id) is None  # the tutorial character is not a shared player
    assert db.commits == 2  # one synchronous unit per shared player


async def test_reset_tutorial_character_starts_the_character_over() -> None:
    support, registry, db, persistence, player_id = _harness(
        stats={"current_dp": 3, "max_dp": 80, "corruption": 12, "position": "sitting"},
        tutorial_instance_id="instance-1",
    )

    await support.reset_tutorial_character("E2ETutorial")

    view = registry.peek(player_id)
    assert view is not None
    assert view.row.current_room_id == DEFAULT_RESPAWN_ROOM and view.row.respawn_room_id == DEFAULT_RESPAWN_ROOM
    assert view.row.tutorial_instance_id == PENDING_INSTANCE_ID
    assert view.row.stats["current_dp"] == 80 and view.row.stats["corruption"] == 0
    assert view.row.stats["position"] == "standing"
    assert [stack["item_name"] for stack in view.inventory.carried] == ["Sling"] and not view.inventory.equipped
    assert view.quests.all() == []
    assert [effect.effect_type for effect in view.effects.effects] == ["login_warded"]
    assert view.lucidity.lcd == 100 and view.lucidity.tier == "lucid"
    assert view.cooldowns.expires_at("debrief_pending") is None
    assert DELETE_QUEST_INSTANCES_SQL in db.statements
    assert persistence.emptied == [CHEST_ID, BANK_ID]


async def test_reset_tutorial_character_without_max_dp_uses_one_hundred() -> None:
    support, registry, _db, _persistence, player_id = _harness(stats={"current_dp": 3})

    await support.reset_tutorial_character("E2ETutorial")

    view = registry.peek(player_id)
    assert view is not None and view.row.stats["current_dp"] == 100


async def test_place_moves_the_character_and_takes_them_out_of_the_tutorial() -> None:
    support, registry, db, _persistence, player_id = _harness(tutorial_instance_id="instance-1")

    await support.place("E2ETutorial", DEFAULT_RESPAWN_ROOM)

    view = registry.peek(player_id)
    assert view is not None
    assert view.row.current_room_id == DEFAULT_RESPAWN_ROOM and view.row.tutorial_instance_id is None
    assert db.commits == 1


async def test_place_refuses_a_room_that_does_not_exist_and_changes_nothing() -> None:
    support, registry, db, _persistence, player_id = _harness()

    with pytest.raises(UnknownRoomError):
        await support.place("E2ETutorial", "no_such_room")

    assert registry.peek(player_id) is None and db.commits == 0


@pytest.mark.parametrize("action", ["reset_tutorial_character", "state"])
async def test_an_unknown_character_is_refused(action: str) -> None:
    support, *_rest = _harness()

    with pytest.raises(UnknownPlayerError):
        await getattr(support, action)("Nobody")

    with pytest.raises(UnknownPlayerError):
        await support.place("Nobody", DEFAULT_RESPAWN_ROOM)


async def test_state_reports_what_the_registry_holds() -> None:
    support, _registry, _db, _persistence, _player_id = _harness(
        stats={"current_dp": 12, "magic_points": 4, "max_magic_points": 9, "intelligence": 61, "corruption": 2},
        tutorial_instance_id="instance-1",
    )

    state = await support.state("E2ETutorial")

    assert state.current_room_id == ELSEWHERE and state.respawn_room_id == DEFAULT_RESPAWN_ROOM
    assert state.tutorial_instance_id == "instance-1"
    assert state.bank_items == ["Silver Coin", "Ring"]
    assert (state.current_dp, state.corruption, state.magic_points) == (12, 2, 4)
    assert (state.max_magic_points, state.intelligence, state.current_lcd) == (9, 61, -40)
    assert state.inventory_items == ["Sling"]
    assert state.quests == {"leave_the_tutorial": "active"}
    assert state.debrief_pending is True


async def test_state_leaves_missing_stats_null() -> None:
    support, *_rest = _harness()

    state = await support.state("E2ETutorial")

    assert state.magic_points is None and state.intelligence is None and state.corruption is None
