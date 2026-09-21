# ConnectionManager

> 122 nodes

## Key Concepts

- **ConnectionManager** (64 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_manager_methods.py** (52 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **UUID** (24 connections)
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **update_player_room_cache_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **convert_uuids_to_strings_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_error_statistics_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_npcs_batch_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_player_by_display_name_method()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_pending_messages_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_websocket_connection_id_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_rate_limit_info_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **has_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **start_health_checks_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **validate_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- *... and 97 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (45 shared connections)
- [asyncio](asyncio.md) (31 shared connections)
- [delegate_game_state_provider](delegate_game_state_provider.md) (6 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (4 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 259 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*