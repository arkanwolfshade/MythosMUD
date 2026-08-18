# server monitoring exception metrics

> 74 nodes

## Key Concepts

- **enhanced_error_logging.py** (39 connections) — `server/utils/enhanced_error_logging.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
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
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- **Any** (5 connections)
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **test_wrap_third_party_exception_enhanced()** (3 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context_with_metadata()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- *... and 49 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (21 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (7 shared connections)
- [server error types errorseverity](server_error_types_errorseverity.md) (7 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (6 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (5 shared connections)
- [claude rules structlog](claude_rules_structlog.md) (5 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (5 shared connections)
- [server exceptions authenticationerror init](server_exceptions_authenticationerror_init.md) (4 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (3 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 193 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*