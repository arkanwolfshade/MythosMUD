# Connection Disconnection Cleanup

> 250 nodes · cohesion 0.01

## Key Concepts

- **ConnectionManager** (172 connections) — `server/realtime/connection_manager.py`
- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **AttributeError** (38 connections)
- **nats_message_handler.py** (33 connections) — `server/realtime/nats_message_handler.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- *... and 225 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (69 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (56 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (29 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (19 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (18 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (9 shared connections)
- [Async Room Cache Tests](Async_Room_Cache_Tests.md) (9 shared connections)
- [Realtime Payload Optimizer](Realtime_Payload_Optimizer.md) (8 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (7 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (7 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 1104 (92%)
- INFERRED: 98 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*