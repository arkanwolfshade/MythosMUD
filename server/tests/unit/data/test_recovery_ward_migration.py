"""Guards the Recovery Ward wing migration (ADR-028, #1079) against authoring mistakes, with no database.

The migration adds a second-floor wing to the Sanitarium (wake-up ward, corridors, a staircase down to the Main Foyer)
and Dr. Morgan's debrief dialogue. This parses the SQL text, like ``test_dml_room_graph`` does for the seed, and checks:
every exit has a reciprocal, a player waking in the ward can walk to the Main Foyer, the wing does not sit on top of
existing rooms on the map, and Morgan's tree validates against the real ``DialogueTree`` schema and drives the
``debrief`` action.
"""

from __future__ import annotations

import json
import re
from collections import deque

from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, RECOVERY_WARD_ROOM_ID
from server.schemas.dialogue import DialogueTree
from server.schemas.scripted_actions import DebriefAction
from server.utils.project_paths import get_project_root

ROOT = get_project_root()
MIGRATION = ROOT / "db" / "migrations" / "20261017120000_recovery_ward_wing.sql"
SEED = ROOT / "data" / "db" / "seed.sql"

_OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east", "up": "down", "down": "up"}
_ROOM_TUPLE = re.compile(
    r"\(\s*'(earth_arkhamcity_sanitarium_room_[a-z0-9_]+)',\s*'([^']+)',.*?(-?\d+\.\d+),\s*(-?\d+\.\d+)\s*\)",
    re.DOTALL,
)
_ROOM_ID = r"'(earth_arkhamcity_sanitarium_room_[a-z0-9_]+)'"
_LINK_ROW = re.compile(r"\(\s*" + _ROOM_ID + r",\s*'(north|south|east|west|up|down)',\s*" + _ROOM_ID + r"\s*\)")
_DIALOGUE = re.compile(r"\$dialogue\$(.*?)\$dialogue\$", re.DOTALL)


def _sections() -> tuple[str, str]:
    text = MIGRATION.read_text(encoding="utf-8")
    up, _, down = text.partition("-- migrate:down")
    return up, down


def _wing_rooms() -> dict[str, tuple[str, float, float]]:
    """stable_id -> (name, map_x, map_y) for the rooms the migration inserts."""
    up, _ = _sections()
    rooms_block = up.split("-- links", 1)[0]
    rooms = {m.group(1): (m.group(2), float(m.group(3)), float(m.group(4))) for m in _ROOM_TUPLE.finditer(rooms_block)}
    assert rooms, "parsed no rooms from the migration: has its layout changed?"
    return rooms


def _links() -> list[tuple[str, str, str]]:
    up, _ = _sections()
    links_block = up.split("-- links", 1)[1]
    links = [(m.group(1), m.group(2), m.group(3)) for m in _LINK_ROW.finditer(links_block)]
    assert links, "parsed no links from the migration: has its layout changed?"
    return links


def _seed_sanitarium_coords() -> set[tuple[float, float]]:
    coords: set[tuple[float, float]] = set()
    in_rooms = False
    for line in SEED.read_text(encoding="utf-8").split("\n"):
        if line.startswith("COPY rooms ("):
            in_rooms = True
        elif in_rooms and line == "\\.":
            break
        elif in_rooms:
            cols = line.split("\t")
            if len(cols) > 7 and "sanitarium" in cols[2] and cols[6] != "\\N":
                coords.add((float(cols[6]), float(cols[7])))
    return coords


def test_the_wake_up_ward_is_the_room_the_constant_names() -> None:
    assert RECOVERY_WARD_ROOM_ID in _wing_rooms()
    assert RECOVERY_WARD_ROOM_ID != DEFAULT_RESPAWN_ROOM


def test_every_exit_has_a_reciprocal() -> None:
    links = set(_links())

    for source, direction, target in links:
        assert (target, _OPPOSITE[direction], source) in links, f"{source} -{direction}-> {target} is one-way"


def test_no_room_has_two_exits_in_the_same_direction() -> None:
    seen = [(source, direction) for source, direction, _ in _links()]

    assert len(seen) == len(set(seen))


def test_every_exit_joins_the_wing_to_itself_or_the_main_foyer() -> None:
    known = set(_wing_rooms()) | {DEFAULT_RESPAWN_ROOM}

    for source, _, target in _links():
        assert source in known
        assert target in known


def test_a_player_waking_in_the_ward_can_walk_to_the_main_foyer() -> None:
    graph: dict[str, list[str]] = {}
    for source, _, target in _links():
        graph.setdefault(source, []).append(target)
    reachable, queue = {RECOVERY_WARD_ROOM_ID}, deque([RECOVERY_WARD_ROOM_ID])
    while queue:
        for nxt in graph.get(queue.popleft(), []):
            if nxt not in reachable:
                reachable.add(nxt)
                queue.append(nxt)

    assert DEFAULT_RESPAWN_ROOM in reachable
    assert set(_wing_rooms()) <= reachable  # nothing in the wing is cut off


def test_the_main_foyer_gets_a_way_up_to_the_wing() -> None:
    foyer_exits = {direction for source, direction, _ in _links() if source == DEFAULT_RESPAWN_ROOM}

    assert foyer_exits == {"up"}


def test_the_wing_does_not_sit_on_top_of_existing_rooms_or_itself() -> None:
    wing_coords = [(x, y) for _, x, y in _wing_rooms().values()]

    assert len(wing_coords) == len(set(wing_coords))
    assert not set(wing_coords) & _seed_sanitarium_coords()


def test_the_down_migration_removes_every_room_it_added() -> None:
    _, down = _sections()

    for stable_id in _wing_rooms():
        assert stable_id in down


def test_the_down_migration_removes_links_into_and_out_of_the_wing_before_its_rooms() -> None:
    """room_links.to_room_id is ON DELETE RESTRICT, so links pointing INTO the wing must go before the rooms do."""
    _, down = _sections()

    link_delete = down.index("DELETE FROM room_links")
    room_delete = down.index("DELETE FROM rooms")
    assert link_delete < room_delete
    link_clause = down[link_delete:room_delete]
    assert "from_room_id" in link_clause
    assert "to_room_id" in link_clause
    for stable_id in _wing_rooms():  # every wing room, not just the one the foyer links to
        assert stable_id in link_clause


def _tree() -> DialogueTree:
    match = _DIALOGUE.search(_sections()[0])
    assert match is not None, "Morgan's dialogue must sit between $dialogue$ markers"
    return DialogueTree.model_validate(json.loads(match.group(1)))


def test_morgans_debrief_tree_validates_against_the_dialogue_schema() -> None:
    tree = _tree()

    assert tree.start == "greeting"


def test_morgan_offers_the_debrief_with_and_without_therapy() -> None:
    tree = _tree()
    debriefs = [a for node in tree.nodes.values() for a in node.actions if isinstance(a, DebriefAction)]

    assert sorted(a.therapy for a in debriefs) == [False, True]
    greeting_targets = {option.next for option in tree.nodes["greeting"].options}
    assert {node_id for node_id, node in tree.nodes.items() if node.actions} <= greeting_targets


def test_the_migration_targets_dr_morgan_and_is_replayable() -> None:
    up, _ = _sections()

    assert "npc_definition_id" in up
    assert "NOT EXISTS" in up  # inserts are guarded so a replay does not duplicate rooms or links
    assert "ON CONFLICT (id) DO UPDATE" in up
