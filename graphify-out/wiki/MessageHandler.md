# MessageHandler

> 33 nodes

## Key Concepts

- **MessageHandler** (14 connections) — `server/realtime/message_handler_factory.py`
- **Any** (8 connections)
- **WebSocket** (8 connections)
- **.handle_message()** (6 connections) — `server/realtime/message_handler_factory.py`
- **FollowResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **PartyInviteResponseMessageHandler** (5 connections) — `server/realtime/message_handler_factory.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **.subscribe()** (3 connections) — `server/infrastructure/message_broker.py`
- **.register_handler()** (3 connections) — `server/realtime/message_handler_factory.py`
- **ABC** (2 connections)
- **Subscribe to a subject/topic with a message handler. Args: subject:…** (1 connections) — `server/infrastructure/message_broker.py`
- **Return the live NPC combat integration service for delegation. Prefer…** (1 connections) — `server/npc/combat_integration_base.py`
- **Register a new message handler. Args: message_type: The message type to handle…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Get a handler for the specified message type. Args: message_type: The message…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a WebSocket message using the appropriate handler. Args: websocket: The…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Abstract base class for message handlers.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a specific message type. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/message_handler_factory.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_message_handler_factory.py](test_message_handler_factory.py.md) (13 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [MessageBroker](MessageBroker.md) (1 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 110 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*