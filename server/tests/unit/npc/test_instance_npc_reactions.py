"""
NPCs spawned into an instance react to the players there.

Instance NPC definitions have no room of their own; the room comes from the spawn. The reaction context used to keep
the definition's (empty) room, so an instanced NPC never greeted anyone, and one that speaks first never spoke. These
tests take the real spawn path: create_npc_instance -> NPCBase -> NPCEventReactionSystem -> EventBus.
"""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import patch

from server.events import EventBus
from server.events.event_types import NPCOpensDialogue, PlayerEnteredRoom
from server.models.npc import NPCDefinition
from server.npc.event_reaction_system import NPCEventReactionSystem
from server.npc.spawning_instance_factory import create_npc_instance
from server.npc.spawning_models import SimpleNPCDefinition

INSTANCE_ROOM = "instance_abc_earth_arkhamcity_first_exposure_room_old_yew_001"


def _instance_definition(behavior_config: str) -> NPCDefinition:
    """The spawn path accepts the lightweight definition too; it is coerced on the way in."""
    definition = SimpleNPCDefinition(
        id=7,
        name="Pale Ghoul",
        npc_type="passive_mob",
        room_id=None,  # instance NPCs are inert definitions: the room comes from the spawn
        description=None,
        base_stats='{"determination_points": 80, "max_dp": 80, "dexterity": 45}',
        behavior_config=behavior_config,
        ai_integration_stub="{}",
    )
    return cast(NPCDefinition, cast(object, definition))


def test_an_npc_spawned_into_an_instance_greets_players_who_enter_there() -> None:
    bus = EventBus()
    reactions = NPCEventReactionSystem(bus)
    npc = create_npc_instance(
        _instance_definition('{"greeting_message": "It watches you."}'),
        INSTANCE_ROOM,
        bus,
        None,
        npc_id="ghoul-1",
        event_reaction_system=reactions,
    )
    assert npc is not None

    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        bus.publish(PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id=INSTANCE_ROOM))

    schedule.assert_called_once()
    assert schedule.call_args.kwargs["room_id"] == INSTANCE_ROOM


def test_an_instanced_npc_that_speaks_first_asks_to_open_its_dialogue() -> None:
    bus = EventBus()
    reactions = NPCEventReactionSystem(bus)
    opened: list[NPCOpensDialogue] = []
    bus.subscribe(NPCOpensDialogue, opened.append, service_id="test")
    _ = create_npc_instance(
        _instance_definition('{"initiates_dialogue": true}'),
        INSTANCE_ROOM,
        bus,
        None,
        npc_id="ghoul-1",
        event_reaction_system=reactions,
    )
    player_id = str(uuid.uuid4())

    bus.publish(PlayerEnteredRoom(player_id=player_id, room_id=INSTANCE_ROOM))

    assert [(e.npc_id, e.room_id, e.player_id) for e in opened] == [("ghoul-1", INSTANCE_ROOM, player_id)]
