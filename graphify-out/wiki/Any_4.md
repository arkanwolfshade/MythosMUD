# Any

> 22 nodes

## Key Concepts

- **Any** (8 connections)
- **WebSocket** (8 connections)
- **.handle_message()** (6 connections) — `server/realtime/message_handler_factory.py`
- **_resolve_npc_combat_service_raw()** (5 connections) — `server/npc/combat_integration_base.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.get_handler()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (5 connections) — `server/realtime/message_handler_factory.py`
- **.handle()** (4 connections) — `server/realtime/message_handler_factory.py`
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

- [test_message_handler_factory.py](test_message_handler_factory.py.md) (10 shared connections)
- [send_game_event](send_game_event.md) (6 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/message_handler_factory.py`

## Audit Trail

- EXTRACTED: 73 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*