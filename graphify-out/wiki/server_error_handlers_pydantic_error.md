# server error handlers pydantic error

> 312 nodes

## Key Concepts

- **MythosMUDError** (66 connections) — `server/exceptions.py`
- **RateLimitError** (49 connections) — `server/exceptions.py`
- **AuthenticationError** (46 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_exceptions.py** (44 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (43 connections) — `server/exceptions.py`
- **test_legacy_error_handlers.py** (43 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **create_error_context()** (35 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (21 connections) — `server/exceptions.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **_get_status_code_for_error()** (19 connections) — `server/legacy_error_handlers.py`
- **_get_severity_for_error()** (18 connections) — `server/legacy_error_handlers.py`
- **legacy_error_sanitization.py** (18 connections) — `server/legacy_error_sanitization.py`
- **ConfigurationError** (17 connections) — `server/exceptions.py`
- **TestSanitization** (17 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **logged_http_exception_handler()** (17 connections) — `server/legacy_error_handlers.py`
- **GameLogicError** (16 connections) — `server/exceptions.py`
- **ErrorResponse** (16 connections) — `server/legacy_error_handlers.py`
- **sanitize_detail_value()** (16 connections) — `server/legacy_error_sanitization.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **create_error_response()** (15 connections) — `server/legacy_error_handlers.py`
- *... and 287 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (69 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (37 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (23 shared connections)
- [server auth utils](server_auth_utils.md) (18 shared connections)
- [server tests unit test legacy](server_tests_unit_test_legacy.md) (17 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (16 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (15 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (12 shared connections)
- [passwordhasher](passwordhasher.md) (8 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (6 shared connections)
- [circuitbreakerresult](circuitbreakerresult.md) (6 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (6 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 674 (80%)
- INFERRED: 168 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*