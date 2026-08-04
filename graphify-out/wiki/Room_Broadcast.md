# Room Broadcast

> 176 nodes

## Key Concepts

- **ConnectionManager** (233 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **UUID** (21 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **get_rate_limit_info_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_session_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **validate_session_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **has_websocket_connection_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_websocket_connection_id_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 151 more nodes in this community*

## Relationships

- [connection realtime delegates](connection_realtime_delegates.md) (52 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (48 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (11 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (8 shared connections)
- [follow game service](follow_game_service.md) (8 shared connections)
- [combat services messaging](combat_services_messaging.md) (7 shared connections)
- [container service services](container_service_services.md) (6 shared connections)
- [game chat service](game_chat_service.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (5 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 744 (96%)
- INFERRED: 35 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*