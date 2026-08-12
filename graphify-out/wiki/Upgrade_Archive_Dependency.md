# Upgrade Archive Dependency

> 15 nodes

## Key Concepts

- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BoundLogger** (2 connections)
- **Exception** (1 connections)
- **Log an exception once, respecting exceptions that have already been logged.** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Unit tests for enhanced_logging_config helpers.  Covers log_exception_once ded** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for these** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is sup** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggedException uses mark_logged(); repeat call does not log again.** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 56 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*