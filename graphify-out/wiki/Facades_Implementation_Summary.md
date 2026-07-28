# Facades Implementation Summary

> 12 nodes · cohesion 0.18

## Key Concepts

- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **Check if this NPC is required to spawn.** (1 connections) — `server/models/npc.py`
- **Get active NPCs from the lifecycle manager (single source of truth).** (1 connections) — `server/npc/population_control.py`
- **Despawn an NPC instance.          This method updates population statistics wh** (1 connections) — `server/npc/population_control.py`
- **Get a summary of NPC populations across all zones.          Returns:** (1 connections) — `server/npc/population_control.py`
- **Return True if the NPC is inactive long enough and not required (eligible for cl** (1 connections) — `server/npc/population_control.py`
- **Clean up NPCs that have been inactive for too long.          Args:** (1 connections) — `server/npc/population_control.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [E 2 E Scenario Whisper](E_2_E_Scenario_Whisper.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (1 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 34 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*