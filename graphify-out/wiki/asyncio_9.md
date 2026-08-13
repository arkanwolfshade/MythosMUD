# asyncio

> 25 nodes

## Key Concepts

- **asyncio** (37 connections)
- **test_get_adjacent_rooms_no_exits()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_target_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_room_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_with_cache_room_object()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_without_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_plane_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_sub_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_room_exists_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_room_exists_without_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() handles room with no exits.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() handles target room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_room_exists() uses cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_room_exists() falls back to persistence.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() handles Room object with get_players/get_npcs.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() falls back to persistence.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() returns False when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_exits() returns empty dict when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by plane and zone.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by sub_zone.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() uses cache when available.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() returns None when room not in cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (12 shared connections)
- [test_get_adjacent_rooms_null_exit](test_get_adjacent_rooms_null_exit.md) (1 shared connections)
- [test_get_adjacent_rooms_source_not_found](test_get_adjacent_rooms_source_not_found.md) (1 shared connections)
- [test_get_adjacent_rooms_success](test_get_adjacent_rooms_success.md) (1 shared connections)
- [test_get_local_chat_scope](test_get_local_chat_scope.md) (1 shared connections)
- [test_get_local_chat_scope_source_not_found](test_get_local_chat_scope_source_not_found.md) (1 shared connections)
- [test_get_room_exits_no_exits](test_get_room_exits_no_exits.md) (1 shared connections)
- [test_get_room_exits_success](test_get_room_exits_success.md) (1 shared connections)
- [test_get_room_info_not_found](test_get_room_info_not_found.md) (1 shared connections)
- [test_get_room_info_success](test_get_room_info_success.md) (1 shared connections)
- [test_get_room_occupants_cache_not_found](test_get_room_occupants_cache_not_found.md) (1 shared connections)
- [test_get_room_occupants_with_cache_dict](test_get_room_occupants_with_cache_dict.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*