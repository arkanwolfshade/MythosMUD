# nats services service

> 26 nodes

## Key Concepts

- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **.canonical_room_id()** (5 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **Any** (3 connections)
- **test_canonical_room_id_impl_none()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_empty_string()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_success_room_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_fallback_to_main_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_room_no_id_attribute()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_canonical_room_id_impl_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_prune_player_from_all_rooms_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Resolve a room id to the canonical Room.id value (public method).** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value (compatibility method).** (1 connections) — `server/realtime/connection_manager.py`
- **Remove a player from all room subscriptions and occupant lists (compatibility me** (1 connections) — `server/realtime/connection_manager.py`
- **Resolve a room id to the canonical Room.id value.      Args:         room_id: Th** (1 connections) — `server/realtime/connection_room_utils.py`
- **Remove a player from all room subscriptions and occupant lists.** (1 connections) — `server/realtime/connection_room_utils.py`
- **Test canonical_room_id_impl() returns None when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns empty string when room_id is empty.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() resolves room ID from room_manager persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() falls back to main persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns original room_id when room not found.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() returns original room_id when room has no id.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **Test canonical_room_id_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- *... and 1 more nodes in this community*

## Relationships

- [config rationale config()](config_rationale_config%28%29.md) (14 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 72 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*