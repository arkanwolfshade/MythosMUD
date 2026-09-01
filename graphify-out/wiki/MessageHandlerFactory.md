# MessageHandlerFactory

> 22 nodes

## Key Concepts

- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory_game_command_alias()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_found()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **test_global_message_handler_factory()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_not_found()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_supported_message_types()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_init()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_register_handler()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **.get_supported_message_types()** (2 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler. Args: message_type: The message type to handle…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type. Args: message_type: The message…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a list of supported message types. Returns: List of supported message type…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Factory for creating and managing message handlers. This factory pattern…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test MessageHandlerFactory.get_supported_message_types() returns list of types.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory handles game_command as alias for command.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test global message_handler_factory instance exists.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.__init__() initializes with default handlers.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.register_handler() registers new handler.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns handler when found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns None when not found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [message_handler_factory.py](message_handler_factory.py.md) (17 shared connections)
- [Any](Any.md) (2 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 34 (83%)
- INFERRED: 7 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*