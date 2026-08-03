# commands rest command

> 13 nodes

## Key Concepts

- **Any** (6 connections)
- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (5 connections) — `server/npc/event_reaction_system.py`
- **.execute()** (5 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **.set_npc_context()** (3 connections) — `server/npc/event_reaction_system.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **Check if this reaction should trigger for the given event.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- **Execute the reaction action.          Args:             event: The event that tr** (1 connections) — `server/npc/event_reaction_system.py`
- **Handle an incoming event and trigger appropriate NPC reactions.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- **Update stored NPC context used by reaction conditions (room, name, alive).** (1 connections) — `server/npc/event_reaction_system.py`
- **Get context information for an NPC.          Args:             npc_id: The ID of** (1 connections) — `server/npc/event_reaction_system.py`
- **Get statistics about an NPC's reactions.          Args:             npc_id: The** (1 connections) — `server/npc/event_reaction_system.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*