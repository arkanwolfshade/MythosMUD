# ConnectionManager

> 160 nodes

## Key Concepts

- **ConnectionManager** (64 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_manager_methods.py** (51 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **UUID** (24 connections)
- **asyncio** (18 connections)
- **broadcast_to_room_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **force_disconnect_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_all_connections_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **convert_uuids_to_strings_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_error_statistics_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_npcs_batch_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_online_player_by_display_name_method()** (5 connections) — `server/realtime/connection_manager_methods.py`
- *... and 135 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (53 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (15 shared connections)
- [RateLimiter](RateLimiter.md) (5 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (1 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [is_websocket_open_impl](is_websocket_open_impl.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 326 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*