"""Guards the First Exposure content migration (ADR-028, #1080) against authoring mistakes, with no database.

The migration adds the 12-room tutorial template, its items, NPC definitions, quests and dialogue. This parses the SQL
text, like ``test_dml_room_graph`` does for the seed, and checks the template as a graph and as data: nothing leaves
it, there is exactly one start, the gated stair is reachable only with the amulet the player can find before it,
everything a room or quest names exists, every dialogue and quest validates against the real schemas, and the Hound's
drain really does end at the floor in about a minute and a half.
"""

from __future__ import annotations

import json
import re
import uuid
from collections import deque
from typing import cast

import pytest

from server.app.game_tick_lucidity_drain import LucidityDrainParams
from server.commands.command_service import CommandService
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, RECOVERY_WARD_ROOM_ID
from server.game.first_exposure import EPILOGUE_QUEST_ID, FINISH_ACTIONS
from server.game.player_creation_service import TUTORIAL_TEMPLATE_ID
from server.game.quest.quest_service import _parse_definition  # pyright: ignore[reportPrivateUsage]
from server.schemas.dialogue import DialogueTree
from server.schemas.scripted_actions import (
    ApplyEffectAction,
    NarrateAction,
    QuestActivityAction,
    StartQuestAction,
    on_put_actions,
)
from server.utils.project_paths import get_project_root

ROOT = get_project_root()
MIGRATION = ROOT / "data" / "db" / "migrations" / "20261018120000_first_exposure_tutorial.sql"
CONVERGENCE = ROOT / "data" / "db" / "migrations" / "20261020100000_first_exposure_content_convergence.sql"
ITEM_CATALOG = ROOT / "data" / "item_catalog" / "catalog" / "first_exposure_items.json"
NPC_CATALOG = ROOT / "data" / "npc_catalog" / "catalog" / "first_exposure_npcs.json"

_OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east", "up": "down", "down": "up"}
_ROOM_ID = r"'(earth_arkhamcity_first_exposure_room_[a-z0-9_]+)'"
_ROOM_TUPLE = re.compile(
    r"\(\s*"
    + _ROOM_ID
    + r",\s*'([^']+)',.*?\$room\$\s*(\{.*?\})\s*\$room\$,\s*(?:NULL::text|'interior'),\s*"
    + r"(-?\d+\.\d+),\s*(-?\d+\.\d+)\s*\)",
    re.DOTALL,
)
_LINK_TUPLE = re.compile(r"\(\s*" + _ROOM_ID + r",\s*'(north|south|east|west|up|down)',\s*" + _ROOM_ID + r"\s*\)")
_OFFER = re.compile(r"\('([a-z_]+)',\s*'(room|quest|npc)',\s*'([^']+)'\)")


def _up() -> str:
    return MIGRATION.read_text(encoding="utf-8").partition("-- migrate:down")[0]


def _tagged(tag: str, text: str) -> list[str]:
    return re.findall(rf"\${tag}\$(.*?)\${tag}\$", text, re.DOTALL)


def _base() -> dict[str, object]:
    [raw] = _tagged("base", _up())
    return cast(dict[str, object], json.loads(raw))


def _rooms() -> dict[str, dict[str, object]]:
    """stable_id -> merged attributes (the shared base overlaid with the room's own), plus name and coordinates."""
    base = _base()
    rooms: dict[str, dict[str, object]] = {}
    for match in _ROOM_TUPLE.finditer(_up()):
        attrs = {**base, **cast(dict[str, object], json.loads(match.group(3)))}
        attrs["_name"] = match.group(2)
        attrs["_xy"] = (float(match.group(4)), float(match.group(5)))
        rooms[match.group(1)] = attrs
    assert rooms, "parsed no rooms from the migration: has its layout changed?"
    return rooms


def _links() -> list[tuple[str, str, str]]:
    block = _up().split("-- links", 1)[1].split("-- quests", 1)[0]
    links = [(m.group(1), m.group(2), m.group(3)) for m in _LINK_TUPLE.finditer(block)]
    assert links, "parsed no links from the migration: has its layout changed?"
    return links


def _quests() -> dict[str, dict[str, object]]:
    quests = [cast(dict[str, object], json.loads(raw)) for raw in _tagged("quest", _up())]
    assert quests
    return {cast(str, quest["name"]): quest for quest in quests}


def _offers() -> set[tuple[str, str, str]]:
    block = _up().split("-- offers", 1)[1].split("-- dialogue", 1)[0]
    return {(m.group(1), m.group(2), m.group(3)) for m in _OFFER.finditer(block)}


def _insert_blocks(table: str) -> list[str]:
    """Each ``INSERT INTO <table>`` statement, up to its terminating semicolon at the end of a line."""
    parts = re.split(rf"(?=INSERT INTO {table}\b)", _up())
    return [part.partition(";\n")[0] for part in parts if part.startswith(f"INSERT INTO {table}")]


def _prototype_ids() -> set[str]:
    return {
        m.group(1)
        for block in _insert_blocks("item_prototypes")
        for m in [re.search(r"VALUES \(\s*'([^']+)'", block)]
        if m
    }


def _npc_names() -> set[str]:
    return {
        m.group(1)
        for block in _insert_blocks("npc_definitions")
        for m in [re.search(r"VALUES \(\s*'([^']+)'", block)]
        if m
    }


def _dialogues() -> dict[str, tuple[str, DialogueTree]]:
    """dialogue id -> (npc name, tree) for the dialogues the migration inserts, plus Morgan's update."""
    found: dict[str, tuple[str, DialogueTree]] = {}
    for block in _insert_blocks("dialogue_definitions"):
        dialogue_id = re.search(r"SELECT\s+'([^']+)' AS id", block)
        npc = re.search(r"n\.name = '([^']+)'", block)
        [raw] = _tagged("dialogue", block)
        assert dialogue_id and npc
        found[dialogue_id.group(1)] = (npc.group(1), DialogueTree.model_validate(json.loads(raw)))
    update = _up().split("UPDATE dialogue_definitions", 1)[1]
    [morgan] = _tagged("dialogue", update)
    found["morgan_debrief"] = ("Dr. Francis Morgan", DialogueTree.model_validate(json.loads(morgan)))
    return found


def _start() -> str:
    [start] = [room for room, attrs in _rooms().items() if attrs.get("instance_start") is True]
    return start


def _reachable(*, has_amulet: bool) -> set[str]:
    """Rooms a player can reach from the start, treating a gated exit as shut unless they hold its item."""
    gates: dict[tuple[str, str], str] = {}
    for room, attrs in _rooms().items():
        for direction, rule in cast(dict[str, dict[str, str]], attrs.get("exit_requirements", {})).items():
            gates[(room, direction)] = rule["item"]
    graph: dict[str, list[str]] = {}
    for source, direction, target in _links():
        gate = gates.get((source, direction))
        if gate is None or has_amulet:
            graph.setdefault(source, []).append(target)
    start = _start()
    seen, queue = {start}, deque([start])
    while queue:
        for nxt in graph.get(queue.popleft(), []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


# --- the template as a graph ------------------------------------------------------------------------------------


def test_the_template_has_twelve_rooms_in_the_engines_template() -> None:
    rooms = _rooms()

    assert len(rooms) == 12
    assert {attrs["instance_template_id"] for attrs in rooms.values()} == {TUTORIAL_TEMPLATE_ID} == {"first_exposure"}


def test_exactly_one_room_is_the_instance_start() -> None:
    starts = [room for room, attrs in _rooms().items() if attrs.get("instance_start") is True]

    assert len(starts) == 1


def test_nothing_leaves_the_template() -> None:
    rooms = set(_rooms())

    for source, direction, target in _links():
        assert source in rooms, f"{source} is not a template room"
        assert target in rooms, f"{source} -{direction}-> {target} leaves the tutorial"


def test_every_exit_has_a_reciprocal_and_no_direction_repeats() -> None:
    links = _links()

    assert len({(source, direction) for source, direction, _ in links}) == len(links)
    for source, direction, target in set(links):
        assert (target, _OPPOSITE[direction], source) in set(links), f"{source} -{direction}-> {target} is one-way"


def test_the_template_does_not_sit_on_top_of_itself_on_the_map() -> None:
    coords = [attrs["_xy"] for attrs in _rooms().values()]

    assert len(coords) == len(set(coords))


def test_every_room_is_safe_to_lose_in_and_leaves_through_the_ward_with_no_passive_corruption() -> None:
    for room, attrs in _rooms().items():
        assert attrs["no_death"] is True, room
        assert attrs["is_instanced"] is True, room
        assert attrs["corruption_rate"] == 0, room
        assert attrs["instance_exit_room_id"] == RECOVERY_WARD_ROOM_ID, room


def test_combat_is_allowed_only_in_the_room_with_the_hostile_ghoul() -> None:
    rooms = _rooms()
    fighting = [room for room, attrs in rooms.items() if attrs["no_combat"] is False]

    assert len(fighting) == 1
    assert rooms[fighting[0]]["instance_npcs"] == ["Ragged Ghoul"]


# --- the gated stair and the amulet -----------------------------------------------------------------------------


def test_the_stair_down_is_gated_on_the_amulet_the_player_can_find_before_it() -> None:
    rooms = _rooms()
    gates = {
        room: cast(dict[str, dict[str, str]], attrs["exit_requirements"])
        for room, attrs in rooms.items()
        if "exit_requirements" in attrs
    }
    [(stair, rule)] = gates.items()
    amulet = rule["down"]["item"]
    amulet_rooms = [
        room
        for room, attrs in rooms.items()
        if any(entry["prototype_id"] == amulet for entry in cast(list[dict[str, object]], attrs.get("items", [])))
    ]

    assert "empty hands" in rule["down"]["refusal"]
    [amulet_room] = amulet_rooms
    assert amulet_room in _reachable(has_amulet=False)
    assert stair in _reachable(has_amulet=False)


def test_the_vault_is_unreachable_without_the_amulet_and_reachable_with_it() -> None:
    [vault] = [room for room, attrs in _rooms().items() if "furniture" in attrs]

    assert vault not in _reachable(has_amulet=False)
    assert vault in _reachable(has_amulet=True)
    assert set(_rooms()) == _reachable(has_amulet=True)  # nothing is cut off once the stair opens


# --- everything named exists ------------------------------------------------------------------------------------


def test_every_prototype_a_room_names_exists() -> None:
    known = _prototype_ids()
    named: set[str] = set()
    for attrs in _rooms().values():
        named |= {entry["prototype_id"] for entry in cast(list[dict[str, str]], attrs.get("items", []))}
        named |= {entry["prototype_id"] for entry in cast(list[dict[str, str]], attrs.get("furniture", []))}
        for rule in cast(dict[str, dict[str, str]], attrs.get("exit_requirements", {})).values():
            named.add(rule["item"])

    assert named
    assert named <= known


def test_every_npc_a_room_spawns_exists_as_an_inert_definition() -> None:
    known = _npc_names()
    spawned = {name for attrs in _rooms().values() for name in cast(list[str], attrs.get("instance_npcs", []))}

    assert spawned == known == {"Lamplighter", "Ragged Ghoul", "Pale Ghoul"}
    for block in _insert_blocks("npc_definitions"):
        assert "NULL,\n    FALSE,\n    0,\n    0.0," in block, (
            "instance NPCs must have no room, no spawn and no population"
        )


def test_the_amulet_and_the_newspaper_die_with_the_instance() -> None:
    for block in _insert_blocks("item_prototypes"):
        if "quest.first_exposure" in block:
            assert "INSTANCE_BOUND" in block


# --- quests -----------------------------------------------------------------------------------------------------


def test_the_four_quests_chain_dusk_to_burying_ground_to_below_and_the_epilogue_stands_alone() -> None:
    quests = _quests()

    assert set(quests) == {
        "first_exposure_dusk",
        "first_exposure_burying_ground",
        "first_exposure_below",
        EPILOGUE_QUEST_ID,
    }
    assert quests["first_exposure_dusk"]["requires_all"] == []
    assert quests["first_exposure_burying_ground"]["requires_all"] == ["first_exposure_dusk"]
    assert quests["first_exposure_below"]["requires_all"] == ["first_exposure_burying_ground"]
    epilogue = quests[EPILOGUE_QUEST_ID]
    assert epilogue["requires_all"] == [] and epilogue["requires_any"] == []
    assert epilogue["triggers"] == []  # only ever started by the ending, so skip and restart work


def test_every_quest_validates_against_the_real_definition_schema() -> None:
    for quest in _quests().values():
        _ = _parse_definition(quest)


def test_every_trigger_has_a_matching_offer_and_dusk_starts_in_the_start_room() -> None:
    offers = _offers()
    for quest_id, quest in _quests().items():
        for trigger in cast(list[dict[str, str]], quest["triggers"]):
            assert (quest_id, trigger["type"], trigger["entity_id"]) in offers
    assert ("first_exposure_dusk", "room", _start()) in offers
    assert ("first_exposure_burying_ground", "quest", "first_exposure_dusk") in offers
    assert ("first_exposure_below", "quest", "first_exposure_burying_ground") in offers


def test_every_goal_can_actually_be_completed() -> None:
    commands = set(CommandService().command_handlers)
    rooms = set(_rooms())
    debrief_targets = {
        action.target
        for _, tree in _dialogues().values()
        for node in tree.nodes.values()
        for action in node.actions
        if isinstance(action, QuestActivityAction)
    }
    for quest in _quests().values():
        for goal in cast(list[dict[str, object]], quest["goals"]):
            target = cast(str, goal["target"])
            if goal["type"] == "collect_n":
                assert target in _prototype_ids()
            elif target.startswith("cmd_"):
                assert target.removeprefix("cmd_") in commands, f"no such command: {target}"
            elif target.startswith("exit_"):
                assert target.removeprefix("exit_") in rooms, f"no such room: {target}"
            else:
                assert target in debrief_targets, f"nothing records activity {target}"


def test_the_epilogue_is_the_quest_the_ending_starts_and_it_rewards_the_sanitarium_respawn() -> None:
    [start_action] = [action for action in FINISH_ACTIONS if isinstance(action, StartQuestAction)]
    rewards = cast(list[dict[str, object]], _quests()[EPILOGUE_QUEST_ID]["rewards"])

    assert start_action.quest_id == EPILOGUE_QUEST_ID
    assert {"type": "respawn_room", "config": {"room_id": DEFAULT_RESPAWN_ROOM}} in rewards


def test_journal_text_tells_the_player_the_commands_to_type() -> None:
    """The fallback for the player who stalls is the journal: each quest must say what to type."""
    for quest in _quests().values():
        assert "'" in cast(str, quest["description"]), quest["name"]


# --- dialogue ---------------------------------------------------------------------------------------------------


def test_every_dialogue_belongs_to_an_npc_that_exists() -> None:
    dialogues = _dialogues()

    assert set(dialogues) == {"first_exposure_lamplighter", "first_exposure_pale_ghoul", "morgan_debrief"}
    for dialogue_id, (npc, _) in dialogues.items():
        assert npc in _npc_names() | {"Dr. Francis Morgan"}, dialogue_id


def test_the_pale_ghoul_heals_over_time_raises_corruption_to_the_floor_and_sends_the_player_for_the_amulet() -> None:
    _, tree = _dialogues()["first_exposure_pale_ghoul"]
    actions = tree.nodes["mend"].actions
    heal = [a for a in actions if isinstance(a, ApplyEffectAction)]

    assert [a.effect["type"] for a in heal] == ["heal_over_time"]
    assert any(a.type == "corruption_at_least" and a.value == 1 for a in actions)  # a floor, never "+1"
    assert "amulet" not in tree.nodes["greeting"].text  # the errand comes after the mending, as a choice
    assert "jade" in tree.nodes["amulet"].text or "green stone" in tree.nodes["amulet"].text


def test_morgans_debrief_still_debriefs_and_now_completes_the_epilogue() -> None:
    _, tree = _dialogues()["morgan_debrief"]

    for node_id in ("debrief", "debrief_therapy"):
        types = [action.type for action in tree.nodes[node_id].actions]
        assert types == ["debrief", "quest_activity"]


# --- the Hound --------------------------------------------------------------------------------------------------


def _coffin_actions() -> list[object]:
    [vault] = [attrs for attrs in _rooms().values() if "furniture" in attrs]
    [coffin] = cast(list[dict[str, object]], vault["furniture"])
    [amulet] = [item for item in _prototype_ids() if item.endswith("jade_amulet")]
    return list(on_put_actions({"on_put": coffin["on_put"]}, amulet))


def test_putting_the_amulet_in_the_coffin_starts_the_hound() -> None:
    actions = _coffin_actions()

    assert isinstance(actions[0], NarrateAction)
    [effect] = [a for a in actions if isinstance(a, ApplyEffectAction)]
    assert effect.effect["type"] == "lucidity_drain_over_time"
    assert effect.effect["instance_scoped"] is True  # a restart or the ending strips it
    assert effect.effect["grants_liabilities"] is False


def test_the_hounds_drain_validates_and_lands_on_delirium_in_about_ninety_seconds() -> None:
    [effect] = [a for a in _coffin_actions() if isinstance(a, ApplyEffectAction)]
    params = LucidityDrainParams.model_validate(effect.effect)

    lcd, seconds = 100, 0
    while lcd > params.floor:
        lcd -= min(
            LucidityDrainParams.model_validate({**effect.effect, "elapsed": seconds}).rate_now(), lcd - params.floor
        )
        seconds += 1
    assert params.floor == -10
    assert 70 <= seconds <= 100  # rapid but not immediate, and always finite
    assert all(line.at < seconds for line in params.narration)  # every beat fires before the end
    assert [line.at for line in params.narration] == sorted(line.at for line in params.narration)


# --- the pipeline and the code agree ----------------------------------------------------------------------------

_HAVE_DATA = ITEM_CATALOG.is_file() and NPC_CATALOG.is_file()


@pytest.mark.skipif(not _HAVE_DATA, reason="the private data/ submodule is not checked out")
def test_the_latest_item_rows_embed_exactly_what_the_item_pipeline_generates() -> None:
    """The convergence migration restates the items (adding keywords, #1106); it is current, the original is not."""
    text = CONVERGENCE.read_text(encoding="utf-8").partition("-- migrate:down")[0]
    for row in cast(list[dict[str, object]], json.loads(ITEM_CATALOG.read_text(encoding="utf-8"))):
        assert f"'{row['prototype_id']}'" in text
        for key in ("flags", "stacking_rules", "metadata", "tags"):
            literal = json.dumps(row[key], separators=(",", ":")).replace("'", "''")
            assert f"'{literal}'::jsonb" in text, f"{row['prototype_id']}.{key} drifted from the catalog"


@pytest.mark.skipif(not _HAVE_DATA, reason="the private data/ submodule is not checked out")
def test_the_migration_embeds_exactly_what_the_npc_pipeline_generates() -> None:
    from server.game.npcs.catalog_dml import prepare_npc_definition

    text = _up()
    for raw in cast(list[dict[str, object]], json.loads(NPC_CATALOG.read_text(encoding="utf-8"))):
        prepared = prepare_npc_definition(raw)
        for key in ("base_stats", "behavior_config"):
            literal = json.dumps(prepared[key], separators=(",", ":")).replace("'", "''")
            assert f"'{literal}'" in text, f"{prepared['name']}.{key} drifted from the catalog"


def test_the_hostile_ghoul_disengages_at_a_valid_ratio_and_the_unwinnable_fight_cannot_kill() -> None:
    from server.models.combat import CombatParticipant, CombatParticipantType
    from server.services.combat_npc_disengage import disengage_ratio

    text = _up()
    match = re.search(r'"disengage_at_target_dp_ratio":([0-9.]+)', text)
    assert match is not None
    ghoul = CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="Ragged Ghoul",
        current_dp=150,
        max_dp=150,
        dexterity=55,
        npc_behavior_config={"disengage_at_target_dp_ratio": float(match.group(1))},
    )

    assert disengage_ratio(ghoul) == 0.25


def test_the_old_tutorial_is_retired_and_its_players_are_moved_somewhere_real() -> None:
    up = _up()

    assert "DELETE FROM quest_definitions\nWHERE id = 'leave_the_tutorial'" in up
    assert "DELETE FROM rooms\nWHERE stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001'" in up
    assert f"SET current_room_id = '{RECOVERY_WARD_ROOM_ID}'" in up
    assert f"SET respawn_room_id = '{DEFAULT_RESPAWN_ROOM}'" in up
    assert "NOT EXISTS" in up  # guarded inserts: a replay does not duplicate rooms or links
