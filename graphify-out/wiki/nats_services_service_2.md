# nats services service

> 38 nodes

## Key Concepts

- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **canonical_room_id_public_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
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
- **Resolve a room id to the canonical Room.id value (public method).** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value (compatibility method).** (1 connections) — `server/realtime/connection_manager.py`
- **Ensure room_occupants only contains currently online players (compatibility meth** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value (public method).** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Room and subscription utility helpers for connection manager.  This module provi** (1 connections) — `server/realtime/connection_room_utils.py`
- **Resolve a room id to the canonical Room.id value.      Args:         room_id: Th** (1 connections) — `server/realtime/connection_room_utils.py`
- *... and 13 more nodes in this community*

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 123 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*