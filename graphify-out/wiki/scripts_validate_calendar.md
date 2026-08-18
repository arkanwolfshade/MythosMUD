# scripts validate calendar

> 79 nodes

## Key Concepts

- **bundles/game.py** (44 connections) — `server/container/bundles/game.py`
- **validate_calendar.py** (18 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **utils.py** (8 connections) — `server/container/utils.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- *... and 54 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (17 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (15 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (6 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (5 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (2 shared connections)
- [server services schedule service databaseloadresult](server_services_schedule_service_databaseloadresult.md) (1 shared connections)
- [server caching cache service professioncacheservice](server_caching_cache_service_professioncacheservice.md) (1 shared connections)
- [server caching cache service rationale](server_caching_cache_service_rationale.md) (1 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*