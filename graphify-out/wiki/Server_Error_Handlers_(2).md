# Server Error Handlers (2)

> 154 nodes

## Key Concepts

- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **error_types.py** (35 connections) — `server/error_types.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **create_websocket_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **PydanticErrorHandler** (23 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **ErrorResponseDetails** (9 connections) — `server/error_types.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **MythosValidationError** (8 connections)
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- *... and 129 more nodes in this community*

## Relationships

- [Server Error Handlers](Server_Error_Handlers.md) (51 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (10 shared connections)
- [Server Utils (3)](Server_Utils_%283%29.md) (9 shared connections)
- [Server Utils](Server_Utils.md) (5 shared connections)
- [Server Api](Server_Api.md) (5 shared connections)
- [Server Middleware (2)](Server_Middleware_%282%29.md) (5 shared connections)
- [Server Admin](Server_Admin.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (34)](Server_Realtime_%2834%29.md) (4 shared connections)
- [Server Realtime (17)](Server_Realtime_%2817%29.md) (4 shared connections)
- [Server Realtime (33)](Server_Realtime_%2833%29.md) (3 shared connections)
- [Server Schemas](Server_Schemas.md) (3 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 700 (96%)
- INFERRED: 27 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*