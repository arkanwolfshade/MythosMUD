# NPCEventReaction

> 29 nodes

## Key Concepts

- **NPCEventReaction** (12 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionTemplates** (8 connections) — `server/npc/event_reaction_system.py`
- **register_default_reactions_for_npc()** (8 connections) — `server/npc/npc_default_reactions.py`
- **Any** (5 connections)
- **.execute()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- **.npc_attacked_retaliation()** (4 connections) — `server/npc/event_reaction_system.py`
- **.player_entered_room_greeting()** (4 connections) — `server/npc/event_reaction_system.py`
- **.player_left_room_farewell()** (4 connections) — `server/npc/event_reaction_system.py`
- **.player_spoke_response()** (4 connections) — `server/npc/event_reaction_system.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **.register_npc_reactions()** (3 connections) — `server/npc/event_reaction_system.py`
- **Register reactions for a specific NPC. Args: npc_id: The ID of the NPC…** (1 connections) — `server/npc/event_reaction_system.py`
- **Handle an incoming event and trigger appropriate NPC reactions. Args: event:…** (1 connections) — `server/npc/event_reaction_system.py`
- **Get context information for an NPC. This method attempts to get actual NPC…** (1 connections) — `server/npc/event_reaction_system.py`
- **Get statistics about an NPC's reactions. Args: npc_id: The ID of the NPC…** (1 connections) — `server/npc/event_reaction_system.py`
- **Templates for common NPC event reactions.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that greets players when they enter the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that says farewell when players leave the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that makes an NPC retaliate when attacked.** (1 connections) — `server/npc/event_reaction_system.py`
- **Create a reaction that responds when players speak in the room.** (1 connections) — `server/npc/event_reaction_system.py`
- **Represents a reaction that an NPC can have to a specific event type. This class…** (1 connections) — `server/npc/event_reaction_system.py`
- *... and 4 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (7 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`
- `server/npc/npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*