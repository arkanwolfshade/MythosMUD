# Pydantic Error Handlers

> 175 nodes · cohesion 0.02

## Key Concepts

- **error_types.py** (37 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **PydanticErrorHandler** (33 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (24 connections) — `server/error_handlers/pydantic_error_handler.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **websocket_handler_validation.py** (20 connections) — `server/realtime/websocket_handler_validation.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **.handle_validation_error()** (14 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._handle_logged_http_exception()** (12 connections) — `server/error_handlers/standardized_responses.py`
- **.handle_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **__init__.py** (9 connections) — `server/error_handlers/__init__.py`
- **convert_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_pydantic_error()** (9 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._handle_http_exception()** (9 connections) — `server/error_handlers/standardized_responses.py`
- **JSONResponse** (9 connections) — `server/error_handlers/standardized_responses.py`
- **_ExtractedErrorInfo** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.convert_to_mythos_error()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **._create_fallback_error_response()** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **handle_api_error()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- *... and 150 more nodes in this community*

## Relationships

- [[Standardized Error Responses]] (47 shared connections)
- [[NPC Admin API]] (9 shared connections)
- [[WebSocket Message Validation]] (9 shared connections)
- [[Dependency Risk Analyzer]] (7 shared connections)
- [[Database Manager Tests]] (5 shared connections)
- [[WebSocket Message Validator]] (5 shared connections)
- [[Error Handling Middleware]] (4 shared connections)
- [[Help and WebSocket Core]] (4 shared connections)
- [[WebSocket Command Handler]] (4 shared connections)
- [[Room Occupant Events]] (3 shared connections)
- [[WebSocket Message Handlers]] (3 shared connections)
- [[Command Service Tests]] (2 shared connections)

## Source Files

- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 756 (94%)
- INFERRED: 47 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
