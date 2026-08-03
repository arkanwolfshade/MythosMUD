# Room Broadcast

> 319 nodes

## Key Concepts

- **ConnectionManager** (221 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (160 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (79 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (41 connections)
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **UUID** (21 connections)
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_presence_statistics_impl()** (8 connections) — `server/realtime/connection_statistics.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- *... and 294 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (42 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (30 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (21 shared connections)
- [container service services](container_service_services.md) (13 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (13 shared connections)
- [connection realtime error](connection_realtime_error.md) (11 shared connections)
- [room connection realtime](room_connection_realtime.md) (10 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (9 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (9 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (8 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (8 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 1399 (98%)
- INFERRED: 35 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*