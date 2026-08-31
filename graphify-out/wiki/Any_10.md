# Any

> 23 nodes

## Key Concepts

- **Any** (8 connections)
- **WebSocket** (8 connections)
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **.handle_message()** (6 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **Return the live NPC combat integration service for delegation. Prefer…** (1 connections) — `server/npc/combat_integration_base.py`
- **Get a handler for the specified message type. Args: message_type: The message…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a WebSocket message using the appropriate handler. Args: websocket: The…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle a specific message type. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle command message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle chat message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle follow_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle party_invite_response message type.** (1 connections) — `server/realtime/message_handler_factory.py`
- **Handle client_error_report message type.** (1 connections) — `server/realtime/message_handler_factory.py`

## Relationships

- [message_handler_factory.py](message_handler_factory.py.md) (10 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*