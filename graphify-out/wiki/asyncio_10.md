# asyncio

> 25 nodes

## Key Concepts

- **asyncio** (38 connections)
- **test_get_adjacent_rooms_no_exits()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_target_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_local_chat_scope_source_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_info_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_with_cache_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_without_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_persistence_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_lookup_explored_stable_ids_calls_procedure_and_binds_uuid_list()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_cache_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_with_cache_false()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() returns None when room not found in persistence.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() handles room with no exits.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() handles target room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_local_chat_scope() returns empty list when source room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() handles room dict.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() falls back to persistence.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() returns False when player not in room.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() handles room dict.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_info() returns comprehensive room information.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test _lookup_explored_stable_ids() calls get_room_stable_ids_by_uuids with the…** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() uses cache when available.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() returns None when room not in cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (12 shared connections)
- [test_get_adjacent_rooms_null_exit](test_get_adjacent_rooms_null_exit.md) (1 shared connections)
- [test_get_adjacent_rooms_source_not_found](test_get_adjacent_rooms_source_not_found.md) (1 shared connections)
- [test_get_adjacent_rooms_success](test_get_adjacent_rooms_success.md) (1 shared connections)
- [test_get_local_chat_scope](test_get_local_chat_scope.md) (1 shared connections)
- [test_get_room_exits_no_exits](test_get_room_exits_no_exits.md) (1 shared connections)
- [test_get_room_exits_room_not_found](test_get_room_exits_room_not_found.md) (1 shared connections)
- [test_get_room_exits_success](test_get_room_exits_success.md) (1 shared connections)
- [test_get_room_info_not_found](test_get_room_info_not_found.md) (1 shared connections)
- [test_get_room_occupants_cache_not_found](test_get_room_occupants_cache_not_found.md) (1 shared connections)
- [test_get_room_occupants_with_cache_room_object](test_get_room_occupants_with_cache_room_object.md) (1 shared connections)
- [test_get_room_persistence_returns_dict](test_get_room_persistence_returns_dict.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*