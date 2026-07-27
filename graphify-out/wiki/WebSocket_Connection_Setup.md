# WebSocket Connection Setup

> 93 nodes · cohesion 0.04

## Key Concepts

- **test_connection_establishment.py** (45 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (20 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (20 connections) — `server/realtime/connection_establishment.py`
- **Any** (12 connections) — `server/realtime/connection_establishment.py`
- **UUID** (12 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_all_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 68 more nodes in this community*

## Relationships

- [[NPC Admin API]] (6 shared connections)
- [[Realtime Connection]] (6 shared connections)
- [[Room Occupant Events]] (3 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 342 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
