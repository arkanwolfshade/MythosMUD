# combat models rationale

> 4 nodes

## Key Concepts

- **ChatMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **test_chat_message_handler_handle()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Handler for chat messages.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ChatMessageHandler.handle() calls handle_chat_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [message handler factory](message_handler_factory.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [command commands aliases](command_commands_aliases.md) (1 shared connections)
- [game chat moderation](game_chat_moderation.md) (1 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*