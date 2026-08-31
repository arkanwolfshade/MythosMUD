# test_message_handlers.py

> 53 nodes

## Key Concepts

- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handler_factory.py** (24 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (16 connections)
- **message_handlers.py** (15 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message_no_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_client_error_report_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_args()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_command()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_accept_success()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_invalid_request_id()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_no_container()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_accept()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_invalid()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- *... and 28 more nodes in this community*

## Relationships

- [MessageHandler](MessageHandler.md) (7 shared connections)
- [Any](Any.md) (6 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [ErrorType](ErrorType.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (1 shared connections)
- [CommandMessageHandler](CommandMessageHandler.md) (1 shared connections)
- [MessageHandlerFactory](MessageHandlerFactory.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 143 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*