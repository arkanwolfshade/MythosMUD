# Room Service Tests

> 98 nodes · cohesion 0.02

## Key Concepts

- **test_room_service.py** (55 connections) — `server/tests/unit/game/test_room_service.py`
- **room_service_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **mock_room_cache()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() returns False when player not in room.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by plane and zone.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test describe_lighting() returns description for day.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Test search_rooms_by_name() returns empty list for short search term.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **sample_room_dict()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_describe_lighting_day()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_describe_lighting_night()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_describe_lighting_unknown_daypart()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_no_exits()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_null_exit()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_source_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_success()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_adjacent_rooms_target_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_environment_state()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_local_chat_scope()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_local_chat_scope_source_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_by_name()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_cache_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_no_exits()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_room_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_exits_success()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- *... and 73 more nodes in this community*

## Relationships

- [[Maps API Endpoints]] (2 shared connections)
- [[Room Data Fixer]] (1 shared connections)
- [[Room Occupant Manager Tests]] (1 shared connections)
- [[Movement Service Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 207 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
