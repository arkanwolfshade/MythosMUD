# game chat moderation

> 16 nodes

## Key Concepts

- **WebSocket** (8 connections)
- **Any** (8 connections)
- **.handle_message()** (7 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (6 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **Handle a specific message type.          Args:             websocket: The WebSoc** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle party_invite_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle client_error_report message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a WebSocket message using the appropriate handler.          Args:** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (3 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)
- [realtime message nats](realtime_message_nats.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*