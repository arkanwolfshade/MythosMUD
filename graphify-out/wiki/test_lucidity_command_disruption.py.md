# test_lucidity_command_disruption.py

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
- **test_lookup_explored_stable_ids_calls_procedure_and_binds_uuid_list()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_room_service_init_with_cache()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_cache_not_found()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_player_in_room_with_cache_false()** (3 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_player_in_room() returns False when player not in room.** (2 connections) — `server/tests/unit/game/test_room_service.py`
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

- [get_room_environment](get_room_environment.md) (11 shared connections)
- [plane](plane.md) (3 shared connections)
- [zone](zone.md) (2 shared connections)
- [exits](exits.md) (2 shared connections)
- [Movement Message Dual Panel Routing](Movement_Message_Dual_Panel_Routing.md) (2 shared connections)
- [test_create_pickup_command](test_create_pickup_command.md) (1 shared connections)
- [test_create_ground_command](test_create_ground_command.md) (1 shared connections)
- [TestCheckRateLimit](TestCheckRateLimit.md) (1 shared connections)
- [test_save_player_with_bool_is_admin](test_save_player_with_bool_is_admin.md) (1 shared connections)
- [test_get_player_lucidity_tier_exception_in_processing](test_get_player_lucidity_tier_exception_in_processing.md) (1 shared connections)
- [test_get_players_batch_success](test_get_players_batch_success.md) (1 shared connections)
- [test_apply_dampening_and_send_message_exception](test_apply_dampening_and_send_message_exception.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*