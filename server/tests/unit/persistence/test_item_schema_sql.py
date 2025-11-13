from __future__ import annotations

import json
import sqlite3
from pathlib import Path

EXPECTED_SLOTS = {
    "HEAD",
    "TORSO",
    "LEGS",
    "MAIN_HAND",
    "OFF_HAND",
    "FEET",
    "HANDS",
    "ACCESSORY",
    "RING",
    "AMULET",
    "BELT",
}


def project_path(*parts: str) -> Path:
    return Path(__file__).resolve().parents[4].joinpath(*parts)


def load_sql(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_item_schema_and_seed_scripts_create_expected_artifacts(tmp_path: Path):
    schema_sql = load_sql(project_path("server", "sql", "items_schema.sql"))
    seed_sql = load_sql(project_path("server", "sql", "items_seed_data.sql"))
    db_path = tmp_path / "items.db"

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        connection.executescript(schema_sql)

        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        assert {"item_prototypes", "item_instances", "item_component_states"} <= tables

        indexes = {row["name"]: row for row in connection.execute("PRAGMA index_list('item_instances')")}
        assert "ix_item_instances_owner" in indexes
        assert "ix_item_instances_prototype_id" in indexes

        fk_list = list(connection.execute("PRAGMA foreign_key_list('item_instances')"))
        assert fk_list, "item_instances should include a foreign key to item_prototypes"
        assert fk_list[0]["table"] == "item_prototypes"

        connection.executescript(seed_sql)

        prototype_count = connection.execute("SELECT COUNT(*) FROM item_prototypes").fetchone()[0]
        assert prototype_count == 22

        # Re-running the seed should be idempotent thanks to INSERT OR REPLACE.
        connection.executescript(seed_sql)
        prototype_count_again = connection.execute("SELECT COUNT(*) FROM item_prototypes").fetchone()[0]
        assert prototype_count_again == prototype_count

        slot_totals = dict.fromkeys(EXPECTED_SLOTS, 0)
        for row in connection.execute("SELECT prototype_id, wear_slots FROM item_prototypes"):
            slots = json.loads(row["wear_slots"])
            for slot in slots:
                if slot in slot_totals:
                    slot_totals[slot] += 1
        assert all(count >= 2 for count in slot_totals.values()), slot_totals

        ordered_ids = [
            row["prototype_id"]
            for row in connection.execute("SELECT prototype_id FROM item_prototypes ORDER BY prototype_id")
        ]
        assert ordered_ids == sorted(ordered_ids)
    finally:
        connection.close()
