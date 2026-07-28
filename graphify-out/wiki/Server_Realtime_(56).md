# Server Realtime (56)

> 34 nodes

## Key Concepts

- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **.canonical_room_id()** (5 connections) — `server/realtime/connection_manager.py`
- **test_canonical_room_id_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **._reconcile_room_presence()** (3 connections) — `server/realtime/connection_manager.py`
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
- **Resolve a room id to the canonical Room.id value (public method).** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value (compatibility method).** (1 connections) — `server/realtime/connection_manager.py`
- **Ensure room_occupants only contains currently online players (compatibility meth** (1 connections) — `server/realtime/connection_manager.py`
- **Room and subscription utility helpers for connection manager.  This module provi** (1 connections) — `server/realtime/connection_room_utils.py`
- **Resolve a room id to the canonical Room.id value.      Args:         room_id: Th** (1 connections) — `server/realtime/connection_room_utils.py`
- *... and 9 more nodes in this community*

## Relationships

- [Server Realtime (7)](Server_Realtime_%287%29.md) (7 shared connections)
- [Server Persistence](Server_Persistence.md) (4 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 116 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*