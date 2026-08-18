# server app lifespan startup

> 230 nodes

## Key Concepts

- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **npc_startup_service.py** (21 connections) — `server/services/npc_startup_service.py`
- **bundles/npc.py** (15 connections) — `server/container/bundles/npc.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **_PopulationLifecycleManager** (7 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- *... and 205 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (49 shared connections)
- [jsondict](jsondict.md) (29 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (22 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (20 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (19 shared connections)
- [moduletype](moduletype.md) (10 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (10 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (8 shared connections)
- [server npc npc utils](server_npc_npc_utils.md) (8 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (8 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (7 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (6 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/zone_config_loader.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_startup_service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 548 (92%)
- INFERRED: 49 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*