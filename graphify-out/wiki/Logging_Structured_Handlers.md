# Logging Structured Handlers

> 9 nodes · cohesion 0.22

## Key Concepts

- **._open()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **.shouldRollover()** (5 connections) — `server/structured_logging/logging_handlers.py`
- **Path** (4 connections) — `server/structured_logging/logging_handlers.py`
- **LogRecord** (3 connections) — `server/structured_logging/logging_handlers.py`
- **.filter()** (3 connections) — `server/structured_logging/logging_handlers.py`
- **Any** (2 connections) — `server/structured_logging/logging_handlers.py`
- **Only allow WARNING level logs.** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Open the log file, ensuring directory exists first.          This overrides the** (1 connections) — `server/structured_logging/logging_handlers.py`
- **Determine if rollover should occur, ensuring directory exists first.          Th** (1 connections) — `server/structured_logging/logging_handlers.py`

## Relationships

- [[Logging File Setup]] (5 shared connections)
- [[Logging Rotating Handlers]] (2 shared connections)
- [[Logging Path Utilities]] (2 shared connections)

## Source Files

- `server/structured_logging/logging_handlers.py`

## Audit Trail

- EXTRACTED: 22 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
