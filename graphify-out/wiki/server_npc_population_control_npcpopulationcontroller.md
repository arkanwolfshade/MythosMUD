# server npc population control npcpopulationcontroller

> 154 nodes

## Key Concepts

- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **population_stats.py** (7 connections) — `server/npc/population_stats.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **mock_event_bus()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **population_controller()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_should_spawn_npc()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **.get_population_stats()** (3 connections) — `server/npc/spawning_service.py`
- **mock_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- *... and 129 more nodes in this community*

## Relationships

- [server app lifespan startup create](server_app_lifespan_startup_create.md) (7 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (7 shared connections)
- [server npc zone config loader](server_npc_zone_config_loader.md) (7 shared connections)
- [draft7validator](draft7validator.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (4 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (2 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 186 (83%)
- INFERRED: 39 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*