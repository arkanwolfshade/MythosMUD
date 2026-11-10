"""Unit tests for the effects part (ADR-029 step 6d) and how the loader builds it."""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import cast

from server.game.player_registry import EffectData, PlayerEffectsPart, load_player_aggregate
from server.game.player_registry.part import DbSession
from server.game.player_registry.player_effects import (
    ADD_EFFECT_SQL,
    ADVANCE_EFFECTS_SQL,
    DELETE_EFFECT_SQL,
    DELETE_EFFECTS_BY_TYPE_SQL,
    DELETE_INSTANCE_SCOPED_SQL,
    UPDATE_PAYLOAD_SQL,
)
from server.game.player_registry.player_lucidity import LOAD_LUCIDITY_SQL
from server.game.player_registry.player_quests import LIST_QUEST_INSTANCES_SQL

from .fakes import raw_row

PLAYER = uuid.UUID("11111111-1111-1111-1111-111111111111")


def _effect(effect_type: str = "heal_over_time", remaining: int | None = None, **extra: object) -> EffectData:
    return EffectData(
        id=uuid.uuid4(),
        effect_type=effect_type,
        category="scripted",
        remaining_seconds=remaining,
        payload=cast(Mapping[str, object], extra.get("payload", {})),
        instance_scoped=bool(extra.get("instance_scoped", False)),
    )


@dataclass
class _Recorder:
    """A session that remembers each statement with its parameters, in order."""

    calls: list[tuple[object, Mapping[str, object]]] = field(default_factory=list)

    async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> None:
        self.calls.append((statement, params or {}))

    def statements(self) -> list[object]:
        return [statement for statement, _params in self.calls]


async def _write_out(part: PlayerEffectsPart) -> _Recorder:
    write = part.take_write()
    assert write is not None
    recorder = _Recorder()
    await write(cast(DbSession, cast(object, recorder)))
    return recorder


def test_adding_an_effect_is_synchronous_and_names_its_id() -> None:
    part = PlayerEffectsPart(PLAYER)

    effect_id = part.add("login_warded", "entry_ward", remaining_seconds=30, source="game_entry")

    [effect] = part.effects
    assert effect.id == effect_id and effect.effect_type == "login_warded" and effect.remaining_seconds == 30
    assert part.dirty and part.sync_required


async def test_an_added_effect_is_written_with_the_id_the_part_gave_it() -> None:
    part = PlayerEffectsPart(PLAYER)
    effect_id = part.add(
        "heal_over_time", "scripted", remaining_seconds=15, payload={"healing": 5}, instance_scoped=True, intensity=2
    )

    recorder = await _write_out(part)

    [(statement, params)] = recorder.calls
    assert statement is ADD_EFFECT_SQL and "add_player_effect" in str(ADD_EFFECT_SQL)
    assert params["effect_id"] == str(effect_id) and params["player_id"] == str(PLAYER)
    assert params["remaining_seconds"] == 15 and params["instance_scoped"] is True and params["intensity"] == 2
    assert json.loads(str(params["payload"])) == {"healing": 5}


def test_an_effect_with_no_time_left_is_never_stored() -> None:
    part = PlayerEffectsPart(PLAYER)

    _ = part.add("blinded", "spell", remaining_seconds=0)

    assert part.effects == () and not part.dirty


async def test_removing_an_effect_deletes_that_row_only() -> None:
    keep, drop = _effect("blinded"), _effect("heal_over_time")
    part = PlayerEffectsPart(PLAYER, [keep, drop])

    assert part.remove(drop.id)
    assert not part.remove(drop.id)  # already gone: nothing more to write

    assert part.effects == (keep,)
    recorder = await _write_out(part)
    assert recorder.calls == [(DELETE_EFFECT_SQL, {"effect_id": str(drop.id)})]


async def test_removing_by_type_ends_every_effect_of_that_type() -> None:
    part = PlayerEffectsPart(PLAYER, [_effect("blinded"), _effect("blinded"), _effect("heal_over_time")])

    assert part.remove_by_type("blinded") == 2
    assert part.remove_by_type("blinded") == 0

    assert [effect.effect_type for effect in part.effects] == ["heal_over_time"]
    recorder = await _write_out(part)
    assert recorder.calls == [(DELETE_EFFECTS_BY_TYPE_SQL, {"player_id": str(PLAYER), "effect_type": "blinded"})]


async def test_clearing_instance_scoped_effects_keeps_the_rest() -> None:
    part = PlayerEffectsPart(PLAYER, [_effect("lucidity_drain_over_time", instance_scoped=True), _effect("blinded")])

    assert part.clear_instance_scoped() == 1
    assert part.clear_instance_scoped() == 0

    assert [effect.effect_type for effect in part.effects] == ["blinded"]
    recorder = await _write_out(part)
    assert recorder.calls == [(DELETE_INSTANCE_SCOPED_SQL, {"player_id": str(PLAYER)})]


async def test_a_payload_change_is_written_and_an_unchanged_one_is_not() -> None:
    drain = _effect("lucidity_drain_over_time", payload={"elapsed": 4})
    part = PlayerEffectsPart(PLAYER, [drain])

    assert not part.set_payload(drain.id, {"elapsed": 4})
    assert not part.dirty
    assert part.set_payload(drain.id, {"elapsed": 5})
    assert not part.set_payload(uuid.uuid4(), {"elapsed": 1})  # not this player's effect

    assert part.effects[0].payload == {"elapsed": 5}
    recorder = await _write_out(part)
    [(statement, params)] = recorder.calls
    assert statement is UPDATE_PAYLOAD_SQL and params["effect_id"] == str(drain.id)
    assert json.loads(str(params["payload"])) == {"elapsed": 5}


def test_a_second_passing_counts_timed_effects_down_and_ends_the_ones_that_run_out() -> None:
    ward, almost, forever = (
        _effect("login_warded", 3),
        _effect("heal_over_time", 1),
        _effect("lucidity_drain_over_time"),
    )
    part = PlayerEffectsPart(PLAYER, [ward, almost, forever])

    ended = part.advance_second()

    assert ended == [almost]
    assert [(effect.effect_type, effect.remaining_seconds) for effect in part.effects] == [
        ("login_warded", 2),
        ("lucidity_drain_over_time", None),
    ]
    assert part.sync_required


async def test_the_countdown_is_written_as_the_database_procedure_that_runs_it() -> None:
    part = PlayerEffectsPart(PLAYER, [_effect("blinded", 5)])
    _ = part.advance_second()

    recorder = await _write_out(part)

    assert recorder.calls == [(ADVANCE_EFFECTS_SQL, {"player_ids": [PLAYER]})]
    assert "advance_player_effects" in str(ADVANCE_EFFECTS_SQL)


def test_untimed_effects_have_no_countdown_to_write() -> None:
    part = PlayerEffectsPart(PLAYER, [_effect("lucidity_drain_over_time")])

    assert part.advance_second() == []
    assert not part.dirty
    assert PlayerEffectsPart(PLAYER).advance_second() == []


async def test_writes_apply_in_the_order_they_were_made() -> None:
    drain = _effect("lucidity_drain_over_time", payload={"elapsed": 0})
    part = PlayerEffectsPart(PLAYER, [drain])
    _ = part.set_payload(drain.id, {"elapsed": 1})
    _ = part.add("blinded", "spell", remaining_seconds=4)
    _ = part.advance_second()
    _ = part.remove(drain.id)

    recorder = await _write_out(part)

    assert recorder.statements() == [UPDATE_PAYLOAD_SQL, ADD_EFFECT_SQL, ADVANCE_EFFECTS_SQL, DELETE_EFFECT_SQL]
    assert not part.dirty and not part.sync_required


def test_rollback_restores_the_effects_and_forgets_the_queued_writes() -> None:
    heal = _effect("heal_over_time", 9)
    part = PlayerEffectsPart(PLAYER, [heal])
    part.begin()
    _ = part.add("blinded", "spell", remaining_seconds=4)
    _ = part.remove(heal.id)
    _ = part.advance_second()
    part.rollback()

    assert part.effects == (heal,)
    assert not part.dirty
    assert part.take_write() is None


async def test_a_failed_flush_puts_its_writes_back_in_front_of_newer_ones() -> None:
    first, second = _effect("blinded"), _effect("heal_over_time")
    part = PlayerEffectsPart(PLAYER, [first, second])
    _ = part.remove(first.id)
    assert part.take_write() is not None  # the flusher took it, then failed
    _ = part.remove(second.id)

    part.write_failed()

    recorder = await _write_out(part)
    assert recorder.calls == [
        (DELETE_EFFECT_SQL, {"effect_id": str(first.id)}),
        (DELETE_EFFECT_SQL, {"effect_id": str(second.id)}),
    ]


def test_the_effects_column_builds_the_part_from_a_json_array_or_its_text() -> None:
    effect_id = uuid.uuid4()
    rows: list[dict[str, object]] = [
        {
            "id": str(effect_id),
            "effect_type": "heal_over_time",
            "category": "scripted",
            "remaining_seconds": 12,
            "payload": {"healing": 5},
            "instance_scoped": False,
            "intensity": 1,
            "source": None,
            "visibility_level": "visible",
        }
    ]

    for column in (rows, json.dumps(rows)):
        [effect] = PlayerEffectsPart.from_json(PLAYER, column).effects
        assert effect == EffectData(effect_id, "heal_over_time", "scripted", 12, {"healing": 5})

    assert PlayerEffectsPart.from_json(PLAYER, None).effects == ()


async def test_the_default_loader_builds_the_effects_part_from_the_lucidity_state_row() -> None:
    player_id = uuid.uuid4()
    effect_id = uuid.uuid4()
    state: dict[str, object] = {
        "current_lcd": None,
        "current_tier": None,
        "liabilities": None,
        "last_updated_at": None,
        "catatonia_entered_at": None,
        "cooldowns": [],
        "exposures": [],
        "effects": [
            {
                "id": str(effect_id),
                "effect_type": "login_warded",
                "category": "entry_ward",
                "remaining_seconds": None,
                "payload": {},
                "instance_scoped": False,
                "intensity": 1,
                "source": "game_entry",
                "visibility_level": "visible",
            }
        ],
    }

    class _Session:
        def __init__(self) -> None:
            self.answer: Sequence[Mapping[str, object]] = []

        async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> _Session:
            _ = params
            if statement is LOAD_LUCIDITY_SQL:
                self.answer = [state]
            elif statement is LIST_QUEST_INSTANCES_SQL:
                self.answer = []
            else:
                self.answer = [raw_row(player_id)]
            return self

        def mappings(self) -> _Session:
            return self

        def first(self) -> Mapping[str, object] | None:
            return self.answer[0] if self.answer else None

        def all(self) -> Sequence[Mapping[str, object]]:
            return self.answer

    loaded = await load_player_aggregate(cast(DbSession, cast(object, _Session())), player_id)

    assert loaded is not None
    [effect] = loaded.effects.effects
    assert effect.id == effect_id and effect.source == "game_entry"
    assert "effects" in str(LOAD_LUCIDITY_SQL)
