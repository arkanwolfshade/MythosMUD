# Test Room Service

> 22 nodes

## Key Concepts

- **asyncio** (38 connections)
- **test_get_adjacent_rooms_null_exit()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_local_chat_scope()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_info_success()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_with_cache_dict()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_plane_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_sub_zone()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_lookup_explored_stable_ids_calls_procedure_and_binds_uuid_list()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_room_service_init_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by plane and zone.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_adjacent_rooms() skips null exits.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_local_chat_scope() returns current room and adjacent rooms.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() handles room dict.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() returns empty list when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_exits() returns exits dictionary.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_info() returns comprehensive room information.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test _lookup_explored_stable_ids() calls get_room_stable_ids_by_uuids with the…** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test RoomService initialization with cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room() returns None when room not in cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [Test Room Service](Test_Room_Service.md) (38 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*