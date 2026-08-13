# lifecycle_periodic.py

> 34 nodes

## Key Concepts

- **lifecycle_periodic.py** (18 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (8 connections) — `server/config/npc_config.py`
- **check_optional_npc_spawns_impl()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **run_periodic_maintenance_impl()** (7 connections) — `server/npc/lifecycle_periodic.py`
- **cleanup_old_records_impl()** (6 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **npc_config.py** (4 connections) — `server/config/npc_config.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **NPC Configuration for MythosMUD. This module defines configuration settings for…** (1 connections) — `server/config/npc_config.py`
- **Configuration for NPC lifecycle maintenance. This class centralizes all timing…** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…** (1 connections) — `server/config/npc_config.py`
- **Check if NPC maintenance should run on this tick. Args: tick_count: Current…** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values. Returns: Dictionary containing…** (1 connections) — `server/config/npc_config.py`
- **Clean up old lifecycle records (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Perform periodic maintenance (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- *... and 9 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (10 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*