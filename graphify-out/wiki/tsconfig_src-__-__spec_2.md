# tsconfig src/**/* spec

> 8 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **Handler for follow_response messages (accept/decline follow request).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle follow_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handler for party_invite_response messages (accept/decline party invite).** (1 connections) — `server/realtime/message_handler_factory.py`
- **Initialize the factory with registered handlers.** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [game chat moderation](game_chat_moderation.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [command commands aliases](command_commands_aliases.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)
- [realtime message nats](realtime_message_nats.md) (1 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*