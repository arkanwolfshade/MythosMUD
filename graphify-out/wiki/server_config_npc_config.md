# server config npc config

> 62 nodes

## Key Concepts

- **test_lifecycle_periodic.py** (41 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **lifecycle_periodic.py** (19 connections) — `server/npc/lifecycle_periodic.py`
- **check_optional_npc_spawns_impl()** (13 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **cleanup_old_records_impl()** (10 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (9 connections) — `server/config/npc_config.py`
- **_attempt_optional_npc_spawn()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_spawn_room_for_definition()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **Any** (8 connections)
- **npc_config.py** (5 connections) — `server/config/npc_config.py`
- **_make_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_despawned()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_cleanup_old_records_removes_stale_error()** (4 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.cleanup_old_records()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.periodic_maintenance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_should_not_skip_when_interval_elapsed()** (3 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (2 connections) — `server/config/npc_config.py`
- **test_attempt_optional_npc_spawn_no_controller()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_no_zone_config()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **test_attempt_optional_npc_spawn_probability_miss()** (2 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- *... and 37 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (11 shared connections)
- [draft7validator](draft7validator.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 131 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*