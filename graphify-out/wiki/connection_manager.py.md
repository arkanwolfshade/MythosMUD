# connection_manager.py

> 111 nodes

## Key Concepts

- **connection_manager.py** (124 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (52 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (32 connections)
- **canonical_room_id_impl()** (16 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **UUID** (12 connections)
- **unsubscribe_from_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **canonical_room_id_public_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **convert_room_players_uuids_to_names_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **convert_uuids_to_strings_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 86 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (38 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (36 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [RateLimiter](RateLimiter.md) (12 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (8 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (5 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (4 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 596 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*