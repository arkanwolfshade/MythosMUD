# canonical room id impl()

> 27 nodes

## Key Concepts

- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **canonical_room_id_impl()** (13 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (5 connections) — `server/realtime/connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (5 connections) — `server/realtime/connection_room_utils.py`
- **test_canonical_room_id_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Any** (3 connections)
- **test_canonical_room_id_impl_none()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_empty_string()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_success_room_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_fallback_to_main_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_room_no_id_attribute()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_reconcile_room_presence_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_prune_player_from_all_rooms_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns original room_id when room not found.** (2 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles DatabaseError.** (2 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Resolve a room id to the canonical Room.id value.      Args:         room_id: Th** (1 connections) — `server/realtime/connection_room_utils.py`
- **Ensure room_occupants only contains currently online players.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Remove a player from all room subscriptions and occupant lists.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Unit tests for connection room utils.  Tests the connection_room_utils module fu** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns None when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns empty string when room_id is empty.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() resolves room ID from room_manager persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() falls back to main persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- *... and 2 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (7 shared connections)

## Source Files

- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 86 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*