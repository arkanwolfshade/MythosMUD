# Async Query Helpers

> 34 nodes

## Key Concepts

- **LoggedException** (23 connections) — `server/exceptions.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_inheritance()** (4 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **Exception** (2 connections)
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **Keyword arguments accepted by create_error_context and ErrorContext().** (2 connections) — `server/exceptions.py`
- **BoundLogger** (2 connections)
- **Marker base class indicating an exception has already produced a log entry.** (1 connections) — `server/exceptions.py`
- **Return True if this exception instance has already been logged.** (1 connections) — `server/exceptions.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Unit tests for enhanced_logging_config helpers.  Covers log_exception_once ded** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for these** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is sup** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- *... and 9 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (17 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (3 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 100 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*