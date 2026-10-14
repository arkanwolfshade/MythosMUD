# NPCPopulationController

> 145 nodes

## Key Concepts

- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCInstanceService** (25 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._create_npc_services()** (10 connections) — `server/container/bundles/npc.py`
- **Any** (10 connections)
- **.__init__()** (8 connections) — `server/npc/population_control.py`
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.move_npc_instance()** (6 connections) — `server/services/npc_instance_service.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **.spawn_npc_instance()** (5 connections) — `server/services/npc_instance_service.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- **._apply_npc_room_move()** (4 connections) — `server/services/npc_instance_service.py`
- **._check_npc_move_blocked_by_combat()** (4 connections) — `server/services/npc_instance_service.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_npc_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- *... and 120 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (39 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (11 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (9 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [ValueError](ValueError.md) (4 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (2 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 272 (89%)
- INFERRED: 32 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*