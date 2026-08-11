# E 2 E Di Migration

> 11 nodes

## Key Concepts

- **NPCMaintenanceConfig** (8 connections) — `server/config/npc_config.py`
- **npc_config.py** (4 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **NPC Configuration for MythosMUD.  This module defines configuration settings for** (1 connections) — `server/config/npc_config.py`
- **Configuration for NPC lifecycle maintenance.      This class centralizes all tim** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type.          Args:             npc_ty** (1 connections) — `server/config/npc_config.py`
- **Check if NPC maintenance should run on this tick.          Args:             tic** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values.          Returns:             Dic** (1 connections) — `server/config/npc_config.py`

## Relationships

- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (3 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*