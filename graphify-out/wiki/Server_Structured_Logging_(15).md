# Server Structured Logging (15)

> 9 nodes

## Key Concepts

- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **Path** (3 connections)
- **LogRecord** (2 connections)
- **Any** (1 connections)
- **Open the log file, ensuring directory exists first.          This overrides the** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Determine if rollover should occur, ensuring directory exists first.          Th** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Only allow WARNING level logs.** (1 connections) — `server/structured_logging/logging_handlers.py`

## Relationships

- [Server Structured Logging (5)](Server_Structured_Logging_%285%29.md) (2 shared connections)
- [Server Structured Logging](Server_Structured_Logging.md) (2 shared connections)
- [Server Structured Logging (6)](Server_Structured_Logging_%286%29.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*