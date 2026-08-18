# GameBundle

> 99 nodes

## Key Concepts

- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **bundles/game.py** (44 connections) — `server/container/bundles/game.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- *... and 74 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (26 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (21 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [_schedule_entry_from_row](_schedule_entry_from_row.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (3 shared connections)
- [ExplorationService](ExplorationService.md) (3 shared connections)
- [InstanceManager](InstanceManager.md) (3 shared connections)
- [MovementService](MovementService.md) (3 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/utils.py`
- `server/services/schedule_service.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 266 (90%)
- INFERRED: 31 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*