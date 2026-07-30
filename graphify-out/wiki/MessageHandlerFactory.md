# MessageHandlerFactory

> 32 nodes

## Key Concepts

- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_ping_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_init()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_register_handler()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_not_found()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_success()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_unknown_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_no_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_supported_message_types()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_global_message_handler_factory()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **.get_supported_message_types()** (2 connections) — `server/realtime/message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Factory for creating and managing message handlers.      This factory pattern el** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a list of supported message types.          Returns:             List of sup** (1 connections) — `server/realtime/message_handler_factory.py`
- **Unit tests for message handler factory.  Tests the message_handler_factory modul** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test ChatMessageHandler.handle() calls handle_chat_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test PingMessageHandler.handle() calls handle_ping_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.__init__() initializes with default handlers.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- *... and 7 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (9 shared connections)
- [Test handle player movement handles](Test_handle_player_movement_handles.md) (6 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (3 shared connections)
- [processing](processing.md) (3 shared connections)
- [PanelManager](PanelManager.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 99 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*