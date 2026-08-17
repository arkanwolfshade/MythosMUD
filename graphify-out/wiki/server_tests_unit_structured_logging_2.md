# server tests unit structured logging

> 5 nodes

## Key Concepts

- **temp_log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **temp_log_file()** (3 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **fixture** (2 connections)
- **Create a temporary directory for log files.** (1 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`
- **Create a temporary log file path.** (1 connections) — `server/tests/unit/structured_logging/test_logging_handlers.py`

## Relationships

- [formatter](formatter.md) (2 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_logging_handlers.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*