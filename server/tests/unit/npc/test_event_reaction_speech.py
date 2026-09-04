"""Unit tests for NPC event reaction speech scheduling (issue #146 MVP)."""

from unittest.mock import MagicMock, patch

from server.events.event_types import NPCAttacked, NPCListened, PlayerEnteredRoom, PlayerLeftRoom
from server.npc.event_reaction_system import (
    NPCEventReaction,
    NPCEventReactionSystem,
    NPCEventReactionTemplates,
)


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


def test_npc_event_reaction_wrong_event_type():
    """should_trigger returns False when event type does not match."""
    reaction = NPCEventReaction(PlayerEnteredRoom, action=lambda _e, _c: True)
    listened = NPCListened(
        npc_id="npc-1",
        room_id="room-a",
        message="hi",
        speaker_id="p1",
        channel="say",
    )
    assert reaction.should_trigger(listened, {}) is False


def test_npc_event_reaction_no_condition_defaults_true():
    """Reactions without a condition trigger for matching event types."""
    reaction = NPCEventReaction(PlayerEnteredRoom, action=lambda _e, _c: True)
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    assert reaction.should_trigger(event, {}) is True


def test_npc_event_reaction_condition_error_returns_false():
    """Condition exceptions are swallowed and should_trigger returns False."""

    def bad_condition(_event: PlayerEnteredRoom, _ctx: dict[str, object]) -> bool:
        raise RuntimeError("condition boom")

    reaction = NPCEventReaction(PlayerEnteredRoom, condition=bad_condition, action=lambda _e, _c: True)
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    assert reaction.should_trigger(event, {}) is False


def test_npc_event_reaction_no_action_returns_true():
    """execute succeeds when no action callback is configured."""
    reaction = NPCEventReaction(PlayerEnteredRoom)
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    assert reaction.execute(event, {}) is True


def test_npc_event_reaction_action_error_returns_false():
    """Action exceptions are swallowed and execute returns False."""

    def bad_action(_event: PlayerEnteredRoom, _ctx: dict[str, object]) -> bool:
        raise RuntimeError("action boom")

    reaction = NPCEventReaction(PlayerEnteredRoom, action=bad_action)
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    assert reaction.execute(event, {}) is False


def test_register_handle_event_and_stats():
    """Registered reactions execute via _handle_event and appear in stats."""
    event_bus = MagicMock()
    system = NPCEventReactionSystem(event_bus)
    executed: list[str] = []

    def action(_event: PlayerEnteredRoom, _ctx: dict[str, object]) -> bool:
        executed.append("ran")
        return True

    reaction = NPCEventReaction(PlayerEnteredRoom, action=action, priority=5)
    system.register_npc_reactions("npc-1", [reaction])
    system.set_npc_context("npc-1", current_room="room-a", name="Morgan")

    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")
    system._handle_event(event)  # pylint: disable=protected-access

    assert executed == ["ran"]
    stats = system.get_npc_reaction_stats("npc-1")
    assert stats["reaction_count"] == 1
    assert stats["total_triggers"] == 1
    assert stats["reactions"][0]["event_type"] == "PlayerEnteredRoom"

    system.unregister_npc_reactions("npc-1")
    assert system.get_npc_reaction_stats("npc-1") == {}


def test_handle_event_respects_cooldown():
    """Second event within cooldown window does not re-run the reaction."""
    event_bus = MagicMock()
    system = NPCEventReactionSystem(event_bus)
    call_count = 0

    def action(_event: PlayerEnteredRoom, _ctx: dict[str, object]) -> bool:
        nonlocal call_count
        call_count += 1
        return True

    system.register_npc_reactions("npc-1", [NPCEventReaction(PlayerEnteredRoom, action=action)])
    system.set_npc_context("npc-1", current_room="room-a")
    event = PlayerEnteredRoom(player_id="p1", room_id="room-a")

    system._handle_event(event)  # pylint: disable=protected-access
    system._handle_event(event)  # pylint: disable=protected-access
    assert call_count == 1


def test_npc_attacked_retaliation_template():
    """Retaliation template triggers only when this NPC is the attack target."""
    reaction = NPCEventReactionTemplates.npc_attacked_retaliation("npc-1")
    matching = NPCAttacked(npc_id="attacker", target_id="npc-1", room_id="room-a", damage=3)
    other = NPCAttacked(npc_id="attacker", target_id="npc-2", room_id="room-a", damage=3)
    ctx: dict[str, object] = {"npc_id": "npc-1"}
    assert reaction.should_trigger(matching, ctx) is True
    assert reaction.should_trigger(other, ctx) is False
    assert reaction.execute(matching, ctx) is True
