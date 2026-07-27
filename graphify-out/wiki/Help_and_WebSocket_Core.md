# Help and WebSocket Core

> 58 nodes · cohesion 0.04

## Key Concepts

- **test_websocket_handler_core.py** (40 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_help.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_get_general_help()** (3 connections) — `server/help/help_content.py`
- **__init__.py** (3 connections) — `server/help/__init__.py`
- **Test handle_websocket_message routes message.** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_aliases_dir()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_in_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_type_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_handle_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 33 more nodes in this community*

## Relationships

- [[WebSocket Command Handler]] (14 shared connections)
- [[Alias Expansion Logic]] (5 shared connections)
- [[Pydantic Error Handlers]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[WebSocket Handler Helpers]] (3 shared connections)
- [[WebSocket Message Validator]] (2 shared connections)
- [[Realtime Websocket Handler]] (2 shared connections)
- [[WebSocket Handler Tests]] (2 shared connections)
- [[WebSocket Message Validation]] (2 shared connections)
- [[Unified Command Handler]] (1 shared connections)
- [[Commands System Help]] (1 shared connections)
- [[Standardized Error Responses]] (1 shared connections)

## Source Files

- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 170 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
