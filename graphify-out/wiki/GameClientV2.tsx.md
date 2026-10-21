# GameClientV2.tsx

> 99 nodes · cohesion 0.04

## Key Concepts

- **logging_file_setup.py** (37 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (24 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **setup_enhanced_file_logging()** (22 connections) — `server/structured_logging/logging_file_setup.py`
- **logging_file_categories.py** (16 connections) — `server/structured_logging/logging_file_categories.py`
- **_Handler** (15 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **add_handler_to_loggers()** (12 connections) — `server/structured_logging/logging_file_categories.py`
- **LoggerNameFilter** (11 connections) — `server/structured_logging/logging_file_categories.py`
- **_setup_aggregator_handlers()** (10 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (9 connections)
- **create_handler_for_category()** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (9 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **create_formatter()** (8 connections) — `server/structured_logging/logging_file_categories.py`
- **DropOldestQueueHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **test_async_log_queue_is_bounded()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_async_setup_applies_category_levels()** (8 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **apply_category_levels()** (7 connections) — `server/structured_logging/logging_file_categories.py`
- **get_queue_listener()** (7 connections) — `server/structured_logging/logging_file_setup.py`
- **Path** (7 connections)
- *... and 74 more nodes in this community*

## Relationships

- [test_status_commands.py](test_status_commands.py.md) (12 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (12 shared connections)
- [Room](Room.md) (9 shared connections)
- [CatalogPage.tsx](CatalogPage.tsx.md) (9 shared connections)
- [Documentation Updates - ConnectionManager Refactoring](Documentation_Updates_-_ConnectionManager_Refactoring.md) (9 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (2 shared connections)
- [format_occupant_display_name](format_occupant_display_name.md) (1 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (1 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (1 shared connections)
- [📊 METRICS AND SUCCESS CRITERIA](📊_METRICS_AND_SUCCESS_CRITERIA.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_categories.py`
- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*