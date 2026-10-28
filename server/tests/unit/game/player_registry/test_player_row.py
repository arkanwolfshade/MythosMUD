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


def test_update_params_serialize_stats_and_utc_times() -> None:
    local = datetime(2026, 10, 26, 12, 0, tzinfo=UTC)
    data = row_data(last_active=local, stats={"current_dp": 20, "max_dp": 20})

    params = data.update_params()

    assert params["last_active"] == local
    assert json.loads(str(params["stats"])) == {"current_dp": 20, "max_dp": 20}


def test_set_stat_marks_lazy_dirty_only_on_change() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 20)
    assert not part.dirty
    part.set_stat("current_dp", 5)
    assert part.dirty and not part.sync_required


def test_rollback_restores_state_and_flags() -> None:
    part = PlayerRowPart(row_data())
    part.begin()
    part.set_stat("current_dp", 1)
    part.set_current_room_id("elsewhere")
    part.rollback()

    assert part.stats["current_dp"] == 20
    assert part.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
    assert not part.dirty and not part.sync_required


def test_take_write_captures_state_at_capture_time() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 1)
    write = part.take_write()
    assert write is not None and not part.dirty
    part.set_stat("current_dp", 2)  # a later change is not in the captured write
    assert part.take_write() is not None


async def test_captured_write_sends_the_row_columns() -> None:
    part = PlayerRowPart(row_data())
    part.set_stat("current_dp", 9)
    write = part.take_write()
    db = FakeDatabase()
    assert write is not None
    async with db.session() as session:
        await write(session)
    params = db.executed[-1]
    assert params is not None and '"current_dp": 9' in str(params["stats"])


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
