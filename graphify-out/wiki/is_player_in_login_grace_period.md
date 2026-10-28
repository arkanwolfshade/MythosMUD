# is_player_in_login_grace_period

> 157 nodes · cohesion 0.02

## Key Concepts

- **websocket_initial_state.py** (57 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (52 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **asyncio** (26 connections)
- **websocket_handler_connection.py** (24 connections) — `server/realtime/websocket_handler_connection.py`
- **get_container_async_persistence()** (21 connections) — `server/container/async_persistence_access.py`
- **send_initial_room_state()** (21 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (20 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (17 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_delirium_notification()** (11 connections) — `server/realtime/websocket_initial_state.py`
- **setup_initial_connection_state()** (10 connections) — `server/realtime/websocket_handler_connection.py`
- **get_event_handler_for_initial_state()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **send_occupants_snapshot_if_needed()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **cleanup_websocket_connection()** (8 connections) — `server/realtime/websocket_handler_connection.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **_resolve_stored_death_location()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **test_check_and_send_death_notification_location_display()** (7 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **UUID** (6 connections)
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **_get_lucidity_for_client()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeEventHandlerForInitialState** (6 connections) — `server/realtime/websocket_initial_state.py`
- *... and 132 more nodes in this community*

## Relationships

- [test_game.py](test_game.py.md) (19 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (9 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (9 shared connections)
- [.publish_with_pool](publish_with_pool.md) (8 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (7 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (5 shared connections)
- [test_party_service.py](test_party_service.py.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (3 shared connections)
- [BaseEvent](BaseEvent.md) (3 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)

## Source Files

- `server/container/async_persistence_access.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 372 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*