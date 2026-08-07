# Room Broadcast

> 209 nodes

## Key Concepts

- **ConnectionManager** (272 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (164 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (80 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (21 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_rate_limit_info_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_player_by_display_name_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_session_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **validate_session_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 184 more nodes in this community*

## Relationships

- [target resolution service](target_resolution_service.md) (49 shared connections)
- [player event handlers](player_event_handlers.md) (42 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (28 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (17 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (14 shared connections)
- [command player state](command_player_state.md) (13 shared connections)
- [container service services](container_service_services.md) (12 shared connections)
- [persistence container parse](persistence_container_parse.md) (12 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (10 shared connections)
- [nats services service](nats_services_service.md) (10 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (9 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (9 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 1089 (96%)
- INFERRED: 41 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*