# scripts validate calendar

> 91 nodes

## Key Concepts

- **bundles/game.py** (44 connections) — `server/container/bundles/game.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **validate_calendar.py** (18 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [scripts validate calendar load and](scripts_validate_calendar_load_and.md) (34 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (18 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (9 shared connections)
- [server services schedule service databaseloadresult](server_services_schedule_service_databaseloadresult.md) (4 shared connections)
- [iteminstance](iteminstance.md) (3 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [holidayresolver](holidayresolver.md) (2 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [server caching cache service](server_caching_cache_service.md) (2 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (2 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/container/bundles/game.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 247 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*