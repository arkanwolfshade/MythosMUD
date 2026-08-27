# build_event

> 227 nodes

## Key Concepts

- **build_event()** (111 connections) — `server/realtime/envelope.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **broadcast_room_update()** (24 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (24 connections)
- **websocket_handler_connection.py** (19 connections) — `server/realtime/websocket_handler_connection.py`
- **clone_room_drops()** (17 connections) — `server/utils/room_renderer.py`
- **test_room_renderer_functions.py** (14 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **log_room_broadcast_result()** (12 connections) — `server/services/combat_messaging/base.py`
- **build_room_drop_summary()** (12 connections) — `server/utils/room_renderer.py`
- **combat_messaging/base.py** (12 connections) — `server/services/combat_messaging/base.py`
- **CombatBroadcastMixin** (11 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **PlayerBroadcastMixin** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (10 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **player_broadcasts.py** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **room_renderer.py** (10 connections) — `server/utils/room_renderer.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- *... and 202 more nodes in this community*

## Relationships

- [test_room_renderer.py](test_room_renderer.py.md) (20 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (11 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (7 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (6 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (5 shared connections)
- [EventHandler](EventHandler.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/utils/test_room_renderer_functions.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 568 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*