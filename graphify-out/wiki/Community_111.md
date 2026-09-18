# Community 111

> 92 nodes

## Key Concepts

- **ErrorType** (52 connections) — `server/error_types.py`
- **error_types.py** (36 connections) — `server/error_types.py`
- **ErrorMessages** (32 connections) — `server/error_types.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (30 connections) — `server/error_types.py`
- **pydantic_error_handler.py** (24 connections) — `server/error_handlers/pydantic_error_handler.py`
- **create_standard_error_response()** (22 connections) — `server/error_types.py`
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **test_error_types.py** (18 connections) — `server/tests/unit/test_error_types.py`
- **ErrorSeverity** (10 connections) — `server/error_types.py`
- **test_standardized_responses_security.py** (10 connections) — `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- **test_websocket_handler_error_handling.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **ErrorResponseDetails** (6 connections) — `server/error_types.py`
- **_normalize_error_response_details()** (6 connections) — `server/error_types.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **TypedDict** (6 connections)
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **test_send_error_response_disconnected()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- **test_send_error_response_websocket_disconnect()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_create_standard_error_response_with_severity()** (5 connections) — `server/tests/unit/test_error_types.py`
- **HttpStandardErrorResponse** (4 connections) — `server/error_types.py`
- **RealtimeErrorResponse** (4 connections) — `server/error_types.py`
- *... and 67 more nodes in this community*

## Relationships

- [Community 147](Community_147.md) (29 shared connections)
- [Community 369](Community_369.md) (17 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (16 shared connections)
- [Community 272](Community_272.md) (15 shared connections)
- [Community 336](Community_336.md) (14 shared connections)
- [Realtime Message Handlers](Realtime_Message_Handlers.md) (9 shared connections)
- [Community 243](Community_243.md) (8 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (7 shared connections)
- [Community 306](Community_306.md) (6 shared connections)
- [Community 31](Community_31.md) (5 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (5 shared connections)
- [Community 154](Community_154.md) (4 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`
- `server/tests/unit/realtime/test_websocket_handler_error_handling.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/test_error_types.py`

## Audit Trail

- EXTRACTED: 274 (86%)
- INFERRED: 43 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*