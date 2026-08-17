# server realtime connection room utils

> 28 nodes

## Key Concepts

- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **canonical_room_id_impl()** (12 connections) — `server/realtime/connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (5 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (5 connections) — `server/realtime/connection_room_utils.py`
- **test_canonical_room_id_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
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
- **Test canonical_room_id_impl() returns original room_id when room not found.** (2 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Resolve a room id to the canonical Room.id value. Args: room_id: The room ID to…** (1 connections) — `server/realtime/connection_room_utils.py`
- **Ensure room_occupants only contains currently online players.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Remove a player from all room subscriptions and occupant lists.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Unit tests for connection room utils. Tests the connection_room_utils module…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test reconcile_room_presence_impl() calls…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test prune_player_from_all_rooms_impl() calls…** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns None when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- *... and 3 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)

## Source Files

- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 45 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*