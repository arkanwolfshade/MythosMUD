# server realtime connection establishment cleanup

> 69 nodes

## Key Concepts

- **test_connection_establishment.py** (59 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_as_mgr()** (44 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_make_manager()** (42 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_remove_dead_connection()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection_existing_player()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_with_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_FakeEstablishmentManager** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_cancels_leftover_rest()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_reconnect_during_grace_runs_enter_setup()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_no_player()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 44 more nodes in this community*

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (49 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (40 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 237 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*