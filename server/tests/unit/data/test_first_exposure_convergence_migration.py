"""Guards the First Exposure convergence migration (#1106) with no database.

``20261020100000_first_exposure_content_convergence.sql`` restates the tutorial content of the original migration so a
database that applied a since-edited draft ends up identical to a fresh one. It is generated from the original, so
these tests keep the two in step (a hand edit to one without the other fails here) and check the one thing it adds:
the Arkham Advertiser's keywords. They also check the player-facing promise behind #1106: every ``get``/``read``/
``talk`` the quest text tells the player to type finds something, through the same matchers the commands use.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import cast

import pytest
from pydantic import BaseModel, TypeAdapter

from server.commands.inventory_item_matching import match_room_drop_by_name
from server.utils.project_paths import get_project_root

ROOT = get_project_root()
ORIGINAL = ROOT / "data" / "db" / "migrations" / "20261018120000_first_exposure_tutorial.sql"
CONVERGENCE = ROOT / "data" / "db" / "migrations" / "20261020100000_first_exposure_content_convergence.sql"
ITEM_CATALOG = ROOT / "data" / "item_catalog" / "catalog" / "first_exposure_items.json"
NPC_CATALOG = ROOT / "data" / "npc_catalog" / "catalog" / "first_exposure_npcs.json"

needs_data = pytest.mark.skipif(
    not (ITEM_CATALOG.is_file() and NPC_CATALOG.is_file()), reason="the private data/ submodule is not checked out"
)

ADVERTISER = "quest.first_exposure.arkham_advertiser"
KEYWORDS = '"keywords":["newspaper","paper","advertiser"],'


def _up(path: Path) -> str:
    return path.read_text(encoding="utf-8").partition("-- migrate:down")[0]


def _between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def _tagged(tag: str, text: str) -> list[str]:
    return re.findall(rf"\${tag}\$(.*?)\${tag}\$", text, re.DOTALL)


def test_rooms_quests_and_dialogue_are_the_originals_word_for_word() -> None:
    new, old = _up(CONVERGENCE), _up(ORIGINAL)

    for tag in ("base", "room", "quest", "dialogue"):
        assert _tagged(tag, new) == _tagged(tag, old), f"${tag}$ blocks drifted from the original migration"
    assert _between(new, "CROSS JOIN (VALUES", ") AS v (stable_id") == _between(
        old, "CROSS JOIN (VALUES", ") AS v (stable_id"
    )
    assert _between(new, "-- offers", "-- dialogue") == _between(old, "-- offers", "-- dialogue")


def test_items_and_npcs_are_the_originals_plus_the_advertiser_keywords() -> None:
    new, old = _up(CONVERGENCE), _up(ORIGINAL)
    start, end = "-- noqa: disable=LT05", "-- noqa: enable=LT05"

    assert new.count(KEYWORDS) == 1
    assert _between(new, start, end).replace(KEYWORDS, "") == _between(old, start, end)


def test_rooms_are_upserted_and_nothing_else_is_touched() -> None:
    new = _up(CONVERGENCE)

    assert "ON CONFLICT (subzone_id, stable_id) DO UPDATE SET" in new
    assert "NOT EXISTS" not in new  # the original's insert-if-missing guard would leave drifted rooms alone
    # Links belong to the one-way path (#1111); the retirement of the old bedroom already ran.
    assert not re.search(r"\b(room_links|DELETE|players)\b", new)


@needs_data
def test_the_catalog_and_the_migration_agree_on_the_keywords() -> None:
    catalog = cast(list[dict[str, object]], json.loads(ITEM_CATALOG.read_text(encoding="utf-8")))
    [advertiser] = [item for item in catalog if item["prototype_id"] == ADVERTISER]
    from_catalog = cast(dict[str, object], advertiser["metadata"])["keywords"]

    assert from_catalog == json.loads(f"{{{KEYWORDS.rstrip(',')}}}")["keywords"]


def _catalog_stacks() -> list[dict[str, object]]:
    catalog = cast(list[dict[str, object]], json.loads(ITEM_CATALOG.read_text(encoding="utf-8")))
    return [
        {
            "item_name": item["name"],
            "item_id": item["prototype_id"],
            "prototype_id": item["prototype_id"],
            "metadata": item["metadata"],
        }
        for item in catalog
    ]


def _npc_stacks() -> list[dict[str, object]]:
    """The tutorial's NPCs plus Dr. Morgan, who lives in the base world's Sanitarium, not in this catalog."""
    names = [npc["name"] for npc in cast(list[dict[str, str]], json.loads(NPC_CATALOG.read_text(encoding="utf-8")))]
    return [{"item_name": name} for name in [*names, "Dr. Francis Morgan"]]


def _hints() -> list[tuple[str, str]]:
    """(verb, target) for every `get|read|talk|put <target>` the quest text puts in quotes."""
    text = " ".join(cast(str, json.loads(raw)["description"]) for raw in _tagged("quest", _up(CONVERGENCE)))
    found = re.findall(r"'(get|read|talk|put) ([a-z][a-z' -]*?)(?: in [a-z ]+)?'", text)
    assert found, "parsed no command hints from the quest descriptions: has their wording changed?"
    return found


@needs_data
@pytest.mark.parametrize(("verb", "target"), _hints())
def test_every_command_the_quest_text_suggests_finds_its_target(verb: str, target: str) -> None:
    """The player types what the quest says, so each hint must resolve to an item or NPC the tutorial really has."""
    stacks = _npc_stacks() if verb == "talk" else _catalog_stacks()

    assert match_room_drop_by_name(stacks, target) is not None, f"'{verb} {target}' finds nothing"


GHOUL_MEND = ROOT / "data" / "db" / "migrations" / "20261020110000_pale_ghoul_mend_single_option.sql"


@pytest.mark.skipif(not GHOUL_MEND.is_file(), reason="the private data/ submodule is not checked out")
def test_the_ghoul_mend_node_keeps_one_answer_that_continues_the_scene_and_down_restores_the_original() -> None:
    """#1107: "Thank you." ended the talk before the quest hand-off; the migration is targeted and reversible."""
    original = [json.loads(block) for block in _tagged("dialogue", _up(ORIGINAL)) if '"mend"' in block]
    assert len(original) == 1
    nodes = cast(dict[str, dict[str, object]], original[0]["nodes"])
    up, _, down = GHOUL_MEND.read_text(encoding="utf-8").partition("-- migrate:down")

    options = TypeAdapter(list[dict[str, str | None]])
    kept = options.validate_json("[" + _between(up, "'[", "]'::jsonb") + "]")
    restored = options.validate_json("[" + _between(down, "'[", "]'::jsonb") + "]")

    assert kept == [{"label": "What do you want from me?", "next": "amulet"}]
    assert kept[0]["next"] in nodes
    assert restored == nodes["mend"]["options"]
    assert "jsonb_set" in up and "first_exposure_pale_ghoul" in up


GOAL_DESCRIPTIONS = ROOT / "data" / "db" / "migrations" / "20261021100000_first_exposure_goal_descriptions.sql"


class _Quest(BaseModel):
    name: str
    goals: list[dict[str, object]]


def _statement_for(sql: str, quest_id: str) -> str:
    return next(statement for statement in sql.split(";") if f"id = '{quest_id}'" in statement)


def _goal_indexes(statement: str) -> set[int]:
    return {int(part.split(",")[0]) for part in statement.split("{goals,")[1:] if ",description}" in part}


@pytest.mark.skipif(not GOAL_DESCRIPTIONS.is_file(), reason="the private data/ submodule is not checked out")
def test_every_first_exposure_goal_gets_a_player_facing_description_and_down_removes_them() -> None:
    """#1102: the journal showed `cmd_talk: 0/1`; every goal of every tutorial quest now has authored text."""
    quests = [_Quest.model_validate_json(block) for block in _tagged("quest", _up(CONVERGENCE))]
    up, _, down = GOAL_DESCRIPTIONS.read_text(encoding="utf-8").partition("-- migrate:down")

    assert len(quests) == 4
    for quest in quests:
        every_goal = set(range(len(quest.goals)))
        written = _statement_for(up, quest.name)
        assert _goal_indexes(written) == every_goal, f"{quest.name}: every goal needs a description"
        assert len(re.findall(r"'\"[^\"]+\"'::jsonb", written)) == len(every_goal), f"{quest.name}: empty text"
        assert _goal_indexes(_statement_for(down, quest.name)) == every_goal, f"{quest.name}: down must remove them"
