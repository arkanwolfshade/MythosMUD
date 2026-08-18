# build_event

> 371 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **deque** (26 connections)
- **asyncio** (24 connections)
- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **message_broadcaster.py** (16 connections) — `server/realtime/messaging/message_broadcaster.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (13 connections)
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- *... and 346 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (75 shared connections)
- [RateLimiter](RateLimiter.md) (20 shared connections)
- [.state](state.md) (18 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (9 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (8 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (8 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (7 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/room_subscription_manager.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 927 (94%)
- INFERRED: 54 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*