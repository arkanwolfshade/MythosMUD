# ConnectionManager

> 250 nodes · cohesion 0.01

## Key Concepts

- **ConnectionManager** (172 connections) — `server/realtime/connection_manager.py`
- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **AttributeError** (38 connections)
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

- [get_logger](get_logger.md) (70 shared connections)
- [UUID](UUID.md) (56 shared connections)
- [connection_manager.py](connection_manager.py.md) (29 shared connections)
- [CombatService](CombatService.md) (20 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (18 shared connections)
- [EventHandler](EventHandler.md) (9 shared connections)
- [cleanup_websocket_connection](cleanup_websocket_connection.md) (9 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (8 shared connections)
- [send_game_event](send_game_event.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (7 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)

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

- EXTRACTED: 1110 (92%)
- INFERRED: 98 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*