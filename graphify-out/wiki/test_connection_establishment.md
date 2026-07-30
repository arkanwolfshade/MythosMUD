# test connection establishment

> 97 nodes

## Key Concepts

- **test_connection_establishment.py** (47 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (24 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (23 connections) — `server/realtime/connection_establishment.py`
- **UUID** (12 connections)
- **Any** (12 connections)
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **_cancel_rest_countdown_if_active()** (6 connections) — `server/realtime/connection_establishment.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_all_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 72 more nodes in this community*

## Relationships

- [real time](real_time.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 363 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*