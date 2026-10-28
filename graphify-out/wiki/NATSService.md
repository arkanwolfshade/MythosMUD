# NATSService

> 160 nodes · cohesion 0.03

## Key Concepts

- **test_websocket_handler_core.py** (47 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_message_handlers.py** (35 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handler_factory.py** (32 connections) — `server/realtime/message_handler_factory.py`
- **asyncio** (28 connections)
- **message_handlers.py** (27 connections) — `server/realtime/message_handlers.py`
- **websocket_messages.py** (26 connections) — `server/schemas/realtime/websocket_messages.py`
- **schemas/realtime/__init__.py** (25 connections) — `server/schemas/realtime/__init__.py`
- **test_websocket_message_schema_registry.py** (23 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- **CommandMessage** (17 connections) — `server/schemas/realtime/websocket_messages.py`
- **ChatMessage** (16 connections) — `server/schemas/realtime/websocket_messages.py`
- **CommandData** (16 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_follow_response_message()** (15 connections) — `server/realtime/message_handlers.py`
- **asyncio** (15 connections)
- **FollowResponseMessage** (14 connections) — `server/schemas/realtime/websocket_messages.py`
- **PartyInviteResponseMessage** (14 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **ClientErrorReportMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **GameCommandMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **PingMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_command_message()** (12 connections) — `server/realtime/message_handlers.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **ChatData** (10 connections) — `server/schemas/realtime/websocket_messages.py`
- **_discriminator_values()** (10 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- **handle_ping_message()** (9 connections) — `server/realtime/message_handlers.py`
- *... and 135 more nodes in this community*

## Relationships

- [PlayerDPUpdated](PlayerDPUpdated.md) (36 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (13 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (12 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [Alias](Alias.md) (10 shared connections)
- [useAsciiMapState.ts](useAsciiMapState.ts.md) (10 shared connections)
- [Room](Room.md) (5 shared connections)
- [.publish_with_pool](publish_with_pool.md) (4 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (4 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (3 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/websocket_messages.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- `server/tests/unit/realtime/test_websocket_message_schema_registry.py`

## Audit Trail

- EXTRACTED: 409 (87%)
- INFERRED: 62 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*