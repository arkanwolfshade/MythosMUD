# load_player_guid_formatter_class

> 13 nodes

## Key Concepts

- **logging_file_categories.py** (11 connections) — `server/structured_logging/logging_file_categories.py`
- **load_player_guid_formatter_class()** (10 connections) — `server/structured_logging/logging_utilities.py`
- **create_handler_for_category()** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **create_formatter()** (8 connections) — `server/structured_logging/logging_file_categories.py`
- **Formatter** (1 connections)
- **_PlayerGuidFormatterType** (1 connections)
- **Path** (1 connections)
- **RotatingFileHandler** (1 connections)
- **Logger-name categories and per-category file handlers for enhanced logging. The…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Create formatter (with or without PlayerGuidFormatter).** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **# NOTE: When async logging is enabled, this filter is added to the QueueHandler,** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Create handler for a log category with graceful error handling. If handler…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Return PlayerGuidFormatter without a static import from caller modules. Import-…** (1 connections) — `server/structured_logging/logging_utilities.py`

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (8 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (4 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (3 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_categories.py`
- `server/structured_logging/logging_utilities.py`

## Audit Trail

- EXTRACTED: 31 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*