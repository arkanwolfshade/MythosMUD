# Room Broadcast

> 219 nodes

## Key Concepts

- **ConnectionManager** (233 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **UUID** (21 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
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
- **check_all_connections_health_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 194 more nodes in this community*

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (56 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (47 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (10 shared connections)
- [follow game service](follow_game_service.md) (10 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (9 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (7 shared connections)
- [profession models rationale](profession_models_rationale.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [container service services](container_service_services.md) (6 shared connections)
- [persistence container parse](persistence_container_parse.md) (6 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (5 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 863 (96%)
- INFERRED: 34 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*