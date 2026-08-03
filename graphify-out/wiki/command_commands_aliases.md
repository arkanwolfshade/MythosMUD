# command commands aliases

> 11 nodes

## Key Concepts

- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **ABC** (2 connections)
- **Subscribe to a subject/topic with a message handler.          Args:** (1 connections) — `server/infrastructure/message_broker.py`
- **Return the live NPC combat integration service for delegation.      Prefer ``C** (1 connections) — `server/npc/combat_integration_base.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Register a new message handler.          Args:             message_type: The mes** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type.          Args:             message** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (2 shared connections)
- [game chat moderation](game_chat_moderation.md) (2 shared connections)
- [message handler factory](message_handler_factory.md) (2 shared connections)
- [infrastructure message broker](infrastructure_message_broker.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [npc combat base](npc_combat_base.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [realtime message nats](realtime_message_nats.md) (1 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 34 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*