# logging handlers structured

> 137 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_handlers.py** (28 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **create_aggregator_handler()** (22 connections) — `server/structured_logging/logging_handlers.py`
- **WindowsSafeRotatingFileHandler** (21 connections) — `server/structured_logging/windows_safe_rotation.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **SafeRotatingFileHandler** (20 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (17 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (13 connections) — `server/structured_logging/logging_handlers.py`
- **AsyncioConnLostWriteFilter** (11 connections) — `server/structured_logging/logging_handlers.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (7 connections)
- **windows_safe_rotation.py** (7 connections) — `server/structured_logging/windows_safe_rotation.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 112 more nodes in this community*

## Relationships

- [logging structured utilities](logging_structured_utilities.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (11 shared connections)
- [services admin auth](services_admin_auth.md) (9 shared connections)
- [player guid formatter](player_guid_formatter.md) (4 shared connections)
- [follow game service](follow_game_service.md) (4 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/structured_logging/windows_safe_rotation.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 504 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*