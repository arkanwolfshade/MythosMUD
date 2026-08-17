# server tests unit game test

> 21 nodes

## Key Concepts

- **asyncio** (37 connections)
- **test_get_adjacent_rooms_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_no_exits()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_info_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_with_cache_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_plane_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_sub_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_room_service_init()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_with_cache_false()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_room_exists_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() returns False when player not in room.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by plane and zone.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() returns adjacent rooms.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_room_exists() uses cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() handles room dict.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_exits() returns empty dict when room has no exits.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_info() returns None when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test RoomService initialization.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() uses cache when available.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [server tests unit game test](server_tests_unit_game_test.md) (37 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*