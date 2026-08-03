# message handler factory

> 22 nodes

## Key Concepts

- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
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
- **Get a list of supported message types.          Returns:             List of sup** (1 connections) — `server/realtime/message_handler_factory.py`
- **Unit tests for message handler factory.  Tests the message_handler_factory modul** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.__init__() initializes with default handlers.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.register_handler() registers new handler.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns None when not found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() successfully handles message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() sends error for unknown type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() handles message with no type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_supported_message_types() returns list of types.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test global message_handler_factory instance exists.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [dead letter queue](dead_letter_queue.md) (6 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (2 shared connections)
- [game chat moderation](game_chat_moderation.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*