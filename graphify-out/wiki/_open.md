# ._open

> 10 nodes

## Key Concepts

- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **LogRecord** (3 connections)
- **Path** (3 connections)
- **.filter()** (2 connections) — `server/structured_logging/logging_handlers.py`
- **Any** (1 connections)
- **Only allow WARNING level logs.** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Open the log file, ensuring directory exists first. This overrides the parent…** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Determine if rollover should occur, ensuring directory exists first. This…** (1 connections) — `server/structured_logging/logging_handlers.py`

## Relationships

- [test_logging_handlers.py](test_logging_handlers.py.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*