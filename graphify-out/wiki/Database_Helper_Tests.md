# Database Helper Tests

> 97 nodes

## Key Concepts

- **WebSocketMessageValidator** (42 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (36 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (28 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **websocket_handler_validation.py** (21 connections) — `server/realtime/websocket_handler_validation.py`
- **message_validator.py** (9 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **test_websocket_handler_validation.py** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_validation.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_websocket_message()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **WebSocket** (4 connections)
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 72 more nodes in this community*

## Relationships

- [Combat Command Helpers](Combat_Command_Helpers.md) (8 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (4 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_handler_validation.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 344 (92%)
- INFERRED: 30 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*