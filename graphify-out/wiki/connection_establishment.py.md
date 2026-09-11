# connection_establishment.py

> 44 nodes

## Key Concepts

- **connection_establishment.py** (41 connections) — `server/realtime/connection_establishment.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **test_connection_metadata_dataclass_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_equality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_inequality()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_init()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_connection_metadata_with_optional_fields()** (3 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Connection establishment management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 19 more nodes in this community*

## Relationships

- [_as_mgr](_as_mgr.md) (27 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (25 shared connections)
- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [MessageQueue](MessageQueue.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 161 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*