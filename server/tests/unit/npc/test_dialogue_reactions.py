"""NPCs that speak first: a player entering the room makes the NPC open its dialogue (initiates_dialogue)."""

from typing import cast
from unittest.mock import MagicMock, patch

from server.events.event_bus import EventBus
from server.events.event_types import NPCOpensDialogue, PlayerEnteredRoom
from server.npc.dialogue_reactions import build_dialogue_opening
from server.npc.npc_default_reactions import register_default_reactions_for_npc


class _RecordingBus:
    def __init__(self) -> None:
        self.events: list[object] = []

    def publish(self, event: object) -> None:
        self.events.append(event)


def test_a_player_entering_the_npcs_room_asks_for_the_dialogue_to_open() -> None:
    bus = _RecordingBus()
    reaction = build_dialogue_opening("ghoul-1", cast(EventBus, cast(object, bus)))
    event = PlayerEnteredRoom(player_id="p1", room_id="yew")
    context: dict[str, object] = {"current_room": "yew", "name": "Pale Ghoul"}

    assert reaction.event_type is PlayerEnteredRoom
    assert reaction.condition is not None and reaction.condition(event, context)
    assert reaction.action is not None and reaction.action(event, context)

    [opened] = bus.events
    assert isinstance(opened, NPCOpensDialogue)
    assert (opened.npc_id, opened.npc_name, opened.room_id, opened.player_id) == ("ghoul-1", "Pale Ghoul", "yew", "p1")


def test_a_player_entering_another_room_is_ignored() -> None:
    reaction = build_dialogue_opening("ghoul-1", cast(EventBus, cast(object, _RecordingBus())))
    assert reaction.condition is not None
    assert not reaction.condition(PlayerEnteredRoom(player_id="p1", room_id="square"), {"current_room": "yew"})


def test_initiates_dialogue_replaces_the_greeting_instead_of_adding_to_it() -> None:
    """Only the first matching reaction runs, so the opening must stand in for the greeting."""
    bus = MagicMock()
    system = MagicMock(event_bus=bus)
    with (
        patch("server.npc.dialogue_reactions.build_dialogue_opening") as opening,
        patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as greeting,
    ):
        register_default_reactions_for_npc("ghoul-1", "passive_mob", {"initiates_dialogue": True}, system)

    opening.assert_called_once_with("ghoul-1", bus)
    greeting.assert_not_called()


def test_without_the_flag_the_npc_still_greets() -> None:
    system = MagicMock()
    with (
        patch("server.npc.dialogue_reactions.build_dialogue_opening") as opening,
        patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as greeting,
    ):
        register_default_reactions_for_npc("npc-1", "passive_mob", {"greeting_message": "Hi"}, system)

    opening.assert_not_called()
    greeting.assert_called_once()
