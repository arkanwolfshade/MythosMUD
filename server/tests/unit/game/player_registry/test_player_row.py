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


def test_update_params_send_only_the_changed_columns_and_stats() -> None:
    """A write sets just what it changed (steps 5c, 6a): players are still saved outside the registry."""
    local = datetime(2026, 10, 26, 12, 0, tzinfo=UTC)
    data = row_data(last_active=local, respawn_room_id=None, stats={"current_dp": 20, "max_dp": 20, "corruption": 4})

    nothing = data.update_params()
    assert json.loads(str(nothing["changes"])) == {} and json.loads(str(nothing["stats_changes"])) == {}
    some = data.update_params(["last_active", "respawn_room_id"], ["corruption"])
    assert json.loads(str(some["changes"])) == {
        "last_active": local.isoformat(),
        "respawn_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",  # PlayerSavePreparer's default
    }
    assert json.loads(str(some["stats_changes"])) == {"corruption": 4}


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
    params = await _written(part)  # the rolled-back changes are not sent later either
    assert json.loads(str(params["stats_changes"])) == {} and json.loads(str(params["changes"])) == {}


def test_take_write_captures_state_at_capture_time() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 1)
    write = part.take_write()
    assert write is not None and not part.dirty
    part.set_stat("current_dp", 2)  # a later change is not in the captured write
    assert part.take_write() is not None


async def test_captured_write_sends_only_what_changed() -> None:
    """A stats change must not write back the aggregate's copy of the room, XP or last_active (step 6a)."""
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 9)
    write = part.take_write()
    db = FakeDatabase()
    assert write is not None
    async with db.session() as session:
        await write(session)
    params = db.executed[-1]
    assert params is not None and json.loads(str(params["stats_changes"])) == {"current_dp": 9}
    assert json.loads(str(params["changes"])) == {}

    part.set_current_room_id("elsewhere")
    part.set_experience(10, 1)  # the level is unchanged, so only the XP is sent
    params = await _written(part)
    assert json.loads(str(params["changes"])) == {"current_room_id": "elsewhere", "experience_points": 10}
    assert json.loads(str(params["stats_changes"])) == {}


async def test_remove_stat_sends_the_key_as_null_which_removes_it() -> None:
    part = PlayerRowPart(row_data(stats={"current_dp": 20, "death_room_id": "street"}))

    part.remove_stat("death_room_id", sync=True)
    part.remove_stat("never_there")  # a no-op

    assert "death_room_id" not in part.stats and part.sync_required
    assert json.loads(str((await _written(part))["stats_changes"])) == {"death_room_id": None}


async def test_a_failed_lazy_flush_sends_its_changes_again() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 9)
    part.set_current_room_id("elsewhere")
    assert part.take_write() is not None
    part.set_stat("max_dp", 30)

    part.write_failed()

    assert part.dirty
    params = await _written(part)
    assert json.loads(str(params["stats_changes"])) == {"current_dp": 9, "max_dp": 30}
    assert json.loads(str(params["changes"])) == {"current_room_id": "elsewhere"}


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
