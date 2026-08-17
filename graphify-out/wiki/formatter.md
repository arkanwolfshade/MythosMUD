# formatter

> 111 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_handlers.py** (29 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **create_aggregator_handler()** (22 connections) — `server/structured_logging/logging_handlers.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **WindowsSafeRotatingFileHandler** (17 connections) — `server/structured_logging/windows_safe_rotation.py`
- **SafeRotatingFileHandler** (15 connections) — `server/structured_logging/logging_handlers.py`
- **logging_handlers.py** (15 connections) — `server/structured_logging/logging_handlers.py`
- **WarningOnlyFilter** (12 connections) — `server/structured_logging/logging_handlers.py`
- **load_player_guid_formatter_class()** (11 connections) — `server/structured_logging/logging_utilities.py`
- **AsyncioConnLostWriteFilter** (9 connections) — `server/structured_logging/logging_handlers.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **windows_safe_rotation.py** (7 connections) — `server/structured_logging/windows_safe_rotation.py`
- **LoggerNameFilter** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (6 connections)
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_aggregator_handler_class_for_windows()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **_make_exec_for_aggregator()** (5 connections) — `server/structured_logging/logging_handlers.py`
- *... and 86 more nodes in this community*

## Relationships

- [server structured logging logging utilities](server_structured_logging_logging_utilities.md) (15 shared connections)
- [server structured logging windows safe](server_structured_logging_windows_safe.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server structured logging logging file](server_structured_logging_logging_file.md) (8 shared connections)
- [queuelistener](queuelistener.md) (7 shared connections)
- [server structured logging logging handlers](server_structured_logging_logging_handlers.md) (5 shared connections)
- [claude rules structlog](claude_rules_structlog.md) (4 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (2 shared connections)
- [eventdict](eventdict.md) (1 shared connections)
- [server app lifespan](server_app_lifespan.md) (1 shared connections)
- [scripts bandit](scripts_bandit.md) (1 shared connections)
- [logentry](logentry.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`
- `server/structured_logging/windows_safe_rotation.py`
- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 218 (87%)
- INFERRED: 34 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*