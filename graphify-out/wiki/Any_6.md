# Any

> 15 nodes

## Key Concepts

- **Any** (6 connections)
- **.execute()** (4 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.should_trigger()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **._handle_event()** (4 connections) — `server/npc/event_reaction_system.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **.set_npc_context()** (3 connections) — `server/npc/event_reaction_system.py`
- **Handle an incoming event and trigger appropriate NPC reactions. Args: event:…** (1 connections) — `server/npc/event_reaction_system.py`
- **Update stored NPC context used by reaction conditions (room, name, alive).** (1 connections) — `server/npc/event_reaction_system.py`
- **Get context information for an NPC. Args: npc_id: The ID of the NPC Returns:…** (1 connections) — `server/npc/event_reaction_system.py`
- **Get statistics about an NPC's reactions. Args: npc_id: The ID of the NPC…** (1 connections) — `server/npc/event_reaction_system.py`
- **Initialize an NPC event reaction. Args: event_type: The type of event this…** (1 connections) — `server/npc/event_reaction_system.py`
- **Check if this reaction should trigger for the given event. Args: event: The…** (1 connections) — `server/npc/event_reaction_system.py`
- **Execute the reaction action. Args: event: The event that triggered the reaction…** (1 connections) — `server/npc/event_reaction_system.py`

## Relationships

- [EventBus](EventBus.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*