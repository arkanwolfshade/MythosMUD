# Logging File Setup

> 56 nodes · cohesion 0.07

## Key Concepts

- **WindowsSafeRotatingFileHandler** (31 connections) — `server/structured_logging/windows_safe_rotation.py`
- **logging_file_setup.py** (30 connections) — `server/structured_logging/logging_file_setup.py`
- **SafeRotatingFileHandler** (25 connections) — `server/structured_logging/logging_handlers.py`
- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **Queue** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_aggregator_handlers()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **Handler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **RotatingFileHandler** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **LoggerNameFilter** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_category_handlers()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_console_handler()** (8 connections) — `server/structured_logging/logging_file_setup.py`
- **_CategoryHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_ConsoleHandlerConfig** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_setup_async_logging_queue()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **LogRecord** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **Path** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_add_handler_to_loggers()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_create_formatter()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_class()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_or_create_log_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **Formatter** (4 connections) — `server/structured_logging/logging_file_setup.py`
- **QueueListener** (4 connections) — `server/structured_logging/logging_file_setup.py`
- **_get_handler_classes()** (4 connections) — `server/structured_logging/logging_file_setup.py`
- *... and 31 more nodes in this community*

## Relationships

- [[Logging Rotating Handlers]] (16 shared connections)
- [[Windows Log Rotation]] (10 shared connections)
- [[Logging Path Utilities]] (9 shared connections)
- [[Logging Structured Setup]] (8 shared connections)
- [[Logging Structured Handlers]] (5 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Logging Structured Player]] (3 shared connections)
- [[Logging Migration Examples]] (1 shared connections)
- [[Monitoring Bundle Services]] (1 shared connections)
- [[Structured Logging Windows]] (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_handlers.py`
- `server/structured_logging/windows_safe_rotation.py`

## Audit Trail

- EXTRACTED: 236 (83%)
- INFERRED: 47 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
