# ._get_active_npcs_from_lifecycle_manager

> 10 nodes

## Key Concepts

- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **Check if this NPC is required to spawn.** (1 connections) — `server/models/npc.py`
- **Get active NPCs from the lifecycle manager (single source of truth). Returns:…** (1 connections) — `server/npc/population_control.py`
- **Get a summary of NPC populations across all zones. Returns: Dictionary…** (1 connections) — `server/npc/population_control.py`
- **Return True if the NPC is inactive long enough and not required (eligible for…** (1 connections) — `server/npc/population_control.py`
- **Clean up NPCs that have been inactive for too long. Args: max_age_seconds:…** (1 connections) — `server/npc/population_control.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (3 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 17 (89%)
- INFERRED: 2 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*