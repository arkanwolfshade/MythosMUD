# Any

> 32 nodes

## Key Concepts

- **lifecycle_periodic.py** (18 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (8 connections) — `server/config/npc_config.py`
- **Any** (8 connections)
- **check_optional_npc_spawns_impl()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (7 connections) — `server/npc/lifecycle_periodic.py`
- **cleanup_old_records_impl()** (6 connections) — `server/npc/lifecycle_periodic.py`
- **_attempt_optional_npc_spawn()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (5 connections) — `server/npc/lifecycle_periodic.py`
- **npc_config.py** (4 connections) — `server/config/npc_config.py`
- **_should_skip_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (4 connections) — `server/npc/lifecycle_periodic.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **NPC Configuration for MythosMUD.  This module defines configuration settings for** (1 connections) — `server/config/npc_config.py`
- **Configuration for NPC lifecycle maintenance.      This class centralizes all tim** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type.          Args:             npc_ty** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values.          Returns:             Dic** (1 connections) — `server/config/npc_config.py`
- **Clean up old lifecycle records (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Perform periodic maintenance (delegates to lifecycle_periodic).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Periodic maintenance and optional NPC spawn checks for lifecycle.  Extracted fro** (1 connections) — `server/npc/lifecycle_periodic.py`
- **Clean up old lifecycle records. Returns number of records removed.** (1 connections) — `server/npc/lifecycle_periodic.py`
- *... and 7 more nodes in this community*

## Relationships

- [. repr ()](_repr_%28%29.md) (11 shared connections)
- [game tick processing](game_tick_processing.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 109 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*