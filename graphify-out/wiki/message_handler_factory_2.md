# message handler factory

> 24 nodes

## Key Concepts

- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory_init()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_register_handler()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_not_found()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_success()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_unknown_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_no_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_supported_message_types()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_global_message_handler_factory()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **.get_supported_message_types()** (2 connections) — `server/realtime/message_handler_factory.py`
- **Factory for creating and managing message handlers.      This factory pattern el** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a list of supported message types.          Returns:             List of sup** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test MessageHandlerFactory.__init__() initializes with default handlers.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.register_handler() registers new handler.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns None when not found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() successfully handles message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() sends error for unknown type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() handles message with no type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_supported_message_types() returns list of types.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test global message_handler_factory instance exists.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (15 shared connections)
- [game chat moderation](game_chat_moderation.md) (2 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 61 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*