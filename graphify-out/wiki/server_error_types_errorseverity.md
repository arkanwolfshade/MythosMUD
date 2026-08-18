# server error types errorseverity

> 210 nodes

## Key Concepts

- **MythosMUDError** (66 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_legacy_error_handlers.py** (43 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (21 connections) — `server/exceptions.py`
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- **_get_status_code_for_error()** (19 connections) — `server/legacy_error_handlers.py`
- **_get_severity_for_error()** (18 connections) — `server/legacy_error_handlers.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **ConfigurationError** (17 connections) — `server/exceptions.py`
- **TestSanitization** (17 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **logged_http_exception_handler()** (17 connections) — `server/legacy_error_handlers.py`
- **GameLogicError** (16 connections) — `server/exceptions.py`
- **ErrorResponse** (16 connections) — `server/legacy_error_handlers.py`
- **sanitize_detail_value()** (16 connections) — `server/legacy_error_sanitization.py`
- **create_error_response()** (15 connections) — `server/legacy_error_handlers.py`
- **http_exception_handler()** (15 connections) — `server/legacy_error_handlers.py`
- **handle_exception()** (13 connections) — `server/exceptions.py`
- **general_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **mythos_exception_handler()** (12 connections) — `server/legacy_error_handlers.py`
- **register_error_handlers()** (11 connections) — `server/legacy_error_handlers.py`
- **sanitize_context()** (11 connections) — `server/legacy_error_sanitization.py`
- *... and 185 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (55 shared connections)
- [server exceptions authenticationerror init](server_exceptions_authenticationerror_init.md) (38 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (24 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (17 shared connections)
- [server tests unit test legacy](server_tests_unit_test_legacy.md) (16 shared connections)
- [server auth utils](server_auth_utils.md) (12 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (8 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (7 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (6 shared connections)
- [circuitbreakerresult](circuitbreakerresult.md) (6 shared connections)
- [server api players](server_api_players.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)

## Source Files

- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 513 (87%)
- INFERRED: 77 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*