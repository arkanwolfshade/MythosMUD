# Subzone Schema Definition

> 30 nodes

## Key Concepts

- **test_message_handler_factory.py** (21 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **MessageHandlerFactory** (18 connections) — `server/realtime/message_handler_factory.py`
- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory_get_handler_found()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_game_command_alias()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_command_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_init()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_register_handler()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_handler_not_found()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_success()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_unknown_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_no_type()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_get_supported_message_types()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_global_message_handler_factory()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **.get_supported_message_types()** (2 connections) — `server/realtime/message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Factory for creating and managing message handlers.      This factory pattern el** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a list of supported message types.          Returns:             List of sup** (1 connections) — `server/realtime/message_handler_factory.py`
- **Unit tests for message handler factory.  Tests the message_handler_factory modul** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test CommandMessageHandler.handle() calls handle_command_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.__init__() initializes with default handlers.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.register_handler() registers new handler.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns handler when found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns None when not found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() successfully handles message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- *... and 5 more nodes in this community*

## Relationships

- [Database Error Handling](Database_Error_Handling.md) (13 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 94 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*