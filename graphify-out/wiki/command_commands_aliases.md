# command commands aliases

> 9 nodes

## Key Concepts

- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **ABC** (2 connections)
- **Subscribe to a subject/topic with a message handler.          Args:** (1 connections) — `server/infrastructure/message_broker.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [game chat moderation](game_chat_moderation.md) (2 shared connections)
- [message handler factory](message_handler_factory.md) (2 shared connections)
- [infrastructure message broker](infrastructure_message_broker.md) (1 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 30 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*