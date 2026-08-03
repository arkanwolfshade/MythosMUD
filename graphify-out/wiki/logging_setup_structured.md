# logging setup structured

> 55 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (7 connections)
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **Handler** (6 connections)
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **LogRecord** (3 connections)
- **Path** (3 connections)
- **RotatingFileHandler** (3 connections)
- **_convert_max_size_to_bytes()** (3 connections) — `server/structured_logging/logging_file_setup.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 30 more nodes in this community*

## Relationships

- [logging handlers structured](logging_handlers_structured.md) (15 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (9 shared connections)
- [logging file setup](logging_file_setup.md) (9 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (4 shared connections)
- [logging utilities structured](logging_utilities_structured.md) (3 shared connections)
- [player guid formatter](player_guid_formatter.md) (3 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`

## Audit Trail

- EXTRACTED: 238 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*