"""Unit tests for the players-row part: parsing a get_player_by_id row, update parameters, mutators, rollback."""

from __future__ import annotations

import json
import re
import uuid
from datetime import UTC, datetime

from server.game.player_registry import PlayerRowPart, fetch_player_row
from server.game.player_registry.player_row import LOAD_PLAYER_SQL, UPDATE_PLAYER_ROW_SQL

from .fakes import FakeDatabase, row_data


def test_from_row_parses_json_text_and_defaults() -> None:
    data = row_data(stats='{"current_dp": 3}', profession_id=0, current_room_id=None, level=None)

    assert data.stats == {"current_dp": 3}
    assert data.profession_id is None  # PlayerSavePreparer sends NULL for a falsy profession
    assert data.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
    assert data.level == 1


def test_load_sql_calls_the_procedure_and_selects_every_column_either_part_reads() -> None:
    sql = " ".join(str(LOAD_PLAYER_SQL).split())
    assert sql.endswith("FROM get_player_by_id(:id)")
    selected = {column.strip() for column in sql.removeprefix("SELECT ").split(" FROM ")[0].split(",")}
    read_by_from_row = {
        "player_id", "user_id", "name", "current_room_id", "respawn_room_id", "experience_points", "level",
        "is_admin", "profession_id", "created_at", "last_active", "is_deleted", "deleted_at",
        "tutorial_instance_id", "stats", "inventory", "equipped_json",
    }  # fmt: skip
    assert read_by_from_row <= selected


def test_update_params_cover_every_procedure_argument_and_no_inventory() -> None:
    expected = set(re.findall(r":(\w+)", str(UPDATE_PLAYER_ROW_SQL)))
    params = row_data().update_params()

    assert set(params) == expected
    assert not {"inventory", "inventory_json", "equipped_json"} & set(params)  # the inventory part writes those


def test_update_params_send_only_the_changed_stats_and_utc_times() -> None:
    """A write merges just the keys it changed (step 5c): DP and MP still have writers outside the registry."""
    local = datetime(2026, 10, 26, 12, 0, tzinfo=UTC)
    data = row_data(last_active=local, stats={"current_dp": 20, "max_dp": 20, "corruption": 4})

    assert data.update_params()["last_active"] == local
    assert json.loads(str(data.update_params()["stats_changes"])) == {}
    assert json.loads(str(data.update_params(["corruption"])["stats_changes"])) == {"corruption": 4}


def test_set_stat_marks_lazy_dirty_only_on_change() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 20)
    assert not part.dirty
    part.set_stat("current_dp", 5)
    assert part.dirty and not part.sync_required


def test_set_stat_can_require_a_sync_commit() -> None:
    part = PlayerRowPart(row_data())

    part.set_stat("corruption", 3, sync=True)

    assert part.dirty and part.sync_required


async def test_rollback_restores_state_and_flags() -> None:
    part = PlayerRowPart(row_data())
    part.begin()
    part.set_stat("current_dp", 1)
    part.set_current_room_id("elsewhere")
    part.rollback()

    assert part.stats["current_dp"] == 20
    assert part.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
    assert not part.dirty and not part.sync_required
    assert (
        json.loads(str((await _written(part))["stats_changes"])) == {}
    )  # the rolled-back key is not sent later either


def test_take_write_captures_state_at_capture_time() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 1)
    write = part.take_write()
    assert write is not None and not part.dirty
    part.set_stat("current_dp", 2)  # a later change is not in the captured write
    assert part.take_write() is not None


async def test_captured_write_sends_the_row_columns_and_only_the_changed_stats() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 9)
    write = part.take_write()
    db = FakeDatabase()
    assert write is not None
    async with db.session() as session:
        await write(session)
    params = db.executed[-1]
    assert params is not None and json.loads(str(params["stats_changes"])) == {"current_dp": 9}

    part.set_current_room_id("elsewhere")  # a later write of other columns sends no stats
    assert json.loads(str((await _written(part))["stats_changes"])) == {}


async def test_a_failed_lazy_flush_sends_its_stats_keys_again() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 9)
    assert part.take_write() is not None
    part.set_stat("max_dp", 30)

    part.write_failed()

    assert part.dirty
    assert json.loads(str((await _written(part))["stats_changes"])) == {"current_dp": 9, "max_dp": 30}


async def _written(part: PlayerRowPart) -> dict[str, object]:
    """The parameters of the part's next write (dirtying it first, so there is one)."""
    part.mark_dirty()
    write = part.take_write()
    assert write is not None
    db = FakeDatabase()
    async with db.session() as session:
        await write(session)
    params = db.executed[-1]
    assert params is not None
    return dict(params)


async def test_fetch_player_row() -> None:
    pid = uuid.uuid4()
    db = FakeDatabase(row={**_raw_row(pid)})
    async with db.session() as session:
        row = await fetch_player_row(session, pid)
    assert row is not None and row["player_id"] == pid

    async with FakeDatabase(row=None).session() as session:
        assert await fetch_player_row(session, pid) is None


def _raw_row(pid: uuid.UUID) -> dict[str, object]:
    return {
        "player_id": pid,
        "user_id": uuid.uuid4(),
        "name": "Loaded",
        "current_room_id": "room",
        "stats": {"current_dp": 20},
        "inventory": "[]",
        "equipped_json": "{}",
    }
