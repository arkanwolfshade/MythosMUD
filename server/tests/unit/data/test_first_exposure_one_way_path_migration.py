"""Guards the First Exposure one-way path migration (#1111) with no database.

``20261021110000_first_exposure_one_way_path.sql`` removes the back-links of the twelve-room tutorial and gates the
exits forward on the step each room teaches. These tests rebuild the finished graph from the original migration plus
that one and check what the design promises: a single line from the square to the Vault, no way back, every gate on
an exit that exists, and every gate openable by something the tutorial actually asks the player to do.
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from pathlib import Path

import pytest
from pydantic import BaseModel, TypeAdapter

from server.utils.project_paths import get_project_root

ROOT = get_project_root()
MIGRATIONS = ROOT / "data" / "db" / "migrations"
ORIGINAL = MIGRATIONS / "20261018120000_first_exposure_tutorial.sql"
ONE_WAY = MIGRATIONS / "20261021110000_first_exposure_one_way_path.sql"

pytestmark = pytest.mark.skipif(
    not (ORIGINAL.is_file() and ONE_WAY.is_file()), reason="the private data/ submodule is not checked out"
)

PREFIX = "earth_arkhamcity_first_exposure_room_"
SQUARE, VAULT = f"{PREFIX}independence_square_001", f"{PREFIX}vault_of_the_owner_001"
AMULET = "quest.first_exposure.jade_amulet"

Gate = dict[str, dict[str, str]]


class _Quest(BaseModel):
    name: str
    goals: list[dict[str, object]]


def _up(path: Path) -> str:
    return path.read_text(encoding="utf-8").partition("-- migrate:down")[0]


def _between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def _original_links() -> list[tuple[str, str, str]]:
    block = _between(_up(ORIGINAL), "INSERT INTO room_links", ") AS v (from_stable")
    pattern = re.compile(rf"\(\s*'(?P<src>{PREFIX}\w+)',\s*'(?P<dir>\w+)',\s*'(?P<dst>{PREFIX}\w+)'\s*\)")
    return [(m["src"], m["dir"], m["dst"]) for m in pattern.finditer(block)]


def _removed() -> set[tuple[str, str]]:
    block = _between(_up(ONE_WAY), "AND (f.stable_id, l.direction) IN (", ");")
    return {(m["src"], m["dir"]) for m in re.finditer(rf"\('(?P<src>{PREFIX}\w+)', '(?P<dir>\w+)'\)", block)}


def _remaining() -> dict[str, dict[str, str]]:
    """room -> {direction: destination} once the back-links are gone."""
    removed = _removed()
    graph: dict[str, dict[str, str]] = {}
    for src, direction, dst in _original_links():
        if (src, direction) not in removed:
            graph.setdefault(src, {})[direction] = dst
    return graph


def _gates() -> dict[str, Gate]:
    adapter = TypeAdapter(dict[str, dict[str, str]])
    block = _between(_up(ONE_WAY), "SET attributes = r.attributes", ") AS v (stable_id, requirements)")
    pairs = re.finditer(rf"'(?P<room>{PREFIX}\w+)',\s*\$req\$(?P<json>.*?)\$req\$", block, re.DOTALL)
    return {m["room"]: adapter.validate_json(m["json"]) for m in pairs}


def _retargets() -> dict[tuple[str, int], str]:
    """(quest id, goal index) -> the new target."""
    pattern = re.compile(
        r"'\{goals,(?P<i>\d+),target\}', '\"(?P<target>\w+)\"'::jsonb\),\s*updated_at = now\(\)\s*WHERE id = '(?P<q>\w+)'"
    )
    return {(m["q"], int(m["i"])): m["target"] for m in pattern.finditer(_up(ONE_WAY))}


def _goal_targets() -> set[str]:
    blocks = re.finditer(r"\$quest\$(?P<json>.*?)\$quest\$", _up(ORIGINAL), re.DOTALL)
    quests = [_Quest.model_validate_json(m["json"]) for m in blocks]
    retargets = _retargets()
    return {
        retargets.get((q.name, i), str(goal["target"]))
        for q in quests
        for i, goal in enumerate(q.goals)
        if goal["type"] == "complete_activity"
    }


def _fired_by_dialogue() -> set[str]:
    return set(re.findall(r'"type": "quest_activity", "target": "(\w+)"', _up(ONE_WAY)))


def _line_from(start: str, graph: dict[str, dict[str, str]]) -> Iterator[str]:
    room = start
    while True:
        yield room
        exits = graph.get(room, {})
        assert len(exits) <= 1, f"{room} must have one way on, has {sorted(exits)}"
        if not exits:
            return
        room = next(iter(exits.values()))


def test_the_tutorial_is_a_single_line_from_the_square_to_the_vault_with_no_way_back() -> None:
    graph = _remaining()
    path = list(_line_from(SQUARE, graph))

    assert path[0] == SQUARE
    assert path[-1] == VAULT
    assert len(path) == len(set(path)) == 12  # twelve distinct rooms, none revisited
    assert all(len(graph[room]) == 1 for room in path[:-1]), "every room before the Vault has a forward exit"
    assert VAULT not in graph, "the Vault is the end of the line"


def test_every_back_link_that_is_removed_really_leads_to_an_earlier_room() -> None:
    """Guards the DELETE list: it must remove only links that go back up the line, never a forward link."""
    original = _original_links()
    order = {room: i for i, room in enumerate(_line_from(SQUARE, _remaining()))}

    for src, direction in _removed():
        (dst,) = {d for s, dr, d in original if (s, dr) == (src, direction)}
        assert order[dst] < order[src], f"{src} {direction} -> {dst} is not a way back"


def test_every_gate_is_on_an_exit_that_exists_and_has_a_refusal() -> None:
    graph = _remaining()
    for room, gate in _gates().items():
        for direction, rule in gate.items():
            assert direction in graph[room], f"{room} gates {direction}, which is not an exit"
            assert rule.get("refusal"), f"{room} {direction}: a gate explains itself"
            assert rule.keys() <= {"item", "quest_activity", "refusal"}, f"{room} {direction}: unknown condition"


def test_every_quest_gate_opens_with_a_step_the_tutorial_asks_for() -> None:
    """A gate on an activity nothing records would be a soft-lock: check each target has a goal and a source."""
    goal_targets = _goal_targets()
    fired = _fired_by_dialogue()

    for room, gate in _gates().items():
        for rule in gate.values():
            target = rule.get("quest_activity")
            if target is None:
                continue
            assert target in goal_targets, f"{room}: no quest goal listens for {target}"
            assert target.startswith("cmd_") or target in fired, f"{room}: nothing fires {target}"


def test_the_talk_goals_now_complete_with_the_conversation_not_the_greeting() -> None:
    assert _retargets() == {
        ("first_exposure_dusk", 1): "dialogue_complete_lamplighter",
        ("first_exposure_burying_ground", 0): "dialogue_complete_pale_ghoul",
    }
    assert _fired_by_dialogue() == {"dialogue_complete_lamplighter", "dialogue_complete_pale_ghoul"}


def test_the_amulet_gate_moves_to_the_grave_so_the_stair_cannot_strand_anyone() -> None:
    gates = _gates()
    grave = gates[f"{PREFIX}robbed_grave_001"]

    assert grave["south"]["item"] == AMULET
    assert f"{PREFIX}mausoleum_stair_001" not in gates
    assert f"SET attributes = attributes - 'exit_requirements'\nWHERE stable_id = '{PREFIX}mausoleum_stair_001'" in _up(
        ONE_WAY
    )


def test_the_gates_cover_the_steps_the_tutorial_teaches() -> None:
    wanted = {
        f"{PREFIX}independence_square_001": "cmd_look",
        f"{PREFIX}gravel_walk_001": "dialogue_complete_lamplighter",
        f"{PREFIX}beneath_the_limes_001": "cmd_read",
        f"{PREFIX}old_yew_001": "dialogue_complete_pale_ghoul",
    }
    gates = _gates()

    assert {room: gates[room]["east"]["quest_activity"] for room in wanted} == wanted
