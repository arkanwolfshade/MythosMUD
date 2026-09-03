# Logging File Categories

> 28 nodes

## Key Concepts

- **logging_file_categories.py** (10 connections) — `server/structured_logging/logging_file_categories.py`
- **LoggerNameFilter** (9 connections) — `server/structured_logging/logging_file_categories.py`
- **create_handler_for_category()** (8 connections) — `server/structured_logging/logging_file_categories.py`
- **add_handler_to_loggers()** (6 connections) — `server/structured_logging/logging_file_categories.py`
- **create_formatter()** (6 connections) — `server/structured_logging/logging_file_categories.py`
- **test_logging_file_categories.py** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_file_categories.py`
- **test_realtime_module_loggers_match_communications_category()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **.__init__()** (2 connections) — `server/structured_logging/logging_file_categories.py`
- **test_infrastructure_category_removed()** (2 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **test_no_category_still_references_infrastructure_module()** (2 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- **Handler** (2 connections)
- **Formatter** (1 connections)
- **LogRecord** (1 connections)
- **RotatingFileHandler** (1 connections)
- **Path** (1 connections)
- **Logger-name categories and per-category file handlers for enhanced logging. The…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Create formatter (with or without PlayerGuidFormatter).** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Filter that only allows logs from loggers matching specified prefixes. This…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Initialize filter with allowed logger name prefixes. Args: allowed_prefixes:…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Check if the log record's logger name matches any allowed prefix. Args: record:…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Add handler to loggers that match the prefixes. Adds a filter to the handler to…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **# NOTE: When async logging is enabled, this filter is added to the QueueHandler,** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Create handler for a log category with graceful error handling. If handler…** (1 connections) — `server/structured_logging/logging_file_categories.py`
- **Unit tests for DEFAULT_LOG_CATEGORIES. Regression coverage for #687: the…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_categories.py`
- *... and 3 more nodes in this community*

## Relationships

- [Logging File Setup](Logging_File_Setup.md) (9 shared connections)
- [Test Logging Handlers](Test_Logging_Handlers.md) (1 shared connections)
- [Test Logging Utilities](Test_Logging_Utilities.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_categories.py`
- `server/tests/unit/structured_logging/test_logging_file_categories.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*