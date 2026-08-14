# ConnectionManager

> 208 nodes

## Key Concepts

- **ConnectionManager** (267 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **is_websocket_open_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **convert_uuids_to_strings_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **get_active_connection_count_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_health_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_dual_connection_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_memory_alerts_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_memory_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_next_sequence_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_players_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_performance_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_session_connections_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **stop_health_checks_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- *... and 183 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (94 shared connections)
- [container_events.py](container_events.py.md) (29 shared connections)
- [connection_manager.py](connection_manager.py.md) (26 shared connections)
- [LootAllRequest](LootAllRequest.md) (10 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (9 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [event_handlers.py](event_handlers.py.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 514 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*