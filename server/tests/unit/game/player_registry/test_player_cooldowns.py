"""Unit tests for the cooldowns and exposure parts (ADR-029 step 5b-ii) and their load with the lucidity row."""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime, timedelta
from typing import cast

from server.game.player_registry import (
    Exposure,
    PlayerCooldownsPart,
    PlayerExposurePart,
    load_player_aggregate,
)
from server.game.player_registry.player_cooldowns import REPLACE_COOLDOWNS_SQL, parse_timestamp
from server.game.player_registry.player_exposure import UPSERT_EXPOSURES_SQL
from server.game.player_registry.player_lucidity import LOAD_LUCIDITY_SQL
from server.game.player_registry.player_quests import LIST_QUEST_INSTANCES_SQL

from .fakes import FakeDatabase, raw_row

T0 = datetime(2026, 11, 2, 12, 0, tzinfo=UTC)


def test_parse_timestamp_accepts_datetimes_and_iso_strings_and_assumes_utc_for_naive_ones() -> None:
    assert parse_timestamp(T0) == T0
    assert parse_timestamp("2026-11-02T12:00:00+00:00") == T0
    assert parse_timestamp(datetime(2026, 11, 2, 12, 0)) == T0


def test_a_cooldown_is_active_until_it_expires() -> None:
    part = PlayerCooldownsPart(uuid.uuid4(), {"pray": T0})

    assert part.active("pray", T0 - timedelta(seconds=1))
    assert not part.active("pray", T0)
    assert not part.active("meditate", T0)
    assert part.expires_at("pray") == T0 and part.expires_at("meditate") is None


def test_setting_and_clearing_a_cooldown_is_synchronous() -> None:
    part = PlayerCooldownsPart(uuid.uuid4())

    part.set("pray", T0)
    assert part.dirty and part.sync_required

    _ = part.take_write()
    assert part.clear("pray") and part.sync_required
    assert not part.clear("pray")  # nothing left to clear


def test_an_unchanged_cooldown_is_not_dirty() -> None:
    part = PlayerCooldownsPart(uuid.uuid4(), {"pray": T0})

    part.set("pray", T0)

    assert not part.dirty


def test_clear_prefix_removes_only_the_matching_cooldowns() -> None:
    part = PlayerCooldownsPart(uuid.uuid4(), {"hallucination_timer": T0, "hallucination_x": T0, "pray": T0})

    assert part.clear_prefix("hallucination_") == 2
    assert part.expires_at("pray") == T0 and part.expires_at("hallucination_timer") is None
    assert PlayerCooldownsPart(uuid.uuid4()).clear_prefix("hallucination_") == 0


def test_rollback_restores_the_cooldowns() -> None:
    part = PlayerCooldownsPart(uuid.uuid4(), {"pray": T0})
    part.begin()
    _ = part.clear("pray")
    part.set("debrief_pending", T0)
    part.rollback()

    assert part.expires_at("pray") == T0 and part.expires_at("debrief_pending") is None
    assert not part.dirty


async def test_a_cooldown_write_replaces_the_whole_set() -> None:
    player_id = uuid.uuid4()
    part = PlayerCooldownsPart(player_id, {"pray": T0})
    part.set("meditate", T0 + timedelta(minutes=10))
    write = part.take_write()
    assert write is not None

    db = FakeDatabase()
    async with db.session() as session:
        await write(session)

    [params] = [params for params in db.executed if params is not None]
    assert params["player_id"] == str(player_id)
    rows = cast(list[dict[str, object]], json.loads(str(params["cooldowns"])))
    assert {row["action_code"] for row in rows} == {"meditate", "pray"}
    assert "replace_lucidity_cooldowns" in str(REPLACE_COOLDOWNS_SQL)


def test_recording_an_encounter_counts_up_and_is_synchronous() -> None:
    part = PlayerExposurePart(uuid.uuid4(), {"ghoul": Exposure(2, T0)})

    assert part.record_encounter("ghoul", T0) == 3
    assert part.record_encounter("byakhee", T0) == 1
    assert part.encounter_count("ghoul") == 3 and part.encounter_count("deep_one") == 0
    assert part.sync_required


def test_exposure_rollback_forgets_the_encounter() -> None:
    part = PlayerExposurePart(uuid.uuid4())
    part.begin()
    _ = part.record_encounter("ghoul", T0)
    part.rollback()

    assert part.encounter_count("ghoul") == 0 and not part.dirty


async def test_an_exposure_write_upserts_every_archetype() -> None:
    part = PlayerExposurePart(uuid.uuid4(), {"ghoul": Exposure(1, T0)})
    _ = part.record_encounter("byakhee", T0)
    write = part.take_write()
    assert write is not None

    db = FakeDatabase()
    async with db.session() as session:
        await write(session)

    [params] = [params for params in db.executed if params is not None]
    rows = cast(list[dict[str, object]], json.loads(str(params["exposures"])))
    assert [(row["entity_archetype"], row["encounter_count"]) for row in rows] == [("byakhee", 1), ("ghoul", 1)]
    assert "upsert_lucidity_exposures" in str(UPSERT_EXPOSURES_SQL)


async def test_the_default_loader_builds_lucidity_cooldowns_and_exposure_from_one_row() -> None:
    player_id = uuid.uuid4()
    state: dict[str, object] = {
        "current_lcd": None,  # no player_lucidity row yet
        "current_tier": None,
        "liabilities": None,
        "last_updated_at": None,
        "catatonia_entered_at": None,
        "cooldowns": [{"action_code": "debrief_pending", "expires_at": "2026-11-02T12:00:00+00:00"}],
        "exposures": json.dumps(
            [{"entity_archetype": "ghoul", "encounter_count": 4, "last_encounter_at": "2026-11-02T12:00:00+00:00"}]
        ),
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

        async def commit(self) -> None:
            return None

        async def rollback(self) -> None:
            return None

    loaded = await load_player_aggregate(_Session(), player_id)

    assert loaded is not None
    assert loaded.lucidity.lcd == 100  # the starting value
    assert loaded.cooldowns.expires_at("debrief_pending") == T0
    assert loaded.exposure.encounter_count("ghoul") == 4
