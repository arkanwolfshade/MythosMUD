"""An NPC that speaks first: its reaction to a player entering its room is to open a conversation."""

from __future__ import annotations

from ..events.event_bus import EventBus
from ..events.event_types import NPCOpensDialogue, PlayerEnteredRoom
from .event_reaction_system import NPCEventReaction


def build_dialogue_opening(npc_id: str, event_bus: EventBus) -> NPCEventReaction:
    """
    A reaction that raises NPCOpensDialogue for each player who enters the NPC's room.

    It replaces the NPC's greeting rather than joining it: the reaction system runs only the first
    reaction whose condition matches an event, and opening the conversation is the greeting.
    """

    def condition(event: PlayerEnteredRoom, npc_context: dict[str, object]) -> bool:
        return event.room_id == npc_context.get("current_room")

    def action(event: PlayerEnteredRoom, npc_context: dict[str, object]) -> bool:
        room_id = npc_context.get("current_room")
        if not room_id or room_id == "unknown":
            return False
        raw_name = npc_context.get("name")
        event_bus.publish(
            NPCOpensDialogue(
                npc_id=npc_id,
                npc_name=raw_name if isinstance(raw_name, str) else "Someone",
                room_id=str(room_id),
                player_id=event.player_id,
            )
        )
        return True

    return NPCEventReaction(event_type=PlayerEnteredRoom, condition=condition, action=action, priority=1)
