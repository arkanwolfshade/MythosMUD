# Test Connection Establishment

> 32 nodes

## Key Concepts

- **test_connection_establishment.py** (59 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_meta()** (12 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_failed_connection_success()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_cancels_leftover_rest()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (2 connections)
- **ConnectionMetadata** (1 connections)
- **Remove a single dead connection from tracking structures. Args: conn_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock. Args: dead_connection_ids: List of dead…** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure. Args: connection_id: The connection ID to clean…** (1 connections) — `server/realtime/connection_establishment.py`
- **Unit tests for connection establishment. Tests the connection_establishment…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() removes connection from tracking.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() handles connection not present.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 7 more nodes in this community*

## Relationships

- [Test Connection Establishment](Test_Connection_Establishment.md) (52 shared connections)
- [Connection Establishment](Connection_Establishment.md) (18 shared connections)
- [Test Connection Establishment Ws](Test_Connection_Establishment_Ws.md) (14 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 141 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*