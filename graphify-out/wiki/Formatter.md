# Formatter

> 55 nodes

## Key Concepts

- **logging_file_setup.py** (35 connections) — `server/structured_logging/logging_file_setup.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **SafeRotatingFileHandler** (20 connections) — `server/structured_logging/logging_handlers.py`
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

- [logging handlers](logging_handlers.md) (16 shared connections)
- [QueueListener](QueueListener.md) (9 shared connections)
- [Path](Path.md) (9 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [windows safe rotation](windows_safe_rotation.md) (5 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (3 shared connections)
- [logging utilities](logging_utilities.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [lifespan](lifespan.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/logging_utilities.py`

## Audit Trail

- EXTRACTED: 229 (93%)
- INFERRED: 16 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*