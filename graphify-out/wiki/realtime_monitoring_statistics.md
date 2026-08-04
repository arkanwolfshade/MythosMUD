# realtime monitoring statistics

> 85 nodes

## Key Concepts

- **connection_manager.py** (161 connections) — `server/realtime/connection_manager.py`
- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **send_room_event()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **subscribe_to_room_events_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_events_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_memory_stats_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_dual_connection_stats_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_performance_stats_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_memory_alerts_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_error_statistics_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_active_connection_count_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_players_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_session_connections_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **stop_health_checks_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- *... and 60 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (48 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (27 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (9 shared connections)
- [services npc startup](services_npc_startup.md) (9 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [container service services](container_service_services.md) (7 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [connection realtime error](connection_realtime_error.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (6 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (5 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 436 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*