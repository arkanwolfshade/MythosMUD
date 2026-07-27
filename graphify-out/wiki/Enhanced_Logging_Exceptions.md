# Enhanced Logging Exceptions

> 74 nodes · cohesion 0.03

## Key Concepts

- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **LoggedException** (21 connections) — `server/exceptions.py`
- **test_enhanced_logging_config.py** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **ErrorContextInitKwargs** (5 connections) — `server/exceptions.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_logged_http_exception_initialization()** (4 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_authentication_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_configuration_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_database_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_database_error_without_table()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_error_context_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_error_context_with_values()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_game_logic_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_already_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_exception_mark_logged()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_inheritance()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_logged_http_exception_with_logger_name()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_mythos_mud_error_initialization()** (3 connections) — `server/tests/unit/test_exceptions.py`
- *... and 49 more nodes in this community*

## Relationships

- [[Standardized Error Responses]] (35 shared connections)
- [[NPC Admin API]] (10 shared connections)
- [[Container Exception Handlers]] (6 shared connections)
- [[Player Death Service]] (3 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[Pydantic Error Handlers]] (1 shared connections)
- [[Combat Domain Events]] (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 223 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
