"""Guards the #829 Arkham street-grid migration (`data/db/migrations/20260913_*`).

The migration converges a database loaded before #829 onto the current base DML without
the destructive world-seed reload. Three defects were found by running it, and each is
pinned here because each fails silently or late rather than obviously:

* `npc_definitions.room_id` was `character varying(50)`. 200 of the 518 rebuilt room ids
  are longer than that, so those rooms could not host an NPC at all. A future street name
  can reintroduce this the moment an id outgrows a column that stores one.
* `room_links.to_room_id` is `ON DELETE RESTRICT` (only `from_room_id` cascades), so exits
  must be cleared before rooms are deleted or the migration aborts.
* Rooms whose `stable_id` survived the rebuild keep their UUID and are upserted rather
  than deleted, so their OLD exits never cascade away. Without an explicit clear, an exit
  in a direction the room no longer has survives as a link between two live rooms.

Reads the SQL and the DML as text, so no database is needed.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from server.utils.project_paths import get_project_root

_DML = "data/db/mythos_dev_dml.sql"
_MIGRATION = "data/db/migrations/20260913_arkham_street_grid_dev.sql"
_DDL = "db/mythos_dev_ddl.sql"
_ARKHAM = "earth_arkhamcity_"


def _read(relative: str) -> str:
    return (get_project_root() / relative).read_bytes().decode("utf-8")


@pytest.fixture(scope="module")
def migration() -> str:
    return _read(_MIGRATION)


@pytest.fixture(scope="module")
def arkham_room_ids() -> list[str]:
    text = _read(_DML)
    m = re.search(r"^COPY [\w.]+\.rooms \([^)]*\) FROM stdin;\n", text, re.M)
    assert m
    rows = text[m.end() : text.index("\n\\.", m.end()) + 1].rstrip("\n").split("\n")
    return [r.split("\t")[2] for r in rows if r.split("\t")[2].startswith(_ARKHAM)]


class TestColumnWidths:
    """Room ids are stored as `text` on `rooms`, but referenced from narrower columns."""

    def test_no_room_id_outgrows_a_column_that_stores_one(self, arkham_room_ids: list[str]) -> None:
        ddl = _read(_DDL)
        widths: dict[str, int] = {}
        for m in re.finditer(r"CREATE TABLE mythos_dev\.(\w+) \((.*?)\r?\n\);", ddl, re.S):
            table, body = m.group(1), m.group(2)
            for line in body.splitlines():
                col = re.match(
                    r"\s*(room_id|current_room_id|respawn_room_id) character varying\((\d+)\)",
                    line,
                )
                if col:
                    widths[f"{table}.{col.group(1)}"] = int(col.group(2))

        assert widths, "no varchar column storing a room id was found - has the schema changed?"
        longest = max(arkham_room_ids, key=len)
        too_narrow = {c: w for c, w in widths.items() if w < len(longest)}
        assert not too_narrow, (
            f"the longest Arkham room id is {len(longest)} chars ({longest}), which does not "
            f"fit: {too_narrow}. Widen the column or shorten the id."
        )

    def test_the_migration_widens_the_npc_room_id_column(self, migration: str) -> None:
        assert "ALTER TABLE npc_definitions ALTER COLUMN room_id TYPE character varying(255)" in migration


class TestOrdering:
    def test_exits_are_cleared_before_rooms_are_deleted(self, migration: str) -> None:
        """`room_links.to_room_id` is ON DELETE RESTRICT: a room anything leads to cannot
        be deleted, so the link clear has to come first."""
        clear = migration.index("DELETE FROM room_links")
        drop = migration.index("DELETE FROM rooms")
        assert clear < drop, "rooms are deleted before their inbound exits are cleared"

    def test_every_arkham_exit_is_cleared_not_just_outbound(self, migration: str) -> None:
        """Clearing only `from_room_id` leaves inbound exits from outside Arkham - the
        Innsmouth causeway among them - pointing at rooms about to be replaced."""
        clause = migration[migration.index("DELETE FROM room_links") :][:400]
        assert "from_room_id IN" in clause
        assert "to_room_id" in clause

    def test_the_migration_is_one_transaction(self, migration: str) -> None:
        """A partial application would leave the world half-rebuilt and unwalkable."""
        assert migration.lstrip().splitlines()[0].startswith("--")
        assert "\nBEGIN;" in migration
        assert migration.rstrip().endswith("COMMIT;")


class TestEscaping:
    def test_apostrophes_in_prose_are_doubled(self, migration: str) -> None:
        """Arkham's prose is full of them - "Hangman's Hill", "Ladies' Ward". A single
        unescaped apostrophe terminates the literal and corrupts everything after it."""
        assert "Hangman''s Hill" in migration, "apostrophes are not being escaped"
        assert "'Hangman's Hill'" not in migration

    def test_no_unbalanced_quotes_on_any_value_line(self, migration: str) -> None:
        for i, line in enumerate(migration.splitlines(), 1):
            if not line.startswith("    (") or "--" in line[:6]:
                continue
            assert line.count("'") % 2 == 0, f"line {i} has an odd number of quotes: {line[:90]}"


class TestCoverage:
    def test_the_migration_carries_every_arkham_room_in_the_dml(
        self, migration: str, arkham_room_ids: list[str]
    ) -> None:
        """The migration is generated from the DML; if they drift, a migrated database
        and a freshly seeded one stop agreeing about what Arkham is."""
        missing = [r for r in arkham_room_ids if f"'{r}'" not in migration]
        assert not missing, f"{len(missing)} DML rooms absent from the migration: {missing[:5]}"

    def test_the_landmark_subzones_are_created(self, migration: str) -> None:
        for subzone in (
            "hangmans_hill",
            "wooded_graveyard",
            "old_arkham_graveyard",
            "independence_square",
            "the_island",
        ):
            assert f"'{subzone}'" in migration, f"{subzone} is not created by the migration"

    def test_all_three_environments_have_a_migration(self) -> None:
        for env in ("dev", "unit", "e2e"):
            path = Path(get_project_root() / f"data/db/migrations/20260913_arkham_street_grid_{env}.sql")
            assert path.exists(), f"missing migration for {env}"
            assert f"SET search_path TO mythos_{env};" in path.read_bytes().decode("utf-8")
