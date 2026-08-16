# NPCMaintenanceConfig

> 11 nodes

## Key Concepts

- **NPCMaintenanceConfig** (10 connections) — `server/config/npc_config.py`
- **npc_config.py** (5 connections) — `server/config/npc_config.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **NPC Configuration for MythosMUD. This module defines configuration settings for…** (1 connections) — `server/config/npc_config.py`
- **Configuration for NPC lifecycle maintenance. This class centralizes all timing…** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…** (1 connections) — `server/config/npc_config.py`
- **Check if NPC maintenance should run on this tick. Args: tick_count: Current…** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values. Returns: Dictionary containing…** (1 connections) — `server/config/npc_config.py`

## Relationships

- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*