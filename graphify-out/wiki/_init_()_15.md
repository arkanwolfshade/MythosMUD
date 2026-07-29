# . init ()

> 103 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **WebSocketMessageValidator** (42 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (36 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (28 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **message_validator.py** (9 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **test_websocket_handler_validation.py** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_validation.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- *... and 78 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (18 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (8 shared connections)
- [websocket handler commands](websocket_handler_commands.md) (8 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (7 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [test websocket handler helpers extended](test_websocket_handler_helpers_extended.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [websocket handler connection](websocket_handler_connection.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_handler_validation.py`

## Audit Trail

- EXTRACTED: 450 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*