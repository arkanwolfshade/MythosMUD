"""Unit tests for NPC event reaction speech scheduling (issue #146 MVP)."""

from unittest.mock import MagicMock, patch

from server.events.event_types import NPCListened, PlayerEnteredRoom, PlayerLeftRoom
from server.npc.event_reaction_system import NPCEventReactionSystem, NPCEventReactionTemplates


def test_greeting_reaction_schedules_npc_speech():
    """PlayerEnteredRoom greeting schedules ChatService NPC say when room matches."""
    reaction = NPCEventReactionTemplates.player_entered_room_greeting("npc-1", "Hello there!")
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    context = {"npc_id": "npc-1", "current_room": "room-a", "name": "Morgan"}

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        assert reaction.should_trigger(event, context) is True
        assert reaction.execute(event, context) is True

    schedule.assert_called_once()
    assert schedule.call_args.kwargs["message"] == "Hello there!"
    assert schedule.call_args.kwargs["npc_name"] == "Morgan"


def test_greeting_reaction_skips_unknown_room():
    """Greeting does not speak when NPC room context is unknown."""
    reaction = NPCEventReactionTemplates.player_entered_room_greeting("npc-1", "Hello")
    event = PlayerEnteredRoom(player_id="p1", room_id="unknown")
    context = {"npc_id": "npc-1", "current_room": "unknown"}

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        assert reaction.execute(event, context) is False
    schedule.assert_not_called()


def test_farewell_and_spoke_reactions_schedule_speech():
    """Farewell and player-spoke responses schedule NPC room speech."""
    farewell = NPCEventReactionTemplates.player_left_room_farewell("npc-1", "Goodbye!")
    left = PlayerLeftRoom(player_id="p1", room_id="room-a")
    context = {"npc_id": "npc-1", "current_room": "room-a", "name": "Morgan"}

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        assert farewell.execute(left, context) is True
    assert schedule.call_args.kwargs["message"] == "Goodbye!"

    spoke = NPCEventReactionTemplates.player_spoke_response("npc-1", "I heard you!")
    listened = NPCListened(
        npc_id="npc-1",
        room_id="room-a",
        message="hi",
        speaker_id="p1",
        channel="say",
    )
    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        assert spoke.should_trigger(listened, context) is True
        assert spoke.execute(listened, context) is True
    assert schedule.call_args.kwargs["message"] == "I heard you!"


def test_set_npc_context_updates_room():
    """Reaction system stores NPC room context for condition checks."""
    system = NPCEventReactionSystem(MagicMock())
    system.set_npc_context("npc-1", current_room="room-b", name="Daisy")
    ctx = system._get_npc_context("npc-1")  # pylint: disable=protected-access
    assert ctx is not None
    assert ctx["current_room"] == "room-b"
    assert ctx["name"] == "Daisy"
    system.clear_npc_context("npc-1")
    assert system._get_npc_context("npc-1")["current_room"] == "unknown"  # pylint: disable=protected-access
