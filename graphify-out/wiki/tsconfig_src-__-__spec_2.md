# tsconfig src/**/* spec

> 10 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **ClientErrorReportMessageHandler** (7 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **test_client_error_report_handler_logs()** (3 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for client_error_report messages (client-reported errors for server logg** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [command commands aliases](command_commands_aliases.md) (3 shared connections)
- [game chat moderation](game_chat_moderation.md) (3 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*