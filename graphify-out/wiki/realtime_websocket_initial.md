# realtime websocket initial

> 89 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (6 connections)
- **WebSocket** (5 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **_passthrough_room_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_prepare_room_data_with_occupants()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 64 more nodes in this community*

## Relationships

- [room websocket updates](room_websocket_updates.md) (11 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (11 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (8 shared connections)
- [world models rationale](world_models_rationale.md) (8 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [combat commands handler](combat_commands_handler.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [commands combat handler](commands_combat_handler.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [room models instance](room_models_instance.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 366 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*