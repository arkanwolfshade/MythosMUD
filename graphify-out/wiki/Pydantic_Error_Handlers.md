# Pydantic Error Handlers

> 126 nodes · cohesion 0.03

## Key Concepts

- **error_types.py** (37 connections) — `server/error_types.py`
- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **JSONResponse** (30 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **websocket_handler_validation.py** (21 connections) — `server/realtime/websocket_handler_validation.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **.handle_exception()** (14 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_mythos_error()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_generic_exception()** (10 connections) — `server/error_handlers/standardized_responses.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TestStandardizedResponsesSecurity** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **ErrorResponseDetails** (9 connections) — `server/error_types.py`
- **handle_api_error()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._create_fallback_response()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_http_exception()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **._handle_pydantic_validation_error()** (7 connections) — `server/error_handlers/standardized_responses.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **_SampleModel** (7 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **TypedDict** (6 connections)
- *... and 101 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (67 shared connections)
- [API Type Guards](API_Type_Guards.md) (25 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (5 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (5 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (5 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (5 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (4 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (3 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 608 (95%)
- INFERRED: 29 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*