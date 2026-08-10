# Memory Leak Audit

> 13 nodes

## Key Concepts

- **._handle_event()** (6 connections) — `server/npc/event_reaction_system.py`
- **Any** (5 connections)
- **.should_trigger()** (5 connections) — `server/npc/event_reaction_system.py`
- **.execute()** (5 connections) — `server/npc/event_reaction_system.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **._get_npc_context()** (4 connections) — `server/npc/event_reaction_system.py`
- **.get_npc_reaction_stats()** (3 connections) — `server/npc/event_reaction_system.py`
- **Initialize an NPC event reaction.          Args:             event_type: The typ** (1 connections) — `server/npc/event_reaction_system.py`
- **Check if this reaction should trigger for the given event.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- **Execute the reaction action.          Args:             event: The event that tr** (1 connections) — `server/npc/event_reaction_system.py`
- **Handle an incoming event and trigger appropriate NPC reactions.          Args:** (1 connections) — `server/npc/event_reaction_system.py`
- **Get context information for an NPC.          This method attempts to get actual** (1 connections) — `server/npc/event_reaction_system.py`
- **Get statistics about an NPC's reactions.          Args:             npc_id: The** (1 connections) — `server/npc/event_reaction_system.py`

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (6 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*