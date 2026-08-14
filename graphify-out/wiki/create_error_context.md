# create_error_context

> 81 nodes

## Key Concepts

- **create_error_context()** (35 connections) — `server/exceptions.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.test_sanitize_context_empty()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_sanitize_context_with_safe_fields()** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_log_and_raise_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- *... and 56 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (43 shared connections)
- [MythosMUDError](MythosMUDError.md) (11 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (10 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (6 shared connections)
- [ErrorType](ErrorType.md) (5 shared connections)
- [log_with_context](log_with_context.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [create_error_context](create_error_context.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 196 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*