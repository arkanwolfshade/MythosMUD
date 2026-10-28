# start_grace_period

> 63 nodes · cohesion 0.06

## Key Concepts

- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **get_project_root()** (16 connections) — `server/utils/project_paths.py`
- **project_paths.py** (15 connections) — `server/utils/project_paths.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **test_integration_cleanup_helpers.py** (11 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **.__init__()** (8 connections) — `server/services/schedule_service.py`
- **_should_preserve_table_on_cleanup()** (8 connections) — `server/tests/fixtures/integration/__init__.py`
- **get_environment_data_dir()** (8 connections) — `server/utils/project_paths.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **test_does_not_preserve_mutable_player_tables()** (4 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_preserves_every_orm_table_that_seed_sql_populates()** (4 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- **test_preserves_every_reference_seed_table()** (4 connections) — `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- *... and 38 more nodes in this community*

## Relationships

- [OccupantFormatter](OccupantFormatter.md) (14 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (14 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (9 shared connections)
- [Room](Room.md) (9 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (8 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (4 shared connections)
- [test_party_service.py](test_party_service.py.md) (3 shared connections)
- [populate_npc_sample_data.py](populate_npc_sample_data.py.md) (3 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (3 shared connections)
- [MessageCategory](MessageCategory.md) (3 shared connections)
- [Delight Techniques](Delight_Techniques.md) (3 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/container/bundles/time.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/fixtures/test_integration_cleanup_helpers.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 193 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*