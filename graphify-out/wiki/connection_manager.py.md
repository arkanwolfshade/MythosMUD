# connection_manager.py

> 95 nodes

## Key Concepts

- **connection_manager.py** (124 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (52 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (32 connections)
- **connection_delegates.py** (21 connections) — `server/realtime/connection_delegates.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **UUID** (12 connections)
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
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
- **canonical_room_id_public_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **convert_room_players_uuids_to_names_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 70 more nodes in this community*

## Relationships

- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (28 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (26 shared connections)
- [UUID](UUID.md) (25 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [time.py](time.py.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (5 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (5 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (5 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (4 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (4 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 567 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*