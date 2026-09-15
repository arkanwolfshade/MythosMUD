# NPCPopulationController

> 146 nodes

## Key Concepts

- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._create_npc_services()** (10 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- *... and 121 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (27 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (16 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (9 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (5 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [FollowService](FollowService.md) (2 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 280 (91%)
- INFERRED: 28 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*