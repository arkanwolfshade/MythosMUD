# test_connection_establishment.py

> 77 nodes

## Key Concepts

- **test_connection_establishment.py** (59 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **connection_models.py** (13 connections) — `server/realtime/connection_models.py`
- **_meta()** (12 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_cleanup_failed_connection_success()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_failed_connection_none()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 52 more nodes in this community*

## Relationships

- [_as_mgr](_as_mgr.md) (66 shared connections)
- [_track_player_presence](_track_player_presence.md) (22 shared connections)
- [connection_manager.py](connection_manager.py.md) (22 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (10 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (6 shared connections)
- [_FakeEstablishmentManager](_FakeEstablishmentManager.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 276 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*