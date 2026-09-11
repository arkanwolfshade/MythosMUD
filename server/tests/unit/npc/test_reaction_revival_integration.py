"""
Integration-shape unit tests for the NPC reaction system revival (#815).

Before this round, `_build_shopkeeper`/`_build_passive`/`_build_aggressive`
(server/npc/spawning_instance_factory.py) hardcoded `event_reaction_system=None`, so a real
`NPCBase` subclass with a live `NPCEventReactionSystem` -- greeting on room entry, farewell on
room exit, per-NPC cooldown -- could never be exercised end-to-end; only the templates in
isolation (test_event_reaction_speech.py) or the registration counts
(test_npc_default_reactions.py) were testable. These tests exercise the whole path a real spawn
now takes: EventBus -> NPCEventReactionSystem -> NPCBase.__init__ -> registered reactions ->
publish -> schedule_npc_room_speech.
"""

from __future__ import annotations

import uuid
from unittest.mock import patch

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.npc.event_reaction_system import NPCEventReactionSystem
from server.npc.shopkeeper_npc import ShopkeeperNPC
from server.npc.spawning_models import SimpleNPCDefinition


def _shopkeeper(event_bus: EventBus, reaction_system: NPCEventReactionSystem, room_id: str) -> ShopkeeperNPC:
    definition = SimpleNPCDefinition(
        id=1,
        name="Ezekiel Whateley",
        npc_type="shopkeeper",
        room_id=room_id,
        description=None,
        base_stats="{}",
        behavior_config='{"greeting_message": "Welcome, seeker of knowledge...", "farewell_message": "May the stars guide your path."}',
        ai_integration_stub="{}",
    )
    return ShopkeeperNPC(
        definition=definition, npc_id="npc-51", event_bus=event_bus, event_reaction_system=reaction_system
    )


def test_player_entered_room_triggers_the_npcs_own_greeting() -> None:
    event_bus = EventBus()
    reaction_system = NPCEventReactionSystem(event_bus)
    npc = _shopkeeper(event_bus, reaction_system, "room-1")

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        event_bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room-1"))

    schedule.assert_called_once()
    assert schedule.call_args.kwargs["npc_id"] == npc.npc_id
    assert schedule.call_args.kwargs["message"] == "Welcome, seeker of knowledge..."


def test_player_left_room_triggers_the_npcs_own_farewell() -> None:
    event_bus = EventBus()
    reaction_system = NPCEventReactionSystem(event_bus)
    _ = _shopkeeper(event_bus, reaction_system, "room-2")

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        event_bus.publish(PlayerLeftRoom(player_id=str(uuid.uuid4()), room_id="room-2"))

    schedule.assert_called_once()
    assert schedule.call_args.kwargs["message"] == "May the stars guide your path."


def test_greeting_does_not_fire_for_a_different_room() -> None:
    event_bus = EventBus()
    reaction_system = NPCEventReactionSystem(event_bus)
    _ = _shopkeeper(event_bus, reaction_system, "room-3")

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        event_bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="some-other-room"))

    schedule.assert_not_called()


def test_greeting_respects_the_per_npc_per_event_cooldown() -> None:
    """NPCEventReactionSystem enforces a 1s cooldown per (npc, event_type) -- a second entry event
    immediately after the first must not schedule a second greeting."""
    event_bus = EventBus()
    reaction_system = NPCEventReactionSystem(event_bus)
    _ = _shopkeeper(event_bus, reaction_system, "room-4")

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        event_bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room-4"))
        event_bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room-4"))

    schedule.assert_called_once()


def test_no_reactions_registered_without_a_reaction_system() -> None:
    """The pre-#815 shape must still work: event_reaction_system=None spawns a reaction-less NPC
    rather than failing."""
    event_bus = EventBus()
    definition = SimpleNPCDefinition(
        id=2,
        name="Silent Shopkeeper",
        npc_type="shopkeeper",
        room_id="room-5",
        description=None,
        base_stats="{}",
        behavior_config="{}",
        ai_integration_stub="{}",
    )
    npc = ShopkeeperNPC(definition=definition, npc_id="npc-52", event_bus=event_bus, event_reaction_system=None)
    assert npc.event_reaction_system is None

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        event_bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room-5"))

    schedule.assert_not_called()


if __name__ == "__main__":
    # ponytail: smallest runnable check that the whole revival chain actually fires.
    bus = EventBus()
    system = NPCEventReactionSystem(bus)
    shopkeeper = _shopkeeper(bus, system, "demo-room")
    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as demo_schedule:
        bus.publish(PlayerEnteredRoom(player_id="demo-player", room_id="demo-room"))
    demo_schedule.assert_called_once()
    assert demo_schedule.call_args.kwargs["message"] == "Welcome, seeker of knowledge..."
    print("reaction revival demo OK")
