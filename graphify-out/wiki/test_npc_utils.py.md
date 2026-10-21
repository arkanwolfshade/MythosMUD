# test_npc_utils.py

> 149 nodes · cohesion 0.04

## Key Concepts

- **test_connection_establishment.py** (57 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_as_mgr()** (44 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_make_manager()** (42 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (41 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_connection_establishment_ws.py** (23 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_meta()** (11 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- *... and 124 more nodes in this community*

## Relationships

- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (9 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (9 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`

## Audit Trail

- EXTRACTED: 442 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*