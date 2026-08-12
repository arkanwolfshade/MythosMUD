# GameBundle

> 69 nodes

## Key Concepts

- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **ScheduleService** (27 connections) — `server/services/schedule_service.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **.__init__()** (4 connections) — `server/game/level_service.py`
- **._load_from_database()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._resolve_hourly_holidays()** (3 connections) — `server/container/bundles/game.py`
- *... and 44 more nodes in this community*

## Relationships

- [ScheduleEntry](ScheduleEntry.md) (14 shared connections)
- [bundles/game.py](bundles-game.py.md) (13 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_level_service.py](test_level_service.py.md) (5 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (4 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (2 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/level_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 248 (88%)
- INFERRED: 35 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*