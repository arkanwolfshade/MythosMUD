# npc combat services

> 9 nodes

## Key Concepts

- **NPCMaintenanceConfig** (9 connections) — `server/config/npc_config.py`
- **npc_config.py** (5 connections) — `server/config/npc_config.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **NPC Configuration for MythosMUD.  This module defines configuration settings for** (1 connections) — `server/config/npc_config.py`
- **Configuration for NPC lifecycle maintenance.      This class centralizes all tim** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type.          Args:             npc_ty** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values.          Returns:             Dic** (1 connections) — `server/config/npc_config.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (2 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*