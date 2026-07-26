# .despawn_npc

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

- [get_logger](get_logger.md) (7 shared connections)
- [extract_npc_metadata](extract_npc_metadata.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [extract_room_id_from_npc](extract_room_id_from_npc.md) (1 shared connections)
- [extract_definition_id_from_npc](extract_definition_id_from_npc.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 34 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*