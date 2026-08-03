# dead letter queue

> 8 nodes

## Key Concepts

- **CommandMessageHandler** (9 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory_get_handler_found()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_game_command_alias()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_command_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Handler for command messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test CommandMessageHandler.handle() calls handle_command_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.get_handler() returns handler when found.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory handles game_command as alias for command.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [message handler factory](message_handler_factory.md) (6 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [command commands aliases](command_commands_aliases.md) (1 shared connections)
- [game chat moderation](game_chat_moderation.md) (1 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 20 (83%)
- INFERRED: 4 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*