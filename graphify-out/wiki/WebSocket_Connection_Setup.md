# WebSocket Connection Setup

> 109 nodes

## Key Concepts

- **test_connection_establishment.py** (46 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (22 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (21 connections) — `server/realtime/connection_establishment.py`
- **ConnectionMetadata** (14 connections) — `server/realtime/connection_models.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **UUID** (11 connections)
- **Any** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **connection_models.py** (6 connections) — `server/realtime/connection_models.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_all_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 84 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 395 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*