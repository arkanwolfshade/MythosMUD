# ASGIApp

> 7 nodes

## Key Concepts

- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **test_add_correlation_id_missing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_correlation_id_existing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Add correlation ID to log entries if not already present.      This processor en** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test add_correlation_id() adds correlation_id when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_correlation_id() preserves existing correlation_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [QueueListener](QueueListener.md) (3 shared connections)
- [real time](real_time.md) (1 shared connections)
- [CommandRequest](CommandRequest.md) (1 shared connections)
- [enhance player ids()](enhance_player_ids%28%29.md) (1 shared connections)
- [alias storage()](alias_storage%28%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*