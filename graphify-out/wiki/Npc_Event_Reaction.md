# Npc Event Reaction

> 26 nodes · cohesion 0.10

## Key Concepts

- **NPCEventReaction** (12 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **.execute()** (5 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (5 connections) — `server/npc/event_reaction_system.py`
- **Any** (5 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **BaseEvent** (4 connections) — `server/npc/event_reaction_system.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **.register_npc_reactions()** (3 connections) — `server/npc/event_reaction_system.py`
- **.npc_attacked_retaliation()** (3 connections) — `server/npc/event_reaction_system.py`
- **.player_entered_room_greeting()** (3 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (3 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (3 connections) — `server/npc/event_reaction_system.py`
- **Register reactions for a specific NPC.          Args:             npc_id: The ID** (1 connections) — `server/npc/event_reaction_system.py`
- **Handle an incoming event and trigger appropriate NPC reactions.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- **Get context information for an NPC.          This method attempts to get actual** (1 connections) — `server/npc/event_reaction_system.py`
- **Get statistics about an NPC's reactions.          Args:             npc_id: The** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that greets players when they enter the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that says farewell when players leave the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that makes an NPC retaliate when attacked.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that responds when players speak in the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Represents a reaction that an NPC can have to a specific event type.      This c** (1 connections) — `server/npc/event_reaction_system.py`
- **Initialize an NPC event reaction.          Args:             event_type: The typ** (1 connections) — `server/npc/event_reaction_system.py`
- **Check if this reaction should trigger for the given event.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (6 shared connections)
- [[Aggressive Mob NPC]] (5 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
