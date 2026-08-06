# config rationale config()

> 10 nodes

## Key Concepts

- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **test_canonical_room_id_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_reconcile_room_presence_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Room and subscription utility helpers for connection manager.  This module provi** (1 connections) — `server/realtime/connection_room_utils.py`
- **Ensure room_occupants only contains currently online players.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Unit tests for connection room utils.  Tests the connection_room_utils module fu** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test reconcile_room_presence_impl() calls room_manager.reconcile_room_presence()** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`

## Relationships

- [nats services service](nats_services_service.md) (14 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*