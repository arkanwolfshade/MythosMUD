# test_connection_room_utils.py

> 29 nodes

## Key Concepts

- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **test_canonical_room_id_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **._reconcile_room_presence()** (3 connections) — `server/realtime/connection_manager.py`
- **test_canonical_room_id_impl_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_empty_string()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_fallback_to_main_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_none()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_room_no_id_attribute()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_success_room_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_prune_player_from_all_rooms_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_reconcile_room_presence_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Any** (3 connections)
- **Ensure room_occupants only contains currently online players (compatibility…** (1 connections) — `server/realtime/connection_manager.py`
- **Ensure room_occupants only contains currently online players.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Remove a player from all room subscriptions and occupant lists.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Unit tests for connection room utils. Tests the connection_room_utils module…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test reconcile_room_presence_impl() calls…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test prune_player_from_all_rooms_impl() calls…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns None when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns empty string when room_id is empty.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- *... and 4 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*