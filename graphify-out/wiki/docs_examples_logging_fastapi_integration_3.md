# docs examples logging fastapi integration

> 139 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **test_standardized_responses_security.py** (13 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **create_standardized_error_response()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- *... and 114 more nodes in this community*

## Relationships

- [server error types errorseverity](server_error_types_errorseverity.md) (44 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (27 shared connections)
- [server error types errormessages](server_error_types_errormessages.md) (20 shared connections)
- [server realtime websocket handler commands](server_realtime_websocket_handler_commands.md) (11 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (8 shared connections)
- [server realtime websocket handler handle](server_realtime_websocket_handler_handle.md) (8 shared connections)
- [server api players](server_api_players.md) (7 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (6 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (6 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (5 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (5 shared connections)
- [server realtime message handler factory](server_realtime_message_handler_factory.md) (4 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 419 (90%)
- INFERRED: 49 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*