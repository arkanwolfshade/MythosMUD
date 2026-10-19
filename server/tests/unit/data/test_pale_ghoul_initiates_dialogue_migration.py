"""The Pale Ghoul speaks first: the migration and the NPC catalog it mirrors agree on initiates_dialogue."""

import json
from pathlib import Path
from typing import cast

REPO_ROOT = Path(__file__).resolve().parents[4]
MIGRATION = REPO_ROOT / "db" / "migrations" / "20261018140000_pale_ghoul_initiates_dialogue.sql"
CATALOG = REPO_ROOT / "data" / "npc_catalog" / "catalog" / "first_exposure_npcs.json"


def _sections() -> tuple[str, str]:
    text = MIGRATION.read_text(encoding="utf-8")
    up, down = text.split("-- migrate:down")
    return up.split("-- migrate:up")[1], down


def test_up_sets_the_flag_on_the_pale_ghoul_only() -> None:
    up, _ = _sections()
    assert "'{\"initiates_dialogue\": true}'::jsonb" in up
    assert "WHERE name = 'Pale Ghoul' AND sub_zone_id = 'arena'" in up


def test_down_removes_only_that_key() -> None:
    _, down = _sections()
    assert "behavior_config::jsonb - 'initiates_dialogue'" in down
    assert "WHERE name = 'Pale Ghoul' AND sub_zone_id = 'arena'" in down


def test_the_catalog_carries_the_same_flag() -> None:
    npcs = cast(list[dict[str, object]], json.loads(CATALOG.read_text(encoding="utf-8")))
    [ghoul] = [npc for npc in npcs if npc["name"] == "Pale Ghoul"]
    assert ghoul["behavior_config"] == {"initiates_dialogue": True}
