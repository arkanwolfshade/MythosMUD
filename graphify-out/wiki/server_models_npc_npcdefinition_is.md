# server models npc npcdefinition is

> 95 nodes

## Key Concepts

- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (11 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_PopulationLifecycleManager** (6 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **Any** (5 connections)
- **.is_required()** (4 connections) — `server/models/npc.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **.spawn_npc()** (3 connections) — `server/npc/population_control.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_has_definition_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_definition()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_record()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 70 more nodes in this community*

## Relationships

- [server app lifespan startup create](server_app_lifespan_startup_create.md) (13 shared connections)
- [server events event bus](server_events_event_bus.md) (11 shared connections)
- [draft7validator](draft7validator.md) (8 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server npc zone config loader](server_npc_zone_config_loader.md) (4 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (3 shared connections)
- [server npc init](server_npc_init.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (1 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (1 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 195 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*