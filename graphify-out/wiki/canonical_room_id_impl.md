# canonical_room_id_impl

> 35 nodes

## Key Concepts

- **canonical_room_id_impl()** (16 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **canonical_room_id_public_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
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
- **Resolve a room id to the canonical Room.id value (public method).** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Ensure room_occupants only contains currently online players (compatibility…** (1 connections) — `server/realtime/connection_manager.py`
- **Remove a player from all room subscriptions and occupant lists (compatibility…** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value. Args: room_id: The room ID to…** (1 connections) — `server/realtime/connection_room_utils.py`
- **Ensure room_occupants only contains currently online players.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Remove a player from all room subscriptions and occupant lists.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Unit tests for connection room utils. Tests the connection_room_utils module…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*