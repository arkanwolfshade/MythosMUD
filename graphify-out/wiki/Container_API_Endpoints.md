# Container API Endpoints

> 122 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **ErrorType** (47 connections) — `server/error_types.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **error_types.py** (37 connections) — `server/error_types.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (25 connections) — `server/error_handlers/pydantic_error_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_validation.py** (21 connections) — `server/realtime/websocket_handler_validation.py`
- **test_error_types.py** (21 connections) — `server/tests/unit/test_error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **._handle_logged_http_exception()** (11 connections) — `server/error_handlers/standardized_responses.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **ErrorResponseDetails** (9 connections) — `server/error_types.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **TypedDict** (6 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- *... and 97 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (58 shared connections)
- [Player Position Service](Player_Position_Service.md) (27 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (18 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (17 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (9 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (8 shared connections)
- [Database Helper Tests](Database_Helper_Tests.md) (8 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (7 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (7 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (4 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (4 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 646 (94%)
- INFERRED: 43 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*