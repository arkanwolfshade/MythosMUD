# realtime message nats

> 4 nodes

## Key Concepts

- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server logg** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [message handler factory](message_handler_factory.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
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