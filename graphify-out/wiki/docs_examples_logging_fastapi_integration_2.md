# docs examples logging fastapi integration

> 190 nodes

## Key Concepts

- **ErrorType** (65 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (46 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (38 connections) — `server/error_types.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (31 connections) — `server/error_types.py`
- **test_standardized_responses.py** (30 connections) — `server/tests/unit/error_handlers/test_standardized_responses.py`
- **create_standard_error_response()** (26 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (26 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (22 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **JSONResponse** (20 connections) — `docs/examples/logging/fastapi_integration.py`
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- **create_sse_error_response()** (16 connections) — `server/error_types.py`
- **.handle_validation_error()** (13 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **.handle_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **handle_api_error()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **error_handlers/__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorContextInitKwargs** (8 connections) — `server/exceptions.py`
- **convert_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- *... and 165 more nodes in this community*

## Relationships

- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (54 shared connections)
- [server error types errormessages](server_error_types_errormessages.md) (20 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (13 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (12 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (8 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (6 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (5 shared connections)
- [server middleware error handling middleware](server_middleware_error_handling_middleware.md) (5 shared connections)
- [server container main get container](server_container_main_get_container.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `monitoring/webhook-receiver.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`
- `server/tests/unit/error_handlers/test_standardized_responses.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 491 (88%)
- INFERRED: 69 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*